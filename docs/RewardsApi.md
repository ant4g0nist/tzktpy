# swagger_client.RewardsApi

All URIs are relative to *https://api.tzkt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rewards_get_baker_rewards**](RewardsApi.md#rewards_get_baker_rewards) | **GET** /v1/rewards/bakers/{address} | Get baker cycle rewards
[**rewards_get_baker_rewards_by_cycle**](RewardsApi.md#rewards_get_baker_rewards_by_cycle) | **GET** /v1/rewards/bakers/{address}/{cycle} | Get baker cycle rewards by cycle
[**rewards_get_baker_rewards_count**](RewardsApi.md#rewards_get_baker_rewards_count) | **GET** /v1/rewards/bakers/{address}/count | Get baker cycle rewards count
[**rewards_get_delegator_rewards**](RewardsApi.md#rewards_get_delegator_rewards) | **GET** /v1/rewards/delegators/{address} | Get delegator cycle rewards
[**rewards_get_delegator_rewards_by_cycle**](RewardsApi.md#rewards_get_delegator_rewards_by_cycle) | **GET** /v1/rewards/delegators/{address}/{cycle} | Get delegator cycle rewards by cycle
[**rewards_get_delegator_rewards_count**](RewardsApi.md#rewards_get_delegator_rewards_count) | **GET** /v1/rewards/delegators/{address}/count | Get delegator cycle rewards count
[**rewards_get_reward_split**](RewardsApi.md#rewards_get_reward_split) | **GET** /v1/rewards/split/{baker}/{cycle} | Get reward split
[**rewards_get_reward_split_delegator**](RewardsApi.md#rewards_get_reward_split_delegator) | **GET** /v1/rewards/split/{baker}/{cycle}/{delegator} | Get reward split delegator

# **rewards_get_baker_rewards**
> list[BakerRewards] rewards_get_baker_rewards(address, cycle=cycle, select=select, sort=sort, offset=offset, limit=limit, quote=quote)

Get baker cycle rewards

Returns a list of baker rewards for every cycle, including future cycles.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RewardsApi()
address = 'address_example' # str | Baker address.
cycle = swagger_client.Cycle() # Cycle | Filters rewards by cycle. (optional)
select = swagger_client.Select36() # Select36 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort43() # Sort43 | Sorts cycle rewards by specified field. Supported fields: `cycle` (default, desc). (optional)
offset = swagger_client.Offset41() # Offset41 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
quote = swagger_client.Quote51() # Quote51 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get baker cycle rewards
    api_response = api_instance.rewards_get_baker_rewards(address, cycle=cycle, select=select, sort=sort, offset=offset, limit=limit, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RewardsApi->rewards_get_baker_rewards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Baker address. | 
 **cycle** | [**Cycle**](.md)| Filters rewards by cycle. | [optional] 
 **select** | [**Select36**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort43**](.md)| Sorts cycle rewards by specified field. Supported fields: &#x60;cycle&#x60; (default, desc). | [optional] 
 **offset** | [**Offset41**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **quote** | [**Quote51**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[BakerRewards]**](BakerRewards.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rewards_get_baker_rewards_by_cycle**
> BakerRewards rewards_get_baker_rewards_by_cycle(address, cycle, quote=quote)

Get baker cycle rewards by cycle

Returns baker cycle rewards for the specified cycle.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RewardsApi()
address = 'address_example' # str | Baker address
cycle = 56 # int | Rewards cycle
quote = swagger_client.Quote52() # Quote52 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get baker cycle rewards by cycle
    api_response = api_instance.rewards_get_baker_rewards_by_cycle(address, cycle, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RewardsApi->rewards_get_baker_rewards_by_cycle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Baker address | 
 **cycle** | **int**| Rewards cycle | 
 **quote** | [**Quote52**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**BakerRewards**](BakerRewards.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rewards_get_baker_rewards_count**
> int rewards_get_baker_rewards_count(address)

Get baker cycle rewards count

Returns total number of cycles where the baker was active

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RewardsApi()
address = 'address_example' # str | Baker address

try:
    # Get baker cycle rewards count
    api_response = api_instance.rewards_get_baker_rewards_count(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RewardsApi->rewards_get_baker_rewards_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Baker address | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rewards_get_delegator_rewards**
> list[DelegatorRewards] rewards_get_delegator_rewards(address, cycle=cycle, select=select, sort=sort, offset=offset, limit=limit, quote=quote)

Get delegator cycle rewards

Returns a list of delegator rewards for every cycle, including future cycles.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RewardsApi()
address = 'address_example' # str | Delegator address.
cycle = swagger_client.Cycle1() # Cycle1 | Filters rewards by cycle. (optional)
select = swagger_client.Select37() # Select37 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort44() # Sort44 | Sorts cycle rewards by specified field. Supported fields: `cycle` (default, desc). (optional)
offset = swagger_client.Offset42() # Offset42 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
quote = swagger_client.Quote53() # Quote53 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get delegator cycle rewards
    api_response = api_instance.rewards_get_delegator_rewards(address, cycle=cycle, select=select, sort=sort, offset=offset, limit=limit, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RewardsApi->rewards_get_delegator_rewards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Delegator address. | 
 **cycle** | [**Cycle1**](.md)| Filters rewards by cycle. | [optional] 
 **select** | [**Select37**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort44**](.md)| Sorts cycle rewards by specified field. Supported fields: &#x60;cycle&#x60; (default, desc). | [optional] 
 **offset** | [**Offset42**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **quote** | [**Quote53**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[DelegatorRewards]**](DelegatorRewards.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rewards_get_delegator_rewards_by_cycle**
> DelegatorRewards rewards_get_delegator_rewards_by_cycle(address, cycle, quote=quote)

Get delegator cycle rewards by cycle

Returns delegator cycle rewards for the specified cycle.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RewardsApi()
address = 'address_example' # str | Delegator address
cycle = 56 # int | Rewards cycle
quote = swagger_client.Quote54() # Quote54 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get delegator cycle rewards by cycle
    api_response = api_instance.rewards_get_delegator_rewards_by_cycle(address, cycle, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RewardsApi->rewards_get_delegator_rewards_by_cycle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Delegator address | 
 **cycle** | **int**| Rewards cycle | 
 **quote** | [**Quote54**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**DelegatorRewards**](DelegatorRewards.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rewards_get_delegator_rewards_count**
> int rewards_get_delegator_rewards_count(address)

Get delegator cycle rewards count

Returns total number of cycles where the delegator was delegated to an active baker

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RewardsApi()
address = 'address_example' # str | Delegator address

try:
    # Get delegator cycle rewards count
    api_response = api_instance.rewards_get_delegator_rewards_count(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RewardsApi->rewards_get_delegator_rewards_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Delegator address | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rewards_get_reward_split**
> RewardSplit rewards_get_reward_split(baker, cycle, offset=offset, limit=limit)

Get reward split

Returns baker rewards for the specified cycle with all delegator balances at that cycle to allow rewards distribution in proportion to shares.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RewardsApi()
baker = 'baker_example' # str | Baker address
cycle = 56 # int | Rewards cycle
offset = 0 # int | Specifies how many delegators in the reward split should be skipped (optional) (default to 0)
limit = 100 # int | Maximum number of delegators to return (optional) (default to 100)

try:
    # Get reward split
    api_response = api_instance.rewards_get_reward_split(baker, cycle, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RewardsApi->rewards_get_reward_split: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **baker** | **str**| Baker address | 
 **cycle** | **int**| Rewards cycle | 
 **offset** | **int**| Specifies how many delegators in the reward split should be skipped | [optional] [default to 0]
 **limit** | **int**| Maximum number of delegators to return | [optional] [default to 100]

### Return type

[**RewardSplit**](RewardSplit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rewards_get_reward_split_delegator**
> SplitDelegator rewards_get_reward_split_delegator(baker, cycle, delegator)

Get reward split delegator

Returns delegator from the reward split for the specified cycle.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RewardsApi()
baker = 'baker_example' # str | Baker address
cycle = 56 # int | Reward split cycle
delegator = 'delegator_example' # str | Delegator address

try:
    # Get reward split delegator
    api_response = api_instance.rewards_get_reward_split_delegator(baker, cycle, delegator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RewardsApi->rewards_get_reward_split_delegator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **baker** | **str**| Baker address | 
 **cycle** | **int**| Reward split cycle | 
 **delegator** | **str**| Delegator address | 

### Return type

[**SplitDelegator**](SplitDelegator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

