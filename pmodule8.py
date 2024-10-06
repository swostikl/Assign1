# 1.Write a program that asks the user to enter the ICAO code of an airport. The program fetches
# and prints out the corresponding airport name and location (town) from the airport database used
# on this course. The ICAO codes are stored in the ident column of the airport table.


import mysql.connector
from geopy.distance import geodesic


connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database='flight_game',
    user='swosti',
    password='Amazol12',
    autocommit=True,
    charset="utf8mb4",
    collation="utf8mb4_general_ci"
    )
cursor = connection.cursor()
def get_airport_by_icao_code():
    icoa= input("Enter icoa code: ").upper()
    sql='SELECT name, municipality from airport where ident=%s'
    cursor.execute(sql,(icoa,))
    result=cursor.fetchall()
    if len(result)==1:
        print(f'name: {result[0][0]}')
        print(f'municipality: {result[0][1]}')
get_airport_by_icao_code()

# 2.Write a program that asks the user to enter the area code (for example FI) and prints out the airports
# located in that country ordered by airport type. For example, Finland has 65 small airports, 15
# helicopter airports and so on.


connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database='flight_game',
    user='swosti',
    password='Amazol12',
    autocommit=True,
    charset="utf8mb4",
    collation="utf8mb4_general_ci"
    )

cursor = connection.cursor()
def get_air_by_area_code():
    iso_country = input("ISO country code: ").upper()
    sql = 'SELECT name, type FROM airport WHERE iso_country = %s ORDER BY type'
    cursor.execute(sql, (iso_country, ))
    response = cursor.fetchall()
    if len(response) > 0:
        for airport in response:
            print(f"name: {airport[0]}, type: {airport[1]}")


get_air_by_area_code()


# 3.Write a program that asks the user to enter the ICAO codes of two airports. The program prints out the
# distance between the two airports in kilometers. The calculation is based on the airport coordinates
# fetched from the database. Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/.
# Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE, write geopy into the
# search field and finish the installation.


connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database='flight_game',
    user='swosti',
    password='Amazol12',
    autocommit=True,
    charset="utf8mb4",
    collation="utf8mb4_general_ci"
    )
cursor=connection.cursor()
def get_ai_icao_code():
    icao_code1 = input("Enter ICAO code 1 : ").upper()
    icao_code2 = input("Enter ICAO code 2: ").upper()
    sql = 'SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s OR ident = %s'
    cursor.execute(sql, (icao_code1, icao_code2))
    response = cursor.fetchall()
    if len(response) == 2:
        latitude1 = response[0][0]
        longitude1 = response[0][1]
        latitude2 = response[1][0]
        longitude2 = response[1][1]
        location1 = (latitude1, longitude1)
        location2 = (latitude2, longitude2)
        distance = geodesic(location1, location2).km
        print(f"distance: {distance} km")


get_ai_icao_code()