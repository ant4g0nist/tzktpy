# swagger_client.OperationsApi

All URIs are relative to *https://api.tzkt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operations_get_activation_by_hash**](OperationsApi.md#operations_get_activation_by_hash) | **GET** /v1/operations/activations/{hash} | Get activation by hash
[**operations_get_activations**](OperationsApi.md#operations_get_activations) | **GET** /v1/operations/activations | Get activations
[**operations_get_activations_count**](OperationsApi.md#operations_get_activations_count) | **GET** /v1/operations/activations/count | Get activations count
[**operations_get_baking**](OperationsApi.md#operations_get_baking) | **GET** /v1/operations/baking | Get baking
[**operations_get_baking_by_id**](OperationsApi.md#operations_get_baking_by_id) | **GET** /v1/operations/baking/{id} | Get baking by id
[**operations_get_baking_count**](OperationsApi.md#operations_get_baking_count) | **GET** /v1/operations/baking/count | Get baking count
[**operations_get_ballot_by_hash**](OperationsApi.md#operations_get_ballot_by_hash) | **GET** /v1/operations/ballots/{hash} | Get ballot by hash
[**operations_get_ballots**](OperationsApi.md#operations_get_ballots) | **GET** /v1/operations/ballots | Get ballots
[**operations_get_ballots_count**](OperationsApi.md#operations_get_ballots_count) | **GET** /v1/operations/ballots/count | Get ballots count
[**operations_get_by_hash**](OperationsApi.md#operations_get_by_hash) | **GET** /v1/operations/{hash} | Get operations by hash
[**operations_get_by_hash_counter**](OperationsApi.md#operations_get_by_hash_counter) | **GET** /v1/operations/{hash}/{counter} | Get operations by hash and counter
[**operations_get_by_hash_counter_nonce**](OperationsApi.md#operations_get_by_hash_counter_nonce) | **GET** /v1/operations/{hash}/{counter}/{nonce} | Get operations by hash, counter and nonce
[**operations_get_delegation_by_hash**](OperationsApi.md#operations_get_delegation_by_hash) | **GET** /v1/operations/delegations/{hash} | Get delegation by hash
[**operations_get_delegations**](OperationsApi.md#operations_get_delegations) | **GET** /v1/operations/delegations | Get delegations
[**operations_get_delegations_count**](OperationsApi.md#operations_get_delegations_count) | **GET** /v1/operations/delegations/count | Get delegations count
[**operations_get_double_baking**](OperationsApi.md#operations_get_double_baking) | **GET** /v1/operations/double_baking | Get double baking
[**operations_get_double_baking_by_hash**](OperationsApi.md#operations_get_double_baking_by_hash) | **GET** /v1/operations/double_baking/{hash} | Get double baking by hash
[**operations_get_double_baking_count**](OperationsApi.md#operations_get_double_baking_count) | **GET** /v1/operations/double_baking/count | Get double baking count
[**operations_get_double_endorsing**](OperationsApi.md#operations_get_double_endorsing) | **GET** /v1/operations/double_endorsing | Get double endorsing
[**operations_get_double_endorsing_by_hash**](OperationsApi.md#operations_get_double_endorsing_by_hash) | **GET** /v1/operations/double_endorsing/{hash} | Get double endorsing by hash
[**operations_get_double_endorsing_count**](OperationsApi.md#operations_get_double_endorsing_count) | **GET** /v1/operations/double_endorsing/count | Get double endorsing count
[**operations_get_double_preendorsing**](OperationsApi.md#operations_get_double_preendorsing) | **GET** /v1/operations/double_preendorsing | Get double preendorsing
[**operations_get_double_preendorsing_by_hash**](OperationsApi.md#operations_get_double_preendorsing_by_hash) | **GET** /v1/operations/double_preendorsing/{hash} | Get double preendorsing by hash
[**operations_get_double_preendorsing_count**](OperationsApi.md#operations_get_double_preendorsing_count) | **GET** /v1/operations/double_preendorsing/count | Get double preendorsing count
[**operations_get_endorsement_by_hash**](OperationsApi.md#operations_get_endorsement_by_hash) | **GET** /v1/operations/endorsements/{hash} | Get endorsement by hash
[**operations_get_endorsements**](OperationsApi.md#operations_get_endorsements) | **GET** /v1/operations/endorsements | Get endorsements
[**operations_get_endorsements_count**](OperationsApi.md#operations_get_endorsements_count) | **GET** /v1/operations/endorsements/count | Get endorsements count
[**operations_get_endorsing_reward_by_id**](OperationsApi.md#operations_get_endorsing_reward_by_id) | **GET** /v1/operations/endorsing_rewards/{id} | Get endorsing reward by id
[**operations_get_endorsing_rewards**](OperationsApi.md#operations_get_endorsing_rewards) | **GET** /v1/operations/endorsing_rewards | Get endorsing rewards
[**operations_get_endorsing_rewards_count**](OperationsApi.md#operations_get_endorsing_rewards_count) | **GET** /v1/operations/endorsing_rewards/count | Get endorsing rewards count
[**operations_get_migration_by_id**](OperationsApi.md#operations_get_migration_by_id) | **GET** /v1/operations/migrations/{id} | Get migration by id
[**operations_get_migrations**](OperationsApi.md#operations_get_migrations) | **GET** /v1/operations/migrations | Get migrations
[**operations_get_migrations_count**](OperationsApi.md#operations_get_migrations_count) | **GET** /v1/operations/migrations/count | Get migrations count
[**operations_get_nonce_revelation_by_hash**](OperationsApi.md#operations_get_nonce_revelation_by_hash) | **GET** /v1/operations/nonce_revelations/{hash} | Get nonce revelation by hash
[**operations_get_nonce_revelations**](OperationsApi.md#operations_get_nonce_revelations) | **GET** /v1/operations/nonce_revelations | Get nonce revelations
[**operations_get_nonce_revelations_count**](OperationsApi.md#operations_get_nonce_revelations_count) | **GET** /v1/operations/nonce_revelations/count | Get nonce revelations count
[**operations_get_origination_by_hash**](OperationsApi.md#operations_get_origination_by_hash) | **GET** /v1/operations/originations/{hash} | Get origination by hash
[**operations_get_originations**](OperationsApi.md#operations_get_originations) | **GET** /v1/operations/originations | Get originations
[**operations_get_originations_count**](OperationsApi.md#operations_get_originations_count) | **GET** /v1/operations/originations/count | Get originations count
[**operations_get_preendorsement_by_hash**](OperationsApi.md#operations_get_preendorsement_by_hash) | **GET** /v1/operations/preendorsements/{hash} | Get preendorsement by hash
[**operations_get_preendorsements**](OperationsApi.md#operations_get_preendorsements) | **GET** /v1/operations/preendorsements | Get preendorsements
[**operations_get_preendorsements_count**](OperationsApi.md#operations_get_preendorsements_count) | **GET** /v1/operations/preendorsements/count | Get preendorsements count
[**operations_get_proposal_by_hash**](OperationsApi.md#operations_get_proposal_by_hash) | **GET** /v1/operations/proposals/{hash} | Get proposal by hash
[**operations_get_proposals**](OperationsApi.md#operations_get_proposals) | **GET** /v1/operations/proposals | Get proposals
[**operations_get_proposals_count**](OperationsApi.md#operations_get_proposals_count) | **GET** /v1/operations/proposals/count | Get proposals count
[**operations_get_register_constant_by_hash**](OperationsApi.md#operations_get_register_constant_by_hash) | **GET** /v1/operations/register_constants/{hash} | Get register constant by hash
[**operations_get_register_constants**](OperationsApi.md#operations_get_register_constants) | **GET** /v1/operations/register_constants | Get register constants
[**operations_get_register_constants_count**](OperationsApi.md#operations_get_register_constants_count) | **GET** /v1/operations/register_constants/count | Get register constants count
[**operations_get_reveal_by_hash**](OperationsApi.md#operations_get_reveal_by_hash) | **GET** /v1/operations/reveals/{hash} | Get reveal by hash
[**operations_get_reveals**](OperationsApi.md#operations_get_reveals) | **GET** /v1/operations/reveals | Get reveals
[**operations_get_reveals_count**](OperationsApi.md#operations_get_reveals_count) | **GET** /v1/operations/reveals/count | Get reveals count
[**operations_get_revelation_penalties**](OperationsApi.md#operations_get_revelation_penalties) | **GET** /v1/operations/revelation_penalties | Get revelation penalties
[**operations_get_revelation_penalties_count**](OperationsApi.md#operations_get_revelation_penalties_count) | **GET** /v1/operations/revelation_penalties/count | Get revelation penalties count
[**operations_get_revelation_penalty_by_id**](OperationsApi.md#operations_get_revelation_penalty_by_id) | **GET** /v1/operations/revelation_penalties/{id} | Get revelation penalty by id
[**operations_get_set_deposits_limit_by_hash**](OperationsApi.md#operations_get_set_deposits_limit_by_hash) | **GET** /v1/operations/set_deposits_limits/{hash} | Get set deposits limit by hash
[**operations_get_set_deposits_limits**](OperationsApi.md#operations_get_set_deposits_limits) | **GET** /v1/operations/set_deposits_limits | Get set deposits limits
[**operations_get_set_deposits_limits_count**](OperationsApi.md#operations_get_set_deposits_limits_count) | **GET** /v1/operations/set_deposits_limits/count | Get set deposits limits count
[**operations_get_transaction_by_hash**](OperationsApi.md#operations_get_transaction_by_hash) | **GET** /v1/operations/transactions/{hash} | Get transaction by hash
[**operations_get_transaction_by_hash_counter**](OperationsApi.md#operations_get_transaction_by_hash_counter) | **GET** /v1/operations/transactions/{hash}/{counter} | Get transaction by hash and counter
[**operations_get_transaction_by_hash_counter_nonce**](OperationsApi.md#operations_get_transaction_by_hash_counter_nonce) | **GET** /v1/operations/transactions/{hash}/{counter}/{nonce} | Get transaction by hash, counter and nonce
[**operations_get_transactions**](OperationsApi.md#operations_get_transactions) | **GET** /v1/operations/transactions | Get transactions
[**operations_get_transactions_count**](OperationsApi.md#operations_get_transactions_count) | **GET** /v1/operations/transactions/count | Get transactions count

# **operations_get_activation_by_hash**
> list[ActivationOperation] operations_get_activation_by_hash(hash, quote=quote)

Get activation by hash

Returns an activation operation with specified hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
hash = 'hash_example' # str | Operation hash
quote = swagger_client.Quote20() # Quote20 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get activation by hash
    api_response = api_instance.operations_get_activation_by_hash(hash, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_activation_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Operation hash | 
 **quote** | [**Quote20**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[ActivationOperation]**](ActivationOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_activations**
> list[ActivationOperation] operations_get_activations(account=account, level=level, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit, quote=quote)

Get activations

Returns a list of activation operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
account = swagger_client.Account() # Account | Filters activations by account. Allowed fields for `.eqx` mode: none. (optional)
level = swagger_client.Level11() # Level11 | Filters activations by level. (optional)
timestamp = swagger_client.Timestamp11() # Timestamp11 | Filters activations by timestamp. (optional)
select = swagger_client.Select20() # Select20 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort26() # Sort26 | Sorts activations by specified field. Supported fields: `id` (default), `level`, `balance`. (optional)
offset = swagger_client.Offset24() # Offset24 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
quote = swagger_client.Quote19() # Quote19 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get activations
    api_response = api_instance.operations_get_activations(account=account, level=level, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_activations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | [**Account**](.md)| Filters activations by account. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **level** | [**Level11**](.md)| Filters activations by level. | [optional] 
 **timestamp** | [**Timestamp11**](.md)| Filters activations by timestamp. | [optional] 
 **select** | [**Select20**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort26**](.md)| Sorts activations by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;level&#x60;, &#x60;balance&#x60;. | [optional] 
 **offset** | [**Offset24**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **quote** | [**Quote19**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[ActivationOperation]**](ActivationOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_activations_count**
> int operations_get_activations_count(level=level, timestamp=timestamp)

Get activations count

Returns the total number of activation operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
level = swagger_client.Level12() # Level12 | Filters activations by level. (optional)
timestamp = swagger_client.Timestamp12() # Timestamp12 | Filters activations by timestamp. (optional)

try:
    # Get activations count
    api_response = api_instance.operations_get_activations_count(level=level, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_activations_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | [**Level12**](.md)| Filters activations by level. | [optional] 
 **timestamp** | [**Timestamp12**](.md)| Filters activations by timestamp. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_baking**
> list[BakingOperation] operations_get_baking(baker=baker, anyof=anyof, proposer=proposer, producer=producer, level=level, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit, quote=quote)

Get baking

Returns a list of baking operations (synthetic type).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
baker = swagger_client.Baker4() # Baker4 | [DEPRECATED] (optional)
anyof = 'anyof_example' # str | Filters by any of the specified fields. Example: `anyof.proposer.producer=tz1...`. (optional)
proposer = swagger_client.Proposer1() # Proposer1 | Filters by block proposer. Allowed fields for `.eqx` mode: none. (optional)
producer = swagger_client.Producer1() # Producer1 | Filters by block producer. Allowed fields for `.eqx` mode: none. (optional)
level = swagger_client.Level37() # Level37 | Filters baking operations by level. (optional)
timestamp = swagger_client.Timestamp37() # Timestamp37 | Filters baking operations by timestamp. (optional)
select = swagger_client.Select33() # Select33 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort39() # Sort39 | Sorts baking operations by specified field. Supported fields: `id` (default), `level`. (optional)
offset = swagger_client.Offset37() # Offset37 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
quote = swagger_client.Quote47() # Quote47 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get baking
    api_response = api_instance.operations_get_baking(baker=baker, anyof=anyof, proposer=proposer, producer=producer, level=level, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_baking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **baker** | [**Baker4**](.md)| [DEPRECATED] | [optional] 
 **anyof** | **str**| Filters by any of the specified fields. Example: &#x60;anyof.proposer.producer&#x3D;tz1...&#x60;. | [optional] 
 **proposer** | [**Proposer1**](.md)| Filters by block proposer. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **producer** | [**Producer1**](.md)| Filters by block producer. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **level** | [**Level37**](.md)| Filters baking operations by level. | [optional] 
 **timestamp** | [**Timestamp37**](.md)| Filters baking operations by timestamp. | [optional] 
 **select** | [**Select33**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort39**](.md)| Sorts baking operations by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;level&#x60;. | [optional] 
 **offset** | [**Offset37**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **quote** | [**Quote47**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[BakingOperation]**](BakingOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_baking_by_id**
> BakingOperation operations_get_baking_by_id(id, quote=quote)

Get baking by id

Returns baking operation with specified id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
id = 56 # int | Operation id
quote = swagger_client.Quote48() # Quote48 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get baking by id
    api_response = api_instance.operations_get_baking_by_id(id, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_baking_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Operation id | 
 **quote** | [**Quote48**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**BakingOperation**](BakingOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_baking_count**
> int operations_get_baking_count(level=level, timestamp=timestamp)

Get baking count

Returns the total number of baking operations (synthetic type).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
level = swagger_client.Level38() # Level38 | Filters baking operations by level. (optional)
timestamp = swagger_client.Timestamp38() # Timestamp38 | Filters baking operations by timestamp. (optional)

try:
    # Get baking count
    api_response = api_instance.operations_get_baking_count(level=level, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_baking_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | [**Level38**](.md)| Filters baking operations by level. | [optional] 
 **timestamp** | [**Timestamp38**](.md)| Filters baking operations by timestamp. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_ballot_by_hash**
> list[BallotOperation] operations_get_ballot_by_hash(hash, quote=quote)

Get ballot by hash

Returns a ballot operation with specified hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
hash = 'hash_example' # str | Operation hash
quote = swagger_client.Quote16() # Quote16 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get ballot by hash
    api_response = api_instance.operations_get_ballot_by_hash(hash, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_ballot_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Operation hash | 
 **quote** | [**Quote16**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[BallotOperation]**](BallotOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_ballots**
> list[BallotOperation] operations_get_ballots(delegate=delegate, level=level, timestamp=timestamp, epoch=epoch, period=period, proposal=proposal, vote=vote, select=select, sort=sort, offset=offset, limit=limit, quote=quote)

Get ballots

Returns a list of ballot operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
delegate = swagger_client.Delegate4() # Delegate4 | Filters ballots by delegate. Allowed fields for `.eqx` mode: none. (optional)
level = swagger_client.Level7() # Level7 | Filters ballots by level. (optional)
timestamp = swagger_client.Timestamp7() # Timestamp7 | Filters ballots by timestamp. (optional)
epoch = swagger_client.Epoch() # Epoch | Filters ballots by voting epoch. (optional)
period = swagger_client.Period() # Period | Filters ballots by voting period. (optional)
proposal = swagger_client.Proposal() # Proposal | Filters ballots by proposal hash. (optional)
vote = swagger_client.Vote() # Vote | Filters ballots by vote (`yay`, `nay`, `pass`). (optional)
select = swagger_client.Select18() # Select18 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort24() # Sort24 | Sorts ballots by specified field. Supported fields: `id` (default), `level`. (optional)
offset = swagger_client.Offset22() # Offset22 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
quote = swagger_client.Quote15() # Quote15 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get ballots
    api_response = api_instance.operations_get_ballots(delegate=delegate, level=level, timestamp=timestamp, epoch=epoch, period=period, proposal=proposal, vote=vote, select=select, sort=sort, offset=offset, limit=limit, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_ballots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegate** | [**Delegate4**](.md)| Filters ballots by delegate. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **level** | [**Level7**](.md)| Filters ballots by level. | [optional] 
 **timestamp** | [**Timestamp7**](.md)| Filters ballots by timestamp. | [optional] 
 **epoch** | [**Epoch**](.md)| Filters ballots by voting epoch. | [optional] 
 **period** | [**Period**](.md)| Filters ballots by voting period. | [optional] 
 **proposal** | [**Proposal**](.md)| Filters ballots by proposal hash. | [optional] 
 **vote** | [**Vote**](.md)| Filters ballots by vote (&#x60;yay&#x60;, &#x60;nay&#x60;, &#x60;pass&#x60;). | [optional] 
 **select** | [**Select18**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort24**](.md)| Sorts ballots by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;level&#x60;. | [optional] 
 **offset** | [**Offset22**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **quote** | [**Quote15**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[BallotOperation]**](BallotOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_ballots_count**
> int operations_get_ballots_count(level=level, timestamp=timestamp)

Get ballots count

Returns the total number of ballot operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
level = swagger_client.Level8() # Level8 | Filters ballot operations by level. (optional)
timestamp = swagger_client.Timestamp8() # Timestamp8 | Filters ballot operations by timestamp. (optional)

try:
    # Get ballots count
    api_response = api_instance.operations_get_ballots_count(level=level, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_ballots_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | [**Level8**](.md)| Filters ballot operations by level. | [optional] 
 **timestamp** | [**Timestamp8**](.md)| Filters ballot operations by timestamp. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_by_hash**
> list[Operation] operations_get_by_hash(hash, micheline=micheline, quote=quote)

Get operations by hash

Returns a list of operations with the specified hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
hash = 'hash_example' # str | Operation hash
micheline = swagger_client.Micheline19() # Micheline19 | Format of the parameters, storage and diffs: `0` - JSON, `1` - JSON string, `2` - raw micheline, `3` - raw micheline string (optional)
quote = swagger_client.Quote8() # Quote8 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get operations by hash
    api_response = api_instance.operations_get_by_hash(hash, micheline=micheline, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Operation hash | 
 **micheline** | [**Micheline19**](.md)| Format of the parameters, storage and diffs: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - raw micheline, &#x60;3&#x60; - raw micheline string | [optional] 
 **quote** | [**Quote8**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[Operation]**](Operation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_by_hash_counter**
> list[Operation] operations_get_by_hash_counter(hash, counter, micheline=micheline, quote=quote)

Get operations by hash and counter

Returns a list of operations with the specified hash and counter.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
hash = 'hash_example' # str | Operation hash
counter = 56 # int | Operation counter
micheline = swagger_client.Micheline20() # Micheline20 | Format of the parameters, storage and diffs: `0` - JSON, `1` - JSON string, `2` - raw micheline, `3` - raw micheline string (optional)
quote = swagger_client.Quote9() # Quote9 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get operations by hash and counter
    api_response = api_instance.operations_get_by_hash_counter(hash, counter, micheline=micheline, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_by_hash_counter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Operation hash | 
 **counter** | **int**| Operation counter | 
 **micheline** | [**Micheline20**](.md)| Format of the parameters, storage and diffs: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - raw micheline, &#x60;3&#x60; - raw micheline string | [optional] 
 **quote** | [**Quote9**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[Operation]**](Operation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_by_hash_counter_nonce**
> list[Operation] operations_get_by_hash_counter_nonce(hash, counter, nonce, micheline=micheline, quote=quote)

Get operations by hash, counter and nonce

Returns an internal operations with the specified hash, counter and nonce.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
hash = 'hash_example' # str | Operation hash
counter = 56 # int | Operation counter
nonce = 56 # int | Operation nonce (internal)
micheline = swagger_client.Micheline21() # Micheline21 | Format of the parameters, storage and diffs: `0` - JSON, `1` - JSON string, `2` - raw micheline, `3` - raw micheline string (optional)
quote = swagger_client.Quote10() # Quote10 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get operations by hash, counter and nonce
    api_response = api_instance.operations_get_by_hash_counter_nonce(hash, counter, nonce, micheline=micheline, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_by_hash_counter_nonce: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Operation hash | 
 **counter** | **int**| Operation counter | 
 **nonce** | **int**| Operation nonce (internal) | 
 **micheline** | [**Micheline21**](.md)| Format of the parameters, storage and diffs: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - raw micheline, &#x60;3&#x60; - raw micheline string | [optional] 
 **quote** | [**Quote10**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[Operation]**](Operation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_delegation_by_hash**
> list[DelegationOperation] operations_get_delegation_by_hash(hash, quote=quote)

Get delegation by hash

Returns a delegation operation with specified hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
hash = 'hash_example' # str | Operation hash
quote = swagger_client.Quote30() # Quote30 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get delegation by hash
    api_response = api_instance.operations_get_delegation_by_hash(hash, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_delegation_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Operation hash | 
 **quote** | [**Quote30**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[DelegationOperation]**](DelegationOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_delegations**
> list[DelegationOperation] operations_get_delegations(anyof=anyof, initiator=initiator, sender=sender, prev_delegate=prev_delegate, new_delegate=new_delegate, level=level, timestamp=timestamp, status=status, select=select, sort=sort, offset=offset, limit=limit, quote=quote)

Get delegations

Returns a list of delegation operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
anyof = 'anyof_example' # str | Filters delegations by any of the specified fields. Example: `anyof.prevDelegate.newDelegate=tz1...` will return operations where `prevDelegate` OR `newDelegate` is equal to the specified value. This parameter is useful when you need to retrieve all delegations associated with a specified account. (optional)
initiator = swagger_client.Initiator1() # Initiator1 | Filters delegations by initiator. Allowed fields for `.eqx` mode: `prevDelegate`, `newDelegate`. (optional)
sender = swagger_client.Sender2() # Sender2 | Filters delegations by sender. Allowed fields for `.eqx` mode: `prevDelegate`, `newDelegate`. (optional)
prev_delegate = swagger_client.PrevDelegate1() # PrevDelegate1 | Filters delegations by prev delegate. Allowed fields for `.eqx` mode: `initiator`, `sender`, `newDelegate`. (optional)
new_delegate = swagger_client.NewDelegate1() # NewDelegate1 | Filters delegations by new delegate. Allowed fields for `.eqx` mode: `initiator`, `sender`, `prevDelegate`. (optional)
level = swagger_client.Level21() # Level21 | Filters delegations by level. (optional)
timestamp = swagger_client.Timestamp21() # Timestamp21 | Filters delegations by timestamp. (optional)
status = swagger_client.Status1() # Status1 | Filters delegations by operation status (`applied`, `failed`, `backtracked`, `skipped`). (optional)
select = swagger_client.Select25() # Select25 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort31() # Sort31 | Sorts delegations by specified field. Supported fields: `id` (default), `level`, `gasUsed`, `bakerFee`. (optional)
offset = swagger_client.Offset29() # Offset29 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
quote = swagger_client.Quote29() # Quote29 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get delegations
    api_response = api_instance.operations_get_delegations(anyof=anyof, initiator=initiator, sender=sender, prev_delegate=prev_delegate, new_delegate=new_delegate, level=level, timestamp=timestamp, status=status, select=select, sort=sort, offset=offset, limit=limit, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_delegations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anyof** | **str**| Filters delegations by any of the specified fields. Example: &#x60;anyof.prevDelegate.newDelegate&#x3D;tz1...&#x60; will return operations where &#x60;prevDelegate&#x60; OR &#x60;newDelegate&#x60; is equal to the specified value. This parameter is useful when you need to retrieve all delegations associated with a specified account. | [optional] 
 **initiator** | [**Initiator1**](.md)| Filters delegations by initiator. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;prevDelegate&#x60;, &#x60;newDelegate&#x60;. | [optional] 
 **sender** | [**Sender2**](.md)| Filters delegations by sender. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;prevDelegate&#x60;, &#x60;newDelegate&#x60;. | [optional] 
 **prev_delegate** | [**PrevDelegate1**](.md)| Filters delegations by prev delegate. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;initiator&#x60;, &#x60;sender&#x60;, &#x60;newDelegate&#x60;. | [optional] 
 **new_delegate** | [**NewDelegate1**](.md)| Filters delegations by new delegate. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;initiator&#x60;, &#x60;sender&#x60;, &#x60;prevDelegate&#x60;. | [optional] 
 **level** | [**Level21**](.md)| Filters delegations by level. | [optional] 
 **timestamp** | [**Timestamp21**](.md)| Filters delegations by timestamp. | [optional] 
 **status** | [**Status1**](.md)| Filters delegations by operation status (&#x60;applied&#x60;, &#x60;failed&#x60;, &#x60;backtracked&#x60;, &#x60;skipped&#x60;). | [optional] 
 **select** | [**Select25**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort31**](.md)| Sorts delegations by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;level&#x60;, &#x60;gasUsed&#x60;, &#x60;bakerFee&#x60;. | [optional] 
 **offset** | [**Offset29**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **quote** | [**Quote29**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[DelegationOperation]**](DelegationOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_delegations_count**
> int operations_get_delegations_count(level=level, timestamp=timestamp)

Get delegations count

Returns the total number of delegation operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
level = swagger_client.Level22() # Level22 | Filters delegations by level. (optional)
timestamp = swagger_client.Timestamp22() # Timestamp22 | Filters delegations by timestamp. (optional)

try:
    # Get delegations count
    api_response = api_instance.operations_get_delegations_count(level=level, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_delegations_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | [**Level22**](.md)| Filters delegations by level. | [optional] 
 **timestamp** | [**Timestamp22**](.md)| Filters delegations by timestamp. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_double_baking**
> list[DoubleBakingOperation] operations_get_double_baking(anyof=anyof, accuser=accuser, offender=offender, level=level, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit, quote=quote)

Get double baking

Returns a list of double baking operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
anyof = 'anyof_example' # str | Filters double baking operations by any of the specified fields. Example: `anyof.accuser.offender=tz1...` will return operations where `accuser` OR `offender` is equal to the specified value. This parameter is useful when you need to retrieve all operations associated with a specified account. (optional)
accuser = swagger_client.Accuser1() # Accuser1 | Filters double baking operations by accuser. Allowed fields for `.eqx` mode: `offender`. (optional)
offender = swagger_client.Offender1() # Offender1 | Filters double baking operations by offender. Allowed fields for `.eqx` mode: `accuser`. (optional)
level = swagger_client.Level13() # Level13 | Filters double baking operations by level. (optional)
timestamp = swagger_client.Timestamp13() # Timestamp13 | Filters double baking operations by timestamp. (optional)
select = swagger_client.Select21() # Select21 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort27() # Sort27 | Sorts double baking operations by specified field. Supported fields: `id` (default), `level`, `accusedLevel`, `accuserRewards`, `offenderLostDeposits`, `offenderLostRewards`, `offenderLostFees`. (optional)
offset = swagger_client.Offset25() # Offset25 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
quote = swagger_client.Quote21() # Quote21 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get double baking
    api_response = api_instance.operations_get_double_baking(anyof=anyof, accuser=accuser, offender=offender, level=level, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_double_baking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anyof** | **str**| Filters double baking operations by any of the specified fields. Example: &#x60;anyof.accuser.offender&#x3D;tz1...&#x60; will return operations where &#x60;accuser&#x60; OR &#x60;offender&#x60; is equal to the specified value. This parameter is useful when you need to retrieve all operations associated with a specified account. | [optional] 
 **accuser** | [**Accuser1**](.md)| Filters double baking operations by accuser. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;offender&#x60;. | [optional] 
 **offender** | [**Offender1**](.md)| Filters double baking operations by offender. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;accuser&#x60;. | [optional] 
 **level** | [**Level13**](.md)| Filters double baking operations by level. | [optional] 
 **timestamp** | [**Timestamp13**](.md)| Filters double baking operations by timestamp. | [optional] 
 **select** | [**Select21**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort27**](.md)| Sorts double baking operations by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;level&#x60;, &#x60;accusedLevel&#x60;, &#x60;accuserRewards&#x60;, &#x60;offenderLostDeposits&#x60;, &#x60;offenderLostRewards&#x60;, &#x60;offenderLostFees&#x60;. | [optional] 
 **offset** | [**Offset25**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **quote** | [**Quote21**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[DoubleBakingOperation]**](DoubleBakingOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_double_baking_by_hash**
> list[DoubleBakingOperation] operations_get_double_baking_by_hash(hash, quote=quote)

Get double baking by hash

Returns a double baking operation with specified hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
hash = 'hash_example' # str | Operation hash
quote = swagger_client.Quote22() # Quote22 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get double baking by hash
    api_response = api_instance.operations_get_double_baking_by_hash(hash, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_double_baking_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Operation hash | 
 **quote** | [**Quote22**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[DoubleBakingOperation]**](DoubleBakingOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_double_baking_count**
> int operations_get_double_baking_count(level=level, timestamp=timestamp)

Get double baking count

Returns the total number of double baking operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
level = swagger_client.Level14() # Level14 | Filters double baking operations by level. (optional)
timestamp = swagger_client.Timestamp14() # Timestamp14 | Filters double baking operations by timestamp. (optional)

try:
    # Get double baking count
    api_response = api_instance.operations_get_double_baking_count(level=level, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_double_baking_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | [**Level14**](.md)| Filters double baking operations by level. | [optional] 
 **timestamp** | [**Timestamp14**](.md)| Filters double baking operations by timestamp. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_double_endorsing**
> list[DoubleEndorsingOperation] operations_get_double_endorsing(anyof=anyof, accuser=accuser, offender=offender, level=level, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit, quote=quote)

Get double endorsing

Returns a list of double endorsing operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
anyof = 'anyof_example' # str | Filters double endorsing operations by any of the specified fields. Example: `anyof.accuser.offender=tz1...` will return operations where `accuser` OR `offender` is equal to the specified value. This parameter is useful when you need to retrieve all operations associated with a specified account. (optional)
accuser = swagger_client.Accuser2() # Accuser2 | Filters double endorsing operations by accuser. Allowed fields for `.eqx` mode: `offender`. (optional)
offender = swagger_client.Offender2() # Offender2 | Filters double endorsing operations by offender. Allowed fields for `.eqx` mode: `accuser`. (optional)
level = swagger_client.Level15() # Level15 | Filters double endorsing operations by level. (optional)
timestamp = swagger_client.Timestamp15() # Timestamp15 | Filters double endorsing operations by timestamp. (optional)
select = swagger_client.Select22() # Select22 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort28() # Sort28 | Sorts double endorsing operations by specified field. Supported fields: `id` (default), `level`, `accusedLevel`, `accuserRewards`, `offenderLostDeposits`, `offenderLostRewards`, `offenderLostFees`. (optional)
offset = swagger_client.Offset26() # Offset26 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
quote = swagger_client.Quote23() # Quote23 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get double endorsing
    api_response = api_instance.operations_get_double_endorsing(anyof=anyof, accuser=accuser, offender=offender, level=level, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_double_endorsing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anyof** | **str**| Filters double endorsing operations by any of the specified fields. Example: &#x60;anyof.accuser.offender&#x3D;tz1...&#x60; will return operations where &#x60;accuser&#x60; OR &#x60;offender&#x60; is equal to the specified value. This parameter is useful when you need to retrieve all operations associated with a specified account. | [optional] 
 **accuser** | [**Accuser2**](.md)| Filters double endorsing operations by accuser. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;offender&#x60;. | [optional] 
 **offender** | [**Offender2**](.md)| Filters double endorsing operations by offender. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;accuser&#x60;. | [optional] 
 **level** | [**Level15**](.md)| Filters double endorsing operations by level. | [optional] 
 **timestamp** | [**Timestamp15**](.md)| Filters double endorsing operations by timestamp. | [optional] 
 **select** | [**Select22**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort28**](.md)| Sorts double endorsing operations by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;level&#x60;, &#x60;accusedLevel&#x60;, &#x60;accuserRewards&#x60;, &#x60;offenderLostDeposits&#x60;, &#x60;offenderLostRewards&#x60;, &#x60;offenderLostFees&#x60;. | [optional] 
 **offset** | [**Offset26**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **quote** | [**Quote23**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[DoubleEndorsingOperation]**](DoubleEndorsingOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_double_endorsing_by_hash**
> list[DoubleEndorsingOperation] operations_get_double_endorsing_by_hash(hash, quote=quote)

Get double endorsing by hash

Returns a double endorsing operation with specified hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
hash = 'hash_example' # str | Operation hash
quote = swagger_client.Quote24() # Quote24 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get double endorsing by hash
    api_response = api_instance.operations_get_double_endorsing_by_hash(hash, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_double_endorsing_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Operation hash | 
 **quote** | [**Quote24**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[DoubleEndorsingOperation]**](DoubleEndorsingOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_double_endorsing_count**
> int operations_get_double_endorsing_count(level=level, timestamp=timestamp)

Get double endorsing count

Returns the total number of double endorsing operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
level = swagger_client.Level16() # Level16 | Filters double endorsing operations by level. (optional)
timestamp = swagger_client.Timestamp16() # Timestamp16 | Filters double endorsing operations by timestamp. (optional)

try:
    # Get double endorsing count
    api_response = api_instance.operations_get_double_endorsing_count(level=level, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_double_endorsing_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | [**Level16**](.md)| Filters double endorsing operations by level. | [optional] 
 **timestamp** | [**Timestamp16**](.md)| Filters double endorsing operations by timestamp. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_double_preendorsing**
> list[DoublePreendorsingOperation] operations_get_double_preendorsing(anyof=anyof, accuser=accuser, offender=offender, level=level, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit, quote=quote)

Get double preendorsing

Returns a list of double preendorsing operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
anyof = 'anyof_example' # str | Filters by any of the specified fields. Example: `anyof.accuser.offender=tz1...` will return operations where `accuser` OR `offender` is equal to the specified value. This parameter is useful when you need to retrieve all operations associated with a specified account. (optional)
accuser = swagger_client.Accuser3() # Accuser3 | Filters by accuser. Allowed fields for `.eqx` mode: `offender`. (optional)
offender = swagger_client.Offender3() # Offender3 | Filters by offender. Allowed fields for `.eqx` mode: `accuser`. (optional)
level = swagger_client.Level17() # Level17 | Filters by level. (optional)
timestamp = swagger_client.Timestamp17() # Timestamp17 | Filters by timestamp. (optional)
select = swagger_client.Select23() # Select23 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort29() # Sort29 | Sorts by specified field. Supported fields: `id` (default), `level`, `accusedLevel`, `accuserRewards`, `offenderLostDeposits`, `offenderLostRewards`, `offenderLostFees`. (optional)
offset = swagger_client.Offset27() # Offset27 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
quote = swagger_client.Quote25() # Quote25 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get double preendorsing
    api_response = api_instance.operations_get_double_preendorsing(anyof=anyof, accuser=accuser, offender=offender, level=level, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_double_preendorsing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anyof** | **str**| Filters by any of the specified fields. Example: &#x60;anyof.accuser.offender&#x3D;tz1...&#x60; will return operations where &#x60;accuser&#x60; OR &#x60;offender&#x60; is equal to the specified value. This parameter is useful when you need to retrieve all operations associated with a specified account. | [optional] 
 **accuser** | [**Accuser3**](.md)| Filters by accuser. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;offender&#x60;. | [optional] 
 **offender** | [**Offender3**](.md)| Filters by offender. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;accuser&#x60;. | [optional] 
 **level** | [**Level17**](.md)| Filters by level. | [optional] 
 **timestamp** | [**Timestamp17**](.md)| Filters by timestamp. | [optional] 
 **select** | [**Select23**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort29**](.md)| Sorts by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;level&#x60;, &#x60;accusedLevel&#x60;, &#x60;accuserRewards&#x60;, &#x60;offenderLostDeposits&#x60;, &#x60;offenderLostRewards&#x60;, &#x60;offenderLostFees&#x60;. | [optional] 
 **offset** | [**Offset27**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **quote** | [**Quote25**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[DoublePreendorsingOperation]**](DoublePreendorsingOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_double_preendorsing_by_hash**
> list[DoublePreendorsingOperation] operations_get_double_preendorsing_by_hash(hash, quote=quote)

Get double preendorsing by hash

Returns a double preendorsing operation with specified hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
hash = 'hash_example' # str | Operation hash
quote = swagger_client.Quote26() # Quote26 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get double preendorsing by hash
    api_response = api_instance.operations_get_double_preendorsing_by_hash(hash, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_double_preendorsing_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Operation hash | 
 **quote** | [**Quote26**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[DoublePreendorsingOperation]**](DoublePreendorsingOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_double_preendorsing_count**
> int operations_get_double_preendorsing_count(level=level, timestamp=timestamp)

Get double preendorsing count

Returns the total number of double preendorsing operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
level = swagger_client.Level18() # Level18 | Filters by level. (optional)
timestamp = swagger_client.Timestamp18() # Timestamp18 | Filters by timestamp. (optional)

try:
    # Get double preendorsing count
    api_response = api_instance.operations_get_double_preendorsing_count(level=level, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_double_preendorsing_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | [**Level18**](.md)| Filters by level. | [optional] 
 **timestamp** | [**Timestamp18**](.md)| Filters by timestamp. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_endorsement_by_hash**
> list[EndorsementOperation] operations_get_endorsement_by_hash(hash, quote=quote)

Get endorsement by hash

Returns an endorsement operation with specified hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
hash = 'hash_example' # str | Operation hash
quote = swagger_client.Quote12() # Quote12 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get endorsement by hash
    api_response = api_instance.operations_get_endorsement_by_hash(hash, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_endorsement_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Operation hash | 
 **quote** | [**Quote12**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[EndorsementOperation]**](EndorsementOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_endorsements**
> list[EndorsementOperation] operations_get_endorsements(delegate=delegate, level=level, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit, quote=quote)

Get endorsements

Returns a list of endorsement operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
delegate = swagger_client.Delegate2() # Delegate2 | Filters endorsements by delegate. Allowed fields for `.eqx` mode: none. (optional)
level = swagger_client.Level3() # Level3 | Filters endorsements by level. (optional)
timestamp = swagger_client.Timestamp3() # Timestamp3 | Filters endorsements by timestamp. (optional)
select = swagger_client.Select16() # Select16 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort22() # Sort22 | Sorts endorsements by specified field. Supported fields: `id` (default), `level`. (optional)
offset = swagger_client.Offset20() # Offset20 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
quote = swagger_client.Quote11() # Quote11 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get endorsements
    api_response = api_instance.operations_get_endorsements(delegate=delegate, level=level, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_endorsements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegate** | [**Delegate2**](.md)| Filters endorsements by delegate. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **level** | [**Level3**](.md)| Filters endorsements by level. | [optional] 
 **timestamp** | [**Timestamp3**](.md)| Filters endorsements by timestamp. | [optional] 
 **select** | [**Select16**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort22**](.md)| Sorts endorsements by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;level&#x60;. | [optional] 
 **offset** | [**Offset20**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **quote** | [**Quote11**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[EndorsementOperation]**](EndorsementOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_endorsements_count**
> int operations_get_endorsements_count(level=level, timestamp=timestamp)

Get endorsements count

Returns the total number of endorsement operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
level = swagger_client.Level4() # Level4 | Filters endorsements by level. (optional)
timestamp = swagger_client.Timestamp4() # Timestamp4 | Filters endorsements by timestamp. (optional)

try:
    # Get endorsements count
    api_response = api_instance.operations_get_endorsements_count(level=level, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_endorsements_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | [**Level4**](.md)| Filters endorsements by level. | [optional] 
 **timestamp** | [**Timestamp4**](.md)| Filters endorsements by timestamp. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_endorsing_reward_by_id**
> EndorsingRewardOperation operations_get_endorsing_reward_by_id(id, quote=quote)

Get endorsing reward by id

Returns endorsing reward operation with specified id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
id = 56 # int | Operation id
quote = swagger_client.Quote50() # Quote50 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get endorsing reward by id
    api_response = api_instance.operations_get_endorsing_reward_by_id(id, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_endorsing_reward_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Operation id | 
 **quote** | [**Quote50**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**EndorsingRewardOperation**](EndorsingRewardOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_endorsing_rewards**
> list[EndorsingRewardOperation] operations_get_endorsing_rewards(baker=baker, level=level, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit, quote=quote)

Get endorsing rewards

Returns a list of endorsing reward operations (synthetic type).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
baker = swagger_client.Baker5() # Baker5 | Filters by baker. Allowed fields for `.eqx` mode: none. (optional)
level = swagger_client.Level39() # Level39 | Filters by level. (optional)
timestamp = swagger_client.Timestamp39() # Timestamp39 | Filters by timestamp. (optional)
select = swagger_client.Select34() # Select34 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort40() # Sort40 | Sorts by specified field. Supported fields: `id` (default), `level`. (optional)
offset = swagger_client.Offset38() # Offset38 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
quote = swagger_client.Quote49() # Quote49 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get endorsing rewards
    api_response = api_instance.operations_get_endorsing_rewards(baker=baker, level=level, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_endorsing_rewards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **baker** | [**Baker5**](.md)| Filters by baker. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **level** | [**Level39**](.md)| Filters by level. | [optional] 
 **timestamp** | [**Timestamp39**](.md)| Filters by timestamp. | [optional] 
 **select** | [**Select34**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort40**](.md)| Sorts by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;level&#x60;. | [optional] 
 **offset** | [**Offset38**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **quote** | [**Quote49**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[EndorsingRewardOperation]**](EndorsingRewardOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_endorsing_rewards_count**
> int operations_get_endorsing_rewards_count(level=level, timestamp=timestamp)

Get endorsing rewards count

Returns the total number of endorsing reward operations (synthetic type).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
level = swagger_client.Level40() # Level40 | Filters by level. (optional)
timestamp = swagger_client.Timestamp40() # Timestamp40 | Filters by timestamp. (optional)

try:
    # Get endorsing rewards count
    api_response = api_instance.operations_get_endorsing_rewards_count(level=level, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_endorsing_rewards_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | [**Level40**](.md)| Filters by level. | [optional] 
 **timestamp** | [**Timestamp40**](.md)| Filters by timestamp. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_migration_by_id**
> MigrationOperation operations_get_migration_by_id(id, micheline=micheline, quote=quote)

Get migration by id

Returns migration operation with specified id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
id = 56 # int | Operation id
micheline = swagger_client.Micheline30() # Micheline30 | Format of the parameters, storage and diffs: `0` - JSON, `1` - JSON string, `2` - raw micheline, `3` - raw micheline string (optional)
quote = swagger_client.Quote44() # Quote44 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get migration by id
    api_response = api_instance.operations_get_migration_by_id(id, micheline=micheline, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_migration_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Operation id | 
 **micheline** | [**Micheline30**](.md)| Format of the parameters, storage and diffs: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - raw micheline, &#x60;3&#x60; - raw micheline string | [optional] 
 **quote** | [**Quote44**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**MigrationOperation**](MigrationOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_migrations**
> list[MigrationOperation] operations_get_migrations(account=account, kind=kind, balance_change=balance_change, id=id, level=level, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit, micheline=micheline, quote=quote)

Get migrations

Returns a list of migration operations (synthetic type).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
account = swagger_client.Account1() # Account1 | Filters migration operations by account. Allowed fields for `.eqx` mode: none. (optional)
kind = swagger_client.Kind4() # Kind4 | Filters migration operations by kind (`bootstrap`, `activate_delegate`, `airdrop`, `proposal_invoice`, `origination`, `subsidy`). (optional)
balance_change = swagger_client.BalanceChange() # BalanceChange | Filters migration operations by amount. (optional)
id = swagger_client.Id2() # Id2 | Filters migration operations by internal TzKT id. (optional)
level = swagger_client.Level33() # Level33 | Filters migration operations by level. (optional)
timestamp = swagger_client.Timestamp33() # Timestamp33 | Filters migration operations by timestamp. (optional)
select = swagger_client.Select31() # Select31 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort37() # Sort37 | Sorts migrations by specified field. Supported fields: `id` (default), `level`. (optional)
offset = swagger_client.Offset35() # Offset35 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
micheline = swagger_client.Micheline29() # Micheline29 | Format of the parameters, storage and diffs: `0` - JSON, `1` - JSON string, `2` - raw micheline, `3` - raw micheline string (optional)
quote = swagger_client.Quote43() # Quote43 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get migrations
    api_response = api_instance.operations_get_migrations(account=account, kind=kind, balance_change=balance_change, id=id, level=level, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit, micheline=micheline, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_migrations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | [**Account1**](.md)| Filters migration operations by account. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **kind** | [**Kind4**](.md)| Filters migration operations by kind (&#x60;bootstrap&#x60;, &#x60;activate_delegate&#x60;, &#x60;airdrop&#x60;, &#x60;proposal_invoice&#x60;, &#x60;origination&#x60;, &#x60;subsidy&#x60;). | [optional] 
 **balance_change** | [**BalanceChange**](.md)| Filters migration operations by amount. | [optional] 
 **id** | [**Id2**](.md)| Filters migration operations by internal TzKT id. | [optional] 
 **level** | [**Level33**](.md)| Filters migration operations by level. | [optional] 
 **timestamp** | [**Timestamp33**](.md)| Filters migration operations by timestamp. | [optional] 
 **select** | [**Select31**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort37**](.md)| Sorts migrations by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;level&#x60;. | [optional] 
 **offset** | [**Offset35**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **micheline** | [**Micheline29**](.md)| Format of the parameters, storage and diffs: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - raw micheline, &#x60;3&#x60; - raw micheline string | [optional] 
 **quote** | [**Quote43**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[MigrationOperation]**](MigrationOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_migrations_count**
> int operations_get_migrations_count(level=level, timestamp=timestamp)

Get migrations count

Returns the total number of migration operations (synthetic type).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
level = swagger_client.Level34() # Level34 | Filters migrations by level. (optional)
timestamp = swagger_client.Timestamp34() # Timestamp34 | Filters migrations by timestamp. (optional)

try:
    # Get migrations count
    api_response = api_instance.operations_get_migrations_count(level=level, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_migrations_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | [**Level34**](.md)| Filters migrations by level. | [optional] 
 **timestamp** | [**Timestamp34**](.md)| Filters migrations by timestamp. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_nonce_revelation_by_hash**
> list[NonceRevelationOperation] operations_get_nonce_revelation_by_hash(hash, quote=quote)

Get nonce revelation by hash

Returns a seed nonce revelation operation with specified hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
hash = 'hash_example' # str | Operation hash
quote = swagger_client.Quote28() # Quote28 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get nonce revelation by hash
    api_response = api_instance.operations_get_nonce_revelation_by_hash(hash, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_nonce_revelation_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Operation hash | 
 **quote** | [**Quote28**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[NonceRevelationOperation]**](NonceRevelationOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_nonce_revelations**
> list[NonceRevelationOperation] operations_get_nonce_revelations(anyof=anyof, baker=baker, sender=sender, level=level, revealed_cycle=revealed_cycle, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit, quote=quote)

Get nonce revelations

Returns a list of seed nonce revelation operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
anyof = 'anyof_example' # str | Filters nonce revelation operations by any of the specified fields. Example: `anyof.baker.sender=tz1...` will return operations where `baker` OR `sender` is equal to the specified value. This parameter is useful when you need to retrieve all operations associated with a specified account. (optional)
baker = swagger_client.Baker2() # Baker2 | Filters nonce revelation operations by baker. Allowed fields for `.eqx` mode: `sender`. (optional)
sender = swagger_client.Sender1() # Sender1 | Filters nonce revelation operations by sender. Allowed fields for `.eqx` mode: `baker`. (optional)
level = swagger_client.Level19() # Level19 | Filters nonce revelation operations by level. (optional)
revealed_cycle = swagger_client.RevealedCycle() # RevealedCycle | Filters by cycle for which the nonce was revealed. (optional)
timestamp = swagger_client.Timestamp19() # Timestamp19 | Filters nonce revelation operations by timestamp. (optional)
select = swagger_client.Select24() # Select24 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort30() # Sort30 | Sorts nonce revelation operations by specified field. Supported fields: `id` (default), `level`, `revealedLevel`. (optional)
offset = swagger_client.Offset28() # Offset28 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
quote = swagger_client.Quote27() # Quote27 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get nonce revelations
    api_response = api_instance.operations_get_nonce_revelations(anyof=anyof, baker=baker, sender=sender, level=level, revealed_cycle=revealed_cycle, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_nonce_revelations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anyof** | **str**| Filters nonce revelation operations by any of the specified fields. Example: &#x60;anyof.baker.sender&#x3D;tz1...&#x60; will return operations where &#x60;baker&#x60; OR &#x60;sender&#x60; is equal to the specified value. This parameter is useful when you need to retrieve all operations associated with a specified account. | [optional] 
 **baker** | [**Baker2**](.md)| Filters nonce revelation operations by baker. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;sender&#x60;. | [optional] 
 **sender** | [**Sender1**](.md)| Filters nonce revelation operations by sender. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;baker&#x60;. | [optional] 
 **level** | [**Level19**](.md)| Filters nonce revelation operations by level. | [optional] 
 **revealed_cycle** | [**RevealedCycle**](.md)| Filters by cycle for which the nonce was revealed. | [optional] 
 **timestamp** | [**Timestamp19**](.md)| Filters nonce revelation operations by timestamp. | [optional] 
 **select** | [**Select24**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort30**](.md)| Sorts nonce revelation operations by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;level&#x60;, &#x60;revealedLevel&#x60;. | [optional] 
 **offset** | [**Offset28**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **quote** | [**Quote27**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[NonceRevelationOperation]**](NonceRevelationOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_nonce_revelations_count**
> int operations_get_nonce_revelations_count(level=level, timestamp=timestamp)

Get nonce revelations count

Returns the total number of seed nonce revelation operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
level = swagger_client.Level20() # Level20 | Filters seed nonce revelation operations by level. (optional)
timestamp = swagger_client.Timestamp20() # Timestamp20 | Filters seed nonce revelation operations by timestamp. (optional)

try:
    # Get nonce revelations count
    api_response = api_instance.operations_get_nonce_revelations_count(level=level, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_nonce_revelations_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | [**Level20**](.md)| Filters seed nonce revelation operations by level. | [optional] 
 **timestamp** | [**Timestamp20**](.md)| Filters seed nonce revelation operations by timestamp. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_origination_by_hash**
> list[OriginationOperation] operations_get_origination_by_hash(hash, micheline=micheline, quote=quote)

Get origination by hash

Returns origination operations with specified hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
hash = 'hash_example' # str | Operation hash
micheline = swagger_client.MichelineFormat() # MichelineFormat | Format of the parameters, storage and diffs: `0` - JSON, `1` - JSON string, `2` - raw micheline, `3` - raw micheline string (optional)
quote = swagger_client.Quote32() # Quote32 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get origination by hash
    api_response = api_instance.operations_get_origination_by_hash(hash, micheline=micheline, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_origination_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Operation hash | 
 **micheline** | [**MichelineFormat**](.md)| Format of the parameters, storage and diffs: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - raw micheline, &#x60;3&#x60; - raw micheline string | [optional] 
 **quote** | [**Quote32**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[OriginationOperation]**](OriginationOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_originations**
> list[OriginationOperation] operations_get_originations(anyof=anyof, initiator=initiator, sender=sender, contract_manager=contract_manager, contract_delegate=contract_delegate, originated_contract=originated_contract, id=id, type_hash=type_hash, code_hash=code_hash, level=level, timestamp=timestamp, status=status, select=select, sort=sort, offset=offset, limit=limit, micheline=micheline, quote=quote)

Get originations

Returns a list of origination operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
anyof = 'anyof_example' # str | Filters originations by any of the specified fields. Example: `anyof.sender.initiator=tz1...` will return operations where `sender` OR `initiator` is equal to the specified value. This parameter is useful when you need to retrieve all originations associated with a specified account. (optional)
initiator = swagger_client.Initiator2() # Initiator2 | Filters origination operations by initiator. Allowed fields for `.eqx` mode: `contractManager`, `contractDelegate`. (optional)
sender = swagger_client.Sender3() # Sender3 | Filters origination operations by sender. Allowed fields for `.eqx` mode: `contractManager`, `contractDelegate`. (optional)
contract_manager = swagger_client.ContractManager1() # ContractManager1 | Filters origination operations by manager. Allowed fields for `.eqx` mode: `initiator`, `sender`, `contractDelegate`. (optional)
contract_delegate = swagger_client.ContractDelegate1() # ContractDelegate1 | Filters origination operations by delegate. Allowed fields for `.eqx` mode: `initiator`, `sender`, `contractManager`. (optional)
originated_contract = swagger_client.OriginatedContract1() # OriginatedContract1 | Filters origination operations by originated contract. Allowed fields for `.eqx` mode: none. (optional)
id = swagger_client.Id() # Id | Filters origination operations by internal TzKT id (optional)
type_hash = swagger_client.TypeHash1() # TypeHash1 | Filters origination operations by 32-bit hash of originated contract parameter and storage types (helpful for searching originations of similar contracts) (optional)
code_hash = swagger_client.CodeHash1() # CodeHash1 | Filters origination operations by 32-bit hash of originated contract code (helpful for searching originations of same contracts) (optional)
level = swagger_client.Level23() # Level23 | Filters origination operations by level. (optional)
timestamp = swagger_client.Timestamp23() # Timestamp23 | Filters origination operations by timestamp. (optional)
status = swagger_client.Status2() # Status2 | Filters origination operations by operation status (`applied`, `failed`, `backtracked`, `skipped`). (optional)
select = swagger_client.Select26() # Select26 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort32() # Sort32 | Sorts originations by specified field. Supported fields: `id` (default), `level`, `gasUsed`, `storageUsed`, `bakerFee`, `storageFee`, `allocationFee`, `contractBalance`. (optional)
offset = swagger_client.Offset30() # Offset30 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
micheline = swagger_client.Micheline22() # Micheline22 | Format of the parameters, storage and diffs: `0` - JSON, `1` - JSON string, `2` - raw micheline, `3` - raw micheline string (optional)
quote = swagger_client.Quote31() # Quote31 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get originations
    api_response = api_instance.operations_get_originations(anyof=anyof, initiator=initiator, sender=sender, contract_manager=contract_manager, contract_delegate=contract_delegate, originated_contract=originated_contract, id=id, type_hash=type_hash, code_hash=code_hash, level=level, timestamp=timestamp, status=status, select=select, sort=sort, offset=offset, limit=limit, micheline=micheline, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_originations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anyof** | **str**| Filters originations by any of the specified fields. Example: &#x60;anyof.sender.initiator&#x3D;tz1...&#x60; will return operations where &#x60;sender&#x60; OR &#x60;initiator&#x60; is equal to the specified value. This parameter is useful when you need to retrieve all originations associated with a specified account. | [optional] 
 **initiator** | [**Initiator2**](.md)| Filters origination operations by initiator. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;contractManager&#x60;, &#x60;contractDelegate&#x60;. | [optional] 
 **sender** | [**Sender3**](.md)| Filters origination operations by sender. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;contractManager&#x60;, &#x60;contractDelegate&#x60;. | [optional] 
 **contract_manager** | [**ContractManager1**](.md)| Filters origination operations by manager. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;initiator&#x60;, &#x60;sender&#x60;, &#x60;contractDelegate&#x60;. | [optional] 
 **contract_delegate** | [**ContractDelegate1**](.md)| Filters origination operations by delegate. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;initiator&#x60;, &#x60;sender&#x60;, &#x60;contractManager&#x60;. | [optional] 
 **originated_contract** | [**OriginatedContract1**](.md)| Filters origination operations by originated contract. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **id** | [**Id**](.md)| Filters origination operations by internal TzKT id | [optional] 
 **type_hash** | [**TypeHash1**](.md)| Filters origination operations by 32-bit hash of originated contract parameter and storage types (helpful for searching originations of similar contracts) | [optional] 
 **code_hash** | [**CodeHash1**](.md)| Filters origination operations by 32-bit hash of originated contract code (helpful for searching originations of same contracts) | [optional] 
 **level** | [**Level23**](.md)| Filters origination operations by level. | [optional] 
 **timestamp** | [**Timestamp23**](.md)| Filters origination operations by timestamp. | [optional] 
 **status** | [**Status2**](.md)| Filters origination operations by operation status (&#x60;applied&#x60;, &#x60;failed&#x60;, &#x60;backtracked&#x60;, &#x60;skipped&#x60;). | [optional] 
 **select** | [**Select26**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort32**](.md)| Sorts originations by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;level&#x60;, &#x60;gasUsed&#x60;, &#x60;storageUsed&#x60;, &#x60;bakerFee&#x60;, &#x60;storageFee&#x60;, &#x60;allocationFee&#x60;, &#x60;contractBalance&#x60;. | [optional] 
 **offset** | [**Offset30**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **micheline** | [**Micheline22**](.md)| Format of the parameters, storage and diffs: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - raw micheline, &#x60;3&#x60; - raw micheline string | [optional] 
 **quote** | [**Quote31**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[OriginationOperation]**](OriginationOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_originations_count**
> int operations_get_originations_count(level=level, timestamp=timestamp)

Get originations count

Returns the total number of origination operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
level = swagger_client.Level24() # Level24 | Filters originations by level. (optional)
timestamp = swagger_client.Timestamp24() # Timestamp24 | Filters originations by timestamp. (optional)

try:
    # Get originations count
    api_response = api_instance.operations_get_originations_count(level=level, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_originations_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | [**Level24**](.md)| Filters originations by level. | [optional] 
 **timestamp** | [**Timestamp24**](.md)| Filters originations by timestamp. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_preendorsement_by_hash**
> list[PreendorsementOperation] operations_get_preendorsement_by_hash(hash, quote=quote)

Get preendorsement by hash

Returns an preendorsement operation with specified hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
hash = 'hash_example' # str | Operation hash
quote = swagger_client.Quote14() # Quote14 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get preendorsement by hash
    api_response = api_instance.operations_get_preendorsement_by_hash(hash, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_preendorsement_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Operation hash | 
 **quote** | [**Quote14**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[PreendorsementOperation]**](PreendorsementOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_preendorsements**
> list[PreendorsementOperation] operations_get_preendorsements(delegate=delegate, level=level, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit, quote=quote)

Get preendorsements

Returns a list of preendorsement operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
delegate = swagger_client.Delegate3() # Delegate3 | Filters by delegate. Allowed fields for `.eqx` mode: none. (optional)
level = swagger_client.Level5() # Level5 | Filters by level. (optional)
timestamp = swagger_client.Timestamp5() # Timestamp5 | Filters by timestamp. (optional)
select = swagger_client.Select17() # Select17 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort23() # Sort23 | Sorts by specified field. Supported fields: `id` (default), `level`. (optional)
offset = swagger_client.Offset21() # Offset21 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
quote = swagger_client.Quote13() # Quote13 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get preendorsements
    api_response = api_instance.operations_get_preendorsements(delegate=delegate, level=level, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_preendorsements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegate** | [**Delegate3**](.md)| Filters by delegate. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **level** | [**Level5**](.md)| Filters by level. | [optional] 
 **timestamp** | [**Timestamp5**](.md)| Filters by timestamp. | [optional] 
 **select** | [**Select17**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort23**](.md)| Sorts by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;level&#x60;. | [optional] 
 **offset** | [**Offset21**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **quote** | [**Quote13**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[PreendorsementOperation]**](PreendorsementOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_preendorsements_count**
> int operations_get_preendorsements_count(level=level, timestamp=timestamp)

Get preendorsements count

Returns the total number of preendorsement operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
level = swagger_client.Level6() # Level6 | Filters by level. (optional)
timestamp = swagger_client.Timestamp6() # Timestamp6 | Filters by timestamp. (optional)

try:
    # Get preendorsements count
    api_response = api_instance.operations_get_preendorsements_count(level=level, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_preendorsements_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | [**Level6**](.md)| Filters by level. | [optional] 
 **timestamp** | [**Timestamp6**](.md)| Filters by timestamp. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_proposal_by_hash**
> list[ProposalOperation] operations_get_proposal_by_hash(hash, quote=quote)

Get proposal by hash

Returns a proposal operation with specified hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
hash = 'hash_example' # str | Operation hash
quote = swagger_client.Quote18() # Quote18 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get proposal by hash
    api_response = api_instance.operations_get_proposal_by_hash(hash, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_proposal_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Operation hash | 
 **quote** | [**Quote18**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[ProposalOperation]**](ProposalOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_proposals**
> list[ProposalOperation] operations_get_proposals(delegate=delegate, level=level, timestamp=timestamp, epoch=epoch, period=period, proposal=proposal, duplicated=duplicated, select=select, sort=sort, offset=offset, limit=limit, quote=quote)

Get proposals

Returns a list of proposal operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
delegate = swagger_client.Delegate5() # Delegate5 | Filters proposal operations by delegate. Allowed fields for `.eqx` mode: none. (optional)
level = swagger_client.Level9() # Level9 | Filters proposal operations by level. (optional)
timestamp = swagger_client.Timestamp9() # Timestamp9 | Filters proposal operations by timestamp. (optional)
epoch = swagger_client.Epoch1() # Epoch1 | Filters proposal operations by voting epoch. (optional)
period = swagger_client.Period1() # Period1 | Filters proposal operations by voting period. (optional)
proposal = swagger_client.Proposal1() # Proposal1 | Filters proposal operations by proposal hash. (optional)
duplicated = swagger_client.Duplicated() # Duplicated | Specify whether to include or exclude duplicates, which didn't actually upvote a proposal. (optional)
select = swagger_client.Select19() # Select19 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort25() # Sort25 | Sorts proposal operations by specified field. Supported fields: `id` (default), `level`. (optional)
offset = swagger_client.Offset23() # Offset23 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
quote = swagger_client.Quote17() # Quote17 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get proposals
    api_response = api_instance.operations_get_proposals(delegate=delegate, level=level, timestamp=timestamp, epoch=epoch, period=period, proposal=proposal, duplicated=duplicated, select=select, sort=sort, offset=offset, limit=limit, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_proposals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegate** | [**Delegate5**](.md)| Filters proposal operations by delegate. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **level** | [**Level9**](.md)| Filters proposal operations by level. | [optional] 
 **timestamp** | [**Timestamp9**](.md)| Filters proposal operations by timestamp. | [optional] 
 **epoch** | [**Epoch1**](.md)| Filters proposal operations by voting epoch. | [optional] 
 **period** | [**Period1**](.md)| Filters proposal operations by voting period. | [optional] 
 **proposal** | [**Proposal1**](.md)| Filters proposal operations by proposal hash. | [optional] 
 **duplicated** | [**Duplicated**](.md)| Specify whether to include or exclude duplicates, which didn&#x27;t actually upvote a proposal. | [optional] 
 **select** | [**Select19**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort25**](.md)| Sorts proposal operations by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;level&#x60;. | [optional] 
 **offset** | [**Offset23**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **quote** | [**Quote17**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[ProposalOperation]**](ProposalOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_proposals_count**
> int operations_get_proposals_count(level=level, timestamp=timestamp)

Get proposals count

Returns the total number of proposal operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
level = swagger_client.Level10() # Level10 | Filters proposal operations by level. (optional)
timestamp = swagger_client.Timestamp10() # Timestamp10 | Filters proposal operations by timestamp. (optional)

try:
    # Get proposals count
    api_response = api_instance.operations_get_proposals_count(level=level, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_proposals_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | [**Level10**](.md)| Filters proposal operations by level. | [optional] 
 **timestamp** | [**Timestamp10**](.md)| Filters proposal operations by timestamp. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_register_constant_by_hash**
> list[RegisterConstantOperation] operations_get_register_constant_by_hash(hash, micheline=micheline, quote=quote)

Get register constant by hash

Returns register global constant operation with specified hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
hash = 'hash_example' # str | Operation hash
micheline = swagger_client.Micheline28() # Micheline28 | Format of the constant value: `0` - JSON, `1` - JSON string, `2` - raw micheline, `3` - raw micheline string (optional)
quote = swagger_client.Quote40() # Quote40 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get register constant by hash
    api_response = api_instance.operations_get_register_constant_by_hash(hash, micheline=micheline, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_register_constant_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Operation hash | 
 **micheline** | [**Micheline28**](.md)| Format of the constant value: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - raw micheline, &#x60;3&#x60; - raw micheline string | [optional] 
 **quote** | [**Quote40**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[RegisterConstantOperation]**](RegisterConstantOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_register_constants**
> list[RegisterConstantOperation] operations_get_register_constants(sender=sender, address=address, level=level, timestamp=timestamp, status=status, select=select, sort=sort, offset=offset, limit=limit, micheline=micheline, quote=quote)

Get register constants

Returns a list of register global constant operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
sender = swagger_client.Sender7() # Sender7 | Filters operations by sender. Allowed fields for `.eqx` mode: none. (optional)
address = swagger_client.Address1() # Address1 | Filters operations by global address of the created constant (starts with `expr..`). (optional)
level = swagger_client.Level29() # Level29 | Filters operations by level. (optional)
timestamp = swagger_client.Timestamp29() # Timestamp29 | Filters operations by timestamp. (optional)
status = swagger_client.Status6() # Status6 | Filters operations by status (`applied`, `failed`, `backtracked`, `skipped`). (optional)
select = swagger_client.Select29() # Select29 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort35() # Sort35 | Sorts operations by specified field. Supported fields: `id` (default), `level`, `gasUsed`, `storageUsed`, `bakerFee`, `storageFee`. (optional)
offset = swagger_client.Offset33() # Offset33 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
micheline = swagger_client.Micheline27() # Micheline27 | Format of the constant value: `0` - JSON, `1` - JSON string, `2` - raw micheline, `3` - raw micheline string (optional)
quote = swagger_client.Quote39() # Quote39 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get register constants
    api_response = api_instance.operations_get_register_constants(sender=sender, address=address, level=level, timestamp=timestamp, status=status, select=select, sort=sort, offset=offset, limit=limit, micheline=micheline, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_register_constants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sender** | [**Sender7**](.md)| Filters operations by sender. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **address** | [**Address1**](.md)| Filters operations by global address of the created constant (starts with &#x60;expr..&#x60;). | [optional] 
 **level** | [**Level29**](.md)| Filters operations by level. | [optional] 
 **timestamp** | [**Timestamp29**](.md)| Filters operations by timestamp. | [optional] 
 **status** | [**Status6**](.md)| Filters operations by status (&#x60;applied&#x60;, &#x60;failed&#x60;, &#x60;backtracked&#x60;, &#x60;skipped&#x60;). | [optional] 
 **select** | [**Select29**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort35**](.md)| Sorts operations by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;level&#x60;, &#x60;gasUsed&#x60;, &#x60;storageUsed&#x60;, &#x60;bakerFee&#x60;, &#x60;storageFee&#x60;. | [optional] 
 **offset** | [**Offset33**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **micheline** | [**Micheline27**](.md)| Format of the constant value: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - raw micheline, &#x60;3&#x60; - raw micheline string | [optional] 
 **quote** | [**Quote39**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[RegisterConstantOperation]**](RegisterConstantOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_register_constants_count**
> int operations_get_register_constants_count(level=level, timestamp=timestamp)

Get register constants count

Returns the total number of register global constant operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
level = swagger_client.Level30() # Level30 | Filters operations by level. (optional)
timestamp = swagger_client.Timestamp30() # Timestamp30 | Filters operations by timestamp. (optional)

try:
    # Get register constants count
    api_response = api_instance.operations_get_register_constants_count(level=level, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_register_constants_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | [**Level30**](.md)| Filters operations by level. | [optional] 
 **timestamp** | [**Timestamp30**](.md)| Filters operations by timestamp. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_reveal_by_hash**
> list[RevealOperation] operations_get_reveal_by_hash(hash, quote=quote)

Get reveal by hash

Returns reveal operation with specified hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
hash = 'hash_example' # str | Operation hash
quote = swagger_client.Quote38() # Quote38 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get reveal by hash
    api_response = api_instance.operations_get_reveal_by_hash(hash, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_reveal_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Operation hash | 
 **quote** | [**Quote38**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[RevealOperation]**](RevealOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_reveals**
> list[RevealOperation] operations_get_reveals(sender=sender, level=level, timestamp=timestamp, status=status, select=select, sort=sort, offset=offset, limit=limit, quote=quote)

Get reveals

Returns a list of reveal operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
sender = swagger_client.Sender6() # Sender6 | Filters reveal operations by sender. Allowed fields for `.eqx` mode: none. (optional)
level = swagger_client.Level27() # Level27 | Filters reveal operations by level. (optional)
timestamp = swagger_client.Timestamp27() # Timestamp27 | Filters reveal operations by timestamp. (optional)
status = swagger_client.Status5() # Status5 | Filters reveal operations by operation status (`applied`, `failed`, `backtracked`, `skipped`). (optional)
select = swagger_client.Select28() # Select28 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort34() # Sort34 | Sorts reveals by specified field. Supported fields: `id` (default), `level`, `gasUsed`, `bakerFee`. (optional)
offset = swagger_client.Offset32() # Offset32 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
quote = swagger_client.Quote37() # Quote37 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get reveals
    api_response = api_instance.operations_get_reveals(sender=sender, level=level, timestamp=timestamp, status=status, select=select, sort=sort, offset=offset, limit=limit, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_reveals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sender** | [**Sender6**](.md)| Filters reveal operations by sender. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **level** | [**Level27**](.md)| Filters reveal operations by level. | [optional] 
 **timestamp** | [**Timestamp27**](.md)| Filters reveal operations by timestamp. | [optional] 
 **status** | [**Status5**](.md)| Filters reveal operations by operation status (&#x60;applied&#x60;, &#x60;failed&#x60;, &#x60;backtracked&#x60;, &#x60;skipped&#x60;). | [optional] 
 **select** | [**Select28**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort34**](.md)| Sorts reveals by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;level&#x60;, &#x60;gasUsed&#x60;, &#x60;bakerFee&#x60;. | [optional] 
 **offset** | [**Offset32**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **quote** | [**Quote37**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[RevealOperation]**](RevealOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_reveals_count**
> int operations_get_reveals_count(level=level, timestamp=timestamp)

Get reveals count

Returns the total number of reveal operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
level = swagger_client.Level28() # Level28 | Filters reveals by level. (optional)
timestamp = swagger_client.Timestamp28() # Timestamp28 | Filters reveals by timestamp. (optional)

try:
    # Get reveals count
    api_response = api_instance.operations_get_reveals_count(level=level, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_reveals_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | [**Level28**](.md)| Filters reveals by level. | [optional] 
 **timestamp** | [**Timestamp28**](.md)| Filters reveals by timestamp. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_revelation_penalties**
> list[RevelationPenaltyOperation] operations_get_revelation_penalties(baker=baker, level=level, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit, quote=quote)

Get revelation penalties

Returns a list of revelation penalty operations (synthetic type).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
baker = swagger_client.Baker3() # Baker3 | Filters revelation penalty operations by baker. Allowed fields for `.eqx` mode: none. (optional)
level = swagger_client.Level35() # Level35 | Filters revelation penalty operations by level. (optional)
timestamp = swagger_client.Timestamp35() # Timestamp35 | Filters revelation penalty operations by timestamp. (optional)
select = swagger_client.Select32() # Select32 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort38() # Sort38 | Sorts revelation penalty operations by specified field. Supported fields: `id` (default), `level`. (optional)
offset = swagger_client.Offset36() # Offset36 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
quote = swagger_client.Quote45() # Quote45 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get revelation penalties
    api_response = api_instance.operations_get_revelation_penalties(baker=baker, level=level, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_revelation_penalties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **baker** | [**Baker3**](.md)| Filters revelation penalty operations by baker. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **level** | [**Level35**](.md)| Filters revelation penalty operations by level. | [optional] 
 **timestamp** | [**Timestamp35**](.md)| Filters revelation penalty operations by timestamp. | [optional] 
 **select** | [**Select32**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort38**](.md)| Sorts revelation penalty operations by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;level&#x60;. | [optional] 
 **offset** | [**Offset36**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **quote** | [**Quote45**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[RevelationPenaltyOperation]**](RevelationPenaltyOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_revelation_penalties_count**
> int operations_get_revelation_penalties_count(level=level, timestamp=timestamp)

Get revelation penalties count

Returns the total number of revelation penalty operations (synthetic type).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
level = swagger_client.Level36() # Level36 | Filters revelation penalty operations by level. (optional)
timestamp = swagger_client.Timestamp36() # Timestamp36 | Filters revelation penalty operations by timestamp. (optional)

try:
    # Get revelation penalties count
    api_response = api_instance.operations_get_revelation_penalties_count(level=level, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_revelation_penalties_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | [**Level36**](.md)| Filters revelation penalty operations by level. | [optional] 
 **timestamp** | [**Timestamp36**](.md)| Filters revelation penalty operations by timestamp. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_revelation_penalty_by_id**
> RevelationPenaltyOperation operations_get_revelation_penalty_by_id(id, quote=quote)

Get revelation penalty by id

Returns revelation penalty operation with specified id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
id = 56 # int | Operation id
quote = swagger_client.Quote46() # Quote46 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get revelation penalty by id
    api_response = api_instance.operations_get_revelation_penalty_by_id(id, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_revelation_penalty_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Operation id | 
 **quote** | [**Quote46**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**RevelationPenaltyOperation**](RevelationPenaltyOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_set_deposits_limit_by_hash**
> list[SetDepositsLimitOperation] operations_get_set_deposits_limit_by_hash(hash, quote=quote)

Get set deposits limit by hash

Returns set deposits limit operation with specified hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
hash = 'hash_example' # str | Operation hash
quote = swagger_client.Quote42() # Quote42 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get set deposits limit by hash
    api_response = api_instance.operations_get_set_deposits_limit_by_hash(hash, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_set_deposits_limit_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Operation hash | 
 **quote** | [**Quote42**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[SetDepositsLimitOperation]**](SetDepositsLimitOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_set_deposits_limits**
> list[SetDepositsLimitOperation] operations_get_set_deposits_limits(sender=sender, level=level, timestamp=timestamp, status=status, select=select, sort=sort, offset=offset, limit=limit, quote=quote)

Get set deposits limits

Returns a list of set deposits limit operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
sender = swagger_client.Sender8() # Sender8 | Filters by sender. Allowed fields for `.eqx` mode: none. (optional)
level = swagger_client.Level31() # Level31 | Filters by level. (optional)
timestamp = swagger_client.Timestamp31() # Timestamp31 | Filters by timestamp. (optional)
status = swagger_client.Status7() # Status7 | Filters by status (`applied`, `failed`, `backtracked`, `skipped`). (optional)
select = swagger_client.Select30() # Select30 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort36() # Sort36 | Sorts by specified field. Supported fields: `id` (default), `level`, `gasUsed`, `bakerFee`. (optional)
offset = swagger_client.Offset34() # Offset34 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
quote = swagger_client.Quote41() # Quote41 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get set deposits limits
    api_response = api_instance.operations_get_set_deposits_limits(sender=sender, level=level, timestamp=timestamp, status=status, select=select, sort=sort, offset=offset, limit=limit, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_set_deposits_limits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sender** | [**Sender8**](.md)| Filters by sender. Allowed fields for &#x60;.eqx&#x60; mode: none. | [optional] 
 **level** | [**Level31**](.md)| Filters by level. | [optional] 
 **timestamp** | [**Timestamp31**](.md)| Filters by timestamp. | [optional] 
 **status** | [**Status7**](.md)| Filters by status (&#x60;applied&#x60;, &#x60;failed&#x60;, &#x60;backtracked&#x60;, &#x60;skipped&#x60;). | [optional] 
 **select** | [**Select30**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort36**](.md)| Sorts by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;level&#x60;, &#x60;gasUsed&#x60;, &#x60;bakerFee&#x60;. | [optional] 
 **offset** | [**Offset34**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **quote** | [**Quote41**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[SetDepositsLimitOperation]**](SetDepositsLimitOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_set_deposits_limits_count**
> int operations_get_set_deposits_limits_count(level=level, timestamp=timestamp)

Get set deposits limits count

Returns the total number of set deposits limit operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
level = swagger_client.Level32() # Level32 | Filters by level. (optional)
timestamp = swagger_client.Timestamp32() # Timestamp32 | Filters by timestamp. (optional)

try:
    # Get set deposits limits count
    api_response = api_instance.operations_get_set_deposits_limits_count(level=level, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_set_deposits_limits_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | [**Level32**](.md)| Filters by level. | [optional] 
 **timestamp** | [**Timestamp32**](.md)| Filters by timestamp. | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_transaction_by_hash**
> list[TransactionOperation] operations_get_transaction_by_hash(hash, micheline=micheline, quote=quote)

Get transaction by hash

Returns transaction operations with specified hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
hash = 'hash_example' # str | Operation hash
micheline = swagger_client.Micheline24() # Micheline24 | Format of the parameters, storage and diffs: `0` - JSON, `1` - JSON string, `2` - raw micheline, `3` - raw micheline string (optional)
quote = swagger_client.Quote34() # Quote34 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get transaction by hash
    api_response = api_instance.operations_get_transaction_by_hash(hash, micheline=micheline, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_transaction_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Operation hash | 
 **micheline** | [**Micheline24**](.md)| Format of the parameters, storage and diffs: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - raw micheline, &#x60;3&#x60; - raw micheline string | [optional] 
 **quote** | [**Quote34**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[TransactionOperation]**](TransactionOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_transaction_by_hash_counter**
> list[TransactionOperation] operations_get_transaction_by_hash_counter(hash, counter, micheline=micheline, quote=quote)

Get transaction by hash and counter

Returns transaction operations with specified hash and counter.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
hash = 'hash_example' # str | Operation hash
counter = 56 # int | Operation counter
micheline = swagger_client.Micheline25() # Micheline25 | Format of the parameters, storage and diffs: `0` - JSON, `1` - JSON string, `2` - raw micheline, `3` - raw micheline string (optional)
quote = swagger_client.Quote35() # Quote35 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get transaction by hash and counter
    api_response = api_instance.operations_get_transaction_by_hash_counter(hash, counter, micheline=micheline, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_transaction_by_hash_counter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Operation hash | 
 **counter** | **int**| Operation counter | 
 **micheline** | [**Micheline25**](.md)| Format of the parameters, storage and diffs: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - raw micheline, &#x60;3&#x60; - raw micheline string | [optional] 
 **quote** | [**Quote35**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[TransactionOperation]**](TransactionOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_transaction_by_hash_counter_nonce**
> list[TransactionOperation] operations_get_transaction_by_hash_counter_nonce(hash, counter, nonce, micheline=micheline, quote=quote)

Get transaction by hash, counter and nonce

Returns an internal transaction operation with specified hash, counter and nonce.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
hash = 'hash_example' # str | Operation hash
counter = 56 # int | Operation counter
nonce = 56 # int | Operation nonce (internal)
micheline = swagger_client.Micheline26() # Micheline26 | Format of the parameters, storage and diffs: `0` - JSON, `1` - JSON string, `2` - raw micheline, `3` - raw micheline string (optional)
quote = swagger_client.Quote36() # Quote36 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get transaction by hash, counter and nonce
    api_response = api_instance.operations_get_transaction_by_hash_counter_nonce(hash, counter, nonce, micheline=micheline, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_transaction_by_hash_counter_nonce: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Operation hash | 
 **counter** | **int**| Operation counter | 
 **nonce** | **int**| Operation nonce (internal) | 
 **micheline** | [**Micheline26**](.md)| Format of the parameters, storage and diffs: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - raw micheline, &#x60;3&#x60; - raw micheline string | [optional] 
 **quote** | [**Quote36**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[TransactionOperation]**](TransactionOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_transactions**
> list[TransactionOperation] operations_get_transactions(anyof=anyof, initiator=initiator, sender=sender, target=target, amount=amount, id=id, level=level, timestamp=timestamp, entrypoint=entrypoint, parameter=parameter, has_internals=has_internals, status=status, select=select, sort=sort, offset=offset, limit=limit, micheline=micheline, quote=quote)

Get transactions

Returns a list of transaction operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
anyof = 'anyof_example' # str | Filters transactions by any of the specified fields. Example: `anyof.sender.target=tz1...` will return operations where `sender` OR `target` is equal to the specified value. This parameter is useful when you need to retrieve all transactions associated with a specified account. (optional)
initiator = swagger_client.Initiator3() # Initiator3 | Filters transactions by initiator. Allowed fields for `.eqx` mode: `target`. (optional)
sender = swagger_client.Sender4() # Sender4 | Filters transactions by sender. Allowed fields for `.eqx` mode: `target`. (optional)
target = swagger_client.Target1() # Target1 | Filters transactions by target. Allowed fields for `.eqx` mode: `sender`, `initiator`. (optional)
amount = swagger_client.Amount() # Amount | Filters transactions by amount (microtez). (optional)
id = swagger_client.Id1() # Id1 | Filters transactions by id. (optional)
level = swagger_client.Level25() # Level25 | Filters transactions by level. (optional)
timestamp = swagger_client.Timestamp25() # Timestamp25 | Filters transactions by timestamp. (optional)
entrypoint = swagger_client.Entrypoint1() # Entrypoint1 | Filters transactions by entrypoint called on the target contract. (optional)
parameter = swagger_client.Parameter1() # Parameter1 | Filters transactions by parameter value. Note, this query parameter supports the following format: `?parameter{.path?}{.mode?}=...`,             so you can specify a path to a particular field to filter by, for example: `?parameter.token_id=...` or `?parameter.sigs.0.ne=...`. (optional)
has_internals = swagger_client.HasInternals1() # HasInternals1 | Filters transactions by presence of internal operations. (optional)
status = swagger_client.Status3() # Status3 | Filters transactions by operation status (`applied`, `failed`, `backtracked`, `skipped`). (optional)
select = swagger_client.Select27() # Select27 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort33() # Sort33 | Sorts transactions by specified field. Supported fields: `id` (default), `level`, `gasUsed`, `storageUsed`, `bakerFee`, `storageFee`, `allocationFee`, `amount`. (optional)
offset = swagger_client.Offset31() # Offset31 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
micheline = swagger_client.Micheline23() # Micheline23 | Format of the parameters, storage and diffs: `0` - JSON, `1` - JSON string, `2` - raw micheline, `3` - raw micheline string (optional)
quote = swagger_client.Quote33() # Quote33 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get transactions
    api_response = api_instance.operations_get_transactions(anyof=anyof, initiator=initiator, sender=sender, target=target, amount=amount, id=id, level=level, timestamp=timestamp, entrypoint=entrypoint, parameter=parameter, has_internals=has_internals, status=status, select=select, sort=sort, offset=offset, limit=limit, micheline=micheline, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anyof** | **str**| Filters transactions by any of the specified fields. Example: &#x60;anyof.sender.target&#x3D;tz1...&#x60; will return operations where &#x60;sender&#x60; OR &#x60;target&#x60; is equal to the specified value. This parameter is useful when you need to retrieve all transactions associated with a specified account. | [optional] 
 **initiator** | [**Initiator3**](.md)| Filters transactions by initiator. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;target&#x60;. | [optional] 
 **sender** | [**Sender4**](.md)| Filters transactions by sender. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;target&#x60;. | [optional] 
 **target** | [**Target1**](.md)| Filters transactions by target. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;sender&#x60;, &#x60;initiator&#x60;. | [optional] 
 **amount** | [**Amount**](.md)| Filters transactions by amount (microtez). | [optional] 
 **id** | [**Id1**](.md)| Filters transactions by id. | [optional] 
 **level** | [**Level25**](.md)| Filters transactions by level. | [optional] 
 **timestamp** | [**Timestamp25**](.md)| Filters transactions by timestamp. | [optional] 
 **entrypoint** | [**Entrypoint1**](.md)| Filters transactions by entrypoint called on the target contract. | [optional] 
 **parameter** | [**Parameter1**](.md)| Filters transactions by parameter value. Note, this query parameter supports the following format: &#x60;?parameter{.path?}{.mode?}&#x3D;...&#x60;,             so you can specify a path to a particular field to filter by, for example: &#x60;?parameter.token_id&#x3D;...&#x60; or &#x60;?parameter.sigs.0.ne&#x3D;...&#x60;. | [optional] 
 **has_internals** | [**HasInternals1**](.md)| Filters transactions by presence of internal operations. | [optional] 
 **status** | [**Status3**](.md)| Filters transactions by operation status (&#x60;applied&#x60;, &#x60;failed&#x60;, &#x60;backtracked&#x60;, &#x60;skipped&#x60;). | [optional] 
 **select** | [**Select27**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort33**](.md)| Sorts transactions by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;level&#x60;, &#x60;gasUsed&#x60;, &#x60;storageUsed&#x60;, &#x60;bakerFee&#x60;, &#x60;storageFee&#x60;, &#x60;allocationFee&#x60;, &#x60;amount&#x60;. | [optional] 
 **offset** | [**Offset31**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **micheline** | [**Micheline23**](.md)| Format of the parameters, storage and diffs: &#x60;0&#x60; - JSON, &#x60;1&#x60; - JSON string, &#x60;2&#x60; - raw micheline, &#x60;3&#x60; - raw micheline string | [optional] 
 **quote** | [**Quote33**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[TransactionOperation]**](TransactionOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_get_transactions_count**
> int operations_get_transactions_count(anyof=anyof, initiator=initiator, sender=sender, target=target, level=level, timestamp=timestamp, entrypoint=entrypoint, status=status)

Get transactions count

Returns the total number of transaction operations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
anyof = 'anyof_example' # str | Filters transactions by any of the specified fields. Example: `anyof.sender.target=tz1...` will return operations where `sender` OR `target` is equal to the specified value. This parameter is useful when you need to retrieve all transactions associated with a specified account. (optional)
initiator = swagger_client.Initiator4() # Initiator4 | Filters transactions by initiator. Allowed fields for `.eqx` mode: `target`. (optional)
sender = swagger_client.Sender5() # Sender5 | Filters transactions by sender. Allowed fields for `.eqx` mode: `target`. (optional)
target = swagger_client.Target2() # Target2 | Filters transactions by target. Allowed fields for `.eqx` mode: `sender`, `initiator`. (optional)
level = swagger_client.Level26() # Level26 | Filters transactions by level. (optional)
timestamp = swagger_client.Timestamp26() # Timestamp26 | Filters transactions by timestamp. (optional)
entrypoint = swagger_client.Entrypoint2() # Entrypoint2 | Filters transactions by entrypoint called on the target contract. (optional)
status = swagger_client.Status4() # Status4 | Filters transactions by operation status (`applied`, `failed`, `backtracked`, `skipped`). (optional)

try:
    # Get transactions count
    api_response = api_instance.operations_get_transactions_count(anyof=anyof, initiator=initiator, sender=sender, target=target, level=level, timestamp=timestamp, entrypoint=entrypoint, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get_transactions_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anyof** | **str**| Filters transactions by any of the specified fields. Example: &#x60;anyof.sender.target&#x3D;tz1...&#x60; will return operations where &#x60;sender&#x60; OR &#x60;target&#x60; is equal to the specified value. This parameter is useful when you need to retrieve all transactions associated with a specified account. | [optional] 
 **initiator** | [**Initiator4**](.md)| Filters transactions by initiator. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;target&#x60;. | [optional] 
 **sender** | [**Sender5**](.md)| Filters transactions by sender. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;target&#x60;. | [optional] 
 **target** | [**Target2**](.md)| Filters transactions by target. Allowed fields for &#x60;.eqx&#x60; mode: &#x60;sender&#x60;, &#x60;initiator&#x60;. | [optional] 
 **level** | [**Level26**](.md)| Filters transactions by level. | [optional] 
 **timestamp** | [**Timestamp26**](.md)| Filters transactions by timestamp. | [optional] 
 **entrypoint** | [**Entrypoint2**](.md)| Filters transactions by entrypoint called on the target contract. | [optional] 
 **status** | [**Status4**](.md)| Filters transactions by operation status (&#x60;applied&#x60;, &#x60;failed&#x60;, &#x60;backtracked&#x60;, &#x60;skipped&#x60;). | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

