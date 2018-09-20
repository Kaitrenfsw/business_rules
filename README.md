# Business Rules

# Topics administration API
Database: Postgres  9.5.12>=

## How to Run?

## Running with Docker:

``` $ docker-compose up```

### Linux/MacOS

Install a virtualenv with python3 more info [here](https://rukbottoland.com/blog/tutorial-de-python-virtualenv/)


Run the virtualenv:

``` $ source venv/bin/activate```

Install requirements.txt:

``` $ pip install -r requirements.txt ```

Run Migrations and fixture from service_TM folder:

``` python manage.py makemigrations ```

``` python manage.py migrate ```

Run Django API from service_TM folder:

``` $ python manage.py runserver ```


#API Endpoints use via BFF:

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


##### TopicUser: [http://127.0.0.1:8000/topicUser/pk/](http://127.0.0.1:8000/topicUser/)

- methods allowed: GET
- pk: user id
- request: empty

- Response: All topics id subscribed by a certain user
- Response format:
``` [
    {
        "topic_id": 11
    },
    {
        "topic_id": 12
    },
    ...
]
```
##### TopicUser: [http://127.0.0.1:8000/topicUser/pk/](http://127.0.0.1:8000/topicUser/)

- methods allowed: PUT
- pk: user id 
- request: 
``` {
    "user_id": 1,
    "user_topics_id": [11,12,13,14,15,16]
}
```
- user_topics_id : topics subscribed after save last selection in UI
- Response format: 
``` ["Topics updated successfully!"] STATUS CODE 200
    ["Bad Request, check sent parameters"] STATUS CODE 500
    ["Exception raised": e] STATUS CODE 400   
]
```
