FROM python:3.9-slim

WORKDIR app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=80"]