# StationExit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifies this station exit. This is an internal identifier and must not be shown to the rider.  | 
**stop_id** | **str** | Identifies the station that this exit gives access to. When used in a walk Leg, this value will match a Stop &#x60;id&#x60; value in an adjoining transit Leg. This is an internal identifier and must not be shown to the rider.  | 
**coordinates** | **AllOfStationExitCoordinates** | The geographical location of this exit.  | 
**name** | **str** | A rider-facing longer descriptive name for this exit. Depending on the station signage, an exit may have any combination of &#x60;name&#x60; and &#x60;short_name&#x60; (or neither).  | [optional] 
**short_name** | **str** | A rider-facing short code identifying this exit, usually a few numbers and/or letters. Depending on the station signage, an exit may have any combination of &#x60;name&#x60; and &#x60;short_name&#x60; (or neither).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

