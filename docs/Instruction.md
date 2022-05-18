# Instruction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path_index** | **int** | 0-based index into the list of coordinates provided by the &#x60;path&#x60; property of the Leg. This indicates the location at which the instruction is to be followed, so it will be the location of the turn on the path, or the start or end of the Leg.  | 
**distance_meters** | **int** | The distance in meters of the section of the &#x60;path&#x60; **prior to** this instruction. This property will be omitted for initial instructions of type &#x60;depart&#x60;.  | [optional] 
**time_seconds** | **int** | The time in seconds that the user is expected to take to traverse the section of the &#x60;path&#x60; **prior to** this instruction. This property will be omitted for initial instructions of type &#x60;depart&#x60;.  | [optional] 
**description_text** | **str** | Plain-text description of the Instruction to the user.  | [optional] 
**description_format** | **str** | Text format for rendering the Instruction with emphasized elements, where &#x60;{key}&#x60; indicates a part of the string that must be replaced with content defined by the entry corresponding to &#x60;key&#x60; in &#x60;description_format_replacements&#x60;.  This allows the elements described by the replacements to be formatted differently by the client, if desired.  Key strings will contain only the characters &#x60;[a-zA-Z0-9]&#x60;.  &#x60;{ }&#x60; will not be nested, and the literal characters &#x60;{&#x60; and &#x60;}&#x60; are encoded by the escape sequences &#x60;\\{&#x60; and &#x60;\\}&#x60;, respectively.  | [optional] 
**description_format_replacements** | [**list[InstructionDescriptionFormatReplacements]**](InstructionDescriptionFormatReplacements.md) |  | [optional] 
**type** | **str** | Indicates the type of Instruction.  **NOTE: New values may be added to this list at any time.**  | [optional] 
**type_direction** | **str** | Indicates a direction that modifies this Instruction.  **NOTE: New values may be added to this list at any time.**  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

