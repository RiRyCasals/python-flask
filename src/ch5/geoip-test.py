import os
import geoip2.database

check_ip = '157.7.44.174'

path = os.path.dirname(__file__) + '/GeoLite2-City_20220329/GeoLite2-City.mmdb'
reader = geoip2.database.Reader(path)

rec = reader.city(check_ip)

print('IP: ', check_ip)
print('Country: ', rec.country.name)
print('City: ', rec.city.name)
print('Latitude: ', rec.location.latitude)
print('Longitude: ', rec.location.longitude)
