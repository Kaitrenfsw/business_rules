# Business Rules

# Topics administration API
Database: Postgres  9.5.12>=

## How to Run?

## Running with Docker:

``` $ docker-compose up```

Run fixture in container to load data:

``` docker-compose exec procesamiento python3 service_TM/manage.py loaddata service_TM/fixture.json```


### Linux/MacOS

Install a virtualenv with python3 more info [here](https://rukbottoland.com/blog/tutorial-de-python-virtualenv/)


Run the virtualenv:

``` $ source venv/bin/activate```

Install requirements.txt:

``` $ pip install -r requirements.txt ```

Run Migrations and fixture from service_TM folder:

``` python manage.py makemigrations ```

``` python manage.py migrate ```

```python manage.py loaddata fixture.json```

Run Django API from service_TM folder:

``` $ python manage.py runserver ```


#API Endpoints:

##### Topic: [http://127.0.0.1:8000/topic/](http://127.0.0.1:8000/topic/)

- methods allowed: GET
- Request: empty
- Response: All topics available
- Response format:
``` [
    {
        "id": 1,
        "topic_number": 0,
        "lda_model": 1,
        "name": null,
        "keyword_topic": [
            {
                "id": 1,
                "name": "ad",
                "weight": 0.00999999977648258
            },
            {
                "id": 2,
                "name": "food",
                "weight": 0.00999999977648258
            },
            {
                "id": 3,
                "name": "ads",
                "weight": 0.00999999977648258
            },
            ...
        ]
    },
    {
        "id": 2,
        "topic_number": 1,
        "lda_model": 1,
        "name": null,
        "keyword_topic": [
            {
                "id": 6,
                "name": "say",
                "weight": 0.0299999993294477
            },
            {
                "id": 7,
                "name": "us",
                "weight": 0.00999999977648258
            },
            ...
        ]
    },
    ...
    
]
``` 
- methods allowed: POST
- Request: 
``` 
{
	"topic_number": 1,
	"lda_model_filename": "lda_01_20000.model",
	"topic_name": "topic1"
}
```
- Response: Status message
- Response format:
```
- HTTP_200_OK: {"New Topic added successfully"}
- HTTP_500_INTERNAL_SERVER_ERROR: {<specific exception>}
- HTTP_400_BAD_REQUEST: {"Bad Request, check sent parameters"}
```

##### Topic: [http://127.0.0.1:8000/topic/pk](http://127.0.0.1:8000/topic/)

- methods allowed: GET
- pk: topic_id
- Request: empty
- Response: All topics and keywords from a certain Topic
- Response format:
``` [
    {
        "id": 1,
        "topic_number": 0,
        "lda_model": 1,
        "name": null,
        "keyword_topic": [
            {
                "id": 1,
                "name": "ad",
                "weight": 0.00999999977648258
            },
            {
                "id": 2,
                "name": "food",
                "weight": 0.00999999977648258
            },
            {
                "id": 3,
                "name": "ads",
                "weight": 0.00999999977648258
            },
            ...
        ]
    },
    {
        "id": 2,
        "topic_number": 1,
        "lda_model": 1,
        "name": null,
        "keyword_topic": [
            {
                "id": 6,
                "name": "say",
                "weight": 0.0299999993294477
            },
            {
                "id": 7,
                "name": "us",
                "weight": 0.00999999977648258
            },
            ...
        ]
    },
    ...
    
]
``` 

##### TopicUser: [http://127.0.0.1:8000/topicUser/pk](http://127.0.0.1:8000/topicUser/)

- methods allowed: GET
- pk: user_id
- request: empty

- Response: All topics and keywords selected for a certain User
- Response format:
``` [
    {
        "id": 1,
        "topic_number": 0,
        "lda_model": 1,
        "name": null,
        "keyword_topic": [
            {
                "id": 1,
                "name": "ad",
                "weight": 0.00999999977648258
            },
            {
                "id": 2,
                "name": "food",
                "weight": 0.00999999977648258
            },
            ...
        ]
    },
    ...
]
```

- methods allowed: PUT
- action: update topics related to certain user
- Request: 
``` 
{
	"user_id": 12
	"user_topics_id": [1, 18]
}
```
- Response: Status message
- Response format:
```
- HTTP_200_OK: {"Topics updated successfully"}
- HTTP_500_INTERNAL_SERVER_ERROR: {<specific exception>}
- HTTP_400_BAD_REQUEST: {"Bad Request, check sent parameters"}
```
##### TopicUser: [http://127.0.0.1:8000/topicUser/](http://127.0.0.1:8000/topicUser/)

- methods allowed: GET
- request: empty

- Response: All topics and keywords
- Response format:
``` [
    {
        "id": 1,
        "topic_number": 0,
        "lda_model": 1,
        "name": null,
        "keyword_topic": [
            {
                "id": 1,
                "name": "ad",
                "weight": 0.00999999977648258
            },
            {
                "id": 2,
                "name": "food",
                "weight": 0.00999999977648258
            },
            ...
        ]
    },
    ...
]
```
