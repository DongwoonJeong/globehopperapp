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
