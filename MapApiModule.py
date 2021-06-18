import openrouteservice as ors
import folium
import urllib
import config
import logging
import logger_config
import webbrowser


log = logging.getLogger(__name__)
log.info("Entered module: %s" % __name__)

try:
    client = ors.Client(key=config.key)  # global variable client
except ValueError as e:
    logging.debug(e)
    client = None


def _get_location(location_text):
    """Used to preprocess the input location_text for URL encoding.
    Doesn't do much right now. But provides a place to add such steps in future.
    """
    return location_text.strip().lower()


@logger_config.logger
def direction(origin, destination):
    result = client.directions(origin, destination)
    logging.debug("Summary: " + result[0]["summary"])

    def geo(location)  :  
        m = folium.Map(tiles='cartodbpositron', zoom_start=13)

        address = location

        geocode = client.pelias_search(
            text=address,
            focus_point=list(reversed(m.location)),
            validate=False,
        )

        for result in geocode['features']:
            folium.Marker(
                location=list(reversed(result['geometry']['coordinates'])),
                icon=folium.Icon(icon='compass', color='green', prefix='fa'),
                popup=folium.Popup(result['properties']['name'])
            ).add_to(m)
            # print(list(reversed(result['geometry']['coordinates'])))
            break
        return list((result['geometry']['coordinates']))
       
    m = folium.Map()
    coordinates = [geo(origin),geo(destination)]
    route = client.directions(
        coordinates=coordinates,
        profile='foot-walking',
        format='geojson',
        options={"avoid_features": ["steps"]},
        validate=False,
    )
    folium.PolyLine(locations=[list(reversed(coord)) 
                            for coord in 
                            route['features'][0]['geometry']['coordinates']]).add_to(m)
        
    m.save("mymap.html")
    webbrowser.open("mymap.html")
    # return [origin,destination]
    


@logger_config.logger
def timezone(search_location):
    result = client.geocode(search_location)
    logging.debug("Formatted Address: " + result[0]["formatted_address"])
    latlng = (
        result[0]["geometry"]["location"]["lat"],
        result[0]["geometry"]["location"]["lng"],
    )
    logging.debug(f"Latitude: {latlng[0]} Longitude: {latlng[1]}")
    timezone = client.timezone(latlng)
    timeZoneId = timezone["timeZoneId"]
    import pytz

    tz_obj = pytz.timezone(timeZoneId)
    current_time = pytz.datetime.datetime.now(tz=tz_obj)
    time_in_timezone = pytz.datetime.datetime.strftime(
        current_time, "%a, %d %b %Y %H:%M:%S %Z"
    )
    return timeZoneId, time_in_timezone


@logger_config.logger
def geocoding(search_location):
    m = folium.Map()
    address = search_location
    geocode = client.pelias_search(
        text=address,
        focus_point=list(reversed(m.location)),
        validate=False,
    )
    for result in geocode['features']:
        folium.Marker(
            location=list(reversed(result['geometry']['coordinates'])),
            icon=folium.Icon(icon='compass', color='green', prefix='fa'),
            popup=folium.Popup(result['properties']['name']),
            tiles='cartodbpositron', zoom_start=13
        ).add_to(m)
        break
    m.save("mymap.html")
    webbrowser.open("mymap.html")
    return list((result['geometry']['coordinates']))


@logger_config.logger
def elevation(search_location):
    result = client.geocode(search_location)
    latlng = (
        result[0]["geometry"]["location"]["lat"],
        result[0]["geometry"]["location"]["lng"],
    )
    result = client.elevation(latlng)
    result_value = result[0]["elevation"]
    position = "above" if result_value > 0 else "below"
    logging.debug(
        f"{search_location} is {round(result_value,2)} metres {position} sea level"
    )
    return str(result_value) + " metres"


@logger_config.logger
def places(search_location):
    locations = client.places(search_location)
    N = 3
    place_details = {}
    try:
        filtered_locations = sorted(
            locations["results"],
            key=lambda loc: (loc["user_ratings_total"], loc["rating"]),
            reverse=True,
        )[:N]
    except Exception:
        filtered_locations = locations["results"]
    logging.debug(filtered_locations)
    first_N_places = {res["name"]: res["place_id"] for res in filtered_locations}
    for name, place_id in first_N_places.items():
        place_details[name] = client.place(place_id)["result"]["url"]
    return place_details
