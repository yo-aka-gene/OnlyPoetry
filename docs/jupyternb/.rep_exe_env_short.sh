#!/usr/bin/env bash
set -u

echo "=== Execution Start ==="
echo "Timestamp (UTC): $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
echo "Hostname:        $(hostname)"
echo "OS:              $(grep '^PRETTY_NAME=' /etc/os-release 2>/dev/null | cut -d= -f2- | tr -d '"')"
echo "======================="
