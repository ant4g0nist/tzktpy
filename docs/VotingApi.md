# swagger_client.VotingApi

All URIs are relative to *https://api.tzkt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**voting_get_current_epoch**](VotingApi.md#voting_get_current_epoch) | **GET** /v1/voting/epochs/current | Get current voting epoch
[**voting_get_current_period**](VotingApi.md#voting_get_current_period) | **GET** /v1/voting/periods/current | Get current voting period
[**voting_get_epoch**](VotingApi.md#voting_get_epoch) | **GET** /v1/voting/epochs/{index} | Get voting epoch by index
[**voting_get_epochs**](VotingApi.md#voting_get_epochs) | **GET** /v1/voting/epochs | Get voting epochs
[**voting_get_latest_voting**](VotingApi.md#voting_get_latest_voting) | **GET** /v1/voting/epochs/latest_voting | Get latest voting
[**voting_get_period**](VotingApi.md#voting_get_period) | **GET** /v1/voting/periods/{index} | Get voting period by index
[**voting_get_period_voter**](VotingApi.md#voting_get_period_voter) | **GET** /v1/voting/periods/{index}/voters/{address} | Get period voter
[**voting_get_period_voter2**](VotingApi.md#voting_get_period_voter2) | **GET** /v1/voting/periods/current/voters/{address} | Get current period voter
[**voting_get_period_voters**](VotingApi.md#voting_get_period_voters) | **GET** /v1/voting/periods/{index}/voters | Get period voters
[**voting_get_period_voters2**](VotingApi.md#voting_get_period_voters2) | **GET** /v1/voting/periods/current/voters | Get current period voters
[**voting_get_periods**](VotingApi.md#voting_get_periods) | **GET** /v1/voting/periods | Get voting periods
[**voting_get_proposal_by_hash**](VotingApi.md#voting_get_proposal_by_hash) | **GET** /v1/voting/proposals/{hash} | Get proposal by hash
[**voting_get_proposals**](VotingApi.md#voting_get_proposals) | **GET** /v1/voting/proposals | Get proposals
[**voting_get_proposals_count**](VotingApi.md#voting_get_proposals_count) | **GET** /v1/voting/proposals/count | Get proposals count

# **voting_get_current_epoch**
> VotingEpoch voting_get_current_epoch()

Get current voting epoch

Returns the current voting epoch

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VotingApi()

try:
    # Get current voting epoch
    api_response = api_instance.voting_get_current_epoch()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VotingApi->voting_get_current_epoch: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VotingEpoch**](VotingEpoch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voting_get_current_period**
> VotingPeriod voting_get_current_period()

Get current voting period

Returns current voting period.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VotingApi()

try:
    # Get current voting period
    api_response = api_instance.voting_get_current_period()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VotingApi->voting_get_current_period: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VotingPeriod**](VotingPeriod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voting_get_epoch**
> VotingEpoch voting_get_epoch(index)

Get voting epoch by index

Returns a voting epoch at the specified index.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VotingApi()
index = 56 # int | Voting epoch index starting from zero

try:
    # Get voting epoch by index
    api_response = api_instance.voting_get_epoch(index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VotingApi->voting_get_epoch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| Voting epoch index starting from zero | 

### Return type

[**VotingEpoch**](VotingEpoch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voting_get_epochs**
> list[VotingEpoch] voting_get_epochs(sort=sort, offset=offset, limit=limit)

Get voting epochs

Returns a list of voting epochs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VotingApi()
sort = swagger_client.Sort58() # Sort58 | Sorts voting epochs by specified field. Supported fields: `id` (default). (optional)
offset = swagger_client.Offset56() # Offset56 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)

try:
    # Get voting epochs
    api_response = api_instance.voting_get_epochs(sort=sort, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VotingApi->voting_get_epochs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | [**Sort58**](.md)| Sorts voting epochs by specified field. Supported fields: &#x60;id&#x60; (default). | [optional] 
 **offset** | [**Offset56**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]

### Return type

[**list[VotingEpoch]**](VotingEpoch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voting_get_latest_voting**
> VotingEpoch voting_get_latest_voting()

Get latest voting

Returns the latest epoch with at least one proposal

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VotingApi()

try:
    # Get latest voting
    api_response = api_instance.voting_get_latest_voting()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VotingApi->voting_get_latest_voting: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VotingEpoch**](VotingEpoch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voting_get_period**
> VotingPeriod voting_get_period(index)

Get voting period by index

Returns a voting period at the specified index.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VotingApi()
index = 56 # int | Voting period index starting from zero

try:
    # Get voting period by index
    api_response = api_instance.voting_get_period(index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VotingApi->voting_get_period: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| Voting period index starting from zero | 

### Return type

[**VotingPeriod**](VotingPeriod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voting_get_period_voter**
> VoterSnapshot voting_get_period_voter(index, address)

Get period voter

Returns a voter with the specified address from the voting period at the specified index.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VotingApi()
index = 56 # int | Voting period index starting from zero
address = 'address_example' # str | Voter address

try:
    # Get period voter
    api_response = api_instance.voting_get_period_voter(index, address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VotingApi->voting_get_period_voter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| Voting period index starting from zero | 
 **address** | **str**| Voter address | 

### Return type

[**VoterSnapshot**](VoterSnapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voting_get_period_voter2**
> VoterSnapshot voting_get_period_voter2(address)

Get current period voter

Returns a voter with the specified address from the current period.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VotingApi()
address = 'address_example' # str | Voter address

try:
    # Get current period voter
    api_response = api_instance.voting_get_period_voter2(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VotingApi->voting_get_period_voter2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Voter address | 

### Return type

[**VoterSnapshot**](VoterSnapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voting_get_period_voters**
> list[VoterSnapshot] voting_get_period_voters(index, status=status, sort=sort, offset=offset, limit=limit)

Get period voters

Returns voters from the voting period at the specified index.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VotingApi()
index = 56 # int | Voting period index starting from zero
status = swagger_client.Status10() # Status10 | Filters voters by status (`none`, `upvoted`, `voted_yay`, `voted_nay`, `voted_pass`) (optional)
sort = swagger_client.Sort56() # Sort56 | Sorts voters by specified field. Supported fields: `id` (default), `rolls`. (optional)
offset = swagger_client.Offset54() # Offset54 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)

try:
    # Get period voters
    api_response = api_instance.voting_get_period_voters(index, status=status, sort=sort, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VotingApi->voting_get_period_voters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| Voting period index starting from zero | 
 **status** | [**Status10**](.md)| Filters voters by status (&#x60;none&#x60;, &#x60;upvoted&#x60;, &#x60;voted_yay&#x60;, &#x60;voted_nay&#x60;, &#x60;voted_pass&#x60;) | [optional] 
 **sort** | [**Sort56**](.md)| Sorts voters by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;rolls&#x60;. | [optional] 
 **offset** | [**Offset54**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]

### Return type

[**list[VoterSnapshot]**](VoterSnapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voting_get_period_voters2**
> list[VoterSnapshot] voting_get_period_voters2(status=status, sort=sort, offset=offset, limit=limit)

Get current period voters

Returns voters from the current period.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VotingApi()
status = swagger_client.Status11() # Status11 | Filters voters by status (`none`, `upvoted`, `voted_yay`, `voted_nay`, `voted_pass`) (optional)
sort = swagger_client.Sort57() # Sort57 | Sorts voters by specified field. Supported fields: `id` (default), `rolls`. (optional)
offset = swagger_client.Offset55() # Offset55 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)

try:
    # Get current period voters
    api_response = api_instance.voting_get_period_voters2(status=status, sort=sort, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VotingApi->voting_get_period_voters2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**Status11**](.md)| Filters voters by status (&#x60;none&#x60;, &#x60;upvoted&#x60;, &#x60;voted_yay&#x60;, &#x60;voted_nay&#x60;, &#x60;voted_pass&#x60;) | [optional] 
 **sort** | [**Sort57**](.md)| Sorts voters by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;rolls&#x60;. | [optional] 
 **offset** | [**Offset55**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]

### Return type

[**list[VoterSnapshot]**](VoterSnapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voting_get_periods**
> list[VotingPeriod] voting_get_periods(select=select, sort=sort, offset=offset, limit=limit)

Get voting periods

Returns a list of voting periods.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VotingApi()
select = swagger_client.Select49() # Select49 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort55() # Sort55 | Sorts voting periods by specified field. Supported fields: `id` (default). (optional)
offset = swagger_client.Offset53() # Offset53 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)

try:
    # Get voting periods
    api_response = api_instance.voting_get_periods(select=select, sort=sort, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VotingApi->voting_get_periods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | [**Select49**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort55**](.md)| Sorts voting periods by specified field. Supported fields: &#x60;id&#x60; (default). | [optional] 
 **offset** | [**Offset53**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]

### Return type

[**list[VotingPeriod]**](VotingPeriod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voting_get_proposal_by_hash**
> Proposal voting_get_proposal_by_hash(hash)

Get proposal by hash

Returns the most recent protocol proposal with the specified hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VotingApi()
hash = 'hash_example' # str | Proposal hash

try:
    # Get proposal by hash
    api_response = api_instance.voting_get_proposal_by_hash(hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VotingApi->voting_get_proposal_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Proposal hash | 

### Return type

[**Proposal**](Proposal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voting_get_proposals**
> list[Proposal] voting_get_proposals(hash=hash, epoch=epoch, select=select, sort=sort, offset=offset, limit=limit)

Get proposals

Returns a list of protocol proposals.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VotingApi()
hash = swagger_client.Hash() # Hash | Filters proposals by hash (optional)
epoch = swagger_client.Epoch2() # Epoch2 | Filters proposals by voting epoch (optional)
select = swagger_client.Select48() # Select48 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort54() # Sort54 | Sorts proposals by specified field. Supported fields: `id` (default), `upvotes`, `rolls`. (optional)
offset = swagger_client.Offset52() # Offset52 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)

try:
    # Get proposals
    api_response = api_instance.voting_get_proposals(hash=hash, epoch=epoch, select=select, sort=sort, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VotingApi->voting_get_proposals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | [**Hash**](.md)| Filters proposals by hash | [optional] 
 **epoch** | [**Epoch2**](.md)| Filters proposals by voting epoch | [optional] 
 **select** | [**Select48**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort54**](.md)| Sorts proposals by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;upvotes&#x60;, &#x60;rolls&#x60;. | [optional] 
 **offset** | [**Offset52**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]

### Return type

[**list[Proposal]**](Proposal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voting_get_proposals_count**
> int voting_get_proposals_count()

Get proposals count

Returns the total number of protocol proposals.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VotingApi()

try:
    # Get proposals count
    api_response = api_instance.voting_get_proposals_count()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VotingApi->voting_get_proposals_count: %s\n" % e)
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

