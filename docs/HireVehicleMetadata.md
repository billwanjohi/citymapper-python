# HireVehicleMetadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The public name of this vehicle, if applicable, for display to the user. | [optional] 
**service_id** | **str** | Indicates which Service in the Leg this Vehicle belongs to, in order to indicate Service and Brand naming and imagery. This is redundant in single-Service Legs, but it&#x27;s essential in Legs that have alternate equivalent services.  | 
**propulsion_type** | **str** | The type of fuel this vehicle uses for propulsion (if any). Note, it is possible that additional values will be added to this list in future. If this field is not present, the vehicle has no internal propulsion source (i.e. it is purely human-powered).  | value | description | | ----- | ----------------- | | electric | Powered by battery-powered electric motor - either entirely using a throttle, or as assistance to human power | | combustion | Powered by gasoline combustion engine |  | [optional] 
**current_range_meters** | **int** | The estimated range this vehicle can travel with its remaining power or fuel, if applicable. | [optional] 
**current_fuel_percent** | **float** | This vehicle&#x27;s remaining power or fuel, expressed as a value between 0 and 1. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

