# DateTimeParameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eq** | **datetime** | **Equal** filter mode (optional, i.e. &#x60;param.eq&#x3D;2020-01-01&#x60; is the same as &#x60;param&#x3D;2020-01-01&#x60;). \\ Specify a datetime to get items where the specified field is equal to the specified value.  Example: &#x60;?timestamp&#x3D;2020-02-20T02:40:57Z&#x60;. | [optional] 
**ne** | **datetime** | **Not equal** filter mode. \\ Specify a datetime to get items where the specified field is not equal to the specified value.  Example: &#x60;?timestamp.ne&#x3D;2020-02-20T02:40:57Z&#x60;. | [optional] 
**gt** | **datetime** | **Greater than** filter mode. \\ Specify a datetime to get items where the specified field is greater than the specified value.  Example: &#x60;?timestamp.gt&#x3D;2020-02-20T02:40:57Z&#x60;. | [optional] 
**ge** | **datetime** | **Greater or equal** filter mode. \\ Specify a datetime to get items where the specified field is greater than equal to the specified value.  Example: &#x60;?timestamp.ge&#x3D;2020-02-20T02:40:57Z&#x60;. | [optional] 
**lt** | **datetime** | **Less than** filter mode. \\ Specify a datetime to get items where the specified field is less than the specified value.  Example: &#x60;?timestamp.lt&#x3D;2020-02-20T02:40:57Z&#x60;. | [optional] 
**le** | **datetime** | **Less or equal** filter mode. \\ Specify a datetime to get items where the specified field is less than or equal to the specified value.  Example: &#x60;?timestamp.le&#x3D;2020-02-20T02:40:57Z&#x60;. | [optional] 
**_in** | **list[datetime]** | **In list** (any of) filter mode. \\ Specify a comma-separated list of datetimes to get items where the specified field is equal to one of the specified values.  Example: &#x60;?timestamp.in&#x3D;2020-02-20,2020-02-21&#x60;. | [optional] 
**ni** | **list[datetime]** | **Not in list** (none of) filter mode. \\ Specify a comma-separated list of datetimes to get items where the specified field is not equal to all the specified values.  Example: &#x60;?timestamp.ni&#x3D;2020-02-20,2020-02-21&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

