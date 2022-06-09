# swagger_client.ContractsApi

All URIs are relative to *https://api.tzkt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contracts_build_entrypoint_parameters_get**](ContractsApi.md#contracts_build_entrypoint_parameters_get) | **GET** /v1/contracts/{address}/entrypoints/{name}/build | Build entrypoint parameters
[**contracts_build_entrypoint_parameters_post**](ContractsApi.md#contracts_build_entrypoint_parameters_post) | **POST** /v1/contracts/{address}/entrypoints/{name}/build | Build entrypoint parameters
[**contracts_get**](ContractsApi.md#contracts_get) | **GET** /v1/contracts | Get contracts
[**contracts_get_big_map_by_name**](ContractsApi.md#contracts_get_big_map_by_name) | **GET** /v1/contracts/{address}/bigmaps/{name} | Get bigmap by name
[**contracts_get_big_map_by_name_keys**](ContractsApi.md#contracts_get_big_map_by_name_keys) | **GET** /v1/contracts/{address}/bigmaps/{name}/keys | Get bigmap keys
[**contracts_get_big_maps**](ContractsApi.md#contracts_get_big_maps) | **GET** /v1/contracts/{address}/bigmaps | Get contract bigmaps
[**contracts_get_by_address**](ContractsApi.md#contracts_get_by_address) | **GET** /v1/contracts/{address} | Get contract by address
[**contracts_get_code**](ContractsApi.md#contracts_get_code) | **GET** /v1/contracts/{address}/code | Get contract code
[**contracts_get_contract_view_by_name**](ContractsApi.md#contracts_get_contract_view_by_name) | **GET** /v1/contracts/{address}/views/{name} | Get view by name
[**contracts_get_contract_views**](ContractsApi.md#contracts_get_contract_views) | **GET** /v1/contracts/{address}/views | Get contract views
[**contracts_get_count**](ContractsApi.md#contracts_get_count) | **GET** /v1/contracts/count | Get contracts count
[**contracts_get_entrypoint_by_name**](ContractsApi.md#contracts_get_entrypoint_by_name) | **GET** /v1/contracts/{address}/entrypoints/{name} | Get entrypoint by name
[**contracts_get_entrypoints**](ContractsApi.md#contracts_get_entrypoints) | **GET** /v1/contracts/{address}/entrypoints | Get contract entrypoints
[**contracts_get_historical_keys**](ContractsApi.md#contracts_get_historical_keys) | **GET** /v1/contracts/{address}/bigmaps/{name}/historical_keys/{level} | Get historical keys
[**contracts_get_interface**](ContractsApi.md#contracts_get_interface) | **GET** /v1/contracts/{address}/interface | Get JSON Schema [2020-12] interface for the contract
[**contracts_get_key**](ContractsApi.md#contracts_get_key) | **GET** /v1/contracts/{address}/bigmaps/{name}/keys/{key} | Get bigmap key
[**contracts_get_key2**](ContractsApi.md#contracts_get_key2) | **GET** /v1/contracts/{address}/bigmaps/{name}/historical_keys/{level}/{key} | Get historical key
[**contracts_get_key_updates**](ContractsApi.md#contracts_get_key_updates) | **GET** /v1/contracts/{address}/bigmaps/{name}/keys/{key}/updates | Get bigmap key updates
[**contracts_get_raw_storage**](ContractsApi.md#contracts_get_raw_storage) | **GET** /v1/contracts/{address}/storage/raw | Get raw contract storage
[**contracts_get_raw_storage_history**](ContractsApi.md#contracts_get_raw_storage_history) | **GET** /v1/contracts/{address}/storage/raw/history | Get raw contract storage history
[**contracts_get_raw_storage_schema**](ContractsApi.md#contracts_get_raw_storage_schema) | **GET** /v1/contracts/{address}/storage/raw/schema | Get raw contract storage schema
[**contracts_get_same**](ContractsApi.md#contracts_get_same) | **GET** /v1/contracts/{address}/same | Get same contracts
[**contracts_get_similar**](ContractsApi.md#contracts_get_similar) | **GET** /v1/contracts/{address}/similar | Get similar contracts
[**contracts_get_storage**](ContractsApi.md#contracts_get_storage) | **GET** /v1/contracts/{address}/storage | Get contract storage
[**contracts_get_storage_history**](ContractsApi.md#contracts_get_storage_history) | **GET** /v1/contracts/{address}/storage/history | Get contract storage history
[**contracts_get_storage_schema**](ContractsApi.md#contracts_get_storage_schema) | **GET** /v1/contracts/{address}/storage/schema | Get contract storage schema

# **contracts_build_entrypoint_parameters_get**
> str contracts_build_entrypoint_parameters_get(address, name, value=value)

Build entrypoint parameters

Returns micheline parameters converted from its JSON representation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
address = 'address_example' # str | Contract address
name = 'name_example' # str | Entrypoint name
value = 'value_example' # str | Json parameters (optional)

try:
    # Build entrypoint parameters
    api_response = api_instance.contracts_build_entrypoint_parameters_get(address, name, value=value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_build_entrypoint_parameters_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Contract address | 
 **name** | **str**| Entrypoint name | 
 **value** | **str**| Json parameters | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_build_entrypoint_parameters_post**
> str contracts_build_entrypoint_parameters_post(body, address, name)

Build entrypoint parameters

Returns micheline parameters converted from its JSON representation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
body = NULL # object | Json parameters
address = 'address_example' # str | Contract address
name = 'name_example' # str | Entrypoint name

try:
    # Build entrypoint parameters
    api_response = api_instance.contracts_build_entrypoint_parameters_post(body, address, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_build_entrypoint_parameters_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Json parameters | 
 **address** | **str**| Contract address | 
 **name** | **str**| Entrypoint name | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get**
> list[Contract] contracts_get(kind=kind, tzips=tzips, creator=creator, manager=manager, delegate=delegate, balance=balance, last_activity=last_activity, type_hash=type_hash, code_hash=code_hash, select=select, sort=sort, offset=offset, limit=limit, include_storage=include_storage)

Get contracts

Returns a list of contract accounts.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
kind = swagger_client.Kind2() # Kind2 | Contract kind to filter by (`delegator_contract`, `smart_contract`, or `asset`) (optional)
tzips = swagger_client.Tzips() # Tzips | Filters by tzips (`fa1`, `fa12`, or `fa2`) (optional)
creator = swagger_client.Creator1() # Creator1 | Filters contracts by creator. Allowed fields for `.eqx` mode: `manager`, `delegate`. (optional)
manager = swagger_client.Manager() # Manager | Filters contracts by manager. Allowed fields for `.eqx` mode: `creator`, `delegate`. (optional)
delegate = swagger_client.Delegate1() # Delegate1 | Filters contracts by delegate. Allowed fields for `.eqx` mode: `manager`, `creator`. (optional)
balance = swagger_client.Balance5() # Balance5 | Filters contracts by balance (optional)
last_activity = swagger_client.LastActivity1() # LastActivity1 | Filters contracts by last activity level (where the contract was updated) (optional)
type_hash = swagger_client.TypeHash() # TypeHash | Filters contracts by 32-bit hash of contract parameter and storage types (helpful for searching similar contracts) (optional)
code_hash = swagger_client.CodeHash() # CodeHash | Filters contracts by 32-bit hash of contract code (helpful for searching same contracts) (optional)
select = swagger_client.Select8() # Select8 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort13() # Sort13 | Sorts contracts by specified field. Supported fields: `id` (default), `balance`, `firstActivity`, `lastActivity`, `numTransactions`. (optional)
offset = swagger_client.Offset11() # Offset11 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
include_storage = false # bool | Specifies whether to include contract storage value in response. (optional) (default to false)

try:
    # Get contracts
    api_response = api_instance.contracts_get(kind=kind, tzips=tzips, creator=creator, manager=manager, delegate=delegate, balance=balance, last_activity=last_activity, type_hash=type_hash, code_hash=code_hash, select=select, sort=sort, offset=offset, limit=limit, include_storage=include_storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kind** | [**Kind2**](.md)| Contract kind to filter by (&#x60;delegator_contract&#x60;, &#x60;smart_contract&#x60;, or &#x60;asset&#x60;) | [optional] 
 **tzips** | [**Tzips**](.md)| Filters by tzips (&#x60;fa1&#x60;, &#x60;fa12&#x60;, or &#x60;fa2&#x60;) | [optional] 
 **creator** | [**Creator1**](.md)| Filters contracts by creator. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;manager&#x60;, &#x60;delegate&#x60;. | [optional] 
 **manager** | [**Manager**](.md)| Filters contracts by manager. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;creator&#x60;, &#x60;delegate&#x60;. | [optional] 
 **delegate** | [**Delegate1**](.md)| Filters contracts by delegate. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;manager&#x60;, &#x60;creator&#x60;. | [optional] 
 **balance** | [**Balance5**](.md)| Filters contracts by balance | [optional] 
 **last_activity** | [**LastActivity1**](.md)| Filters contracts by last activity level (where the contract was updated) | [optional] 
 **type_hash** | [**TypeHash**](.md)| Filters contracts by 32-bit hash of contract parameter and storage types (helpful for searching similar contracts) | [optional] 
 **code_hash** | [**CodeHash**](.md)| Filters contracts by 32-bit hash of contract code (helpful for searching same contracts) | [optional] 
 **select** | [**Select8**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort13**](.md)| Sorts contracts by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;balance&#x60;, &#x60;firstActivity&#x60;, &#x60;lastActivity&#x60;, &#x60;numTransactions&#x60;. | [optional] 
 **offset** | [**Offset11**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **include_storage** | **bool**| Specifies whether to include contract storage value in response. | [optional] [default to false]

### Return type

[**list[Contract]**](Contract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get_big_map_by_name**
> BigMap contracts_get_big_map_by_name(address, name, micheline=micheline)

Get bigmap by name

Returns contract bigmap with the specified name or storage path.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
address = 'address_example' # str | Contract address
name = 'name_example' # str | Bigmap name is the last piece of the bigmap storage path.             For example, if the storage path is `ledger` or `assets.ledger`, then the name is `ledger`.             If there are multiple bigmaps with the same name, for example `assets.ledger` and `tokens.ledger`, you can specify the full path.
micheline = swagger_client.Micheline13() # Micheline13 | Format of the bigmap key and value: `0` - JSON, `1` - JSON string, `2` - Micheline, `3` - Micheline string (optional)

try:
    # Get bigmap by name
    api_response = api_instance.contracts_get_big_map_by_name(address, name, micheline=micheline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get_big_map_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Contract address | 
 **name** | **str**| Bigmap name is the last piece of the bigmap storage path.             For example, if the storage path is &#x60;ledger&#x60; or &#x60;assets.ledger&#x60;, then the name is &#x60;ledger&#x60;.             If there are multiple bigmaps with the same name, for example &#x60;assets.ledger&#x60; and &#x60;tokens.ledger&#x60;, you can specify the full path. | 
 **micheline** | [**Micheline13**](.md)| Format of the bigmap key and value: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - Micheline, &#x60;3&#x60; - Micheline string | [optional] 

### Return type

[**BigMap**](BigMap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get_big_map_by_name_keys**
> list[BigMapKey] contracts_get_big_map_by_name_keys(address, name, active=active, key=key, value=value, last_level=last_level, select=select, sort=sort, offset=offset, limit=limit, micheline=micheline)

Get bigmap keys

Returns keys of a contract bigmap with the specified name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
address = 'address_example' # str | Contract address
name = 'name_example' # str | Bigmap name is the last piece of the bigmap storage path.             For example, if the storage path is `ledger` or `assets.ledger`, then the name is `ledger`.             If there are multiple bigmaps with the same name, for example `assets.ledger` and `tokens.ledger`, you can specify the full path.
active = true # bool | Filters keys by status: `true` - active, `false` - removed. (optional)
key = swagger_client.Key2() # Key2 | Filters keys by JSON key. Note, this query parameter supports the following format: `?key{.path?}{.mode?}=...`,             so you can specify a path to a particular field to filter by, for example: `?key.token_id=...`. (optional)
value = swagger_client.Value3() # Value3 | Filters keys by JSON value. Note, this query parameter supports the following format: `?value{.path?}{.mode?}=...`,             so you can specify a path to a particular field to filter by, for example: `?value.balance.gt=...`. (optional)
last_level = swagger_client.LastLevel2() # LastLevel2 | Filters bigmap keys by the last update level. (optional)
select = swagger_client.Select12() # Select12 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort17() # Sort17 | Sorts bigmap keys by specified field. Supported fields: `id` (default), `firstLevel`, `lastLevel`, `updates`. (optional)
offset = swagger_client.Offset15() # Offset15 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
micheline = swagger_client.Micheline14() # Micheline14 | Format of the bigmap key and value: `0` - JSON, `1` - JSON string, `2` - Micheline, `3` - Micheline string (optional)

try:
    # Get bigmap keys
    api_response = api_instance.contracts_get_big_map_by_name_keys(address, name, active=active, key=key, value=value, last_level=last_level, select=select, sort=sort, offset=offset, limit=limit, micheline=micheline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get_big_map_by_name_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Contract address | 
 **name** | **str**| Bigmap name is the last piece of the bigmap storage path.             For example, if the storage path is &#x60;ledger&#x60; or &#x60;assets.ledger&#x60;, then the name is &#x60;ledger&#x60;.             If there are multiple bigmaps with the same name, for example &#x60;assets.ledger&#x60; and &#x60;tokens.ledger&#x60;, you can specify the full path. | 
 **active** | **bool**| Filters keys by status: &#x60;true&#x60; - active, &#x60;false&#x60; - removed. | [optional] 
 **key** | [**Key2**](.md)| Filters keys by JSON key. Note, this query parameter supports the following format: &#x60;?key{.path?}{.mode?}&#x3D;...&#x60;,             so you can specify a path to a particular field to filter by, for example: &#x60;?key.token_id&#x3D;...&#x60;. | [optional] 
 **value** | [**Value3**](.md)| Filters keys by JSON value. Note, this query parameter supports the following format: &#x60;?value{.path?}{.mode?}&#x3D;...&#x60;,             so you can specify a path to a particular field to filter by, for example: &#x60;?value.balance.gt&#x3D;...&#x60;. | [optional] 
 **last_level** | [**LastLevel2**](.md)| Filters bigmap keys by the last update level. | [optional] 
 **select** | [**Select12**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort17**](.md)| Sorts bigmap keys by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;firstLevel&#x60;, &#x60;lastLevel&#x60;, &#x60;updates&#x60;. | [optional] 
 **offset** | [**Offset15**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **micheline** | [**Micheline14**](.md)| Format of the bigmap key and value: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - Micheline, &#x60;3&#x60; - Micheline string | [optional] 

### Return type

[**list[BigMapKey]**](BigMapKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get_big_maps**
> list[BigMap] contracts_get_big_maps(address, tags=tags, select=select, sort=sort, offset=offset, limit=limit, micheline=micheline)

Get contract bigmaps

Returns all active bigmaps allocated in the contract storage.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
address = 'address_example' # str | Contract address
tags = swagger_client.Tags2() # Tags2 | Filters bigmaps tags (`metadata`, `token_metadata`, `ledger`). (optional)
select = swagger_client.Select11() # Select11 | Specify comma-separated list of fields to include into response or leave it undefined to return full object.             If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort16() # Sort16 | Sorts bigmaps by specified field. Supported fields: `id` (default), `firstLevel`, `lastLevel`, `totalKeys`, `activeKeys`, `updates`. (optional)
offset = swagger_client.Offset14() # Offset14 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
micheline = swagger_client.Micheline12() # Micheline12 | Format of the bigmap key and value: `0` - JSON, `1` - JSON string, `2` - Micheline, `3` - Micheline string (optional)

try:
    # Get contract bigmaps
    api_response = api_instance.contracts_get_big_maps(address, tags=tags, select=select, sort=sort, offset=offset, limit=limit, micheline=micheline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get_big_maps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Contract address | 
 **tags** | [**Tags2**](.md)| Filters bigmaps tags (&#x60;metadata&#x60;, &#x60;token_metadata&#x60;, &#x60;ledger&#x60;). | [optional] 
 **select** | [**Select11**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object.             If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort16**](.md)| Sorts bigmaps by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;firstLevel&#x60;, &#x60;lastLevel&#x60;, &#x60;totalKeys&#x60;, &#x60;activeKeys&#x60;, &#x60;updates&#x60;. | [optional] 
 **offset** | [**Offset14**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **micheline** | [**Micheline12**](.md)| Format of the bigmap key and value: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - Micheline, &#x60;3&#x60; - Micheline string | [optional] 

### Return type

[**list[BigMap]**](BigMap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get_by_address**
> Contract contracts_get_by_address(address)

Get contract by address

Returns a contract account with the specified address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
address = 'address_example' # str | Contract address (starting with KT)

try:
    # Get contract by address
    api_response = api_instance.contracts_get_by_address(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get_by_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Contract address (starting with KT) | 

### Return type

[**Contract**](Contract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get_code**
> str contracts_get_code(address, level=level, format=format)

Get contract code

Returns a code of the specified contract.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
address = 'address_example' # str | Contract address (starting with KT)
level = 0 # int | Level at which contract code should be taken. If `0` or not specified, the current value will be returned. (optional) (default to 0)
format = 0 # int | Code format (`0` - micheline, `1` - michelson, `2` - bytes (base64)) (optional) (default to 0)

try:
    # Get contract code
    api_response = api_instance.contracts_get_code(address, level=level, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Contract address (starting with KT) | 
 **level** | **int**| Level at which contract code should be taken. If &#x60;0&#x60; or not specified, the current value will be returned. | [optional] [default to 0]
 **format** | **int**| Code format (&#x60;0&#x60; - micheline, &#x60;1&#x60; - michelson, &#x60;2&#x60; - bytes (base64)) | [optional] [default to 0]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get_contract_view_by_name**
> ContractView contracts_get_contract_view_by_name(address, name, json=json, micheline=micheline, michelson=michelson)

Get view by name

Returns contract view with specified name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
address = 'address_example' # str | Contract address (starting with KT)
name = 'name_example' # str | View name
json = true # bool | Include parameter and return types in human-readable JSON format (optional) (default to true)
micheline = false # bool | Include parameter and return types in micheline format (optional) (default to false)
michelson = false # bool | Include parameter and return types in michelson format (optional) (default to false)

try:
    # Get view by name
    api_response = api_instance.contracts_get_contract_view_by_name(address, name, json=json, micheline=micheline, michelson=michelson)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get_contract_view_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Contract address (starting with KT) | 
 **name** | **str**| View name | 
 **json** | **bool**| Include parameter and return types in human-readable JSON format | [optional] [default to true]
 **micheline** | **bool**| Include parameter and return types in micheline format | [optional] [default to false]
 **michelson** | **bool**| Include parameter and return types in michelson format | [optional] [default to false]

### Return type

[**ContractView**](ContractView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get_contract_views**
> list[ContractView] contracts_get_contract_views(address, json=json, micheline=micheline, michelson=michelson)

Get contract views

Returns all views of the specified contract.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
address = 'address_example' # str | Contract address (starting with KT)
json = true # bool | Include parameter and return types in human-readable JSON format (optional) (default to true)
micheline = false # bool | Include parameter and return types in micheline format (optional) (default to false)
michelson = false # bool | Include parameter and return types in michelson format (optional) (default to false)

try:
    # Get contract views
    api_response = api_instance.contracts_get_contract_views(address, json=json, micheline=micheline, michelson=michelson)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get_contract_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Contract address (starting with KT) | 
 **json** | **bool**| Include parameter and return types in human-readable JSON format | [optional] [default to true]
 **micheline** | **bool**| Include parameter and return types in micheline format | [optional] [default to false]
 **michelson** | **bool**| Include parameter and return types in michelson format | [optional] [default to false]

### Return type

[**list[ContractView]**](ContractView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get_count**
> int contracts_get_count(kind=kind)

Get contracts count

Returns a number of contract accounts.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
kind = swagger_client.Kind3() # Kind3 | Contract kind to filter by (`delegator_contract` or `smart_contract`) (optional)

try:
    # Get contracts count
    api_response = api_instance.contracts_get_count(kind=kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kind** | [**Kind3**](.md)| Contract kind to filter by (&#x60;delegator_contract&#x60; or &#x60;smart_contract&#x60;) | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get_entrypoint_by_name**
> Entrypoint contracts_get_entrypoint_by_name(address, name, json=json, micheline=micheline, michelson=michelson)

Get entrypoint by name

Returns contract's entrypoint with specified name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
address = 'address_example' # str | Contract address (starting with KT)
name = 'name_example' # str | Entrypoint name
json = true # bool | Include parameters schema in human-readable JSON format (optional) (default to true)
micheline = false # bool | Include parameters schema in micheline format (optional) (default to false)
michelson = false # bool | Include parameters schema in michelson format (optional) (default to false)

try:
    # Get entrypoint by name
    api_response = api_instance.contracts_get_entrypoint_by_name(address, name, json=json, micheline=micheline, michelson=michelson)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get_entrypoint_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Contract address (starting with KT) | 
 **name** | **str**| Entrypoint name | 
 **json** | **bool**| Include parameters schema in human-readable JSON format | [optional] [default to true]
 **micheline** | **bool**| Include parameters schema in micheline format | [optional] [default to false]
 **michelson** | **bool**| Include parameters schema in michelson format | [optional] [default to false]

### Return type

[**Entrypoint**](Entrypoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get_entrypoints**
> list[Entrypoint] contracts_get_entrypoints(address, all=all, json=json, micheline=micheline, michelson=michelson)

Get contract entrypoints

Returns entrypoints of the specified contract.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
address = 'address_example' # str | Contract address (starting with KT)
all = false # bool | If true, returns all entrypoints, including unused ones.             Unused means that the entrypoint can be normalized to a more specific one.             For example here `(or %entry1 (unit %entry2) (nat %entry3))` the `%entry1` is unused entrypoint             because it can be normalized to `%entry2` or `%entry3` (optional) (default to false)
json = true # bool | Include parameters schema in human-readable JSON format (optional) (default to true)
micheline = false # bool | Include parameters schema in micheline format (optional) (default to false)
michelson = false # bool | Include parameters schema in michelson format (optional) (default to false)

try:
    # Get contract entrypoints
    api_response = api_instance.contracts_get_entrypoints(address, all=all, json=json, micheline=micheline, michelson=michelson)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get_entrypoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Contract address (starting with KT) | 
 **all** | **bool**| If true, returns all entrypoints, including unused ones.             Unused means that the entrypoint can be normalized to a more specific one.             For example here &#x60;(or %entry1 (unit %entry2) (nat %entry3))&#x60; the &#x60;%entry1&#x60; is unused entrypoint             because it can be normalized to &#x60;%entry2&#x60; or &#x60;%entry3&#x60; | [optional] [default to false]
 **json** | **bool**| Include parameters schema in human-readable JSON format | [optional] [default to true]
 **micheline** | **bool**| Include parameters schema in micheline format | [optional] [default to false]
 **michelson** | **bool**| Include parameters schema in michelson format | [optional] [default to false]

### Return type

[**list[Entrypoint]**](Entrypoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get_historical_keys**
> list[BigMapKeyHistorical] contracts_get_historical_keys(address, name, level, active=active, key=key, value=value, select=select, sort=sort, offset=offset, limit=limit, micheline=micheline)

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
api_instance = swagger_client.ContractsApi()
address = 'address_example' # str | Contract address
name = 'name_example' # str | Bigmap name is the last piece of the bigmap storage path.             For example, if the storage path is `ledger` or `assets.ledger`, then the name is `ledger`.             If there are multiple bigmaps with the same name, for example `assets.ledger` and `tokens.ledger`, you can specify the full path.
level = 56 # int | Level of the block at which you want to get bigmap keys
active = true # bool | Filters keys by status: `true` - active, `false` - removed. (optional)
key = swagger_client.Key3() # Key3 | Filters keys by JSON key. Note, this query parameter supports the following format: `?key{.path?}{.mode?}=...`,             so you can specify a path to a particular field to filter by, for example: `?key.token_id=...`. (optional)
value = swagger_client.Value4() # Value4 | Filters keys by JSON value. Note, this query parameter supports the following format: `?value{.path?}{.mode?}=...`,             so you can specify a path to a particular field to filter by, for example: `?value.balance.gt=...`. (optional)
select = swagger_client.Select13() # Select13 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort19() # Sort19 | Sorts bigmap keys by specified field. Supported fields: `id` (default). (optional)
offset = swagger_client.Offset17() # Offset17 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
micheline = swagger_client.Micheline17() # Micheline17 | Format of the bigmap key and value: `0` - JSON, `1` - JSON string, `2` - Micheline, `3` - Micheline string (optional)

try:
    # Get historical keys
    api_response = api_instance.contracts_get_historical_keys(address, name, level, active=active, key=key, value=value, select=select, sort=sort, offset=offset, limit=limit, micheline=micheline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get_historical_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Contract address | 
 **name** | **str**| Bigmap name is the last piece of the bigmap storage path.             For example, if the storage path is &#x60;ledger&#x60; or &#x60;assets.ledger&#x60;, then the name is &#x60;ledger&#x60;.             If there are multiple bigmaps with the same name, for example &#x60;assets.ledger&#x60; and &#x60;tokens.ledger&#x60;, you can specify the full path. | 
 **level** | **int**| Level of the block at which you want to get bigmap keys | 
 **active** | **bool**| Filters keys by status: &#x60;true&#x60; - active, &#x60;false&#x60; - removed. | [optional] 
 **key** | [**Key3**](.md)| Filters keys by JSON key. Note, this query parameter supports the following format: &#x60;?key{.path?}{.mode?}&#x3D;...&#x60;,             so you can specify a path to a particular field to filter by, for example: &#x60;?key.token_id&#x3D;...&#x60;. | [optional] 
 **value** | [**Value4**](.md)| Filters keys by JSON value. Note, this query parameter supports the following format: &#x60;?value{.path?}{.mode?}&#x3D;...&#x60;,             so you can specify a path to a particular field to filter by, for example: &#x60;?value.balance.gt&#x3D;...&#x60;. | [optional] 
 **select** | [**Select13**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort19**](.md)| Sorts bigmap keys by specified field. Supported fields: &#x60;id&#x60; (default). | [optional] 
 **offset** | [**Offset17**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **micheline** | [**Micheline17**](.md)| Format of the bigmap key and value: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - Micheline, &#x60;3&#x60; - Micheline string | [optional] 

### Return type

[**list[BigMapKeyHistorical]**](BigMapKeyHistorical.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get_interface**
> ContractInterface contracts_get_interface(address)

Get JSON Schema [2020-12] interface for the contract

Returns standard JSON Schema for contract storage, entrypoints, and Big_map entries.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
address = 'address_example' # str | Contract address

try:
    # Get JSON Schema [2020-12] interface for the contract
    api_response = api_instance.contracts_get_interface(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Contract address | 

### Return type

[**ContractInterface**](ContractInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get_key**
> BigMapKey contracts_get_key(address, name, key, micheline=micheline)

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
api_instance = swagger_client.ContractsApi()
address = 'address_example' # str | Contract address
name = 'name_example' # str | Bigmap name is the last piece of the bigmap storage path.             For example, if the storage path is `ledger` or `assets.ledger`, then the name is `ledger`.             If there are multiple bigmaps with the same name, for example `assets.ledger` and `tokens.ledger`, you can specify the full path.
key = 'key_example' # str | Either a key hash (`expr123...`) or a plain value (`abcde...`).             Even if the key is complex (an object or an array), you can specify it as is, for example, `/keys/{\"address\":\"tz123\",\"nat\":\"123\"}`.
micheline = swagger_client.Micheline15() # Micheline15 | Format of the bigmap key and value: `0` - JSON, `1` - JSON string, `2` - Micheline, `3` - Micheline string (optional)

try:
    # Get bigmap key
    api_response = api_instance.contracts_get_key(address, name, key, micheline=micheline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Contract address | 
 **name** | **str**| Bigmap name is the last piece of the bigmap storage path.             For example, if the storage path is &#x60;ledger&#x60; or &#x60;assets.ledger&#x60;, then the name is &#x60;ledger&#x60;.             If there are multiple bigmaps with the same name, for example &#x60;assets.ledger&#x60; and &#x60;tokens.ledger&#x60;, you can specify the full path. | 
 **key** | **str**| Either a key hash (&#x60;expr123...&#x60;) or a plain value (&#x60;abcde...&#x60;).             Even if the key is complex (an object or an array), you can specify it as is, for example, &#x60;/keys/{\&quot;address\&quot;:\&quot;tz123\&quot;,\&quot;nat\&quot;:\&quot;123\&quot;}&#x60;. | 
 **micheline** | [**Micheline15**](.md)| Format of the bigmap key and value: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - Micheline, &#x60;3&#x60; - Micheline string | [optional] 

### Return type

[**BigMapKey**](BigMapKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get_key2**
> BigMapKeyHistorical contracts_get_key2(address, name, level, key, micheline=micheline)

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
api_instance = swagger_client.ContractsApi()
address = 'address_example' # str | Contract address
name = 'name_example' # str | Bigmap name is the last piece of the bigmap storage path.             For example, if the storage path is `ledger` or `assets.ledger`, then the name is `ledger`.             If there are multiple bigmaps with the same name, for example `assets.ledger` and `tokens.ledger`, you can specify the full path.
level = 56 # int | Level of the block at which you want to get bigmap key
key = 'key_example' # str | Either a key hash (`expr123...`) or a plain value (`abcde...`).             Even if the key is complex (an object or an array), you can specify it as is, for example, `/keys/{\"address\":\"tz123\",\"nat\":\"123\"}`.
micheline = swagger_client.Micheline18() # Micheline18 | Format of the bigmap key and value: `0` - JSON, `1` - JSON string, `2` - Micheline, `3` - Micheline string (optional)

try:
    # Get historical key
    api_response = api_instance.contracts_get_key2(address, name, level, key, micheline=micheline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get_key2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Contract address | 
 **name** | **str**| Bigmap name is the last piece of the bigmap storage path.             For example, if the storage path is &#x60;ledger&#x60; or &#x60;assets.ledger&#x60;, then the name is &#x60;ledger&#x60;.             If there are multiple bigmaps with the same name, for example &#x60;assets.ledger&#x60; and &#x60;tokens.ledger&#x60;, you can specify the full path. | 
 **level** | **int**| Level of the block at which you want to get bigmap key | 
 **key** | **str**| Either a key hash (&#x60;expr123...&#x60;) or a plain value (&#x60;abcde...&#x60;).             Even if the key is complex (an object or an array), you can specify it as is, for example, &#x60;/keys/{\&quot;address\&quot;:\&quot;tz123\&quot;,\&quot;nat\&quot;:\&quot;123\&quot;}&#x60;. | 
 **micheline** | [**Micheline18**](.md)| Format of the bigmap key and value: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - Micheline, &#x60;3&#x60; - Micheline string | [optional] 

### Return type

[**BigMapKeyHistorical**](BigMapKeyHistorical.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get_key_updates**
> list[BigMapKeyUpdate] contracts_get_key_updates(address, name, key, sort=sort, offset=offset, limit=limit, micheline=micheline)

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
api_instance = swagger_client.ContractsApi()
address = 'address_example' # str | Contract address
name = 'name_example' # str | Bigmap name is the last piece of the bigmap storage path.             For example, if the storage path is `ledger` or `assets.ledger`, then the name is `ledger`.             If there are multiple bigmaps with the same name, for example `assets.ledger` and `tokens.ledger`, you can specify the full path.
key = 'key_example' # str | Either a key hash (`expr123...`) or a plain value (`abcde...`).             Even if the key is complex (an object or an array), you can specify it as is, for example, `/keys/{\"address\":\"tz123\",\"nat\":\"123\"}`.
sort = swagger_client.Sort18() # Sort18 | Sorts bigmap updates by specified field. Supported fields: `id` (default). (optional)
offset = swagger_client.Offset16() # Offset16 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
micheline = swagger_client.Micheline16() # Micheline16 | Format of the key value: `0` - JSON, `1` - JSON string, `2` - Micheline, `3` - Micheline string (optional)

try:
    # Get bigmap key updates
    api_response = api_instance.contracts_get_key_updates(address, name, key, sort=sort, offset=offset, limit=limit, micheline=micheline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get_key_updates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Contract address | 
 **name** | **str**| Bigmap name is the last piece of the bigmap storage path.             For example, if the storage path is &#x60;ledger&#x60; or &#x60;assets.ledger&#x60;, then the name is &#x60;ledger&#x60;.             If there are multiple bigmaps with the same name, for example &#x60;assets.ledger&#x60; and &#x60;tokens.ledger&#x60;, you can specify the full path. | 
 **key** | **str**| Either a key hash (&#x60;expr123...&#x60;) or a plain value (&#x60;abcde...&#x60;).             Even if the key is complex (an object or an array), you can specify it as is, for example, &#x60;/keys/{\&quot;address\&quot;:\&quot;tz123\&quot;,\&quot;nat\&quot;:\&quot;123\&quot;}&#x60;. | 
 **sort** | [**Sort18**](.md)| Sorts bigmap updates by specified field. Supported fields: &#x60;id&#x60; (default). | [optional] 
 **offset** | [**Offset16**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **micheline** | [**Micheline16**](.md)| Format of the key value: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - Micheline, &#x60;3&#x60; - Micheline string | [optional] 

### Return type

[**list[BigMapKeyUpdate]**](BigMapKeyUpdate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get_raw_storage**
> IMicheline contracts_get_raw_storage(address, level=level)

Get raw contract storage

Returns raw contract storage value in micheline format.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
address = 'address_example' # str | Contract address
level = 0 # int | Level at which storage value should be taken. If `0` or not specified, the current value will be returned. (optional) (default to 0)

try:
    # Get raw contract storage
    api_response = api_instance.contracts_get_raw_storage(address, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get_raw_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Contract address | 
 **level** | **int**| Level at which storage value should be taken. If &#x60;0&#x60; or not specified, the current value will be returned. | [optional] [default to 0]

### Return type

[**IMicheline**](IMicheline.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get_raw_storage_history**
> list[StorageRecord] contracts_get_raw_storage_history(address, last_id=last_id, limit=limit)

Get raw contract storage history

Returns raw contract storage historical values.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
address = 'address_example' # str | Contract address
last_id = 0 # int | Id of the last item received (for pagination) (optional) (default to 0)
limit = 10 # int | Maximum number of items to return (optional) (default to 10)

try:
    # Get raw contract storage history
    api_response = api_instance.contracts_get_raw_storage_history(address, last_id=last_id, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get_raw_storage_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Contract address | 
 **last_id** | **int**| Id of the last item received (for pagination) | [optional] [default to 0]
 **limit** | **int**| Maximum number of items to return | [optional] [default to 10]

### Return type

[**list[StorageRecord]**](StorageRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get_raw_storage_schema**
> IMicheline contracts_get_raw_storage_schema(address, level=level)

Get raw contract storage schema

Returns micheline schema (type) of the contract storage.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
address = 'address_example' # str | Contract address
level = 0 # int | Level at which storage schema should be taken. If `0` or not specified, the current schema will be returned. (optional) (default to 0)

try:
    # Get raw contract storage schema
    api_response = api_instance.contracts_get_raw_storage_schema(address, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get_raw_storage_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Contract address | 
 **level** | **int**| Level at which storage schema should be taken. If &#x60;0&#x60; or not specified, the current schema will be returned. | [optional] [default to 0]

### Return type

[**IMicheline**](IMicheline.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get_same**
> list[Contract] contracts_get_same(address, select=select, sort=sort, offset=offset, limit=limit, include_storage=include_storage)

Get same contracts

Returns contracts which have the same script as the specified one. Note, contract scripts are compared by 32-bit hash, so in very rare cases there may be collisions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
address = 'address_example' # str | Contract address (starting with KT)
select = swagger_client.Select9() # Select9 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort14() # Sort14 | Sorts contracts by specified field. Supported fields: `id` (default), `balance`, `firstActivity`, `lastActivity`, `numTransactions`. (optional)
offset = swagger_client.Offset12() # Offset12 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
include_storage = false # bool | Specifies whether to include contract storage value in response. (optional) (default to false)

try:
    # Get same contracts
    api_response = api_instance.contracts_get_same(address, select=select, sort=sort, offset=offset, limit=limit, include_storage=include_storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get_same: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Contract address (starting with KT) | 
 **select** | [**Select9**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort14**](.md)| Sorts contracts by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;balance&#x60;, &#x60;firstActivity&#x60;, &#x60;lastActivity&#x60;, &#x60;numTransactions&#x60;. | [optional] 
 **offset** | [**Offset12**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **include_storage** | **bool**| Specifies whether to include contract storage value in response. | [optional] [default to false]

### Return type

[**list[Contract]**](Contract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get_similar**
> list[Contract] contracts_get_similar(address, select=select, sort=sort, offset=offset, limit=limit, include_storage=include_storage)

Get similar contracts

Returns contracts which have the same interface (parameter and storage types) as the specified one. Note, contract parameter and storage types are compared by 32-bit hash, so in very rare cases there may be collisions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
address = 'address_example' # str | Contract address (starting with KT)
select = swagger_client.Select10() # Select10 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort15() # Sort15 | Sorts contracts by specified field. Supported fields: `id` (default), `balance`, `firstActivity`, `lastActivity`, `numTransactions`. (optional)
offset = swagger_client.Offset13() # Offset13 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
include_storage = false # bool | Specifies whether to include contract storage value in response. (optional) (default to false)

try:
    # Get similar contracts
    api_response = api_instance.contracts_get_similar(address, select=select, sort=sort, offset=offset, limit=limit, include_storage=include_storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get_similar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Contract address (starting with KT) | 
 **select** | [**Select10**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort15**](.md)| Sorts contracts by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;balance&#x60;, &#x60;firstActivity&#x60;, &#x60;lastActivity&#x60;, &#x60;numTransactions&#x60;. | [optional] 
 **offset** | [**Offset13**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **include_storage** | **bool**| Specifies whether to include contract storage value in response. | [optional] [default to false]

### Return type

[**list[Contract]**](Contract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get_storage**
> str contracts_get_storage(address, level=level, path=path)

Get contract storage

Returns contract storage value in JSON format.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
address = 'address_example' # str | Contract address
level = 0 # int | Level at which storage value should be taken. If `0` or not specified, the current value will be returned. (optional) (default to 0)
path = 'path_example' # str | Path in the JSON value (point-separated list of field names, e.g. `path=settings.refund_time` to return (optional)

try:
    # Get contract storage
    api_response = api_instance.contracts_get_storage(address, level=level, path=path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Contract address | 
 **level** | **int**| Level at which storage value should be taken. If &#x60;0&#x60; or not specified, the current value will be returned. | [optional] [default to 0]
 **path** | **str**| Path in the JSON value (point-separated list of field names, e.g. &#x60;path&#x3D;settings.refund_time&#x60; to return | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get_storage_history**
> list[StorageRecord] contracts_get_storage_history(address, last_id=last_id, limit=limit)

Get contract storage history

Returns contract storage historical values.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
address = 'address_example' # str | Contract address
last_id = 0 # int | Id of the last item received (for pagination) (optional) (default to 0)
limit = 10 # int | Maximum number of items to return (optional) (default to 10)

try:
    # Get contract storage history
    api_response = api_instance.contracts_get_storage_history(address, last_id=last_id, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get_storage_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Contract address | 
 **last_id** | **int**| Id of the last item received (for pagination) | [optional] [default to 0]
 **limit** | **int**| Maximum number of items to return | [optional] [default to 10]

### Return type

[**list[StorageRecord]**](StorageRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_get_storage_schema**
> str contracts_get_storage_schema(address, level=level)

Get contract storage schema

Returns JSON schema of the contract storage.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
address = 'address_example' # str | Contract address
level = 0 # int | Level at which storage schema should be taken. If `0` or not specified, the current schema will be returned. (optional) (default to 0)

try:
    # Get contract storage schema
    api_response = api_instance.contracts_get_storage_schema(address, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get_storage_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Contract address | 
 **level** | **int**| Level at which storage schema should be taken. If &#x60;0&#x60; or not specified, the current schema will be returned. | [optional] [default to 0]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

