import math
# tee ratkaisu tänne
# Write your solution here
def get_station_data(filename: str) -> dict:
  station_location = {}
  with open(filename) as station_data:
    for line in station_data:
      line = line.strip()
      parts = line.split(";")
      if parts[0] == "Longitude":
        continue 
      lon = float(parts[0])
      lat = float(parts[1])
      name = parts[3]
      station_location[name] = (lon, lat)
  # print(station_location)
  return station_location

def distance(stations: dict, station1: str, station2: str) -> float:
  long1 = stations[station1][0]
  lat1 = stations[station1][1]

  long2 = stations[station2][0]
  lat2 = stations[station2][1]

  x_km = (long1 - long2) * 55.26
  y_km = (lat1 - lat2) * 111.2
  dist_km = math.sqrt(x_km**2 + y_km**2)

  return dist_km

def greatest_distance(stations: dict) -> tuple:
  station_names = []
  print(stations)
  greatest_dist = 0
  (stat1, stat2) = ("", "")
  station_names = list(stations)
  # for name in stations:
  #   station_names.append(name)
  # for i in range(len(station_names)):
  #   for j in range(i+1, len(station_names)):
  #     d = distance(stations, station_names[i], station_names[j])
  #     if d > greatest_dist:
  #       greatest_dist = d
  #       (stat1, stat2) = (station_names[i], station_names[j])
  # return (stat1, stat2, greatest_dist)
  print(station_names)



if __name__ == "__main__":
  # get_station_data("stations1.csv")
  stations = get_station_data('stations1.csv')
  # d = distance(stations, "Designmuseo", "Hietalahdentori")
  # print(d)
  # d = distance(stations, "Viiskulma", "Kaivopuisto")
  # print(d)
  greatest_distance(stations)
  # station1, station2, greatest = greatest_distance(stations)
  # print(station1, station2, greatest)
