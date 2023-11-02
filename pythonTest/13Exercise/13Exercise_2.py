#Implement a backend service that gets the ICAO code of an airport
# and then returns the name and location of the airport in JSON format.
# The information is fetched from the airport database used on this course.
# For example, the GET request for EFHK would be: http://127.0.0.1:5000/airport/EFHK.
# The response must be in the format of: {"ICAO":"EFHK", "Name":"Helsinki-Vantaa Airport", "Location":"Helsinki"}.
import json

import mysql.connector
from flask import Flask, Response

app=Flask(__name__)
# app.config ['JSON_SORT_KEYS'] = False
@app.route('/airport/<ICAO>')
def getAirportInfo(ICAO):
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port="6033",
        database="flight_game",
        user="root",
        password="root",
        autocommit=True
    )
    cursor = connection.cursor()
    sql = "select ident,name,municipality from airport where ident='" + ICAO + "'"
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            response={
                "ICAO": row[0],
                "Name": row[1],
                "Location": row[2]
            }
            print(response)
            return Response(json.dumps(response),mimetype='application/json')

    else:
        print("there is no data")



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)