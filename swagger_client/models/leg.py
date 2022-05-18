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

class Leg(object):
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
        'travel_mode': 'str',
        'duration_seconds': 'int',
        'path': 'str',
        'instructions': 'list[Instruction]'
    }

    attribute_map = {
        'travel_mode': 'travel_mode',
        'duration_seconds': 'duration_seconds',
        'path': 'path',
        'instructions': 'instructions'
    }

    discriminator_value_class_map = {
            'self_piloted'.lower(): '#/components/schemas/LegVariantSelfPiloted',
            'walk'.lower(): '#/components/schemas/LegVariantWalk',
            'transit'.lower(): '#/components/schemas/LegVariantTransit',
            'on_demand'.lower(): '#/components/schemas/LegVariantServices',
    }

    def __init__(self, travel_mode=None, duration_seconds=None, path=None, instructions=None):  # noqa: E501
        """Leg - a model defined in Swagger"""  # noqa: E501
        self._travel_mode = None
        self._duration_seconds = None
        self._path = None
        self._instructions = None
        self.discriminator = 'travel_mode'
        self.travel_mode = travel_mode
        if duration_seconds is not None:
            self.duration_seconds = duration_seconds
        self.path = path
        if instructions is not None:
            self.instructions = instructions

    @property
    def travel_mode(self):
        """Gets the travel_mode of this Leg.  # noqa: E501

        Identifies the kind of travel described by this leg. New options are likely to be added over time. This value indicates which other fields are likely to be populated in the Leg.  | value | description | | ----- | ----------- | | walk | Walking | | transit | Public transportation with fixed routes & stops such as bus, metro, train, ferry | | self_piloted | Vehicles such as e-scooters, bicycles, motor scooters, private automobiles that the user pilots themselves | | on_demand | Services such as rideshare, cab, demand-responsive transit services where the path, pickup and dropoff points are determined by the user rather than fully pre-determined |   # noqa: E501

        :return: The travel_mode of this Leg.  # noqa: E501
        :rtype: str
        """
        return self._travel_mode

    @travel_mode.setter
    def travel_mode(self, travel_mode):
        """Sets the travel_mode of this Leg.

        Identifies the kind of travel described by this leg. New options are likely to be added over time. This value indicates which other fields are likely to be populated in the Leg.  | value | description | | ----- | ----------- | | walk | Walking | | transit | Public transportation with fixed routes & stops such as bus, metro, train, ferry | | self_piloted | Vehicles such as e-scooters, bicycles, motor scooters, private automobiles that the user pilots themselves | | on_demand | Services such as rideshare, cab, demand-responsive transit services where the path, pickup and dropoff points are determined by the user rather than fully pre-determined |   # noqa: E501

        :param travel_mode: The travel_mode of this Leg.  # noqa: E501
        :type: str
        """
        if travel_mode is None:
            raise ValueError("Invalid value for `travel_mode`, must not be `None`")  # noqa: E501
        allowed_values = ["self_piloted", "walk", "transit", "on_demand"]  # noqa: E501
        if travel_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `travel_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(travel_mode, allowed_values)
            )

        self._travel_mode = travel_mode

    @property
    def duration_seconds(self):
        """Gets the duration_seconds of this Leg.  # noqa: E501

        The time required to traverse this leg, excluding any waiting or boarding time at the beginning. May be omitted in rare circumstances when the duration cannot be computed.  # noqa: E501

        :return: The duration_seconds of this Leg.  # noqa: E501
        :rtype: int
        """
        return self._duration_seconds

    @duration_seconds.setter
    def duration_seconds(self, duration_seconds):
        """Sets the duration_seconds of this Leg.

        The time required to traverse this leg, excluding any waiting or boarding time at the beginning. May be omitted in rare circumstances when the duration cannot be computed.  # noqa: E501

        :param duration_seconds: The duration_seconds of this Leg.  # noqa: E501
        :type: int
        """

        self._duration_seconds = duration_seconds

    @property
    def path(self):
        """Gets the path of this Leg.  # noqa: E501

        The geographic path that the leg traverses, as a series of WGS84 coordinates encoded in [Google Polyline Format](https://developers.google.com/maps/documentation/utilities/polylinealgorithm), with a decimal precision of 5 digits.  For example, the value `_flyHbjPDZBTBNDJ` encodes the following series of (latitude, longitude) coordinates: ``` [(51.51344, -0.08882),  (51.51341, -0.08896),  (51.51339, -0.08907),  (51.51337, -0.08915),  (51.51334, -0.08921)] ```   # noqa: E501

        :return: The path of this Leg.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Leg.

        The geographic path that the leg traverses, as a series of WGS84 coordinates encoded in [Google Polyline Format](https://developers.google.com/maps/documentation/utilities/polylinealgorithm), with a decimal precision of 5 digits.  For example, the value `_flyHbjPDZBTBNDJ` encodes the following series of (latitude, longitude) coordinates: ``` [(51.51344, -0.08882),  (51.51341, -0.08896),  (51.51339, -0.08907),  (51.51337, -0.08915),  (51.51334, -0.08921)] ```   # noqa: E501

        :param path: The path of this Leg.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def instructions(self):
        """Gets the instructions of this Leg.  # noqa: E501

        (May be included when `travel_mode` is `walk` or `self_piloted`.)  This provides the list of turn instructions to guide the user through Legs where the user needs to navigate, such as when walking or using a scooter or bike.   # noqa: E501

        :return: The instructions of this Leg.  # noqa: E501
        :rtype: list[Instruction]
        """
        return self._instructions

    @instructions.setter
    def instructions(self, instructions):
        """Sets the instructions of this Leg.

        (May be included when `travel_mode` is `walk` or `self_piloted`.)  This provides the list of turn instructions to guide the user through Legs where the user needs to navigate, such as when walking or using a scooter or bike.   # noqa: E501

        :param instructions: The instructions of this Leg.  # noqa: E501
        :type: list[Instruction]
        """

        self._instructions = instructions

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(Leg, dict):
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
        if not isinstance(other, Leg):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
