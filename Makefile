PROJECT_ROOT := app
PROJECT := app
GCLOUD_PROJECT := smart-sheets-backend
DB_CONNECTION_NAME := smart-sheets-backend:europe-west3:postgres1
PROXY_PORT := 5435
GC_PROXY := cloud_sql_proxy
GC_PROXY_URL := https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64
GC_LOCAL_ENV := DJANGO_CONFIGURATION=Local DJANGO_DATABASE_PORT=$(PROXY_PORT)
CFG_COMPILE_IGNORE := PORT='$$PORT'

include $(PROJECT_ROOT)/.env
export

.PHONY: pipenv
pipenv:
	pipenv shell

.PHONY: collectstatic
collectstatic:
	cd $(PROJECT_ROOT) && python manage.py collectstatic --clear --no-input

.PHONY: freeze
freeze: 
	pipenv run pip freeze > requirements.txt

.PHONY: compilecfg
compilecfg:
	$(CFG_COMPILE_IGNORE) envsubst < ./app.tml.yaml > app.yaml

.PHONY: deploy
deploy: freeze collectstatic compilecfg
	gcloud app deploy --quiet
	gcloud app browse
	rm -f app.yaml 

.PHONY: getproxy
getproxy:
	test -s $(GC_PROXY) || wget $(GC_PROXY_URL) -O $(GC_PROXY)
	chmod +x $(GC_PROXY)

.PHONY: runproxy
runproxy: getproxy
	./$(GC_PROXY) -instances="$(DB_CONNECTION_NAME)"=tcp:$(PROXY_PORT)

.PHONY: devdbup
devdbup:
	cd deployments/dev && docker-compose up -d 

.PHONY: run
run: devdbup
	cd $(PROJECT_ROOT) && python manage.py runserver

.PHONY: migrate
migrate: devdbup
	cd $(PROJECT_ROOT) && python manage.py makemigrations && python manage.py migrate 

.PHONY: gcrun
gcrun: 
	cd $(PROJECT_ROOT) && $(GC_LOCAL_ENV) python manage.py runserver

.PHONY: gcmigrate
gcmigrate:
	cd $(PROJECT_ROOT) && $(GC_LOCAL_ENV) python manage.py makemigrations && $(GC_LOCAL_ENV) python manage.py migrate