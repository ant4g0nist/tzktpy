# TokenTransfer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Internal TzKT id.   **[sortable]** | [optional] 
**level** | **int** | Level of the block, at which the token transfer was made.   **[sortable]** | [optional] 
**timestamp** | **datetime** | Timestamp of the block, at which the token transfer was made. | [optional] 
**token** | **OneOfTokenTransferToken** | Token info.   Click on the field to expand more details. | [optional] 
**_from** | **OneOfTokenTransferFrom** | Sender account.   Click on the field to expand more details. | [optional] 
**to** | **OneOfTokenTransferTo** | Target account.   Click on the field to expand more details. | [optional] 
**amount** | **str** | Amount of tokens transferred (raw value, not divided by &#x60;decimals&#x60;).   **[sortable]** | [optional] 
**transaction_id** | **int** | Internal TzKT id of the transaction operation, caused the token transfer. | [optional] 
**origination_id** | **int** | Internal TzKT id of the origination operation, caused the token transfer. | [optional] 
**migration_id** | **int** | Internal TzKT id of the migration operation, caused the token transfer. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

