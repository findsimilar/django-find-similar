test:
	python manage.py test

coverage:
	coverage run --source='.' manage.py test
	coverage html --omit=settings/asgi.py,settings/wsgi.py,manage.py,django_find_similar/management/*,django_find_similar/package.py,setup.py
	coverage report --omit=settings/asgi.py,settings/wsgi.py,manage.py,examples/django_find_similar/*,django_find_similar/package.py,setup.py --fail-under=100


yamllint:
	yamllint -d relaxed .

black:
	black .

build:
	python -m build

install:
	make build
	pip install dist/*.whl

uninstall:
	pip uninstall django-find-similar -y
	rm -rf dist
	rm -rf django-find-similar.egg-info

reinstall:
	make uninstall
	make install

pylint:
	pylint $(shell git ls-files '*.py')

lint:
	make yamllint
	make pylint

sphinx-help:
	make help -f Sphinxfile

package_docs:
	sphinx-apidoc -o docs/package django_find_similar/