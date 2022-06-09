# swagger_client.BigMapsApi

All URIs are relative to *https://api.tzkt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**big_maps_get_big_map_by_id**](BigMapsApi.md#big_maps_get_big_map_by_id) | **GET** /v1/bigmaps/{id} | Get bigmap by Id
[**big_maps_get_big_map_type**](BigMapsApi.md#big_maps_get_big_map_type) | **GET** /v1/bigmaps/{id}/type | Get bigmap type
[**big_maps_get_big_map_updates**](BigMapsApi.md#big_maps_get_big_map_updates) | **GET** /v1/bigmaps/updates | Get bigmap updates
[**big_maps_get_big_maps**](BigMapsApi.md#big_maps_get_big_maps) | **GET** /v1/bigmaps | Get bigmaps
[**big_maps_get_big_maps_count**](BigMapsApi.md#big_maps_get_big_maps_count) | **GET** /v1/bigmaps/count | Get bigmaps count
[**big_maps_get_historical_keys**](BigMapsApi.md#big_maps_get_historical_keys) | **GET** /v1/bigmaps/{id}/historical_keys/{level} | Get historical keys
[**big_maps_get_key**](BigMapsApi.md#big_maps_get_key) | **GET** /v1/bigmaps/{id}/keys/{key} | Get bigmap key
[**big_maps_get_key2**](BigMapsApi.md#big_maps_get_key2) | **GET** /v1/bigmaps/{id}/historical_keys/{level}/{key} | Get historical key
[**big_maps_get_key_updates**](BigMapsApi.md#big_maps_get_key_updates) | **GET** /v1/bigmaps/{id}/keys/{key}/updates | Get bigmap key updates
[**big_maps_get_keys**](BigMapsApi.md#big_maps_get_keys) | **GET** /v1/bigmaps/{id}/keys | Get bigmap keys

# **big_maps_get_big_map_by_id**
> BigMap big_maps_get_big_map_by_id(id, micheline=micheline)

Get bigmap by Id

Returns a bigmap with the specified Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BigMapsApi()
id = 56 # int | Bigmap Id
micheline = swagger_client.Micheline3() # Micheline3 | Format of the bigmap key and value type: `0` - JSON, `2` - Micheline (optional)

try:
    # Get bigmap by Id
    api_response = api_instance.big_maps_get_big_map_by_id(id, micheline=micheline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BigMapsApi->big_maps_get_big_map_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Bigmap Id | 
 **micheline** | [**Micheline3**](.md)| Format of the bigmap key and value type: &#x60;0&#x60; - JSON, &#x60;2&#x60; - Micheline | [optional] 

### Return type

[**BigMap**](BigMap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **big_maps_get_big_map_type**
> MichelinePrim big_maps_get_big_map_type(id)

Get bigmap type

Returns a type of the bigmap with the specified Id in Micheline format (with annotations).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BigMapsApi()
id = 56 # int | Bigmap Id

try:
    # Get bigmap type
    api_response = api_instance.big_maps_get_big_map_type(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BigMapsApi->big_maps_get_big_map_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Bigmap Id | 

### Return type

[**MichelinePrim**](MichelinePrim.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **big_maps_get_big_map_updates**
> list[BigMapUpdate] big_maps_get_big_map_updates(bigmap=bigmap, path=path, contract=contract, tags=tags, action=action, value=value, level=level, timestamp=timestamp, sort=sort, offset=offset, limit=limit, micheline=micheline)

Get bigmap updates

Returns a list of all bigmap updates.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BigMapsApi()
bigmap = swagger_client.Bigmap() # Bigmap | Filters updates by bigmap ptr (optional)
path = swagger_client.Path1() # Path1 | Filters updates by bigmap path (optional)
contract = swagger_client.Contract1() # Contract1 | Filters updates by bigmap contract (optional)
tags = swagger_client.Tags1() # Tags1 | Filters updates by bigmap tags: `metadata`, `token_metadata`, `ledger` (optional)
action = swagger_client.Action() # Action | Filters updates by action (optional)
value = swagger_client.Value() # Value | Filters updates by JSON value. Note, this query parameter supports the following format: `?value{.path?}{.mode?}=...`,             so you can specify a path to a particular field to filter by, for example: `?value.balance.gt=...`. (optional)
level = swagger_client.Level1() # Level1 | Filters updates by level (optional)
timestamp = swagger_client.Timestamp1() # Timestamp1 | Filters updates by timestamp. (optional)
sort = swagger_client.Sort6() # Sort6 | Sorts bigmaps by specified field. Supported fields: `id` (default), `ptr`, `firstLevel`, `lastLevel`, `totalKeys`, `activeKeys`, `updates`. (optional)
offset = swagger_client.Offset4() # Offset4 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
micheline = swagger_client.Micheline2() # Micheline2 | Format of the bigmap key and value type: `0` - JSON, `2` - Micheline (optional)

try:
    # Get bigmap updates
    api_response = api_instance.big_maps_get_big_map_updates(bigmap=bigmap, path=path, contract=contract, tags=tags, action=action, value=value, level=level, timestamp=timestamp, sort=sort, offset=offset, limit=limit, micheline=micheline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BigMapsApi->big_maps_get_big_map_updates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bigmap** | [**Bigmap**](.md)| Filters updates by bigmap ptr | [optional] 
 **path** | [**Path1**](.md)| Filters updates by bigmap path | [optional] 
 **contract** | [**Contract1**](.md)| Filters updates by bigmap contract | [optional] 
 **tags** | [**Tags1**](.md)| Filters updates by bigmap tags: &#x60;metadata&#x60;, &#x60;token_metadata&#x60;, &#x60;ledger&#x60; | [optional] 
 **action** | [**Action**](.md)| Filters updates by action | [optional] 
 **value** | [**Value**](.md)| Filters updates by JSON value. Note, this query parameter supports the following format: &#x60;?value{.path?}{.mode?}&#x3D;...&#x60;,             so you can specify a path to a particular field to filter by, for example: &#x60;?value.balance.gt&#x3D;...&#x60;. | [optional] 
 **level** | [**Level1**](.md)| Filters updates by level | [optional] 
 **timestamp** | [**Timestamp1**](.md)| Filters updates by timestamp. | [optional] 
 **sort** | [**Sort6**](.md)| Sorts bigmaps by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;ptr&#x60;, &#x60;firstLevel&#x60;, &#x60;lastLevel&#x60;, &#x60;totalKeys&#x60;, &#x60;activeKeys&#x60;, &#x60;updates&#x60;. | [optional] 
 **offset** | [**Offset4**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **micheline** | [**Micheline2**](.md)| Format of the bigmap key and value type: &#x60;0&#x60; - JSON, &#x60;2&#x60; - Micheline | [optional] 

### Return type

[**list[BigMapUpdate]**](BigMapUpdate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **big_maps_get_big_maps**
> list[BigMap] big_maps_get_big_maps(contract=contract, path=path, tags=tags, active=active, last_level=last_level, select=select, sort=sort, offset=offset, limit=limit, micheline=micheline)

Get bigmaps

Returns a list of bigmaps.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BigMapsApi()
contract = swagger_client.Contract() # Contract | Filters bigmaps by smart contract address. (optional)
path = swagger_client.Path() # Path | Filters bigmaps by path in the contract storage. (optional)
tags = swagger_client.Tags() # Tags | Filters bigmaps by tags: `metadata`, `token_metadata`, `ledger`. (optional)
active = true # bool | Filters bigmaps by status: `true` - active, `false` - removed. (optional)
last_level = swagger_client.LastLevel() # LastLevel | Filters bigmaps by the last update level. (optional)
select = swagger_client.Select2() # Select2 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort5() # Sort5 | Sorts bigmaps by specified field. Supported fields: `id` (default), `ptr`, `firstLevel`, `lastLevel`, `totalKeys`, `activeKeys`, `updates`. (optional)
offset = swagger_client.Offset3() # Offset3 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
micheline = swagger_client.Micheline1() # Micheline1 | Format of the bigmap key and value type: `0` - JSON, `2` - Micheline (optional)

try:
    # Get bigmaps
    api_response = api_instance.big_maps_get_big_maps(contract=contract, path=path, tags=tags, active=active, last_level=last_level, select=select, sort=sort, offset=offset, limit=limit, micheline=micheline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BigMapsApi->big_maps_get_big_maps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | [**Contract**](.md)| Filters bigmaps by smart contract address. | [optional] 
 **path** | [**Path**](.md)| Filters bigmaps by path in the contract storage. | [optional] 
 **tags** | [**Tags**](.md)| Filters bigmaps by tags: &#x60;metadata&#x60;, &#x60;token_metadata&#x60;, &#x60;ledger&#x60;. | [optional] 
 **active** | **bool**| Filters bigmaps by status: &#x60;true&#x60; - active, &#x60;false&#x60; - removed. | [optional] 
 **last_level** | [**LastLevel**](.md)| Filters bigmaps by the last update level. | [optional] 
 **select** | [**Select2**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort5**](.md)| Sorts bigmaps by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;ptr&#x60;, &#x60;firstLevel&#x60;, &#x60;lastLevel&#x60;, &#x60;totalKeys&#x60;, &#x60;activeKeys&#x60;, &#x60;updates&#x60;. | [optional] 
 **offset** | [**Offset3**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **micheline** | [**Micheline1**](.md)| Format of the bigmap key and value type: &#x60;0&#x60; - JSON, &#x60;2&#x60; - Micheline | [optional] 

### Return type

[**list[BigMap]**](BigMap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **big_maps_get_big_maps_count**
> int big_maps_get_big_maps_count()

Get bigmaps count

Returns the total number of bigmaps.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BigMapsApi()

try:
    # Get bigmaps count
    api_response = api_instance.big_maps_get_big_maps_count()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BigMapsApi->big_maps_get_big_maps_count: %s\n" % e)
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

# **big_maps_get_historical_keys**
> list[BigMapKeyHistorical] big_maps_get_historical_keys(id, level, active=active, key=key, value=value, select=select, sort=sort, offset=offset, limit=limit, micheline=micheline)

Get historical keys

Returns a list of bigmap keys at the specific block.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BigMapsApi()
id = 56 # int | Bigmap Id
level = 56 # int | Level of the block at which you want to get bigmap keys
active = true # bool | Filters keys by status: `true` - active, `false` - removed. (optional)
key = swagger_client.Key1() # Key1 | Filters keys by JSON key. Note, this query parameter supports the following format: `?key{.path?}{.mode?}=...`,             so you can specify a path to a particular field to filter by, for example: `?key.token_id=...`. (optional)
value = swagger_client.Value2() # Value2 | Filters keys by JSON value. Note, this query parameter supports the following format: `?value{.path?}{.mode?}=...`,             so you can specify a path to a particular field to filter by, for example: `?value.balance.gt=...`. (optional)
select = swagger_client.Select4() # Select4 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort9() # Sort9 | Sorts bigmap keys by specified field. Supported fields: `id` (default). (optional)
offset = swagger_client.Offset7() # Offset7 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
micheline = swagger_client.Micheline7() # Micheline7 | Format of the bigmap key and value: `0` - JSON, `1` - JSON string, `2` - Micheline, `3` - Micheline string (optional)

try:
    # Get historical keys
    api_response = api_instance.big_maps_get_historical_keys(id, level, active=active, key=key, value=value, select=select, sort=sort, offset=offset, limit=limit, micheline=micheline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BigMapsApi->big_maps_get_historical_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Bigmap Id | 
 **level** | **int**| Level of the block at which you want to get bigmap keys | 
 **active** | **bool**| Filters keys by status: &#x60;true&#x60; - active, &#x60;false&#x60; - removed. | [optional] 
 **key** | [**Key1**](.md)| Filters keys by JSON key. Note, this query parameter supports the following format: &#x60;?key{.path?}{.mode?}&#x3D;...&#x60;,             so you can specify a path to a particular field to filter by, for example: &#x60;?key.token_id&#x3D;...&#x60;. | [optional] 
 **value** | [**Value2**](.md)| Filters keys by JSON value. Note, this query parameter supports the following format: &#x60;?value{.path?}{.mode?}&#x3D;...&#x60;,             so you can specify a path to a particular field to filter by, for example: &#x60;?value.balance.gt&#x3D;...&#x60;. | [optional] 
 **select** | [**Select4**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort9**](.md)| Sorts bigmap keys by specified field. Supported fields: &#x60;id&#x60; (default). | [optional] 
 **offset** | [**Offset7**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **micheline** | [**Micheline7**](.md)| Format of the bigmap key and value: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - Micheline, &#x60;3&#x60; - Micheline string | [optional] 

### Return type

[**list[BigMapKeyHistorical]**](BigMapKeyHistorical.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **big_maps_get_key**
> BigMapKey big_maps_get_key(id, key, micheline=micheline)

Get bigmap key

Returns the specified bigmap key.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BigMapsApi()
id = 56 # int | Bigmap Id
key = 'key_example' # str | Either a key hash (`expr123...`) or a plain value (`abcde...`).             Even if the key is complex (an object or an array), you can specify it as is, for example, `/keys/{\"address\":\"tz123\",\"nat\":\"123\"}`.
micheline = swagger_client.Micheline5() # Micheline5 | Format of the bigmap key and value: `0` - JSON, `1` - JSON string, `2` - Micheline, `3` - Micheline string (optional)

try:
    # Get bigmap key
    api_response = api_instance.big_maps_get_key(id, key, micheline=micheline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BigMapsApi->big_maps_get_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Bigmap Id | 
 **key** | **str**| Either a key hash (&#x60;expr123...&#x60;) or a plain value (&#x60;abcde...&#x60;).             Even if the key is complex (an object or an array), you can specify it as is, for example, &#x60;/keys/{\&quot;address\&quot;:\&quot;tz123\&quot;,\&quot;nat\&quot;:\&quot;123\&quot;}&#x60;. | 
 **micheline** | [**Micheline5**](.md)| Format of the bigmap key and value: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - Micheline, &#x60;3&#x60; - Micheline string | [optional] 

### Return type

[**BigMapKey**](BigMapKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **big_maps_get_key2**
> BigMapKeyHistorical big_maps_get_key2(id, level, key, micheline=micheline)

Get historical key

Returns the specified bigmap key at the specific block.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BigMapsApi()
id = 56 # int | Bigmap Id
level = 56 # int | Level of the block at which you want to get bigmap key
key = 'key_example' # str | Either a key hash (`expr123...`) or a plain value (`abcde...`).             Even if the key is complex (an object or an array), you can specify it as is, for example, `/keys/{\"address\":\"tz123\",\"nat\":\"123\"}`.
micheline = swagger_client.Micheline8() # Micheline8 | Format of the bigmap key and value: `0` - JSON, `1` - JSON string, `2` - Micheline, `3` - Micheline string (optional)

try:
    # Get historical key
    api_response = api_instance.big_maps_get_key2(id, level, key, micheline=micheline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BigMapsApi->big_maps_get_key2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Bigmap Id | 
 **level** | **int**| Level of the block at which you want to get bigmap key | 
 **key** | **str**| Either a key hash (&#x60;expr123...&#x60;) or a plain value (&#x60;abcde...&#x60;).             Even if the key is complex (an object or an array), you can specify it as is, for example, &#x60;/keys/{\&quot;address\&quot;:\&quot;tz123\&quot;,\&quot;nat\&quot;:\&quot;123\&quot;}&#x60;. | 
 **micheline** | [**Micheline8**](.md)| Format of the bigmap key and value: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - Micheline, &#x60;3&#x60; - Micheline string | [optional] 

### Return type

[**BigMapKeyHistorical**](BigMapKeyHistorical.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **big_maps_get_key_updates**
> list[BigMapKeyUpdate] big_maps_get_key_updates(id, key, sort=sort, offset=offset, limit=limit, micheline=micheline)

Get bigmap key updates

Returns updates history for the specified bigmap key.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BigMapsApi()
id = 56 # int | Bigmap Id
key = 'key_example' # str | Either a key hash (`expr123...`) or a plain value (`abcde...`).             Even if the key is complex (an object or an array), you can specify it as is, for example, `/keys/{\"address\":\"tz123\",\"nat\":\"123\"}`.
sort = swagger_client.Sort8() # Sort8 | Sorts bigmap updates by specified field. Supported fields: `id` (default). (optional)
offset = swagger_client.Offset6() # Offset6 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
micheline = swagger_client.Micheline6() # Micheline6 | Format of the key value: `0` - JSON, `1` - JSON string, `2` - Micheline, `3` - Micheline string (optional)

try:
    # Get bigmap key updates
    api_response = api_instance.big_maps_get_key_updates(id, key, sort=sort, offset=offset, limit=limit, micheline=micheline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BigMapsApi->big_maps_get_key_updates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Bigmap Id | 
 **key** | **str**| Either a key hash (&#x60;expr123...&#x60;) or a plain value (&#x60;abcde...&#x60;).             Even if the key is complex (an object or an array), you can specify it as is, for example, &#x60;/keys/{\&quot;address\&quot;:\&quot;tz123\&quot;,\&quot;nat\&quot;:\&quot;123\&quot;}&#x60;. | 
 **sort** | [**Sort8**](.md)| Sorts bigmap updates by specified field. Supported fields: &#x60;id&#x60; (default). | [optional] 
 **offset** | [**Offset6**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **micheline** | [**Micheline6**](.md)| Format of the key value: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - Micheline, &#x60;3&#x60; - Micheline string | [optional] 

### Return type

[**list[BigMapKeyUpdate]**](BigMapKeyUpdate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **big_maps_get_keys**
> list[BigMapKey] big_maps_get_keys(id, active=active, key=key, value=value, last_level=last_level, select=select, sort=sort, offset=offset, limit=limit, micheline=micheline)

Get bigmap keys

Returns a list of bigmap keys.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BigMapsApi()
id = 56 # int | Bigmap Id
active = true # bool | Filters keys by status: `true` - active, `false` - removed. (optional)
key = swagger_client.Key() # Key | Filters keys by JSON key. Note, this query parameter supports the following format: `?key{.path?}{.mode?}=...`,             so you can specify a path to a particular field to filter by, for example: `?key.token_id=...`. (optional)
value = swagger_client.Value1() # Value1 | Filters keys by JSON value. Note, this query parameter supports the following format: `?value{.path?}{.mode?}=...`,             so you can specify a path to a particular field to filter by, for example: `?value.balance.gt=...`. (optional)
last_level = swagger_client.LastLevel1() # LastLevel1 | Filters bigmap keys by the last update level. (optional)
select = swagger_client.Select3() # Select3 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort7() # Sort7 | Sorts bigmap keys by specified field. Supported fields: `id` (default), `firstLevel`, `lastLevel`, `updates`. (optional)
offset = swagger_client.Offset5() # Offset5 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
micheline = swagger_client.Micheline4() # Micheline4 | Format of the bigmap key and value: `0` - JSON, `1` - JSON string, `2` - Micheline, `3` - Micheline string (optional)

try:
    # Get bigmap keys
    api_response = api_instance.big_maps_get_keys(id, active=active, key=key, value=value, last_level=last_level, select=select, sort=sort, offset=offset, limit=limit, micheline=micheline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BigMapsApi->big_maps_get_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Bigmap Id | 
 **active** | **bool**| Filters keys by status: &#x60;true&#x60; - active, &#x60;false&#x60; - removed. | [optional] 
 **key** | [**Key**](.md)| Filters keys by JSON key. Note, this query parameter supports the following format: &#x60;?key{.path?}{.mode?}&#x3D;...&#x60;,             so you can specify a path to a particular field to filter by, for example: &#x60;?key.token_id&#x3D;...&#x60;. | [optional] 
 **value** | [**Value1**](.md)| Filters keys by JSON value. Note, this query parameter supports the following format: &#x60;?value{.path?}{.mode?}&#x3D;...&#x60;,             so you can specify a path to a particular field to filter by, for example: &#x60;?value.balance.gt&#x3D;...&#x60;. | [optional] 
 **last_level** | [**LastLevel1**](.md)| Filters bigmap keys by the last update level. | [optional] 
 **select** | [**Select3**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort7**](.md)| Sorts bigmap keys by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;firstLevel&#x60;, &#x60;lastLevel&#x60;, &#x60;updates&#x60;. | [optional] 
 **offset** | [**Offset5**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **micheline** | [**Micheline4**](.md)| Format of the bigmap key and value: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - Micheline, &#x60;3&#x60; - Micheline string | [optional] 

### Return type

[**list[BigMapKey]**](BigMapKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

