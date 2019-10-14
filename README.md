# AWSGeolocation
Provide an address and get few parts of the Address (It uses Google API)

## User Guide 
### Using Web service
1) Please go to this [URL](https://mns-lambda-api.s3.us-east-2.amazonaws.com/index.html)
2) Provide an address and click on "Find State" . It will return the State , Latitude and Longitude

### Using Postman
1) Please use GET method with site URL as
        https://r0j1b44db9.execute-api.us-east-2.amazonaws.com/default/GetStateFromAddress 
2) Provide a key value pair as "addr" and your choice of address and SEND the request
3) It will return the State , Latitude and Longitude

### Sample Input and Outputs
  
  Input 2900 Westside Pkwy , 30005" will return 
            "[{'Input':'2900 Westside Pkwy , 30005','State':'Georgia','Latitude':34.0860298,'Longitude':-84.2740195}]"
          
  b) "Calcutta University" will return 
            "[{'Input':'Calcutta University','State':'West Bengal','Latitude':22.5750862,'Longitude':88.3629188}]"
          
  c) "Orlando fl" will return
            "[{'Input':'orlando fl','State':'Florida','Latitude':28.5383355,'Longitude':-81.3792365}]"


## Steps Involved
- Receive Address from User and pass it to teh AWS API Gateway
- API Gateway in turn invokes a Lambda Function (Python) - Please refer to the code file function.py
- Inside Lambda function it calls Google Geocoding API and parses the result into State, Latitude and Longitude
- These values are returned to the calling client. 

## Note 
The plan for this project is to obtain State using [US State shapefile](https://www.census.gov/programs-surveys/geography.html).  As this is authentic dataset containing information on State borders. The shape file has been loaded into the POSTGIS enables PostgreSQL database in AWS. But, due to some technical difficulty with this dataset the State can't be identified from Latitude and Longitude at the moment. So as a temporary solution, the State has been obtained from Google API. This is not the right way as, google is not the authority for state borders. We will continue to work on this and fix this problem .
