app.build.dev:
	docker-compose up --build -d
	make app.migrate

app.migrate:
	docker exec -it ghibli_web python manage.py migrate

app.create_migrations:
	docker exec -it ghibli_web python manage.py makemigrations ghibliapp

app.docker.bash:
	docker exec -it ghibli_web bash

app.run.tests:
	docker exec -it ghibli_web pip install -r requirements-test.txt
	docker exec -it ghibli_web python manage.py test ghibliapp

app.run.loadghibli:
	docker exec -it ghibli_web python manage.py loadghiblidata

app.run.server:
	docker exec -it ghibli_web python manage.py runserver 0.0.0.0:8000

app.check.code_style:
	docker exec -it ghibli_web pycodestyle --show-source --show-pep8 --exclude=tests,settings.py,migrations,templates,.env,.env.example,asgi.py,wsgi.py ghibliapp/
