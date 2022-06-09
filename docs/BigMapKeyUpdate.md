# BigMapKeyUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal Id, can be used for pagination | [optional] 
**level** | **int** | Level of the block where the bigmap key was updated | [optional] 
**timestamp** | **datetime** | Timestamp of the block where the bigmap key was updated | [optional] 
**action** | **str** | Action with the key (&#x60;add_key&#x60;, &#x60;update_key&#x60;, &#x60;remove_key&#x60;) | [optional] 
**value** | **object** | Value in JSON or Micheline format, depending on the &#x60;micheline&#x60; query parameter. Note, if the action is &#x60;remove_key&#x60; it will contain the last non-null value. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

