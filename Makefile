build:
	python -m build
	ls -l dist

pip_release_install:
	pip install twine build

publish_pypi_test: pip_release_install build
	twine upload -r testpypi dist/*

publish_pypi: pip_release_install build
	twine upload -r pypi dist/*