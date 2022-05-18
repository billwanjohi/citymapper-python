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
from swagger_client.models.leg import Leg  # noqa: F401,E501

class LegVariantWalk(Leg):
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
        'station_walk_type': 'str',
        'walk_details_enter_station': 'object',
        'walk_details_exit_station': 'object'
    }
    if hasattr(Leg, "swagger_types"):
        swagger_types.update(Leg.swagger_types)

    attribute_map = {
        'station_walk_type': 'station_walk_type',
        'walk_details_enter_station': 'walk_details_enter_station',
        'walk_details_exit_station': 'walk_details_exit_station'
    }
    if hasattr(Leg, "attribute_map"):
        attribute_map.update(Leg.attribute_map)

    def __init__(self, station_walk_type='outside_station', walk_details_enter_station=None, walk_details_exit_station=None, *args, **kwargs):  # noqa: E501
        """LegVariantWalk - a model defined in Swagger"""  # noqa: E501
        self._station_walk_type = None
        self._walk_details_enter_station = None
        self._walk_details_exit_station = None
        self.discriminator = None
        if station_walk_type is not None:
            self.station_walk_type = station_walk_type
        if walk_details_enter_station is not None:
            self.walk_details_enter_station = walk_details_enter_station
        if walk_details_exit_station is not None:
            self.walk_details_exit_station = walk_details_exit_station
        Leg.__init__(self, *args, **kwargs)

    @property
    def station_walk_type(self):
        """Gets the station_walk_type of this LegVariantWalk.  # noqa: E501

        If provided, indicates which parts of a walk are inside of a station.  | value | description | | ----- | ----------- | | outside_station | This walking leg has no relationship to a transit station, so no `walk_details_*` fields are provided. This is the default when this field is omitted. | | enter_station | This walking leg ends by entering a station and walking to the platform, `walk_details_enter_station` is provided | | change_platform | This walking leg takes place entirely between two platforms in one station, no `walk_details_*` fields are provided. | | exit_station | This walking leg starts by exiting a station, `walk_details_exit_station` is provided | | walk_between_stations | This walking leg involves exiting a station and entering another nearby station; both `walk_details_exit_station` and `walk_details_enter_station` are provided |  This field is only provided when `travel_mode` is `walk`.   # noqa: E501

        :return: The station_walk_type of this LegVariantWalk.  # noqa: E501
        :rtype: str
        """
        return self._station_walk_type

    @station_walk_type.setter
    def station_walk_type(self, station_walk_type):
        """Sets the station_walk_type of this LegVariantWalk.

        If provided, indicates which parts of a walk are inside of a station.  | value | description | | ----- | ----------- | | outside_station | This walking leg has no relationship to a transit station, so no `walk_details_*` fields are provided. This is the default when this field is omitted. | | enter_station | This walking leg ends by entering a station and walking to the platform, `walk_details_enter_station` is provided | | change_platform | This walking leg takes place entirely between two platforms in one station, no `walk_details_*` fields are provided. | | exit_station | This walking leg starts by exiting a station, `walk_details_exit_station` is provided | | walk_between_stations | This walking leg involves exiting a station and entering another nearby station; both `walk_details_exit_station` and `walk_details_enter_station` are provided |  This field is only provided when `travel_mode` is `walk`.   # noqa: E501

        :param station_walk_type: The station_walk_type of this LegVariantWalk.  # noqa: E501
        :type: str
        """
        allowed_values = ["outside_station", "enter_station", "change_platforms", "exit_station", "walk_between_stations"]  # noqa: E501
        if station_walk_type not in allowed_values:
            raise ValueError(
                "Invalid value for `station_walk_type` ({0}), must be one of {1}"  # noqa: E501
                .format(station_walk_type, allowed_values)
            )

        self._station_walk_type = station_walk_type

    @property
    def walk_details_enter_station(self):
        """Gets the walk_details_enter_station of this LegVariantWalk.  # noqa: E501

        When a walk Leg ends by entering a transit station, this can provide information on which entrance the rider should use, and how much of the Leg's walk duration takes place between the entrance and the platform.  This field is relevant for `station_walk_type` of `enter_station` and `walk_between_stations`.   # noqa: E501

        :return: The walk_details_enter_station of this LegVariantWalk.  # noqa: E501
        :rtype: object
        """
        return self._walk_details_enter_station

    @walk_details_enter_station.setter
    def walk_details_enter_station(self, walk_details_enter_station):
        """Sets the walk_details_enter_station of this LegVariantWalk.

        When a walk Leg ends by entering a transit station, this can provide information on which entrance the rider should use, and how much of the Leg's walk duration takes place between the entrance and the platform.  This field is relevant for `station_walk_type` of `enter_station` and `walk_between_stations`.   # noqa: E501

        :param walk_details_enter_station: The walk_details_enter_station of this LegVariantWalk.  # noqa: E501
        :type: object
        """

        self._walk_details_enter_station = walk_details_enter_station

    @property
    def walk_details_exit_station(self):
        """Gets the walk_details_exit_station of this LegVariantWalk.  # noqa: E501

        When a walk Leg begins by exiting a transit station, this can provide information on which exit the rider should use, and how much of the Leg's walk duration takes place between the platform and the exit.  This field is relevant for `station_walk_type` of `exit_station` and `walk_between_stations`.   # noqa: E501

        :return: The walk_details_exit_station of this LegVariantWalk.  # noqa: E501
        :rtype: object
        """
        return self._walk_details_exit_station

    @walk_details_exit_station.setter
    def walk_details_exit_station(self, walk_details_exit_station):
        """Sets the walk_details_exit_station of this LegVariantWalk.

        When a walk Leg begins by exiting a transit station, this can provide information on which exit the rider should use, and how much of the Leg's walk duration takes place between the platform and the exit.  This field is relevant for `station_walk_type` of `exit_station` and `walk_between_stations`.   # noqa: E501

        :param walk_details_exit_station: The walk_details_exit_station of this LegVariantWalk.  # noqa: E501
        :type: object
        """

        self._walk_details_exit_station = walk_details_exit_station

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
        if issubclass(LegVariantWalk, dict):
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
        if not isinstance(other, LegVariantWalk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
