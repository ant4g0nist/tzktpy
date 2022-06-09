# BigMapUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal Id, can be used for pagination | [optional] 
**level** | **int** | Level of the block where the bigmap was updated | [optional] 
**timestamp** | **datetime** | Timestamp of the block where the bigmap was updated | [optional] 
**bigmap** | **int** | Bigmap ptr | [optional] 
**contract** | **OneOfBigMapUpdateContract** | Smart contract in which&#x27;s storage the bigmap is allocated | [optional] 
**path** | **str** | Path to the bigmap in the contract storage | [optional] 
**action** | **str** | Action with the bigmap (&#x60;allocate&#x60;, &#x60;add_key&#x60;, &#x60;update_key&#x60;, &#x60;remove_key&#x60;, &#x60;remove&#x60;) | [optional] 
**content** | **OneOfBigMapUpdateContent** | Updated key. If the action is &#x60;allocate&#x60; or &#x60;remove&#x60; the content will be &#x60;null&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

