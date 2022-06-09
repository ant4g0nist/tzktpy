# swagger_client.ConstantsApi

All URIs are relative to *https://api.tzkt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**constants_get**](ConstantsApi.md#constants_get) | **GET** /v1/constants | Get global constants
[**constants_get_by_address**](ConstantsApi.md#constants_get_by_address) | **GET** /v1/constants/{address} | Get global constant by address
[**constants_get_count**](ConstantsApi.md#constants_get_count) | **GET** /v1/constants/count | Get global constants count

# **constants_get**
> list[Constant] constants_get(address=address, creation_level=creation_level, creation_time=creation_time, creator=creator, refs=refs, size=size, select=select, sort=sort, offset=offset, limit=limit, format=format)

Get global constants

Returns a list of global constants.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConstantsApi()
address = swagger_client.Address() # Address | Filters constants by global address (starts with `expr..`). (optional)
creation_level = swagger_client.CreationLevel() # CreationLevel | Filters constants by creation level. (optional)
creation_time = swagger_client.CreationTime() # CreationTime | Filters constants by creation time. (optional)
creator = swagger_client.Creator() # Creator | Filters constants by creator. (optional)
refs = swagger_client.Refs() # Refs | Filters constants by number of refs. (optional)
size = swagger_client.Size() # Size | Filters constants by size in bytes. (optional)
select = swagger_client.Select7() # Select7 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort12() # Sort12 | Sorts delegators by specified field. Supported fields: `id` (default), `creationLevel`, `size`, `refs`. (optional)
offset = swagger_client.Offset10() # Offset10 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
format = 0 # int | Constant value format (`0` - micheline, `1` - michelson, `2` - bytes (base64)) (optional) (default to 0)

try:
    # Get global constants
    api_response = api_instance.constants_get(address=address, creation_level=creation_level, creation_time=creation_time, creator=creator, refs=refs, size=size, select=select, sort=sort, offset=offset, limit=limit, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConstantsApi->constants_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | [**Address**](.md)| Filters constants by global address (starts with &#x60;expr..&#x60;). | [optional] 
 **creation_level** | [**CreationLevel**](.md)| Filters constants by creation level. | [optional] 
 **creation_time** | [**CreationTime**](.md)| Filters constants by creation time. | [optional] 
 **creator** | [**Creator**](.md)| Filters constants by creator. | [optional] 
 **refs** | [**Refs**](.md)| Filters constants by number of refs. | [optional] 
 **size** | [**Size**](.md)| Filters constants by size in bytes. | [optional] 
 **select** | [**Select7**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort12**](.md)| Sorts delegators by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;creationLevel&#x60;, &#x60;size&#x60;, &#x60;refs&#x60;. | [optional] 
 **offset** | [**Offset10**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **format** | **int**| Constant value format (&#x60;0&#x60; - micheline, &#x60;1&#x60; - michelson, &#x60;2&#x60; - bytes (base64)) | [optional] [default to 0]

### Return type

[**list[Constant]**](Constant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **constants_get_by_address**
> Constant constants_get_by_address(address, format=format)

Get global constant by address

Returns global constant with specified address (expression hash).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConstantsApi()
address = 'address_example' # str | Global address (starts with `expr..`)
format = 0 # int | Constant value format (`0` - micheline, `1` - michelson, `2` - bytes (base64)) (optional) (default to 0)

try:
    # Get global constant by address
    api_response = api_instance.constants_get_by_address(address, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConstantsApi->constants_get_by_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Global address (starts with &#x60;expr..&#x60;) | 
 **format** | **int**| Constant value format (&#x60;0&#x60; - micheline, &#x60;1&#x60; - michelson, &#x60;2&#x60; - bytes (base64)) | [optional] [default to 0]

### Return type

[**Constant**](Constant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **constants_get_count**
> int constants_get_count(refs=refs)

Get global constants count

Returns a number of global constants.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConstantsApi()
refs = swagger_client.Refs1() # Refs1 | Filters constants by number of refs. (optional)

try:
    # Get global constants count
    api_response = api_instance.constants_get_count(refs=refs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConstantsApi->constants_get_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refs** | [**Refs1**](.md)| Filters constants by number of refs. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

