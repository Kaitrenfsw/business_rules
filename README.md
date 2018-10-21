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

##### userDashboard: [http://127.0.0.1:8000/userDashboard/pk/](http://127.0.0.1:8000/userDashboard/)

- methods allowed: PUT
- pk: user_id
- graph_type:
    - 1 = Frequency graph
    - 2 = relation graph
    - 3 = hot topics graph
    
- request: 
``` 
    {"graphs_selected":[     
                        {"graph_type": 1,
                        "topics_selected": [
                                            {"topic_id": 23},
                                            {"topic_id": 24},
                                            {"topic_id": 25}...
                                            ]
                        },
                        {"graph_type": 3,
                        "topics_selected": [
                                            {"topic_id": 66},
                                            {"topic_id": 77},
                                            {"topic_id": 88}
                                            ]
                        }...] 
   }
```

- Response format: 
``` 
    {"User preferences updated!"} STATUS CODE 200
    {"Exception raised": e} STATUS CODE 500
```

##### userDashboard: [http://127.0.0.1:8000/userDashboard/pk/](http://127.0.0.1:8000/userDashboard/)

- methods allowed: DELETE
- pk: user_id

- request: empty

- Response format: 
``` 
    {"User preferences deleted!"} STATUS CODE 200
    {"Exception raised": e} STATUS CODE 500
```

##### userDashboard: [http://127.0.0.1:8000/userDashboard/pk/](http://127.0.0.1:8000/userDashboard/)

- methods allowed: GET
- pk: user_id
- graph_type:
    - 1 = Frequency graph
    - 2 = relation graph
    - 3 = hot topics graph

- Response format:
``` 
[
  [
    {
    "user_id": 1,
    "graphs_selected":[     
                        {"graph_type": 1,
                        "topics_selected": [
                                            {"topic_id": 23},
                                            {"topic_id": 24},
                                            {"topic_id": 25}...
                                            ]
                        },
                        {"graph_type": 3,
                        "topics_selected": [
                                            {"topic_id": 66},
                                            {"topic_id": 77},
                                            {"topic_id": 88}
                                            ]
                        }...] 
   }

  ]
]

{"Exception raised": e} STATUS CODE 500     
```

##### dateConversion: [http://127.0.0.1:8000/dateConversion/yyyy-mm-dd/](http://127.0.0.1:8000/dateConversion/yyyy-mm-dd/)

- methods allowed: GET
- yyyy-mm-dd: example -> 2014-12-28
- request: empty

- Response format: 
``` 
[{"date":"2010-01-01","week":1,"sunday_date":"2010-01-03"},...] STATUS CODE 200
{"Exception raised": e} STATUS CODE 500   
``` 

##### TopicComparison: [http://127.0.0.1:8000/topicComparison/<pk>/](http://127.0.0.1:8000/topicComparison/<pk>/)

- methods allowed: GET
- pk: Topic id
- request: empty

- Response format: 
``` 
[
[{
    "topic1_id":1,
    "topic2_id":99,
    "distance":0.6740753962,
    "topic2_name": "Cybersecurity",
    "topic2_name": "Blogging",
    "keywords_match":[
                        {"name":"part"},
                        {"name":"technology"}, ...]
   },...
   ]
]
STATUS CODE 200

{"Exception raised": e} STATUS CODE 500   
```