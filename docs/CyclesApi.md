# swagger_client.CyclesApi

All URIs are relative to *https://api.tzkt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cycles_get**](CyclesApi.md#cycles_get) | **GET** /v1/cycles | Get cycles
[**cycles_get_by_index**](CyclesApi.md#cycles_get_by_index) | **GET** /v1/cycles/{index} | Get cycle by index
[**cycles_get_count**](CyclesApi.md#cycles_get_count) | **GET** /v1/cycles/count | Get cycles count

# **cycles_get**
> list[Cycle] cycles_get(snapshot_index=snapshot_index, select=select, sort=sort, offset=offset, limit=limit, quote=quote)

Get cycles

Returns a list of cycles, including future cycles.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CyclesApi()
snapshot_index = swagger_client.SnapshotIndex() # SnapshotIndex | Filters cycles by snapshot index (0..15) (optional)
select = swagger_client.Select14() # Select14 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort20() # Sort20 | Sorts cycles by specified field. Supported fields: `index` (default, desc). (optional)
offset = swagger_client.Offset18() # Offset18 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
quote = swagger_client.Quote6() # Quote6 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get cycles
    api_response = api_instance.cycles_get(snapshot_index=snapshot_index, select=select, sort=sort, offset=offset, limit=limit, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CyclesApi->cycles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_index** | [**SnapshotIndex**](.md)| Filters cycles by snapshot index (0..15) | [optional] 
 **select** | [**Select14**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort20**](.md)| Sorts cycles by specified field. Supported fields: &#x60;index&#x60; (default, desc). | [optional] 
 **offset** | [**Offset18**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **quote** | [**Quote6**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[Cycle]**](Cycle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cycles_get_by_index**
> Cycle cycles_get_by_index(index, quote=quote)

Get cycle by index

Returns a cycle at the specified index.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CyclesApi()
index = 56 # int | Cycle index starting from zero
quote = swagger_client.Quote7() # Quote7 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get cycle by index
    api_response = api_instance.cycles_get_by_index(index, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CyclesApi->cycles_get_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| Cycle index starting from zero | 
 **quote** | [**Quote7**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**Cycle**](Cycle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cycles_get_count**
> int cycles_get_count()

Get cycles count

Returns the total number of cycles, including future cycles.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CyclesApi()

try:
    # Get cycles count
    api_response = api_instance.cycles_get_count()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CyclesApi->cycles_get_count: %s\n" % e)
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

