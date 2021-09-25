# flask-demo

Demo web app for testing purposes. Listens on port 5000 and will respond to GET requests and log out request information.

## Setup

Assuming you have python3 installed you can run the following to start the app:

    python3 -m venv env
    env/bin/pip install -r requirements.txt
    flask run

The app will now be visible at [http://127.0.0.1:5000](http://127.0.0.1:5000)


### Running with docker

    docker build -t flask-demo .
    docker run -p 80:80 flask-demo

The app should now be visible at [http://127.0.0.1/](http://127.0.0.1/)