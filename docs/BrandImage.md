# BrandImage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ui_role** | **str** |  | [optional] 
**is_generic** | **bool** | If &#x60;true&#x60;, this indicates that this is a generic image entirely based on the vehicle type, rather than being customized for the specific brand or service. When a specific branded image of the same &#x60;ui_role&#x60; is available, it will be provided earlier in the list of images.  | [optional] [default to False]
**has_space_for_text** | **bool** | If &#x60;true&#x60;, this image contains a designated area for overlaying extra textual elements such as \&quot;stop indicator\&quot; letters. (Some regions have 2-4 letter codes on bus stop poles to distinguish between nearby stops.) The specific renderable area will depend on the &#x60;ui_role&#x60;.  When this is &#x60;true&#x60;, there will generally also be a peer &#x60;Image&#x60; without space for text, for the more common case where no text rendering is needed. This alternate &#x60;Image&#x60; will appear earlier in the list of &#x60;Image&#x60;s.  | [optional] [default to False]
**is_dropoff_place** | **bool** | Applies to &#x60;BrandImage&#x60;s with &#x60;ui_role&#x60; of &#x60;pin&#x60; or &#x60;station&#x60; if Brand offers hire vehicles.  If &#x60;true&#x60;, then this image represents a drop-off place for hire vehicles, for example a docking station for cycles or a parking area for e-scooters.  An image representing drop-off place (&#x60;is_dropoff_place&#x60; set to &#x60;true&#x60;) will always be accompanied by an image representing pick-up place (&#x60;is_dropoff_place&#x60; set to &#x60;false&#x60;) provided earlier in the list of images.  | [optional] [default to False]
**low_capacity** | **bool** | Applies to &#x60;BrandImage&#x60;s with &#x60;ui_role&#x60; of &#x60;pin&#x60; or &#x60;station&#x60; if Brand offers hire vehicles.  If &#x60;true&#x60;, then this image represents a low capacity variant of pick-up or drop-off place for hire vehicles.  Low capacity variant will always be accompanied by high capacity variant provided earlier in the list of images.  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

