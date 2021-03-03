from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

#Create an instance of Flask
app = Flask(__name__)

#Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home():
    mars_data = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars_data)


db.mars_db.drop()

@app.route("/scrape")
def scraper():
    mars_data = mongo.db.mars
    mars = scrape_mars.scrape()
    mars_data.update({}, mars, upsert=True)

    # Redirect back to home page
    return 'successful'

if __name__ == "__main__":
    app.run(debug=True)