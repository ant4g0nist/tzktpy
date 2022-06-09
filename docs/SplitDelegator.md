# SplitDelegator

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address of the delegator | [optional] 
**balance** | **int** | Balance of the delegator at the snapshot time | [optional] 
**current_balance** | **int** | Balance of the delegator at the moment | [optional] 
**emptied** | **bool** | Indicates whether the delegator is emptied (at the moment, not at the snapshot time). Emptied accounts (users with zero balance) should be re-allocated, so if you make payment to emptied account you will pay (burn) &#x60;0.257 tez&#x60; allocation fee. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

