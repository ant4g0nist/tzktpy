# TokenBalance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal TzKT id.   **[sortable]** | [optional] 
**account** | **OneOfTokenBalanceAccount** | Owner account.   Click on the field to expand more details. | [optional] 
**token** | **OneOfTokenBalanceToken** | Token info.   Click on the field to expand more details. | [optional] 
**balance** | **str** | Balance (raw value, not divided by &#x60;decimals&#x60;).   **[sortable]** | [optional] 
**transfers_count** | **int** | Total number of transfers, affecting the token balance.   **[sortable]** | [optional] 
**first_level** | **int** | Level of the block where the token balance was first changed.   **[sortable]** | [optional] 
**first_time** | **datetime** | Timestamp of the block where the token balance was first changed. | [optional] 
**last_level** | **int** | Level of the block where the token balance was last changed.   **[sortable]** | [optional] 
**last_time** | **datetime** | Timestamp of the block where the token balance was last changed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

