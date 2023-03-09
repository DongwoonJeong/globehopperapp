#Starting point of our WebApp - main
#pip install Flask
from flask import Flask, request, jsonify
import country
import city

#Using Flask framework
app = Flask(__name__)

#Countries API
#Create country
@app.post('/countries')
def createcountry():
    data=request.json
    return country.createcountryController(data)

#Read country
@app.get('/countries')
def getallcountries():
    return country.allcountriesController()

#Read country by continent.
@app.get('/countries/<continent>')
def getcountriesbyContinent(continent):
    return country.getcountriesbyContinentController(continent)

#get details about the capital city of the country
#error fixed. originally, /<country>/1 throws error because python does not know what to point. country.py ? or what.
@app.get('/countries/<countryname>/1')
def getcapitalCityDetails(countryname):
    return country.getcapitalCityDetailsController(countryname)

#Update country
@app.put('/countries/<int:id>')
def updatecountries(id):
    data=request.json
    return country.updatecountriesController(id, data)

#Delete country
@app.delete('/countries/<int:id>')
def deletecountries(id):
    return country.deletecountriesController(id)




#API for Cities
#Create = POST API
@app.post('/cities')
def createcity():
    data=request.json
    return city.createcityController(data)

#Read API
@app.get('/cities')
def allcities():
    return city.allcitiesController()

#Update API
@app.put('/cities/<int:id>')
def updatecities(id):
    data=request.json
    return city.updatecitiesController(id, data)

#Delete API
@app.delete('/cities/<int:id>')
def deletecities(id):
    return city.deletecitiesController(id)

#Execute as a script.
if __name__ == '__main__':
    app.run(debug=True)