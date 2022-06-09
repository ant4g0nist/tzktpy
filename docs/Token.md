# Token

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal TzKT id (not the same as &#x60;tokenId&#x60;).   **[sortable]** | [optional] 
**contract** | **OneOfTokenContract** | Contract, created the token. | [optional] 
**token_id** | **str** | Token id, unique within the contract.   **[sortable]** | [optional] 
**standard** | **str** | Token standard (&#x60;fa1.2&#x60; or &#x60;fa2&#x60;). | [optional] 
**first_level** | **int** | Level of the block where the token was first seen.   **[sortable]** | [optional] 
**first_time** | **datetime** | Timestamp of the block where the token was first seen. | [optional] 
**last_level** | **int** | Level of the block where the token was last seen.   **[sortable]** | [optional] 
**last_time** | **datetime** | Timestamp of the block where the token was last seen. | [optional] 
**transfers_count** | **int** | Total number of transfers.   **[sortable]** | [optional] 
**balances_count** | **int** | Total number of holders ever seen.   **[sortable]** | [optional] 
**holders_count** | **int** | Total number of current holders.   **[sortable]** | [optional] 
**total_minted** | **str** | Total number of minted tokens (raw value, not divided by &#x60;decimals&#x60;). | [optional] 
**total_burned** | **str** | Total number of burned tokens (raw value, not divided by &#x60;decimals&#x60;). | [optional] 
**total_supply** | **str** | Total number of existing tokens (raw value, not divided by &#x60;decimals&#x60;). | [optional] 
**metadata** | **object** | Token metadata.   **[sortable]** | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

