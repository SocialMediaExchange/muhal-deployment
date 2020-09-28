# muhal-deployment
Dockerized version of Muhal platform for easy deployment. 

It contains the following: 
- The admin interface of the backend, written in Python using Django. It exposes an restful API. 
- Frontend, written Javascript using Vue.js and Nuxt.js. 
- Nginx reverse proxy to serve the components and static files 


## Backups 

Create a cron job to backup the data of the platform using the following command: 

`docker exec -it muhal-deployment_backend_1 python manage.py dumpdata > ../muhal-$(date +"%Y-%m-%d-%I:%M").json`