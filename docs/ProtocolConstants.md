# ProtocolConstants

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ramp_up_cycles** | **int** | The number of cycles where security deposit is ramping up | [optional] 
**no_reward_cycles** | **int** | The number of cycles with no baking rewards | [optional] 
**preserved_cycles** | **int** | A number of cycles in which baker&#x27;s security deposit and rewards are frozen | [optional] 
**blocks_per_cycle** | **int** | A number of blocks the cycle contains | [optional] 
**blocks_per_commitment** | **int** | A number of blocks that indicates how often seed nonce hash is included in a block. Seed nonce hash presents in only one out of &#x60;blocksPerCommitment&#x60; | [optional] 
**blocks_per_snapshot** | **int** | A number of blocks that indicates how often a snapshot (snapshots are records of the state of rolls distributions) is taken | [optional] 
**blocks_per_voting** | **int** | A number of block that indicates how long a voting period takes | [optional] 
**time_between_blocks** | **int** | Minimum amount of seconds between blocks | [optional] 
**endorsers_per_block** | **int** | Number of bakers that assigned to endorse a block | [optional] 
**hard_operation_gas_limit** | **int** | Maximum amount of gas that one operation can consume | [optional] 
**hard_operation_storage_limit** | **int** | Maximum amount of storage that one operation can consume | [optional] 
**hard_block_gas_limit** | **int** | Maximum amount of total gas usage of a single block | [optional] 
**tokens_per_roll** | **int** | Required number of tokens to get 1 roll (micro tez) | [optional] 
**revelation_reward** | **int** | Reward for seed nonce revelation (micro tez) | [optional] 
**block_deposit** | **int** | Security deposit for baking (producing) a block (micro tez) | [optional] 
**block_reward** | **list[int]** | Reward for baking (producing) a block (micro tez) | [optional] 
**endorsement_deposit** | **int** | Security deposit for sending an endorsement operation (micro tez) | [optional] 
**endorsement_reward** | **list[int]** | Reward for sending an endorsement operation (micro tez) | [optional] 
**origination_size** | **int** | Initial storage size of an originated (created) account (bytes) | [optional] 
**byte_cost** | **int** | Cost of one storage byte in the blockchain (micro tez) | [optional] 
**proposal_quorum** | **float** | Percentage of the total number of rolls required to select a proposal on the proposal period | [optional] 
**ballot_quorum_min** | **float** | The minimum value of quorum percentage on the exploration and promotion periods | [optional] 
**ballot_quorum_max** | **float** | The maximum value of quorum percentage on the exploration and promotion periods | [optional] 
**lb_subsidy** | **int** | Liquidity baking subsidy is 1/16th of total rewards for a block of priority 0 with all endorsements | [optional] 
**lb_sunset_level** | **int** | Level after protocol activation when liquidity baking shuts off | [optional] 
**lb_escape_threshold** | **int** | 1/2 window size of 2000 blocks with precision of 1000 for integer computation | [optional] 
**consensus_threshold** | **int** | Endorsement quorum | [optional] 
**min_participation_numerator** | **int** | Number of endorsed slots needed to receive endorsing rewards | [optional] 
**min_participation_denominator** | **int** | Number of endorsed slots needed to receive endorsing rewards | [optional] 
**max_slashing_period** | **int** | Number of cycles after double baking/(pre)endorsing where an accusation operation can be injected | [optional] 
**frozen_deposits_percentage** | **int** | How much of baker&#x27;s active stake is frozen as a security deposit | [optional] 
**double_baking_punishment** | **int** | How much mutez is burned from baker&#x27;s frozen deposits, in case of double baking | [optional] 
**double_endorsing_punishment_numerator** | **int** | How much is burned from baker&#x27;s frozen deposits, in case of double (pre)endorsing | [optional] 
**double_endorsing_punishment_denominator** | **int** | How much is burned from baker&#x27;s frozen deposits, in case of double (pre)endorsing | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

