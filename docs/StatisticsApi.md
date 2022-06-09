# swagger_client.StatisticsApi

All URIs are relative to *https://api.tzkt.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statistics_get**](StatisticsApi.md#statistics_get) | **GET** /v1/statistics | Get statistics
[**statistics_get_cycles**](StatisticsApi.md#statistics_get_cycles) | **GET** /v1/statistics/current | Get current statistics
[**statistics_get_cycles_all**](StatisticsApi.md#statistics_get_cycles_all) | **GET** /v1/statistics/cyclic | Get cyclic statistics
[**statistics_get_daily**](StatisticsApi.md#statistics_get_daily) | **GET** /v1/statistics/daily | Get daily statistics

# **statistics_get**
> list[Statistics] statistics_get(level=level, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit, quote=quote)

Get statistics

Returns a list of end-of-block statistics.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatisticsApi()
level = swagger_client.Level44() # Level44 | Filters statistics by level. (optional)
timestamp = swagger_client.Timestamp42() # Timestamp42 | Filters statistics by timestamp. (optional)
select = swagger_client.Select40() # Select40 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort47() # Sort47 | Sorts delegators by specified field. Supported fields: `id` (default), `level`, `cycle`, `date`. (optional)
offset = swagger_client.Offset45() # Offset45 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
quote = swagger_client.Quote55() # Quote55 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get statistics
    api_response = api_instance.statistics_get(level=level, timestamp=timestamp, select=select, sort=sort, offset=offset, limit=limit, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->statistics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | [**Level44**](.md)| Filters statistics by level. | [optional] 
 **timestamp** | [**Timestamp42**](.md)| Filters statistics by timestamp. | [optional] 
 **select** | [**Select40**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort47**](.md)| Sorts delegators by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;level&#x60;, &#x60;cycle&#x60;, &#x60;date&#x60;. | [optional] 
 **offset** | [**Offset45**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **quote** | [**Quote55**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[Statistics]**](Statistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_get_cycles**
> Statistics statistics_get_cycles(select=select, quote=quote)

Get current statistics

Returns statistics at the end of a head block.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatisticsApi()
select = swagger_client.Select43() # Select43 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
quote = swagger_client.Quote58() # Quote58 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get current statistics
    api_response = api_instance.statistics_get_cycles(select=select, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->statistics_get_cycles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | [**Select43**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **quote** | [**Quote58**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**Statistics**](Statistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_get_cycles_all**
> list[Statistics] statistics_get_cycles_all(cycle=cycle, select=select, sort=sort, offset=offset, limit=limit, quote=quote)

Get cyclic statistics

Returns a list of end-of-cycle statistics.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatisticsApi()
cycle = swagger_client.Cycle4() # Cycle4 | Filters statistics by cycle. (optional)
select = swagger_client.Select42() # Select42 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort49() # Sort49 | Sorts delegators by specified field. Supported fields: `id` (default), `level`, `cycle`, `date`. (optional)
offset = swagger_client.Offset47() # Offset47 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
quote = swagger_client.Quote57() # Quote57 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get cyclic statistics
    api_response = api_instance.statistics_get_cycles_all(cycle=cycle, select=select, sort=sort, offset=offset, limit=limit, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->statistics_get_cycles_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cycle** | [**Cycle4**](.md)| Filters statistics by cycle. | [optional] 
 **select** | [**Select42**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort49**](.md)| Sorts delegators by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;level&#x60;, &#x60;cycle&#x60;, &#x60;date&#x60;. | [optional] 
 **offset** | [**Offset47**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **quote** | [**Quote57**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[Statistics]**](Statistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_get_daily**
> list[Statistics] statistics_get_daily(_date=_date, select=select, sort=sort, offset=offset, limit=limit, quote=quote)

Get daily statistics

Returns a list of end-of-day statistics.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatisticsApi()
_date = '2013-10-20' # date | Filters statistics by date. (optional)
select = swagger_client.Select41() # Select41 | Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both `.fields` and `.values` modes. (optional)
sort = swagger_client.Sort48() # Sort48 | Sorts delegators by specified field. Supported fields: `id` (default), `level`, `cycle`, `date`. (optional)
offset = swagger_client.Offset46() # Offset46 | Specifies which or how many items should be skipped (optional)
limit = 100 # int | Maximum number of items to return (optional) (default to 100)
quote = swagger_client.Quote56() # Quote56 | Comma-separated list of ticker symbols to inject historical prices into response (optional)

try:
    # Get daily statistics
    api_response = api_instance.statistics_get_daily(_date=_date, select=select, sort=sort, offset=offset, limit=limit, quote=quote)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->statistics_get_daily: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | [**date**](.md)| Filters statistics by date. | [optional] 
 **select** | [**Select41**](.md)| Specify comma-separated list of fields to include into response or leave it undefined to return full object. If you select single field, response will be an array of values in both &#x60;.fields&#x60; and &#x60;.values&#x60; modes. | [optional] 
 **sort** | [**Sort48**](.md)| Sorts delegators by specified field. Supported fields: &#x60;id&#x60; (default), &#x60;level&#x60;, &#x60;cycle&#x60;, &#x60;date&#x60;. | [optional] 
 **offset** | [**Offset46**](.md)| Specifies which or how many items should be skipped | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 100]
 **quote** | [**Quote56**](.md)| Comma-separated list of ticker symbols to inject historical prices into response | [optional] 

### Return type

[**list[Statistics]**](Statistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

