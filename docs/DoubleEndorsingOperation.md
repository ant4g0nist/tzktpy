# DoubleEndorsingOperation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the operation, &#x60;double_endorsing&#x60; - is used by bakers to provide evidence of double endorsement (endorsing two different blocks at the same block height) by a baker | [optional] 
**id** | **int** | Unique ID of the operation, stored in the TzKT indexer database | [optional] 
**level** | **int** | Height of the block from the genesis block, in which the operation was included | [optional] 
**timestamp** | **datetime** | Datetime of the block, in which the operation was included (ISO 8601, e.g. &#x60;2020-02-20T02:40:57Z&#x60;) | [optional] 
**block** | **str** | Hash of the block, in which the operation was included | [optional] 
**hash** | **str** | Hash of the operation | [optional] 
**accused_level** | **int** | Height of the block from the genesis, at which double endorsing occurred  | [optional] 
**accuser** | **object** | Information about the baker, produced the block, in which the accusation was included | [optional] 
**accuser_reward** | **int** | Reward of the baker, produced the block, in which the accusation was included | [optional] 
**offender** | **object** | Information about the baker, accused for producing two different endorsements at the same level | [optional] 
**offender_loss** | **int** | Amount of frozen deposits lost by accused baker | [optional] 
**quote** | **object** | Injected historical quote at the time of operation | [optional] 
**accuser_rewards** | **int** | [DEPRECATED] | [optional] 
**offender_lost_deposits** | **int** | [DEPRECATED] | [optional] 
**offender_lost_rewards** | **int** | [DEPRECATED] | [optional] 
**offender_lost_fees** | **int** | [DEPRECATED] | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

