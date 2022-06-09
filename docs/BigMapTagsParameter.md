# BigMapTagsParameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eq** | **list[str]** | **Equal** filter mode (optional, i.e. &#x60;param.eq&#x3D;123&#x60; is the same as &#x60;param&#x3D;123&#x60;). \\ Specify a comma-separated list of bigmap tags to get bigmaps with exactly the same set of tags. Avoid using this mode and use &#x60;.any&#x60; or &#x60;.all&#x60; instead, because it may not work as expected due to internal &#x27;hidden&#x27; tags.  Example: &#x60;?tags&#x3D;metadata&#x60; or &#x60;?tags&#x3D;token_metadata,metadata&#x60;. | [optional] 
**any** | **list[str]** | **Has any** filter mode. \\ Specify a comma-separated list of bigmap tags to get bigmaps where at least one of the specified tags is presented.  Example: &#x60;?tags.any&#x3D;metadata&#x60; or &#x60;?tags.any&#x3D;token_metadata,metadata&#x60;. | [optional] 
**all** | **list[str]** | **Has all** filter mode. \\ Specify a comma-separated list of bigmap tags to get bigmaps where all of the specified tags are presented.  Example: &#x60;?tags.all&#x3D;metadata&#x60; or &#x60;?tags.all&#x3D;token_metadata,metadata&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

