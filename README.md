# location Station
***A xml rest api that return listings and average price for a given outcode***

## prerequisite
docker and docker-compose

### setup
1. clone the repo
    - navigate into locationstation
2. run command 
    - docker-compose up
3. in a new bash script
    - run command 
    - docker-compose run locationstation python manage.py createsuperuser
4. login into the admin area
    - click on listings
    - upload the listing file

### endpoints
1. api/outcodes/M1
2. api/nexus/M1
