install:
	docker-compose run --rm server pip install -r requirements-.txt --user --upgrade --no-warn-script-location

start:
	docker-compose up server

build:
	docker build -t employee_department .