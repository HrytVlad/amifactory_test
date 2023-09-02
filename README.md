# AmiFactory Test Task

## How to start:
 ```
git clone https://github.com/HrytVlad/amifactory_test.git
 ```
 ```
docker-compose build
 ```
 ```
docker-compose up -d
 ```
 ```
docker-compose exec app python manage.py createsuperuser 
 ```
## Url to check:
 ```
http://127.0.0.1:8000/api/v1/genres/
 ```
 ```
http://127.0.0.1:8000/api/v1/movies/?genre=1&src=Lio&page=1
 ```
 ```
http://127.0.0.1:8000/api/v1/movies/1
 ```