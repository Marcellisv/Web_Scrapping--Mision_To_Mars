from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

#Create an instance of Flask
app = Flask(__name__)


mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

@app.route("/")
def home():
    
    combined_mars_dict = mongo.db.mars_db.find_one()

    return render_template("index.html", mars_db=combined_mars_dict)

@app.route("/scrape")
def scraper():
    combined_mars_dict = mongo.db.mars
    mars = scrape_mars.scrape()
    combined_mars_dict.update({}, mars, upsert=True)

    return 'successful'
    

if __name__ == "__main__":
    app.run(debug=True)