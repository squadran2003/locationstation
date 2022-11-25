# location Station
***A xml rest api that return listings and average price for a given outcode***

## prerequisite
1. docker
2. docker-compose
3. listings.csv

### setup
1. clone the repo
    - navigate into locationstation
2. create a .env file with the below variables
    - SECRET_KEY = ''
    - DEBUG = True
    - DB_NAME = 'databasename'
    - DB_USER = ''
    - DB_PASS = ''
    - ALLOWED_HOSTS = "*"
    - CSRF_TRUSTED_ORIGINS = "http://0.0.0.0" 
    - DJANGO_SUPERUSER_PASSWORD="your password"
    - DJANGO_SUPERUSER_EMAIL=example@example.com
    - DJANGO_SUPERUSER_USERNAME=admin

3. run command 
    - docker-compose up

4. login into the admin area
    - click on listings
    - click on import and select listing file
    - click submit button
    - click confirm import 

### endpoints
1. http://0.0.0.0/api/outcode/M1/
2. http://0.0.0.0/api/nexus/M1

### production
The container is already setup for production using ngnix and gunicorn.
Change the below env varaibles

1. DEBUG = False
2. ALLOWED_HOSTS = "yourdomainname.com,yourseconddomainname.com"
3. CSRF_TRUSTED_ORIGINS = "http://yourdomainname.com,http://yourseconddomainname.com" 
4. DJANGO_SUPERUSER_PASSWORD="more secure password"
5. DJANGO_SUPERUSER_EMAIL=example@example.com
6. DJANGO_SUPERUSER_USERNAME=admin
7. ***change secret key to something more secure***
    - SECRET_KEY = ''
