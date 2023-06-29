makemigrations:
	sudo docker-compose run --rm app sh -c "python manage.py makemigrations"

remove_images:
	 sudo docker rmi -f $(sudo docker images -aq)

up:
	sudo docker-compose up

down:
	sudo docker-compose down

build:
	sudo docker-compose build
