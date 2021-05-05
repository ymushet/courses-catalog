# catalog rest api



To set up and run a project you have to have a docker installed on your OS.

Execute following commands inside project directory:

>$ docker build .

>$ docker-compose run webapp python /src/manage.py migrate

>$ docker-compose run webapp python /src/manage.py test

Create your superuser and remember credentials for write access

>$ docker-compose run webapp python /src/manage.py createsuperuser

>$ docker-compose up --build

Visit localhost to work with api
> http://127.0.0.1:8000/

For the first app start course list is empty:

To create one log-in to your user with

> http://127.0.0.1:8000/api-auth/login/?next=/courses/

Feel in your course data and create it with a POST button.
You should see your new course in response.

Example:

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "name": "Golang School",
        "start_at": "2021-09-09T17:00:00Z",
        "end_at": "2022-07-07T17:00:00Z",
        "lectures": 5,
        "author": "admin"
    },
    {
        "id": 2,
        "name": "Python Basics",
        "start_at": "2021-09-09T17:00:00Z",
        "end_at": "2022-07-07T17:00:00Z",
        "lectures": 10,
        "author": "admin"
    }
]
```

Course view support search, ordering, and filtering by start and end dates.

To see course details visit

> http://127.0.0.1:8000/<ind:id>

If you are log in as a course author you can UPDATE course info with PUT request or delete it with DELETE request. 
