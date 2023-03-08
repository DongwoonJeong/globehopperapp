#define all functions related to Country APIs.

from flask import Flask, request, jsonify
import services



#Create city
def createcityController(data):
    services.createcityService(data)
    return jsonify({'message':'Data inserted successfully'})

#Read city
def allcitiesController():
    results= services.allcitiesService()
    data = []
    #Converted a list to dictionary
    for row in results:
        data.append({
            "CityId":row[0],
            "Name":row[1],
            "CountryId":row[2],
            "Capital":row[3],
            "FirstLandmark":row[4],
            "SecondLandmark":row[5],
            "ThirdLandmark":row[6]
        })
    return jsonify(data)

#Update API
def updatecitiesController(id, data):
    services.updatecitiesService(id, data)
    return jsonify({'message':'city updateed successfully'})

#Delete API
def deletecitiesController(id):
    services.deletecitiesService(id)
    return jsonify({'message':'city delete successfully'})