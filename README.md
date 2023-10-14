# DataSenderDB
## Web serise on FastAPI + Postgresql
### FastAPI
implemented a web service on the FastAPI framework that accepts a post request for the purpose of further data processing . In this case, the request specifies the number of questions to be received from the public API. In this case, information about the quiz question is stored in the database. The table has 4 fields: id, question, answer and time created. After each post request, the last record that was saved after the previous request will be sent to the server in response.
Request:

    	Method: Post
        		Path: http://localhost:8000/create_query
        		Headers: Content-type : json
        		Body: { "questions_num":123 }	
    	Response:
    		Headers: Content-type: json
    	    HTTP Code 200
		Body: {"last record": [
                48489,
                "This popular Crimean health resort was an ancient Greek colony",
                "Yalta",
                "2022-12-30T18:58:01.954Z"
                ]}
### Postgresql
Postgresql with Sqlalchemy is used for data storage. This bundle allows you to conveniently connect to the database and work productively with it. Sqlalchemy allows you to use python code to work with databases as if they were ordinary objects in Python

### usage

1. ```git clone https://github.com/maxpurrp/DataSenderDB```
2. ```cd DataSenderDB```
3. ```docker-compose up -d```
4. Send a post request using the Postman application or another similar one by specifying the address ``http://localhost:8000/create_query `` , in the request body, select the data type - json and insert the data ``{
"questions_num":10
}``
After the first request, you will get 'No entries have been added yet' in response, since nothing was recorded in the database before your request. If you send another request, you will get something like this:```{
    "last record": [
                    48489,
                    "This popular Crimean health resort was an ancient Greek colony",
                    "Yalta",
                    "2022-12-30T18:58:01.954Z"
                    ]}```
