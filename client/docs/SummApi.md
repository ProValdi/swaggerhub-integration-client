# swagger_client.SummApi

All URIs are relative to *https://virtserver.swaggerhub.com/ProValdi/test-integrations/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**do_action**](SummApi.md#do_action) | **POST** /operate | operate 2 numbers
[**get_results**](SummApi.md#get_results) | **GET** /results | Get previous results


# **do_action**
> do_action(body)

operate 2 numbers



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: petstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SummApi(swagger_client.ApiClient(configuration))
body = swagger_client.Nums() # Nums | 2 numbers to operate with

try:
    # operate 2 numbers
    api_instance.do_action(body)
except ApiException as e:
    print("Exception when calling SummApi->do_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Nums**](Nums.md)| 2 numbers to operate with | 

### Return type

void (empty response body)

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_results**
> list[Results] get_results()

Get previous results

Multiple status values can be provided with comma separated strings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: petstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SummApi(swagger_client.ApiClient(configuration))

try:
    # Get previous results
    api_response = api_instance.get_results()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummApi->get_results: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Results]**](Results.md)

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

