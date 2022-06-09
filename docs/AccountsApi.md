# swagger_client.AccountsApi

All URIs are relative to *https://api.tzkt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_get**](AccountsApi.md#accounts_get) | **GET** /v1/accounts | Get accounts
[**accounts_get_balance**](AccountsApi.md#accounts_get_balance) | **GET** /v1/accounts/{address}/balance | Get balance
[**accounts_get_balance_at_date**](AccountsApi.md#accounts_get_balance_at_date) | **GET** /v1/accounts/{address}/balance_history/{datetime} | Get balance at date
[**accounts_get_balance_at_level**](AccountsApi.md#accounts_get_balance_at_level) | **GET** /v1/accounts/{address}/balance_history/{level} | Get balance at level
[**accounts_get_balance_history**](AccountsApi.md#accounts_get_balance_history) | **GET** /v1/accounts/{address}/balance_history | Get balance history
[**accounts_get_balance_report**](AccountsApi.md#accounts_get_balance_report) | **GET** /v1/accounts/{address}/report | Get account report
[**accounts_get_by_address**](AccountsApi.md#accounts_get_by_address) | **GET** /v1/accounts/{address} | Get account by address
[**accounts_get_contracts**](AccountsApi.md#accounts_get_contracts) | **GET** /v1/accounts/{address}/contracts | Get account contracts
[**accounts_get_count**](AccountsApi.md#accounts_get_count) | **GET** /v1/accounts/count | Get accounts count
[**accounts_get_counter**](AccountsApi.md#accounts_get_counter) | **GET** /v1/accounts/{address}/counter | Get counter
[**accounts_get_delegators**](AccountsApi.md#accounts_get_delegators) | **GET** /v1/accounts/{address}/delegators | Get account delegators
[**accounts_get_metadata**](AccountsApi.md#accounts_get_metadata) | **GET** /v1/accounts/{address}/metadata | Get account metadata
[**accounts_get_operations**](AccountsApi.md#accounts_get_operations) | **GET** /v1/accounts/{address}/operations | Get account operations

# **accounts_get**
> list[Account] accounts_get(type=type, kind=kind, delegate=delegate, balance=balance, staked=staked, last_activity=last_activity, select=select, sort=sort, offset=offset, limit=limit)

Get accounts

Returns a list of accounts.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
type = swagger_client.Type() # Type | Filters accounts by type (`user`, `delegate`, `contract`, `ghost`). (optional)
kind = swagger_client.Kind() # Kind | Filters accounts by contract kind (`delegator_contract` or `smart_contract`) (optional)
delegate = swagger_client.Delegate() # Delegate | Filters accounts by delegate. Allowed fields for `.eqx` mode: none. (optional)
balance = swagger_client.Balance() # Balance | Filters accounts by balance (optional)
staked = swagger_client.Staked() # Staked | Filters accounts by participation in staking (optional)
last_activity = swagger_client.LastActivity() # LastActivity | Filters accounts by last activity level (where the account was updated) (optional)
select = swagger_client.Select() # Select | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort() # Sort | Sorts delegators by specified field. Supported fields: `id` (default), `balance`, `firstActivity`, `lastActivity`, `numTransactions`, `numContracts`. (optional)
offset = swagger_client.Offset() # Offset | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)

try:
    # Get accounts
    api_response = api_instance.accounts_get(type=type, kind=kind, delegate=delegate, balance=balance, staked=staked, last_activity=last_activity, select=select, sort=sort, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**Type**](.md)| Filters accounts by type (&#x60;user&#x60;, &#x60;delegate&#x60;, &#x60;contract&#x60;, &#x60;ghost&#x60;). | [optional] 
 **kind** | [**Kind**](.md)| Filters accounts by contract kind (&#x60;delegator_contract&#x60; or &#x60;smart_contract&#x60;) | [optional] 
 **delegate** | [**Delegate**](.md)| Filters accounts by delegate. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **balance** | [**Balance**](.md)| Filters accounts by balance | [optional] 
 **staked** | [**Staked**](.md)| Filters accounts by participation in staking | [optional] 
 **last_activity** | [**LastActivity**](.md)| Filters accounts by last activity level (where the account was updated) | [optional] 
 **select** | [**Select**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort**](.md)| Sorts delegators by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;balance&#x60;, &#x60;firstActivity&#x60;, &#x60;lastActivity&#x60;, &#x60;numTransactions&#x60;, &#x60;numContracts&#x60;. | [optional] 
 **offset** | [**Offset**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]

### Return type

[**list[Account]**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get_balance**
> int accounts_get_balance(address)

Get balance

Returns account balance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
address = 'address_example' # str | Account address (starting with tz or KT)

try:
    # Get balance
    api_response = api_instance.accounts_get_balance(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Account address (starting with tz or KT) | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get_balance_at_date**
> int accounts_get_balance_at_date(address, _datetime)

Get balance at date

Returns account balance at the specified datetime

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
address = 'address_example' # str | Account address (starting with tz or KT)
_datetime = '2013-10-20T19:20:30+01:00' # datetime | Datetime at which you want to know account balance (e.g. `2020-01-01`, or `2019-12-30T23:42:59Z`)

try:
    # Get balance at date
    api_response = api_instance.accounts_get_balance_at_date(address, _datetime)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_balance_at_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Account address (starting with tz or KT) | 
 **_datetime** | **datetime**| Datetime at which you want to know account balance (e.g. &#x60;2020-01-01&#x60;, or &#x60;2019-12-30T23:42:59Z&#x60;) | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get_balance_at_level**
> int accounts_get_balance_at_level(address, level)

Get balance at level

Returns account balance at the specified block

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
address = 'address_example' # str | Account address (starting with tz or KT)
level = 56 # int | Block height at which you want to know account balance

try:
    # Get balance at level
    api_response = api_instance.accounts_get_balance_at_level(address, level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_balance_at_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Account address (starting with tz or KT) | 
 **level** | **int**| Block height at which you want to know account balance | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get_balance_history**
> list[HistoricalBalance] accounts_get_balance_history(address, step=step, select=select, sort=sort, offset=offset, limit=limit, quote=quote)

Get balance history

Returns time series with historical balances (only changes, without duplicates).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
address = 'address_example' # str | Account address (starting with tz or KT)
step = 56 # int | Step of the time series, for example if `step = 1000` you will get balances at blocks `1000, 2000, 3000, ...`. (optional)
select = swagger_client.Select1() # Select1 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort4() # Sort4 | Sorts historical balances by specified field. Supported fields: `level`. (optional)
offset = 0 # int | Specifies which or how many items should be skipped (optional) (default to 0)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
quote = swagger_client.Quote1() # Quote1 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get balance history
    api_response = api_instance.accounts_get_balance_history(address, step=step, select=select, sort=sort, offset=offset, limit=limit, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_balance_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Account address (starting with tz or KT) | 
 **step** | **int**| Step of the time series, for example if &#x60;step &#x3D; 1000&#x60; you will get balances at blocks &#x60;1000, 2000, 3000, ...&#x60;. | [optional] 
 **select** | [**Select1**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort4**](.md)| Sorts historical balances by specified field. Supported fields: &#x60;level&#x60;. | [optional] 
 **offset** | **int**| Specifies which or how many items should be skipped | [optional] [default to 0]
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **quote** | [**Quote1**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[HistoricalBalance]**](HistoricalBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get_balance_report**
> str accounts_get_balance_report(address, _from=_from, to=to, currency=currency, historical=historical, delimiter=delimiter, separator=separator)

Get account report

Exports account balance report in .csv format

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
address = 'address_example' # str | Account address (starting with tz or KT)
_from = '2013-10-20T19:20:30+01:00' # datetime | Start of the datetime range to filter by (ISO 8601, e.g. 2019-11-31) (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | End of the datetime range to filter by (ISO 8601, e.g. 2019-12-31) (optional)
currency = 'currency_example' # str | Currency to convert amounts to (`btc`, `eur`, `usd`, `cny`, `jpy`, `krw`, `eth`, `gbp`) (optional)
historical = false # bool | `true` if you want to use historical prices, `false` to use current price (optional) (default to false)
delimiter = 'comma' # str | Column delimiter (`comma`, `semicolon`) (optional) (default to comma)
separator = 'point' # str | Decimal separator (`comma`, `point`) (optional) (default to point)

try:
    # Get account report
    api_response = api_instance.accounts_get_balance_report(address, _from=_from, to=to, currency=currency, historical=historical, delimiter=delimiter, separator=separator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_balance_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Account address (starting with tz or KT) | 
 **_from** | **datetime**| Start of the datetime range to filter by (ISO 8601, e.g. 2019-11-31) | [optional] 
 **to** | **datetime**| End of the datetime range to filter by (ISO 8601, e.g. 2019-12-31) | [optional] 
 **currency** | **str**| Currency to convert amounts to (&#x60;btc&#x60;, &#x60;eur&#x60;, &#x60;usd&#x60;, &#x60;cny&#x60;, &#x60;jpy&#x60;, &#x60;krw&#x60;, &#x60;eth&#x60;, &#x60;gbp&#x60;) | [optional] 
 **historical** | **bool**| &#x60;true&#x60; if you want to use historical prices, &#x60;false&#x60; to use current price | [optional] [default to false]
 **delimiter** | **str**| Column delimiter (&#x60;comma&#x60;, &#x60;semicolon&#x60;) | [optional] [default to comma]
 **separator** | **str**| Decimal separator (&#x60;comma&#x60;, &#x60;point&#x60;) | [optional] [default to point]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get_by_address**
> Account accounts_get_by_address(address, metadata=metadata)

Get account by address

Returns an account with the specified address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
address = 'address_example' # str | Account address (starting with tz or KT)
metadata = false # bool | Include or not account metadata (optional) (default to false)

try:
    # Get account by address
    api_response = api_instance.accounts_get_by_address(address, metadata=metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_by_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Account address (starting with tz or KT) | 
 **metadata** | **bool**| Include or not account metadata | [optional] [default to false]

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get_contracts**
> list[RelatedContract] accounts_get_contracts(address, sort=sort, offset=offset, limit=limit)

Get account contracts

Returns a list of contracts created by (or related to) the specified account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
address = 'address_example' # str | Account address (starting with tz or KT)
sort = swagger_client.Sort1() # Sort1 | Sorts contracts by specified field. Supported fields: `id` (default, desc), `balance`, `creationLevel`. (optional)
offset = swagger_client.Offset1() # Offset1 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)

try:
    # Get account contracts
    api_response = api_instance.accounts_get_contracts(address, sort=sort, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_contracts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Account address (starting with tz or KT) | 
 **sort** | [**Sort1**](.md)| Sorts contracts by specified field. Supported fields: &#x60;id&#x60; (default, desc), &#x60;balance&#x60;, &#x60;creationLevel&#x60;. | [optional] 
 **offset** | [**Offset1**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]

### Return type

[**list[RelatedContract]**](RelatedContract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get_count**
> int accounts_get_count(type=type, kind=kind, balance=balance, staked=staked)

Get accounts count

Returns a number of accounts.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
type = swagger_client.Type1() # Type1 | Filters accounts by type (`user`, `delegate`, `contract`, `ghost`). (optional)
kind = swagger_client.Kind1() # Kind1 | Filters accounts by contract kind (`delegator_contract` or `smart_contract`) (optional)
balance = swagger_client.Balance1() # Balance1 | Filters accounts by balance (optional)
staked = swagger_client.Staked1() # Staked1 | Filters accounts by participation in staking (optional)

try:
    # Get accounts count
    api_response = api_instance.accounts_get_count(type=type, kind=kind, balance=balance, staked=staked)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**Type1**](.md)| Filters accounts by type (&#x60;user&#x60;, &#x60;delegate&#x60;, &#x60;contract&#x60;, &#x60;ghost&#x60;). | [optional] 
 **kind** | [**Kind1**](.md)| Filters accounts by contract kind (&#x60;delegator_contract&#x60; or &#x60;smart_contract&#x60;) | [optional] 
 **balance** | [**Balance1**](.md)| Filters accounts by balance | [optional] 
 **staked** | [**Staked1**](.md)| Filters accounts by participation in staking | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get_counter**
> int accounts_get_counter(address)

Get counter

Returns account counter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
address = 'address_example' # str | Account address (starting with tz or KT)

try:
    # Get counter
    api_response = api_instance.accounts_get_counter(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_counter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Account address (starting with tz or KT) | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get_delegators**
> list[Delegator] accounts_get_delegators(address, type=type, balance=balance, delegation_level=delegation_level, sort=sort, offset=offset, limit=limit)

Get account delegators

Returns a list of accounts delegated to the specified account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
address = 'address_example' # str | Account address (starting with tz)
type = swagger_client.Type2() # Type2 | Filters delegators by type (`user`, `delegate`, `contract`, `ghost`). (optional)
balance = swagger_client.Balance2() # Balance2 | Filters delegators by balance. (optional)
delegation_level = swagger_client.DelegationLevel() # DelegationLevel | Number of items to skip (optional)
sort = swagger_client.Sort2() # Sort2 | Sorts delegators by specified field. Supported fields: `delegationLevel` (default, desc), `balance`. (optional)
offset = swagger_client.Offset2() # Offset2 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)

try:
    # Get account delegators
    api_response = api_instance.accounts_get_delegators(address, type=type, balance=balance, delegation_level=delegation_level, sort=sort, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_delegators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Account address (starting with tz) | 
 **type** | [**Type2**](.md)| Filters delegators by type (&#x60;user&#x60;, &#x60;delegate&#x60;, &#x60;contract&#x60;, &#x60;ghost&#x60;). | [optional] 
 **balance** | [**Balance2**](.md)| Filters delegators by balance. | [optional] 
 **delegation_level** | [**DelegationLevel**](.md)| Number of items to skip | [optional] 
 **sort** | [**Sort2**](.md)| Sorts delegators by specified field. Supported fields: &#x60;delegationLevel&#x60; (default, desc), &#x60;balance&#x60;. | [optional] 
 **offset** | [**Offset2**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]

### Return type

[**list[Delegator]**](Delegator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get_metadata**
> ProfileMetadata accounts_get_metadata(address)

Get account metadata

Returns metadata of the specified account (alias, logo, website, contacts, etc).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
address = 'address_example' # str | Account address (starting with tz or KT)

try:
    # Get account metadata
    api_response = api_instance.accounts_get_metadata(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Account address (starting with tz or KT) | 

### Return type

[**ProfileMetadata**](ProfileMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get_operations**
> list[Operation] accounts_get_operations(address, type=type, initiator=initiator, sender=sender, target=target, prev_delegate=prev_delegate, new_delegate=new_delegate, contract_manager=contract_manager, contract_delegate=contract_delegate, originated_contract=originated_contract, accuser=accuser, offender=offender, baker=baker, level=level, timestamp=timestamp, entrypoint=entrypoint, parameter=parameter, has_internals=has_internals, status=status, sort=sort, last_id=last_id, limit=limit, micheline=micheline, quote=quote)

Get account operations

Returns a list of operations related to the specified account. Note: for better flexibility this endpoint accumulates query parameters (filters) of each `/operations/{type}` endpoint, so a particular filter may affect several operation types containing this filter. For example, if you specify an `initiator` it will affect all transactions, delegations and originations, because all these types have an `initiator` field.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
address = 'address_example' # str | Account address (starting with tz or KT)
type = 'type_example' # str | Comma separated list of operation types to return (`endorsement`, `preendorsement`, `ballot`, `proposal`, `activation`, `double_baking`, `double_endorsing`, `double_preendorsing`, `nonce_revelation`, `delegation`, `origination`, `transaction`, `reveal`, `register_constant`, `set_deposits_limit`, `migration`, `revelation_penalty`, `baking`, `endorsing_reward`). If not specified then the default set will be returned. (optional)
initiator = swagger_client.Initiator() # Initiator | Filters transactions, delegations and originations by initiator. Allowed fields for `.eqx` mode: none. (optional)
sender = swagger_client.Sender() # Sender | Filters transactions, delegations, originations, reveals and seed nonce revelations by sender. Allowed fields for `.eqx` mode: none. (optional)
target = swagger_client.Target() # Target | Filters transactions by target. Allowed fields for `.eqx` mode: none. (optional)
prev_delegate = swagger_client.PrevDelegate() # PrevDelegate | Filters delegations by prev delegate. Allowed fields for `.eqx` mode: none. (optional)
new_delegate = swagger_client.NewDelegate() # NewDelegate | Filters delegations by new delegate. Allowed fields for `.eqx` mode: none. (optional)
contract_manager = swagger_client.ContractManager() # ContractManager | Filters origination operations by manager. Allowed fields for `.eqx` mode: none. (optional)
contract_delegate = swagger_client.ContractDelegate() # ContractDelegate | Filters origination operations by delegate. Allowed fields for `.eqx` mode: none. (optional)
originated_contract = swagger_client.OriginatedContract() # OriginatedContract | Filters origination operations by originated contract. Allowed fields for `.eqx` mode: none. (optional)
accuser = swagger_client.Accuser() # Accuser | Filters double baking and double endorsing by accuser. Allowed fields for `.eqx` mode: none. (optional)
offender = swagger_client.Offender() # Offender | Filters double baking and double endorsing by offender. Allowed fields for `.eqx` mode: none. (optional)
baker = swagger_client.Baker() # Baker | Filters seed nonce revelation operations by baker. Allowed fields for `.eqx` mode: none. (optional)
level = swagger_client.Level() # Level | Filters operations by level. (optional)
timestamp = swagger_client.Timestamp() # Timestamp | Filters operations by timestamp. (optional)
entrypoint = swagger_client.Entrypoint() # Entrypoint | Filters transactions by entrypoint called on the target contract. (optional)
parameter = swagger_client.Parameter() # Parameter | Filters transactions by parameter value. Note, this query parameter supports the following format: `?parameter{.path?}{.mode?}=...`,             so you can specify a path to a particular field to filter by, for example: `?parameter.token_id=...` or `?parameter.sigs.0.ne=...`. (optional)
has_internals = swagger_client.HasInternals() # HasInternals | Filters transactions by presence of internal operations. (optional)
status = swagger_client.Status() # Status | Filters transactions, delegations, originations and reveals by operation status (`applied`, `failed`, `backtracked`, `skipped`). (optional)
sort = swagger_client.Sort3() # Sort3 | Sort mode (0 - ascending, 1 - descending), operations of different types can only be sorted by ID. (optional)
last_id = 56 # int | Id of the last operation received, which is used as an offset for pagination (optional)
limit = 100 # int | Number of items to return (optional) (default to 100)
micheline = swagger_client.Micheline() # Micheline | Format of the parameters, storage and diffs: `0` - JSON, `1` - JSON string, `2` - raw micheline, `3` - raw micheline string (optional)
quote = swagger_client.Quote() # Quote | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get account operations
    api_response = api_instance.accounts_get_operations(address, type=type, initiator=initiator, sender=sender, target=target, prev_delegate=prev_delegate, new_delegate=new_delegate, contract_manager=contract_manager, contract_delegate=contract_delegate, originated_contract=originated_contract, accuser=accuser, offender=offender, baker=baker, level=level, timestamp=timestamp, entrypoint=entrypoint, parameter=parameter, has_internals=has_internals, status=status, sort=sort, last_id=last_id, limit=limit, micheline=micheline, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_operations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Account address (starting with tz or KT) | 
 **type** | **str**| Comma separated list of operation types to return (&#x60;endorsement&#x60;, &#x60;preendorsement&#x60;, &#x60;ballot&#x60;, &#x60;proposal&#x60;, &#x60;activation&#x60;, &#x60;double_baking&#x60;, &#x60;double_endorsing&#x60;, &#x60;double_preendorsing&#x60;, &#x60;nonce_revelation&#x60;, &#x60;delegation&#x60;, &#x60;origination&#x60;, &#x60;transaction&#x60;, &#x60;reveal&#x60;, &#x60;register_constant&#x60;, &#x60;set_deposits_limit&#x60;, &#x60;migration&#x60;, &#x60;revelation_penalty&#x60;, &#x60;baking&#x60;, &#x60;endorsing_reward&#x60;). If not specified then the default set will be returned. | [optional] 
 **initiator** | [**Initiator**](.md)| Filters transactions, delegations and originations by initiator. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **sender** | [**Sender**](.md)| Filters transactions, delegations, originations, reveals and seed nonce revelations by sender. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **target** | [**Target**](.md)| Filters transactions by target. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **prev_delegate** | [**PrevDelegate**](.md)| Filters delegations by prev delegate. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **new_delegate** | [**NewDelegate**](.md)| Filters delegations by new delegate. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **contract_manager** | [**ContractManager**](.md)| Filters origination operations by manager. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **contract_delegate** | [**ContractDelegate**](.md)| Filters origination operations by delegate. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **originated_contract** | [**OriginatedContract**](.md)| Filters origination operations by originated contract. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **accuser** | [**Accuser**](.md)| Filters double baking and double endorsing by accuser. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **offender** | [**Offender**](.md)| Filters double baking and double endorsing by offender. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **baker** | [**Baker**](.md)| Filters seed nonce revelation operations by baker. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **level** | [**Level**](.md)| Filters operations by level. | [optional] 
 **timestamp** | [**Timestamp**](.md)| Filters operations by timestamp. | [optional] 
 **entrypoint** | [**Entrypoint**](.md)| Filters transactions by entrypoint called on the target contract. | [optional] 
 **parameter** | [**Parameter**](.md)| Filters transactions by parameter value. Note, this query parameter supports the following format: &#x60;?parameter{.path?}{.mode?}&#x3D;...&#x60;,             so you can specify a path to a particular field to filter by, for example: &#x60;?parameter.token_id&#x3D;...&#x60; or &#x60;?parameter.sigs.0.ne&#x3D;...&#x60;. | [optional] 
 **has_internals** | [**HasInternals**](.md)| Filters transactions by presence of internal operations. | [optional] 
 **status** | [**Status**](.md)| Filters transactions, delegations, originations and reveals by operation status (&#x60;applied&#x60;, &#x60;failed&#x60;, &#x60;backtracked&#x60;, &#x60;skipped&#x60;). | [optional] 
 **sort** | [**Sort3**](.md)| Sort mode (0 - ascending, 1 - descending), operations of different types can only be sorted by ID. | [optional] 
 **last_id** | **int**| Id of the last operation received, which is used as an offset for pagination | [optional] 
 **limit** | **int**| Number of items to return | [optional] [default to 100]
 **micheline** | [**Micheline**](.md)| Format of the parameters, storage and diffs: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - raw micheline, &#x60;3&#x60; - raw micheline string | [optional] 
 **quote** | [**Quote**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[Operation]**](Operation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

