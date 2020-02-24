PROJECT_ROOT := app
PROJECT := app
GCLOUD_PROJECT := smart-sheets-backend
DB_CONNECTION_NAME := smart-sheets-backend:europe-west3:postgres1
PROXY_PORT := 5433
GC_PROXY = cloud_sql_proxy
GC_PROXY_URL = https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64
GC_LOCAL_ENV = DJANGO_CONFIGURATION=Local DJANGO_DATABASE_PORT=$(PROXY_PORT)


pipenv:
	pipenv shell

collectstatic:
	cd $(PROJECT_ROOT) && python manage.py collectstatic --clear --no-input

freeze: 
	pipenv run pip freeze > requirements.txt

deploy: freeze collectstatic
	gcloud app deploy --quiet
	gcloud app browse

getproxy:
	test -s $(GC_PROXY) || wget $(GC_PROXY_URL) -O $(GC_PROXY)
	chmod +x $(GC_PROXY)

runproxy: getproxy
	./$(GC_PROXY) -instances="$(DB_CONNECTION_NAME)"=tcp:$(DB_PORT)

devdbup:
	cd deployments/dev && docker-compose up -d 

run: devdbup
	cd $(PROJECT_ROOT) && python manage.py runserver

migrate: devdbup
	cd $(PROJECT_ROOT) && python manage.py makemigrations && python manage.py migrate 

gcrun: 
	make runproxy & cd $(PROJECT_ROOT) && $(GC_LOCAL_ENV) python manage.py runserver

gcmigrate:
	make runproxy & cd $(PROJECT_ROOT) && $(GC_LOCAL_ENV) python manage.py makemigrations && $(GC_LOCAL_ENV) python manage.py migrate