# Status

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Indicates the type/level/severity expressed by this Status. This can be used to choose icons, and determine whether to show different Status entries.  | value | description | | ----- | ----------- | | unknown | The type/severity of this status couldn&#x27;t be determined. Should be rare. May still populate &#x60;title&#x60; and &#x60;description&#x60;. | | no_issues | No known issues that would affect travel over the specified services and/or stops. May still populate &#x60;title&#x60; and &#x60;description&#x60;. | | travel_affected | Travel over the specified services and/or stops may be delayed or otherwise affected. | | travel_prevented | Travel over the specified services and/or stops may not be possible. |  | 
**title** | **str** | A relatively short title for the Status. | [optional] 
**description** | **str** | An in-depth description of the Status. This will be provided as plain text. | [optional] 
**service_ids** | **list[str]** | If this Status relates to Services rather than Stops, this will contain the &#x60;id&#x60; of one or more Services. The ability to specify multiple services is intended to prevent needless duplication of Status reporting.  | [optional] 
**stop_ids** | **list[str]** | If this Status relates to specific stops (as opposed to Services, or sections of Services running between specific stops), this will contain the &#x60;id&#x60; of one or more relevant Stops.  Example: A Status might use this to identify specific metro Stops where riders can&#x27;t board or alight because they&#x27;re closed, even though trains are passing through them.  | [optional] 
**service_stop_ranges** | [**list[StatusServiceStopRanges]**](StatusServiceStopRanges.md) | If this Status relates to sections of Services between different Stops, this will indicate which sections, in combination with &#x60;service_ids&#x60;. This field relates to services traveling between Stops, rather than whether or not the Stops are open or closed (which is represented by &#x60;stop_ids&#x60;).  Example: A Status might use this to indicate that a particular train isn&#x27;t running between a set of Stops, even if those Stops remain open for other services.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

