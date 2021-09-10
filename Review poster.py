#! /usr/bin/env python3

import os
import requests
from requests.models import Response

path = '/data/feedback'
url = 'http://35.222.18.120/feedback'
review_dict = {}

''' Generates a dictionary to be pushed to the URL listed below '''

for file in os.listdir(path):
    if file.endswith('.txt'):
        txt_file = os.path.join(path, file)
        with open(txt_file, 'r') as review:
            counter = 0
            for line in review:
                counter += 1
                if counter == 1:
                    review_dict['title'] = line
                if counter == 2:
                    review_dict['name'] = line
                if counter == 3:
                    review_dict['date'] = line
                if counter == 4:
                    review_dict['feedback'] = line
                    response = requests.post(r'http://35.222.18.120/feedback', data=review_dict)
                    print('Response', response_satus_code) 
                    





