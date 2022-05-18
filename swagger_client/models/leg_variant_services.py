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

class LegVariantServices(Leg):
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
        'vehicle_types': 'list[VehicleType]',
        'path_annotations': 'list[PathAnnotation]',
        'services': 'list[Service]'
    }
    if hasattr(Leg, "swagger_types"):
        swagger_types.update(Leg.swagger_types)

    attribute_map = {
        'vehicle_types': 'vehicle_types',
        'path_annotations': 'path_annotations',
        'services': 'services'
    }
    if hasattr(Leg, "attribute_map"):
        attribute_map.update(Leg.attribute_map)

    def __init__(self, vehicle_types=None, path_annotations=None, services=None, *args, **kwargs):  # noqa: E501
        """LegVariantServices - a model defined in Swagger"""  # noqa: E501
        self._vehicle_types = None
        self._path_annotations = None
        self._services = None
        self.discriminator = None
        if vehicle_types is not None:
            self.vehicle_types = vehicle_types
        if path_annotations is not None:
            self.path_annotations = path_annotations
        if services is not None:
            self.services = services
        Leg.__init__(self, *args, **kwargs)

    @property
    def vehicle_types(self):
        """Gets the vehicle_types of this LegVariantServices.  # noqa: E501

        This is a priority list of vehicle types that can be used to describe the vehicle used in this leg. The list is ordered from more specific to less specific vehicle type, to allow for refinements to the list of types to be added over time, and to allow consumers of the API to make more generic distinctions if desired. In the case that this Leg has Services specified, this value will contain the intersection of values given in the individual Services' `vehicle_types` fields.  This property is omitted when no vehicle is involved, such as when `travel_mode` is `walk`.   # noqa: E501

        :return: The vehicle_types of this LegVariantServices.  # noqa: E501
        :rtype: list[VehicleType]
        """
        return self._vehicle_types

    @vehicle_types.setter
    def vehicle_types(self, vehicle_types):
        """Sets the vehicle_types of this LegVariantServices.

        This is a priority list of vehicle types that can be used to describe the vehicle used in this leg. The list is ordered from more specific to less specific vehicle type, to allow for refinements to the list of types to be added over time, and to allow consumers of the API to make more generic distinctions if desired. In the case that this Leg has Services specified, this value will contain the intersection of values given in the individual Services' `vehicle_types` fields.  This property is omitted when no vehicle is involved, such as when `travel_mode` is `walk`.   # noqa: E501

        :param vehicle_types: The vehicle_types of this LegVariantServices.  # noqa: E501
        :type: list[VehicleType]
        """

        self._vehicle_types = vehicle_types

    @property
    def path_annotations(self):
        """Gets the path_annotations of this LegVariantServices.  # noqa: E501

        Array of Path Annotations providing extra metadata about sections of the `path`. For instance, in Legs with `travel_mode` of `self_piloted`, these annotations can indicate sections of the path where the user should dismount their vehicle and walk alongside it due to terrain or restrictions.  Each Path Annotation specifies a `start_index` and `end_index`, which are indices into the series of coordinates encoded by `path`. (For example, an index of `1` refers to the coordinate `(51.51341, -0.08896)` in the `path` example above.)  `path_annotations` will contain annotations in order of increasing `start_index`, and will not contain overlapped ranges (though multiple annotations can refer to the same coordinate).   # noqa: E501

        :return: The path_annotations of this LegVariantServices.  # noqa: E501
        :rtype: list[PathAnnotation]
        """
        return self._path_annotations

    @path_annotations.setter
    def path_annotations(self, path_annotations):
        """Sets the path_annotations of this LegVariantServices.

        Array of Path Annotations providing extra metadata about sections of the `path`. For instance, in Legs with `travel_mode` of `self_piloted`, these annotations can indicate sections of the path where the user should dismount their vehicle and walk alongside it due to terrain or restrictions.  Each Path Annotation specifies a `start_index` and `end_index`, which are indices into the series of coordinates encoded by `path`. (For example, an index of `1` refers to the coordinate `(51.51341, -0.08896)` in the `path` example above.)  `path_annotations` will contain annotations in order of increasing `start_index`, and will not contain overlapped ranges (though multiple annotations can refer to the same coordinate).   # noqa: E501

        :param path_annotations: The path_annotations of this LegVariantServices.  # noqa: E501
        :type: list[PathAnnotation]
        """

        self._path_annotations = path_annotations

    @property
    def services(self):
        """Gets the services of this LegVariantServices.  # noqa: E501

        Indicates the services that can be used to complete this Leg. This field is omitted when the concept is not relevant, for instance when `travel_mode` is `walk` or `self_piloted` (in non-branded results). When more than one service is listed, that means that alternate equivalent services are available (for instance, two buses or trains that travel between the same set of stops).   # noqa: E501

        :return: The services of this LegVariantServices.  # noqa: E501
        :rtype: list[Service]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this LegVariantServices.

        Indicates the services that can be used to complete this Leg. This field is omitted when the concept is not relevant, for instance when `travel_mode` is `walk` or `self_piloted` (in non-branded results). When more than one service is listed, that means that alternate equivalent services are available (for instance, two buses or trains that travel between the same set of stops).   # noqa: E501

        :param services: The services of this LegVariantServices.  # noqa: E501
        :type: list[Service]
        """

        self._services = services

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
        if issubclass(LegVariantServices, dict):
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
        if not isinstance(other, LegVariantServices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
