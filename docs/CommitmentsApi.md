# swagger_client.CommitmentsApi

All URIs are relative to *https://api.tzkt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commitments_get**](CommitmentsApi.md#commitments_get) | **GET** /v1/commitments/{address} | Get commitment by blinded address
[**commitments_get_all**](CommitmentsApi.md#commitments_get_all) | **GET** /v1/commitments | Get commitments
[**commitments_get_count**](CommitmentsApi.md#commitments_get_count) | **GET** /v1/commitments/count | Get commitments count

# **commitments_get**
> Commitment commitments_get(address)

Get commitment by blinded address

Returns a commitment with the specified blinded address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommitmentsApi()
address = 'address_example' # str | Blinded address (starting with btz)

try:
    # Get commitment by blinded address
    api_response = api_instance.commitments_get(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitmentsApi->commitments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Blinded address (starting with btz) | 

### Return type

[**Commitment**](Commitment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commitments_get_all**
> list[Commitment] commitments_get_all(activated=activated, activation_level=activation_level, balance=balance, select=select, sort=sort, offset=offset, limit=limit)

Get commitments

Returns a list of commitments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommitmentsApi()
activated = true # bool | Filters commitments by activation status (optional)
activation_level = swagger_client.ActivationLevel() # ActivationLevel | Filters commitments by activation level (optional)
balance = swagger_client.Balance3() # Balance3 | Filters commitments by activated balance (optional)
select = swagger_client.Select6() # Select6 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort11() # Sort11 | Sorts delegators by specified field. Supported fields: `id` (default), `balance`, `activationLevel`. (optional)
offset = swagger_client.Offset9() # Offset9 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)

try:
    # Get commitments
    api_response = api_instance.commitments_get_all(activated=activated, activation_level=activation_level, balance=balance, select=select, sort=sort, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitmentsApi->commitments_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activated** | **bool**| Filters commitments by activation status | [optional] 
 **activation_level** | [**ActivationLevel**](.md)| Filters commitments by activation level | [optional] 
 **balance** | [**Balance3**](.md)| Filters commitments by activated balance | [optional] 
 **select** | [**Select6**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort11**](.md)| Sorts delegators by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;balance&#x60;, &#x60;activationLevel&#x60;. | [optional] 
 **offset** | [**Offset9**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]

### Return type

[**list[Commitment]**](Commitment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commitments_get_count**
> int commitments_get_count(activated=activated, balance=balance)

Get commitments count

Returns a number of commitments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommitmentsApi()
activated = true # bool | Filters commitments by activation status (optional)
balance = swagger_client.Balance4() # Balance4 | Filters commitments by activated balance (optional)

try:
    # Get commitments count
    api_response = api_instance.commitments_get_count(activated=activated, balance=balance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitmentsApi->commitments_get_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activated** | **bool**| Filters commitments by activation status | [optional] 
 **balance** | [**Balance4**](.md)| Filters commitments by activated balance | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

