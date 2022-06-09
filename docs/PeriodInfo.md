# PeriodInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Voting period index, starting from zero | [optional] 
**epoch** | **int** | Voting epoch index, starting from zero | [optional] 
**kind** | **str** | Kind of the voting period &#x60;proposal&#x60; - delegates can submit protocol amendment proposals using the proposal operation &#x60;exploration&#x60; -  bakers (delegates) may vote on the top-ranked proposal from the previous Proposal Period using the ballot operation &#x60;testing&#x60; - If the proposal is approved in the Exploration Period, the testing (or &#x27;cooldown&#x27;) period begins and bakers start testing the new protocol &#x60;promotion&#x60; - delegates can cast one vote to promote or not the tested proposal using the ballot operation &#x60;adoption&#x60; - after the proposal is actually accepted, the ecosystem has some time to prepare to the upgrade Learn more: https://tezos.gitlab.io/whitedoc/voting.html | [optional] 
**first_level** | **int** | The height of the block in which the period starts | [optional] 
**last_level** | **int** | The height of the block in which the period ends | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

