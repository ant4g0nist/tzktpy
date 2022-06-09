# MigrationOperation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the operation, &#x60;migration&#x60; - result of the context (database) migration during a protocol update (synthetic type) | [optional] 
**id** | **int** | Unique ID of the operation, stored in the TzKT indexer database | [optional] 
**level** | **int** | The height of the block from the genesis block, in which the operation was included | [optional] 
**timestamp** | **datetime** | Datetime of the block, in which the operation was included (ISO 8601, e.g. &#x60;2020-02-20T02:40:57Z&#x60;) | [optional] 
**block** | **str** | Hash of the block, in which the operation was included | [optional] 
**kind** | **str** | Kind of the migration  &#x60;bootstrap&#x60; - balance updates, included in the first block after genesis &#x60;activate_delegate&#x60; - registering a new baker (delegator) during protocol migration &#x60;airdrop&#x60; - airdrop of 1 micro tez during Babylon protocol upgrade &#x60;proposal_invoice&#x60; - invoice for creation a proposal for protocol upgrade &#x60;code_change&#x60; - changing contract scripts during Babylon protocol upgrade &#x60;origination&#x60; - implicit (hardcoded in the protocol) origination of liquidity baking contracts &#x60;subsidy&#x60; - liquidity baking subsidy | [optional] 
**account** | **object** | Information about the account whose balance has updated as a result of the operation | [optional] 
**balance_change** | **int** | The amount for which the operation updated the balance (micro tez) | [optional] 
**storage** | **object** | Contract storage after the migration converted to human-readable JSON. Note: you can configure storage format by setting &#x60;micheline&#x60; query parameter. | [optional] 
**diffs** | [**list[BigMapDiff]**](BigMapDiff.md) | List of bigmap updates caused by the migration. | [optional] 
**token_transfers_count** | **int** | Number of token transfers produced by the operation, or &#x60;null&#x60; if there are no transfers | [optional] 
**quote** | **object** | Injected historical quote at the time of operation | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

