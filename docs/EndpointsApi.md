# swagger_client.EndpointsApi

All URIs are relative to *https://api.external.citymapper.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bikedirections**](EndpointsApi.md#bikedirections) | **GET** /api/1/directions/bike | Bike directions between two points (hire vehicles)
[**bikeridedirections**](EndpointsApi.md#bikeridedirections) | **GET** /api/1/directions/bikeride | Bike directions between two points (ride only)
[**liverouteupdates**](EndpointsApi.md#liverouteupdates) | **POST** /api/1/live/routeupdates | Live departure and availability information for multiple Routes at once
[**motorscooterdirections**](EndpointsApi.md#motorscooterdirections) | **GET** /api/1/directions/motorscooter | Motor scooter directions between two points (hire vehicles)
[**motorscooterridedirections**](EndpointsApi.md#motorscooterridedirections) | **GET** /api/1/directions/motorscooterride | Motor scooter directions between two points (ride only)
[**scenariodirections**](EndpointsApi.md#scenariodirections) | **GET** /api/1/directions/scenario | Scenario based directions between two points
[**scooterdirections**](EndpointsApi.md#scooterdirections) | **GET** /api/1/directions/scooter | E-scooter directions between two points (hire vehicles)
[**scooterridedirections**](EndpointsApi.md#scooterridedirections) | **GET** /api/1/directions/scooterride | E-scooter directions between two points (ride only)
[**transitdirections**](EndpointsApi.md#transitdirections) | **GET** /api/1/directions/transit | Transit directions between two points
[**traveltime**](EndpointsApi.md#traveltime) | **GET** /api/1/traveltimes | Travel times between two locations
[**walkdirections**](EndpointsApi.md#walkdirections) | **GET** /api/1/directions/walk | Walking directions between two points

# **bikedirections**
> DirectionsResponse bikedirections(start, end, brand_id, ride_state=ride_state, current_location=current_location, ride_start_location=ride_start_location, ride_end_location=ride_end_location, profiles=profiles, language=language, reroute_signature=reroute_signature, start_bearing=start_bearing)

Bike directions between two points (hire vehicles)

**NOTE this API is not available through open access, please contact sales**. Please contact Citymapper using the details provided at the top of the page for information on integrating and using this API.  Gets an bike route between two points, including any initial and final walks. The resulting Route provides enough information to render it on a map, along with a duration estimate.  This call can be used in several different ways:    **Use any bike of the specified Brand**  This is the simplest call, only requiring `start`, `end`, and `brand_id`. Citymapper assumes that the user is at the `start` point, and chooses a bike of the specified Brand, if possible.  **Use a bike at a specified location**  By adding `original_vehicle_location` to `start`, `end`, and `brand_id`, Citymapper plans a Route that assumes the bike is at the given location.  **Update a Route in progress**  In order to retrieve an updated Route that includes rerouting from the user's current location if they've diverged from the planned Route, the caller can add the `current_location` and `ride_state` properties, which indicates which Leg of the resulting Route should be rerouted around the user's `current_location`.  Successful responses (HTTP code `200`) will consume one \"Bike Route\" credit (or one \"Bike Reroute\" credit if `reroute_signature` is used) for each HTTP response. Unsuccessful calls will not consume any credits. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
configuration = swagger_client.Configuration()
configuration.api_key['Citymapper-Partner-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Citymapper-Partner-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
start = [3.4] # list[float] | The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used.
end = [3.4] # list[float] | The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used.
brand_id = 'brand_id_example' # str | The ID of the Brand of bike to use for this route. This is necessary in order to determine the location of available bikes, along with any associated coverage and parking restrictions. 
ride_state = 'ride_state_example' # str | Indicates where along the Route the user is. If omitted, `walking_to_vehicle` is used. This property along with `current_location` allows the retrieval of an updated Route that reflects the user's current progress through it.  | value | description | | ----- | ----------- | | walking_to_vehicle | Indicates that the user is walking to collect the vehicle | | riding | Indicates that the user is riding the vehicle | | walking_to_end | Indicates that the user has left the vehicle and is walking to their destination |  (optional)
current_location = 'current_location_example' # str | The user's current location, in order to update the Route based on the user's location. Provided in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  This parameter is used to get an updated Route that reflects the user's actual location if they diverge from the path given in the Route.  If this is provided, the returned Route will contain this location. Which Leg of the Route will contain this location is decided by the value of the `ride_state` parameter.  (optional)
ride_start_location = 'ride_start_location_example' # str | The location of the vehicle to be used, at the beginning of the vehicle ride part of the user's trip along the Route. Provided in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  This must be provided when `ride_state` is `riding` or `walking_to_end`. If not provided when `ride_state` is `walking_to_vehicle` (or not specified), Citymapper will attempt to find the most appropriate vehicle that belongs to the specified `brand_id`.  For compatibility, `original_vehicle_location` is an alias for this parameter  (optional)
ride_end_location = 'ride_end_location_example' # str | The location the vehicle was dropped off at the end of the vehicle ride part of the user's trip along the Route. Provided in WGS84 'latitude,longitude' format. Coordinates should  be in decimal, and only the first 6 digits of precision will be used.  This must be provided when `ride_state` is `walking_to_end`. In all other states this parameter is ignored.  (optional)
profiles = 'profiles_example' # str | Indicates which \"profiles\" to use when calculating bike directions. Each profile can generate a different Route option, so requesting more profiles will generally give more options. Note that sometimes some of the resulting Routes will be identical (in the case of one route being optimal in more than one way), and a profile may not always yield a Route.  | value | description | | ----- | ----------- | | quiet | Attempts to use roads with less traffic | | regular | The default profile, balances traffic with directness | | fast | Attempts to find the shortest sensible Route |  If no profiles are specified, `regular` will be used.  (optional)
language = 'language_example' # str | An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language.  (optional)
reroute_signature = 'reroute_signature_example' # str | When rerouting (requesting an update to a previous response that accounts for the user's updated location), this value should be set to the `signature` provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the `current_location` (when applicable) or `start` location should be set to the user's latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the `end` location is different, or if more than 1 hour has passed since the original request.  (optional)
start_bearing = 56 # int | An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route.  (optional)

try:
    # Bike directions between two points (hire vehicles)
    api_response = api_instance.bikedirections(start, end, brand_id, ride_state=ride_state, current_location=current_location, ride_start_location=ride_start_location, ride_end_location=ride_end_location, profiles=profiles, language=language, reroute_signature=reroute_signature, start_bearing=start_bearing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->bikedirections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | [**list[float]**](float.md)| The geographical start of the route, in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 decimal places will be used. | 
 **end** | [**list[float]**](float.md)| The geographical end of the route, in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 decimal places will be used. | 
 **brand_id** | **str**| The ID of the Brand of bike to use for this route. This is necessary in order to determine the location of available bikes, along with any associated coverage and parking restrictions.  | 
 **ride_state** | **str**| Indicates where along the Route the user is. If omitted, &#x60;walking_to_vehicle&#x60; is used. This property along with &#x60;current_location&#x60; allows the retrieval of an updated Route that reflects the user&#x27;s current progress through it.  | value | description | | ----- | ----------- | | walking_to_vehicle | Indicates that the user is walking to collect the vehicle | | riding | Indicates that the user is riding the vehicle | | walking_to_end | Indicates that the user has left the vehicle and is walking to their destination |  | [optional] 
 **current_location** | **str**| The user&#x27;s current location, in order to update the Route based on the user&#x27;s location. Provided in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  This parameter is used to get an updated Route that reflects the user&#x27;s actual location if they diverge from the path given in the Route.  If this is provided, the returned Route will contain this location. Which Leg of the Route will contain this location is decided by the value of the &#x60;ride_state&#x60; parameter.  | [optional] 
 **ride_start_location** | **str**| The location of the vehicle to be used, at the beginning of the vehicle ride part of the user&#x27;s trip along the Route. Provided in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  This must be provided when &#x60;ride_state&#x60; is &#x60;riding&#x60; or &#x60;walking_to_end&#x60;. If not provided when &#x60;ride_state&#x60; is &#x60;walking_to_vehicle&#x60; (or not specified), Citymapper will attempt to find the most appropriate vehicle that belongs to the specified &#x60;brand_id&#x60;.  For compatibility, &#x60;original_vehicle_location&#x60; is an alias for this parameter  | [optional] 
 **ride_end_location** | **str**| The location the vehicle was dropped off at the end of the vehicle ride part of the user&#x27;s trip along the Route. Provided in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should  be in decimal, and only the first 6 digits of precision will be used.  This must be provided when &#x60;ride_state&#x60; is &#x60;walking_to_end&#x60;. In all other states this parameter is ignored.  | [optional] 
 **profiles** | **str**| Indicates which \&quot;profiles\&quot; to use when calculating bike directions. Each profile can generate a different Route option, so requesting more profiles will generally give more options. Note that sometimes some of the resulting Routes will be identical (in the case of one route being optimal in more than one way), and a profile may not always yield a Route.  | value | description | | ----- | ----------- | | quiet | Attempts to use roads with less traffic | | regular | The default profile, balances traffic with directness | | fast | Attempts to find the shortest sensible Route |  If no profiles are specified, &#x60;regular&#x60; will be used.  | [optional] 
 **language** | **str**| An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user&#x27;s language preference.    When provided, the response will contain a &#x60;language&#x60; property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn&#x27;t expressed in the request (this will generally be &#x60;en-US&#x60; as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language.  | [optional] 
 **reroute_signature** | **str**| When rerouting (requesting an update to a previous response that accounts for the user&#x27;s updated location), this value should be set to the &#x60;signature&#x60; provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the &#x60;current_location&#x60; (when applicable) or &#x60;start&#x60; location should be set to the user&#x27;s latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the &#x60;end&#x60; location is different, or if more than 1 hour has passed since the original request.  | [optional] 
 **start_bearing** | **int**| An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route.  | [optional] 

### Return type

[**DirectionsResponse**](DirectionsResponse.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bikeridedirections**
> DirectionsResponse bikeridedirections(start, end, profiles=profiles, language=language, reroute_signature=reroute_signature, start_bearing=start_bearing)

Bike directions between two points (ride only)

Gets a bike route between two points, providing enough information to render it on a map, along with a duration estimate.  This call assumes that the rider has a bicycle at the `start` point, and provides a biking route from there to the `end` point if both are within Citymapper's supported areas. The resulting route should contain a single bike leg, though the `path_annotations` property of the Leg may indicate sections during which the user should walk beside the bike.  This call does not incorporate any information about bike operators' coverage or parking areas, but other API calls may be available to do so.  The maximum great-circle distance between the start and end is limited to 200km for this API.  Successful responses (HTTP code `200`) will consume one \"Bike Route\" credit (or one \"Bike Reroute\" credit if `reroute_signature` is used) for each HTTP response. Unsuccessful calls will not consume any credits. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
configuration = swagger_client.Configuration()
configuration.api_key['Citymapper-Partner-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Citymapper-Partner-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
start = [3.4] # list[float] | The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used.
end = [3.4] # list[float] | The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used.
profiles = 'profiles_example' # str | Indicates which \"profiles\" to use when calculating bike directions. Each profile can generate a different Route option, so requesting more profiles will generally give more options. Note that sometimes some of the resulting Routes will be identical (in the case of one route being optimal in more than one way), and a profile may not always yield a Route.  | value | description | | ----- | ----------- | | quiet | Attempts to use roads with less traffic | | regular | The default profile, balances traffic with directness | | fast | Attempts to find the shortest sensible Route |  If no profiles are specified, `regular` will be used.  (optional)
language = 'language_example' # str | An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language.  (optional)
reroute_signature = 'reroute_signature_example' # str | When rerouting (requesting an update to a previous response that accounts for the user's updated location), this value should be set to the `signature` provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the `current_location` (when applicable) or `start` location should be set to the user's latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the `end` location is different, or if more than 1 hour has passed since the original request.  (optional)
start_bearing = 56 # int | An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route.  (optional)

try:
    # Bike directions between two points (ride only)
    api_response = api_instance.bikeridedirections(start, end, profiles=profiles, language=language, reroute_signature=reroute_signature, start_bearing=start_bearing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->bikeridedirections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | [**list[float]**](float.md)| The geographical start of the route, in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 decimal places will be used. | 
 **end** | [**list[float]**](float.md)| The geographical end of the route, in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 decimal places will be used. | 
 **profiles** | **str**| Indicates which \&quot;profiles\&quot; to use when calculating bike directions. Each profile can generate a different Route option, so requesting more profiles will generally give more options. Note that sometimes some of the resulting Routes will be identical (in the case of one route being optimal in more than one way), and a profile may not always yield a Route.  | value | description | | ----- | ----------- | | quiet | Attempts to use roads with less traffic | | regular | The default profile, balances traffic with directness | | fast | Attempts to find the shortest sensible Route |  If no profiles are specified, &#x60;regular&#x60; will be used.  | [optional] 
 **language** | **str**| An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user&#x27;s language preference.    When provided, the response will contain a &#x60;language&#x60; property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn&#x27;t expressed in the request (this will generally be &#x60;en-US&#x60; as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language.  | [optional] 
 **reroute_signature** | **str**| When rerouting (requesting an update to a previous response that accounts for the user&#x27;s updated location), this value should be set to the &#x60;signature&#x60; provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the &#x60;current_location&#x60; (when applicable) or &#x60;start&#x60; location should be set to the user&#x27;s latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the &#x60;end&#x60; location is different, or if more than 1 hour has passed since the original request.  | [optional] 
 **start_bearing** | **int**| An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route.  | [optional] 

### Return type

[**DirectionsResponse**](DirectionsResponse.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **liverouteupdates**
> LiveRouteUpdateMultipleResponse liverouteupdates(body=body)

Live departure and availability information for multiple Routes at once

This retrieves current and live departure information for multiple Routes previously obtained from the `/directions/` endpoints.  Only Routes that have at least one Leg with a Leg Updatable Detail can be updated using this API.  Note it may not always be possible for Citymapper to provide current times or live departure and disruption information for a Leg.  Successful responses (HTTP code `200`) will consume one \"Live Update\" credit for each HTTP response. Unsuccessful calls will not consume any credits. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
configuration = swagger_client.Configuration()
configuration.api_key['Citymapper-Partner-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Citymapper-Partner-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
body = swagger_client.LiveRouteupdatesBody() # LiveRouteupdatesBody |  (optional)

try:
    # Live departure and availability information for multiple Routes at once
    api_response = api_instance.liverouteupdates(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->liverouteupdates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LiveRouteupdatesBody**](LiveRouteupdatesBody.md)|  | [optional] 

### Return type

[**LiveRouteUpdateMultipleResponse**](LiveRouteUpdateMultipleResponse.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **motorscooterdirections**
> DirectionsResponse motorscooterdirections(start, end, brand_id, ride_state=ride_state, current_location=current_location, ride_start_location=ride_start_location, ride_end_location=ride_end_location, language=language, reroute_signature=reroute_signature, start_bearing=start_bearing)

Motor scooter directions between two points (hire vehicles)

**NOTE this API is not available through open access, please contact sales**. Please contact Citymapper using the details provided at the top of the page for information on integrating and using this API.  Gets a motorscooter route between two points, including any initial and final walks. The resulting Route provides enough information to render it on a map, along with a duration estimate. (These results are optimized for larger internal combustion or electric scooters where the rider is seated.)  **NOTE:** The resulting Route currently assumes that the user can ride directly to the specified `end` location, not taking into account any parking or coverage zones. Thus, the resulting Route will contain only an initial Leg of `travel_mode` `walk` and a second Leg of `travel_mode` `self_piloted`. A future update will incorporate parking and coverage zones and add a final `walk` Leg.  This call can be used in several different ways:    **Use any scooter of the specified Brand**  This is the simplest call, only requiring `start`, `end`, and `brand_id`. Citymapper assumes that the user is at the `start` point, and chooses a scooter of the specified Brand, if possible.  **Use a scooter at a specified location**  By adding `original_vehicle_location` to `start`, `end`, and `brand_id`, Citymapper plans a Route that assumes the scooter is at the given location.  **Update a Route in progress**  In order to retrieve an updated Route that includes rerouting from the user's current location if they've diverged from the planned Route, the caller can add the `current_location` and `ride_state` properties, which indicates which Leg of the resulting Route should be rerouted around the user's `current_location`.  Successful responses (HTTP code `200`) will consume one \"Motor Scooter Route\" credit (or one \"Motor Scooter Reroute\" credit if `reroute_signature` is used) for each HTTP response. Unsuccessful calls will not consume any credits. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
configuration = swagger_client.Configuration()
configuration.api_key['Citymapper-Partner-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Citymapper-Partner-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
start = [3.4] # list[float] | The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used.
end = [3.4] # list[float] | The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used.
brand_id = 'brand_id_example' # str | The ID of the Brand of scooters to use for this route. This is necessary in order to determine the location of available scooters, along with any associated coverage and parking restrictions. 
ride_state = 'ride_state_example' # str | Indicates where along the Route the user is. If omitted, `walking_to_vehicle` is used. This property along with `current_location` allows the retrieval of an updated Route that reflects the user's current progress through it.  | value | description | | ----- | ----------- | | walking_to_vehicle | Indicates that the user is walking to collect the vehicle | | riding | Indicates that the user is riding the vehicle | | walking_to_end | Indicates that the user has left the vehicle and is walking to their destination |  (optional)
current_location = 'current_location_example' # str | The user's current location, in order to update the Route based on the user's location. Provided in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  This parameter is used to get an updated Route that reflects the user's actual location if they diverge from the path given in the Route.  If this is provided, the returned Route will contain this location. Which Leg of the Route will contain this location is decided by the value of the `ride_state` parameter.  (optional)
ride_start_location = 'ride_start_location_example' # str | The location of the vehicle to be used, at the beginning of the vehicle ride part of the user's trip along the Route. Provided in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  This must be provided when `ride_state` is `riding` or `walking_to_end`. If not provided when `ride_state` is `walking_to_vehicle` (or not specified), Citymapper will attempt to find the most appropriate vehicle that belongs to the specified `brand_id`.  For compatibility, `original_vehicle_location` is an alias for this parameter  (optional)
ride_end_location = 'ride_end_location_example' # str | The location the vehicle was dropped off at the end of the vehicle ride part of the user's trip along the Route. Provided in WGS84 'latitude,longitude' format. Coordinates should  be in decimal, and only the first 6 digits of precision will be used.  This must be provided when `ride_state` is `walking_to_end`. In all other states this parameter is ignored.  (optional)
language = 'language_example' # str | An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language.  (optional)
reroute_signature = 'reroute_signature_example' # str | When rerouting (requesting an update to a previous response that accounts for the user's updated location), this value should be set to the `signature` provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the `current_location` (when applicable) or `start` location should be set to the user's latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the `end` location is different, or if more than 1 hour has passed since the original request.  (optional)
start_bearing = 56 # int | An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route.  (optional)

try:
    # Motor scooter directions between two points (hire vehicles)
    api_response = api_instance.motorscooterdirections(start, end, brand_id, ride_state=ride_state, current_location=current_location, ride_start_location=ride_start_location, ride_end_location=ride_end_location, language=language, reroute_signature=reroute_signature, start_bearing=start_bearing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->motorscooterdirections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | [**list[float]**](float.md)| The geographical start of the route, in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 decimal places will be used. | 
 **end** | [**list[float]**](float.md)| The geographical end of the route, in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 decimal places will be used. | 
 **brand_id** | **str**| The ID of the Brand of scooters to use for this route. This is necessary in order to determine the location of available scooters, along with any associated coverage and parking restrictions.  | 
 **ride_state** | **str**| Indicates where along the Route the user is. If omitted, &#x60;walking_to_vehicle&#x60; is used. This property along with &#x60;current_location&#x60; allows the retrieval of an updated Route that reflects the user&#x27;s current progress through it.  | value | description | | ----- | ----------- | | walking_to_vehicle | Indicates that the user is walking to collect the vehicle | | riding | Indicates that the user is riding the vehicle | | walking_to_end | Indicates that the user has left the vehicle and is walking to their destination |  | [optional] 
 **current_location** | **str**| The user&#x27;s current location, in order to update the Route based on the user&#x27;s location. Provided in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  This parameter is used to get an updated Route that reflects the user&#x27;s actual location if they diverge from the path given in the Route.  If this is provided, the returned Route will contain this location. Which Leg of the Route will contain this location is decided by the value of the &#x60;ride_state&#x60; parameter.  | [optional] 
 **ride_start_location** | **str**| The location of the vehicle to be used, at the beginning of the vehicle ride part of the user&#x27;s trip along the Route. Provided in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  This must be provided when &#x60;ride_state&#x60; is &#x60;riding&#x60; or &#x60;walking_to_end&#x60;. If not provided when &#x60;ride_state&#x60; is &#x60;walking_to_vehicle&#x60; (or not specified), Citymapper will attempt to find the most appropriate vehicle that belongs to the specified &#x60;brand_id&#x60;.  For compatibility, &#x60;original_vehicle_location&#x60; is an alias for this parameter  | [optional] 
 **ride_end_location** | **str**| The location the vehicle was dropped off at the end of the vehicle ride part of the user&#x27;s trip along the Route. Provided in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should  be in decimal, and only the first 6 digits of precision will be used.  This must be provided when &#x60;ride_state&#x60; is &#x60;walking_to_end&#x60;. In all other states this parameter is ignored.  | [optional] 
 **language** | **str**| An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user&#x27;s language preference.    When provided, the response will contain a &#x60;language&#x60; property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn&#x27;t expressed in the request (this will generally be &#x60;en-US&#x60; as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language.  | [optional] 
 **reroute_signature** | **str**| When rerouting (requesting an update to a previous response that accounts for the user&#x27;s updated location), this value should be set to the &#x60;signature&#x60; provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the &#x60;current_location&#x60; (when applicable) or &#x60;start&#x60; location should be set to the user&#x27;s latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the &#x60;end&#x60; location is different, or if more than 1 hour has passed since the original request.  | [optional] 
 **start_bearing** | **int**| An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route.  | [optional] 

### Return type

[**DirectionsResponse**](DirectionsResponse.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **motorscooterridedirections**
> DirectionsResponse motorscooterridedirections(start, end, language=language, reroute_signature=reroute_signature, start_bearing=start_bearing)

Motor scooter directions between two points (ride only)

Gets a motorscooter route between two points, providing enough information to render it on a map, along with a duration estimate. (These results are optimized for larger internal combustion or electric scooters where the rider is seated.)  This call assumes that the rider has a scooter at the `start` point, and provides an e-scooter route from there to the `end` point if both are within Citymapper's supported areas. The resulting route should contain a single scooter leg, though the `path_annotations` property of the Leg may indicate sections during which the user should walk beside the scooter.  This call does not incorporate any information about scooter operators' coverage or parking areas, but other API calls may be available to do so.  Successful responses (HTTP code `200`) will consume one \"Motor Scooter Route\" credit (or one \"Motor Scooter Reroute\" credit if `reroute_signature` is used) for each HTTP response. Unsuccessful calls will not consume any credits. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
configuration = swagger_client.Configuration()
configuration.api_key['Citymapper-Partner-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Citymapper-Partner-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
start = [3.4] # list[float] | The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used.
end = [3.4] # list[float] | The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used.
language = 'language_example' # str | An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language.  (optional)
reroute_signature = 'reroute_signature_example' # str | When rerouting (requesting an update to a previous response that accounts for the user's updated location), this value should be set to the `signature` provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the `current_location` (when applicable) or `start` location should be set to the user's latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the `end` location is different, or if more than 1 hour has passed since the original request.  (optional)
start_bearing = 56 # int | An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route.  (optional)

try:
    # Motor scooter directions between two points (ride only)
    api_response = api_instance.motorscooterridedirections(start, end, language=language, reroute_signature=reroute_signature, start_bearing=start_bearing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->motorscooterridedirections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | [**list[float]**](float.md)| The geographical start of the route, in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 decimal places will be used. | 
 **end** | [**list[float]**](float.md)| The geographical end of the route, in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 decimal places will be used. | 
 **language** | **str**| An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user&#x27;s language preference.    When provided, the response will contain a &#x60;language&#x60; property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn&#x27;t expressed in the request (this will generally be &#x60;en-US&#x60; as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language.  | [optional] 
 **reroute_signature** | **str**| When rerouting (requesting an update to a previous response that accounts for the user&#x27;s updated location), this value should be set to the &#x60;signature&#x60; provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the &#x60;current_location&#x60; (when applicable) or &#x60;start&#x60; location should be set to the user&#x27;s latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the &#x60;end&#x60; location is different, or if more than 1 hour has passed since the original request.  | [optional] 
 **start_bearing** | **int**| An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route.  | [optional] 

### Return type

[**DirectionsResponse**](DirectionsResponse.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scenariodirections**
> DirectionsResponse scenariodirections(scenario_id, start, end, time=time, time_type=time_type, language=language)

Scenario based directions between two points

**NOTE** This API requires the use of a Scenario ID to select the routing scenario used to determine the type and properties of Routes returned from this endpoint. Please contact Citymapper using the details provided at the top of the page for information on integrating and using this API.  Computes Routes between two points based on a provided scenario.  One or more groups of routes can be provided depending on a scenario. Each group will contain several Routes. Each Route will contain one or more Legs.  Successful responses (HTTP code `200`) will consume \"Scenario Route\" credits depending on a provided scenario and may vary. Unsuccessful calls will not consume any credits. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
configuration = swagger_client.Configuration()
configuration.api_key['Citymapper-Partner-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Citymapper-Partner-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
scenario_id = 'scenario_id_example' # str | Scenario ID for directions.
start = [3.4] # list[float] | The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used.
end = [3.4] # list[float] | The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used.
time = 'time_example' # str | The time to be used as a departure or arrival time constraint when getting directions.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone. For example, `2020-08-19T08:10:42-04:00` expresses August 19, 2020 at 8:10am in Eastern Daylight Time.  (optional)
time_type = 'time_type_example' # str | When a `time` value is given, this determines how the time will be used to constrain the directions that are returned. When this isn't specified, `depart_approximate` is used.  If no `time` is given, this has no effect.  | value | description | | ----- | ----------- | | arrive | Directions are chosen that get the user to their destination on or before `time` | | depart | Directions are chosen assuming the user leaves their origin as soon after `time` as possible | | depart_approximate | Similar to `depart`, but allowing for later departures in order to return more preferable options even if they leave a bit later. This is Citymapper's default way of choosing directions when the time isn't specified |  (optional)
language = 'language_example' # str | An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language.  (optional)

try:
    # Scenario based directions between two points
    api_response = api_instance.scenariodirections(scenario_id, start, end, time=time, time_type=time_type, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->scenariodirections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenario_id** | **str**| Scenario ID for directions. | 
 **start** | [**list[float]**](float.md)| The geographical start of the route, in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 decimal places will be used. | 
 **end** | [**list[float]**](float.md)| The geographical end of the route, in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 decimal places will be used. | 
 **time** | **str**| The time to be used as a departure or arrival time constraint when getting directions.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone. For example, &#x60;2020-08-19T08:10:42-04:00&#x60; expresses August 19, 2020 at 8:10am in Eastern Daylight Time.  | [optional] 
 **time_type** | **str**| When a &#x60;time&#x60; value is given, this determines how the time will be used to constrain the directions that are returned. When this isn&#x27;t specified, &#x60;depart_approximate&#x60; is used.  If no &#x60;time&#x60; is given, this has no effect.  | value | description | | ----- | ----------- | | arrive | Directions are chosen that get the user to their destination on or before &#x60;time&#x60; | | depart | Directions are chosen assuming the user leaves their origin as soon after &#x60;time&#x60; as possible | | depart_approximate | Similar to &#x60;depart&#x60;, but allowing for later departures in order to return more preferable options even if they leave a bit later. This is Citymapper&#x27;s default way of choosing directions when the time isn&#x27;t specified |  | [optional] 
 **language** | **str**| An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user&#x27;s language preference.    When provided, the response will contain a &#x60;language&#x60; property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn&#x27;t expressed in the request (this will generally be &#x60;en-US&#x60; as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language.  | [optional] 

### Return type

[**DirectionsResponse**](DirectionsResponse.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scooterdirections**
> DirectionsResponse scooterdirections(start, end, brand_id, ride_state=ride_state, current_location=current_location, ride_start_location=ride_start_location, ride_end_location=ride_end_location, language=language, reroute_signature=reroute_signature, start_bearing=start_bearing)

E-scooter directions between two points (hire vehicles)

**NOTE this API is not available through open access, please contact sales**. Please contact Citymapper using the details provided at the top of the page for information on integrating and using this API.  Gets an e-scooter route between two points, including any initial and final walks. The resulting Route provides enough information to render it on a map, along with a duration estimate. These results are optimized for small battery-powered scooters that the rider stands on.  This call can be used in several different ways:    **Use any scooter of the specified Brand**  This is the simplest call, only requiring `start`, `end`, and `brand_id`. Citymapper assumes that the user is at the `start` point, and chooses a scooter of the specified Brand, if possible.  **Use a scooter at a specified location**  By adding `original_vehicle_location` to `start`, `end`, and `brand_id`, Citymapper plans a Route that assumes the scooter is at the given location.  **Update a Route in progress**  In order to retrieve an updated Route that includes rerouting from the user's current location if they've diverged from the planned Route, the caller can add the `current_location` and `ride_state` properties, which indicates which Leg of the resulting Route should be rerouted around the user's `current_location`.  Successful responses (HTTP code `200`) will consume one \"Scooter Route\" credit (or one \"Scooter Reroute\" credit if `reroute_signature` is used) for each HTTP response. Unsuccessful calls will not consume any credits. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
configuration = swagger_client.Configuration()
configuration.api_key['Citymapper-Partner-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Citymapper-Partner-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
start = [3.4] # list[float] | The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used.
end = [3.4] # list[float] | The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used.
brand_id = 'brand_id_example' # str | The ID of the Brand of e-scooters to use for this route. This is necessary in order to determine the location of available scooters, along with any associated coverage and parking restrictions. 
ride_state = 'ride_state_example' # str | Indicates where along the Route the user is. If omitted, `walking_to_vehicle` is used. This property along with `current_location` allows the retrieval of an updated Route that reflects the user's current progress through it.  | value | description | | ----- | ----------- | | walking_to_vehicle | Indicates that the user is walking to collect the vehicle | | riding | Indicates that the user is riding the vehicle | | walking_to_end | Indicates that the user has left the vehicle and is walking to their destination |  (optional)
current_location = 'current_location_example' # str | The user's current location, in order to update the Route based on the user's location. Provided in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  This parameter is used to get an updated Route that reflects the user's actual location if they diverge from the path given in the Route.  If this is provided, the returned Route will contain this location. Which Leg of the Route will contain this location is decided by the value of the `ride_state` parameter.  (optional)
ride_start_location = 'ride_start_location_example' # str | The location of the vehicle to be used, at the beginning of the vehicle ride part of the user's trip along the Route. Provided in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  This must be provided when `ride_state` is `riding` or `walking_to_end`. If not provided when `ride_state` is `walking_to_vehicle` (or not specified), Citymapper will attempt to find the most appropriate vehicle that belongs to the specified `brand_id`.  For compatibility, `original_vehicle_location` is an alias for this parameter  (optional)
ride_end_location = 'ride_end_location_example' # str | The location the vehicle was dropped off at the end of the vehicle ride part of the user's trip along the Route. Provided in WGS84 'latitude,longitude' format. Coordinates should  be in decimal, and only the first 6 digits of precision will be used.  This must be provided when `ride_state` is `walking_to_end`. In all other states this parameter is ignored.  (optional)
language = 'language_example' # str | An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language.  (optional)
reroute_signature = 'reroute_signature_example' # str | When rerouting (requesting an update to a previous response that accounts for the user's updated location), this value should be set to the `signature` provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the `current_location` (when applicable) or `start` location should be set to the user's latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the `end` location is different, or if more than 1 hour has passed since the original request.  (optional)
start_bearing = 56 # int | An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route.  (optional)

try:
    # E-scooter directions between two points (hire vehicles)
    api_response = api_instance.scooterdirections(start, end, brand_id, ride_state=ride_state, current_location=current_location, ride_start_location=ride_start_location, ride_end_location=ride_end_location, language=language, reroute_signature=reroute_signature, start_bearing=start_bearing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->scooterdirections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | [**list[float]**](float.md)| The geographical start of the route, in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 decimal places will be used. | 
 **end** | [**list[float]**](float.md)| The geographical end of the route, in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 decimal places will be used. | 
 **brand_id** | **str**| The ID of the Brand of e-scooters to use for this route. This is necessary in order to determine the location of available scooters, along with any associated coverage and parking restrictions.  | 
 **ride_state** | **str**| Indicates where along the Route the user is. If omitted, &#x60;walking_to_vehicle&#x60; is used. This property along with &#x60;current_location&#x60; allows the retrieval of an updated Route that reflects the user&#x27;s current progress through it.  | value | description | | ----- | ----------- | | walking_to_vehicle | Indicates that the user is walking to collect the vehicle | | riding | Indicates that the user is riding the vehicle | | walking_to_end | Indicates that the user has left the vehicle and is walking to their destination |  | [optional] 
 **current_location** | **str**| The user&#x27;s current location, in order to update the Route based on the user&#x27;s location. Provided in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  This parameter is used to get an updated Route that reflects the user&#x27;s actual location if they diverge from the path given in the Route.  If this is provided, the returned Route will contain this location. Which Leg of the Route will contain this location is decided by the value of the &#x60;ride_state&#x60; parameter.  | [optional] 
 **ride_start_location** | **str**| The location of the vehicle to be used, at the beginning of the vehicle ride part of the user&#x27;s trip along the Route. Provided in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  This must be provided when &#x60;ride_state&#x60; is &#x60;riding&#x60; or &#x60;walking_to_end&#x60;. If not provided when &#x60;ride_state&#x60; is &#x60;walking_to_vehicle&#x60; (or not specified), Citymapper will attempt to find the most appropriate vehicle that belongs to the specified &#x60;brand_id&#x60;.  For compatibility, &#x60;original_vehicle_location&#x60; is an alias for this parameter  | [optional] 
 **ride_end_location** | **str**| The location the vehicle was dropped off at the end of the vehicle ride part of the user&#x27;s trip along the Route. Provided in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should  be in decimal, and only the first 6 digits of precision will be used.  This must be provided when &#x60;ride_state&#x60; is &#x60;walking_to_end&#x60;. In all other states this parameter is ignored.  | [optional] 
 **language** | **str**| An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user&#x27;s language preference.    When provided, the response will contain a &#x60;language&#x60; property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn&#x27;t expressed in the request (this will generally be &#x60;en-US&#x60; as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language.  | [optional] 
 **reroute_signature** | **str**| When rerouting (requesting an update to a previous response that accounts for the user&#x27;s updated location), this value should be set to the &#x60;signature&#x60; provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the &#x60;current_location&#x60; (when applicable) or &#x60;start&#x60; location should be set to the user&#x27;s latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the &#x60;end&#x60; location is different, or if more than 1 hour has passed since the original request.  | [optional] 
 **start_bearing** | **int**| An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route.  | [optional] 

### Return type

[**DirectionsResponse**](DirectionsResponse.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scooterridedirections**
> DirectionsResponse scooterridedirections(start, end, language=language, reroute_signature=reroute_signature, start_bearing=start_bearing)

E-scooter directions between two points (ride only)

Gets a scooter route between two points, providing enough information to render it on a map, along with a duration estimate. (These results are optimized for small battery-powered scooters that the rider stands on.)  This call assumes that the rider has a scooter at the `start` point, and provides an e-scooter route from there to the `end` point if both are within Citymapper's supported areas. The resulting route should contain a single scooter leg, though the `path_annotations` property of the Leg may indicate sections during which the user should walk beside the scooter.  This call does not incorporate any information about scooter operators' coverage or parking areas, but other API calls may be available to do so.  Successful responses (HTTP code `200`) will consume one \"Scooter Route\" credit (or one \"Scooter Reroute\" credit if `reroute_signature` is used) for each HTTP response. Unsuccessful calls will not consume any credits. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
configuration = swagger_client.Configuration()
configuration.api_key['Citymapper-Partner-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Citymapper-Partner-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
start = [3.4] # list[float] | The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used.
end = [3.4] # list[float] | The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used.
language = 'language_example' # str | An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language.  (optional)
reroute_signature = 'reroute_signature_example' # str | When rerouting (requesting an update to a previous response that accounts for the user's updated location), this value should be set to the `signature` provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the `current_location` (when applicable) or `start` location should be set to the user's latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the `end` location is different, or if more than 1 hour has passed since the original request.  (optional)
start_bearing = 56 # int | An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route.  (optional)

try:
    # E-scooter directions between two points (ride only)
    api_response = api_instance.scooterridedirections(start, end, language=language, reroute_signature=reroute_signature, start_bearing=start_bearing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->scooterridedirections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | [**list[float]**](float.md)| The geographical start of the route, in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 decimal places will be used. | 
 **end** | [**list[float]**](float.md)| The geographical end of the route, in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 decimal places will be used. | 
 **language** | **str**| An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user&#x27;s language preference.    When provided, the response will contain a &#x60;language&#x60; property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn&#x27;t expressed in the request (this will generally be &#x60;en-US&#x60; as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language.  | [optional] 
 **reroute_signature** | **str**| When rerouting (requesting an update to a previous response that accounts for the user&#x27;s updated location), this value should be set to the &#x60;signature&#x60; provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the &#x60;current_location&#x60; (when applicable) or &#x60;start&#x60; location should be set to the user&#x27;s latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the &#x60;end&#x60; location is different, or if more than 1 hour has passed since the original request.  | [optional] 
 **start_bearing** | **int**| An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route.  | [optional] 

### Return type

[**DirectionsResponse**](DirectionsResponse.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transitdirections**
> DirectionsResponse transitdirections(start, end, time=time, time_type=time_type, language=language, limit=limit)

Transit directions between two points

Computes several public transportation routes between two points.  By default, the results will contain up to 5 Routes. Each one will contain several Legs: usually one at the start and end of the Route with `travel_mode` of `walk`, with at least one with `travel_mode` of `transit` in between.  Successful responses (HTTP code `200`) will consume one \"Transit Route\" credit for each HTTP response. Unsuccessful calls will not consume any credits. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
configuration = swagger_client.Configuration()
configuration.api_key['Citymapper-Partner-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Citymapper-Partner-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
start = [3.4] # list[float] | The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used.
end = [3.4] # list[float] | The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used.
time = 'time_example' # str | The time to be used as a departure or arrival time constraint when getting directions.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone. For example, `2020-08-19T08:10:42-04:00` expresses August 19, 2020 at 8:10am in Eastern Daylight Time.  (optional)
time_type = 'time_type_example' # str | When a `time` value is given, this determines how the time will be used to constrain the directions that are returned. When this isn't specified, `depart_approximate` is used.  If no `time` is given, this has no effect.  | value | description | | ----- | ----------- | | arrive | Directions are chosen that get the user to their destination on or before `time` | | depart | Directions are chosen assuming the user leaves their origin as soon after `time` as possible | | depart_approximate | Similar to `depart`, but allowing for later departures in order to return more preferable options even if they leave a bit later. This is Citymapper's default way of choosing directions when the time isn't specified |  (optional)
language = 'language_example' # str | An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language.  (optional)
limit = 5 # int | Maximum number of Routes to return. (optional) (default to 5)

try:
    # Transit directions between two points
    api_response = api_instance.transitdirections(start, end, time=time, time_type=time_type, language=language, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->transitdirections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | [**list[float]**](float.md)| The geographical start of the route, in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 decimal places will be used. | 
 **end** | [**list[float]**](float.md)| The geographical end of the route, in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 decimal places will be used. | 
 **time** | **str**| The time to be used as a departure or arrival time constraint when getting directions.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone. For example, &#x60;2020-08-19T08:10:42-04:00&#x60; expresses August 19, 2020 at 8:10am in Eastern Daylight Time.  | [optional] 
 **time_type** | **str**| When a &#x60;time&#x60; value is given, this determines how the time will be used to constrain the directions that are returned. When this isn&#x27;t specified, &#x60;depart_approximate&#x60; is used.  If no &#x60;time&#x60; is given, this has no effect.  | value | description | | ----- | ----------- | | arrive | Directions are chosen that get the user to their destination on or before &#x60;time&#x60; | | depart | Directions are chosen assuming the user leaves their origin as soon after &#x60;time&#x60; as possible | | depart_approximate | Similar to &#x60;depart&#x60;, but allowing for later departures in order to return more preferable options even if they leave a bit later. This is Citymapper&#x27;s default way of choosing directions when the time isn&#x27;t specified |  | [optional] 
 **language** | **str**| An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user&#x27;s language preference.    When provided, the response will contain a &#x60;language&#x60; property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn&#x27;t expressed in the request (this will generally be &#x60;en-US&#x60; as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language.  | [optional] 
 **limit** | **int**| Maximum number of Routes to return. | [optional] [default to 5]

### Return type

[**DirectionsResponse**](DirectionsResponse.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **traveltime**
> InlineResponse200 traveltime(start, end, traveltime_types=traveltime_types)

Travel times between two locations

Determines the travel time in various modes of travel between the given two points at the time the request is made. If the call returns code `200`, at least one of the `*_time_minutes` fields will be populated. Otherwise, a code `400` response will be returned.  A request outside of the API coverage areas will be signaled with a code `400` response containing an `error_code` value of `coverage-start` or `coverage-end`. These failures are fast/resource-efficient and are not billed, so there's no need to pre-filter potential requests by location.  Successful responses (HTTP code `200`) will consume one \"Travel Time\" credit for each time returned. Unsuccessful calls will not consume any credits. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
configuration = swagger_client.Configuration()
configuration.api_key['Citymapper-Partner-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Citymapper-Partner-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
start = 'start_example' # str | The geographical start point of the trip, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 digits of precision will be used. 
end = 'end_example' # str | The geographical end point of the trip, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 digits of precision will be used. 
traveltime_types = ['traveltime_types_example'] # list[str] | A comma-separated list of different travel time types to attempt to request. Each request value corresponds to a particular field in the response (response fields will only be present when Citymapper was able to calculate a time for that travel time type).  | value | response property | description | | ----- | ----------------- | ------------| | walk | walk_travel_time_minutes | Walking | | transit | transit_time_minutes | Public transit travel | | bike | bike_time_minutes | Bicycle travel (riding the entire way) | | scooter | scooter_time_minutes | Standing e-scooter travel (riding the entire way) | | motorscooter | motorscooter_time_minutes | Seated motor scooter travel (riding the entire way) |  When this field is omitted or empty, a default value of `walk,transit` will be used.  (optional)

try:
    # Travel times between two locations
    api_response = api_instance.traveltime(start, end, traveltime_types=traveltime_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->traveltime: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **str**| The geographical start point of the trip, in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  | 
 **end** | **str**| The geographical end point of the trip, in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  | 
 **traveltime_types** | [**list[str]**](str.md)| A comma-separated list of different travel time types to attempt to request. Each request value corresponds to a particular field in the response (response fields will only be present when Citymapper was able to calculate a time for that travel time type).  | value | response property | description | | ----- | ----------------- | ------------| | walk | walk_travel_time_minutes | Walking | | transit | transit_time_minutes | Public transit travel | | bike | bike_time_minutes | Bicycle travel (riding the entire way) | | scooter | scooter_time_minutes | Standing e-scooter travel (riding the entire way) | | motorscooter | motorscooter_time_minutes | Seated motor scooter travel (riding the entire way) |  When this field is omitted or empty, a default value of &#x60;walk,transit&#x60; will be used.  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **walkdirections**
> DirectionsResponse walkdirections(start, end, language=language, profiles=profiles, reroute_signature=reroute_signature, start_bearing=start_bearing)

Walking directions between two points

Gets a walking route between two points, providing enough information to render it on a map, along with a duration estimate.  Walking routes are expected to have a single Leg with a `travel_mode` of `walk`.  If Citymapper can't compute walking directions for those points (generally for coverage reasons), the API will return a code `400` response.  The maximum great-circle distance between the `start` and `end` is limited to 100km for this API.  Successful responses (HTTP code `200`) will consume one \"Walk Route\" credit (or one \"Walk Reroute\" credit if `reroute_signature` is used) for each HTTP response. Unsuccessful calls will not consume any credits. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
configuration = swagger_client.Configuration()
configuration.api_key['Citymapper-Partner-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Citymapper-Partner-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
start = [3.4] # list[float] | The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used.
end = [3.4] # list[float] | The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used.
language = 'language_example' # str | An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language.  (optional)
profiles = 'profiles_example' # str | Indicates which \"profiles\" to use when calculating walking directions. Each profile can generate a different Route option, so requesting more profiles will generally give more options. Note that sometimes some of the resulting Routes will be identical (in the case of one route being optimal in more than one way), and a profile may not always yield a Route.  Not all profiles will be available for all start and end routes. Unavailable profiles will be omitted from the response.  | value | description | | ----- | ----------- | | fast | The default profile, attempts to find the fastest sensible Route | | main_roads | Attempts to avoid backstreets and parks |  If no profiles are specified, `fast` will be used.  (optional)
reroute_signature = 'reroute_signature_example' # str | When rerouting (requesting an update to a previous response that accounts for the user's updated location), this value should be set to the `signature` provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the `current_location` (when applicable) or `start` location should be set to the user's latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the `end` location is different, or if more than 1 hour has passed since the original request.  (optional)
start_bearing = 56 # int | An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route.  (optional)

try:
    # Walking directions between two points
    api_response = api_instance.walkdirections(start, end, language=language, profiles=profiles, reroute_signature=reroute_signature, start_bearing=start_bearing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->walkdirections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | [**list[float]**](float.md)| The geographical start of the route, in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 decimal places will be used. | 
 **end** | [**list[float]**](float.md)| The geographical end of the route, in WGS84 &#x27;latitude,longitude&#x27; format. Coordinates should be in decimal, and only the first 6 decimal places will be used. | 
 **language** | **str**| An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user&#x27;s language preference.    When provided, the response will contain a &#x60;language&#x60; property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn&#x27;t expressed in the request (this will generally be &#x60;en-US&#x60; as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language.  | [optional] 
 **profiles** | **str**| Indicates which \&quot;profiles\&quot; to use when calculating walking directions. Each profile can generate a different Route option, so requesting more profiles will generally give more options. Note that sometimes some of the resulting Routes will be identical (in the case of one route being optimal in more than one way), and a profile may not always yield a Route.  Not all profiles will be available for all start and end routes. Unavailable profiles will be omitted from the response.  | value | description | | ----- | ----------- | | fast | The default profile, attempts to find the fastest sensible Route | | main_roads | Attempts to avoid backstreets and parks |  If no profiles are specified, &#x60;fast&#x60; will be used.  | [optional] 
 **reroute_signature** | **str**| When rerouting (requesting an update to a previous response that accounts for the user&#x27;s updated location), this value should be set to the &#x60;signature&#x60; provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the &#x60;current_location&#x60; (when applicable) or &#x60;start&#x60; location should be set to the user&#x27;s latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the &#x60;end&#x60; location is different, or if more than 1 hour has passed since the original request.  | [optional] 
 **start_bearing** | **int**| An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route.  | [optional] 

### Return type

[**DirectionsResponse**](DirectionsResponse.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

