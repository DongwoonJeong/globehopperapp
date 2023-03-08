#define all functions related to Country APIs.

from flask import Flask, request, jsonify
import services

#Function to get all countries and return as json object.
def allCountries():
    results= services.allCountries()
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

#Create country
def createCountry(data):
    services.createCountry(data)
    return jsonify({'message':'Data inserted successfully'})