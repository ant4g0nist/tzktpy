# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**address** | **str** | Public key hash of the account | [optional] 
**alias** | **str** | Name of the project behind the account or account description | [optional] 
**public_key** | **str** | Base58 representation of account&#x27;s public key, revealed by the account | [optional] 
**revealed** | **bool** | Public key revelation status. Unrevealed account can&#x27;t send manager operation (transaction, origination etc.) | [optional] 
**balance** | **int** | Account balance | [optional] 
**counter** | **int** | An account nonce which is used to prevent operation replay | [optional] 
**delegate** | **object** | Information about the current delegate of the account. &#x60;null&#x60; if it&#x27;s not delegated | [optional] 
**delegation_level** | **int** | Block height of latest delegation. &#x60;null&#x60; if it&#x27;s not delegated | [optional] 
**delegation_time** | **datetime** | Block datetime of latest delegation (ISO 8601, e.g. &#x60;2020-02-20T02:40:57Z&#x60;). &#x60;null&#x60; if it&#x27;s not delegated | [optional] 
**num_contracts** | **int** | Number of contracts, created (originated) and/or managed by the contract | [optional] 
**active_tokens_count** | **int** | Number of account tokens with non-zero balances | [optional] 
**token_balances_count** | **int** | Number of tokens the account ever had | [optional] 
**token_transfers_count** | **int** | Number of token transfers from/to the account | [optional] 
**num_activations** | **int** | Number of account activation operations. Are used to activate accounts that were recommended allocations of tezos tokens for donations to the Tezos Foundation’s fundraiser | [optional] 
**num_delegations** | **int** | Number of delegation operations, related to the account | [optional] 
**num_originations** | **int** | Number of all origination (deployment / contract creation) operations, related to the account | [optional] 
**num_transactions** | **int** | Number of all transaction (tez transfer) operations, related to the account | [optional] 
**num_reveals** | **int** | Number of reveal (is used to reveal the public key associated with an account) operations of the contract | [optional] 
**num_register_constants** | **int** | Number of register global constant operations sent by the account | [optional] 
**num_set_deposits_limits** | **int** | Number of set deposits limit operations sent by the account | [optional] 
**num_migrations** | **int** | Number of migration (result of the context (database) migration during a protocol update) operations, related to the account (synthetic type)  | [optional] 
**first_activity** | **int** | Block height of the first operation, related to the account | [optional] 
**first_activity_time** | **datetime** | Block datetime of the first operation, related to the account (ISO 8601, e.g. &#x60;2020-02-20T02:40:57Z&#x60;) | [optional] 
**last_activity** | **int** | Height of the block in which the account state was changed last time | [optional] 
**last_activity_time** | **datetime** | Datetime of the block in which the account state was changed last time (ISO 8601, e.g. &#x60;2020-02-20T02:40:57Z&#x60;) | [optional] 
**metadata** | **object** | Metadata of the account (alias, logo, website, contacts, etc) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

