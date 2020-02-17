# Python Back-end Assignment: Movie List by Christos Georgiou
The purpose of this task is to consume two endpoints from Studio Ghibli REST API and produce
a view with a list of movies and the people in the movie

## Requirements
In order to run the application you will need to have installed in your machine
* make - example: ```sudo apt-get install make```
* docker with docker-compose

## Logic of the application
### Consuming Studio Ghibli API
Because the consuming of the data needs to be asynchronous I've created a command that will
run in a cron job every minute in production. Because I don't want to run in my dev environment 
to load the data every minute the cronjob is not included in this task.
### Serving the movies list
After consuming the data and saving them in our local db based on the models relationships, under the url path
```
http://localhost:8000/movies
```
you can find the list of the movies with a title, description and the last update at information,
alongside with the people's name playing in it. In order to see data on the endpoint first you need to run
the consume command.

Not all movies have people related to them and the given API doesn't support pagination just a limit option so I am 
just loading the whole data with the maximum limit of 250. The responses of the endpoints are not having
more than 250 results but this is not the optimal way as we need to cater for results bigger than 250 with pagination.

## Running the application
In order to run the application you need to run the following command to build the dev environment docker machines
### Build
```
make app.build.dev
```
The above command will run the docker and run the database migrations

### Consume data
```
make app.run.loadghibli
```
The above command will consume both endpoints and load the data to our database

### Load page with movies list
```
make app.run.server
```
Will start the server for our web app and then the result can be accessed by the url
```
http://localhost:8000/movies
```

### Run tests
```
make app.run.tests
```
The above command will install the test requirements and run all the tests written for the app 

### Check PEP8 Code style
```
make app.check.code_style
```
Will run the sniffer for our application to check for any violations of PEP8

### Other useful commands
```
# Will run the migrations
make app.migrate 

# Will try to find differences of the current migrations and generate migration files
make app.create_migrations

# Will access the docker container in bash shell
make app.docker.bash
```

## Tests
I have written two type of tests. Unit and Behavioral tests. Usually I prefer to unit testing all the services
in my app with mocked dependencies and testing only the behavior of the class. As for functional tests
I prefer a gherkin type tool with pre loaded fixtures in order to have specific data to test for my environment.
In the current behavioral tests only the view is being tested and not the command and the fixtures are loaded
on the fly from each method. 

These two types of tests are covering the integration tests and every other aspect of testing during the execution of the
application like persisting/retrieving models, deserializing/serializing, validations and responses from an API.

