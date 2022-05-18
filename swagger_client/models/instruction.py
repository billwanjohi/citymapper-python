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

class Instruction(object):
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
        'path_index': 'int',
        'distance_meters': 'int',
        'time_seconds': 'int',
        'description_text': 'str',
        'description_format': 'str',
        'description_format_replacements': 'list[InstructionDescriptionFormatReplacements]',
        'type': 'str',
        'type_direction': 'str'
    }

    attribute_map = {
        'path_index': 'path_index',
        'distance_meters': 'distance_meters',
        'time_seconds': 'time_seconds',
        'description_text': 'description_text',
        'description_format': 'description_format',
        'description_format_replacements': 'description_format_replacements',
        'type': 'type',
        'type_direction': 'type_direction'
    }

    def __init__(self, path_index=None, distance_meters=None, time_seconds=None, description_text=None, description_format=None, description_format_replacements=None, type=None, type_direction=None):  # noqa: E501
        """Instruction - a model defined in Swagger"""  # noqa: E501
        self._path_index = None
        self._distance_meters = None
        self._time_seconds = None
        self._description_text = None
        self._description_format = None
        self._description_format_replacements = None
        self._type = None
        self._type_direction = None
        self.discriminator = None
        self.path_index = path_index
        if distance_meters is not None:
            self.distance_meters = distance_meters
        if time_seconds is not None:
            self.time_seconds = time_seconds
        if description_text is not None:
            self.description_text = description_text
        if description_format is not None:
            self.description_format = description_format
        if description_format_replacements is not None:
            self.description_format_replacements = description_format_replacements
        if type is not None:
            self.type = type
        if type_direction is not None:
            self.type_direction = type_direction

    @property
    def path_index(self):
        """Gets the path_index of this Instruction.  # noqa: E501

        0-based index into the list of coordinates provided by the `path` property of the Leg. This indicates the location at which the instruction is to be followed, so it will be the location of the turn on the path, or the start or end of the Leg.   # noqa: E501

        :return: The path_index of this Instruction.  # noqa: E501
        :rtype: int
        """
        return self._path_index

    @path_index.setter
    def path_index(self, path_index):
        """Sets the path_index of this Instruction.

        0-based index into the list of coordinates provided by the `path` property of the Leg. This indicates the location at which the instruction is to be followed, so it will be the location of the turn on the path, or the start or end of the Leg.   # noqa: E501

        :param path_index: The path_index of this Instruction.  # noqa: E501
        :type: int
        """
        if path_index is None:
            raise ValueError("Invalid value for `path_index`, must not be `None`")  # noqa: E501

        self._path_index = path_index

    @property
    def distance_meters(self):
        """Gets the distance_meters of this Instruction.  # noqa: E501

        The distance in meters of the section of the `path` **prior to** this instruction. This property will be omitted for initial instructions of type `depart`.   # noqa: E501

        :return: The distance_meters of this Instruction.  # noqa: E501
        :rtype: int
        """
        return self._distance_meters

    @distance_meters.setter
    def distance_meters(self, distance_meters):
        """Sets the distance_meters of this Instruction.

        The distance in meters of the section of the `path` **prior to** this instruction. This property will be omitted for initial instructions of type `depart`.   # noqa: E501

        :param distance_meters: The distance_meters of this Instruction.  # noqa: E501
        :type: int
        """

        self._distance_meters = distance_meters

    @property
    def time_seconds(self):
        """Gets the time_seconds of this Instruction.  # noqa: E501

        The time in seconds that the user is expected to take to traverse the section of the `path` **prior to** this instruction. This property will be omitted for initial instructions of type `depart`.   # noqa: E501

        :return: The time_seconds of this Instruction.  # noqa: E501
        :rtype: int
        """
        return self._time_seconds

    @time_seconds.setter
    def time_seconds(self, time_seconds):
        """Sets the time_seconds of this Instruction.

        The time in seconds that the user is expected to take to traverse the section of the `path` **prior to** this instruction. This property will be omitted for initial instructions of type `depart`.   # noqa: E501

        :param time_seconds: The time_seconds of this Instruction.  # noqa: E501
        :type: int
        """

        self._time_seconds = time_seconds

    @property
    def description_text(self):
        """Gets the description_text of this Instruction.  # noqa: E501

        Plain-text description of the Instruction to the user.   # noqa: E501

        :return: The description_text of this Instruction.  # noqa: E501
        :rtype: str
        """
        return self._description_text

    @description_text.setter
    def description_text(self, description_text):
        """Sets the description_text of this Instruction.

        Plain-text description of the Instruction to the user.   # noqa: E501

        :param description_text: The description_text of this Instruction.  # noqa: E501
        :type: str
        """

        self._description_text = description_text

    @property
    def description_format(self):
        """Gets the description_format of this Instruction.  # noqa: E501

        Text format for rendering the Instruction with emphasized elements, where `{key}` indicates a part of the string that must be replaced with content defined by the entry corresponding to `key` in `description_format_replacements`.  This allows the elements described by the replacements to be formatted differently by the client, if desired.  Key strings will contain only the characters `[a-zA-Z0-9]`.  `{ }` will not be nested, and the literal characters `{` and `}` are encoded by the escape sequences `\\{` and `\\}`, respectively.   # noqa: E501

        :return: The description_format of this Instruction.  # noqa: E501
        :rtype: str
        """
        return self._description_format

    @description_format.setter
    def description_format(self, description_format):
        """Sets the description_format of this Instruction.

        Text format for rendering the Instruction with emphasized elements, where `{key}` indicates a part of the string that must be replaced with content defined by the entry corresponding to `key` in `description_format_replacements`.  This allows the elements described by the replacements to be formatted differently by the client, if desired.  Key strings will contain only the characters `[a-zA-Z0-9]`.  `{ }` will not be nested, and the literal characters `{` and `}` are encoded by the escape sequences `\\{` and `\\}`, respectively.   # noqa: E501

        :param description_format: The description_format of this Instruction.  # noqa: E501
        :type: str
        """

        self._description_format = description_format

    @property
    def description_format_replacements(self):
        """Gets the description_format_replacements of this Instruction.  # noqa: E501


        :return: The description_format_replacements of this Instruction.  # noqa: E501
        :rtype: list[InstructionDescriptionFormatReplacements]
        """
        return self._description_format_replacements

    @description_format_replacements.setter
    def description_format_replacements(self, description_format_replacements):
        """Sets the description_format_replacements of this Instruction.


        :param description_format_replacements: The description_format_replacements of this Instruction.  # noqa: E501
        :type: list[InstructionDescriptionFormatReplacements]
        """

        self._description_format_replacements = description_format_replacements

    @property
    def type(self):
        """Gets the type of this Instruction.  # noqa: E501

        Indicates the type of Instruction.  **NOTE: New values may be added to this list at any time.**   # noqa: E501

        :return: The type of this Instruction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Instruction.

        Indicates the type of Instruction.  **NOTE: New values may be added to this list at any time.**   # noqa: E501

        :param type: The type of this Instruction.  # noqa: E501
        :type: str
        """
        allowed_values = ["depart", "turn", "enter_roundabout", "exit_roundabout", "arrive"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def type_direction(self):
        """Gets the type_direction of this Instruction.  # noqa: E501

        Indicates a direction that modifies this Instruction.  **NOTE: New values may be added to this list at any time.**   # noqa: E501

        :return: The type_direction of this Instruction.  # noqa: E501
        :rtype: str
        """
        return self._type_direction

    @type_direction.setter
    def type_direction(self, type_direction):
        """Sets the type_direction of this Instruction.

        Indicates a direction that modifies this Instruction.  **NOTE: New values may be added to this list at any time.**   # noqa: E501

        :param type_direction: The type_direction of this Instruction.  # noqa: E501
        :type: str
        """
        allowed_values = ["straight", "uturn", "left", "slight_left", "sharp_left", "right", "slight_right", "sharp_right"]  # noqa: E501
        if type_direction not in allowed_values:
            raise ValueError(
                "Invalid value for `type_direction` ({0}), must be one of {1}"  # noqa: E501
                .format(type_direction, allowed_values)
            )

        self._type_direction = type_direction

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
        if issubclass(Instruction, dict):
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
        if not isinstance(other, Instruction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
