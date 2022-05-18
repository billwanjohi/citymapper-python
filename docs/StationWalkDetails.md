# StationWalkDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommended_exit** | **AllOfStationWalkDetailsRecommendedExit** | Provides information about the station entrance/exit that the rider passes through as part of this walk.  | [optional] 
**alternate_exits** | [**list[StationExit]**](StationExit.md) | Provides information about the other station entrances/exits for contextual display.  | [optional] 
**duration_seconds** | **int** | Indicates how much of the walking time in this Leg occurs inside of the station between the recommended entrance/exit and the platform.  When omitted, this indicates that no information about the duration of the in-station portion of the walk is available.  To determine the amount of walking time that occurs outside of the station, subtract this value from the Leg&#x27;s overall &#x60;duration_seconds&#x60;. (The value is encoded this way so that API consumers that don&#x27;t want to display this level of detail can simply display the Leg&#x27;s &#x60;duration_seconds&#x60;.)  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

