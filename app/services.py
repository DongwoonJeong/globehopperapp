#define all services for country.

from flask import Flask,request,jsonify

import conn


#get all data records from table using sql
def allCountries():
    #open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Execute the SQL
    mycursor.execute("SELECT * FROM Country")
    results = mycursor.fetchall()
    #Close connection
    mycursor.close()
    conn.myconn.close()

    return results

def createCountry(data):
    #open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    countryId=data['CountryId']
    name=data['Name']
    population=data['Population']
    continent=data['Continent']
    #Execute the SQL
    mysql = mycursor.execute("INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (%s,%s,%s,%s)")
    values=(countryId,name,population,continent)
    mycursor.execute(mysql, values)

    #Close connection
    mycursor.close()
    conn.myconn.close()

