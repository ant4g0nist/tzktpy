# SelectionParameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | **list[str]** | **Fields** selection mode (optional, i.e. &#x60;select.fields&#x3D;balance&#x60; is the same as &#x60;select&#x3D;balance&#x60;). \\ Specify a comma-separated list of fields to include into response.  Example: &#x60;?select&#x3D;address,balance as b,metadata.name as meta_name&#x60; will result in &#x60;[ { \&quot;address\&quot;: \&quot;asd\&quot;, \&quot;b\&quot;: 10, \&quot;meta_name\&quot;: \&quot;qwe\&quot; } ]&#x60;. | [optional] 
**values** | **list[str]** | **Values** selection mode. \\ Specify a comma-separated list of fields to include their values into response.  Example: &#x60;?select.values&#x3D;address,balance,metadata.name&#x60;  will result in &#x60;[ [ \&quot;asd\&quot;, 10, \&quot;qwe\&quot; ] ]&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

