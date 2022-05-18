# LegVariantWalk

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**station_walk_type** | **str** | If provided, indicates which parts of a walk are inside of a station.  | value | description | | ----- | ----------- | | outside_station | This walking leg has no relationship to a transit station, so no &#x60;walk_details_*&#x60; fields are provided. This is the default when this field is omitted. | | enter_station | This walking leg ends by entering a station and walking to the platform, &#x60;walk_details_enter_station&#x60; is provided | | change_platform | This walking leg takes place entirely between two platforms in one station, no &#x60;walk_details_*&#x60; fields are provided. | | exit_station | This walking leg starts by exiting a station, &#x60;walk_details_exit_station&#x60; is provided | | walk_between_stations | This walking leg involves exiting a station and entering another nearby station; both &#x60;walk_details_exit_station&#x60; and &#x60;walk_details_enter_station&#x60; are provided |  This field is only provided when &#x60;travel_mode&#x60; is &#x60;walk&#x60;.  | [optional] [default to 'outside_station']
**walk_details_enter_station** | **object** | When a walk Leg ends by entering a transit station, this can provide information on which entrance the rider should use, and how much of the Leg&#x27;s walk duration takes place between the entrance and the platform.  This field is relevant for &#x60;station_walk_type&#x60; of &#x60;enter_station&#x60; and &#x60;walk_between_stations&#x60;.  | [optional] 
**walk_details_exit_station** | **object** | When a walk Leg begins by exiting a transit station, this can provide information on which exit the rider should use, and how much of the Leg&#x27;s walk duration takes place between the platform and the exit.  This field is relevant for &#x60;station_walk_type&#x60; of &#x60;exit_station&#x60; and &#x60;walk_between_stations&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

