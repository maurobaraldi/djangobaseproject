.PHONY: clean lint test helm

clean:
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
	find . -name '*.orig' -exec rm -f {} \;
	find . -name '*~' -exec rm -f {} \;
	find . -depth -name '__pycache__' -exec rm -rf {} \;

lint:
	flake8 --exclude=.tox

tests: clean
	python manage.py test

run:
	python manage.py runserver

shell:
	python manage.py shell


