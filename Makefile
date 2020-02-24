PROJECT_ROOT := app
PROJECT := app



pipenv:
	pipenv shell

collectstatic:
	cd $(PROJECT_ROOT) && python manage.py collectstatic --clear --no-input

freeze: 
	pipenv run pip freeze > requirements.txt

deploy: freeze collectstatic
	gcloud app deploy --quiet
