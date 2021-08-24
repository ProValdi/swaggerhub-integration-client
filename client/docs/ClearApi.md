# swagger_client.ClearApi

All URIs are relative to *http://localhost:8080/server/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_results**](ClearApi.md#delete_results) | **GET** /clear | clear list of requests

# **delete_results**
> str delete_results()

clear list of requests

clear list of requests

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClearApi()

try:
    # clear list of requests
    api_response = api_instance.delete_results()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClearApi->delete_results: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

