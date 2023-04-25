import mysql.connector
from WeatherModel import Weather


class WeatherRepository:
    def __init__(self, host: str,user: str, password: str, database: str):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )


    def insert_weather_to_db(self,weather:Weather):
        cursor = self.connection.cursor()
        params = (weather.city, weather.temperature, weather.description, weather.humidity,)
        query = "INSERT INTO weather_data(city,temperature,description,humidity) VALUES(%s,%s,%s,%s)"
        cursor.execute(query,params)
        self.connection.commit()

        cursor.close()


    def select_weather_from_db(self,city: str):
        cursor = self.connection.cursor()
        params = (city,)
        query = "SELECT * FROM weather_data WHERE city= %s"
        cursor.execute(query,params)
        result = cursor.fetchone()

        if result is None:
            return None
        else:
            weather = Weather(city=result[0], temperature=result[1], description=result[2], humidity=result[3])
        return weather


