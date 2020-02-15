app.build.dev:
	docker-compose up --build -d

app.docker.bash:
	docker exec -it ghibli_web bash

app.run.tests:
	docker exec -it ghibli_web python -m unittest discover -s tests/  -p "*Test.py"