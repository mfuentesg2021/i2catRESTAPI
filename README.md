# i2catRESTAPI Programming challenge

# The Requirements
Create a REST API in Python3 application that fetches specific resources from the StackExchange API (https://api.stackexchange.com/docs). Use the following tools:

    Python’s requests library (https://docs.python-requests.org/en/master/)

    Python’s Flask server (https://flask.palletsprojects.com/en/2.0.x/quickstart/) running the server from the code (https://flask.palletsprojects.com/en/2.0.x/server/), listening on port 6789 and allowing debug mode / refreshing the server when the code is modified


Specifically, you should provide an API with two endpoints to provide:

 1.-   The “creation_date” and “link” of the 3 first/oldest posts from 31/5/2021.

 2.-   The “name” and “award_count” of the 10 first badges shown when sorting by rank and ordering in ascending manner.
    
## Explanation

A python file including the app on python_i2cat.py has been generated.  
The 2 endopints requested can be depicted on host by accesing the following :

 1.-  The first endopint need as input   http://127.0.0.1:6789/post/<order>/<pagesize>
        example :  " http://127.0.0.1:6789/post/asc/3"   
      <order> is limited to : asc ord descto get the  first/oldest posts from 31/5/2021.
      The date 31/5/2021 has already has already been parsed on the url for requests.get( ) with value fromdate= '1622419200'.
       The result are the <pagesize> first/oldest (<order>) posts  from 31/5/2021 in a list of dictionaries.

 1.-  The first endopint need as input   http://127.0.0.1:6789/badges/<order>
        example :  " http://127.0.0.1:6789/badges/desc"    
       <order> is limited to : asc or desc .
      The date 31/5/2021 has already has already been parsed on the url for requests.get( ) with value fromdate= '1622419200'.
      The result are  first/oldest (<order>) 10 badges when sorting by rank and ordering in ascending manner from 31/5/2021 in a list of dictionaries.

  
  
## Deployment (Docker)
        The **Dockerfile** contains the steps tu create the image  and tag on windows
         Create the image:
         docker build -f DockerProject/Dockerfile -t mfuentesg2021/i2cat .   
     
    
         
