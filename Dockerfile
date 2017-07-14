FROM python:3.6.1-onbuild

ADD ./dj_project_name /dj_project_name
COPY ./entrypoint.sh /dj_project_name/
WORKDIR /dj_poject_name
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
ENV DJANGO_SETTINGS_MODULE config.settings.prod
RUN ["chmod", "+x", "/dj_project_name/entrypoint.sh"]
ENTRYPOINT ["sh", "/dj_project_name/entrypoint.sh"]
