#define all functions related to Country APIs.

from flask import Flask, request, jsonify
import services

#Function to get all countries and return as json object.
def allCountries():
    results= services.allCountries()
    return jsonify(results)