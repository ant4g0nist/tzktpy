# EndorsingRewardOperation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the operation, &#x60;endorsing_reward&#x60; | [optional] 
**id** | **int** | Unique ID of the operation, stored in the TzKT indexer database | [optional] 
**level** | **int** | Height of the block from the genesis | [optional] 
**timestamp** | **datetime** | Datetime at which the block is claimed to have been created (ISO 8601, e.g. &#x60;2020-02-20T02:40:57Z&#x60;) | [optional] 
**block** | **str** | Block hash | [optional] 
**baker** | **object** | Baker expected to receive endorsing reward | [optional] 
**expected** | **int** | Expected endorsing reward, based on baker&#x27;s active stake (micro tez) | [optional] 
**received** | **int** | Actually received endorsing reward (micro tez) | [optional] 
**quote** | **object** | Injected historical quote at the time of operation | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

