# AWSGeolocation
Provide an address and get few parts of the Address (It uses Google API)

## User Guide 
### Using Web service
1) Please go to this URL 
        https://mns-lambda-api.s3.us-east-2.amazonaws.com/index.html 
2) Provide an address and click on "Find State" . It will return the State , Latitude and Longitude

### Using Postman
1) Please use GET method with site URL as
        https://r0j1b44db9.execute-api.us-east-2.amazonaws.com/default/GetStateFromAddress 
2) Provide a key value pair as "addr" and your choice of address and SEND the request
3) It will return the State , Latitude and Longitude

### Sample Input and Outputs
  
  a) 2900 Westside Pkwy , 30005" will return 
            "[{'Input':'2900 Westside Pkwy , 30005','State':'Georgia','Latitude':34.0860298,'Longitude':-84.2740195}]"
          
  b) "Calcutta University" will return 
            "[{'Input':'Calcutta University','State':'West Bengal','Latitude':22.5750862,'Longitude':88.3629188}]"
          
  c) "Orlando fl" will return
            "[{'Input':'orlando fl','State':'Florida','Latitude':28.5383355,'Longitude':-81.3792365}]"

### Steps Involved
1) Receive Address from User and pass it to teh AWS API Gateway
2) API Gateway in turn invokes a Lambda Function (Python) - Please refer to the code file function.py
3) Inside Lambda function it calls Google Geocoding API and parses the result into State, Latitude and Longitude
4) These values are returned to the calling client. 

** Note : The State is supposed to be obtained from a POSTGIS database using thhe Latitude and Longitude obtained from Google API call. For this purpose a PostgreSQL database has been set up in AWS and has been enabled with extension POSTGIS . The dataset tl_2019_us_state.shp has been obtained for this purpose from https://www.census.gov/programs-surveys/geography.html . This shape file has been loaded into the POSTGIS enables PostgreSQL database. Due to some technical challengel with this data the State could not be identified from this dataset . So as a temporary measure , the State has been obtained from Google API . This is not the right way as , google is not the authority for state borders . The Government data is more reliable for this purpose . We will continue to work on this and fix this problem .
