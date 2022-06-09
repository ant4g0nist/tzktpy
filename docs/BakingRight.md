# BakingRight

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the right: - &#x60;baking&#x60; - right to bake (produce) a block; - &#x60;endorsing&#x60; - right to endorse (validate) a block. | [optional] 
**cycle** | **int** | Cycle on which the right can be realized. | [optional] 
**level** | **int** | Level at which a block must be baked or an endorsement must be sent. | [optional] 
**timestamp** | **datetime** | Time (estimated, in case of future rights) when a block must be baked or an endorsement must be sent. | [optional] 
**round** | **int** | Round (0 - ∞) at which the baker can propose/produce a block. If a baker at round  &#x60;0&#x60; doesn&#x27;t produce a block within the given time interval, then the right goes to a baker at round&#x60; 1&#x60;, etc. For &#x60;endorsing&#x60; rights this field is always &#x60;null&#x60;. | [optional] 
**slots** | **int** | Number of slots (1 - 32) to be endorsed. For &#x60;baking&#x60; rights this field is always &#x60;null&#x60;. | [optional] 
**baker** | **OneOfBakingRightBaker** | Baker to which baking or endorsing right has been given. | [optional] 
**status** | **str** | Status of the baking or endorsing right: - &#x60;future&#x60; - the right is not realized yet; - &#x60;realized&#x60; - the right was successfully realized; - &#x60;missed&#x60; - the right was not realized. | [optional] 
**priority** | **int** | [DEPRECATED] | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

