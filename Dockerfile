FROM python:3.6.1-onbuild

ADD ./heyo /heyo
COPY ./entrypoint.sh /heyo/
WORKDIR /
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
ENV DJANGO_SETTINGS_MODULE config.settings.prod
RUN ["chmod", "+x", "/heyo/entrypoint.sh"]
ENTRYPOINT ["sh", "/heyo/entrypoint.sh"]