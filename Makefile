clean:
	find . -name \*.py[cod] -delete
	find . -name __pycache__ -delete

install-dev:
	rez python -m pip install -e .

install:
	rez python -m pip install .

uninstall:
	rez python -m pip uninstall rez_run

test:
	python -m unittest discover
