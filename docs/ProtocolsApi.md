# swagger_client.ProtocolsApi

All URIs are relative to *https://api.tzkt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protocols_get**](ProtocolsApi.md#protocols_get) | **GET** /v1/protocols | Get protocols
[**protocols_get_by_code**](ProtocolsApi.md#protocols_get_by_code) | **GET** /v1/protocols/{code} | Get protocol by code
[**protocols_get_by_cycle**](ProtocolsApi.md#protocols_get_by_cycle) | **GET** /v1/protocols/cycles/{cycle} | Get protocol by cycle
[**protocols_get_by_hash**](ProtocolsApi.md#protocols_get_by_hash) | **GET** /v1/protocols/{hash} | Get protocol by hash
[**protocols_get_count**](ProtocolsApi.md#protocols_get_count) | **GET** /v1/protocols/count | Get protocols count
[**protocols_get_current**](ProtocolsApi.md#protocols_get_current) | **GET** /v1/protocols/current | Get current protocol

# **protocols_get**
> list[Protocol] protocols_get(sort=sort, offset=offset, limit=limit)

Get protocols

Returns a list of protocols.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProtocolsApi()
sort = swagger_client.Sort41() # Sort41 | Sorts protocols by specified field. Supported fields: `code` (default), `firstLevel`, `lastLevel`. (optional)
offset = swagger_client.Offset39() # Offset39 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)

try:
    # Get protocols
    api_response = api_instance.protocols_get(sort=sort, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->protocols_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | [**Sort41**](.md)| Sorts protocols by specified field. Supported fields: &#x60;code&#x60; (default), &#x60;firstLevel&#x60;, &#x60;lastLevel&#x60;. | [optional] 
 **offset** | [**Offset39**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]

### Return type

[**list[Protocol]**](Protocol.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protocols_get_by_code**
> Protocol protocols_get_by_code(code)

Get protocol by code

Returns a protocol with the specified proto code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProtocolsApi()
code = 56 # int | Protocol code (e.g. 4 for Athens, 5 for Babylon, etc)

try:
    # Get protocol by code
    api_response = api_instance.protocols_get_by_code(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->protocols_get_by_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **int**| Protocol code (e.g. 4 for Athens, 5 for Babylon, etc) | 

### Return type

[**Protocol**](Protocol.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protocols_get_by_cycle**
> Protocol protocols_get_by_cycle(cycle)

Get protocol by cycle

Returns a protocol at the specified cycle.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProtocolsApi()
cycle = 56 # int | Cycle index

try:
    # Get protocol by cycle
    api_response = api_instance.protocols_get_by_cycle(cycle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->protocols_get_by_cycle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cycle** | **int**| Cycle index | 

### Return type

[**Protocol**](Protocol.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protocols_get_by_hash**
> Protocol protocols_get_by_hash(hash)

Get protocol by hash

Returns a protocol with the specified hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProtocolsApi()
hash = 'hash_example' # str | Protocol hash

try:
    # Get protocol by hash
    api_response = api_instance.protocols_get_by_hash(hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->protocols_get_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Protocol hash | 

### Return type

[**Protocol**](Protocol.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protocols_get_count**
> int protocols_get_count()

Get protocols count

Returns the total number of protocols.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProtocolsApi()

try:
    # Get protocols count
    api_response = api_instance.protocols_get_count()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->protocols_get_count: %s\n" % e)
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

# **protocols_get_current**
> Protocol protocols_get_current()

Get current protocol

Returns current protocol.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProtocolsApi()

try:
    # Get current protocol
    api_response = api_instance.protocols_get_current()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->protocols_get_current: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Protocol**](Protocol.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

