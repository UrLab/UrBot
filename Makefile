all: prod

ve:
	python3 -m venv ve

prod: ve requirements/requirements.txt
	ve/bin/pip install -r requirements/requirements.txt

dev: ve prod requirements/requirements-dev.txt
	ve/bin/pip install -r requirements/requirements-dev.txt

requirements/requirements.txt: ve ve/bin/pip-compile requirements/requirements.in
	ve/bin/pip-compile requirements/requirements.in

requirements/requirements-dev.txt: ve ve/bin/pip-compile requirements/requirements-dev.in
	ve/bin/pip-compile requirements/requirements-dev.in

ve/bin/pip-compile:
	ve/bin/pip install pip-tools
