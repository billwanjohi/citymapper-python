# coding: utf-8

"""
    Citymapper API

    # Introduction  ### Add journey planning and turn-by-turn navigation to your products with our APIs.  Our APIs are powered by our industry-leading global transport data and custom routing algorithms trained on billions of trips.  With our journey planning APIs you can:  - Calculate public transport routes and travel times - Retrieve live departure information for public transport routes - Calculate walk, cycling, e-scooter and motor scooter routes and travel times, including turn-by-turn instructions  Developing a mobile app? See our iOS and Android SDK [here](/).  <div class=\"cta\">  Ready to start?  <a class=\"button\" href=\"https://enterprise.citymapper.com/signup\">Get Access&ensp;&rarr;</a>  </div>  &nbsp;  ### Other resources  [SDK Docs](/)  [Deep Links](https://citymapper.com/news/2386/launch-citymapper-for-directions)  [Learn more about Powered by Citymapper](https://citymapper.com/enterprise)  # Support  ### Have questions?  Check out our FAQ [here](/support/faq.html).  ### Have product feedback or suggestions?  We'd love to hear about your experiences using our APIs, and features you'd like to see next. Please contribute feedback [here](https://form.jotform.com/213393057055353), and keep an eye out for future product releases.  ### Have a sales question?  If you are an enterprise user, or require functionality not available in our public APIs, our sales team are here to help.  Please [contact us](https://citymapper.com/contact/powered) with a description of your project or business need and we'll be in touch.  # Pricing  ### Get started for free  Get 5,000 monthly [requests](#requests) for free across all our products, making it easy to start building with our API or SDK.  <div class=\"cta\">  <a class=\"button\" href=\"https://enterprise.citymapper.com/signup\">Sign up&ensp;&rarr;</a>  </div>  &nbsp;  ### **Pay as you go**  Ready to launch? Scale quickly and flexibly with our pay-as-you-go plan.  Pick the products you need and only get charged for what you use – plus enjoy £100 free credit allowance from us each month.  To switch to the pay-as-you-go plan, please visit the [enterprise dashboard](https://enterprise.citymapper.com) and add a payment method. It’s that simple.  See below for our API pricing:  | Travel Time API           | Unit             | Price per Unit | | ------------------------- | ---------------- | -------------- | | Walk Travel Time          | per 1000 results | £0.40          | | Cycle Travel Time         | per 1000 results | £0.80          | | E-Scooter Travel Time     | per 1000 results | £0.80          | | Motor Scooter Travel Time | per 1000 results | £0.80          | | Transit Travel Time       | per 1000 results | £1.00          |  | Directions API                        | Unit                       | Price per Unit                     | | ------------------------------------- | -------------------------- | ---------------------------------- | | Walk Directions: Fast Profile         | per 1000 results           | £0.50                              | | Walk Directions: Main Roads Profile   | per 1000 results           | £0.50                              | | Cycle Directions: Quiet Profile       | per 1000 results           | £1.00                              | | Cycle Directions: Regular Profile     | per 1000 results           | £1.00                              | | Cycle Directions: Fast Profile        | per 1000 results           | £1.00                              | | E-Scooter Directions                  | per 1000 results           | £1.00                              | | Motor Scooter Directions              | per 1000 results           | £1.00                              | | Transit Directions                    | per 1000 routes\\*          | £1.20                              | | Transit Directions: Real-Time Updates | per 1000 route updates\\*\\* | Available on Enterprise plans only | | Hire Vehicle Directions               | per 1000 results           | Available on Enterprise plans only |  \\* Up to 5 transit routes can be returned in a single result  \\*\\* One update applies to a single transit route. Updates are refreshed every minute  ### Enterprise plans to help you grow  Looking for additional features or have higher volume requirements? Please [contact our sales team](https://citymapper.com/contact/powered).  ### Terms of service  Read the full [terms of service](https://citymapper.com/developer-terms).  ### Requests  A request is defined as a single call which successfully returns a travel time, directions or navigation result. Monthly requests are aggregated across all Powered by Citymapper products. If you're not on a paid plan, you’ll be notified via email once you exceed the free usage allowance in a given month (the month-long period aligns with the calendar month). Further requests will no longer return results for the remainder of that month, and your free usage allowance will reset at the start of the next month.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    OpenAPI spec version: v1.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class EndpointsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def bikedirections(self, start, end, brand_id, **kwargs):  # noqa: E501
        """Bike directions between two points (hire vehicles)  # noqa: E501

        **NOTE this API is not available through open access, please contact sales**. Please contact Citymapper using the details provided at the top of the page for information on integrating and using this API.  Gets an bike route between two points, including any initial and final walks. The resulting Route provides enough information to render it on a map, along with a duration estimate.  This call can be used in several different ways:    **Use any bike of the specified Brand**  This is the simplest call, only requiring `start`, `end`, and `brand_id`. Citymapper assumes that the user is at the `start` point, and chooses a bike of the specified Brand, if possible.  **Use a bike at a specified location**  By adding `original_vehicle_location` to `start`, `end`, and `brand_id`, Citymapper plans a Route that assumes the bike is at the given location.  **Update a Route in progress**  In order to retrieve an updated Route that includes rerouting from the user's current location if they've diverged from the planned Route, the caller can add the `current_location` and `ride_state` properties, which indicates which Leg of the resulting Route should be rerouted around the user's `current_location`.  Successful responses (HTTP code `200`) will consume one \"Bike Route\" credit (or one \"Bike Reroute\" credit if `reroute_signature` is used) for each HTTP response. Unsuccessful calls will not consume any credits.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bikedirections(start, end, brand_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[float] start: The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param list[float] end: The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param str brand_id: The ID of the Brand of bike to use for this route. This is necessary in order to determine the location of available bikes, along with any associated coverage and parking restrictions.  (required)
        :param str ride_state: Indicates where along the Route the user is. If omitted, `walking_to_vehicle` is used. This property along with `current_location` allows the retrieval of an updated Route that reflects the user's current progress through it.  | value | description | | ----- | ----------- | | walking_to_vehicle | Indicates that the user is walking to collect the vehicle | | riding | Indicates that the user is riding the vehicle | | walking_to_end | Indicates that the user has left the vehicle and is walking to their destination | 
        :param str current_location: The user's current location, in order to update the Route based on the user's location. Provided in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  This parameter is used to get an updated Route that reflects the user's actual location if they diverge from the path given in the Route.  If this is provided, the returned Route will contain this location. Which Leg of the Route will contain this location is decided by the value of the `ride_state` parameter. 
        :param str ride_start_location: The location of the vehicle to be used, at the beginning of the vehicle ride part of the user's trip along the Route. Provided in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  This must be provided when `ride_state` is `riding` or `walking_to_end`. If not provided when `ride_state` is `walking_to_vehicle` (or not specified), Citymapper will attempt to find the most appropriate vehicle that belongs to the specified `brand_id`.  For compatibility, `original_vehicle_location` is an alias for this parameter 
        :param str ride_end_location: The location the vehicle was dropped off at the end of the vehicle ride part of the user's trip along the Route. Provided in WGS84 'latitude,longitude' format. Coordinates should  be in decimal, and only the first 6 digits of precision will be used.  This must be provided when `ride_state` is `walking_to_end`. In all other states this parameter is ignored. 
        :param str profiles: Indicates which \"profiles\" to use when calculating bike directions. Each profile can generate a different Route option, so requesting more profiles will generally give more options. Note that sometimes some of the resulting Routes will be identical (in the case of one route being optimal in more than one way), and a profile may not always yield a Route.  | value | description | | ----- | ----------- | | quiet | Attempts to use roads with less traffic | | regular | The default profile, balances traffic with directness | | fast | Attempts to find the shortest sensible Route |  If no profiles are specified, `regular` will be used. 
        :param str language: An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language. 
        :param str reroute_signature: When rerouting (requesting an update to a previous response that accounts for the user's updated location), this value should be set to the `signature` provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the `current_location` (when applicable) or `start` location should be set to the user's latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the `end` location is different, or if more than 1 hour has passed since the original request. 
        :param int start_bearing: An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route. 
        :return: DirectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bikedirections_with_http_info(start, end, brand_id, **kwargs)  # noqa: E501
        else:
            (data) = self.bikedirections_with_http_info(start, end, brand_id, **kwargs)  # noqa: E501
            return data

    def bikedirections_with_http_info(self, start, end, brand_id, **kwargs):  # noqa: E501
        """Bike directions between two points (hire vehicles)  # noqa: E501

        **NOTE this API is not available through open access, please contact sales**. Please contact Citymapper using the details provided at the top of the page for information on integrating and using this API.  Gets an bike route between two points, including any initial and final walks. The resulting Route provides enough information to render it on a map, along with a duration estimate.  This call can be used in several different ways:    **Use any bike of the specified Brand**  This is the simplest call, only requiring `start`, `end`, and `brand_id`. Citymapper assumes that the user is at the `start` point, and chooses a bike of the specified Brand, if possible.  **Use a bike at a specified location**  By adding `original_vehicle_location` to `start`, `end`, and `brand_id`, Citymapper plans a Route that assumes the bike is at the given location.  **Update a Route in progress**  In order to retrieve an updated Route that includes rerouting from the user's current location if they've diverged from the planned Route, the caller can add the `current_location` and `ride_state` properties, which indicates which Leg of the resulting Route should be rerouted around the user's `current_location`.  Successful responses (HTTP code `200`) will consume one \"Bike Route\" credit (or one \"Bike Reroute\" credit if `reroute_signature` is used) for each HTTP response. Unsuccessful calls will not consume any credits.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bikedirections_with_http_info(start, end, brand_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[float] start: The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param list[float] end: The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param str brand_id: The ID of the Brand of bike to use for this route. This is necessary in order to determine the location of available bikes, along with any associated coverage and parking restrictions.  (required)
        :param str ride_state: Indicates where along the Route the user is. If omitted, `walking_to_vehicle` is used. This property along with `current_location` allows the retrieval of an updated Route that reflects the user's current progress through it.  | value | description | | ----- | ----------- | | walking_to_vehicle | Indicates that the user is walking to collect the vehicle | | riding | Indicates that the user is riding the vehicle | | walking_to_end | Indicates that the user has left the vehicle and is walking to their destination | 
        :param str current_location: The user's current location, in order to update the Route based on the user's location. Provided in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  This parameter is used to get an updated Route that reflects the user's actual location if they diverge from the path given in the Route.  If this is provided, the returned Route will contain this location. Which Leg of the Route will contain this location is decided by the value of the `ride_state` parameter. 
        :param str ride_start_location: The location of the vehicle to be used, at the beginning of the vehicle ride part of the user's trip along the Route. Provided in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  This must be provided when `ride_state` is `riding` or `walking_to_end`. If not provided when `ride_state` is `walking_to_vehicle` (or not specified), Citymapper will attempt to find the most appropriate vehicle that belongs to the specified `brand_id`.  For compatibility, `original_vehicle_location` is an alias for this parameter 
        :param str ride_end_location: The location the vehicle was dropped off at the end of the vehicle ride part of the user's trip along the Route. Provided in WGS84 'latitude,longitude' format. Coordinates should  be in decimal, and only the first 6 digits of precision will be used.  This must be provided when `ride_state` is `walking_to_end`. In all other states this parameter is ignored. 
        :param str profiles: Indicates which \"profiles\" to use when calculating bike directions. Each profile can generate a different Route option, so requesting more profiles will generally give more options. Note that sometimes some of the resulting Routes will be identical (in the case of one route being optimal in more than one way), and a profile may not always yield a Route.  | value | description | | ----- | ----------- | | quiet | Attempts to use roads with less traffic | | regular | The default profile, balances traffic with directness | | fast | Attempts to find the shortest sensible Route |  If no profiles are specified, `regular` will be used. 
        :param str language: An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language. 
        :param str reroute_signature: When rerouting (requesting an update to a previous response that accounts for the user's updated location), this value should be set to the `signature` provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the `current_location` (when applicable) or `start` location should be set to the user's latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the `end` location is different, or if more than 1 hour has passed since the original request. 
        :param int start_bearing: An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route. 
        :return: DirectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start', 'end', 'brand_id', 'ride_state', 'current_location', 'ride_start_location', 'ride_end_location', 'profiles', 'language', 'reroute_signature', 'start_bearing']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bikedirections" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'start' is set
        if ('start' not in params or
                params['start'] is None):
            raise ValueError("Missing the required parameter `start` when calling `bikedirections`")  # noqa: E501
        # verify the required parameter 'end' is set
        if ('end' not in params or
                params['end'] is None):
            raise ValueError("Missing the required parameter `end` when calling `bikedirections`")  # noqa: E501
        # verify the required parameter 'brand_id' is set
        if ('brand_id' not in params or
                params['brand_id'] is None):
            raise ValueError("Missing the required parameter `brand_id` when calling `bikedirections`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501
            collection_formats['start'] = 'multi'  # noqa: E501
        if 'end' in params:
            query_params.append(('end', params['end']))  # noqa: E501
            collection_formats['end'] = 'multi'  # noqa: E501
        if 'brand_id' in params:
            query_params.append(('brand_id', params['brand_id']))  # noqa: E501
        if 'ride_state' in params:
            query_params.append(('ride_state', params['ride_state']))  # noqa: E501
        if 'current_location' in params:
            query_params.append(('current_location', params['current_location']))  # noqa: E501
        if 'ride_start_location' in params:
            query_params.append(('ride_start_location', params['ride_start_location']))  # noqa: E501
        if 'ride_end_location' in params:
            query_params.append(('ride_end_location', params['ride_end_location']))  # noqa: E501
        if 'profiles' in params:
            query_params.append(('profiles', params['profiles']))  # noqa: E501
        if 'language' in params:
            query_params.append(('language', params['language']))  # noqa: E501
        if 'reroute_signature' in params:
            query_params.append(('reroute_signature', params['reroute_signature']))  # noqa: E501
        if 'start_bearing' in params:
            query_params.append(('start_bearing', params['start_bearing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API Key']  # noqa: E501

        return self.api_client.call_api(
            '/api/1/directions/bike', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DirectionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def bikeridedirections(self, start, end, **kwargs):  # noqa: E501
        """Bike directions between two points (ride only)  # noqa: E501

        Gets a bike route between two points, providing enough information to render it on a map, along with a duration estimate.  This call assumes that the rider has a bicycle at the `start` point, and provides a biking route from there to the `end` point if both are within Citymapper's supported areas. The resulting route should contain a single bike leg, though the `path_annotations` property of the Leg may indicate sections during which the user should walk beside the bike.  This call does not incorporate any information about bike operators' coverage or parking areas, but other API calls may be available to do so.  The maximum great-circle distance between the start and end is limited to 200km for this API.  Successful responses (HTTP code `200`) will consume one \"Bike Route\" credit (or one \"Bike Reroute\" credit if `reroute_signature` is used) for each HTTP response. Unsuccessful calls will not consume any credits.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bikeridedirections(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[float] start: The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param list[float] end: The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param str profiles: Indicates which \"profiles\" to use when calculating bike directions. Each profile can generate a different Route option, so requesting more profiles will generally give more options. Note that sometimes some of the resulting Routes will be identical (in the case of one route being optimal in more than one way), and a profile may not always yield a Route.  | value | description | | ----- | ----------- | | quiet | Attempts to use roads with less traffic | | regular | The default profile, balances traffic with directness | | fast | Attempts to find the shortest sensible Route |  If no profiles are specified, `regular` will be used. 
        :param str language: An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language. 
        :param str reroute_signature: When rerouting (requesting an update to a previous response that accounts for the user's updated location), this value should be set to the `signature` provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the `current_location` (when applicable) or `start` location should be set to the user's latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the `end` location is different, or if more than 1 hour has passed since the original request. 
        :param int start_bearing: An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route. 
        :return: DirectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bikeridedirections_with_http_info(start, end, **kwargs)  # noqa: E501
        else:
            (data) = self.bikeridedirections_with_http_info(start, end, **kwargs)  # noqa: E501
            return data

    def bikeridedirections_with_http_info(self, start, end, **kwargs):  # noqa: E501
        """Bike directions between two points (ride only)  # noqa: E501

        Gets a bike route between two points, providing enough information to render it on a map, along with a duration estimate.  This call assumes that the rider has a bicycle at the `start` point, and provides a biking route from there to the `end` point if both are within Citymapper's supported areas. The resulting route should contain a single bike leg, though the `path_annotations` property of the Leg may indicate sections during which the user should walk beside the bike.  This call does not incorporate any information about bike operators' coverage or parking areas, but other API calls may be available to do so.  The maximum great-circle distance between the start and end is limited to 200km for this API.  Successful responses (HTTP code `200`) will consume one \"Bike Route\" credit (or one \"Bike Reroute\" credit if `reroute_signature` is used) for each HTTP response. Unsuccessful calls will not consume any credits.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bikeridedirections_with_http_info(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[float] start: The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param list[float] end: The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param str profiles: Indicates which \"profiles\" to use when calculating bike directions. Each profile can generate a different Route option, so requesting more profiles will generally give more options. Note that sometimes some of the resulting Routes will be identical (in the case of one route being optimal in more than one way), and a profile may not always yield a Route.  | value | description | | ----- | ----------- | | quiet | Attempts to use roads with less traffic | | regular | The default profile, balances traffic with directness | | fast | Attempts to find the shortest sensible Route |  If no profiles are specified, `regular` will be used. 
        :param str language: An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language. 
        :param str reroute_signature: When rerouting (requesting an update to a previous response that accounts for the user's updated location), this value should be set to the `signature` provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the `current_location` (when applicable) or `start` location should be set to the user's latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the `end` location is different, or if more than 1 hour has passed since the original request. 
        :param int start_bearing: An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route. 
        :return: DirectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start', 'end', 'profiles', 'language', 'reroute_signature', 'start_bearing']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bikeridedirections" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'start' is set
        if ('start' not in params or
                params['start'] is None):
            raise ValueError("Missing the required parameter `start` when calling `bikeridedirections`")  # noqa: E501
        # verify the required parameter 'end' is set
        if ('end' not in params or
                params['end'] is None):
            raise ValueError("Missing the required parameter `end` when calling `bikeridedirections`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501
            collection_formats['start'] = 'multi'  # noqa: E501
        if 'end' in params:
            query_params.append(('end', params['end']))  # noqa: E501
            collection_formats['end'] = 'multi'  # noqa: E501
        if 'profiles' in params:
            query_params.append(('profiles', params['profiles']))  # noqa: E501
        if 'language' in params:
            query_params.append(('language', params['language']))  # noqa: E501
        if 'reroute_signature' in params:
            query_params.append(('reroute_signature', params['reroute_signature']))  # noqa: E501
        if 'start_bearing' in params:
            query_params.append(('start_bearing', params['start_bearing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API Key']  # noqa: E501

        return self.api_client.call_api(
            '/api/1/directions/bikeride', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DirectionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def liverouteupdates(self, **kwargs):  # noqa: E501
        """Live departure and availability information for multiple Routes at once  # noqa: E501

        This retrieves current and live departure information for multiple Routes previously obtained from the `/directions/` endpoints.  Only Routes that have at least one Leg with a Leg Updatable Detail can be updated using this API.  Note it may not always be possible for Citymapper to provide current times or live departure and disruption information for a Leg.  Successful responses (HTTP code `200`) will consume one \"Live Update\" credit for each HTTP response. Unsuccessful calls will not consume any credits.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.liverouteupdates(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LiveRouteupdatesBody body:
        :return: LiveRouteUpdateMultipleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.liverouteupdates_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.liverouteupdates_with_http_info(**kwargs)  # noqa: E501
            return data

    def liverouteupdates_with_http_info(self, **kwargs):  # noqa: E501
        """Live departure and availability information for multiple Routes at once  # noqa: E501

        This retrieves current and live departure information for multiple Routes previously obtained from the `/directions/` endpoints.  Only Routes that have at least one Leg with a Leg Updatable Detail can be updated using this API.  Note it may not always be possible for Citymapper to provide current times or live departure and disruption information for a Leg.  Successful responses (HTTP code `200`) will consume one \"Live Update\" credit for each HTTP response. Unsuccessful calls will not consume any credits.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.liverouteupdates_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LiveRouteupdatesBody body:
        :return: LiveRouteUpdateMultipleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method liverouteupdates" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API Key']  # noqa: E501

        return self.api_client.call_api(
            '/api/1/live/routeupdates', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LiveRouteUpdateMultipleResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def motorscooterdirections(self, start, end, brand_id, **kwargs):  # noqa: E501
        """Motor scooter directions between two points (hire vehicles)  # noqa: E501

        **NOTE this API is not available through open access, please contact sales**. Please contact Citymapper using the details provided at the top of the page for information on integrating and using this API.  Gets a motorscooter route between two points, including any initial and final walks. The resulting Route provides enough information to render it on a map, along with a duration estimate. (These results are optimized for larger internal combustion or electric scooters where the rider is seated.)  **NOTE:** The resulting Route currently assumes that the user can ride directly to the specified `end` location, not taking into account any parking or coverage zones. Thus, the resulting Route will contain only an initial Leg of `travel_mode` `walk` and a second Leg of `travel_mode` `self_piloted`. A future update will incorporate parking and coverage zones and add a final `walk` Leg.  This call can be used in several different ways:    **Use any scooter of the specified Brand**  This is the simplest call, only requiring `start`, `end`, and `brand_id`. Citymapper assumes that the user is at the `start` point, and chooses a scooter of the specified Brand, if possible.  **Use a scooter at a specified location**  By adding `original_vehicle_location` to `start`, `end`, and `brand_id`, Citymapper plans a Route that assumes the scooter is at the given location.  **Update a Route in progress**  In order to retrieve an updated Route that includes rerouting from the user's current location if they've diverged from the planned Route, the caller can add the `current_location` and `ride_state` properties, which indicates which Leg of the resulting Route should be rerouted around the user's `current_location`.  Successful responses (HTTP code `200`) will consume one \"Motor Scooter Route\" credit (or one \"Motor Scooter Reroute\" credit if `reroute_signature` is used) for each HTTP response. Unsuccessful calls will not consume any credits.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.motorscooterdirections(start, end, brand_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[float] start: The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param list[float] end: The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param str brand_id: The ID of the Brand of scooters to use for this route. This is necessary in order to determine the location of available scooters, along with any associated coverage and parking restrictions.  (required)
        :param str ride_state: Indicates where along the Route the user is. If omitted, `walking_to_vehicle` is used. This property along with `current_location` allows the retrieval of an updated Route that reflects the user's current progress through it.  | value | description | | ----- | ----------- | | walking_to_vehicle | Indicates that the user is walking to collect the vehicle | | riding | Indicates that the user is riding the vehicle | | walking_to_end | Indicates that the user has left the vehicle and is walking to their destination | 
        :param str current_location: The user's current location, in order to update the Route based on the user's location. Provided in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  This parameter is used to get an updated Route that reflects the user's actual location if they diverge from the path given in the Route.  If this is provided, the returned Route will contain this location. Which Leg of the Route will contain this location is decided by the value of the `ride_state` parameter. 
        :param str ride_start_location: The location of the vehicle to be used, at the beginning of the vehicle ride part of the user's trip along the Route. Provided in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  This must be provided when `ride_state` is `riding` or `walking_to_end`. If not provided when `ride_state` is `walking_to_vehicle` (or not specified), Citymapper will attempt to find the most appropriate vehicle that belongs to the specified `brand_id`.  For compatibility, `original_vehicle_location` is an alias for this parameter 
        :param str ride_end_location: The location the vehicle was dropped off at the end of the vehicle ride part of the user's trip along the Route. Provided in WGS84 'latitude,longitude' format. Coordinates should  be in decimal, and only the first 6 digits of precision will be used.  This must be provided when `ride_state` is `walking_to_end`. In all other states this parameter is ignored. 
        :param str language: An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language. 
        :param str reroute_signature: When rerouting (requesting an update to a previous response that accounts for the user's updated location), this value should be set to the `signature` provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the `current_location` (when applicable) or `start` location should be set to the user's latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the `end` location is different, or if more than 1 hour has passed since the original request. 
        :param int start_bearing: An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route. 
        :return: DirectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.motorscooterdirections_with_http_info(start, end, brand_id, **kwargs)  # noqa: E501
        else:
            (data) = self.motorscooterdirections_with_http_info(start, end, brand_id, **kwargs)  # noqa: E501
            return data

    def motorscooterdirections_with_http_info(self, start, end, brand_id, **kwargs):  # noqa: E501
        """Motor scooter directions between two points (hire vehicles)  # noqa: E501

        **NOTE this API is not available through open access, please contact sales**. Please contact Citymapper using the details provided at the top of the page for information on integrating and using this API.  Gets a motorscooter route between two points, including any initial and final walks. The resulting Route provides enough information to render it on a map, along with a duration estimate. (These results are optimized for larger internal combustion or electric scooters where the rider is seated.)  **NOTE:** The resulting Route currently assumes that the user can ride directly to the specified `end` location, not taking into account any parking or coverage zones. Thus, the resulting Route will contain only an initial Leg of `travel_mode` `walk` and a second Leg of `travel_mode` `self_piloted`. A future update will incorporate parking and coverage zones and add a final `walk` Leg.  This call can be used in several different ways:    **Use any scooter of the specified Brand**  This is the simplest call, only requiring `start`, `end`, and `brand_id`. Citymapper assumes that the user is at the `start` point, and chooses a scooter of the specified Brand, if possible.  **Use a scooter at a specified location**  By adding `original_vehicle_location` to `start`, `end`, and `brand_id`, Citymapper plans a Route that assumes the scooter is at the given location.  **Update a Route in progress**  In order to retrieve an updated Route that includes rerouting from the user's current location if they've diverged from the planned Route, the caller can add the `current_location` and `ride_state` properties, which indicates which Leg of the resulting Route should be rerouted around the user's `current_location`.  Successful responses (HTTP code `200`) will consume one \"Motor Scooter Route\" credit (or one \"Motor Scooter Reroute\" credit if `reroute_signature` is used) for each HTTP response. Unsuccessful calls will not consume any credits.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.motorscooterdirections_with_http_info(start, end, brand_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[float] start: The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param list[float] end: The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param str brand_id: The ID of the Brand of scooters to use for this route. This is necessary in order to determine the location of available scooters, along with any associated coverage and parking restrictions.  (required)
        :param str ride_state: Indicates where along the Route the user is. If omitted, `walking_to_vehicle` is used. This property along with `current_location` allows the retrieval of an updated Route that reflects the user's current progress through it.  | value | description | | ----- | ----------- | | walking_to_vehicle | Indicates that the user is walking to collect the vehicle | | riding | Indicates that the user is riding the vehicle | | walking_to_end | Indicates that the user has left the vehicle and is walking to their destination | 
        :param str current_location: The user's current location, in order to update the Route based on the user's location. Provided in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  This parameter is used to get an updated Route that reflects the user's actual location if they diverge from the path given in the Route.  If this is provided, the returned Route will contain this location. Which Leg of the Route will contain this location is decided by the value of the `ride_state` parameter. 
        :param str ride_start_location: The location of the vehicle to be used, at the beginning of the vehicle ride part of the user's trip along the Route. Provided in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  This must be provided when `ride_state` is `riding` or `walking_to_end`. If not provided when `ride_state` is `walking_to_vehicle` (or not specified), Citymapper will attempt to find the most appropriate vehicle that belongs to the specified `brand_id`.  For compatibility, `original_vehicle_location` is an alias for this parameter 
        :param str ride_end_location: The location the vehicle was dropped off at the end of the vehicle ride part of the user's trip along the Route. Provided in WGS84 'latitude,longitude' format. Coordinates should  be in decimal, and only the first 6 digits of precision will be used.  This must be provided when `ride_state` is `walking_to_end`. In all other states this parameter is ignored. 
        :param str language: An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language. 
        :param str reroute_signature: When rerouting (requesting an update to a previous response that accounts for the user's updated location), this value should be set to the `signature` provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the `current_location` (when applicable) or `start` location should be set to the user's latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the `end` location is different, or if more than 1 hour has passed since the original request. 
        :param int start_bearing: An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route. 
        :return: DirectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start', 'end', 'brand_id', 'ride_state', 'current_location', 'ride_start_location', 'ride_end_location', 'language', 'reroute_signature', 'start_bearing']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method motorscooterdirections" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'start' is set
        if ('start' not in params or
                params['start'] is None):
            raise ValueError("Missing the required parameter `start` when calling `motorscooterdirections`")  # noqa: E501
        # verify the required parameter 'end' is set
        if ('end' not in params or
                params['end'] is None):
            raise ValueError("Missing the required parameter `end` when calling `motorscooterdirections`")  # noqa: E501
        # verify the required parameter 'brand_id' is set
        if ('brand_id' not in params or
                params['brand_id'] is None):
            raise ValueError("Missing the required parameter `brand_id` when calling `motorscooterdirections`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501
            collection_formats['start'] = 'multi'  # noqa: E501
        if 'end' in params:
            query_params.append(('end', params['end']))  # noqa: E501
            collection_formats['end'] = 'multi'  # noqa: E501
        if 'brand_id' in params:
            query_params.append(('brand_id', params['brand_id']))  # noqa: E501
        if 'ride_state' in params:
            query_params.append(('ride_state', params['ride_state']))  # noqa: E501
        if 'current_location' in params:
            query_params.append(('current_location', params['current_location']))  # noqa: E501
        if 'ride_start_location' in params:
            query_params.append(('ride_start_location', params['ride_start_location']))  # noqa: E501
        if 'ride_end_location' in params:
            query_params.append(('ride_end_location', params['ride_end_location']))  # noqa: E501
        if 'language' in params:
            query_params.append(('language', params['language']))  # noqa: E501
        if 'reroute_signature' in params:
            query_params.append(('reroute_signature', params['reroute_signature']))  # noqa: E501
        if 'start_bearing' in params:
            query_params.append(('start_bearing', params['start_bearing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API Key']  # noqa: E501

        return self.api_client.call_api(
            '/api/1/directions/motorscooter', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DirectionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def motorscooterridedirections(self, start, end, **kwargs):  # noqa: E501
        """Motor scooter directions between two points (ride only)  # noqa: E501

        Gets a motorscooter route between two points, providing enough information to render it on a map, along with a duration estimate. (These results are optimized for larger internal combustion or electric scooters where the rider is seated.)  This call assumes that the rider has a scooter at the `start` point, and provides an e-scooter route from there to the `end` point if both are within Citymapper's supported areas. The resulting route should contain a single scooter leg, though the `path_annotations` property of the Leg may indicate sections during which the user should walk beside the scooter.  This call does not incorporate any information about scooter operators' coverage or parking areas, but other API calls may be available to do so.  Successful responses (HTTP code `200`) will consume one \"Motor Scooter Route\" credit (or one \"Motor Scooter Reroute\" credit if `reroute_signature` is used) for each HTTP response. Unsuccessful calls will not consume any credits.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.motorscooterridedirections(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[float] start: The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param list[float] end: The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param str language: An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language. 
        :param str reroute_signature: When rerouting (requesting an update to a previous response that accounts for the user's updated location), this value should be set to the `signature` provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the `current_location` (when applicable) or `start` location should be set to the user's latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the `end` location is different, or if more than 1 hour has passed since the original request. 
        :param int start_bearing: An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route. 
        :return: DirectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.motorscooterridedirections_with_http_info(start, end, **kwargs)  # noqa: E501
        else:
            (data) = self.motorscooterridedirections_with_http_info(start, end, **kwargs)  # noqa: E501
            return data

    def motorscooterridedirections_with_http_info(self, start, end, **kwargs):  # noqa: E501
        """Motor scooter directions between two points (ride only)  # noqa: E501

        Gets a motorscooter route between two points, providing enough information to render it on a map, along with a duration estimate. (These results are optimized for larger internal combustion or electric scooters where the rider is seated.)  This call assumes that the rider has a scooter at the `start` point, and provides an e-scooter route from there to the `end` point if both are within Citymapper's supported areas. The resulting route should contain a single scooter leg, though the `path_annotations` property of the Leg may indicate sections during which the user should walk beside the scooter.  This call does not incorporate any information about scooter operators' coverage or parking areas, but other API calls may be available to do so.  Successful responses (HTTP code `200`) will consume one \"Motor Scooter Route\" credit (or one \"Motor Scooter Reroute\" credit if `reroute_signature` is used) for each HTTP response. Unsuccessful calls will not consume any credits.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.motorscooterridedirections_with_http_info(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[float] start: The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param list[float] end: The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param str language: An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language. 
        :param str reroute_signature: When rerouting (requesting an update to a previous response that accounts for the user's updated location), this value should be set to the `signature` provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the `current_location` (when applicable) or `start` location should be set to the user's latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the `end` location is different, or if more than 1 hour has passed since the original request. 
        :param int start_bearing: An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route. 
        :return: DirectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start', 'end', 'language', 'reroute_signature', 'start_bearing']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method motorscooterridedirections" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'start' is set
        if ('start' not in params or
                params['start'] is None):
            raise ValueError("Missing the required parameter `start` when calling `motorscooterridedirections`")  # noqa: E501
        # verify the required parameter 'end' is set
        if ('end' not in params or
                params['end'] is None):
            raise ValueError("Missing the required parameter `end` when calling `motorscooterridedirections`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501
            collection_formats['start'] = 'multi'  # noqa: E501
        if 'end' in params:
            query_params.append(('end', params['end']))  # noqa: E501
            collection_formats['end'] = 'multi'  # noqa: E501
        if 'language' in params:
            query_params.append(('language', params['language']))  # noqa: E501
        if 'reroute_signature' in params:
            query_params.append(('reroute_signature', params['reroute_signature']))  # noqa: E501
        if 'start_bearing' in params:
            query_params.append(('start_bearing', params['start_bearing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API Key']  # noqa: E501

        return self.api_client.call_api(
            '/api/1/directions/motorscooterride', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DirectionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def scenariodirections(self, scenario_id, start, end, **kwargs):  # noqa: E501
        """Scenario based directions between two points  # noqa: E501

        **NOTE** This API requires the use of a Scenario ID to select the routing scenario used to determine the type and properties of Routes returned from this endpoint. Please contact Citymapper using the details provided at the top of the page for information on integrating and using this API.  Computes Routes between two points based on a provided scenario.  One or more groups of routes can be provided depending on a scenario. Each group will contain several Routes. Each Route will contain one or more Legs.  Successful responses (HTTP code `200`) will consume \"Scenario Route\" credits depending on a provided scenario and may vary. Unsuccessful calls will not consume any credits.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scenariodirections(scenario_id, start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scenario_id: Scenario ID for directions. (required)
        :param list[float] start: The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param list[float] end: The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param str time: The time to be used as a departure or arrival time constraint when getting directions.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone. For example, `2020-08-19T08:10:42-04:00` expresses August 19, 2020 at 8:10am in Eastern Daylight Time. 
        :param str time_type: When a `time` value is given, this determines how the time will be used to constrain the directions that are returned. When this isn't specified, `depart_approximate` is used.  If no `time` is given, this has no effect.  | value | description | | ----- | ----------- | | arrive | Directions are chosen that get the user to their destination on or before `time` | | depart | Directions are chosen assuming the user leaves their origin as soon after `time` as possible | | depart_approximate | Similar to `depart`, but allowing for later departures in order to return more preferable options even if they leave a bit later. This is Citymapper's default way of choosing directions when the time isn't specified | 
        :param str language: An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language. 
        :return: DirectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.scenariodirections_with_http_info(scenario_id, start, end, **kwargs)  # noqa: E501
        else:
            (data) = self.scenariodirections_with_http_info(scenario_id, start, end, **kwargs)  # noqa: E501
            return data

    def scenariodirections_with_http_info(self, scenario_id, start, end, **kwargs):  # noqa: E501
        """Scenario based directions between two points  # noqa: E501

        **NOTE** This API requires the use of a Scenario ID to select the routing scenario used to determine the type and properties of Routes returned from this endpoint. Please contact Citymapper using the details provided at the top of the page for information on integrating and using this API.  Computes Routes between two points based on a provided scenario.  One or more groups of routes can be provided depending on a scenario. Each group will contain several Routes. Each Route will contain one or more Legs.  Successful responses (HTTP code `200`) will consume \"Scenario Route\" credits depending on a provided scenario and may vary. Unsuccessful calls will not consume any credits.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scenariodirections_with_http_info(scenario_id, start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scenario_id: Scenario ID for directions. (required)
        :param list[float] start: The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param list[float] end: The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param str time: The time to be used as a departure or arrival time constraint when getting directions.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone. For example, `2020-08-19T08:10:42-04:00` expresses August 19, 2020 at 8:10am in Eastern Daylight Time. 
        :param str time_type: When a `time` value is given, this determines how the time will be used to constrain the directions that are returned. When this isn't specified, `depart_approximate` is used.  If no `time` is given, this has no effect.  | value | description | | ----- | ----------- | | arrive | Directions are chosen that get the user to their destination on or before `time` | | depart | Directions are chosen assuming the user leaves their origin as soon after `time` as possible | | depart_approximate | Similar to `depart`, but allowing for later departures in order to return more preferable options even if they leave a bit later. This is Citymapper's default way of choosing directions when the time isn't specified | 
        :param str language: An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language. 
        :return: DirectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scenario_id', 'start', 'end', 'time', 'time_type', 'language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scenariodirections" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scenario_id' is set
        if ('scenario_id' not in params or
                params['scenario_id'] is None):
            raise ValueError("Missing the required parameter `scenario_id` when calling `scenariodirections`")  # noqa: E501
        # verify the required parameter 'start' is set
        if ('start' not in params or
                params['start'] is None):
            raise ValueError("Missing the required parameter `start` when calling `scenariodirections`")  # noqa: E501
        # verify the required parameter 'end' is set
        if ('end' not in params or
                params['end'] is None):
            raise ValueError("Missing the required parameter `end` when calling `scenariodirections`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'scenario_id' in params:
            query_params.append(('scenario_id', params['scenario_id']))  # noqa: E501
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501
            collection_formats['start'] = 'multi'  # noqa: E501
        if 'end' in params:
            query_params.append(('end', params['end']))  # noqa: E501
            collection_formats['end'] = 'multi'  # noqa: E501
        if 'time' in params:
            query_params.append(('time', params['time']))  # noqa: E501
        if 'time_type' in params:
            query_params.append(('time_type', params['time_type']))  # noqa: E501
        if 'language' in params:
            query_params.append(('language', params['language']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API Key']  # noqa: E501

        return self.api_client.call_api(
            '/api/1/directions/scenario', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DirectionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def scooterdirections(self, start, end, brand_id, **kwargs):  # noqa: E501
        """E-scooter directions between two points (hire vehicles)  # noqa: E501

        **NOTE this API is not available through open access, please contact sales**. Please contact Citymapper using the details provided at the top of the page for information on integrating and using this API.  Gets an e-scooter route between two points, including any initial and final walks. The resulting Route provides enough information to render it on a map, along with a duration estimate. These results are optimized for small battery-powered scooters that the rider stands on.  This call can be used in several different ways:    **Use any scooter of the specified Brand**  This is the simplest call, only requiring `start`, `end`, and `brand_id`. Citymapper assumes that the user is at the `start` point, and chooses a scooter of the specified Brand, if possible.  **Use a scooter at a specified location**  By adding `original_vehicle_location` to `start`, `end`, and `brand_id`, Citymapper plans a Route that assumes the scooter is at the given location.  **Update a Route in progress**  In order to retrieve an updated Route that includes rerouting from the user's current location if they've diverged from the planned Route, the caller can add the `current_location` and `ride_state` properties, which indicates which Leg of the resulting Route should be rerouted around the user's `current_location`.  Successful responses (HTTP code `200`) will consume one \"Scooter Route\" credit (or one \"Scooter Reroute\" credit if `reroute_signature` is used) for each HTTP response. Unsuccessful calls will not consume any credits.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scooterdirections(start, end, brand_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[float] start: The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param list[float] end: The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param str brand_id: The ID of the Brand of e-scooters to use for this route. This is necessary in order to determine the location of available scooters, along with any associated coverage and parking restrictions.  (required)
        :param str ride_state: Indicates where along the Route the user is. If omitted, `walking_to_vehicle` is used. This property along with `current_location` allows the retrieval of an updated Route that reflects the user's current progress through it.  | value | description | | ----- | ----------- | | walking_to_vehicle | Indicates that the user is walking to collect the vehicle | | riding | Indicates that the user is riding the vehicle | | walking_to_end | Indicates that the user has left the vehicle and is walking to their destination | 
        :param str current_location: The user's current location, in order to update the Route based on the user's location. Provided in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  This parameter is used to get an updated Route that reflects the user's actual location if they diverge from the path given in the Route.  If this is provided, the returned Route will contain this location. Which Leg of the Route will contain this location is decided by the value of the `ride_state` parameter. 
        :param str ride_start_location: The location of the vehicle to be used, at the beginning of the vehicle ride part of the user's trip along the Route. Provided in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  This must be provided when `ride_state` is `riding` or `walking_to_end`. If not provided when `ride_state` is `walking_to_vehicle` (or not specified), Citymapper will attempt to find the most appropriate vehicle that belongs to the specified `brand_id`.  For compatibility, `original_vehicle_location` is an alias for this parameter 
        :param str ride_end_location: The location the vehicle was dropped off at the end of the vehicle ride part of the user's trip along the Route. Provided in WGS84 'latitude,longitude' format. Coordinates should  be in decimal, and only the first 6 digits of precision will be used.  This must be provided when `ride_state` is `walking_to_end`. In all other states this parameter is ignored. 
        :param str language: An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language. 
        :param str reroute_signature: When rerouting (requesting an update to a previous response that accounts for the user's updated location), this value should be set to the `signature` provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the `current_location` (when applicable) or `start` location should be set to the user's latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the `end` location is different, or if more than 1 hour has passed since the original request. 
        :param int start_bearing: An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route. 
        :return: DirectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.scooterdirections_with_http_info(start, end, brand_id, **kwargs)  # noqa: E501
        else:
            (data) = self.scooterdirections_with_http_info(start, end, brand_id, **kwargs)  # noqa: E501
            return data

    def scooterdirections_with_http_info(self, start, end, brand_id, **kwargs):  # noqa: E501
        """E-scooter directions between two points (hire vehicles)  # noqa: E501

        **NOTE this API is not available through open access, please contact sales**. Please contact Citymapper using the details provided at the top of the page for information on integrating and using this API.  Gets an e-scooter route between two points, including any initial and final walks. The resulting Route provides enough information to render it on a map, along with a duration estimate. These results are optimized for small battery-powered scooters that the rider stands on.  This call can be used in several different ways:    **Use any scooter of the specified Brand**  This is the simplest call, only requiring `start`, `end`, and `brand_id`. Citymapper assumes that the user is at the `start` point, and chooses a scooter of the specified Brand, if possible.  **Use a scooter at a specified location**  By adding `original_vehicle_location` to `start`, `end`, and `brand_id`, Citymapper plans a Route that assumes the scooter is at the given location.  **Update a Route in progress**  In order to retrieve an updated Route that includes rerouting from the user's current location if they've diverged from the planned Route, the caller can add the `current_location` and `ride_state` properties, which indicates which Leg of the resulting Route should be rerouted around the user's `current_location`.  Successful responses (HTTP code `200`) will consume one \"Scooter Route\" credit (or one \"Scooter Reroute\" credit if `reroute_signature` is used) for each HTTP response. Unsuccessful calls will not consume any credits.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scooterdirections_with_http_info(start, end, brand_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[float] start: The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param list[float] end: The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param str brand_id: The ID of the Brand of e-scooters to use for this route. This is necessary in order to determine the location of available scooters, along with any associated coverage and parking restrictions.  (required)
        :param str ride_state: Indicates where along the Route the user is. If omitted, `walking_to_vehicle` is used. This property along with `current_location` allows the retrieval of an updated Route that reflects the user's current progress through it.  | value | description | | ----- | ----------- | | walking_to_vehicle | Indicates that the user is walking to collect the vehicle | | riding | Indicates that the user is riding the vehicle | | walking_to_end | Indicates that the user has left the vehicle and is walking to their destination | 
        :param str current_location: The user's current location, in order to update the Route based on the user's location. Provided in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  This parameter is used to get an updated Route that reflects the user's actual location if they diverge from the path given in the Route.  If this is provided, the returned Route will contain this location. Which Leg of the Route will contain this location is decided by the value of the `ride_state` parameter. 
        :param str ride_start_location: The location of the vehicle to be used, at the beginning of the vehicle ride part of the user's trip along the Route. Provided in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  This must be provided when `ride_state` is `riding` or `walking_to_end`. If not provided when `ride_state` is `walking_to_vehicle` (or not specified), Citymapper will attempt to find the most appropriate vehicle that belongs to the specified `brand_id`.  For compatibility, `original_vehicle_location` is an alias for this parameter 
        :param str ride_end_location: The location the vehicle was dropped off at the end of the vehicle ride part of the user's trip along the Route. Provided in WGS84 'latitude,longitude' format. Coordinates should  be in decimal, and only the first 6 digits of precision will be used.  This must be provided when `ride_state` is `walking_to_end`. In all other states this parameter is ignored. 
        :param str language: An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language. 
        :param str reroute_signature: When rerouting (requesting an update to a previous response that accounts for the user's updated location), this value should be set to the `signature` provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the `current_location` (when applicable) or `start` location should be set to the user's latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the `end` location is different, or if more than 1 hour has passed since the original request. 
        :param int start_bearing: An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route. 
        :return: DirectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start', 'end', 'brand_id', 'ride_state', 'current_location', 'ride_start_location', 'ride_end_location', 'language', 'reroute_signature', 'start_bearing']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scooterdirections" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'start' is set
        if ('start' not in params or
                params['start'] is None):
            raise ValueError("Missing the required parameter `start` when calling `scooterdirections`")  # noqa: E501
        # verify the required parameter 'end' is set
        if ('end' not in params or
                params['end'] is None):
            raise ValueError("Missing the required parameter `end` when calling `scooterdirections`")  # noqa: E501
        # verify the required parameter 'brand_id' is set
        if ('brand_id' not in params or
                params['brand_id'] is None):
            raise ValueError("Missing the required parameter `brand_id` when calling `scooterdirections`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501
            collection_formats['start'] = 'multi'  # noqa: E501
        if 'end' in params:
            query_params.append(('end', params['end']))  # noqa: E501
            collection_formats['end'] = 'multi'  # noqa: E501
        if 'brand_id' in params:
            query_params.append(('brand_id', params['brand_id']))  # noqa: E501
        if 'ride_state' in params:
            query_params.append(('ride_state', params['ride_state']))  # noqa: E501
        if 'current_location' in params:
            query_params.append(('current_location', params['current_location']))  # noqa: E501
        if 'ride_start_location' in params:
            query_params.append(('ride_start_location', params['ride_start_location']))  # noqa: E501
        if 'ride_end_location' in params:
            query_params.append(('ride_end_location', params['ride_end_location']))  # noqa: E501
        if 'language' in params:
            query_params.append(('language', params['language']))  # noqa: E501
        if 'reroute_signature' in params:
            query_params.append(('reroute_signature', params['reroute_signature']))  # noqa: E501
        if 'start_bearing' in params:
            query_params.append(('start_bearing', params['start_bearing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API Key']  # noqa: E501

        return self.api_client.call_api(
            '/api/1/directions/scooter', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DirectionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def scooterridedirections(self, start, end, **kwargs):  # noqa: E501
        """E-scooter directions between two points (ride only)  # noqa: E501

        Gets a scooter route between two points, providing enough information to render it on a map, along with a duration estimate. (These results are optimized for small battery-powered scooters that the rider stands on.)  This call assumes that the rider has a scooter at the `start` point, and provides an e-scooter route from there to the `end` point if both are within Citymapper's supported areas. The resulting route should contain a single scooter leg, though the `path_annotations` property of the Leg may indicate sections during which the user should walk beside the scooter.  This call does not incorporate any information about scooter operators' coverage or parking areas, but other API calls may be available to do so.  Successful responses (HTTP code `200`) will consume one \"Scooter Route\" credit (or one \"Scooter Reroute\" credit if `reroute_signature` is used) for each HTTP response. Unsuccessful calls will not consume any credits.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scooterridedirections(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[float] start: The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param list[float] end: The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param str language: An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language. 
        :param str reroute_signature: When rerouting (requesting an update to a previous response that accounts for the user's updated location), this value should be set to the `signature` provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the `current_location` (when applicable) or `start` location should be set to the user's latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the `end` location is different, or if more than 1 hour has passed since the original request. 
        :param int start_bearing: An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route. 
        :return: DirectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.scooterridedirections_with_http_info(start, end, **kwargs)  # noqa: E501
        else:
            (data) = self.scooterridedirections_with_http_info(start, end, **kwargs)  # noqa: E501
            return data

    def scooterridedirections_with_http_info(self, start, end, **kwargs):  # noqa: E501
        """E-scooter directions between two points (ride only)  # noqa: E501

        Gets a scooter route between two points, providing enough information to render it on a map, along with a duration estimate. (These results are optimized for small battery-powered scooters that the rider stands on.)  This call assumes that the rider has a scooter at the `start` point, and provides an e-scooter route from there to the `end` point if both are within Citymapper's supported areas. The resulting route should contain a single scooter leg, though the `path_annotations` property of the Leg may indicate sections during which the user should walk beside the scooter.  This call does not incorporate any information about scooter operators' coverage or parking areas, but other API calls may be available to do so.  Successful responses (HTTP code `200`) will consume one \"Scooter Route\" credit (or one \"Scooter Reroute\" credit if `reroute_signature` is used) for each HTTP response. Unsuccessful calls will not consume any credits.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scooterridedirections_with_http_info(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[float] start: The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param list[float] end: The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param str language: An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language. 
        :param str reroute_signature: When rerouting (requesting an update to a previous response that accounts for the user's updated location), this value should be set to the `signature` provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the `current_location` (when applicable) or `start` location should be set to the user's latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the `end` location is different, or if more than 1 hour has passed since the original request. 
        :param int start_bearing: An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route. 
        :return: DirectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start', 'end', 'language', 'reroute_signature', 'start_bearing']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scooterridedirections" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'start' is set
        if ('start' not in params or
                params['start'] is None):
            raise ValueError("Missing the required parameter `start` when calling `scooterridedirections`")  # noqa: E501
        # verify the required parameter 'end' is set
        if ('end' not in params or
                params['end'] is None):
            raise ValueError("Missing the required parameter `end` when calling `scooterridedirections`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501
            collection_formats['start'] = 'multi'  # noqa: E501
        if 'end' in params:
            query_params.append(('end', params['end']))  # noqa: E501
            collection_formats['end'] = 'multi'  # noqa: E501
        if 'language' in params:
            query_params.append(('language', params['language']))  # noqa: E501
        if 'reroute_signature' in params:
            query_params.append(('reroute_signature', params['reroute_signature']))  # noqa: E501
        if 'start_bearing' in params:
            query_params.append(('start_bearing', params['start_bearing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API Key']  # noqa: E501

        return self.api_client.call_api(
            '/api/1/directions/scooterride', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DirectionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def transitdirections(self, start, end, **kwargs):  # noqa: E501
        """Transit directions between two points  # noqa: E501

        Computes several public transportation routes between two points.  By default, the results will contain up to 5 Routes. Each one will contain several Legs: usually one at the start and end of the Route with `travel_mode` of `walk`, with at least one with `travel_mode` of `transit` in between.  Successful responses (HTTP code `200`) will consume one \"Transit Route\" credit for each HTTP response. Unsuccessful calls will not consume any credits.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transitdirections(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[float] start: The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param list[float] end: The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param str time: The time to be used as a departure or arrival time constraint when getting directions.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone. For example, `2020-08-19T08:10:42-04:00` expresses August 19, 2020 at 8:10am in Eastern Daylight Time. 
        :param str time_type: When a `time` value is given, this determines how the time will be used to constrain the directions that are returned. When this isn't specified, `depart_approximate` is used.  If no `time` is given, this has no effect.  | value | description | | ----- | ----------- | | arrive | Directions are chosen that get the user to their destination on or before `time` | | depart | Directions are chosen assuming the user leaves their origin as soon after `time` as possible | | depart_approximate | Similar to `depart`, but allowing for later departures in order to return more preferable options even if they leave a bit later. This is Citymapper's default way of choosing directions when the time isn't specified | 
        :param str language: An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language. 
        :param int limit: Maximum number of Routes to return.
        :return: DirectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.transitdirections_with_http_info(start, end, **kwargs)  # noqa: E501
        else:
            (data) = self.transitdirections_with_http_info(start, end, **kwargs)  # noqa: E501
            return data

    def transitdirections_with_http_info(self, start, end, **kwargs):  # noqa: E501
        """Transit directions between two points  # noqa: E501

        Computes several public transportation routes between two points.  By default, the results will contain up to 5 Routes. Each one will contain several Legs: usually one at the start and end of the Route with `travel_mode` of `walk`, with at least one with `travel_mode` of `transit` in between.  Successful responses (HTTP code `200`) will consume one \"Transit Route\" credit for each HTTP response. Unsuccessful calls will not consume any credits.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transitdirections_with_http_info(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[float] start: The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param list[float] end: The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param str time: The time to be used as a departure or arrival time constraint when getting directions.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone. For example, `2020-08-19T08:10:42-04:00` expresses August 19, 2020 at 8:10am in Eastern Daylight Time. 
        :param str time_type: When a `time` value is given, this determines how the time will be used to constrain the directions that are returned. When this isn't specified, `depart_approximate` is used.  If no `time` is given, this has no effect.  | value | description | | ----- | ----------- | | arrive | Directions are chosen that get the user to their destination on or before `time` | | depart | Directions are chosen assuming the user leaves their origin as soon after `time` as possible | | depart_approximate | Similar to `depart`, but allowing for later departures in order to return more preferable options even if they leave a bit later. This is Citymapper's default way of choosing directions when the time isn't specified | 
        :param str language: An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language. 
        :param int limit: Maximum number of Routes to return.
        :return: DirectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start', 'end', 'time', 'time_type', 'language', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transitdirections" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'start' is set
        if ('start' not in params or
                params['start'] is None):
            raise ValueError("Missing the required parameter `start` when calling `transitdirections`")  # noqa: E501
        # verify the required parameter 'end' is set
        if ('end' not in params or
                params['end'] is None):
            raise ValueError("Missing the required parameter `end` when calling `transitdirections`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501
            collection_formats['start'] = 'multi'  # noqa: E501
        if 'end' in params:
            query_params.append(('end', params['end']))  # noqa: E501
            collection_formats['end'] = 'multi'  # noqa: E501
        if 'time' in params:
            query_params.append(('time', params['time']))  # noqa: E501
        if 'time_type' in params:
            query_params.append(('time_type', params['time_type']))  # noqa: E501
        if 'language' in params:
            query_params.append(('language', params['language']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API Key']  # noqa: E501

        return self.api_client.call_api(
            '/api/1/directions/transit', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DirectionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def traveltime(self, start, end, **kwargs):  # noqa: E501
        """Travel times between two locations  # noqa: E501

        Determines the travel time in various modes of travel between the given two points at the time the request is made. If the call returns code `200`, at least one of the `*_time_minutes` fields will be populated. Otherwise, a code `400` response will be returned.  A request outside of the API coverage areas will be signaled with a code `400` response containing an `error_code` value of `coverage-start` or `coverage-end`. These failures are fast/resource-efficient and are not billed, so there's no need to pre-filter potential requests by location.  Successful responses (HTTP code `200`) will consume one \"Travel Time\" credit for each time returned. Unsuccessful calls will not consume any credits.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.traveltime(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start: The geographical start point of the trip, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  (required)
        :param str end: The geographical end point of the trip, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  (required)
        :param list[str] traveltime_types: A comma-separated list of different travel time types to attempt to request. Each request value corresponds to a particular field in the response (response fields will only be present when Citymapper was able to calculate a time for that travel time type).  | value | response property | description | | ----- | ----------------- | ------------| | walk | walk_travel_time_minutes | Walking | | transit | transit_time_minutes | Public transit travel | | bike | bike_time_minutes | Bicycle travel (riding the entire way) | | scooter | scooter_time_minutes | Standing e-scooter travel (riding the entire way) | | motorscooter | motorscooter_time_minutes | Seated motor scooter travel (riding the entire way) |  When this field is omitted or empty, a default value of `walk,transit` will be used. 
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.traveltime_with_http_info(start, end, **kwargs)  # noqa: E501
        else:
            (data) = self.traveltime_with_http_info(start, end, **kwargs)  # noqa: E501
            return data

    def traveltime_with_http_info(self, start, end, **kwargs):  # noqa: E501
        """Travel times between two locations  # noqa: E501

        Determines the travel time in various modes of travel between the given two points at the time the request is made. If the call returns code `200`, at least one of the `*_time_minutes` fields will be populated. Otherwise, a code `400` response will be returned.  A request outside of the API coverage areas will be signaled with a code `400` response containing an `error_code` value of `coverage-start` or `coverage-end`. These failures are fast/resource-efficient and are not billed, so there's no need to pre-filter potential requests by location.  Successful responses (HTTP code `200`) will consume one \"Travel Time\" credit for each time returned. Unsuccessful calls will not consume any credits.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.traveltime_with_http_info(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start: The geographical start point of the trip, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  (required)
        :param str end: The geographical end point of the trip, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 digits of precision will be used.  (required)
        :param list[str] traveltime_types: A comma-separated list of different travel time types to attempt to request. Each request value corresponds to a particular field in the response (response fields will only be present when Citymapper was able to calculate a time for that travel time type).  | value | response property | description | | ----- | ----------------- | ------------| | walk | walk_travel_time_minutes | Walking | | transit | transit_time_minutes | Public transit travel | | bike | bike_time_minutes | Bicycle travel (riding the entire way) | | scooter | scooter_time_minutes | Standing e-scooter travel (riding the entire way) | | motorscooter | motorscooter_time_minutes | Seated motor scooter travel (riding the entire way) |  When this field is omitted or empty, a default value of `walk,transit` will be used. 
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start', 'end', 'traveltime_types']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method traveltime" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'start' is set
        if ('start' not in params or
                params['start'] is None):
            raise ValueError("Missing the required parameter `start` when calling `traveltime`")  # noqa: E501
        # verify the required parameter 'end' is set
        if ('end' not in params or
                params['end'] is None):
            raise ValueError("Missing the required parameter `end` when calling `traveltime`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501
        if 'end' in params:
            query_params.append(('end', params['end']))  # noqa: E501
        if 'traveltime_types' in params:
            query_params.append(('traveltime_types', params['traveltime_types']))  # noqa: E501
            collection_formats['traveltime_types'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API Key']  # noqa: E501

        return self.api_client.call_api(
            '/api/1/traveltimes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def walkdirections(self, start, end, **kwargs):  # noqa: E501
        """Walking directions between two points  # noqa: E501

        Gets a walking route between two points, providing enough information to render it on a map, along with a duration estimate.  Walking routes are expected to have a single Leg with a `travel_mode` of `walk`.  If Citymapper can't compute walking directions for those points (generally for coverage reasons), the API will return a code `400` response.  The maximum great-circle distance between the `start` and `end` is limited to 100km for this API.  Successful responses (HTTP code `200`) will consume one \"Walk Route\" credit (or one \"Walk Reroute\" credit if `reroute_signature` is used) for each HTTP response. Unsuccessful calls will not consume any credits.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.walkdirections(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[float] start: The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param list[float] end: The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param str language: An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language. 
        :param str profiles: Indicates which \"profiles\" to use when calculating walking directions. Each profile can generate a different Route option, so requesting more profiles will generally give more options. Note that sometimes some of the resulting Routes will be identical (in the case of one route being optimal in more than one way), and a profile may not always yield a Route.  Not all profiles will be available for all start and end routes. Unavailable profiles will be omitted from the response.  | value | description | | ----- | ----------- | | fast | The default profile, attempts to find the fastest sensible Route | | main_roads | Attempts to avoid backstreets and parks |  If no profiles are specified, `fast` will be used. 
        :param str reroute_signature: When rerouting (requesting an update to a previous response that accounts for the user's updated location), this value should be set to the `signature` provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the `current_location` (when applicable) or `start` location should be set to the user's latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the `end` location is different, or if more than 1 hour has passed since the original request. 
        :param int start_bearing: An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route. 
        :return: DirectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.walkdirections_with_http_info(start, end, **kwargs)  # noqa: E501
        else:
            (data) = self.walkdirections_with_http_info(start, end, **kwargs)  # noqa: E501
            return data

    def walkdirections_with_http_info(self, start, end, **kwargs):  # noqa: E501
        """Walking directions between two points  # noqa: E501

        Gets a walking route between two points, providing enough information to render it on a map, along with a duration estimate.  Walking routes are expected to have a single Leg with a `travel_mode` of `walk`.  If Citymapper can't compute walking directions for those points (generally for coverage reasons), the API will return a code `400` response.  The maximum great-circle distance between the `start` and `end` is limited to 100km for this API.  Successful responses (HTTP code `200`) will consume one \"Walk Route\" credit (or one \"Walk Reroute\" credit if `reroute_signature` is used) for each HTTP response. Unsuccessful calls will not consume any credits.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.walkdirections_with_http_info(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[float] start: The geographical start of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param list[float] end: The geographical end of the route, in WGS84 'latitude,longitude' format. Coordinates should be in decimal, and only the first 6 decimal places will be used. (required)
        :param str language: An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates the end-user's language preference.    When provided, the response will contain a `language` property that indicates the language used for any localizable elements of the response (such as turning instructions). This language will be a best-effort attempt to fulfill the expressed preference, but it may contain a value that wasn't expressed in the request (this will generally be `en-US` as a fallback).  Note that language preference will generally only affect Citymapper-generated content such as turning instructions. External content such as Stop names and Status descriptions will generally be passed through in their original language. 
        :param str profiles: Indicates which \"profiles\" to use when calculating walking directions. Each profile can generate a different Route option, so requesting more profiles will generally give more options. Note that sometimes some of the resulting Routes will be identical (in the case of one route being optimal in more than one way), and a profile may not always yield a Route.  Not all profiles will be available for all start and end routes. Unavailable profiles will be omitted from the response.  | value | description | | ----- | ----------- | | fast | The default profile, attempts to find the fastest sensible Route | | main_roads | Attempts to avoid backstreets and parks |  If no profiles are specified, `fast` will be used. 
        :param str reroute_signature: When rerouting (requesting an update to a previous response that accounts for the user's updated location), this value should be set to the `signature` provided in the original Route. This allows for more efficient determination of the updated Route.  This value must be URL-encoded.  When providing this parameter, the `current_location` (when applicable) or `start` location should be set to the user's latest location.  When this parameter is included, Citymapper may not return results in cases where the request differs significantly from the original, for instance if the `end` location is different, or if more than 1 hour has passed since the original request. 
        :param int start_bearing: An angle clockwise from North between 0 and 359, where North is 0 and East is 90.  This bearing is used to influence the initial instruction text and/or routing, most-commonly to avoid the user from being asked to make a u-turn, if continuing on their current bearing gives a comparable route.  This should be provided only if you wish to influence the initial direction of travel for the route. 
        :return: DirectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start', 'end', 'language', 'profiles', 'reroute_signature', 'start_bearing']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method walkdirections" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'start' is set
        if ('start' not in params or
                params['start'] is None):
            raise ValueError("Missing the required parameter `start` when calling `walkdirections`")  # noqa: E501
        # verify the required parameter 'end' is set
        if ('end' not in params or
                params['end'] is None):
            raise ValueError("Missing the required parameter `end` when calling `walkdirections`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501
            collection_formats['start'] = 'multi'  # noqa: E501
        if 'end' in params:
            query_params.append(('end', params['end']))  # noqa: E501
            collection_formats['end'] = 'multi'  # noqa: E501
        if 'language' in params:
            query_params.append(('language', params['language']))  # noqa: E501
        if 'profiles' in params:
            query_params.append(('profiles', params['profiles']))  # noqa: E501
        if 'reroute_signature' in params:
            query_params.append(('reroute_signature', params['reroute_signature']))  # noqa: E501
        if 'start_bearing' in params:
            query_params.append(('start_bearing', params['start_bearing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API Key']  # noqa: E501

        return self.api_client.call_api(
            '/api/1/directions/walk', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DirectionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
