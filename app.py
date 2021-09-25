import logging

from flask import Flask, request

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

@app.route("/")
def root():
    app.logger.info(f'Request user agent: {request.user_agent}')
    app.logger.info(f'Request host: {request.host}')
    return '''
        <html>
            <h1>I like cats.</h1>
            <img src="https://placekitten.com/300/300" alt="kitten"/>
        </html>
    '''
