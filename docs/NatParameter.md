# NatParameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eq** | **str** | **Equal** filter mode (optional, i.e. &#x60;param.eq&#x3D;123&#x60; is the same as &#x60;param&#x3D;123&#x60;). \\ Specify a &#x60;nat&#x60; value to get items where the specified field is equal to the specified value.  Example: &#x60;?balance&#x3D;1234&#x60;. | [optional] 
**ne** | **str** | **Not equal** filter mode. \\ Specify a &#x60;nat&#x60; value to get items where the specified field is not equal to the specified value.  Example: &#x60;?balance.ne&#x3D;1234&#x60;. | [optional] 
**gt** | **str** | **Greater than** filter mode. \\ Specify a &#x60;nat&#x60; value to get items where the specified field is greater than the specified value.  Example: &#x60;?balance.gt&#x3D;1234&#x60;. | [optional] 
**ge** | **str** | **Greater or equal** filter mode. \\ Specify a &#x60;nat&#x60; value to get items where the specified field is greater than equal to the specified value.  Example: &#x60;?balance.ge&#x3D;1234&#x60;. | [optional] 
**lt** | **str** | **Less than** filter mode. \\ Specify a &#x60;nat&#x60; value to get items where the specified field is less than the specified value.  Example: &#x60;?balance.lt&#x3D;1234&#x60;. | [optional] 
**le** | **str** | **Less or equal** filter mode. \\ Specify a &#x60;nat&#x60; value to get items where the specified field is less than or equal to the specified value.  Example: &#x60;?balance.le&#x3D;1234&#x60;. | [optional] 
**_in** | **list[str]** | **In list** (any of) filter mode. \\ Specify a comma-separated list of &#x60;nat&#x60; values to get items where the specified field is equal to one of the specified values.  Example: &#x60;?level.in&#x3D;12,14,52,69&#x60;. | [optional] 
**ni** | **list[str]** | **Not in list** (none of) filter mode. \\ Specify a comma-separated list of &#x60;nat&#x60; values to get items where the specified field is not equal to all the specified values.  Example: &#x60;?level.ni&#x3D;12,14,52,69&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

