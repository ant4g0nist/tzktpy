# BallotOperation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the operation, &#x60;ballot&#x60; - is used to vote for a proposal in a given voting cycle | [optional] 
**id** | **int** | Unique ID of the operation, stored in the TzKT indexer database | [optional] 
**level** | **int** | The height of the block from the genesis block, in which the operation was included | [optional] 
**timestamp** | **datetime** | Datetime of the block, in which the operation was included (ISO 8601, e.g. &#x60;2020-02-20T02:40:57Z&#x60;) | [optional] 
**block** | **str** | Hash of the block, in which the operation was included | [optional] 
**hash** | **str** | Hash of the operation | [optional] 
**period** | **object** | Information about the voting period for which the ballot was submitted | [optional] 
**proposal** | **object** | Information about the proposal for which ballot was submitted | [optional] 
**delegate** | **object** | Information about the delegate (baker), submitted the ballot | [optional] 
**rolls** | **int** | Number of baker&#x27;s rolls (baker&#x27;s voting power) | [optional] 
**vote** | **str** | Vote, given in the ballot (&#x60;yay&#x60;, &#x60;nay&#x60;, or &#x60;pass&#x60;) | [optional] 
**quote** | **object** | Injected historical quote at the time of operation | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

