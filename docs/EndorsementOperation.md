# EndorsementOperation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the operation, &#x60;endorsement&#x60; - is operation, which specifies the head of the chain as seen by the endorser of a given slot. The endorser is randomly selected to be included in the block that extends the head of the chain as specified in this operation. A block with more endorsements improves the weight of the chain and increases the likelihood of that chain being the canonical one. | [optional] 
**id** | **int** | Unique ID of the operation, stored in the TzKT indexer database | [optional] 
**level** | **int** | The height of the block from the genesis block, in which the operation was included | [optional] 
**timestamp** | **datetime** | Datetime of the block, in which the operation was included (ISO 8601, e.g. &#x60;2020-02-20T02:40:57Z&#x60;) | [optional] 
**block** | **str** | Hash of the block, in which the operation was included | [optional] 
**hash** | **str** | Hash of the operation | [optional] 
**delegate** | **object** | Information about the baker who sent the operation | [optional] 
**slots** | **int** | Number of assigned endorsement slots to the baker who sent the operation | [optional] 
**deposit** | **int** | Security deposit frozen on the baker&#x27;s account | [optional] 
**rewards** | **int** | Reward of the baker for the operation | [optional] 
**quote** | **object** | Injected historical quote at the time of operation | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

