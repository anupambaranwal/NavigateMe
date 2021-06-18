from herepy import GeocoderApi

geocoder_api = GeocoderApi(api_key="N1EmCfeAuuPNt4nedgHOL6v48tTkWHJmWzq-FXK5ekQ")

# geocodes given search text
response = geocoder_api.free_form("Ranchi")
print(response.as_dict())

# geocodes given search text with in given boundingbox
response = geocoder_api.address_with_boundingbox(
    searchtext="Ranchi",
    top_left=[42.3952, -71.1056],
    bottom_right=[42.3312, -71.0228],
)
print(response.as_dict())

# geocodes with given address details
response = geocoder_api.address_with_details(
    house_number=34, street="Barbaros", city="Istanbul", country="Turkey"
)
print(response.as_dict())

# geocodes with given street and city
response = geocoder_api.street_intersection(street="Barbaros", city="Istanbul")
print(response.as_dict())