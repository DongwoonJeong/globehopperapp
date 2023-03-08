#Starting point of our WebApp - main
#pip install Flask
from flask import Flask, request, jsonify
import country

#Using Flask framework
app = Flask(__name__)

#Create = POST API
@app.post('/countries')
def createcountry():
    data=request.json
    return country.createcountry(data)

#Read API
@app.get('/countries')
def getallcountries():
    return country.allcountries()


#Execute as a script.
if __name__ == '__main__':
    app.run(debug=True)