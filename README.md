# location Station
### A xml rest api that return listings and average price for a given outcode

## prerequisite
docker and docker-compose

setup
: clone the repo
    run command 
        : docker-compose up
    in a new bash script
        run command 
            : docker-compose run locationstation python manage.py createsuperuser
    login into the admin area
        : click on listings
            : upload the listing file

endpoints
: api/outcodes/M1
    M1 for manchester
: api/nexus/M1
    M1 for manchester
