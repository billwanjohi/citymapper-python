# HireVehicleStationMetadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The public name of the station for display to the user. | [optional] 
**service_id** | **str** | Indicates which Service in the Leg the vehicles contained in this dock belongs to, in order to indicate Service  and Brand naming and imagery. This is redundant in single-Service Legs, but it&#x27;s essential in Legs that have alternate equivalent services.  | [optional] 
**num_vehicles_available** | **int** | The number of vehicles at this station currently available for rental.  | [optional] 
**num_docks_available** | **int** | The number of functional docks available that are able to accept vehicles for return. This field will not be present for stations with unlimited docking capacity.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

