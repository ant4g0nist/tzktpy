# Protocol

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Protocol code, representing a number of protocol changes since genesis (mod 256, but &#x60;-1&#x60; for the genesis block) | [optional] 
**hash** | **str** | Hash of the protocol | [optional] 
**first_level** | **int** | Block height where the protocol was applied | [optional] 
**first_cycle** | **int** | Index of the first cycle started with the protocol | [optional] 
**first_cycle_level** | **int** | Level of the first block of the first cycle started with the protocol | [optional] 
**last_level** | **int** | Block height where the protocol ends. &#x60;null&#x60; if the protocol is active | [optional] 
**constants** | **OneOfProtocolConstants** | Information about the protocol constants | [optional] 
**metadata** | **OneOfProtocolMetadata** | Offchain metadata | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

