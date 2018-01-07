# docker-flask-boilerplate

Just how I like to start my docker/flask-projects.

- Edit name ./code/backend/setup/setup.py
- Setup required pip packages with ./code/backend/setup/requirements.txt
- Add routes to ./code/backend/services/api/routes

```
# For dev env
docker-compose run --rm --service-ports api bash
> python run.py
```