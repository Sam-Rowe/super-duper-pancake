import logging
import requests
import json
import random

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed  the get animal request')

    # Roll a dice
    dice = random.randint(1, 6)
    logging.info('Rolled a dice: %s', dice)

    cat_api_url = 'https://catfact.ninja/fact'
    dog_api_url = 'https://dog.ceo/api/breeds/image/random' 

    headers = {'Content-Type': 'application/json'}


    # if dice is even make a web request to the dog api dog_api_url
    animal_response = None
    if dice % 2 == 0:
        animal_response = requests.get(dog_api_url, headers=headers)
    # if dice is odd make a web request to the cat api https://catfact.ninja/fact
    else:
        animal_response = requests.get(cat_api_url, headers=headers)

    # if the response is not 200 then return fun.HttpResponse(status_code=200) with an empty json body
    if animal_response.status_code != 200:
        return func.HttpResponse(status_code=200)
    else:
        # return fun.HttpResponse(status_code=200) with the json body of the response
        return func.HttpResponse(
            json.dumps(animal_response.json()),
            status_code=200
        )  
    

    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )

