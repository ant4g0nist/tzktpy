# OffsetParameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**el** | **int** | **Elements** offset mode (optional, i.e. &#x60;offset.el&#x3D;123&#x60; is the same as &#x60;offset&#x3D;123&#x60;). \\ Skips specified number of elements.  Example: &#x60;?offset&#x3D;100&#x60;. | [optional] 
**pg** | **int** | **Page** offset mode. \\ Skips &#x60;page * limit&#x60; elements. This is a classic pagination.  Example: &#x60;?offset.pg&#x3D;1&#x60;. | [optional] 
**cr** | **int** | **Cursor** offset mode. \\ Skips all elements with the &#x60;cursor&#x60; before (including) the specified value. Cursor is a field used for sorting, e.g. &#x60;id&#x60;. Avoid using this offset mode with non-unique or non-sequential cursors such as &#x60;amount&#x60;, &#x60;balance&#x60;, etc.  Example: &#x60;?offset.cr&#x3D;45837&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

