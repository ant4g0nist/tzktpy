# ProposalOperation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the operation, &#x60;proposal&#x60; - is used by bakers (delegates) to submit and/or upvote proposals to amend the protocol | [optional] 
**id** | **int** | Unique ID of the operation, stored in the TzKT indexer database | [optional] 
**level** | **int** | The height of the block from the genesis block, in which the operation was included | [optional] 
**timestamp** | **datetime** | Datetime of the block, in which the operation was included (ISO 8601, e.g. &#x60;2020-02-20T02:40:57Z&#x60;) | [optional] 
**block** | **str** | Hash of the block, in which the operation was included | [optional] 
**hash** | **str** | Hash of the operation | [optional] 
**period** | **object** | Information about the proposal period for which the proposal was submitted (upvoted) | [optional] 
**proposal** | **object** | Information about the submitted (upvoted) proposal | [optional] 
**delegate** | **object** | Information about the baker (delegate), submitted (upvoted) the proposal operation | [optional] 
**rolls** | **int** | Number of baker&#x27;s rolls (baker&#x27;s voting power) | [optional] 
**duplicated** | **bool** | Indicates whether proposal upvote has already been pushed. Duplicated proposal operations are not counted when selecting proposal-winner. | [optional] 
**quote** | **object** | Injected historical quote at the time of operation | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

