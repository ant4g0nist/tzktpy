# swagger_client.SoftwareApi

All URIs are relative to *https://api.tzkt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**software_get**](SoftwareApi.md#software_get) | **GET** /v1/software | Get baker software
[**software_get_count**](SoftwareApi.md#software_get_count) | **GET** /v1/software/count | Get software count

# **software_get**
> list[Software] software_get(select=select, sort=sort, offset=offset, limit=limit)

Get baker software

Returns a list of baker software.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareApi()
select = swagger_client.Select39() # Select39 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort46() # Sort46 | Sorts delegators by specified field. Supported fields: `id` (default), `firstLevel`, `lastLevel`, `blocksCount`. (optional)
offset = swagger_client.Offset44() # Offset44 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)

try:
    # Get baker software
    api_response = api_instance.software_get(select=select, sort=sort, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->software_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | [**Select39**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort46**](.md)| Sorts delegators by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;firstLevel&#x60;, &#x60;lastLevel&#x60;, &#x60;blocksCount&#x60;. | [optional] 
 **offset** | [**Offset44**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]

### Return type

[**list[Software]**](Software.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_get_count**
> int software_get_count()

Get software count

Returns a number of software.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareApi()

try:
    # Get software count
    api_response = api_instance.software_get_count()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->software_get_count: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

