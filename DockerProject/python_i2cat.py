# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 20:18:10 2021

@author: MiguelF
"""

from flask import Flask
from flask_restful import Api, Resource

import requests

# API creation
app = Flask(__name__)
api = Api(app)

class Posts31May2021(Resource):
    """ Function to  get request with headers order and pagesize included.
    First endpoint “creation_date” & “link” of 3 first/oldest post from 31/5/2021
    """

    def get(self, order, pagesize):
        response2 = requests.get(
            'https://api.stackexchange.com/2.2/posts?fromdate=1622419200&sort=creation&site=stackoverflow',
            params={"order": order, "pagesize": pagesize})
        # Json() on response2 to get response3 as a dictionary
        response3 = response2.json()

        # List of dictionaries to obtain the 'creation_date',
        # 'link' from the response2
        list_of_dicts2 = []
        for dict_ in response3["items"]:
            print("keys on dicts_", dict_.keys())
            res = {key: dict_[key] for key in dict_.keys() &
                   {'creation_date', 'link'}}
            list_of_dicts2.append(res)

        return list_of_dicts2


# Endpoint addition with url routes to complete the order asc
# or desc and pagesize 10
api.add_resource(Posts31May2021, "/post/<string:order>/<string:pagesize>",
                 endpoint='getposts')



class Getbadges(Resource):
    """Function to  get request with headers order included.
    Second endpoint: The “name” and “award_count” of the 10 first badges
    shown when sorting by rank and ordering in ascending manner.
    """
    def get(self, order):
        response2 = requests.get(
            'https://api.stackexchange.com/2.2/badges?pagesize=10&fromdate=1622419200&sort=rank&site=stackoverflow',
            params={"order": order})
        # json() on response2 to get response3 as a dictionary
        response3 = response2.json()

        # List of dictionaries to obtain the 'name', 'award_count'
        # from the response2
        list_of_dicts = []
        for dict_ in response3["items"]:
            res = {key: dict_[key] for key in dict_.keys() &
                   {'name', 'award_count'}}
            list_of_dicts.append(res)

        return list_of_dicts


# Url routes to complete the order asc or desc
api.add_resource(Getbadges, "/badges/<string:order>", endpoint='getbadges')

# Running the app including the port=6789 and allowing debug mode

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, port=6789, host='0.0.0.0')  # Add use_reloader=False  because of message Restarting with winddowsapi realoader exception
