BASALCELL_DEMO_REF ?= main
RAW_BASE := https://raw.githubusercontent.com/yo-aka-gene/BasalCellDemo/$(BASALCELL_DEMO_REF)

KERNEL_NAME := onlypoetry_py

.PHONY: init sync-spec docs

sync-spec:
	curl -fsSL $(RAW_BASE)/pyproject.toml -o pyproject.toml
	curl -fsSL $(RAW_BASE)/poetry.lock -o poetry.lock
	sed -i '0,/^name = "basalcelldemo"$$/s//name = "onlypoetry"/' pyproject.toml

init: sync-spec
	poetry install
	poetry run python -m ipykernel install --user --name $(KERNEL_NAME) --display-name "OnlyPoetry (Python)"

docs:
	@echo "Building Sphinx HTML documentation..."
	@poetry export --with dev --without-hashes --format=requirements.txt > docs/requirements.txt
	@poetry run sphinx-apidoc -f -o docs/auxiliary_api basalcelldemo_tools/
	@poetry run sphinx-build -a -E -b html docs docs/_build/html
	@echo "Opening documentation in browser..."
	@poetry run python -c \
		"import webbrowser, os; webbrowser.open('file://' + os.path.realpath('docs/_build/html/index.html'))"
