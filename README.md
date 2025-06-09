# windows

## prepare docker env

```commandline
docker build -t monkitect_graph -f docker/Dockerfile .
docker run --rm -it --name monkitect_graph -p 4503:4503 -v .\src:/code -v .\logs:/logs -v E:\baiyigali\datasets:/dataset --env-file .env monkitect_graph bash
docker exec -it monkitect_graph bash
```

## create project

ref: https://docs.djangoproject.com/en/4.2/intro/tutorial01/ <br>
generate project (named app) in src directory, which generate app folder and manage.py in src directory

```commandline
cd project_folder
django-admin startproject app src
```

## start project

```commandline
python manage.py runserver 0.0.0.0:4503
```

## enable admin (Optional)

```commandline
python manage.py createsuperuser
```

## create app

ref: https://docs.djangoproject.com/en/4.2/intro/tutorial02/

```commandline
python manage.py startapp videoeditor
```

```commandline
jupyter-notebook --allow-root --ip 0.0.0.0 --port 4503
```

## sitemap

ref: https://docs.djangoproject.com/en/4.2/ref/contrib/sitemaps/

```commandline
python manage.py startapp sitemap

define sitemap class and config urls
```