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

class InstructionDescriptionFormatReplacements(object):
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
        'key': 'str',
        'text': 'str',
        'type': 'str',
        'language': 'str'
    }

    attribute_map = {
        'key': 'key',
        'text': 'text',
        'type': 'type',
        'language': 'language'
    }

    def __init__(self, key=None, text=None, type=None, language=None):  # noqa: E501
        """InstructionDescriptionFormatReplacements - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._text = None
        self._type = None
        self._language = None
        self.discriminator = None
        self.key = key
        self.text = text
        if type is not None:
            self.type = type
        if language is not None:
            self.language = language

    @property
    def key(self):
        """Gets the key of this InstructionDescriptionFormatReplacements.  # noqa: E501

        A key corresponding to a string enclosed in `{}` in `description_format`.   # noqa: E501

        :return: The key of this InstructionDescriptionFormatReplacements.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this InstructionDescriptionFormatReplacements.

        A key corresponding to a string enclosed in `{}` in `description_format`.   # noqa: E501

        :param key: The key of this InstructionDescriptionFormatReplacements.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def text(self):
        """Gets the text of this InstructionDescriptionFormatReplacements.  # noqa: E501

        The text to be used to replace the `{key}` substring in the `description_format`.   # noqa: E501

        :return: The text of this InstructionDescriptionFormatReplacements.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this InstructionDescriptionFormatReplacements.

        The text to be used to replace the `{key}` substring in the `description_format`.   # noqa: E501

        :param text: The text of this InstructionDescriptionFormatReplacements.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def type(self):
        """Gets the type of this InstructionDescriptionFormatReplacements.  # noqa: E501

        A value indicating what kind of real-world thing is being identified by this format replacement. This allows API clients to apply application-specific formatting if desired.  | value | description | | ----- | ----------- | | street_name | The name of a street, road, or other way | | exit_number | The number of an exit, generally from a roundabout |  **NOTE: New values may be added to this list at any time.**   # noqa: E501

        :return: The type of this InstructionDescriptionFormatReplacements.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InstructionDescriptionFormatReplacements.

        A value indicating what kind of real-world thing is being identified by this format replacement. This allows API clients to apply application-specific formatting if desired.  | value | description | | ----- | ----------- | | street_name | The name of a street, road, or other way | | exit_number | The number of an exit, generally from a roundabout |  **NOTE: New values may be added to this list at any time.**   # noqa: E501

        :param type: The type of this InstructionDescriptionFormatReplacements.  # noqa: E501
        :type: str
        """
        allowed_values = ["street_name", "exit_number"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def language(self):
        """Gets the language of this InstructionDescriptionFormatReplacements.  # noqa: E501

        An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates what language the associated `text` is in. Note that this can be different from the language of the surrounding description - this is most common when the replacement is a place-name in a local language whilst the description is in a different language.   # noqa: E501

        :return: The language of this InstructionDescriptionFormatReplacements.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this InstructionDescriptionFormatReplacements.

        An [IETF BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag) that indicates what language the associated `text` is in. Note that this can be different from the language of the surrounding description - this is most common when the replacement is a place-name in a local language whilst the description is in a different language.   # noqa: E501

        :param language: The language of this InstructionDescriptionFormatReplacements.  # noqa: E501
        :type: str
        """

        self._language = language

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
        if issubclass(InstructionDescriptionFormatReplacements, dict):
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
        if not isinstance(other, InstructionDescriptionFormatReplacements):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
