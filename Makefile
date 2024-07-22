build:
	docker-compose build

run:
	docker-compose up

test:
	docker-compose run proxy pytest
