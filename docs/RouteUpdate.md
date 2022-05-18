# RouteUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leg_updates** | [**list[LegUpdatableDetail]**](LegUpdatableDetail.md) | This is an parallel array of Leg Updatable Detail objects, one for every Leg in the original Route being updated. The ones corresponding to walking Legs will be empty, but the details corresponding to transit legs will contain updated departure information.  | 
**route_departure_time** | **str** | The time at which Citymapper thinks the user will set out on this route, given available departure information. This is computed assuming that user is at the start of the route at the time of the request.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone in which the event occurs. For example, &#x60;2020-08-19T08:10:42-04:00&#x60; expresses August 19, 2020 at 8:10am in Eastern Daylight Time.  | [optional] 
**route_arrival_time** | **str** | The time at which Citymapper thinks the user will arrive at the end of this route, given available departure information and expected travel speed. This is computed assuming that user is at the start of the route at the time of the request.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone in which the event occurs. For example, &#x60;2020-08-19T08:10:42-04:00&#x60; expresses August 19, 2020 at 8:10am in Eastern Daylight Time.  | [optional] 
**route_duration_seconds** | **int** | The overall estimated time to traverse the entire route, in seconds.  This value replaces the &#x60;duration_seconds&#x60; value from the original Route, as it will be recomputed to use the specific departure information contained in this Route update response.  May be omitted in rare circumstances when the duration cannot be computed, for instance if the Route can&#x27;t be completed at the given time because the Services involved are not running.  | [optional] 
**route_duration_accuracy** | [**DurationAccuracy**](DurationAccuracy.md) |  | [optional] 
**request_signature** | **str** | This is a Route &#x60;signature&#x60; from the update request, which should be used to associate this update with the correct Route.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

