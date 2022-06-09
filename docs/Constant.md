# Constant

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Global address (expression hash) | [optional] 
**value** | **object** | Constant value (either micheline, michelson or bytes, depending on the &#x60;format&#x60; parameter) | [optional] 
**size** | **int** | Constant size in bytes | [optional] 
**refs** | **int** | Number of contracts referencing this constant | [optional] 
**creator** | **OneOfConstantCreator** | Account registered this constant | [optional] 
**creation_level** | **int** | Level of the first block baked with this software | [optional] 
**creation_time** | **datetime** | Datetime of the first block baked with this software | [optional] 
**metadata** | **OneOfConstantMetadata** | Offchain metadata | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

