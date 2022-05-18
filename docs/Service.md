# Service

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier for the service | 
**name** | **str** | A string that can be displayed to the user to describe this service | 
**vehicle_types** | [**list[VehicleType]**](VehicleType.md) | This is a priority list of vehicle types that can be used to describe the vehicle used by this Service. The list is ordered from more specific to less specific vehicle type, to allow for refinements to the list of types to be added over time, and to allow consumers of the API to  make more generic distinctions if desired.  | [optional] 
**brand** | **AllOfServiceBrand** | Provides the branding attached to the service. The main purpose of Brand is to determine which specific imagery to show for the service, particularly in the case where the Service doesn&#x27;t have distinct &#x60;images&#x60; of its own.  | [optional] 
**images** | [**list[ServiceImage]**](ServiceImage.md) | A list of &#x60;Image&#x60;s that can be used to represent this &#x60;Service&#x60; in a user interface. API consumers should use the first &#x60;Image&#x60; in the list that meets their criteria.  Images given here will have a &#x60;ui_role&#x60; of &#x60;service&#x60;, as they are identifying the specific &#x60;Service&#x60; rather than the general &#x60;Brand&#x60;. If no suitable &#x60;Image&#x60; is provided here, one of the images in the adjacent &#x60;brand&#x60; should be used.  | [optional] 
**color** | **str** | The basic color associated with this service, for graphical uses such as map lines.  The color is encoded as a capitalized hexadecimal RGB value starting with &#x60;#&#x60;. For instance, &#x60;#2850AD&#x60; encodes the 24-bit RGB value of (40, 80, 173).  | [optional] 
**background_color** | **str** | A background color for use with this service, in cases where text will be shown on a colored background. Used in conjunction with &#x60;text_color&#x60;.  The color is encoded as a capitalized hexadecimal RGB value starting with &#x60;#&#x60;. For instance, &#x60;#2850AD&#x60; encodes the 24-bit RGB value of (40, 80, 173).  | [optional] 
**text_color** | **str** | A text color for use with this service, in cases where text will be shown on a colored background. Used in conjunction with &#x60;background_color&#x60;. If omitted, it means that white (&#x60;#FFFFFF&#x60;) has sufficient contrast against the given &#x60;background_color&#x60; or &#x60;color&#x60; values.  The color is encoded as a capitalized hexadecimal RGB value starting with &#x60;#&#x60;. For instance, &#x60;#2850AD&#x60; encodes the 24-bit RGB value of (40, 80, 173).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

