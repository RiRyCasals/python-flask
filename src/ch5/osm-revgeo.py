import geocoder

pos = (35.659025, 139.745025)

g = geocoder.osm(pos, method='reverse')

print('County', g.country)
print('State', g.state)
print('City', g.city)
print('Street', g.street)
