# swagger_client.RightsApi

All URIs are relative to *https://api.tzkt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rights_get**](RightsApi.md#rights_get) | **GET** /v1/rights | Get rights
[**rights_get_count**](RightsApi.md#rights_get_count) | **GET** /v1/rights/count | Get rights count

# **rights_get**
> list[BakingRight] rights_get(type=type, baker=baker, cycle=cycle, level=level, slots=slots, round=round, priority=priority, status=status, select=select, sort=sort, offset=offset, limit=limit)

Get rights

Returns a list of rights.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RightsApi()
type = swagger_client.Type4() # Type4 | Filters rights by type (`baking`, `endorsing`) (optional)
baker = swagger_client.Baker7() # Baker7 | Filters rights by baker (optional)
cycle = swagger_client.Cycle3() # Cycle3 | Filters rights by cycle (optional)
level = swagger_client.Level43() # Level43 | Filters rights by level (optional)
slots = swagger_client.Slots1() # Slots1 | Filters rights by slots (optional)
round = swagger_client.Round1() # Round1 | Filters rights by round (optional)
priority = swagger_client.Priority2() # Priority2 | [DEPRECATED] (optional)
status = swagger_client.Status9() # Status9 | Filters rights by status (`future`, `realized`, `missed`) (optional)
select = swagger_client.Select38() # Select38 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort45() # Sort45 | Sorts rights by specified field. Supported fields: `level` (default). (optional)
offset = swagger_client.Offset43() # Offset43 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)

try:
    # Get rights
    api_response = api_instance.rights_get(type=type, baker=baker, cycle=cycle, level=level, slots=slots, round=round, priority=priority, status=status, select=select, sort=sort, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RightsApi->rights_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**Type4**](.md)| Filters rights by type (&#x60;baking&#x60;, &#x60;endorsing&#x60;) | [optional] 
 **baker** | [**Baker7**](.md)| Filters rights by baker | [optional] 
 **cycle** | [**Cycle3**](.md)| Filters rights by cycle | [optional] 
 **level** | [**Level43**](.md)| Filters rights by level | [optional] 
 **slots** | [**Slots1**](.md)| Filters rights by slots | [optional] 
 **round** | [**Round1**](.md)| Filters rights by round | [optional] 
 **priority** | [**Priority2**](.md)| [DEPRECATED] | [optional] 
 **status** | [**Status9**](.md)| Filters rights by status (&#x60;future&#x60;, &#x60;realized&#x60;, &#x60;missed&#x60;) | [optional] 
 **select** | [**Select38**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort45**](.md)| Sorts rights by specified field. Supported fields: &#x60;level&#x60; (default). | [optional] 
 **offset** | [**Offset43**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]

### Return type

[**list[BakingRight]**](BakingRight.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rights_get_count**
> int rights_get_count(type=type, baker=baker, cycle=cycle, level=level, slots=slots, round=round, priority=priority, status=status)

Get rights count

Returns the total number of stored rights.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RightsApi()
type = swagger_client.Type3() # Type3 | Filters rights by type (`baking`, `endorsing`) (optional)
baker = swagger_client.Baker6() # Baker6 | Filters rights by baker (optional)
cycle = swagger_client.Cycle2() # Cycle2 | Filters rights by cycle (optional)
level = swagger_client.Level42() # Level42 | Filters rights by level (optional)
slots = swagger_client.Slots() # Slots | Filters rights by slots (optional)
round = swagger_client.Round() # Round | Filters rights by round (optional)
priority = swagger_client.Priority1() # Priority1 | [DEPRECATED] (optional)
status = swagger_client.Status8() # Status8 | Filters rights by status (`future`, `realized`, `missed`) (optional)

try:
    # Get rights count
    api_response = api_instance.rights_get_count(type=type, baker=baker, cycle=cycle, level=level, slots=slots, round=round, priority=priority, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RightsApi->rights_get_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**Type3**](.md)| Filters rights by type (&#x60;baking&#x60;, &#x60;endorsing&#x60;) | [optional] 
 **baker** | [**Baker6**](.md)| Filters rights by baker | [optional] 
 **cycle** | [**Cycle2**](.md)| Filters rights by cycle | [optional] 
 **level** | [**Level42**](.md)| Filters rights by level | [optional] 
 **slots** | [**Slots**](.md)| Filters rights by slots | [optional] 
 **round** | [**Round**](.md)| Filters rights by round | [optional] 
 **priority** | [**Priority1**](.md)| [DEPRECATED] | [optional] 
 **status** | [**Status8**](.md)| Filters rights by status (&#x60;future&#x60;, &#x60;realized&#x60;, &#x60;missed&#x60;) | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

