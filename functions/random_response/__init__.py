import logging
from random import *

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    # words is a list of words from the english dictionary
    words = [   'apple', 'banana', 'orange', 'coconut', 'strawberry', 'lime', 'grapefruit', 'lemon', 'kumquat' ]
    # choose a random word from words
    word = choice(words)

    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             f"This HTTP triggered function executed successfully. Your word of the day is {word}",
             status_code=200
        )
