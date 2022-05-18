# Image

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL from which this &#x60;Image&#x60; can be retrieved. The image will be encoded in PNG format unless the &#x60;format&#x60; field indicates otherwise.  | 
**ui_role** | **str** | Indicates the role that this image plays in a user interface. New values may be added at any time. See the parent object in the response for valid values in this context.  | 
**width** | **float** | The width of the image in screen units. This corresponds to &#x60;px&#x60; in CSS, \&quot;points\&quot; on iOS, and \&quot;density-independent pixels\&quot; on Android.  | [optional] 
**height** | **float** | The height of the image in screen units. This corresponds to &#x60;px&#x60; in CSS, \&quot;points\&quot; on iOS, and \&quot;density-independent pixels\&quot; on Android.  | [optional] 
**pixel_ratio** | **float** | Indicates the ratio of image pixels to screen units. When not provided, &#x60;2&#x60; should be assumed. For instance, an &#x60;Image&#x60; with a &#x60;width&#x60; of &#x60;38&#x60;, &#x60;height&#x60; of &#x60;41&#x60;, and &#x60;pixel_ratio&#x60; of &#x60;2&#x60; has image pixel dimensions of 76 x 82.  | [optional] [default to 2]
**format** | **str** | Indicates the file format of the image. The default value is &#x60;png&#x60;, indicating Portable Network Graphics bitmap format. At time of writing, all &#x60;Images&#x60; returned are in &#x60;png&#x60; format, and therefore this field will usually be omitted. However, in the future, additional &#x60;format&#x60; types may be provided in responses.  | [optional] [default to 'png']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

