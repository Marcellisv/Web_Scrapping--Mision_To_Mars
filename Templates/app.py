from flask import Flask, render_template, redirect
import pymongo


# Create an instance of Flask
app = Flask(__name__)

#Create connection 
client = pymongo.MongoClient('mongodb://localhost:27017/')

#Create route to  data form mongodb database
@app.route("/")
def home():
    mars_data = scraped_mars.find_one()
    return  render_template('index.html', mars_data=mars_data)

@app.route("/scrape")
def scrape():
    
    mars_data = client.db.Mars_db
    mars_sraping = scrape_mars.scrape()
    mars.update({}, mars_sraping, upsert = True)

    return redirect("/")

if __name__ == "__main__":
    
    app.run(debug=True)



