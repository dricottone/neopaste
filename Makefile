python = python3

clean:
	rm -rf **/__pycache__ **/__mypycache__ **/*.pyc build dist neopaste.egg-info

test:
	$(python) -m py_compile neopaste/*.py

build:
	gap neopaste/cli.toml -o neopaste/cli.py
	$(python) setup.py sdist bdist_wheel

reinstall: uninstall install

install:
	pipx install .

uninstall:
	pipx uninstall neopaste

