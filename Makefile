VERSION=1.0.3
SRC=$(shell find . -type f -name '*.py')

clean:
	rm -rf **/__pycache__ **/__mypycache__ **/*.pyc dist build *.egg-info

neopaste/cli.py: neopaste/cli.toml
	gap neopaste/cli.toml -o neopaste/cli.py

test:
	python -m py_compile neopaste/*.py

PYBUILD_FILES=pyproject.toml LICENSE.md README.md

dist/neopaste-$(VERSION)-py3-none-any.whl: $(SRC) neopaste/cli.py $(PYBUILD_FILES)
	mkdir -p dist
	pyproject-build --wheel --no-isolation

build: dist/neopaste-$(VERSION)-py3-none-any.whl

install: dist/neopaste-$(VERSION)-py3-none-any.whl
	pipx install build/neopaste-$(VERSION)-py3-none-any.whl

uninstall:
	pipx uninstall neopaste

.PHONY: clean test build install uninstall
