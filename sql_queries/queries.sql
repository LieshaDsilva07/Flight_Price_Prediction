-- 1. Average price per airline
SELECT Airline, AVG(Price) AS avg_price
FROM data_train
GROUP BY Airline;

-- 2. Number of flights from each source
SELECT Source, COUNT(*) AS total_flights
FROM data_train
GROUP BY Source;

-- 3. Top 5 most expensive flights
SELECT *
FROM data_train
ORDER BY Price DESC
LIMIT 5;

-- 4. Average price by number of stops
SELECT Total_Stops, COUNT(*) AS total, AVG(Price) AS avg_price
FROM data_train
GROUP BY Total_Stops;

-- 5. Flights count per airline and source
SELECT Airline, Source, COUNT(*) AS num_flights
FROM data_train
GROUP BY Airline, Source
ORDER BY num_flights DESC;

-- 6. Average duration by airline (requires cleaned duration column in minutes)
SELECT Airline, AVG(Duration_in_minutes) AS avg_duration
FROM data_train
GROUP BY Airline
ORDER BY avg_duration DESC;

-- 7. Flights with more than one stop and price > 10,000
SELECT *
FROM data_train
WHERE Total_Stops != 'non-stop' AND Price > 10000
ORDER BY Price DESC;

-- 8. Average price by route
SELECT Route, COUNT(*) AS num_flights, AVG(Price) AS avg_price
FROM data_train
GROUP BY Route
ORDER BY avg_price DESC
LIMIT 10;

-- 9. Price trends by day of journey
SELECT DAY(Date_of_Journey) AS Day, AVG(Price) AS avg_price
FROM data_train
GROUP BY Day
ORDER BY Day;

-- 10. Flights by airline and number of stops
SELECT Airline, Total_Stops, COUNT(*) AS num_flights
FROM data_train
GROUP BY Airline, Total_Stops
ORDER BY num_flights DESC;

-- 11. Cheapest flight per airline
SELECT Airline, MIN(Price) AS cheapest_price
FROM data_train
GROUP BY Airline;

-- 12. Most common routes
SELECT Route, COUNT(*) AS route_count
FROM data_train
GROUP BY Route
ORDER BY route_count DESC
LIMIT 10;


