# NonceRevelationOperation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the operation, &#x60;nonce_revelation&#x60; - are used by the blockchain to create randomness | [optional] 
**id** | **int** | Unique ID of the operation, stored in the TzKT indexer database | [optional] 
**level** | **int** | The height of the block from the genesis block, in which the operation was included | [optional] 
**timestamp** | **datetime** | Datetime of the block, in which the operation was included (ISO 8601, e.g. &#x60;2020-02-20T02:40:57Z&#x60;) | [optional] 
**block** | **str** | Hash of the block, in which the operation was included | [optional] 
**hash** | **str** | Hash of the operation | [optional] 
**baker** | **object** | Information about the delegate (baker), who produced the block with the operation | [optional] 
**sender** | **object** | Information about the delegate (baker), who revealed the nonce (sent the operation) | [optional] 
**revealed_level** | **int** | Block height of the block, where seed nonce hash is stored | [optional] 
**revealed_cycle** | **int** | Cycle for which seed nonce was revealed | [optional] 
**nonce** | **str** | Seed nonce hex | [optional] 
**reward** | **int** | Baker reward for including seed nonce revelation into a block | [optional] 
**quote** | **object** | Injected historical quote at the time of operation | [optional] 
**baker_rewards** | **int** | [DEPRECATED] | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

