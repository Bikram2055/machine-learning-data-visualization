import phonenumbers
import folium
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

number = '+9779845216027'

scan = phonenumbers.parse(number)
your_location = geocoder.description_for_number(scan, 'en')
print(your_location)

service_provider = carrier.name_for_number(scan, 'en')
print(service_provider)

key = '718aa6de7df040188ccff3db605909bc'
geocode = OpenCageGeocode(key)

result = geocode.geocode(str(your_location))
print(result)

lat = result[0]["geometry"]['lat']
lng = result[0]['geometry']['lng']
print(lat, lng)


map = folium.Map(location=[lat, lng], zoom_start=12)
folium.Marker([lat, lng]).add_to(map)
map.save('tracked.html')
