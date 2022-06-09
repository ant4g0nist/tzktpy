# AccountParameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eq** | **str** | **Equal** filter mode (optional, i.e. &#x60;param.eq&#x3D;123&#x60; is the same as &#x60;param&#x3D;123&#x60;). \\ Specify a &#x60;tz&#x60; or &#x60;KT&#x60; address to get items where the specified field is equal to the specified value.  Example: &#x60;?sender&#x3D;tz1WnfXMPaNTBmH7DBPwqCWs9cPDJdkGBTZ8&#x60;. | [optional] 
**ne** | **str** | **Not equal** filter mode. \\ Specify a &#x60;tz&#x60; or &#x60;KT&#x60; address to get items where the specified field is not equal to the specified value.  Example: &#x60;?sender.ne&#x3D;tz1WnfXMPaNTBmH7DBPwqCWs9cPDJdkGBTZ8&#x60;. | [optional] 
**_in** | **list[str]** | **In list** (any of) filter mode. \\ Specify a comma-separated list of addresses to get items where the specified field is equal to one of the specified values.  Example: &#x60;?sender.in&#x3D;tz1WnfXMPaNTBWnfXMPaNTBWnfXMPaNTBNTB,tz1SiPXX4MYGNJNDSiPXX4MYGNJNDSiPXX4M&#x60;. | [optional] 
**ni** | **list[str]** | **Not in list** (none of) filter mode. \\ Specify a comma-separated list of addresses to get items where the specified field is not equal to all the specified values.  Example: &#x60;?sender.ni&#x3D;tz1WnfXMPaNTBWnfXMPaNTBWnfXMPaNTBNTB,tz1SiPXX4MYGNJNDSiPXX4MYGNJNDSiPXX4M&#x60;. | [optional] 
**eqx** | **str** | **Equal to another field** filter mode. \\ Specify a field name to get items where the specified fields are equal.  Example: &#x60;?sender.eqx&#x3D;target&#x60;. | [optional] 
**nex** | **str** | **Not equal to another field** filter mode. \\ Specify a field name to get items where the specified fields are not equal.  Example: &#x60;?sender.nex&#x3D;initiator&#x60;. | [optional] 
**null** | **bool** | **Is null** filter mode. \\ Use this mode to get items where the specified field is null or not.  Example: &#x60;?initiator.null&#x60; or &#x60;?initiator.null&#x3D;false&#x60;. | [optional] 
**in_has_null** | **bool** |  | [optional] 
**ni_has_null** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

