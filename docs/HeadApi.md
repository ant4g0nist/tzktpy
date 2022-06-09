# swagger_client.HeadApi

All URIs are relative to *https://api.tzkt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**head_get**](HeadApi.md#head_get) | **GET** /v1/head | Get indexer head

# **head_get**
> State head_get()

Get indexer head

Returns indexer head and synchronization status.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HeadApi()

try:
    # Get indexer head
    api_response = api_instance.head_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeadApi->head_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**State**](State.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

