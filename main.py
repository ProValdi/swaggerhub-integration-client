from __future__ import print_function
import time
import client.swagger_client as cli
from client.swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: petstore_auth
configuration = cli.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = cli.SummApi(cli.ApiClient(configuration))
body = cli.Nums()  # Nums | 2 numbers to operate with

try:
    # operate 2 numbers
    api_instance.do_action(body)
except ApiException as e:
    print("Exception when calling SummApi->do_action: %s\n" % e)

