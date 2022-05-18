# Route

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | [**Waypoint**](Waypoint.md) |  | 
**end** | [**Waypoint**](Waypoint.md) |  | 
**distance_meters** | **int** | The overall distance of the entire Route, in meters. | [optional] 
**duration_seconds** | **int** | The overall estimated time to traverse the entire Route, in seconds, based on the selected vehicle or departure in the response. | [optional] 
**duration_accuracy** | [**DurationAccuracy**](DurationAccuracy.md) |  | [optional] 
**price** | **AllOfRoutePrice** | The price to take the Route. Omitted when not available. Generally available only on transit Routes. The price is computed assuming no special passes, with the user paying with cash or the most common fare instrument. | [optional] 
**legs** | [**list[Leg]**](Leg.md) | Array of Legs comprising the Route, in the order in which they should be traversed. Every valid Route will have at least one. | 
**route_departure_time** | **str** | The time at which Citymapper thinks the user will set out on this route, given available departure information. This is computed assuming that user is at the start of the route.  Updated values for &#x60;route_departure_time&#x60; and &#x60;route_arrival_time&#x60; are returned by &#x60;/api/1/live/routeupdates&#x60; to reflect any updated departure information.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone in which the event occurs. For example, &#x60;2020-08-19T08:10:42-04:00&#x60; expresses August 19, 2020 at 8:10am in Eastern Daylight Time.  | [optional] 
**route_arrival_time** | **str** | The time at which Citymapper thinks the user will arrive at the end of this route, given available departure information and expected travel speed. This is computed assuming that user is at the start of the route.  Updated values for &#x60;route_departure_time&#x60; and &#x60;route_arrival_time&#x60; are returned by &#x60;/api/1/live/routeupdates&#x60; to reflect any updated departure information.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone in which the event occurs. For example, &#x60;2020-08-19T08:10:42-04:00&#x60; expresses August 19, 2020 at 8:10am in Eastern Daylight Time.  | [optional] 
**route_metadata** | [**RouteMetadata**](RouteMetadata.md) |  | [optional] 
**profile** | **str** | Indicates which routing \&quot;profile\&quot; was used to calculate this Route. For example, a response from a bike routing endpoint may return multiple routes, one with a &#x60;quiet&#x60; profile and another with a &#x60;fast&#x60; profile.  Note that new values can be added at any time, so any code parsing this field must be able to handle unexpected values.  This value will match the &#x60;profiles&#x60; request parameter on endpoints that support selecting specific routing profiles.  This value is intended to be machine readable only. For a profile name to show to a user, use the &#x60;profile_name&#x60; in the &#x60;route_metadata&#x60; object instead.  | [optional] 
**signature** | **str** | A value to be passed back to the server in subsequent calls to refer to this Route (for instance, when requesting live departure information via &#x60;/api/1/live/routeupdates&#x60;). It must be treated as an opaque value. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

