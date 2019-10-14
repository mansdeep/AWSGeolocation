import googlemaps
from datetime import datetime
#import requests 

def lambda_handler(event, context):
    print("In lambda handler")
    Param = event['queryStringParameters']['addr']     
    print('Input Address:', Param)
    Result=GetSate(Param)
    State = Result['State']
    Latitude = Result['Latitude']
    Longitude = Result['Longitude']
    resp = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": "[{'Input':'" + Param + "','State':'" + State + "','Latitude':" + str(Latitude) + ",'Longitude':" + str(Longitude) + "}]"
    }

    return resp

def GetSate(address):
    gmaps = googlemaps.Client(key='YOUR GOOGLE API KEY HERE') 

# Geocoding an address
    geocode_result2= gmaps.geocode(address)
    print('********Geocode Result********')
    print(geocode_result2)
    item = geocode_result2[0]
    AddressComponents = item['address_components']
    print('********Address Components********')
    print(AddressComponents)
    for AddressComponent in AddressComponents:
        print('Component Type : ',AddressComponent['types'][0])
        if AddressComponent['types'][0] == 'administrative_area_level_1':
            print('Assigned the State')
            State = AddressComponent['long_name']
            print('State:',State)
        
    Geometry = item['geometry']
    print('********Geometry Result********')
    print(Geometry)
    Latitude = Geometry['location']['lat']
    Longitude = Geometry['location']['lng']
    print('Latitude:',Latitude)
    print('Longitude:',Longitude)
    return {'State' : State,'Latitude' : Latitude,'Longitude' : Longitude}