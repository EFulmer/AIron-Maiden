format:
	echo TBD

style_check:
	echo TBD

install_travis:
	pip install -r requirements.txt

install_conda:
	echo TBD

install_pyenv:
	echo TBD

test_dev:
	pytest --pdb --color=yes -vvv tests/

test:
	pytest --cov=scraper --cov=learner --cov-report=term -vvv tests/
