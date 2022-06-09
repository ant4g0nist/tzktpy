# swagger_client.DelegatesApi

All URIs are relative to *https://api.tzkt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delegates_get**](DelegatesApi.md#delegates_get) | **GET** /v1/delegates | Get delegates
[**delegates_get_by_address**](DelegatesApi.md#delegates_get_by_address) | **GET** /v1/delegates/{address} | Get delegate by address
[**delegates_get_count**](DelegatesApi.md#delegates_get_count) | **GET** /v1/delegates/count | Get delegates count

# **delegates_get**
> list[Delegate] delegates_get(active=active, last_activity=last_activity, select=select, sort=sort, offset=offset, limit=limit)

Get delegates

Returns a list of delegate accounts.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DelegatesApi()
active = swagger_client.Active() # Active | Delegate status to filter by (true - only active, false - only deactivated, undefined - all delegates) (optional)
last_activity = swagger_client.LastActivity2() # LastActivity2 | Filters delegates by last activity level (where the delegate was updated) (optional)
select = swagger_client.Select15() # Select15 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort21() # Sort21 | Sorts delegators by specified field. Supported fields: `id` (default), `activationLevel`, `deactivationLevel`, `stakingBalance`, `balance`, `numDelegators`. (optional)
offset = swagger_client.Offset19() # Offset19 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)

try:
    # Get delegates
    api_response = api_instance.delegates_get(active=active, last_activity=last_activity, select=select, sort=sort, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelegatesApi->delegates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | [**Active**](.md)| Delegate status to filter by (true - only active, false - only deactivated, undefined - all delegates) | [optional] 
 **last_activity** | [**LastActivity2**](.md)| Filters delegates by last activity level (where the delegate was updated) | [optional] 
 **select** | [**Select15**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort21**](.md)| Sorts delegators by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;activationLevel&#x60;, &#x60;deactivationLevel&#x60;, &#x60;stakingBalance&#x60;, &#x60;balance&#x60;, &#x60;numDelegators&#x60;. | [optional] 
 **offset** | [**Offset19**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]

### Return type

[**list[Delegate]**](Delegate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delegates_get_by_address**
> Delegate delegates_get_by_address(address)

Get delegate by address

Returns a delegate with the specified address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DelegatesApi()
address = 'address_example' # str | Delegate address (starting with tz)

try:
    # Get delegate by address
    api_response = api_instance.delegates_get_by_address(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelegatesApi->delegates_get_by_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Delegate address (starting with tz) | 

### Return type

[**Delegate**](Delegate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delegates_get_count**
> int delegates_get_count(active=active)

Get delegates count

Returns a number of delegate accounts.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DelegatesApi()
active = swagger_client.Active1() # Active1 | Delegate status to filter by (true - only active, false - only deactivated, undefined - all delegates) (optional)

try:
    # Get delegates count
    api_response = api_instance.delegates_get_count(active=active)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DelegatesApi->delegates_get_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | [**Active1**](.md)| Delegate status to filter by (true - only active, false - only deactivated, undefined - all delegates) | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

