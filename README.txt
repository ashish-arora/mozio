API Docs:

To Get all the providers listed use:

curl http://54.148.141.180:8000/api/v1/providers/ -XGET  -H "Content-Type: application/json"

To create new provider use:

curl http://54.148.141.180:8000/api/v1/providers/ -XPOST  -H "Content-Type: application/json" -d '{"name": "abcmy", "email":"asdasdasdasasdadsd@gmail.com", "phone_number":"234234234", "currency":"INR", "language":"English"}'

To delete a provider use:

curl http://54.148.141.180:8000/api/v1/providers/56d3409bbe4c6b7704268642/ -XDELETE  -H "Content-Type: application/json"

To get the particular provider information use with the provider id:

curl http://54.148.141.180:8000/api/v1/providers/56d3409bbe4c6b7704268642/ -XGET  -H "Content-Type: application/json"

To update particualr provider information:

curl http://54.148.141.180:8000/api/v1/providers/56d3409bbe4c6b7704268642/ -XPUT  -H "Content-Type: application/json" -d '{"name": "abcmy", "email":"asdasdasdasasdadsd@gmail.com", "phone_number":"234234234", "currency":"INR", "language":"English"}'

To find the service areas corresponding to the latitude and longitude use the below api:

curl http://54.148.141.180:8000/api/v1/find-service-area/ -H "Content-Type: application/json" -XGET -d '{"lat":102.0, "long":2.0}'

To get the particular service area information: 

curl http://54.148.141.180:8000/api/v1/service-area/56d2f6ceea8f020231ac416b/ -XGET  -H "Content-Type: application/json"

To delete particular service area: 

curl http://54.148.141.180:8000/api/v1/service-area/56d2f6ceea8f020231ac416b/ -XDELETE  -H "Content-Type: application/json"

To create service area for the providers use where provider is the corresponding provider who is adding the service area:

curl http://54.148.141.180:8000/api/v1/service-area/ -XPOST  -H "Content-Type: application/json" -d '{"provider":"56d3409bbe4c6b7704268642", "loc":{"type":"Polygon", "coordinates":[[[102.0, 2.0], [103.0, 2.0], [103.0, 3.0], [102.0, 3.0], [102.0, 2.0]]], "properties":{"name":"sector 16", "price":20}}}'


To update service area use :

curl http://54.148.141.180:8000/api/v1/service-area/56d2f6ceea8f020231ac416b/ -XPUT -H "Content-Type: application/json" -d '{"provider":"56d3409bbe4c6b7704268642", "loc":{"type":"Polygon", "coordinates":[[[102.0, 2.0], [103.0, 2.0], [103.0, 3.0], [102.0, 3.0], [102.0, 2.0]]], "properties":{"name":"sector 16", "price":20}}}'


To get multi service area use below api , you need to give the service area ids in the "ids" key in the list form

curl http://54.148.141.180:8000/api/v1/get-multi-service-area/ -XPOST  -H "Content-Type: application/json" -d '{"ids":["56d2f6ceea8f020231ac416b", "56d2f7ceea8f020231ac416c"]}'


