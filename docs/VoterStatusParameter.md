# VoterStatusParameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eq** | **str** | **Equal** filter mode (optional, i.e. &#x60;param.eq&#x3D;123&#x60; is the same as &#x60;param&#x3D;123&#x60;). \\ Specify a voter status to get items where the specified field is equal to the specified value.  Example: &#x60;?status&#x3D;none&#x60;. | [optional] 
**ne** | **str** | **Not equal** filter mode. \\ Specify a voter status to get items where the specified field is not equal to the specified value.  Example: &#x60;?status.ne&#x3D;none&#x60;. | [optional] 
**_in** | **list[str]** | **In list** (any of) filter mode. \\ Specify a comma-separated list of voter statuses to get items where the specified field is equal to one of the specified values.  Example: &#x60;?status.in&#x3D;voted_yay,voted_nay&#x60;. | [optional] 
**ni** | **list[str]** | **Not in list** (none of) filter mode. \\ Specify a comma-separated list of voter statuses to get items where the specified field is not equal to all the specified values.  Example: &#x60;?status.ni&#x3D;none,upvoted&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

