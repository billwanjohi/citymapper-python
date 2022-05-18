# InstructionDescriptionFormatReplacements

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A key corresponding to a string enclosed in &#x60;{}&#x60; in &#x60;description_format&#x60;.  | 
**text** | **str** | The text to be used to replace the &#x60;{key}&#x60; substring in the &#x60;description_format&#x60;.  | 
**type** | **str** | A value indicating what kind of real-world thing is being identified by this format replacement. This allows API clients to apply application-specific formatting if desired.  | value | description | | ----- | ----------- | | street_name | The name of a street, road, or other way | | exit_number | The number of an exit, generally from a roundabout |  **NOTE: New values may be added to this list at any time.**  | [optional] 
**language** | **str** | An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates what language the associated &#x60;text&#x60; is in. Note that this can be different from the language of the surrounding description - this is most common when the replacement is a place-name in a local language whilst the description is in a different language.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

