# Leg

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**travel_mode** | **str** | Identifies the kind of travel described by this leg. New options are likely to be added over time. This value indicates which other fields are likely to be populated in the Leg.  | value | description | | ----- | ----------- | | walk | Walking | | transit | Public transportation with fixed routes &amp; stops such as bus, metro, train, ferry | | self_piloted | Vehicles such as e-scooters, bicycles, motor scooters, private automobiles that the user pilots themselves | | on_demand | Services such as rideshare, cab, demand-responsive transit services where the path, pickup and dropoff points are determined by the user rather than fully pre-determined |  | 
**duration_seconds** | **int** | The time required to traverse this leg, excluding any waiting or boarding time at the beginning. May be omitted in rare circumstances when the duration cannot be computed. | [optional] 
**path** | **str** | The geographic path that the leg traverses, as a series of WGS84 coordinates encoded in [Google Polyline Format](https://developers.google.com/maps/documentation/utilities/polylinealgorithm), with a decimal precision of 5 digits.  For example, the value &#x60;_flyHbjPDZBTBNDJ&#x60; encodes the following series of (latitude, longitude) coordinates: &#x60;&#x60;&#x60; [(51.51344, -0.08882),  (51.51341, -0.08896),  (51.51339, -0.08907),  (51.51337, -0.08915),  (51.51334, -0.08921)] &#x60;&#x60;&#x60;  | 
**instructions** | [**list[Instruction]**](Instruction.md) | (May be included when &#x60;travel_mode&#x60; is &#x60;walk&#x60; or &#x60;self_piloted&#x60;.)  This provides the list of turn instructions to guide the user through Legs where the user needs to navigate, such as when walking or using a scooter or bike.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

