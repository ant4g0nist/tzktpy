# Int64Parameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eq** | **int** | **Equal** filter mode (optional, i.e. &#x60;param.eq&#x3D;123&#x60; is the same as &#x60;param&#x3D;123&#x60;). \\ Specify an integer number to get items where the specified field is equal to the specified value.  Example: &#x60;?balance&#x3D;1234&#x60;. | [optional] 
**ne** | **int** | **Not equal** filter mode. \\ Specify an integer number to get items where the specified field is not equal to the specified value.  Example: &#x60;?balance.ne&#x3D;1234&#x60;. | [optional] 
**gt** | **int** | **Greater than** filter mode. \\ Specify an integer number to get items where the specified field is greater than the specified value.  Example: &#x60;?balance.gt&#x3D;1234&#x60;. | [optional] 
**ge** | **int** | **Greater or equal** filter mode. \\ Specify an integer number to get items where the specified field is greater than equal to the specified value.  Example: &#x60;?balance.ge&#x3D;1234&#x60;. | [optional] 
**lt** | **int** | **Less than** filter mode. \\ Specify an integer number to get items where the specified field is less than the specified value.  Example: &#x60;?balance.lt&#x3D;1234&#x60;. | [optional] 
**le** | **int** | **Less or equal** filter mode. \\ Specify an integer number to get items where the specified field is less than or equal to the specified value.  Example: &#x60;?balance.le&#x3D;1234&#x60;. | [optional] 
**_in** | **list[int]** | **In list** (any of) filter mode. \\ Specify a comma-separated list of integers to get items where the specified field is equal to one of the specified values.  Example: &#x60;?level.in&#x3D;12,14,52,69&#x60;. | [optional] 
**ni** | **list[int]** | **Not in list** (none of) filter mode. \\ Specify a comma-separated list of integers to get items where the specified field is not equal to all the specified values.  Example: &#x60;?level.ni&#x3D;12,14,52,69&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

