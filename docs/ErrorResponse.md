# ErrorResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A developer-readable message explaining the problem. Must not be displayed to the end user. | [optional] 
**error_code** | **str** | A string code that can be used for triggering error handling code paths. Only present in responses with non-200 HTTP code. Note new values may be added at any time.  | value | description | | ----- | ----------- | | no-results | The request was in Citymapper&#x27;s coverage regions, but no results were found. | | coverage-region | The request is outside of Citymapper&#x27;s coverage regions, or spans disconnected regions. | | coverage-start | The request&#x27;s &#x60;start&#x60; location falls outside of Citymapper&#x27;s coverage regions. | | coverage-end | The request&#x27;s &#x60;end&#x60; location falls outside of Citymapper&#x27;s coverage regions. | | coverage-distance | The request&#x27;s &#x60;start&#x60; and &#x60;end&#x60; locations are further apart than the maximum allowed for this API. | | signature | A signature included in the request is invalid for use with this API. | | unknown-brand | The request references an unknown Brand ID. | | unknown-scenario | The request references an unknown Scenario ID. | | request-format | The request was semantically malformed. The &#x60;message&#x60; field may contain additional details. | | deprecated | The request was made to a deprecated API. |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

