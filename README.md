# Django Quick Template


This is a template for a quick django application development

## Usage

Clone repo

```bash
$ cd dj_quickie
$ # Run python script to change project name
$ python templator
$ docker build -t <docker image name> .
$ docker run --name <project_name> -d <dockerimage>:latest
```

## Bundles

* Django 1.11.1
* python 3.6.1
* [Whitenoise](https://github.com/evansd/whitenoise) for static files
* [django-environ](https://github.com/joke2k/django-environ) for Environment Variables
* Seperated Settings files for production and development
* Dockerfile
