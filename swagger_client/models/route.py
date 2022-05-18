# coding: utf-8

"""
    Citymapper API

    # Introduction  ### Add journey planning and turn-by-turn navigation to your products with our APIs.  Our APIs are powered by our industry-leading global transport data and custom routing algorithms trained on billions of trips.  With our journey planning APIs you can:  - Calculate public transport routes and travel times - Retrieve live departure information for public transport routes - Calculate walk, cycling, e-scooter and motor scooter routes and travel times, including turn-by-turn instructions  Developing a mobile app? See our iOS and Android SDK [here](/).  <div class=\"cta\">  Ready to start?  <a class=\"button\" href=\"https://enterprise.citymapper.com/signup\">Get Access&ensp;&rarr;</a>  </div>  &nbsp;  ### Other resources  [SDK Docs](/)  [Deep Links](https://citymapper.com/news/2386/launch-citymapper-for-directions)  [Learn more about Powered by Citymapper](https://citymapper.com/enterprise)  # Support  ### Have questions?  Check out our FAQ [here](/support/faq.html).  ### Have product feedback or suggestions?  We'd love to hear about your experiences using our APIs, and features you'd like to see next. Please contribute feedback [here](https://form.jotform.com/213393057055353), and keep an eye out for future product releases.  ### Have a sales question?  If you are an enterprise user, or require functionality not available in our public APIs, our sales team are here to help.  Please [contact us](https://citymapper.com/contact/powered) with a description of your project or business need and we'll be in touch.  # Pricing  ### Get started for free  Get 5,000 monthly [requests](#requests) for free across all our products, making it easy to start building with our API or SDK.  <div class=\"cta\">  <a class=\"button\" href=\"https://enterprise.citymapper.com/signup\">Sign up&ensp;&rarr;</a>  </div>  &nbsp;  ### **Pay as you go**  Ready to launch? Scale quickly and flexibly with our pay-as-you-go plan.  Pick the products you need and only get charged for what you use – plus enjoy £100 free credit allowance from us each month.  To switch to the pay-as-you-go plan, please visit the [enterprise dashboard](https://enterprise.citymapper.com) and add a payment method. It’s that simple.  See below for our API pricing:  | Travel Time API           | Unit             | Price per Unit | | ------------------------- | ---------------- | -------------- | | Walk Travel Time          | per 1000 results | £0.40          | | Cycle Travel Time         | per 1000 results | £0.80          | | E-Scooter Travel Time     | per 1000 results | £0.80          | | Motor Scooter Travel Time | per 1000 results | £0.80          | | Transit Travel Time       | per 1000 results | £1.00          |  | Directions API                        | Unit                       | Price per Unit                     | | ------------------------------------- | -------------------------- | ---------------------------------- | | Walk Directions: Fast Profile         | per 1000 results           | £0.50                              | | Walk Directions: Main Roads Profile   | per 1000 results           | £0.50                              | | Cycle Directions: Quiet Profile       | per 1000 results           | £1.00                              | | Cycle Directions: Regular Profile     | per 1000 results           | £1.00                              | | Cycle Directions: Fast Profile        | per 1000 results           | £1.00                              | | E-Scooter Directions                  | per 1000 results           | £1.00                              | | Motor Scooter Directions              | per 1000 results           | £1.00                              | | Transit Directions                    | per 1000 routes\\*          | £1.20                              | | Transit Directions: Real-Time Updates | per 1000 route updates\\*\\* | Available on Enterprise plans only | | Hire Vehicle Directions               | per 1000 results           | Available on Enterprise plans only |  \\* Up to 5 transit routes can be returned in a single result  \\*\\* One update applies to a single transit route. Updates are refreshed every minute  ### Enterprise plans to help you grow  Looking for additional features or have higher volume requirements? Please [contact our sales team](https://citymapper.com/contact/powered).  ### Terms of service  Read the full [terms of service](https://citymapper.com/developer-terms).  ### Requests  A request is defined as a single call which successfully returns a travel time, directions or navigation result. Monthly requests are aggregated across all Powered by Citymapper products. If you're not on a paid plan, you’ll be notified via email once you exceed the free usage allowance in a given month (the month-long period aligns with the calendar month). Further requests will no longer return results for the remainder of that month, and your free usage allowance will reset at the start of the next month.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    OpenAPI spec version: v1.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Route(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'start': 'Waypoint',
        'end': 'Waypoint',
        'distance_meters': 'int',
        'duration_seconds': 'int',
        'duration_accuracy': 'DurationAccuracy',
        'price': 'AllOfRoutePrice',
        'legs': 'list[Leg]',
        'route_departure_time': 'str',
        'route_arrival_time': 'str',
        'route_metadata': 'RouteMetadata',
        'profile': 'str',
        'signature': 'str'
    }

    attribute_map = {
        'start': 'start',
        'end': 'end',
        'distance_meters': 'distance_meters',
        'duration_seconds': 'duration_seconds',
        'duration_accuracy': 'duration_accuracy',
        'price': 'price',
        'legs': 'legs',
        'route_departure_time': 'route_departure_time',
        'route_arrival_time': 'route_arrival_time',
        'route_metadata': 'route_metadata',
        'profile': 'profile',
        'signature': 'signature'
    }

    def __init__(self, start=None, end=None, distance_meters=None, duration_seconds=None, duration_accuracy=None, price=None, legs=None, route_departure_time=None, route_arrival_time=None, route_metadata=None, profile=None, signature=None):  # noqa: E501
        """Route - a model defined in Swagger"""  # noqa: E501
        self._start = None
        self._end = None
        self._distance_meters = None
        self._duration_seconds = None
        self._duration_accuracy = None
        self._price = None
        self._legs = None
        self._route_departure_time = None
        self._route_arrival_time = None
        self._route_metadata = None
        self._profile = None
        self._signature = None
        self.discriminator = None
        self.start = start
        self.end = end
        if distance_meters is not None:
            self.distance_meters = distance_meters
        if duration_seconds is not None:
            self.duration_seconds = duration_seconds
        if duration_accuracy is not None:
            self.duration_accuracy = duration_accuracy
        if price is not None:
            self.price = price
        self.legs = legs
        if route_departure_time is not None:
            self.route_departure_time = route_departure_time
        if route_arrival_time is not None:
            self.route_arrival_time = route_arrival_time
        if route_metadata is not None:
            self.route_metadata = route_metadata
        if profile is not None:
            self.profile = profile
        self.signature = signature

    @property
    def start(self):
        """Gets the start of this Route.  # noqa: E501


        :return: The start of this Route.  # noqa: E501
        :rtype: Waypoint
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this Route.


        :param start: The start of this Route.  # noqa: E501
        :type: Waypoint
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def end(self):
        """Gets the end of this Route.  # noqa: E501


        :return: The end of this Route.  # noqa: E501
        :rtype: Waypoint
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this Route.


        :param end: The end of this Route.  # noqa: E501
        :type: Waypoint
        """
        if end is None:
            raise ValueError("Invalid value for `end`, must not be `None`")  # noqa: E501

        self._end = end

    @property
    def distance_meters(self):
        """Gets the distance_meters of this Route.  # noqa: E501

        The overall distance of the entire Route, in meters.  # noqa: E501

        :return: The distance_meters of this Route.  # noqa: E501
        :rtype: int
        """
        return self._distance_meters

    @distance_meters.setter
    def distance_meters(self, distance_meters):
        """Sets the distance_meters of this Route.

        The overall distance of the entire Route, in meters.  # noqa: E501

        :param distance_meters: The distance_meters of this Route.  # noqa: E501
        :type: int
        """

        self._distance_meters = distance_meters

    @property
    def duration_seconds(self):
        """Gets the duration_seconds of this Route.  # noqa: E501

        The overall estimated time to traverse the entire Route, in seconds, based on the selected vehicle or departure in the response.  # noqa: E501

        :return: The duration_seconds of this Route.  # noqa: E501
        :rtype: int
        """
        return self._duration_seconds

    @duration_seconds.setter
    def duration_seconds(self, duration_seconds):
        """Sets the duration_seconds of this Route.

        The overall estimated time to traverse the entire Route, in seconds, based on the selected vehicle or departure in the response.  # noqa: E501

        :param duration_seconds: The duration_seconds of this Route.  # noqa: E501
        :type: int
        """

        self._duration_seconds = duration_seconds

    @property
    def duration_accuracy(self):
        """Gets the duration_accuracy of this Route.  # noqa: E501


        :return: The duration_accuracy of this Route.  # noqa: E501
        :rtype: DurationAccuracy
        """
        return self._duration_accuracy

    @duration_accuracy.setter
    def duration_accuracy(self, duration_accuracy):
        """Sets the duration_accuracy of this Route.


        :param duration_accuracy: The duration_accuracy of this Route.  # noqa: E501
        :type: DurationAccuracy
        """

        self._duration_accuracy = duration_accuracy

    @property
    def price(self):
        """Gets the price of this Route.  # noqa: E501

        The price to take the Route. Omitted when not available. Generally available only on transit Routes. The price is computed assuming no special passes, with the user paying with cash or the most common fare instrument.  # noqa: E501

        :return: The price of this Route.  # noqa: E501
        :rtype: AllOfRoutePrice
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Route.

        The price to take the Route. Omitted when not available. Generally available only on transit Routes. The price is computed assuming no special passes, with the user paying with cash or the most common fare instrument.  # noqa: E501

        :param price: The price of this Route.  # noqa: E501
        :type: AllOfRoutePrice
        """

        self._price = price

    @property
    def legs(self):
        """Gets the legs of this Route.  # noqa: E501

        Array of Legs comprising the Route, in the order in which they should be traversed. Every valid Route will have at least one.  # noqa: E501

        :return: The legs of this Route.  # noqa: E501
        :rtype: list[Leg]
        """
        return self._legs

    @legs.setter
    def legs(self, legs):
        """Sets the legs of this Route.

        Array of Legs comprising the Route, in the order in which they should be traversed. Every valid Route will have at least one.  # noqa: E501

        :param legs: The legs of this Route.  # noqa: E501
        :type: list[Leg]
        """
        if legs is None:
            raise ValueError("Invalid value for `legs`, must not be `None`")  # noqa: E501

        self._legs = legs

    @property
    def route_departure_time(self):
        """Gets the route_departure_time of this Route.  # noqa: E501

        The time at which Citymapper thinks the user will set out on this route, given available departure information. This is computed assuming that user is at the start of the route.  Updated values for `route_departure_time` and `route_arrival_time` are returned by `/api/1/live/routeupdates` to reflect any updated departure information.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone in which the event occurs. For example, `2020-08-19T08:10:42-04:00` expresses August 19, 2020 at 8:10am in Eastern Daylight Time.   # noqa: E501

        :return: The route_departure_time of this Route.  # noqa: E501
        :rtype: str
        """
        return self._route_departure_time

    @route_departure_time.setter
    def route_departure_time(self, route_departure_time):
        """Sets the route_departure_time of this Route.

        The time at which Citymapper thinks the user will set out on this route, given available departure information. This is computed assuming that user is at the start of the route.  Updated values for `route_departure_time` and `route_arrival_time` are returned by `/api/1/live/routeupdates` to reflect any updated departure information.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone in which the event occurs. For example, `2020-08-19T08:10:42-04:00` expresses August 19, 2020 at 8:10am in Eastern Daylight Time.   # noqa: E501

        :param route_departure_time: The route_departure_time of this Route.  # noqa: E501
        :type: str
        """

        self._route_departure_time = route_departure_time

    @property
    def route_arrival_time(self):
        """Gets the route_arrival_time of this Route.  # noqa: E501

        The time at which Citymapper thinks the user will arrive at the end of this route, given available departure information and expected travel speed. This is computed assuming that user is at the start of the route.  Updated values for `route_departure_time` and `route_arrival_time` are returned by `/api/1/live/routeupdates` to reflect any updated departure information.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone in which the event occurs. For example, `2020-08-19T08:10:42-04:00` expresses August 19, 2020 at 8:10am in Eastern Daylight Time.   # noqa: E501

        :return: The route_arrival_time of this Route.  # noqa: E501
        :rtype: str
        """
        return self._route_arrival_time

    @route_arrival_time.setter
    def route_arrival_time(self, route_arrival_time):
        """Sets the route_arrival_time of this Route.

        The time at which Citymapper thinks the user will arrive at the end of this route, given available departure information and expected travel speed. This is computed assuming that user is at the start of the route.  Updated values for `route_departure_time` and `route_arrival_time` are returned by `/api/1/live/routeupdates` to reflect any updated departure information.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone in which the event occurs. For example, `2020-08-19T08:10:42-04:00` expresses August 19, 2020 at 8:10am in Eastern Daylight Time.   # noqa: E501

        :param route_arrival_time: The route_arrival_time of this Route.  # noqa: E501
        :type: str
        """

        self._route_arrival_time = route_arrival_time

    @property
    def route_metadata(self):
        """Gets the route_metadata of this Route.  # noqa: E501


        :return: The route_metadata of this Route.  # noqa: E501
        :rtype: RouteMetadata
        """
        return self._route_metadata

    @route_metadata.setter
    def route_metadata(self, route_metadata):
        """Sets the route_metadata of this Route.


        :param route_metadata: The route_metadata of this Route.  # noqa: E501
        :type: RouteMetadata
        """

        self._route_metadata = route_metadata

    @property
    def profile(self):
        """Gets the profile of this Route.  # noqa: E501

        Indicates which routing \"profile\" was used to calculate this Route. For example, a response from a bike routing endpoint may return multiple routes, one with a `quiet` profile and another with a `fast` profile.  Note that new values can be added at any time, so any code parsing this field must be able to handle unexpected values.  This value will match the `profiles` request parameter on endpoints that support selecting specific routing profiles.  This value is intended to be machine readable only. For a profile name to show to a user, use the `profile_name` in the `route_metadata` object instead.   # noqa: E501

        :return: The profile of this Route.  # noqa: E501
        :rtype: str
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this Route.

        Indicates which routing \"profile\" was used to calculate this Route. For example, a response from a bike routing endpoint may return multiple routes, one with a `quiet` profile and another with a `fast` profile.  Note that new values can be added at any time, so any code parsing this field must be able to handle unexpected values.  This value will match the `profiles` request parameter on endpoints that support selecting specific routing profiles.  This value is intended to be machine readable only. For a profile name to show to a user, use the `profile_name` in the `route_metadata` object instead.   # noqa: E501

        :param profile: The profile of this Route.  # noqa: E501
        :type: str
        """

        self._profile = profile

    @property
    def signature(self):
        """Gets the signature of this Route.  # noqa: E501

        A value to be passed back to the server in subsequent calls to refer to this Route (for instance, when requesting live departure information via `/api/1/live/routeupdates`). It must be treated as an opaque value.  # noqa: E501

        :return: The signature of this Route.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this Route.

        A value to be passed back to the server in subsequent calls to refer to this Route (for instance, when requesting live departure information via `/api/1/live/routeupdates`). It must be treated as an opaque value.  # noqa: E501

        :param signature: The signature of this Route.  # noqa: E501
        :type: str
        """
        if signature is None:
            raise ValueError("Invalid value for `signature`, must not be `None`")  # noqa: E501

        self._signature = signature

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Route, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Route):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
