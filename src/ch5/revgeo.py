import reverse_geocode

coords = [(35.659025, 139.74505)]

areas = reverse_geocode.search(coords)
print('Coord: ', coords[0])
print('Country: ', areas[0]['country'])
print('City: ', areas[0]['city'])
