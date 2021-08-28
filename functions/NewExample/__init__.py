import logging
import requests
import matplotlib.pyplot
import numpy as np

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # using the requests libary get the regional carbon data from https://api.carbonintensity.org.uk/regional/england/ and return as a json string
    r = requests.get('https://api.carbonintensity.org.uk/regional/england/')
    
    r_json = r.json()

    # select data from r_json 
    mix_json = r_json['data'][0]['data'][0]['generationmix']

    # for each mix object in mix_json append fuel to  fuels np.array and perc to  percentages np.array
    fuels = np.array([])
    percentages = np.array([])
    for mix in mix_json:
        # log mix
        logging.info(mix)
        fuels = np.append(fuels, mix['fuel'])
        percentages = np.append(percentages, mix['perc'])
    
    # use fuels and percentages to create a pie chart using the matplotlib pyplot pie library
    # export pie chart to jpg file
    # return jpg file as a response
    fig, ax = matplotlib.pyplot.subplots()
    ax.pie(percentages, labels=fuels, autopct='%1.1f%%', shadow=True, startangle=90)
    matplotlib.pyplot.axis('equal')
    matplotlib.pyplot.savefig('mypie.jpg')
    matplotlib.pyplot.close()
    logging.info('mypie.jpg file created')

    # read mypie.jpg file into a bytearray object called image_bytes
    with open('mypie.jpg', 'rb') as image_file:
        image_bytes = image_file.read()
        return func.HttpResponse(image_bytes, mimetype='image/jpg')