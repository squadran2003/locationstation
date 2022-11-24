# location Station
***A xml rest api that return listings and average price for a given outcode***

## prerequisite
docker and docker-compose

### setup
1. clone the repo
    - navigate into locationstation
2. create a .env file with the below variables
    SECRET_KEY = ''
    DEBUG = True
    DB_NAME = 'databasename'
    DB_USER = ''
    DB_PASS = ''
    ALLOWED_HOSTS = "*"
    CSRF_TRUSTED_ORIGINS = "http://0.0.0.0" 
3. run command 
    - docker-compose up
4. in a new bash script
    - run command 
    - docker-compose run locationstation python manage.py createsuperuser
5. login into the admin area
    - click on listings
    - upload the listing file

### endpoints
1. api/outcodes/M1
2. api/nexus/M1
