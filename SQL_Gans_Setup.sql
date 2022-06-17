CREATE DATABASE gans;
USE gans;


CREATE TABLE IF NOT EXISTS cities (
	city_id INT,
    city VARCHAR(200),
    country VARCHAR(200),
    country_code CHAR(2),
    population INT,
    time_zone INT,
    latitude FLOAT,
    longitude FLOAT,
   	PRIMARY KEY(city_id)
);

SELECT * FROM cities;
#DROP TABLE cities;

CREATE TABLE IF NOT EXISTS weathers (
	weather_id INT auto_increment,
    city_id INT,
    time_utc INT,
    local_time CHAR(20),
    temperature FLOAT,
    humidity FLOAT,
    cloudiness_pc INT,
    wind_speed FLOAT,
    precipitation_prob FLOAT,
    rain_volume FLOAT,
    snow_volume FLOAT,
    PRIMARY KEY(weather_id),
    FOREIGN KEY(city_id) REFERENCES cities(city_id)
);

SELECT * FROM weathers;
#DROP TABLE weathers;


CREATE TABLE IF NOT EXISTS airports (
	city_id INT,
    lat FLOAT,
    lon FLOAT,
    icao CHAR(4),
    iata CHAR(3),
    name VARCHAR(200),
    PRIMARY KEY(icao),
    FOREIGN KEY(city_id) REFERENCES cities(city_id)
);

SELECT * FROM airports;
#DROP TABLE airports;



CREATE TABLE IF NOT EXISTS flights (
	flights_id INT auto_increment,
    icao CHAR(4),
    date CHAR(10),
    hour_day CHAR(5),
    num_of_arriv INT,
    num_of_depart INT,
    PRIMARY KEY(flights_id),
    FOREIGN KEY(icao) REFERENCES airports(icao)
);

SELECT * FROM flights;
#DROP TABLE flights;