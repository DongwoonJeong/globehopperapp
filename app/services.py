#define all services for country.

from flask import Flask,request,jsonify
import conn



#Create API service
def createcountryService(data):
    #open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    countryid=data['CountryId']
    name=data['Name']
    population=data['Population']
    continent=data['Continent']
    #Execute the SQL
    mysql = "INSERT INTO Country (Name, Population, Continent) VALUES (%s, %s, %s)"
    values=(name,population,continent)
    mycursor.execute(mysql, values)

    #Close connection
    mycursor.close()
    conn.myconn.close()

#Read API service
#get all data records from table using sql
def allcountriesService():
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

#Update API service
def updatecountriesService(id, data):
    #open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    countryid=id
    name=data['Name']
    population=data['Population']
    continent=data['Continent']
    #Execute the SQL
    mysql = "UPDATE Country SET Name=%s, Population=%s, Continent=%s WHERE CountryId=%s"
    values=(name,population,continent,countryid)
    mycursor.execute(mysql, values)

    #Close connection
    mycursor.close()
    conn.myconn.close()


#Delete API service

def deletecountriesService(id):
    #open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Execute the SQL
    countryid=[id]
    mysql = "DELETE FROM Country WHERE CountryId=%s"
    mycursor.execute(mysql, countryid)

    #Close connection
    mycursor.close()
    conn.myconn.close()





#CIty APIs

#Create API service
def createcityService(data):
    #open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()
    
    name=data['Name']
    countryid=data['CountryId']
    capital=data['Capital']
    firstlandmark=data['FirstLandmark']
    secondlandmark=data['SecondLandmark']
    thirdlandmark=data['ThirdLandmark']
    #Execute the SQL
    mysql = "INSERT INTO City (Name, CountryId, Capital, FirstLandmark, SecondLandmark, ThirdLandmark) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (name,countryid,bool(capital),firstlandmark,secondlandmark,thirdlandmark)
    mycursor.execute(mysql, values)

    #Close connection
    mycursor.close()
    conn.myconn.close()

#Read API service
#get all data records from table using sql
def allcitiesService():
    #open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Execute the SQL
    mycursor.execute("SELECT * FROM City")
    results = mycursor.fetchall()
    #Close connection
    mycursor.close()
    conn.myconn.close()

    return results

#Update API service
def updatecitiesService(id, data):
    #open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    cityid=id
    name=data['Name']
    countryid=data['CountryId']
    capital=data['Capital']
    firstlandmark=data['FirstLandmark']
    secondlandmark=data['SecondLandmark']
    thirdlandmark=data['ThirdLandmark']
    #Execute the SQL
    mysql = "UPDATE City SET Name=%s, CountryId=%s, Capital=%s, FirstLandmark=%s, SecondLandmark=%s, ThirdLandmark=%s WHERE CityId=%s"
    #"UPDATE Country SET Name=%s, Population=%s, Continent=%s WHERE CountryId=%s"
    values=(name,countryid,capital,firstlandmark,secondlandmark,thirdlandmark,cityid)
    mycursor.execute(mysql, values)

    #Close connection
    mycursor.close()
    conn.myconn.close()


#Delete API service

def deletecitiesService(id):
    #open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Execute the SQL
    cityid=[id]
    mysql = "DELETE FROM City WHERE CityId=%s"
    mycursor.execute(mysql, cityid)

    #Close connection
    mycursor.close()
    conn.myconn.close()