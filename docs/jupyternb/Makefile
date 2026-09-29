KERNEL_NAME := onlypoetry_py
ENV_SUFFIX := $(shell hostname -s | sed 's/[^A-Za-z0-9._-]/_/g')

TEMPLATES := $(wildcard *_TEMPLATE.ipynb)

.PHONY: execute check-templates

check-templates:
	@test -n "$(TEMPLATES)" || \
		(echo "ERROR: No *_TEMPLATE.ipynb files found."; exit 1)

execute: check-templates
	@echo "Execution environment: $(ENV_SUFFIX)"
	@echo "Kernel: $(KERNEL_NAME)"
	@echo
	@set -eu; \
	for template in $(TEMPLATES); do \
		name=$$(basename "$$template" _TEMPLATE.ipynb); \
		notebook="$${name}_$(ENV_SUFFIX).ipynb"; \
		echo "============================================================"; \
		echo "Template: $$template"; \
		echo "Output:   $$notebook"; \
		echo "============================================================"; \
		cp "$$template" "$$notebook"; \
		ENV_SUFFIX="$(ENV_SUFFIX)" poetry run jupyter nbconvert \
			--to notebook \
			--execute \
			--inplace \
			--ExecutePreprocessor.kernel_name=$(KERNEL_NAME) \
			--ExecutePreprocessor.timeout=-1 \
			"$$notebook"; \
		echo; \
	done
