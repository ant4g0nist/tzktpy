# VotingPeriod

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Index of the voting period, starting from zero | [optional] 
**epoch** | **int** | Index of the voting epoch, starting from zero | [optional] 
**first_level** | **int** | The height of the block in which the period starts | [optional] 
**start_time** | **datetime** | The timestamp of the block in which the period starts | [optional] 
**last_level** | **int** | The height of the block in which the period ends | [optional] 
**end_time** | **datetime** | The timestamp of the block in which the period ends | [optional] 
**kind** | **str** | Kind of the voting period: &#x60;proposal&#x60; - delegates can submit protocol amendment proposals using the proposal operation &#x60;exploration&#x60; -  bakers (delegates) may vote on the top-ranked proposal from the previous Proposal Period using the ballot operation &#x60;testing&#x60; - If the proposal is approved in the Exploration Period, the testing (or &#x27;cooldown&#x27;) period begins and bakers start testing the new protocol &#x60;promotion&#x60; - delegates can cast one vote to promote or not the tested proposal using the ballot operation &#x60;adoption&#x60; - after the proposal is actually accepted, the ecosystem has some time to prepare to the upgrade Learn more: https://tezos.gitlab.io/whitedoc/voting.html | [optional] 
**status** | **str** | Status of the voting period: &#x60;active&#x60; - means that the voting period is in progress &#x60;no_proposals&#x60; - means that there were no proposals during the voting period &#x60;no_quorum&#x60; - means that there was a voting but the quorum was not reached &#x60;no_supermajority&#x60; - means that there was a voting but the supermajority was not reached &#x60;success&#x60; - means that the period was finished with positive voting result | [optional] 
**total_bakers** | **int** | The number of bakers on the voters list | [optional] 
**total_rolls** | **int** | The number of rolls of bakers on the voters list | [optional] 
**upvotes_quorum** | **float** | Upvotes quorum percentage (only for proposal period) | [optional] 
**proposals_count** | **int** | The number of proposals injected during the voting period (only for proposal period) | [optional] 
**top_upvotes** | **int** | This is how many upvotes (proposal operations) the most upvoted proposal has (only for proposal period) | [optional] 
**top_rolls** | **int** | This is how many rolls the most upvoted proposal has (only for proposal period) | [optional] 
**ballots_quorum** | **float** | Ballots quorum percentage (only for exploration and promotion periods) | [optional] 
**supermajority** | **float** | Supermajority percentage (only for exploration and promotion periods) | [optional] 
**yay_ballots** | **int** | The number of the ballots with \&quot;yay\&quot; vote (only for exploration and promotion periods) | [optional] 
**yay_rolls** | **int** | Total rolls of the ballots with \&quot;yay\&quot; vote (only for exploration and promotion periods) | [optional] 
**nay_ballots** | **int** | The number of the ballots with \&quot;nay\&quot; vote (only for exploration and promotion periods) | [optional] 
**nay_rolls** | **int** | Total rolls of the ballots with \&quot;nay\&quot; vote (only for exploration and promotion periods) | [optional] 
**pass_ballots** | **int** | The number of the ballots with \&quot;pass\&quot; vote (only for exploration and promotion periods) | [optional] 
**pass_rolls** | **int** | Total rolls of the ballots with \&quot;pass\&quot; vote (only for exploration and promotion periods) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

