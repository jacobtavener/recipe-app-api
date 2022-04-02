test:
	docker-compose run --rm app sh -c "python manage.py test && flake8"
migration:
	docker-compose run --rm app sh -c "python manage.py makemigrations"
start-server:
	docker-compose up