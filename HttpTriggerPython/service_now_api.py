#Need to install requests package for python
import requests
# Set the request parameters
url = ''
# Eg. User name="username", Password="password" for this code sample.
user = ''
pwd = ''
# Set proper headers
headers = {"Content-Type":"application/xml","Accept":"application/json"}
# Do the HTTP request
response = requests.post(url, auth=(user, pwd), headers=headers,data="<request><entry><short_description>Creating Service Now ticket using Python Function</short_description><assignment_group>test</assignment_group><urgency>2</urgency><impact>2</impact><description>Creating Ticket using python api</description><caller_id>arshad</caller_id></entry></request>")
# Check for HTTP codes other than 201
if response.status_code != 201: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
    exit()
# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)

