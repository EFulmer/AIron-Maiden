SHELL := /bin/bash

format:
	black --line-length=79 --py36 --verbose tests/ scraper/ learner/ scripts/

style_check:
	flake8 --max-line-length=79 --count --statistics -vvv tests/ scraper/ learner/ scripts/

install_travis:
	pip install -r requirements.txt

install_conda:
	echo TBD

install_pyenv:
	echo TBD

test_dev:
	pytest --pdb --color=yes -vvv tests/

test:
	$(shell cat secrets | xargs) pytest --cov=scraper --cov=learner --cov-report=term -s -vvv tests/

notebook:
	jupyter-notebook --no-browser --notebook-dir=notebooks/
