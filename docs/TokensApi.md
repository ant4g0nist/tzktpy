# swagger_client.TokensApi

All URIs are relative to *https://api.tzkt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tokens_get_token_balances**](TokensApi.md#tokens_get_token_balances) | **GET** /v1/tokens/balances | Get token balances
[**tokens_get_token_balances2**](TokensApi.md#tokens_get_token_balances2) | **GET** /v1/tokens/historical_balances/{level} | Get historical token balances
[**tokens_get_token_balances_count**](TokensApi.md#tokens_get_token_balances_count) | **GET** /v1/tokens/balances/count | Get token balances count
[**tokens_get_token_transfers**](TokensApi.md#tokens_get_token_transfers) | **GET** /v1/tokens/transfers | Get token transfers
[**tokens_get_token_transfers_count**](TokensApi.md#tokens_get_token_transfers_count) | **GET** /v1/tokens/transfers/count | Get token transfers count
[**tokens_get_tokens**](TokensApi.md#tokens_get_tokens) | **GET** /v1/tokens | Get tokens
[**tokens_get_tokens_count**](TokensApi.md#tokens_get_tokens_count) | **GET** /v1/tokens/count | Get tokens count

# **tokens_get_token_balances**
> list[TokenBalance] tokens_get_token_balances(id=id, account=account, token_id=token_id, token_contract=token_contract, token_token_id=token_token_id, token_standard=token_standard, token_metadata=token_metadata, token_has_filters=token_has_filters, balance=balance, first_level=first_level, first_time=first_time, last_level=last_level, last_time=last_time, sort=sort, offset=offset, limit=limit, select=select)

Get token balances

Returns a list of token balances.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokensApi()
id = swagger_client.Id6() # Id6 | Filter by internal TzKT id.   Click on the parameter to expand more details. (optional)
account = swagger_client.Account3() # Account3 | Filter by account address.   Click on the parameter to expand more details. (optional)
token_id = swagger_client.TokenId1() # TokenId1 | Filter by internal TzKT id. Note, this is not the same as `tokenId`.   Click on the parameter to expand more details. (optional)
token_contract = swagger_client.TokenContract1() # TokenContract1 | Filter by contract address.   Click on the parameter to expand more details. (optional)
token_token_id = swagger_client.TokenTokenId1() # TokenTokenId1 | Filter by tokenId (for FA1.2 tokens tokenId is always `\"0\"`).   Click on the parameter to expand more details. (optional)
token_standard = swagger_client.TokenStandard1() # TokenStandard1 | Filter by token standard (`fa1.2` or `fa2`).   Click on the parameter to expand more details. (optional)
token_metadata = swagger_client.TokenMetadata1() # TokenMetadata1 | Filter by metadata. Note, this parameter supports the following format: `token.metadata{.path?}{.mode?}=...`, so you can specify a path to a particular field to filter by, for example: `?token.metadata.symbol.in=kUSD,uUSD`.   Click on the parameter to expand more details. (optional)
token_has_filters = true # bool |  (optional)
balance = swagger_client.Balance7() # Balance7 | Filter by balance.   Click on the parameter to expand more details. (optional)
first_level = swagger_client.FirstLevel3() # FirstLevel3 | Filter by level of the block where the balance was first changed.   Click on the parameter to expand more details. (optional)
first_time = swagger_client.FirstTime3() # FirstTime3 | Filter by timestamp (ISO 8601) of the block where the balance was first changed.   Click on the parameter to expand more details. (optional)
last_level = swagger_client.LastLevel6() # LastLevel6 | Filter by level of the block where the balance was last seen.   Click on the parameter to expand more details. (optional)
last_time = swagger_client.LastTime3() # LastTime3 | Filter by timestamp (ISO 8601) of the block where the balance was last changed.   Click on the parameter to expand more details. (optional)
sort = swagger_client.Sort51() # Sort51 | Sorts items (asc or desc) by the specified field. You can see what fields can be used for sorting in the response description, below.   Click on the parameter to expand more details. (optional)
offset = swagger_client.Offset49() # Offset49 | Specifies which or how many items should be skipped.   Click on the parameter to expand more details. (optional)
limit = 56 # int | Maximum number of items to return. (optional)
select = swagger_client.Select45() # Select45 | Specify a comma-separated list of fields to include into response or leave it undefined to get default set of fields. This parameter accepts values of the following format: `{field}{path?}{as alias?}`, so you can do deep selection (for example, `?select=balance,token.metadata.symbol as token,...`).   Note, if you select just one field, the response will be flatten into a simple array of values.   Click on the parameter to expand the details. (optional)

try:
    # Get token balances
    api_response = api_instance.tokens_get_token_balances(id=id, account=account, token_id=token_id, token_contract=token_contract, token_token_id=token_token_id, token_standard=token_standard, token_metadata=token_metadata, token_has_filters=token_has_filters, balance=balance, first_level=first_level, first_time=first_time, last_level=last_level, last_time=last_time, sort=sort, offset=offset, limit=limit, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApi->tokens_get_token_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id6**](.md)| Filter by internal TzKT id.   Click on the parameter to expand more details. | [optional] 
 **account** | [**Account3**](.md)| Filter by account address.   Click on the parameter to expand more details. | [optional] 
 **token_id** | [**TokenId1**](.md)| Filter by internal TzKT id. Note, this is not the same as &#x60;tokenId&#x60;.   Click on the parameter to expand more details. | [optional] 
 **token_contract** | [**TokenContract1**](.md)| Filter by contract address.   Click on the parameter to expand more details. | [optional] 
 **token_token_id** | [**TokenTokenId1**](.md)| Filter by tokenId (for FA1.2 tokens tokenId is always &#x60;\&quot;0\&quot;&#x60;).   Click on the parameter to expand more details. | [optional] 
 **token_standard** | [**TokenStandard1**](.md)| Filter by token standard (&#x60;fa1.2&#x60; or &#x60;fa2&#x60;).   Click on the parameter to expand more details. | [optional] 
 **token_metadata** | [**TokenMetadata1**](.md)| Filter by metadata. Note, this parameter supports the following format: &#x60;token.metadata{.path?}{.mode?}&#x3D;...&#x60;, so you can specify a path to a particular field to filter by, for example: &#x60;?token.metadata.symbol.in&#x3D;kUSD,uUSD&#x60;.   Click on the parameter to expand more details. | [optional] 
 **token_has_filters** | **bool**|  | [optional] 
 **balance** | [**Balance7**](.md)| Filter by balance.   Click on the parameter to expand more details. | [optional] 
 **first_level** | [**FirstLevel3**](.md)| Filter by level of the block where the balance was first changed.   Click on the parameter to expand more details. | [optional] 
 **first_time** | [**FirstTime3**](.md)| Filter by timestamp (ISO 8601) of the block where the balance was first changed.   Click on the parameter to expand more details. | [optional] 
 **last_level** | [**LastLevel6**](.md)| Filter by level of the block where the balance was last seen.   Click on the parameter to expand more details. | [optional] 
 **last_time** | [**LastTime3**](.md)| Filter by timestamp (ISO 8601) of the block where the balance was last changed.   Click on the parameter to expand more details. | [optional] 
 **sort** | [**Sort51**](.md)| Sorts items (asc or desc) by the specified field. You can see what fields can be used for sorting in the response description, below.   Click on the parameter to expand more details. | [optional] 
 **offset** | [**Offset49**](.md)| Specifies which or how many items should be skipped.   Click on the parameter to expand more details. | [optional] 
 **limit** | **int**| Maximum number of items to return. | [optional] 
 **select** | [**Select45**](.md)| Specify a comma-separated list of fields to include into response or leave it undefined to get default set of fields. This parameter accepts values of the following format: &#x60;{field}{path?}{as alias?}&#x60;, so you can do deep selection (for example, &#x60;?select&#x3D;balance,token.metadata.symbol as token,...&#x60;).   Note, if you select just one field, the response will be flatten into a simple array of values.   Click on the parameter to expand the details. | [optional] 

### Return type

[**list[TokenBalance]**](TokenBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_get_token_balances2**
> list[TokenBalanceShort] tokens_get_token_balances2(level, account=account, token_id=token_id, token_contract=token_contract, token_token_id=token_token_id, token_standard=token_standard, token_metadata=token_metadata, token_has_filters=token_has_filters, balance=balance, sort=sort, offset=offset, limit=limit, select=select)

Get historical token balances

Returns a list of token balances at the end of the specified block. Note, this endpoint is quite heavy, therefore at least one of the filters (`account`, `token.id`, `token.contract` with `token.tokenId`) must be specified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokensApi()
level = 56 # int | Level of the block at the end of which historical balances must be calculated
account = swagger_client.Account4() # Account4 | Filter by account address.   Click on the parameter to expand more details. (optional)
token_id = swagger_client.TokenId4() # TokenId4 | Filter by internal TzKT id. Note, this is not the same as `tokenId`.   Click on the parameter to expand more details. (optional)
token_contract = swagger_client.TokenContract4() # TokenContract4 | Filter by contract address.   Click on the parameter to expand more details. (optional)
token_token_id = swagger_client.TokenTokenId4() # TokenTokenId4 | Filter by tokenId (for FA1.2 tokens tokenId is always `\"0\"`).   Click on the parameter to expand more details. (optional)
token_standard = swagger_client.TokenStandard4() # TokenStandard4 | Filter by token standard (`fa1.2` or `fa2`).   Click on the parameter to expand more details. (optional)
token_metadata = swagger_client.TokenMetadata4() # TokenMetadata4 | Filter by metadata. Note, this parameter supports the following format: `token.metadata{.path?}{.mode?}=...`, so you can specify a path to a particular field to filter by, for example: `?token.metadata.symbol.in=kUSD,uUSD`.   Click on the parameter to expand more details. (optional)
token_has_filters = true # bool |  (optional)
balance = swagger_client.Balance8() # Balance8 | Filter by balance.   Click on the parameter to expand more details. (optional)
sort = swagger_client.Sort53() # Sort53 | Sorts items (asc or desc) by the specified field. You can see what fields can be used for sorting in the response description, below.   Click on the parameter to expand more details. (optional)
offset = swagger_client.Offset51() # Offset51 | Specifies which or how many items should be skipped.   Click on the parameter to expand more details. (optional)
limit = 56 # int | Maximum number of items to return. (optional)
select = swagger_client.Select47() # Select47 | Specify a comma-separated list of fields to include into response or leave it undefined to get default set of fields. This parameter accepts values of the following format: `{field}{path?}{as alias?}`, so you can do deep selection (for example, `?select=balance,token.metadata.symbol as token,...`).   Note, if you select just one field, the response will be flatten into a simple array of values.   Click on the parameter to expand the details. (optional)

try:
    # Get historical token balances
    api_response = api_instance.tokens_get_token_balances2(level, account=account, token_id=token_id, token_contract=token_contract, token_token_id=token_token_id, token_standard=token_standard, token_metadata=token_metadata, token_has_filters=token_has_filters, balance=balance, sort=sort, offset=offset, limit=limit, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApi->tokens_get_token_balances2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **int**| Level of the block at the end of which historical balances must be calculated | 
 **account** | [**Account4**](.md)| Filter by account address.   Click on the parameter to expand more details. | [optional] 
 **token_id** | [**TokenId4**](.md)| Filter by internal TzKT id. Note, this is not the same as &#x60;tokenId&#x60;.   Click on the parameter to expand more details. | [optional] 
 **token_contract** | [**TokenContract4**](.md)| Filter by contract address.   Click on the parameter to expand more details. | [optional] 
 **token_token_id** | [**TokenTokenId4**](.md)| Filter by tokenId (for FA1.2 tokens tokenId is always &#x60;\&quot;0\&quot;&#x60;).   Click on the parameter to expand more details. | [optional] 
 **token_standard** | [**TokenStandard4**](.md)| Filter by token standard (&#x60;fa1.2&#x60; or &#x60;fa2&#x60;).   Click on the parameter to expand more details. | [optional] 
 **token_metadata** | [**TokenMetadata4**](.md)| Filter by metadata. Note, this parameter supports the following format: &#x60;token.metadata{.path?}{.mode?}&#x3D;...&#x60;, so you can specify a path to a particular field to filter by, for example: &#x60;?token.metadata.symbol.in&#x3D;kUSD,uUSD&#x60;.   Click on the parameter to expand more details. | [optional] 
 **token_has_filters** | **bool**|  | [optional] 
 **balance** | [**Balance8**](.md)| Filter by balance.   Click on the parameter to expand more details. | [optional] 
 **sort** | [**Sort53**](.md)| Sorts items (asc or desc) by the specified field. You can see what fields can be used for sorting in the response description, below.   Click on the parameter to expand more details. | [optional] 
 **offset** | [**Offset51**](.md)| Specifies which or how many items should be skipped.   Click on the parameter to expand more details. | [optional] 
 **limit** | **int**| Maximum number of items to return. | [optional] 
 **select** | [**Select47**](.md)| Specify a comma-separated list of fields to include into response or leave it undefined to get default set of fields. This parameter accepts values of the following format: &#x60;{field}{path?}{as alias?}&#x60;, so you can do deep selection (for example, &#x60;?select&#x3D;balance,token.metadata.symbol as token,...&#x60;).   Note, if you select just one field, the response will be flatten into a simple array of values.   Click on the parameter to expand the details. | [optional] 

### Return type

[**list[TokenBalanceShort]**](TokenBalanceShort.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_get_token_balances_count**
> int tokens_get_token_balances_count(id=id, account=account, token_id=token_id, token_contract=token_contract, token_token_id=token_token_id, token_standard=token_standard, token_metadata=token_metadata, token_has_filters=token_has_filters, balance=balance, first_level=first_level, first_time=first_time, last_level=last_level, last_time=last_time)

Get token balances count

Returns a total number of token balances.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokensApi()
id = swagger_client.Id5() # Id5 | Filter by internal TzKT id.   Click on the parameter to expand more details. (optional)
account = swagger_client.Account2() # Account2 | Filter by account address.   Click on the parameter to expand more details. (optional)
token_id = swagger_client.TokenId() # TokenId | Filter by internal TzKT id. Note, this is not the same as `tokenId`.   Click on the parameter to expand more details. (optional)
token_contract = swagger_client.TokenContract() # TokenContract | Filter by contract address.   Click on the parameter to expand more details. (optional)
token_token_id = swagger_client.TokenTokenId() # TokenTokenId | Filter by tokenId (for FA1.2 tokens tokenId is always `\"0\"`).   Click on the parameter to expand more details. (optional)
token_standard = swagger_client.TokenStandard() # TokenStandard | Filter by token standard (`fa1.2` or `fa2`).   Click on the parameter to expand more details. (optional)
token_metadata = swagger_client.TokenMetadata() # TokenMetadata | Filter by metadata. Note, this parameter supports the following format: `token.metadata{.path?}{.mode?}=...`, so you can specify a path to a particular field to filter by, for example: `?token.metadata.symbol.in=kUSD,uUSD`.   Click on the parameter to expand more details. (optional)
token_has_filters = true # bool |  (optional)
balance = swagger_client.Balance6() # Balance6 | Filter by balance.   Click on the parameter to expand more details. (optional)
first_level = swagger_client.FirstLevel2() # FirstLevel2 | Filter by level of the block where the balance was first changed.   Click on the parameter to expand more details. (optional)
first_time = swagger_client.FirstTime2() # FirstTime2 | Filter by timestamp (ISO 8601) of the block where the balance was first changed.   Click on the parameter to expand more details. (optional)
last_level = swagger_client.LastLevel5() # LastLevel5 | Filter by level of the block where the balance was last seen.   Click on the parameter to expand more details. (optional)
last_time = swagger_client.LastTime2() # LastTime2 | Filter by timestamp (ISO 8601) of the block where the balance was last changed.   Click on the parameter to expand more details. (optional)

try:
    # Get token balances count
    api_response = api_instance.tokens_get_token_balances_count(id=id, account=account, token_id=token_id, token_contract=token_contract, token_token_id=token_token_id, token_standard=token_standard, token_metadata=token_metadata, token_has_filters=token_has_filters, balance=balance, first_level=first_level, first_time=first_time, last_level=last_level, last_time=last_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApi->tokens_get_token_balances_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id5**](.md)| Filter by internal TzKT id.   Click on the parameter to expand more details. | [optional] 
 **account** | [**Account2**](.md)| Filter by account address.   Click on the parameter to expand more details. | [optional] 
 **token_id** | [**TokenId**](.md)| Filter by internal TzKT id. Note, this is not the same as &#x60;tokenId&#x60;.   Click on the parameter to expand more details. | [optional] 
 **token_contract** | [**TokenContract**](.md)| Filter by contract address.   Click on the parameter to expand more details. | [optional] 
 **token_token_id** | [**TokenTokenId**](.md)| Filter by tokenId (for FA1.2 tokens tokenId is always &#x60;\&quot;0\&quot;&#x60;).   Click on the parameter to expand more details. | [optional] 
 **token_standard** | [**TokenStandard**](.md)| Filter by token standard (&#x60;fa1.2&#x60; or &#x60;fa2&#x60;).   Click on the parameter to expand more details. | [optional] 
 **token_metadata** | [**TokenMetadata**](.md)| Filter by metadata. Note, this parameter supports the following format: &#x60;token.metadata{.path?}{.mode?}&#x3D;...&#x60;, so you can specify a path to a particular field to filter by, for example: &#x60;?token.metadata.symbol.in&#x3D;kUSD,uUSD&#x60;.   Click on the parameter to expand more details. | [optional] 
 **token_has_filters** | **bool**|  | [optional] 
 **balance** | [**Balance6**](.md)| Filter by balance.   Click on the parameter to expand more details. | [optional] 
 **first_level** | [**FirstLevel2**](.md)| Filter by level of the block where the balance was first changed.   Click on the parameter to expand more details. | [optional] 
 **first_time** | [**FirstTime2**](.md)| Filter by timestamp (ISO 8601) of the block where the balance was first changed.   Click on the parameter to expand more details. | [optional] 
 **last_level** | [**LastLevel5**](.md)| Filter by level of the block where the balance was last seen.   Click on the parameter to expand more details. | [optional] 
 **last_time** | [**LastTime2**](.md)| Filter by timestamp (ISO 8601) of the block where the balance was last changed.   Click on the parameter to expand more details. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_get_token_transfers**
> list[TokenTransfer] tokens_get_token_transfers(id=id, level=level, timestamp=timestamp, token_id=token_id, token_contract=token_contract, token_token_id=token_token_id, token_standard=token_standard, token_metadata=token_metadata, token_has_filters=token_has_filters, anyof=anyof, _from=_from, to=to, amount=amount, transaction_id=transaction_id, origination_id=origination_id, migration_id=migration_id, sort=sort, offset=offset, limit=limit, select=select)

Get token transfers

Returns a list of token transfers.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokensApi()
id = swagger_client.Id8() # Id8 | Filter by internal TzKT id.   Click on the parameter to expand more details. (optional)
level = swagger_client.Level46() # Level46 | Filter by level of the block where the transfer was made.   Click on the parameter to expand more details. (optional)
timestamp = swagger_client.Timestamp44() # Timestamp44 | Filter by timestamp (ISO 8601) of the block where the transfer was made.   Click on the parameter to expand more details. (optional)
token_id = swagger_client.TokenId3() # TokenId3 | Filter by internal TzKT id. Note, this is not the same as `tokenId`.   Click on the parameter to expand more details. (optional)
token_contract = swagger_client.TokenContract3() # TokenContract3 | Filter by contract address.   Click on the parameter to expand more details. (optional)
token_token_id = swagger_client.TokenTokenId3() # TokenTokenId3 | Filter by tokenId (for FA1.2 tokens tokenId is always `\"0\"`).   Click on the parameter to expand more details. (optional)
token_standard = swagger_client.TokenStandard3() # TokenStandard3 | Filter by token standard (`fa1.2` or `fa2`).   Click on the parameter to expand more details. (optional)
token_metadata = swagger_client.TokenMetadata3() # TokenMetadata3 | Filter by metadata. Note, this parameter supports the following format: `token.metadata{.path?}{.mode?}=...`, so you can specify a path to a particular field to filter by, for example: `?token.metadata.symbol.in=kUSD,uUSD`.   Click on the parameter to expand more details. (optional)
token_has_filters = true # bool |  (optional)
anyof = 'anyof_example' # str | Filter by any of the specified fields (`from` or `to`). Example: `anyof.from.to=tz1...` will return transfers where `from` OR `to` is equal to the specified value. This parameter is useful when you need to get both incoming and outgoing transfers of the account at once.   Click on the parameter to expand more details. (optional)
_from = swagger_client.From1() # From1 | Filter by sender account address.   Click on the parameter to expand more details. (optional)
to = swagger_client.To1() # To1 | Filter by target account address.   Click on the parameter to expand more details. (optional)
amount = swagger_client.Amount2() # Amount2 | Filter by amount.   Click on the parameter to expand more details. (optional)
transaction_id = swagger_client.TransactionId1() # TransactionId1 | Filter by id of the transaction, caused the token transfer.   Click on the parameter to expand more details. (optional)
origination_id = swagger_client.OriginationId1() # OriginationId1 | Filter by id of the origination, caused the token transfer.   Click on the parameter to expand more details. (optional)
migration_id = swagger_client.MigrationId1() # MigrationId1 | Filter by id of the migration, caused the token transfer.   Click on the parameter to expand more details. (optional)
sort = swagger_client.Sort52() # Sort52 | Sorts items (asc or desc) by the specified field. You can see what fields can be used for sorting in the response description, below.   Click on the parameter to expand more details. (optional)
offset = swagger_client.Offset50() # Offset50 | Specifies which or how many items should be skipped.   Click on the parameter to expand more details. (optional)
limit = 56 # int | Maximum number of items to return. (optional)
select = swagger_client.Select46() # Select46 | Specify a comma-separated list of fields to include into response or leave it undefined to get default set of fields. This parameter accepts values of the following format: `{field}{path?}{as alias?}`, so you can do deep selection (for example, `?select=balance,token.metadata.symbol as token,...`).   Note, if you select just one field, the response will be flatten into a simple array of values.   Click on the parameter to expand the details. (optional)

try:
    # Get token transfers
    api_response = api_instance.tokens_get_token_transfers(id=id, level=level, timestamp=timestamp, token_id=token_id, token_contract=token_contract, token_token_id=token_token_id, token_standard=token_standard, token_metadata=token_metadata, token_has_filters=token_has_filters, anyof=anyof, _from=_from, to=to, amount=amount, transaction_id=transaction_id, origination_id=origination_id, migration_id=migration_id, sort=sort, offset=offset, limit=limit, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApi->tokens_get_token_transfers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id8**](.md)| Filter by internal TzKT id.   Click on the parameter to expand more details. | [optional] 
 **level** | [**Level46**](.md)| Filter by level of the block where the transfer was made.   Click on the parameter to expand more details. | [optional] 
 **timestamp** | [**Timestamp44**](.md)| Filter by timestamp (ISO 8601) of the block where the transfer was made.   Click on the parameter to expand more details. | [optional] 
 **token_id** | [**TokenId3**](.md)| Filter by internal TzKT id. Note, this is not the same as &#x60;tokenId&#x60;.   Click on the parameter to expand more details. | [optional] 
 **token_contract** | [**TokenContract3**](.md)| Filter by contract address.   Click on the parameter to expand more details. | [optional] 
 **token_token_id** | [**TokenTokenId3**](.md)| Filter by tokenId (for FA1.2 tokens tokenId is always &#x60;\&quot;0\&quot;&#x60;).   Click on the parameter to expand more details. | [optional] 
 **token_standard** | [**TokenStandard3**](.md)| Filter by token standard (&#x60;fa1.2&#x60; or &#x60;fa2&#x60;).   Click on the parameter to expand more details. | [optional] 
 **token_metadata** | [**TokenMetadata3**](.md)| Filter by metadata. Note, this parameter supports the following format: &#x60;token.metadata{.path?}{.mode?}&#x3D;...&#x60;, so you can specify a path to a particular field to filter by, for example: &#x60;?token.metadata.symbol.in&#x3D;kUSD,uUSD&#x60;.   Click on the parameter to expand more details. | [optional] 
 **token_has_filters** | **bool**|  | [optional] 
 **anyof** | **str**| Filter by any of the specified fields (&#x60;from&#x60; or &#x60;to&#x60;). Example: &#x60;anyof.from.to&#x3D;tz1...&#x60; will return transfers where &#x60;from&#x60; OR &#x60;to&#x60; is equal to the specified value. This parameter is useful when you need to get both incoming and outgoing transfers of the account at once.   Click on the parameter to expand more details. | [optional] 
 **_from** | [**From1**](.md)| Filter by sender account address.   Click on the parameter to expand more details. | [optional] 
 **to** | [**To1**](.md)| Filter by target account address.   Click on the parameter to expand more details. | [optional] 
 **amount** | [**Amount2**](.md)| Filter by amount.   Click on the parameter to expand more details. | [optional] 
 **transaction_id** | [**TransactionId1**](.md)| Filter by id of the transaction, caused the token transfer.   Click on the parameter to expand more details. | [optional] 
 **origination_id** | [**OriginationId1**](.md)| Filter by id of the origination, caused the token transfer.   Click on the parameter to expand more details. | [optional] 
 **migration_id** | [**MigrationId1**](.md)| Filter by id of the migration, caused the token transfer.   Click on the parameter to expand more details. | [optional] 
 **sort** | [**Sort52**](.md)| Sorts items (asc or desc) by the specified field. You can see what fields can be used for sorting in the response description, below.   Click on the parameter to expand more details. | [optional] 
 **offset** | [**Offset50**](.md)| Specifies which or how many items should be skipped.   Click on the parameter to expand more details. | [optional] 
 **limit** | **int**| Maximum number of items to return. | [optional] 
 **select** | [**Select46**](.md)| Specify a comma-separated list of fields to include into response or leave it undefined to get default set of fields. This parameter accepts values of the following format: &#x60;{field}{path?}{as alias?}&#x60;, so you can do deep selection (for example, &#x60;?select&#x3D;balance,token.metadata.symbol as token,...&#x60;).   Note, if you select just one field, the response will be flatten into a simple array of values.   Click on the parameter to expand the details. | [optional] 

### Return type

[**list[TokenTransfer]**](TokenTransfer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_get_token_transfers_count**
> int tokens_get_token_transfers_count(id=id, level=level, timestamp=timestamp, token_id=token_id, token_contract=token_contract, token_token_id=token_token_id, token_standard=token_standard, token_metadata=token_metadata, token_has_filters=token_has_filters, anyof=anyof, _from=_from, to=to, amount=amount, transaction_id=transaction_id, origination_id=origination_id, migration_id=migration_id)

Get token transfers count

Returns the total number of token transfers.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokensApi()
id = swagger_client.Id7() # Id7 | Filter by internal TzKT id.   Click on the parameter to expand more details. (optional)
level = swagger_client.Level45() # Level45 | Filter by level of the block where the transfer was made.   Click on the parameter to expand more details. (optional)
timestamp = swagger_client.Timestamp43() # Timestamp43 | Filter by timestamp (ISO 8601) of the block where the transfer was made.   Click on the parameter to expand more details. (optional)
token_id = swagger_client.TokenId2() # TokenId2 | Filter by internal TzKT id. Note, this is not the same as `tokenId`.   Click on the parameter to expand more details. (optional)
token_contract = swagger_client.TokenContract2() # TokenContract2 | Filter by contract address.   Click on the parameter to expand more details. (optional)
token_token_id = swagger_client.TokenTokenId2() # TokenTokenId2 | Filter by tokenId (for FA1.2 tokens tokenId is always `\"0\"`).   Click on the parameter to expand more details. (optional)
token_standard = swagger_client.TokenStandard2() # TokenStandard2 | Filter by token standard (`fa1.2` or `fa2`).   Click on the parameter to expand more details. (optional)
token_metadata = swagger_client.TokenMetadata2() # TokenMetadata2 | Filter by metadata. Note, this parameter supports the following format: `token.metadata{.path?}{.mode?}=...`, so you can specify a path to a particular field to filter by, for example: `?token.metadata.symbol.in=kUSD,uUSD`.   Click on the parameter to expand more details. (optional)
token_has_filters = true # bool |  (optional)
anyof = 'anyof_example' # str | Filter by any of the specified fields (`from` or `to`). Example: `anyof.from.to=tz1...` will return transfers where `from` OR `to` is equal to the specified value. This parameter is useful when you need to get both incoming and outgoing transfers of the account at once.   Click on the parameter to expand more details. (optional)
_from = swagger_client.ModelFrom() # ModelFrom | Filter by sender account address.   Click on the parameter to expand more details. (optional)
to = swagger_client.To() # To | Filter by target account address.   Click on the parameter to expand more details. (optional)
amount = swagger_client.Amount1() # Amount1 | Filter by amount.   Click on the parameter to expand more details. (optional)
transaction_id = swagger_client.TransactionId() # TransactionId | Filter by id of the transaction, caused the token transfer.   Click on the parameter to expand more details. (optional)
origination_id = swagger_client.OriginationId() # OriginationId | Filter by id of the origination, caused the token transfer.   Click on the parameter to expand more details. (optional)
migration_id = swagger_client.MigrationId() # MigrationId | Filter by id of the migration, caused the token transfer.   Click on the parameter to expand more details. (optional)

try:
    # Get token transfers count
    api_response = api_instance.tokens_get_token_transfers_count(id=id, level=level, timestamp=timestamp, token_id=token_id, token_contract=token_contract, token_token_id=token_token_id, token_standard=token_standard, token_metadata=token_metadata, token_has_filters=token_has_filters, anyof=anyof, _from=_from, to=to, amount=amount, transaction_id=transaction_id, origination_id=origination_id, migration_id=migration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApi->tokens_get_token_transfers_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id7**](.md)| Filter by internal TzKT id.   Click on the parameter to expand more details. | [optional] 
 **level** | [**Level45**](.md)| Filter by level of the block where the transfer was made.   Click on the parameter to expand more details. | [optional] 
 **timestamp** | [**Timestamp43**](.md)| Filter by timestamp (ISO 8601) of the block where the transfer was made.   Click on the parameter to expand more details. | [optional] 
 **token_id** | [**TokenId2**](.md)| Filter by internal TzKT id. Note, this is not the same as &#x60;tokenId&#x60;.   Click on the parameter to expand more details. | [optional] 
 **token_contract** | [**TokenContract2**](.md)| Filter by contract address.   Click on the parameter to expand more details. | [optional] 
 **token_token_id** | [**TokenTokenId2**](.md)| Filter by tokenId (for FA1.2 tokens tokenId is always &#x60;\&quot;0\&quot;&#x60;).   Click on the parameter to expand more details. | [optional] 
 **token_standard** | [**TokenStandard2**](.md)| Filter by token standard (&#x60;fa1.2&#x60; or &#x60;fa2&#x60;).   Click on the parameter to expand more details. | [optional] 
 **token_metadata** | [**TokenMetadata2**](.md)| Filter by metadata. Note, this parameter supports the following format: &#x60;token.metadata{.path?}{.mode?}&#x3D;...&#x60;, so you can specify a path to a particular field to filter by, for example: &#x60;?token.metadata.symbol.in&#x3D;kUSD,uUSD&#x60;.   Click on the parameter to expand more details. | [optional] 
 **token_has_filters** | **bool**|  | [optional] 
 **anyof** | **str**| Filter by any of the specified fields (&#x60;from&#x60; or &#x60;to&#x60;). Example: &#x60;anyof.from.to&#x3D;tz1...&#x60; will return transfers where &#x60;from&#x60; OR &#x60;to&#x60; is equal to the specified value. This parameter is useful when you need to get both incoming and outgoing transfers of the account at once.   Click on the parameter to expand more details. | [optional] 
 **_from** | [**ModelFrom**](.md)| Filter by sender account address.   Click on the parameter to expand more details. | [optional] 
 **to** | [**To**](.md)| Filter by target account address.   Click on the parameter to expand more details. | [optional] 
 **amount** | [**Amount1**](.md)| Filter by amount.   Click on the parameter to expand more details. | [optional] 
 **transaction_id** | [**TransactionId**](.md)| Filter by id of the transaction, caused the token transfer.   Click on the parameter to expand more details. | [optional] 
 **origination_id** | [**OriginationId**](.md)| Filter by id of the origination, caused the token transfer.   Click on the parameter to expand more details. | [optional] 
 **migration_id** | [**MigrationId**](.md)| Filter by id of the migration, caused the token transfer.   Click on the parameter to expand more details. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_get_tokens**
> list[Token] tokens_get_tokens(id=id, contract=contract, token_id=token_id, standard=standard, first_level=first_level, first_time=first_time, last_level=last_level, last_time=last_time, metadata=metadata, sort=sort, offset=offset, limit=limit, select=select)

Get tokens

Returns a list of tokens.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokensApi()
id = swagger_client.Id4() # Id4 | Filter by internal TzKT id. Note, this is not the same as `tokenId` nat value.   Click on the parameter to expand more details. (optional)
contract = swagger_client.Contract3() # Contract3 | Filter by contract address.   Click on the parameter to expand more details. (optional)
token_id = swagger_client.TokenId1() # TokenId1 | Filter by tokenId (for FA1.2 tokens tokenId is always `\"0\"`).   Click on the parameter to expand more details. (optional)
standard = swagger_client.Standard1() # Standard1 | Filter by token standard (`fa1.2` or `fa2`).   Click on the parameter to expand more details. (optional)
first_level = swagger_client.FirstLevel1() # FirstLevel1 | Filter by level of the block where the token was first seen.   Click on the parameter to expand more details. (optional)
first_time = swagger_client.FirstTime1() # FirstTime1 | Filter by timestamp (ISO 8601) of the block where the token was first seen.   Click on the parameter to expand more details. (optional)
last_level = swagger_client.LastLevel4() # LastLevel4 | Filter by level of the block where the token was last seen.   Click on the parameter to expand more details. (optional)
last_time = swagger_client.LastTime1() # LastTime1 | Filter by timestamp (ISO 8601) of the block where the token was last seen.   Click on the parameter to expand more details. (optional)
metadata = swagger_client.Metadata1() # Metadata1 | Filter by metadata.   Note, this parameter supports the following format: `metadata{.path?}{.mode?}=...`, so you can specify a path to a particular field to filter by (for example, `?metadata.symbol.in=kUSD,uUSD`).   Click on the parameter to expand more details. (optional)
sort = swagger_client.Sort50() # Sort50 | Sorts items (asc or desc) by the specified field. You can see what fields can be used for sorting in the response description, below.   Click on the parameter to expand more details. (optional)
offset = swagger_client.Offset48() # Offset48 | Specifies which or how many items should be skipped.   Click on the parameter to expand more details. (optional)
limit = 56 # int | Maximum number of items to return. (optional)
select = swagger_client.Select44() # Select44 | Specify a comma-separated list of fields to include into response or leave it undefined to get default set of fields. This parameter accepts values of the following format: `{field}{path?}{as alias?}`, so you can do deep selection (for example, `?select=balance,token.metadata.symbol as token,...`).   Note, if you select just one field, the response will be flatten into a simple array of values.   Click on the parameter to expand the details. (optional)

try:
    # Get tokens
    api_response = api_instance.tokens_get_tokens(id=id, contract=contract, token_id=token_id, standard=standard, first_level=first_level, first_time=first_time, last_level=last_level, last_time=last_time, metadata=metadata, sort=sort, offset=offset, limit=limit, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApi->tokens_get_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id4**](.md)| Filter by internal TzKT id. Note, this is not the same as &#x60;tokenId&#x60; nat value.   Click on the parameter to expand more details. | [optional] 
 **contract** | [**Contract3**](.md)| Filter by contract address.   Click on the parameter to expand more details. | [optional] 
 **token_id** | [**TokenId1**](.md)| Filter by tokenId (for FA1.2 tokens tokenId is always &#x60;\&quot;0\&quot;&#x60;).   Click on the parameter to expand more details. | [optional] 
 **standard** | [**Standard1**](.md)| Filter by token standard (&#x60;fa1.2&#x60; or &#x60;fa2&#x60;).   Click on the parameter to expand more details. | [optional] 
 **first_level** | [**FirstLevel1**](.md)| Filter by level of the block where the token was first seen.   Click on the parameter to expand more details. | [optional] 
 **first_time** | [**FirstTime1**](.md)| Filter by timestamp (ISO 8601) of the block where the token was first seen.   Click on the parameter to expand more details. | [optional] 
 **last_level** | [**LastLevel4**](.md)| Filter by level of the block where the token was last seen.   Click on the parameter to expand more details. | [optional] 
 **last_time** | [**LastTime1**](.md)| Filter by timestamp (ISO 8601) of the block where the token was last seen.   Click on the parameter to expand more details. | [optional] 
 **metadata** | [**Metadata1**](.md)| Filter by metadata.   Note, this parameter supports the following format: &#x60;metadata{.path?}{.mode?}&#x3D;...&#x60;, so you can specify a path to a particular field to filter by (for example, &#x60;?metadata.symbol.in&#x3D;kUSD,uUSD&#x60;).   Click on the parameter to expand more details. | [optional] 
 **sort** | [**Sort50**](.md)| Sorts items (asc or desc) by the specified field. You can see what fields can be used for sorting in the response description, below.   Click on the parameter to expand more details. | [optional] 
 **offset** | [**Offset48**](.md)| Specifies which or how many items should be skipped.   Click on the parameter to expand more details. | [optional] 
 **limit** | **int**| Maximum number of items to return. | [optional] 
 **select** | [**Select44**](.md)| Specify a comma-separated list of fields to include into response or leave it undefined to get default set of fields. This parameter accepts values of the following format: &#x60;{field}{path?}{as alias?}&#x60;, so you can do deep selection (for example, &#x60;?select&#x3D;balance,token.metadata.symbol as token,...&#x60;).   Note, if you select just one field, the response will be flatten into a simple array of values.   Click on the parameter to expand the details. | [optional] 

### Return type

[**list[Token]**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_get_tokens_count**
> int tokens_get_tokens_count(id=id, contract=contract, token_id=token_id, standard=standard, first_level=first_level, first_time=first_time, last_level=last_level, last_time=last_time, metadata=metadata)

Get tokens count

Returns a total number of tokens.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokensApi()
id = swagger_client.Id3() # Id3 | Filter by internal TzKT id. Note, this is not the same as `tokenId` nat value.   Click on the parameter to expand more details. (optional)
contract = swagger_client.Contract2() # Contract2 | Filter by contract address.   Click on the parameter to expand more details. (optional)
token_id = swagger_client.TokenId() # TokenId | Filter by tokenId (for FA1.2 tokens tokenId is always `\"0\"`).   Click on the parameter to expand more details. (optional)
standard = swagger_client.Standard() # Standard | Filter by token standard (`fa1.2` or `fa2`).   Click on the parameter to expand more details. (optional)
first_level = swagger_client.FirstLevel() # FirstLevel | Filter by level of the block where the token was first seen.   Click on the parameter to expand more details. (optional)
first_time = swagger_client.FirstTime() # FirstTime | Filter by timestamp (ISO 8601) of the block where the token was first seen.   Click on the parameter to expand more details. (optional)
last_level = swagger_client.LastLevel3() # LastLevel3 | Filter by level of the block where the token was last seen.   Click on the parameter to expand more details. (optional)
last_time = swagger_client.LastTime() # LastTime | Filter by timestamp (ISO 8601) of the block where the token was last seen.   Click on the parameter to expand more details. (optional)
metadata = swagger_client.Metadata() # Metadata | Filter by metadata.   Note, this parameter supports the following format: `metadata{.path?}{.mode?}=...`, so you can specify a path to a particular field to filter by (for example, `?metadata.symbol.in=kUSD,uUSD`).   Click on the parameter to expand more details. (optional)

try:
    # Get tokens count
    api_response = api_instance.tokens_get_tokens_count(id=id, contract=contract, token_id=token_id, standard=standard, first_level=first_level, first_time=first_time, last_level=last_level, last_time=last_time, metadata=metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApi->tokens_get_tokens_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id3**](.md)| Filter by internal TzKT id. Note, this is not the same as &#x60;tokenId&#x60; nat value.   Click on the parameter to expand more details. | [optional] 
 **contract** | [**Contract2**](.md)| Filter by contract address.   Click on the parameter to expand more details. | [optional] 
 **token_id** | [**TokenId**](.md)| Filter by tokenId (for FA1.2 tokens tokenId is always &#x60;\&quot;0\&quot;&#x60;).   Click on the parameter to expand more details. | [optional] 
 **standard** | [**Standard**](.md)| Filter by token standard (&#x60;fa1.2&#x60; or &#x60;fa2&#x60;).   Click on the parameter to expand more details. | [optional] 
 **first_level** | [**FirstLevel**](.md)| Filter by level of the block where the token was first seen.   Click on the parameter to expand more details. | [optional] 
 **first_time** | [**FirstTime**](.md)| Filter by timestamp (ISO 8601) of the block where the token was first seen.   Click on the parameter to expand more details. | [optional] 
 **last_level** | [**LastLevel3**](.md)| Filter by level of the block where the token was last seen.   Click on the parameter to expand more details. | [optional] 
 **last_time** | [**LastTime**](.md)| Filter by timestamp (ISO 8601) of the block where the token was last seen.   Click on the parameter to expand more details. | [optional] 
 **metadata** | [**Metadata**](.md)| Filter by metadata.   Note, this parameter supports the following format: &#x60;metadata{.path?}{.mode?}&#x3D;...&#x60;, so you can specify a path to a particular field to filter by (for example, &#x60;?metadata.symbol.in&#x3D;kUSD,uUSD&#x60;).   Click on the parameter to expand more details. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

