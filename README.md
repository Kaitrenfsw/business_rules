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
``` {"subscribed_topics":[
        {"id":60,"user_id":1,"topic_id":45},
        {"id":61,"user_id":1,"topic_id":65}, ...],
        "unsubscribed_topics":[
            {"id":null,"user_id":1,"topic_id":56},
            {"id":null,"user_id":1,"topic_id":12}, ...]
    }
    
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
                        "name": "nombre del gráfico",
                        "topics_selected": [
                                            {"topic_id": 23, "name": "topic 1"},
                                            {"topic_id": 24, "name": "topic 1"},
                                            {"topic_id": 25, "name": "topic 1"}...
                                            ]
                        },
                        {"graph_type": 3,
                        "topics_selected": [
                                            {"topic_id": 66, "name": "topic 1"},
                                            {"topic_id": 77, "name": "topic 1"},
                                            {"topic_id": 88, "name": "topic 1"}
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
    - 2 = hot topics graph
    - 3 = relations graph

- Response format:
``` 
[
  [
    {
    "user_id": 1,
    "graphs_selected":[     
                        {"graph_type": 1,
                        "topics_selected": [
                                            {"topic_id": 23, "name": "topic 1"},
                                            {"topic_id": 24, "name": "topic 1"},
                                            {"topic_id": 25, "name": "topic 1"}...
                                            ]
                        },
                        {"graph_type": 3,
                        "topics_selected": [
                                            {"topic_id": 66, "name": "topic 1"},
                                            {"topic_id": 77, "name": "topic 1"},
                                            {"topic_id": 88, "name": "topic 1"}
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

##### TopicComparison: [http://127.0.0.1:8000/topicComparison/pk/](http://127.0.0.1:8000/topicComparison/<pk>/)

- methods allowed: GET
- pk: Topic id
- request: empty

- Response format: 
``` 
{
“topic_name”: STRING,
“topic_id”: INT,
“relations”: 
[
    {
“r_topic_name”: STRING,
“r_topic_id”: INT,
“distance”: FLOAT
} ,
 … 
]
}

STATUS CODE 200

{"Exception raised": e} STATUS CODE 500   
```

##### ContentUser: [http://127.0.0.1:8000/contentUser/pk/](http://127.0.0.1:8000/contentUser/<pk>/)

- methods allowed: GET
- pk: user id
- request: empty

- Response format: 
    - id: internal id of saved content pair (user_id, content_id) in business-rules
    - content_id: id of new in categorized
``` 
{
  "user_id": "1",
  "contents": [
    {
      "id": 1,
      "content_id": "21"
    },
    {
      "id": 2,
      "content_id": "111"
    },
    {
      "id": 3,
      "content_id": "fmslknd"
    },
    {
      "id": 4,
      "content_id": "lmsÃ±cÃ±dslm"
    }
  ]
}

STATUS CODE 200

{"Exception raised": e} STATUS CODE 500   
```


##### ContentUser: [http://127.0.0.1:8000/contentUser/pk/](http://127.0.0.1:8000/contentUser/pk/)

- methods allowed: PUT
- pk: user_id
- request: empty

- Response format: 
``` 
{"user_id":21, "content_id":"Id"}

STATUS CODE 200

{"Exception raised": e} STATUS CODE 500   
```

##### ContentUser: [http://127.0.0.1:8000/contentUser/](http://127.0.0.1:8000/contentUser/)

- methods allowed: POST
- request:
    - user_id : INT
    - content_id: STRING
``` 
{"user_id":21, "content_id":"Id"}
``` 

- Response format: 
``` 
["Content User created!"]

STATUS CODE 201

{"Exception raised": e} STATUS CODE 500   
```


##### SourceUser: [http://127.0.0.1:8000/sourceUser/pk/](http://127.0.0.1:8000/sourceUser/)

- methods allowed: GET
- pk : user_id
- request: empty

- Response format: 
    - id: source id  (used in POST endpoint)
    - sourceUser_id: id of saved content pair (user_id, source) used in DELETE endpoint
``` 
{
  "user_id": "1",
  "sources": [
    {
      "id": 1,
      "name": "google",
      "site": "www.google.cl",
      "sourceUser_id": 3
    },
    {
      "id": 2,
      "name": "youtube.com",
      "site": "www.yotube.com",
      "sourceUser_id": 2
    }
  ]
}

STATUS CODE 200

{"Exception raised": e} STATUS CODE 500   
```

##### SourceUser: [http://127.0.0.1:8000/sourceUser/pk](http://127.0.0.1:8000/sourceUser/)

- methods allowed: PUT
- pk: 
    - 0: delete source
    - 1: save source
- request:
    - user_id : INT
    - source_id: INT
``` 
{"user_id":21, "source_id": 22}
``` 

- Response format: 
``` 
["Source User created!"]

STATUS CODE 201

{"Exception raised": e} STATUS CODE 500  
``` 

##### SourceUser: [http://127.0.0.1:8000/sourceUser/pk/](http://127.0.0.1:8000/sourceUser/<pk>/)

- methods allowed: DELETE
- pk: sourceUser_id (internal id of saved content pair (user_id, content_id) in business-rules), received in GET endpoint
- request: empty

- Response format: 
``` 
["Source User preference deleted!"]

STATUS CODE 200

{"Exception raised": e} STATUS CODE 500   
```

##### UserVote: [http://127.0.0.1:8000/userVote/pk/](http://127.0.0.1:8000/userVote/<pk>/)

- methods allowed: GET
- pk: user_id
- request: empty

- Response format: 
``` 
{"records":[{  "new_id":"ldmlsdlmksandlks",
    "vote":1
    },
 {  "new_id":"dkdsmdsa",
    "vote":1},...]

STATUS CODE 200

{"Exception raised": e} STATUS CODE 500
``` 

##### UserVote: [http://127.0.0.1:8000/userVote/pk/](http://127.0.0.1:8000/userVote/<pk>/)

- methods allowed: PUT
- pk: user_id
- request:
    - new_id: uid of new saved in categorized
    - source_id: 
``` 
{"new_id": "ld",
"source_id": 33,
"vote": 1}
``` 

- Response format: 
``` 
["User preferences updated!"]

STATUS CODE 200

{"Exception raised": e} STATUS CODE 500
``` 

##### SourceVotes: [http://127.0.0.1:8000/sourceVotes/pk/](http://127.0.0.1:8000/sourceVotes/<pk>/)

- methods allowed: GET
- pk: source_id
- request: empty

- Response format: 
``` 
{   "id":17,
    "name":"Hacker News ",
    "site":"https://news.ycombinator.com/ ",
    "up_votes":2,
    "down_votes":1
    }

STATUS CODE 200

{"Exception raised": e} STATUS CODE 404
``` 

##### SourceVotes: [http://127.0.0.1:8000/sourceVotes/](http://127.0.0.1:8000/sourceVotes)

- methods allowed: GET
- request: empty

- Response format: 
``` 
[{   "id":17,
    "name":"Hacker News ",
    "site":"https://news.ycombinator.com/ ",
    "up_votes":2,
    "down_votes":1
    }, ...]

STATUS CODE 200

{"Exception raised": e} STATUS CODE 404
``` 

##### NewVotes: [http://127.0.0.1:8000/newVotes/](http://127.0.0.1:8000/newVotes)

- methods allowed: GET
- request: empty

- Response format: 
``` 
[{  "new_id":"dkdsmdsa",
    "up_votes":1,
    "down_votes":0},
    {"new_id":"dsnalkdnsadn",
    "up_votes":1,
    "down_votes":0},...]

STATUS CODE 200

{"Exception raised": e} STATUS CODE 404
``` 
##### NewVotes: [http://127.0.0.1:8000/newVotes/pk/](http://127.0.0.1:8000/newVotes/pk/)

- methods allowed: GET
- request: empty

- Response format: 
``` 
{  "new_id":"dkdsmdsa",
    "up_votes":1,
    "down_votes":0
    }

STATUS CODE 200

{"Exception raised": e} STATUS CODE 404
``` 

##### TopicStats: [http://127.0.0.1:8000/topicStats/pk](http://127.0.0.1:8000/newVotes)

- methods allowed: GET
- request:
    - user_ids separated by "-" i.e: 1-22-343-33-22

- Response format: 
``` 
{"topics":[
    {"user_amount":2,
    "topic_name":"Intellectual Property",
    "topic_id": 1}, ...]}

STATUS CODE 200

{"Exception raised": e} STATUS CODE 500
```