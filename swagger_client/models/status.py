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

class Status(object):
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
        'type': 'str',
        'title': 'str',
        'description': 'str',
        'service_ids': 'list[str]',
        'stop_ids': 'list[str]',
        'service_stop_ranges': 'list[StatusServiceStopRanges]'
    }

    attribute_map = {
        'type': 'type',
        'title': 'title',
        'description': 'description',
        'service_ids': 'service_ids',
        'stop_ids': 'stop_ids',
        'service_stop_ranges': 'service_stop_ranges'
    }

    def __init__(self, type=None, title=None, description=None, service_ids=None, stop_ids=None, service_stop_ranges=None):  # noqa: E501
        """Status - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._title = None
        self._description = None
        self._service_ids = None
        self._stop_ids = None
        self._service_stop_ranges = None
        self.discriminator = None
        self.type = type
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if service_ids is not None:
            self.service_ids = service_ids
        if stop_ids is not None:
            self.stop_ids = stop_ids
        if service_stop_ranges is not None:
            self.service_stop_ranges = service_stop_ranges

    @property
    def type(self):
        """Gets the type of this Status.  # noqa: E501

        Indicates the type/level/severity expressed by this Status. This can be used to choose icons, and determine whether to show different Status entries.  | value | description | | ----- | ----------- | | unknown | The type/severity of this status couldn't be determined. Should be rare. May still populate `title` and `description`. | | no_issues | No known issues that would affect travel over the specified services and/or stops. May still populate `title` and `description`. | | travel_affected | Travel over the specified services and/or stops may be delayed or otherwise affected. | | travel_prevented | Travel over the specified services and/or stops may not be possible. |   # noqa: E501

        :return: The type of this Status.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Status.

        Indicates the type/level/severity expressed by this Status. This can be used to choose icons, and determine whether to show different Status entries.  | value | description | | ----- | ----------- | | unknown | The type/severity of this status couldn't be determined. Should be rare. May still populate `title` and `description`. | | no_issues | No known issues that would affect travel over the specified services and/or stops. May still populate `title` and `description`. | | travel_affected | Travel over the specified services and/or stops may be delayed or otherwise affected. | | travel_prevented | Travel over the specified services and/or stops may not be possible. |   # noqa: E501

        :param type: The type of this Status.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["unknown", "no_issues", "travel_affected", "travel_prevented"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def title(self):
        """Gets the title of this Status.  # noqa: E501

        A relatively short title for the Status.  # noqa: E501

        :return: The title of this Status.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Status.

        A relatively short title for the Status.  # noqa: E501

        :param title: The title of this Status.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this Status.  # noqa: E501

        An in-depth description of the Status. This will be provided as plain text.  # noqa: E501

        :return: The description of this Status.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Status.

        An in-depth description of the Status. This will be provided as plain text.  # noqa: E501

        :param description: The description of this Status.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def service_ids(self):
        """Gets the service_ids of this Status.  # noqa: E501

        If this Status relates to Services rather than Stops, this will contain the `id` of one or more Services. The ability to specify multiple services is intended to prevent needless duplication of Status reporting.   # noqa: E501

        :return: The service_ids of this Status.  # noqa: E501
        :rtype: list[str]
        """
        return self._service_ids

    @service_ids.setter
    def service_ids(self, service_ids):
        """Sets the service_ids of this Status.

        If this Status relates to Services rather than Stops, this will contain the `id` of one or more Services. The ability to specify multiple services is intended to prevent needless duplication of Status reporting.   # noqa: E501

        :param service_ids: The service_ids of this Status.  # noqa: E501
        :type: list[str]
        """

        self._service_ids = service_ids

    @property
    def stop_ids(self):
        """Gets the stop_ids of this Status.  # noqa: E501

        If this Status relates to specific stops (as opposed to Services, or sections of Services running between specific stops), this will contain the `id` of one or more relevant Stops.  Example: A Status might use this to identify specific metro Stops where riders can't board or alight because they're closed, even though trains are passing through them.   # noqa: E501

        :return: The stop_ids of this Status.  # noqa: E501
        :rtype: list[str]
        """
        return self._stop_ids

    @stop_ids.setter
    def stop_ids(self, stop_ids):
        """Sets the stop_ids of this Status.

        If this Status relates to specific stops (as opposed to Services, or sections of Services running between specific stops), this will contain the `id` of one or more relevant Stops.  Example: A Status might use this to identify specific metro Stops where riders can't board or alight because they're closed, even though trains are passing through them.   # noqa: E501

        :param stop_ids: The stop_ids of this Status.  # noqa: E501
        :type: list[str]
        """

        self._stop_ids = stop_ids

    @property
    def service_stop_ranges(self):
        """Gets the service_stop_ranges of this Status.  # noqa: E501

        If this Status relates to sections of Services between different Stops, this will indicate which sections, in combination with `service_ids`. This field relates to services traveling between Stops, rather than whether or not the Stops are open or closed (which is represented by `stop_ids`).  Example: A Status might use this to indicate that a particular train isn't running between a set of Stops, even if those Stops remain open for other services.   # noqa: E501

        :return: The service_stop_ranges of this Status.  # noqa: E501
        :rtype: list[StatusServiceStopRanges]
        """
        return self._service_stop_ranges

    @service_stop_ranges.setter
    def service_stop_ranges(self, service_stop_ranges):
        """Sets the service_stop_ranges of this Status.

        If this Status relates to sections of Services between different Stops, this will indicate which sections, in combination with `service_ids`. This field relates to services traveling between Stops, rather than whether or not the Stops are open or closed (which is represented by `stop_ids`).  Example: A Status might use this to indicate that a particular train isn't running between a set of Stops, even if those Stops remain open for other services.   # noqa: E501

        :param service_stop_ranges: The service_stop_ranges of this Status.  # noqa: E501
        :type: list[StatusServiceStopRanges]
        """

        self._service_stop_ranges = service_stop_ranges

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
        if issubclass(Status, dict):
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
        if not isinstance(other, Status):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
