# swagger_client.BlocksApi

All URIs are relative to *https://api.tzkt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blocks_get**](BlocksApi.md#blocks_get) | **GET** /v1/blocks | Get blocks
[**blocks_get_by_date**](BlocksApi.md#blocks_get_by_date) | **GET** /v1/blocks/{timestamp} | Get block by timestamp
[**blocks_get_by_date2**](BlocksApi.md#blocks_get_by_date2) | **GET** /v1/blocks/{timestamp}/level | Get level by timestamp
[**blocks_get_by_hash**](BlocksApi.md#blocks_get_by_hash) | **GET** /v1/blocks/{hash} | Get block by hash
[**blocks_get_by_level**](BlocksApi.md#blocks_get_by_level) | **GET** /v1/blocks/{level} | Get block by level
[**blocks_get_by_level2**](BlocksApi.md#blocks_get_by_level2) | **GET** /v1/blocks/{level}/timestamp | Get timestamp by level
[**blocks_get_count**](BlocksApi.md#blocks_get_count) | **GET** /v1/blocks/count | Get blocks count

# **blocks_get**
> list[Block] blocks_get(baker=baker, anyof=anyof, proposer=proposer, producer=producer, level=level, timestamp=timestamp, priority=priority, block_round=block_round, select=select, sort=sort, offset=offset, limit=limit, quote=quote)

Get blocks

Returns a list of blocks.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlocksApi()
baker = swagger_client.Baker1() # Baker1 | [DEPRECATED] (optional)
anyof = 'anyof_example' # str | Filters by any of the specified fields. Example: `anyof.proposer.producer=tz1...`. (optional)
proposer = swagger_client.Proposer() # Proposer | Filters blocks by block proposer. Allowed fields for `.eqx` mode: none. (optional)
producer = swagger_client.Producer() # Producer | Filters blocks by block producer. Allowed fields for `.eqx` mode: none. (optional)
level = swagger_client.Level2() # Level2 | Filters blocks by level. (optional)
timestamp = swagger_client.Timestamp2() # Timestamp2 | Filters blocks by timestamp. (optional)
priority = swagger_client.Priority() # Priority | [DEPRECATED] (optional)
block_round = swagger_client.BlockRound() # BlockRound | Filters blocks by block round. (optional)
select = swagger_client.Select5() # Select5 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort10() # Sort10 | Sorts blocks by specified field. Supported fields: `id` (default), `level`, `payloadRound`, `blockRound`, `validations`, `reward`, `bonus`, `fees`. (optional)
offset = swagger_client.Offset8() # Offset8 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
quote = swagger_client.Quote2() # Quote2 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get blocks
    api_response = api_instance.blocks_get(baker=baker, anyof=anyof, proposer=proposer, producer=producer, level=level, timestamp=timestamp, priority=priority, block_round=block_round, select=select, sort=sort, offset=offset, limit=limit, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->blocks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **baker** | [**Baker1**](.md)| [DEPRECATED] | [optional] 
 **anyof** | **str**| Filters by any of the specified fields. Example: &#x60;anyof.proposer.producer&#x3D;tz1...&#x60;. | [optional] 
 **proposer** | [**Proposer**](.md)| Filters blocks by block proposer. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **producer** | [**Producer**](.md)| Filters blocks by block producer. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **level** | [**Level2**](.md)| Filters blocks by level. | [optional] 
 **timestamp** | [**Timestamp2**](.md)| Filters blocks by timestamp. | [optional] 
 **priority** | [**Priority**](.md)| [DEPRECATED] | [optional] 
 **block_round** | [**BlockRound**](.md)| Filters blocks by block round. | [optional] 
 **select** | [**Select5**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort10**](.md)| Sorts blocks by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;level&#x60;, &#x60;payloadRound&#x60;, &#x60;blockRound&#x60;, &#x60;validations&#x60;, &#x60;reward&#x60;, &#x60;bonus&#x60;, &#x60;fees&#x60;. | [optional] 
 **offset** | [**Offset8**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **quote** | [**Quote2**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[Block]**](Block.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blocks_get_by_date**
> Block blocks_get_by_date(timestamp, operations=operations, micheline=micheline, quote=quote)

Get block by timestamp

Returns a block closest to the specified timestamp.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlocksApi()
timestamp = '2013-10-20T19:20:30+01:00' # datetime | Timestamp, e.g. `2020-01-01T00:00:00Z`
operations = false # bool | Flag indicating whether to include block operations into returned object or not (optional) (default to false)
micheline = swagger_client.Micheline11() # Micheline11 | Format of the parameters, storage and diffs: `0` - JSON, `1` - JSON string, `2` - raw micheline, `3` - raw micheline string (optional)
quote = swagger_client.Quote5() # Quote5 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get block by timestamp
    api_response = api_instance.blocks_get_by_date(timestamp, operations=operations, micheline=micheline, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->blocks_get_by_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **datetime**| Timestamp, e.g. &#x60;2020-01-01T00:00:00Z&#x60; | 
 **operations** | **bool**| Flag indicating whether to include block operations into returned object or not | [optional] [default to false]
 **micheline** | [**Micheline11**](.md)| Format of the parameters, storage and diffs: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - raw micheline, &#x60;3&#x60; - raw micheline string | [optional] 
 **quote** | [**Quote5**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**Block**](Block.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blocks_get_by_date2**
> int blocks_get_by_date2(timestamp)

Get level by timestamp

Returns a level of the block closest to the specified timestamp.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlocksApi()
timestamp = '2013-10-20T19:20:30+01:00' # datetime | Timestamp, e.g. `2020-01-01T00:00:00Z`

try:
    # Get level by timestamp
    api_response = api_instance.blocks_get_by_date2(timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->blocks_get_by_date2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **datetime**| Timestamp, e.g. &#x60;2020-01-01T00:00:00Z&#x60; | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blocks_get_by_hash**
> Block blocks_get_by_hash(hash, operations=operations, micheline=micheline, quote=quote)

Get block by hash

Returns a block with the specified hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlocksApi()
hash = 'hash_example' # str | Block hash
operations = false # bool | Flag indicating whether to include block operations into returned object or not (optional) (default to false)
micheline = swagger_client.Micheline9() # Micheline9 | Format of the parameters, storage and diffs: `0` - JSON, `1` - JSON string, `2` - raw micheline, `3` - raw micheline string (optional)
quote = swagger_client.Quote3() # Quote3 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get block by hash
    api_response = api_instance.blocks_get_by_hash(hash, operations=operations, micheline=micheline, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->blocks_get_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Block hash | 
 **operations** | **bool**| Flag indicating whether to include block operations into returned object or not | [optional] [default to false]
 **micheline** | [**Micheline9**](.md)| Format of the parameters, storage and diffs: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - raw micheline, &#x60;3&#x60; - raw micheline string | [optional] 
 **quote** | [**Quote3**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**Block**](Block.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blocks_get_by_level**
> Block blocks_get_by_level(level, operations=operations, micheline=micheline, quote=quote)

Get block by level

Returns a block at the specified level.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlocksApi()
level = 56 # int | Block level
operations = false # bool | Flag indicating whether to include block operations into returned object or not (optional) (default to false)
micheline = swagger_client.Micheline10() # Micheline10 | Format of the parameters, storage and diffs: `0` - JSON, `1` - JSON string, `2` - raw micheline, `3` - raw micheline string (optional)
quote = swagger_client.Quote4() # Quote4 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get block by level
    api_response = api_instance.blocks_get_by_level(level, operations=operations, micheline=micheline, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->blocks_get_by_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **int**| Block level | 
 **operations** | **bool**| Flag indicating whether to include block operations into returned object or not | [optional] [default to false]
 **micheline** | [**Micheline10**](.md)| Format of the parameters, storage and diffs: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - raw micheline, &#x60;3&#x60; - raw micheline string | [optional] 
 **quote** | [**Quote4**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**Block**](Block.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blocks_get_by_level2**
> datetime blocks_get_by_level2(level)

Get timestamp by level

Returns a timestamp of the block at the specified level.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlocksApi()
level = 56 # int | Block level

try:
    # Get timestamp by level
    api_response = api_instance.blocks_get_by_level2(level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->blocks_get_by_level2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **int**| Block level | 

### Return type

**datetime**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blocks_get_count**
> int blocks_get_count()

Get blocks count

Returns the total number of blocks.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlocksApi()

try:
    # Get blocks count
    api_response = api_instance.blocks_get_count()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->blocks_get_count: %s\n" % e)
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

