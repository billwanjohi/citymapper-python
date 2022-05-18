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

class RouteUpdate(object):
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
        'leg_updates': 'list[LegUpdatableDetail]',
        'route_departure_time': 'str',
        'route_arrival_time': 'str',
        'route_duration_seconds': 'int',
        'route_duration_accuracy': 'DurationAccuracy',
        'request_signature': 'str'
    }

    attribute_map = {
        'leg_updates': 'leg_updates',
        'route_departure_time': 'route_departure_time',
        'route_arrival_time': 'route_arrival_time',
        'route_duration_seconds': 'route_duration_seconds',
        'route_duration_accuracy': 'route_duration_accuracy',
        'request_signature': 'request_signature'
    }

    def __init__(self, leg_updates=None, route_departure_time=None, route_arrival_time=None, route_duration_seconds=None, route_duration_accuracy=None, request_signature=None):  # noqa: E501
        """RouteUpdate - a model defined in Swagger"""  # noqa: E501
        self._leg_updates = None
        self._route_departure_time = None
        self._route_arrival_time = None
        self._route_duration_seconds = None
        self._route_duration_accuracy = None
        self._request_signature = None
        self.discriminator = None
        self.leg_updates = leg_updates
        if route_departure_time is not None:
            self.route_departure_time = route_departure_time
        if route_arrival_time is not None:
            self.route_arrival_time = route_arrival_time
        if route_duration_seconds is not None:
            self.route_duration_seconds = route_duration_seconds
        if route_duration_accuracy is not None:
            self.route_duration_accuracy = route_duration_accuracy
        self.request_signature = request_signature

    @property
    def leg_updates(self):
        """Gets the leg_updates of this RouteUpdate.  # noqa: E501

        This is an parallel array of Leg Updatable Detail objects, one for every Leg in the original Route being updated. The ones corresponding to walking Legs will be empty, but the details corresponding to transit legs will contain updated departure information.   # noqa: E501

        :return: The leg_updates of this RouteUpdate.  # noqa: E501
        :rtype: list[LegUpdatableDetail]
        """
        return self._leg_updates

    @leg_updates.setter
    def leg_updates(self, leg_updates):
        """Sets the leg_updates of this RouteUpdate.

        This is an parallel array of Leg Updatable Detail objects, one for every Leg in the original Route being updated. The ones corresponding to walking Legs will be empty, but the details corresponding to transit legs will contain updated departure information.   # noqa: E501

        :param leg_updates: The leg_updates of this RouteUpdate.  # noqa: E501
        :type: list[LegUpdatableDetail]
        """
        if leg_updates is None:
            raise ValueError("Invalid value for `leg_updates`, must not be `None`")  # noqa: E501

        self._leg_updates = leg_updates

    @property
    def route_departure_time(self):
        """Gets the route_departure_time of this RouteUpdate.  # noqa: E501

        The time at which Citymapper thinks the user will set out on this route, given available departure information. This is computed assuming that user is at the start of the route at the time of the request.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone in which the event occurs. For example, `2020-08-19T08:10:42-04:00` expresses August 19, 2020 at 8:10am in Eastern Daylight Time.   # noqa: E501

        :return: The route_departure_time of this RouteUpdate.  # noqa: E501
        :rtype: str
        """
        return self._route_departure_time

    @route_departure_time.setter
    def route_departure_time(self, route_departure_time):
        """Sets the route_departure_time of this RouteUpdate.

        The time at which Citymapper thinks the user will set out on this route, given available departure information. This is computed assuming that user is at the start of the route at the time of the request.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone in which the event occurs. For example, `2020-08-19T08:10:42-04:00` expresses August 19, 2020 at 8:10am in Eastern Daylight Time.   # noqa: E501

        :param route_departure_time: The route_departure_time of this RouteUpdate.  # noqa: E501
        :type: str
        """

        self._route_departure_time = route_departure_time

    @property
    def route_arrival_time(self):
        """Gets the route_arrival_time of this RouteUpdate.  # noqa: E501

        The time at which Citymapper thinks the user will arrive at the end of this route, given available departure information and expected travel speed. This is computed assuming that user is at the start of the route at the time of the request.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone in which the event occurs. For example, `2020-08-19T08:10:42-04:00` expresses August 19, 2020 at 8:10am in Eastern Daylight Time.   # noqa: E501

        :return: The route_arrival_time of this RouteUpdate.  # noqa: E501
        :rtype: str
        """
        return self._route_arrival_time

    @route_arrival_time.setter
    def route_arrival_time(self, route_arrival_time):
        """Sets the route_arrival_time of this RouteUpdate.

        The time at which Citymapper thinks the user will arrive at the end of this route, given available departure information and expected travel speed. This is computed assuming that user is at the start of the route at the time of the request.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone in which the event occurs. For example, `2020-08-19T08:10:42-04:00` expresses August 19, 2020 at 8:10am in Eastern Daylight Time.   # noqa: E501

        :param route_arrival_time: The route_arrival_time of this RouteUpdate.  # noqa: E501
        :type: str
        """

        self._route_arrival_time = route_arrival_time

    @property
    def route_duration_seconds(self):
        """Gets the route_duration_seconds of this RouteUpdate.  # noqa: E501

        The overall estimated time to traverse the entire route, in seconds.  This value replaces the `duration_seconds` value from the original Route, as it will be recomputed to use the specific departure information contained in this Route update response.  May be omitted in rare circumstances when the duration cannot be computed, for instance if the Route can't be completed at the given time because the Services involved are not running.   # noqa: E501

        :return: The route_duration_seconds of this RouteUpdate.  # noqa: E501
        :rtype: int
        """
        return self._route_duration_seconds

    @route_duration_seconds.setter
    def route_duration_seconds(self, route_duration_seconds):
        """Sets the route_duration_seconds of this RouteUpdate.

        The overall estimated time to traverse the entire route, in seconds.  This value replaces the `duration_seconds` value from the original Route, as it will be recomputed to use the specific departure information contained in this Route update response.  May be omitted in rare circumstances when the duration cannot be computed, for instance if the Route can't be completed at the given time because the Services involved are not running.   # noqa: E501

        :param route_duration_seconds: The route_duration_seconds of this RouteUpdate.  # noqa: E501
        :type: int
        """

        self._route_duration_seconds = route_duration_seconds

    @property
    def route_duration_accuracy(self):
        """Gets the route_duration_accuracy of this RouteUpdate.  # noqa: E501


        :return: The route_duration_accuracy of this RouteUpdate.  # noqa: E501
        :rtype: DurationAccuracy
        """
        return self._route_duration_accuracy

    @route_duration_accuracy.setter
    def route_duration_accuracy(self, route_duration_accuracy):
        """Sets the route_duration_accuracy of this RouteUpdate.


        :param route_duration_accuracy: The route_duration_accuracy of this RouteUpdate.  # noqa: E501
        :type: DurationAccuracy
        """

        self._route_duration_accuracy = route_duration_accuracy

    @property
    def request_signature(self):
        """Gets the request_signature of this RouteUpdate.  # noqa: E501

        This is a Route `signature` from the update request, which should be used to associate this update with the correct Route.   # noqa: E501

        :return: The request_signature of this RouteUpdate.  # noqa: E501
        :rtype: str
        """
        return self._request_signature

    @request_signature.setter
    def request_signature(self, request_signature):
        """Sets the request_signature of this RouteUpdate.

        This is a Route `signature` from the update request, which should be used to associate this update with the correct Route.   # noqa: E501

        :param request_signature: The request_signature of this RouteUpdate.  # noqa: E501
        :type: str
        """
        if request_signature is None:
            raise ValueError("Invalid value for `request_signature`, must not be `None`")  # noqa: E501

        self._request_signature = request_signature

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
        if issubclass(RouteUpdate, dict):
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
        if not isinstance(other, RouteUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
