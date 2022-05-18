# LegUpdatableDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**departures** | [**list[Departure]**](Departure.md) | An array of Departure objects, giving alternate departures for the services in the Legs in which this property appears. The array can contain a mixture of different Departure &#x60;type&#x60;s—for example, it&#x27;s common to receive &#x60;live&#x60; information for the next few departures, followed by &#x60;scheduled&#x60; information. For legs with multiple alternate Services, this array is likely to contain a mixture of departures corresponding to the different alternate services.  The number of Departures returned will depend on the availability of information.  | [optional] 
**live_departure_availability** | **str** | This indicates the availability of live departure information for the Services used in this Leg. Live departure information is not available for all transit services, and some transit services have live information that cannot be determined quickly enough to be included in all requests. The value of this property characterizes the contents of the &#x60;departures&#x60; array in this Leg Updatable Detail, and indicates whether an additional request is likely to yield additional live times for this Leg.  | value | description | | ----- | ----------- | | unknown | The availability of live departure information can&#x27;t be determined | | none_available | No live departure information is available for the services used in this leg. Typically the &#x60;departures&#x60; list will contain entries of type &#x60;scheduled&#x60; or &#x60;frequency&#x60; in this case | | included | Live departure information is available for the services in this Leg, and it is included in the &#x60;departures&#x60; list | | additional_request | Live information is available for the services in this Leg, but some of it will require an additional &#x60;/api/1/live/routeupdate&#x60; request to retrieve |  | [optional] 
**statuses** | [**list[Status]**](Status.md) | An array of Status objects that relate to this Leg.  | [optional] 
**leg_departure_time** | **str** | The time at which Citymapper thinks the user will set out on this leg, given available departure information. In the case of Legs of &#x60;travel_type&#x60; &#x60;transit&#x60;, this excludes waiting time.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone in which the event occurs. For example, &#x60;2020-08-19T08:10:42-04:00&#x60; expresses August 19, 2020 at 8:10am in Eastern Daylight Time.  | [optional] 
**leg_arrival_time** | **str** | The time at which Citymapper thinks the user will arrive at the end of this leg, given available departure information and expected travel speed.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone in which the event occurs. For example, &#x60;2020-08-19T08:10:42-04:00&#x60; expresses August 19, 2020 at 8:10am in Eastern Daylight Time.  | [optional] 
**vehicle_pickup_places** | [**list[HireVehicleLegPickup]**](HireVehicleLegPickup.md) | Included in a &#x60;self_piloted&#x60; leg which involves a hire vehicle. Indicates the locations where the user can pick up a vehicle used to complete the leg. The listed places are the ones determined to be the \&quot;best\&quot; places to pick up a vehicle - they might not always be the closest by crow-flies distance.  The item in the list marked with &#x60;\&quot;suggested\&quot;: true&#x60; is the one that corresponds to the rest of the data in this leg (and any preceeding walk leg). To support situations where new vehicles come available, and  extensions to this API where the user can change the selected vehicle while keeping the order stable,  the suggested location may not necessarily be at the top of the list.  One of &#x60;hire_vehicle&#x60; or &#x60;hire_vehicle_station&#x60; will be populated for each item in the list.  | [optional] 
**vehicle_dropoff_places** | [**list[HireVehicleStationLegDropoff]**](HireVehicleStationLegDropoff.md) | May be included in a &#x60;self_piloted&#x60; leg which involves a hire vehicle. Indicates the locations where can drop off the vehicle used to complete the leg. The listed places are the ones determined to be the \&quot;best\&quot; places to drop the vehicle off - they might not always be the ones closest to the eventual  destination by crow-flies distance.  The item in the list marked with &#x60;\&quot;suggested\&quot;: true&#x60; is the one that corresponds to the rest of the data in this leg (and any subsequent walk leg). To support extensions to this API where the user can change the selected vehicle while keeping the order stable, the suggested location may not necessarily be at the top of the list.  If this drop-off location is at a vehicle docking station, the &#x60;hire_vehicle_station&#x60; property will be included with metadata about the station. Otherwise, the parking location represents either a marked area on the road or  sidewalk/pavement where vehicles of this type can be left, or simply a place within the allowed parking zone  close to the destination of this part of the Route.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
