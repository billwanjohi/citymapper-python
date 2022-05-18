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

class HireVehicleMetadata(object):
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
        'name': 'str',
        'service_id': 'str',
        'propulsion_type': 'str',
        'current_range_meters': 'int',
        'current_fuel_percent': 'float'
    }

    attribute_map = {
        'name': 'name',
        'service_id': 'service_id',
        'propulsion_type': 'propulsion_type',
        'current_range_meters': 'current_range_meters',
        'current_fuel_percent': 'current_fuel_percent'
    }

    def __init__(self, name=None, service_id=None, propulsion_type=None, current_range_meters=None, current_fuel_percent=None):  # noqa: E501
        """HireVehicleMetadata - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._service_id = None
        self._propulsion_type = None
        self._current_range_meters = None
        self._current_fuel_percent = None
        self.discriminator = None
        if name is not None:
            self.name = name
        self.service_id = service_id
        if propulsion_type is not None:
            self.propulsion_type = propulsion_type
        if current_range_meters is not None:
            self.current_range_meters = current_range_meters
        if current_fuel_percent is not None:
            self.current_fuel_percent = current_fuel_percent

    @property
    def name(self):
        """Gets the name of this HireVehicleMetadata.  # noqa: E501

        The public name of this vehicle, if applicable, for display to the user.  # noqa: E501

        :return: The name of this HireVehicleMetadata.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HireVehicleMetadata.

        The public name of this vehicle, if applicable, for display to the user.  # noqa: E501

        :param name: The name of this HireVehicleMetadata.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def service_id(self):
        """Gets the service_id of this HireVehicleMetadata.  # noqa: E501

        Indicates which Service in the Leg this Vehicle belongs to, in order to indicate Service and Brand naming and imagery. This is redundant in single-Service Legs, but it's essential in Legs that have alternate equivalent services.   # noqa: E501

        :return: The service_id of this HireVehicleMetadata.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this HireVehicleMetadata.

        Indicates which Service in the Leg this Vehicle belongs to, in order to indicate Service and Brand naming and imagery. This is redundant in single-Service Legs, but it's essential in Legs that have alternate equivalent services.   # noqa: E501

        :param service_id: The service_id of this HireVehicleMetadata.  # noqa: E501
        :type: str
        """
        if service_id is None:
            raise ValueError("Invalid value for `service_id`, must not be `None`")  # noqa: E501

        self._service_id = service_id

    @property
    def propulsion_type(self):
        """Gets the propulsion_type of this HireVehicleMetadata.  # noqa: E501

        The type of fuel this vehicle uses for propulsion (if any). Note, it is possible that additional values will be added to this list in future. If this field is not present, the vehicle has no internal propulsion source (i.e. it is purely human-powered).  | value | description | | ----- | ----------------- | | electric | Powered by battery-powered electric motor - either entirely using a throttle, or as assistance to human power | | combustion | Powered by gasoline combustion engine |   # noqa: E501

        :return: The propulsion_type of this HireVehicleMetadata.  # noqa: E501
        :rtype: str
        """
        return self._propulsion_type

    @propulsion_type.setter
    def propulsion_type(self, propulsion_type):
        """Sets the propulsion_type of this HireVehicleMetadata.

        The type of fuel this vehicle uses for propulsion (if any). Note, it is possible that additional values will be added to this list in future. If this field is not present, the vehicle has no internal propulsion source (i.e. it is purely human-powered).  | value | description | | ----- | ----------------- | | electric | Powered by battery-powered electric motor - either entirely using a throttle, or as assistance to human power | | combustion | Powered by gasoline combustion engine |   # noqa: E501

        :param propulsion_type: The propulsion_type of this HireVehicleMetadata.  # noqa: E501
        :type: str
        """
        allowed_values = ["electric", "combustion"]  # noqa: E501
        if propulsion_type not in allowed_values:
            raise ValueError(
                "Invalid value for `propulsion_type` ({0}), must be one of {1}"  # noqa: E501
                .format(propulsion_type, allowed_values)
            )

        self._propulsion_type = propulsion_type

    @property
    def current_range_meters(self):
        """Gets the current_range_meters of this HireVehicleMetadata.  # noqa: E501

        The estimated range this vehicle can travel with its remaining power or fuel, if applicable.  # noqa: E501

        :return: The current_range_meters of this HireVehicleMetadata.  # noqa: E501
        :rtype: int
        """
        return self._current_range_meters

    @current_range_meters.setter
    def current_range_meters(self, current_range_meters):
        """Sets the current_range_meters of this HireVehicleMetadata.

        The estimated range this vehicle can travel with its remaining power or fuel, if applicable.  # noqa: E501

        :param current_range_meters: The current_range_meters of this HireVehicleMetadata.  # noqa: E501
        :type: int
        """

        self._current_range_meters = current_range_meters

    @property
    def current_fuel_percent(self):
        """Gets the current_fuel_percent of this HireVehicleMetadata.  # noqa: E501

        This vehicle's remaining power or fuel, expressed as a value between 0 and 1.  # noqa: E501

        :return: The current_fuel_percent of this HireVehicleMetadata.  # noqa: E501
        :rtype: float
        """
        return self._current_fuel_percent

    @current_fuel_percent.setter
    def current_fuel_percent(self, current_fuel_percent):
        """Sets the current_fuel_percent of this HireVehicleMetadata.

        This vehicle's remaining power or fuel, expressed as a value between 0 and 1.  # noqa: E501

        :param current_fuel_percent: The current_fuel_percent of this HireVehicleMetadata.  # noqa: E501
        :type: float
        """

        self._current_fuel_percent = current_fuel_percent

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
        if issubclass(HireVehicleMetadata, dict):
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
        if not isinstance(other, HireVehicleMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
