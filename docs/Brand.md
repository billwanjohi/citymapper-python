# Brand

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier for this Brand | 
**name** | **str** | The name of Brand | 
**images** | [**list[BrandImage]**](BrandImage.md) | A list of &#x60;Image&#x60;s that can be used to represent this &#x60;Brand&#x60; in a user interface. API consumers should use the first &#x60;Image&#x60; in the list that meets their criteria.  Images in this list may have any of the following values for &#x60;ui_role&#x60;:  | value | description | | ----- | ----------- | | pin | A pushpin-styled icon to display the location of a station, a stop or a dock with vehicles for hire on a map | | station | An icon to display beside the name of a station, stop or vehicle hire dock | | vehicle | An icon that depicts the mode of travel for use in directions | | vehicle_compact | A compact icon to be displayed before the &#x60;name&#x60; of a &#x60;Service&#x60; to indicate the vehicle type | | pin_vehicle | A pushpin-styled icon to display a free floating hire vehicle (for example bicycles or e-scooters) on a map |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

