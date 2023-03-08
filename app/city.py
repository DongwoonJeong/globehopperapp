#define all functions related to Country APIs.

from flask import Flask, request, jsonify
import services



#Create city
def createcity(data):
    services.createcity(data)
    return jsonify({'message':'Data inserted successfully'})

#Read city
def allcities():
    results= services.allcities()
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
def updatecities(id, data):
    services.updatecities(id, data)
    return jsonify({'message':'city updateed successfully'})

#Delete API
def deletecities(id):
    services.deletecities(id)
    return jsonify({'message':'city delete successfully'})