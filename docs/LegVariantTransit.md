# LegVariantTransit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stops** | [**list[Stop]**](Stop.md) | (Included when &#x60;travel_mode&#x60; is transit.)  This provides the list of stops traversed in a transit Leg, each with a name and coordinates. Note that the coordinates may not be exactly on the &#x60;path&#x60;.  | [optional] 
**direction_description** | **str** | Optional user-facing hint for guidance inside a station or when approaching a stop. In the case of a station, this will usually attempt to match in-station signage. This will not refer to short platform identifiers; when departures leave from platforms with short identifiers then &#x60;platform_short_name&#x60; in the departure object will instead/additionally be populated. | [optional] 
**updatable_detail** | [**LegUpdatableDetail**](LegUpdatableDetail.md) |  | [optional] 
**best_boarding_sections** | [**LegVariantTransitBestBoardingSections**](LegVariantTransitBestBoardingSections.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

