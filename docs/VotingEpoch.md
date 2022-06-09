# VotingEpoch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Index of the voting epoch, starting from zero | [optional] 
**first_level** | **int** | The height of the block in which the epoch starts | [optional] 
**start_time** | **datetime** | The timestamp of the block in which the epoch starts | [optional] 
**last_level** | **int** | The height of the block in which the epoch ends | [optional] 
**end_time** | **datetime** | The timestamp of the block in which the epoch ends | [optional] 
**status** | **str** | Status of the voting epoch: &#x60;no_proposals&#x60; - there were no proposals proposed &#x60;voting&#x60; - there was at least one proposal and the voting is in progress &#x60;completed&#x60; - voting successfully completed and the proposal was accepted &#x60;failed&#x60; - voting was not completed due to either quorum or supermajority was not reached | [optional] 
**periods** | [**list[VotingPeriod]**](VotingPeriod.md) | Voting periods in the epoch | [optional] 
**proposals** | [**list[Proposal]**](Proposal.md) | Proposals pushed during the voting epoch (null, if there were no proposals). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

