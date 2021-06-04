# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 20:18:10 2021

@author: MiguelF
"""

#importing libraries flask and request

from flask import Flask 
from flask_restful import Api, Resource

import requests

# API Creation
app = Flask(__name__)
api = Api(app)



# 1st endpoint:  “creation_date” and “link” of the 3 first/oldest posts from 31/5/2021


class Posts31May2021(Resource):
      # function to  get resquest with headers order and pagesize included.  
      def get(self,order,pagesize):
          response2 = requests.get('https://api.stackexchange.com/2.2/posts?fromdate=1622419200&sort=creation&site=stackoverflow',
                         headers={"order" :order,"pagesize":pagesize})
          # json() on response2 to get response3 as a dictionary 
          response3= response2.json()

          # list of dictionaries to obtain the 'creation_date', 'link' from the response2
          list_of_dicts2 = []
          for dict_ in response3["items"]:
              print("keys on dicts_",dict_.keys())
              res = {key: dict_[key] for key in dict_.keys()
                               & {'creation_date', 'link'}}
              list_of_dicts2.append(res)
          return list_of_dicts2   


#endpoint addition with url routes to complete the order asc or desc and pagezise 10                  
api.add_resource(Posts31May2021,"/post/<string:order>/<string:pagesize>",endpoint='getposts')


# 2nd endpoint: The “name” and “award_count” of the 10 first badges 
# shown when sorting by rank and ordering in ascending manner                  
                   
class Getbadges(Resource):
    # function to  get resquest with headers order included.
    def get(self,order):
        response2 = requests.get('https://api.stackexchange.com/2.2/badges?pagesize=10&fromdate=1622419200&sort=rank&site=stackoverflow',
                         headers={"order" :order})
        # json() on response2 to get response3 as a dictionary
        response3= response2.json()

        # list of dictionaries to obtain the 'name', 'award_count' from the response2
        list_of_dicts = []
        for dict_ in response3["items"]:
            res = {key: dict_[key] for key in dict_.keys()
                               & {'name', 'award_count'}}
            list_of_dicts.append(res)
        return list_of_dicts   

# url routes to complete the order asc or desc
api.add_resource(Getbadges,"/badges/<string:order>",endpoint='getbadges')

# running the app including the port=6789 and allowing debug mode 

if __name__ == "__main__":
	app.run(debug=True,use_reloader=False,port=6789)  #add use_reloader=False added because of message Restarting with widdowsapi realoader exception 
