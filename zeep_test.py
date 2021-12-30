import pretend  # pip install pretend

from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.transports import Transport

# Replace YOUR-WSDL and OPERATION_NAME with the wsdl url
# and the method name you are calling. The response
# needs to be set in the content=""" """ var.
user = ""
pwd = ""

with open('raw_1.xml') as f:
    content = f.read()

session = Session()
session.auth = HTTPBasicAuth(username=user, password=pwd)
client = Client('https://webservices.fieldforcemanager.com/services/services/JobService-wrapped-0.0.5?wsdl', transport=Transport(session=session))
response = pretend.stub(
    status_code=200,
    headers={},
    content=bytes(content, 'utf-8'))

operation = client.service._binding._operations['getJobs']
result = client.service._binding.process_reply(
    client, operation, response)

print(result)
