# API Test

This is a simple flask app that you can send an REST API request to.  The response will be the path that was requested along with
all the headers, paramaters, and data that was sent in the request.

This is helpful when troubleshooting API requests to endpoints so you can see EXACTLY what was sent


## Running

`docker run -p 8080:5000 cgwyn/apitest`

## Making Requests

`curl -s 'http://127.0.0.1:8000/api/v1/this/that?query=those&thing'`






