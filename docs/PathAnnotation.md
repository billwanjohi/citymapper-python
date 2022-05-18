# PathAnnotation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_index** | **int** | The start index of the coordinate range, as a 0-based index into the list of coordinates encoded by the &#x60;path&#x60; of a Leg.  | 
**end_index** | **int** | The end index of the coordinate range, as a 0-based index into the list of coordinates encoded by the &#x60;path&#x60; of a Leg. &#x60;end_index&#x60; must be greater than or equal to &#x60;start_index&#x60;. If &#x60;end_index&#x60; &#x3D; &#x60;start_index&#x60;, this refers to a single coordinate in the path.  | 
**should_walk** | **bool** | If present and &#x60;true&#x60;, this Path Annotation refers to a section of the path where the user should dismount and walk alongside their vehicle. This only relevant in the case of Legs where &#x60;travel_mode&#x60; is &#x60;self_piloted&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

