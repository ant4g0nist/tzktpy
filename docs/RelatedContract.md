# RelatedContract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Kind of the contract (&#x60;delegator_contract&#x60; or &#x60;smart_contract&#x60;), where &#x60;delegator_contract&#x60; - manager.tz smart contract for delegation purpose only | [optional] 
**alias** | **str** | Name of the project behind the contract or contract description | [optional] 
**address** | **str** | Public key hash of the contract | [optional] 
**balance** | **int** | Contract balance (micro tez) | [optional] 
**delegate** | **OneOfRelatedContractDelegate** | Information about the current delegate of the contract. &#x60;null&#x60; if it&#x27;s not delegated | [optional] 
**creation_level** | **int** | Height of the block where the contract was created | [optional] 
**creation_time** | **datetime** | Datetime of the block where the contract was created (ISO 8601, e.g. &#x60;2020-02-20T02:40:57Z&#x60;) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

