# swagger_client.QuotesApi

All URIs are relative to *https://api.tzkt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotes_get**](QuotesApi.md#quotes_get) | **GET** /v1/quotes | Get quotes
[**quotes_get_count**](QuotesApi.md#quotes_get_count) | **GET** /v1/quotes/count | Get quotes count
[**quotes_get_last**](QuotesApi.md#quotes_get_last) | **GET** /v1/quotes/last | Get last quote

# **quotes_get**
> list[Quote] quotes_get(level=level, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit)

Get quotes

Returns a list of quotes aligned with blocks.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuotesApi()
level = swagger_client.Level41() # Level41 | Filters quotes by level. (optional)
timestamp = swagger_client.Timestamp41() # Timestamp41 | Filters quotes by timestamp. (optional)
select = swagger_client.Select35() # Select35 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort42() # Sort42 | Sorts quotes by specified field. Supported fields: `level` (default). (optional)
offset = swagger_client.Offset40() # Offset40 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)

try:
    # Get quotes
    api_response = api_instance.quotes_get(level=level, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->quotes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | [**Level41**](.md)| Filters quotes by level. | [optional] 
 **timestamp** | [**Timestamp41**](.md)| Filters quotes by timestamp. | [optional] 
 **select** | [**Select35**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort42**](.md)| Sorts quotes by specified field. Supported fields: &#x60;level&#x60; (default). | [optional] 
 **offset** | [**Offset40**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]

### Return type

[**list[Quote]**](Quote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotes_get_count**
> int quotes_get_count()

Get quotes count

Returns the total number of quotes aligned with blocks.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuotesApi()

try:
    # Get quotes count
    api_response = api_instance.quotes_get_count()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->quotes_get_count: %s\n" % e)
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

# **quotes_get_last**
> Quote quotes_get_last()

Get last quote

Returns last known quote.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuotesApi()

try:
    # Get last quote
    api_response = api_instance.quotes_get_last()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->quotes_get_last: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Quote**](Quote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

