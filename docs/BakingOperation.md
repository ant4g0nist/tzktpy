# BakingOperation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the operation, &#x60;baking&#x60; - an operation which contains brief information about a baked (produced) block (synthetic type) | [optional] 
**id** | **int** | Unique ID of the operation, stored in the TzKT indexer database | [optional] 
**level** | **int** | Height of the block from the genesis | [optional] 
**timestamp** | **datetime** | Datetime at which the block is claimed to have been created (ISO 8601, e.g. &#x60;2020-02-20T02:40:57Z&#x60;) | [optional] 
**block** | **str** | Block hash | [optional] 
**proposer** | **object** | Baker who proposed the block payload | [optional] 
**producer** | **object** | Baker who produced the block | [optional] 
**payload_round** | **int** | Round at which the block payload was proposed | [optional] 
**block_round** | **int** | Round at which the block was produced | [optional] 
**deposit** | **int** | Security deposit frozen on the baker&#x27;s account for producing the block (micro tez) | [optional] 
**reward** | **int** | Fixed reward paid to the payload proposer (micro tez) | [optional] 
**bonus** | **int** | Bonus reward paid to the block producer (micro tez) | [optional] 
**fees** | **int** | Total fee gathered from operations, included into the block | [optional] 
**quote** | **object** | Injected historical quote at the time of operation | [optional] 
**baker** | **object** | [DEPRECATED] | [optional] 
**priority** | **int** | [DEPRECATED] | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

