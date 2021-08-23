FROM python:3-alpine
ENV DB_USER=""
ENV DB_HOST=""
ENV DB_PASS=""
ENV DB_NAME=""
ENV JWT_SEED=""
RUN mkdir /var/app
COPY . /var/app
WORKDIR /var/app
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["python","api.py"]