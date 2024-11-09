install_dev:
	@echo "------------------- INSTALL DEV ENV ------------------- "
	rez python -m pip install -e .
	@echo "------------------------------------------------------- "

install:
	@echo "------------------- INSTALL --------------------------- "
	rez python -m pip install .
	@echo "------------------------------------------------------- "

uninstall:
	@echo "------------------- UNINSTALL --------------------------- "
	rez python -m pip uninstall rez_{{cookiecutter.extension_command}}
	@echo "------------------------------------------------------- "

clean:
	@echo "-------------------- CLEAN PACKAGE -------------------- "
	find . -name \*.pyc -delete
	find . -name __pycache__ -delete
	@echo "------------------------------------------------------- "

test:
	@echo "---------------------- RUN TESTS ---------------------- "
	python3 -m unittest discover tests
	@echo "------------------------------------------------------- "
