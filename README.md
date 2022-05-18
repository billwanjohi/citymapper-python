# swagger-client
# Introduction  ### Add journey planning and turn-by-turn navigation to your products with our APIs.  Our APIs are powered by our industry-leading global transport data and custom routing algorithms trained on billions of trips.  With our journey planning APIs you can:  - Calculate public transport routes and travel times - Retrieve live departure information for public transport routes - Calculate walk, cycling, e-scooter and motor scooter routes and travel times, including turn-by-turn instructions  Developing a mobile app? See our iOS and Android SDK [here](/).  <div class=\"cta\">  Ready to start?  <a class=\"button\" href=\"https://enterprise.citymapper.com/signup\">Get Access&ensp;&rarr;</a>  </div>  &nbsp;  ### Other resources  [SDK Docs](/)  [Deep Links](https://citymapper.com/news/2386/launch-citymapper-for-directions)  [Learn more about Powered by Citymapper](https://citymapper.com/enterprise)  # Support  ### Have questions?  Check out our FAQ [here](/support/faq.html).  ### Have product feedback or suggestions?  We'd love to hear about your experiences using our APIs, and features you'd like to see next. Please contribute feedback [here](https://form.jotform.com/213393057055353), and keep an eye out for future product releases.  ### Have a sales question?  If you are an enterprise user, or require functionality not available in our public APIs, our sales team are here to help.  Please [contact us](https://citymapper.com/contact/powered) with a description of your project or business need and we'll be in touch.  # Pricing  ### Get started for free  Get 5,000 monthly [requests](#requests) for free across all our products, making it easy to start building with our API or SDK.  <div class=\"cta\">  <a class=\"button\" href=\"https://enterprise.citymapper.com/signup\">Sign up&ensp;&rarr;</a>  </div>  &nbsp;  ### **Pay as you go**  Ready to launch? Scale quickly and flexibly with our pay-as-you-go plan.  Pick the products you need and only get charged for what you use – plus enjoy £100 free credit allowance from us each month.  To switch to the pay-as-you-go plan, please visit the [enterprise dashboard](https://enterprise.citymapper.com) and add a payment method. It’s that simple.  See below for our API pricing:  | Travel Time API           | Unit             | Price per Unit | | ------------------------- | ---------------- | -------------- | | Walk Travel Time          | per 1000 results | £0.40          | | Cycle Travel Time         | per 1000 results | £0.80          | | E-Scooter Travel Time     | per 1000 results | £0.80          | | Motor Scooter Travel Time | per 1000 results | £0.80          | | Transit Travel Time       | per 1000 results | £1.00          |  | Directions API                        | Unit                       | Price per Unit                     | | ------------------------------------- | -------------------------- | ---------------------------------- | | Walk Directions: Fast Profile         | per 1000 results           | £0.50                              | | Walk Directions: Main Roads Profile   | per 1000 results           | £0.50                              | | Cycle Directions: Quiet Profile       | per 1000 results           | £1.00                              | | Cycle Directions: Regular Profile     | per 1000 results           | £1.00                              | | Cycle Directions: Fast Profile        | per 1000 results           | £1.00                              | | E-Scooter Directions                  | per 1000 results           | £1.00                              | | Motor Scooter Directions              | per 1000 results           | £1.00                              | | Transit Directions                    | per 1000 routes\\*          | £1.20                              | | Transit Directions: Real-Time Updates | per 1000 route updates\\*\\* | Available on Enterprise plans only | | Hire Vehicle Directions               | per 1000 results           | Available on Enterprise plans only |  \\* Up to 5 transit routes can be returned in a single result  \\*\\* One update applies to a single transit route. Updates are refreshed every minute  ### Enterprise plans to help you grow  Looking for additional features or have higher volume requirements? Please [contact our sales team](https://citymapper.com/contact/powered).  ### Terms of service  Read the full [terms of service](https://citymapper.com/developer-terms).  ### Requests  A request is defined as a single call which successfully returns a travel time, directions or navigation result. Monthly requests are aggregated across all Powered by Citymapper products. If you're not on a paid plan, you’ll be notified via email once you exceed the free usage allowance in a given month (the month-long period aligns with the calendar month). Further requests will no longer return results for the remainder of that month, and your free usage allowance will reset at the start of the next month.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1.6.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://api.external.citymapper.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*EndpointsApi* | [**bikedirections**](docs/EndpointsApi.md#bikedirections) | **GET** /api/1/directions/bike | Bike directions between two points (hire vehicles)
*EndpointsApi* | [**bikeridedirections**](docs/EndpointsApi.md#bikeridedirections) | **GET** /api/1/directions/bikeride | Bike directions between two points (ride only)
*EndpointsApi* | [**liverouteupdates**](docs/EndpointsApi.md#liverouteupdates) | **POST** /api/1/live/routeupdates | Live departure and availability information for multiple Routes at once
*EndpointsApi* | [**motorscooterdirections**](docs/EndpointsApi.md#motorscooterdirections) | **GET** /api/1/directions/motorscooter | Motor scooter directions between two points (hire vehicles)
*EndpointsApi* | [**motorscooterridedirections**](docs/EndpointsApi.md#motorscooterridedirections) | **GET** /api/1/directions/motorscooterride | Motor scooter directions between two points (ride only)
*EndpointsApi* | [**scenariodirections**](docs/EndpointsApi.md#scenariodirections) | **GET** /api/1/directions/scenario | Scenario based directions between two points
*EndpointsApi* | [**scooterdirections**](docs/EndpointsApi.md#scooterdirections) | **GET** /api/1/directions/scooter | E-scooter directions between two points (hire vehicles)
*EndpointsApi* | [**scooterridedirections**](docs/EndpointsApi.md#scooterridedirections) | **GET** /api/1/directions/scooterride | E-scooter directions between two points (ride only)
*EndpointsApi* | [**transitdirections**](docs/EndpointsApi.md#transitdirections) | **GET** /api/1/directions/transit | Transit directions between two points
*EndpointsApi* | [**traveltime**](docs/EndpointsApi.md#traveltime) | **GET** /api/1/traveltimes | Travel times between two locations
*EndpointsApi* | [**walkdirections**](docs/EndpointsApi.md#walkdirections) | **GET** /api/1/directions/walk | Walking directions between two points

## Documentation For Models

 - [AllOfRoutePrice](docs/AllOfRoutePrice.md)
 - [AllOfServiceBrand](docs/AllOfServiceBrand.md)
 - [AllOfStationExitCoordinates](docs/AllOfStationExitCoordinates.md)
 - [AllOfStationWalkDetailsRecommendedExit](docs/AllOfStationWalkDetailsRecommendedExit.md)
 - [Brand](docs/Brand.md)
 - [BrandImage](docs/BrandImage.md)
 - [Coordinates](docs/Coordinates.md)
 - [Departure](docs/Departure.md)
 - [DirectionsResponse](docs/DirectionsResponse.md)
 - [DurationAccuracy](docs/DurationAccuracy.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [GatewayError](docs/GatewayError.md)
 - [HireVehicleLegPickup](docs/HireVehicleLegPickup.md)
 - [HireVehicleMetadata](docs/HireVehicleMetadata.md)
 - [HireVehicleStationLegDropoff](docs/HireVehicleStationLegDropoff.md)
 - [HireVehicleStationMetadata](docs/HireVehicleStationMetadata.md)
 - [Image](docs/Image.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [Instruction](docs/Instruction.md)
 - [InstructionDescriptionFormatReplacements](docs/InstructionDescriptionFormatReplacements.md)
 - [Leg](docs/Leg.md)
 - [LegUpdatableDetail](docs/LegUpdatableDetail.md)
 - [LegVariantSelfPiloted](docs/LegVariantSelfPiloted.md)
 - [LegVariantServices](docs/LegVariantServices.md)
 - [LegVariantTransit](docs/LegVariantTransit.md)
 - [LegVariantTransitBestBoardingSections](docs/LegVariantTransitBestBoardingSections.md)
 - [LegVariantWalk](docs/LegVariantWalk.md)
 - [LiveRouteUpdateMultipleResponse](docs/LiveRouteUpdateMultipleResponse.md)
 - [LiveRouteUpdateResponse](docs/LiveRouteUpdateResponse.md)
 - [LiveRouteupdatesBody](docs/LiveRouteupdatesBody.md)
 - [PathAnnotation](docs/PathAnnotation.md)
 - [Price](docs/Price.md)
 - [Route](docs/Route.md)
 - [RouteGroup](docs/RouteGroup.md)
 - [RouteMetadata](docs/RouteMetadata.md)
 - [RouteUpdate](docs/RouteUpdate.md)
 - [Service](docs/Service.md)
 - [ServiceImage](docs/ServiceImage.md)
 - [StationExit](docs/StationExit.md)
 - [StationWalkDetails](docs/StationWalkDetails.md)
 - [Status](docs/Status.md)
 - [StatusServiceStopRanges](docs/StatusServiceStopRanges.md)
 - [Stop](docs/Stop.md)
 - [VehicleType](docs/VehicleType.md)
 - [Waypoint](docs/Waypoint.md)

## Documentation For Authorization


## API Key

- **Type**: API key
- **API key parameter name**: Citymapper-Partner-Key
- **Location**: HTTP header


## Author


