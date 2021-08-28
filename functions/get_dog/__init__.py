import logging
import requests

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    
    dog_url = 'https://dog.ceo/api/breeds/image/random'

    # get a random dog json from the dog_url api using the requests library
    #dog_json = requests.get(dog_url).json()

    # Try to get a dog Json from dog_url api using the requests library
    # if the request fails, return a 500 error
    # else retun a 200 with the dog_json
    try:
        dog_json = requests.get(dog_url).json()
    except requests.exceptions.RequestException as e:
        logging.error(e)
        return func.HttpResponse(
            "500 error",
            status_code=500
        )
    else:
        return func.HttpResponse(
            # dog_json as string
            f"{dog_json}",
            status_code=200
        )
    
    # aws api key
    # aws_api_key = '   '
    

    #return the dog_json as a func.HttpResponse
    # return func.HttpResponse(dog_json)

    
    # logging.info('Python HTTP trigger function processed a request.')

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
