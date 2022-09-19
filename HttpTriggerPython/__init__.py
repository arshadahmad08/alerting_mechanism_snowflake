import logging
import azure.functions as func
import requests
import json
import os
import uuid

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
        
    user = os.getenv('snowflake_cdw_integration_username')
    pwd = os.getenv('snowflake_cdw_integration_password')
    url = os.getenv('snowflake_cdw_integration_url')

    #New code to fetch the json data attributes values
    try: 
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        input = req_body.get('data')
        for item in input:
            assignment_group = item[1]
            caller_id = item[2]
            error_msg = item[3]
            error_msg_details = item[4]
            urgency = str(item[5])
            impact = str(item[6])
            contact_type=  item[7]
            category= item[8]
            subcategory =  item[9]
            business_service = item[10]
            correlation_display=  item[11]
            correlation_id= item[12]
    
    #printing the values        
    print("urgency :",urgency)    
    print("impact :",impact)
    print("assignment_group :",assignment_group)
    print("caller_id :",caller_id)
    print("error_msg :",error_msg)
    print("error_msg_details :",error_msg_details)

    #generating the unique corelation id             

    # Set proper headers
    headers = {"Content-Type":"application/xml","Accept":"application/json"}

    # Do the HTTP request
    response = requests.post(url, auth=(user, pwd), headers=headers,data="<request><entry><short_description>"+error_msg+"</short_description><assignment_group>"+assignment_group+"</assignment_group><urgency>"+urgency+"</urgency><impact>"+impact+"</impact><description>"+error_msg_details+"</description><caller_id>"+caller_id+"</caller_id><contact_type>"+contact_type+"</contact_type><correlation_display>"+correlation_display+"</correlation_display><category>"+category+"</category><subcategory>"+subcategory+"</subcategory><business_service>"+business_service+"</business_service><correlation_id>"+correlation_id+"</correlation_id></entry></request>")

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    print(data)

    # Check for HTTP codes other than 201
    if response.status_code != 201: 
       return func.HttpResponse(" { \"data\" : [[ 0 , \"failure\" ]] }")
       print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
       exit()           
    else :
       #return func.HttpResponse(" { \"data\" : [[ 0,\"" + {response.status_code} + "\" ] ]}")
       return func.HttpResponse(" { \"data\" : [[ 0 , \"success\" ]] }")
