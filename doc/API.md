## Test API REST
Use HTTPie
https://httpie.io/
### GET
```
http http://localhost:5000/example/rest/v1/beers
```
### GET
```
http http://localhost:5000/example/rest/v1/beer/1
```
### POST
```
http POST http://localhost:5000/example/rest/v1/beer <<< '{
    "brand": "Krombach",
    "dateReleased": "1803-10-11T13:44:02",
    "ingredients": [
        {
            "name": "Malta"
        },
        {
            "name": "Agua"
        }
    ],
    "name": "Krombacher",
    "locationId": 5
}'
```
### PUT
```
http PUT http://localhost:5000/example/rest/v1/beer/3 <<< '{
    "brand": "Other",
    "dateReleased": "2001-11-06T13:44:02",
    "name": "Cusqueñita",
    "locationId": 2
}'
```
### DELETE
```
http DELETE http://localhost:5000/example/rest/v1/beer/3
```