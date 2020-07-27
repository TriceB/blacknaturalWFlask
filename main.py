"""
Testing getting tables from Airtable Base
Goal: Use Airtable as a database for Businesses
  Use Python, Flask and Jinja to access the data in Airtable and dynamically/automatically feed into the website

Currently using Bootstrap to create cards which display the Business, Photo, short info, and link on page

Set up with Airtable Fields
<div class="card text-center">
  <img
    src="{{Business Photo}}"
    class="card-img-top"
    alt="{{Business Name}}"
  />
  <div class="card-body">
      <p class="card-text"><small class="text-muted">Photo Credit: {{Business Name}}</small></p>
    <h5 class="card-title">{{Business Name}}</h5>
    <p class="card-text">{{Things Sold}}</p>
    <a href="{{Website Link}}" class="btn btn-info"
      >Visit Website</a
    >
  </div>
</div>
"""

import os
import glfw
from flask import Flask, render_template
from airtable import Airtable
from pprint import pprint
from flask import request

app = Flask(__name__)


#this will render the index.html as the home page
@app.route('/')
def home():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Featured'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key

    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "index.html", featured_businesses=records
    )  # render the tech.html page and create a variable called businesses and store the records from the airtable base


@app.route("/alcohol")
def alcohol():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Alcohol'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key

    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "alcohol.html", alcohol_businesses=records
    )  # render the alcohol.html page and create a variable called businesses and store the records from the airtable base


@app.route("/art")
def art():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Art'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key
    # at = Airtable('BASE', 'AIR_API')
    # at.get('Art')
    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "art.html", art_businesses=records
    )  # render the art.html page and create a variable called businesses and store the records from the airtable base


@app.route("/accessories")
def accessories():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Clothing/Accessories'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key

    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "accessories.html", accessories_businesses=records
    )  # render the accessories.html page and create a variable called businesses and store the records from the airtable base


@app.route("/casual")
def casual():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Clothing/Casual'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key

    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "casual.html", casual_businesses=records
    )  # process the casual.html file and create a variable called businesses and store the records from above


@app.route("/clothing")
def clothing():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Clothing/Dress'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key

    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "clothing.html", clothing_businesses=records
    )  # process the clothing.html file and create a variable called businesses and store the records from above


@app.route("/merch")
def merch():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Clothing/Merch'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key

    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "merch.html", merch_businesses=records
    )  # render the merch.html page and create a variable called businesses and store the records from the airtable base


@app.route("/shoes")
def shoes():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Clothing/Shoes'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key

    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "shoes.html", shoes_businesses=records
    )  # render the shoes.html page and create a variable called businesses and store the records from the airtable base


@app.route("/swim")
def swim():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Clothing/Swim'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key

    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "swim.html", swim_businesses=records
    )  # process the swim.html file and create a variable called businesses and store the records from above


@app.route("/undergarments")
def undergarments():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Clothing/Undergarments'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key

    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "undergarments.html", undergarments_businesses=records
    )  # render the undergarments.html page and create a variable called businesses and store the records from the airtable base


@app.route("/learning")
def learning():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Educational'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key

    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "learning.html", learning_businesses=records
    )  # render the learning.html page and create a variable called businesses and store the records from the airtable base


@app.route("/entertainment")
def entertainment():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Entertainment'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key

    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "entertainment.html", entertainment_businesses=records
    )  # render the entertainment.html page and create a variable called businesses and store the records from the airtable base


@app.route("/food")
def food():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Food/Drinks'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key
    # at = Airtable('BASE', 'AIR_API')
    # at.get('Art')
    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "food.html", food_businesses=records
    )  # render the food.html page and create a variable called businesses and store the records from the airtable base


@app.route("/fun")
def fun():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Fun/Games'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key

    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "fun.html", fun_businesses=records
    )  # render the fun.html page and create a variable called businesses and store the records from the airtable base


@app.route("/hair")
def hair():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Hair'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key

    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "hair.html", hair_businesses=records
    )  # render the hair.html page and create a variable called businesses and store the records from the airtable base


@app.route("/hairaccessories")
def hairaccessories():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Hair Accessories'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key

    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "hairaccessories.html", hairaccessories_businesses=records
    )  # render the hairaccessories.html page and create a variable called businesses and store the records from the airtable base


@app.route("/decor")
def decor():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Home Decor'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key

    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "decor.html", decor_businesses=records
    )  # render the decor.html page and create a variable called businesses and store the records from the airtable base


@app.route("/household")
def household():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Household Essentials'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key

    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "household.html", household_businesses=records
    )  # render the household.html page and create a variable called businesses and store the records from the airtable base


@app.route("/kids")
def kids():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Kids'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key

    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "kids.html", kids_businesses=records
    )  # render the kids.html page and create a variable called businesses and store the records from the airtable base


@app.route("/marketplaces")
def marketplaces():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Marketplaces'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key

    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "marketplaces.html", marketplaces_businesses=records
    )  # render the marketplaces.html page and create a variable called businesses and store the records from the airtable base


@app.route("/services")
def services():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Services'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key

    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "services.html", services_businesses=records
    )  # render the services.html page and create a variable called businesses and store the records from the airtable base


@app.route("/skin")
def skin():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Skin Care/Hygiene'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key

    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "skin.html", skin_businesses=records
    )  # render the skin.html page and create a variable called businesses and store the records from the airtable base

@app.route("/stationery")
def stationery():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Stationery'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key

    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "stationery.html", stationery_businesses=records
    )  # render the stationery.html page and create a variable called businesses and store the records from the airtable base

@app.route("/tech")
def tech():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Tech'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key

    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "tech.html", tech_businesses=records
    )  # render the tech.html page and create a variable called businesses and store the records from the airtable base


@app.route('/wellness')
def wellness():
    base_key = os.environ['BASE']  # Airtable base key
    table_name = 'Wellness'  # Airtable table name
    airtable = Airtable(
        base_key, table_name, api_key=os.environ['AIR_API']
    )  # Airtable authentication with personal Airtable Account key

    records = airtable.get_all(
        sort="Business Name"
    )  # Get all the records from the table and sort them (default sort is ascending)
    # pprint(records) #this will print all the records from the table to the terminal in better format that print

    return render_template(
        "wellness.html", wellness_businesses=records
    )  # render the wellness.html page and create a variable called businesses and store the records from the airtable base


@app.route('/about')
def about():
    
    return render_template("about.html")  # render the about.html 
    

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(
        host=
        '0.0.0.0',  # Establishes the host, required for repl to detect the site
        port=8080)
