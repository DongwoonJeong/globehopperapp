#define all functions related to Country APIs.

from flask import Flask, request, jsonify
import services



#Create country
def createcountryController(data):
    services.createcountryService(data)
    return jsonify({'message':'Data inserted successfully'})



#Function to get all countries and return as json object.
#Read country
def allcountriesController():
    results= services.allcountriesService()
    data = []
    #Converted a list to dictionary
    for row in results:
        data.append({
            "CountryId":row[0],
            "Name":row[1],
            "Population":row[2],
            "Continent":row[3]
        })
    return jsonify(data)

#Update API
def updatecountriesController(id, data):
    services.updatecountriesService(id, data)
    return jsonify({'message':'country updateed successfully'})

#Delete API
def deletecountriesController(id):
    services.deletecountriesService(id)
    return jsonify({'message':'country delete successfully'})