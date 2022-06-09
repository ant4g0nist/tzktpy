# BigMapDiff

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bigmap** | **int** | Bigmap Id | [optional] 
**path** | **str** | Path to the bigmap in the contract storage | [optional] 
**action** | **str** | Action with the bigmap (&#x60;allocate&#x60;, &#x60;add_key&#x60;, &#x60;update_key&#x60;, &#x60;remove_key&#x60;, &#x60;remove&#x60;) | [optional] 
**content** | **OneOfBigMapDiffContent** | Affected key. If the action is &#x60;allocate&#x60; or &#x60;remove&#x60; the key will be &#x60;null&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

