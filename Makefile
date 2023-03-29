.PHONY: integration_tests lint unit_tests

install:
	@echo pip install
	pip install -r requirements.txt

install_dev:
	@echo pip install dev
	pip install -r dev-requirements.txt

unit_tests:
	@echo unit test...
	python -m pytest ./tests/src

package_test:
	./package_test/run.sh

integration_tests:
	@echo integration tests...
	python -m pytest --cov ./pinterest/ --cov-branch ./integration_tests/ --cov-report term-missing

clean: clean-build clean-pyc ## Clean

clean-build:				## Clean python build
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info
	rm -fr .tox

clean-pyc:					## Clean python binaries
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

build: 						## Build command
	python -m build
	ls -l dist

build_test: 				## Build test command
	IS_TEST_BUILD=1 python -m build
	ls -l dist

pip_release_install:
	pip install twine build

publish_pypi_test: clean pip_release_install build_test
	twine upload -r testpypi dist/*

publish_pypi: clean pip_release_install build
	twine upload -r pypi dist/*

pylint:
	@echo lint
	pylint .

flake:
	flake8 . --count --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

lint: pylint flake
