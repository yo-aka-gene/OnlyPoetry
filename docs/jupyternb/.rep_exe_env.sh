#!/usr/bin/env bash

set -u
export LC_ALL=C

emit() {
    printf "%-24s %s\n" "$1:" "$2"
}

echo "============================================================"
echo "Execution Environment"
echo "============================================================"

# ------------------------------------------------------------------
# Basic identity
# ------------------------------------------------------------------
emit "Timestamp (UTC)" "$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
emit "Hostname" "$(hostname)"
emit "FQDN" "$(hostname -f 2>/dev/null || hostname)"

if [[ -r /etc/os-release ]]; then
    OS_NAME=$(
        awk -F= '/^PRETTY_NAME=/ {
            gsub(/^"/, "", $2)
            gsub(/"$/, "", $2)
            print $2
        }' /etc/os-release
    )
else
    OS_NAME="$(uname -s)"
fi

emit "OS" "$OS_NAME"
emit "Kernel" "$(uname -r)"
emit "Architecture" "$(uname -m)"

# ------------------------------------------------------------------
# Hardware
# ------------------------------------------------------------------
if command -v lscpu >/dev/null 2>&1; then
    CPU_MODEL=$(
        lscpu |
        awk -F: '/^Model name:/ {
            sub(/^[[:space:]]+/, "", $2)
            print $2
            exit
        }'
    )
    SOCKETS=$(
        lscpu |
        awk -F: '/^Socket\(s\):/ {
            gsub(/[[:space:]]/, "", $2)
            print $2
            exit
        }'
    )
    CORES_PER_SOCKET=$(
        lscpu |
        awk -F: '/^Core\(s\) per socket:/ {
            gsub(/[[:space:]]/, "", $2)
            print $2
            exit
        }'
    )
    THREADS_PER_CORE=$(
        lscpu |
        awk -F: '/^Thread\(s\) per core:/ {
            gsub(/[[:space:]]/, "", $2)
            print $2
            exit
        }'
    )
    LOGICAL_CPUS=$(
        lscpu |
        awk -F: '/^CPU\(s\):/ {
            gsub(/[[:space:]]/, "", $2)
            print $2
            exit
        }'
    )

    emit "CPU model" "${CPU_MODEL:-unknown}"
    emit "CPU sockets" "${SOCKETS:-unknown}"
    emit "Cores / socket" "${CORES_PER_SOCKET:-unknown}"
    emit "Threads / core" "${THREADS_PER_CORE:-unknown}"
    emit "Logical CPUs" "${LOGICAL_CPUS:-unknown}"
fi

if [[ -r /proc/meminfo ]]; then
    MEM_GIB=$(
        awk '/^MemTotal:/ {
            printf "%.1f GiB", $2 / 1024 / 1024
        }' /proc/meminfo
    )
    emit "System memory" "$MEM_GIB"
fi

# Optional machine model; deliberately excludes serial numbers / UUIDs.
if [[ -r /sys/class/dmi/id/sys_vendor ]]; then
    emit "System vendor" "$(cat /sys/class/dmi/id/sys_vendor)"
fi

if [[ -r /sys/class/dmi/id/product_name ]]; then
    emit "System model" "$(cat /sys/class/dmi/id/product_name)"
fi

# ------------------------------------------------------------------
# GPU
# ------------------------------------------------------------------
if command -v nvidia-smi >/dev/null 2>&1; then
    GPU_INFO=$(
        nvidia-smi \
            --query-gpu=name,memory.total,driver_version \
            --format=csv,noheader 2>/dev/null |
        paste -sd '; ' -
    )

    if [[ -n "$GPU_INFO" ]]; then
        emit "GPU(s)" "$GPU_INFO"
    else
        emit "GPU(s)" "NVIDIA driver present; no visible GPU"
    fi
else
    emit "GPU(s)" "None / nvidia-smi unavailable"
fi

# ------------------------------------------------------------------
# HPC scheduler context, when available
# ------------------------------------------------------------------
[[ -n "${JOB_ID:-}" ]] &&
    emit "SGE job ID" "$JOB_ID"

[[ -n "${QUEUE:-}" ]] &&
    emit "SGE queue" "$QUEUE"

[[ -n "${SLURM_JOB_ID:-}" ]] &&
    emit "SLURM job ID" "$SLURM_JOB_ID"

[[ -n "${SLURM_JOB_NODELIST:-}" ]] &&
    emit "SLURM node(s)" "$SLURM_JOB_NODELIST"

echo "============================================================"
