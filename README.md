# location Station
### A xml rest api that return listings and average price for a given outcode

## prerequisite
docker and docker-compose

### setup
1.clone the repo
    run command 
        1. docker-compose up
    in a new bash script
        run command 
            1. docker-compose run locationstation python manage.py createsuperuser
    login into the admin area
        1. click on listings
        2. upload the listing file

### endpoints
1. api/outcodes/M1
    M1 for manchester
2. api/nexus/M1
    M1 for manchester
