FROM python:3.8

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		mysql-client \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /nt_django_crud
COPY ./nt_django_crud ./nt_django_crud
RUN pip install -r ./nt_django_crud/requirements.txt
RUN python3 ./nt_django_crud/manage.py migrate
COPY . .

EXPOSE 8000
CMD ["python", "./nt_django_crud/manage.py", "runserver", "0.0.0.0:8000"]