# API Test

This is a simple flask app that you can send an REST API request to.  The response will be the path that was requested along with
all the headers, paramaters, and data that was sent in the request.

This is helpful when troubleshooting API requests to endpoints so you can see EXACTLY what was sent


## Running

`docker run -p 8080:5000 ghcr.io/chipgwyn/apitest/apitest:latest`

## Making Requests

`curl -s 'http://127.0.0.1:8080/api/v1/this/that?query=those&thing'`

## Example

### Start the container

```
# docker run -p 8080:5000 ghcr.io/chipgwyn/apitest/apitest:latest
 * Serving Flask app 'app/apitest'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
172.17.0.1 - - [05/Feb/2025 15:31:54] "GET /this/api/v1/that HTTP/1.1" 200 -
```

### Make a request

```
# curl -s 'http://127.0.0.1:8080/this/api/v1/that?query=things&those=that' | jq
{
  "path": "/this/api/v1/that",
  "method": "GET",
  "headers": {
    "Host": "127.0.0.1:8080",
    "User-Agent": "curl/8.7.1",
    "Accept": "*/*"
  },
  "args": {
    "query": "things",
    "those": "that"
  },
  "form": {},
  "data": "",
  "response": "Requested Path: this/api/v1/that"
}
```
