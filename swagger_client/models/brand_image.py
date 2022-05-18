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
from swagger_client.models.image import Image  # noqa: F401,E501

class BrandImage(Image):
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
        'ui_role': 'str',
        'is_generic': 'bool',
        'has_space_for_text': 'bool',
        'is_dropoff_place': 'bool',
        'low_capacity': 'bool'
    }
    if hasattr(Image, "swagger_types"):
        swagger_types.update(Image.swagger_types)

    attribute_map = {
        'ui_role': 'ui_role',
        'is_generic': 'is_generic',
        'has_space_for_text': 'has_space_for_text',
        'is_dropoff_place': 'is_dropoff_place',
        'low_capacity': 'low_capacity'
    }
    if hasattr(Image, "attribute_map"):
        attribute_map.update(Image.attribute_map)

    def __init__(self, ui_role=None, is_generic=False, has_space_for_text=False, is_dropoff_place=False, low_capacity=False, *args, **kwargs):  # noqa: E501
        """BrandImage - a model defined in Swagger"""  # noqa: E501
        self._ui_role = None
        self._is_generic = None
        self._has_space_for_text = None
        self._is_dropoff_place = None
        self._low_capacity = None
        self.discriminator = None
        if ui_role is not None:
            self.ui_role = ui_role
        if is_generic is not None:
            self.is_generic = is_generic
        if has_space_for_text is not None:
            self.has_space_for_text = has_space_for_text
        if is_dropoff_place is not None:
            self.is_dropoff_place = is_dropoff_place
        if low_capacity is not None:
            self.low_capacity = low_capacity
        Image.__init__(self, *args, **kwargs)

    @property
    def ui_role(self):
        """Gets the ui_role of this BrandImage.  # noqa: E501


        :return: The ui_role of this BrandImage.  # noqa: E501
        :rtype: str
        """
        return self._ui_role

    @ui_role.setter
    def ui_role(self, ui_role):
        """Sets the ui_role of this BrandImage.


        :param ui_role: The ui_role of this BrandImage.  # noqa: E501
        :type: str
        """
        allowed_values = ["pin", "station", "vehicle", "vehicle_compact", "pin_vehicle"]  # noqa: E501
        if ui_role not in allowed_values:
            raise ValueError(
                "Invalid value for `ui_role` ({0}), must be one of {1}"  # noqa: E501
                .format(ui_role, allowed_values)
            )

        self._ui_role = ui_role

    @property
    def is_generic(self):
        """Gets the is_generic of this BrandImage.  # noqa: E501

        If `true`, this indicates that this is a generic image entirely based on the vehicle type, rather than being customized for the specific brand or service. When a specific branded image of the same `ui_role` is available, it will be provided earlier in the list of images.   # noqa: E501

        :return: The is_generic of this BrandImage.  # noqa: E501
        :rtype: bool
        """
        return self._is_generic

    @is_generic.setter
    def is_generic(self, is_generic):
        """Sets the is_generic of this BrandImage.

        If `true`, this indicates that this is a generic image entirely based on the vehicle type, rather than being customized for the specific brand or service. When a specific branded image of the same `ui_role` is available, it will be provided earlier in the list of images.   # noqa: E501

        :param is_generic: The is_generic of this BrandImage.  # noqa: E501
        :type: bool
        """

        self._is_generic = is_generic

    @property
    def has_space_for_text(self):
        """Gets the has_space_for_text of this BrandImage.  # noqa: E501

        If `true`, this image contains a designated area for overlaying extra textual elements such as \"stop indicator\" letters. (Some regions have 2-4 letter codes on bus stop poles to distinguish between nearby stops.) The specific renderable area will depend on the `ui_role`.  When this is `true`, there will generally also be a peer `Image` without space for text, for the more common case where no text rendering is needed. This alternate `Image` will appear earlier in the list of `Image`s.   # noqa: E501

        :return: The has_space_for_text of this BrandImage.  # noqa: E501
        :rtype: bool
        """
        return self._has_space_for_text

    @has_space_for_text.setter
    def has_space_for_text(self, has_space_for_text):
        """Sets the has_space_for_text of this BrandImage.

        If `true`, this image contains a designated area for overlaying extra textual elements such as \"stop indicator\" letters. (Some regions have 2-4 letter codes on bus stop poles to distinguish between nearby stops.) The specific renderable area will depend on the `ui_role`.  When this is `true`, there will generally also be a peer `Image` without space for text, for the more common case where no text rendering is needed. This alternate `Image` will appear earlier in the list of `Image`s.   # noqa: E501

        :param has_space_for_text: The has_space_for_text of this BrandImage.  # noqa: E501
        :type: bool
        """

        self._has_space_for_text = has_space_for_text

    @property
    def is_dropoff_place(self):
        """Gets the is_dropoff_place of this BrandImage.  # noqa: E501

        Applies to `BrandImage`s with `ui_role` of `pin` or `station` if Brand offers hire vehicles.  If `true`, then this image represents a drop-off place for hire vehicles, for example a docking station for cycles or a parking area for e-scooters.  An image representing drop-off place (`is_dropoff_place` set to `true`) will always be accompanied by an image representing pick-up place (`is_dropoff_place` set to `false`) provided earlier in the list of images.   # noqa: E501

        :return: The is_dropoff_place of this BrandImage.  # noqa: E501
        :rtype: bool
        """
        return self._is_dropoff_place

    @is_dropoff_place.setter
    def is_dropoff_place(self, is_dropoff_place):
        """Sets the is_dropoff_place of this BrandImage.

        Applies to `BrandImage`s with `ui_role` of `pin` or `station` if Brand offers hire vehicles.  If `true`, then this image represents a drop-off place for hire vehicles, for example a docking station for cycles or a parking area for e-scooters.  An image representing drop-off place (`is_dropoff_place` set to `true`) will always be accompanied by an image representing pick-up place (`is_dropoff_place` set to `false`) provided earlier in the list of images.   # noqa: E501

        :param is_dropoff_place: The is_dropoff_place of this BrandImage.  # noqa: E501
        :type: bool
        """

        self._is_dropoff_place = is_dropoff_place

    @property
    def low_capacity(self):
        """Gets the low_capacity of this BrandImage.  # noqa: E501

        Applies to `BrandImage`s with `ui_role` of `pin` or `station` if Brand offers hire vehicles.  If `true`, then this image represents a low capacity variant of pick-up or drop-off place for hire vehicles.  Low capacity variant will always be accompanied by high capacity variant provided earlier in the list of images.   # noqa: E501

        :return: The low_capacity of this BrandImage.  # noqa: E501
        :rtype: bool
        """
        return self._low_capacity

    @low_capacity.setter
    def low_capacity(self, low_capacity):
        """Sets the low_capacity of this BrandImage.

        Applies to `BrandImage`s with `ui_role` of `pin` or `station` if Brand offers hire vehicles.  If `true`, then this image represents a low capacity variant of pick-up or drop-off place for hire vehicles.  Low capacity variant will always be accompanied by high capacity variant provided earlier in the list of images.   # noqa: E501

        :param low_capacity: The low_capacity of this BrandImage.  # noqa: E501
        :type: bool
        """

        self._low_capacity = low_capacity

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
        if issubclass(BrandImage, dict):
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
        if not isinstance(other, BrandImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
