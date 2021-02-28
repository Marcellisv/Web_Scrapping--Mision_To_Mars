from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

#Create connection 
mongo = PyMongo(app, uri="mongodb://localhost:27017/Mars_db")

#Create route to  data form mongodb database
@app.route("/")
def home():
    mars_data = scraped_mars.find()
    return  render_template('index.html', mars_data=mars_data)

@app.route("/scrape")
def scrape():
    
    scrape_mars.scrape()

    return redirect("/")

if __name__ == "__main__":
    
    app.run(debug=True)



