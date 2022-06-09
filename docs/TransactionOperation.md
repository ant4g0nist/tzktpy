# TransactionOperation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the operation, &#x60;transaction&#x60; - is a standard operation used to transfer tezos tokens to an account | [optional] 
**id** | **int** | Unique ID of the operation, stored in the TzKT indexer database | [optional] 
**level** | **int** | The height of the block from the genesis block, in which the operation was included | [optional] 
**timestamp** | **datetime** | Datetime of the block, in which the operation was included (ISO 8601, e.g. &#x60;2020-02-20T02:40:57Z&#x60;) | [optional] 
**block** | **str** | Hash of the block, in which the operation was included | [optional] 
**hash** | **str** | Hash of the operation | [optional] 
**counter** | **int** | An account nonce which is used to prevent operation replay | [optional] 
**initiator** | **object** | Information about the initiator of the transaction call | [optional] 
**sender** | **object** | Information about the account sent the transaction | [optional] 
**nonce** | **int** | An account nonce which is used to prevent internal operation replay | [optional] 
**gas_limit** | **int** | A cap on the amount of gas a given operation can consume | [optional] 
**gas_used** | **int** | Amount of gas, consumed by the operation | [optional] 
**storage_limit** | **int** | A cap on the amount of storage a given operation can consume | [optional] 
**storage_used** | **int** | Amount of storage, consumed by the operation | [optional] 
**baker_fee** | **int** | Fee to the baker, produced block, in which the operation was included (micro tez) | [optional] 
**storage_fee** | **int** | The amount of funds burned from the sender account for used the blockchain storage (micro tez) | [optional] 
**allocation_fee** | **int** | The amount of funds burned from the sender account for account creation (micro tez) | [optional] 
**target** | **object** | Information about the target of the transaction | [optional] 
**amount** | **int** | The transaction amount (micro tez) | [optional] 
**parameter** | **object** | Transaction parameter, including called entrypoint and value passed to the entrypoint. | [optional] 
**storage** | **object** | Contract storage after executing the transaction converted to human-readable JSON. Note: you can configure storage format by setting &#x60;micheline&#x60; query parameter. | [optional] 
**diffs** | [**list[BigMapDiff]**](BigMapDiff.md) | List of bigmap updates (aka big_map_diffs) caused by the transaction. | [optional] 
**status** | **str** | Operation status (&#x60;applied&#x60; - an operation applied by the node and successfully added to the blockchain, &#x60;failed&#x60; - an operation which failed with some particular error (not enough balance, gas limit, etc), &#x60;backtracked&#x60; - an operation which was successful but reverted due to one of the following operations in the same operation group was failed, &#x60;skipped&#x60; - all operations after the failed one in an operation group) | [optional] 
**errors** | [**list[OperationError]**](OperationError.md) | List of errors provided by the node, injected the operation to the blockchain. &#x60;null&#x60; if there is no errors | [optional] 
**has_internals** | **bool** | An indication of whether the transaction has an internal operations &#x60;true&#x60; - there are internal operations &#x60;false&#x60; - no internal operations | [optional] 
**token_transfers_count** | **int** | Number of token transfers produced by the operation, or &#x60;null&#x60; if there are no transfers | [optional] 
**quote** | **object** | Injected historical quote at the time of operation | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

