
# Write a program that asks the user to enter the ICAO code of an airport.
# The program fetches and prints out the corresponding airport name and location (town) from the airport database used on this course.
# The ICAO codes are stored in the ident column of the airport table.
#
import mysql.connector
connection=mysql.connector.connect(
    host="127.0.0.1",
    port="6033",
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)
cursor=connection.cursor()

ICAO=input("please enter the ICAO code:")
sql="select name,municipality from airport where ident='"+ICAO+"'"
cursor.execute(sql)
result=cursor.fetchall()
if cursor.rowcount>0:
    for row in result:
        print(f"the airport name is {row[0]} and location is {row[1]}")
else:print("there is no data")








# Write a program that asks the user to enter the area code (for example FI)
# and prints out the airports located in that country ordered by airport type.
# For example, Finland has 65 small airports, 15 helicopter airports and so on.
#

areaCode=input("please enter the area code: ")
sql1="select type,count(*) as cnt from airport where iso_country='"+areaCode+"' group by type order by type  "
cursor.execute(sql1)
result1=cursor.fetchall()
if cursor.rowcount>0:
    for result in result1:
        print(f"the {result[0]} airport count is {result[1]}")
else:print("there is no data")




# Write a program that asks the user to enter the ICAO codes of two airports.
# The program prints out the distance between the two airports in kilometers.
# The calculation is based on the airport coordinates fetched from the database.
# Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/.
# Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE,
# write geopy into the search field and finish the installation.

from geopy.distance import geodesic
ICAO1=input("please enter the first city ICAO: ")
ICAO2=input("please enter the second city ICAO: ")
airport1=()
airport2=()
sql="select ident,latitude_deg as lat,longitude_deg as lon from airport where ident in ('"+ICAO1+"','" +ICAO2+"')"

cursor.execute(sql)
result=cursor.fetchall()
if cursor.rowcount>0:
    for row in result:
        if row[0]==ICAO1:
            airport1=(row[1],row[2])
        else:airport2=(row[1],row[2])

    print(f"the distance of two airports is {geodesic(airport1,airport2).kilometers} km")
else:print("there is no data")

