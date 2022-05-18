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

class Service(object):
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
        'id': 'str',
        'name': 'str',
        'vehicle_types': 'list[VehicleType]',
        'brand': 'AllOfServiceBrand',
        'images': 'list[ServiceImage]',
        'color': 'str',
        'background_color': 'str',
        'text_color': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'vehicle_types': 'vehicle_types',
        'brand': 'brand',
        'images': 'images',
        'color': 'color',
        'background_color': 'background_color',
        'text_color': 'text_color'
    }

    def __init__(self, id=None, name=None, vehicle_types=None, brand=None, images=None, color=None, background_color=None, text_color=None):  # noqa: E501
        """Service - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._vehicle_types = None
        self._brand = None
        self._images = None
        self._color = None
        self._background_color = None
        self._text_color = None
        self.discriminator = None
        self.id = id
        self.name = name
        if vehicle_types is not None:
            self.vehicle_types = vehicle_types
        if brand is not None:
            self.brand = brand
        if images is not None:
            self.images = images
        if color is not None:
            self.color = color
        if background_color is not None:
            self.background_color = background_color
        if text_color is not None:
            self.text_color = text_color

    @property
    def id(self):
        """Gets the id of this Service.  # noqa: E501

        The identifier for the service  # noqa: E501

        :return: The id of this Service.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Service.

        The identifier for the service  # noqa: E501

        :param id: The id of this Service.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Service.  # noqa: E501

        A string that can be displayed to the user to describe this service  # noqa: E501

        :return: The name of this Service.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Service.

        A string that can be displayed to the user to describe this service  # noqa: E501

        :param name: The name of this Service.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def vehicle_types(self):
        """Gets the vehicle_types of this Service.  # noqa: E501

        This is a priority list of vehicle types that can be used to describe the vehicle used by this Service. The list is ordered from more specific to less specific vehicle type, to allow for refinements to the list of types to be added over time, and to allow consumers of the API to  make more generic distinctions if desired.   # noqa: E501

        :return: The vehicle_types of this Service.  # noqa: E501
        :rtype: list[VehicleType]
        """
        return self._vehicle_types

    @vehicle_types.setter
    def vehicle_types(self, vehicle_types):
        """Sets the vehicle_types of this Service.

        This is a priority list of vehicle types that can be used to describe the vehicle used by this Service. The list is ordered from more specific to less specific vehicle type, to allow for refinements to the list of types to be added over time, and to allow consumers of the API to  make more generic distinctions if desired.   # noqa: E501

        :param vehicle_types: The vehicle_types of this Service.  # noqa: E501
        :type: list[VehicleType]
        """

        self._vehicle_types = vehicle_types

    @property
    def brand(self):
        """Gets the brand of this Service.  # noqa: E501

        Provides the branding attached to the service. The main purpose of Brand is to determine which specific imagery to show for the service, particularly in the case where the Service doesn't have distinct `images` of its own.   # noqa: E501

        :return: The brand of this Service.  # noqa: E501
        :rtype: AllOfServiceBrand
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this Service.

        Provides the branding attached to the service. The main purpose of Brand is to determine which specific imagery to show for the service, particularly in the case where the Service doesn't have distinct `images` of its own.   # noqa: E501

        :param brand: The brand of this Service.  # noqa: E501
        :type: AllOfServiceBrand
        """

        self._brand = brand

    @property
    def images(self):
        """Gets the images of this Service.  # noqa: E501

        A list of `Image`s that can be used to represent this `Service` in a user interface. API consumers should use the first `Image` in the list that meets their criteria.  Images given here will have a `ui_role` of `service`, as they are identifying the specific `Service` rather than the general `Brand`. If no suitable `Image` is provided here, one of the images in the adjacent `brand` should be used.   # noqa: E501

        :return: The images of this Service.  # noqa: E501
        :rtype: list[ServiceImage]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this Service.

        A list of `Image`s that can be used to represent this `Service` in a user interface. API consumers should use the first `Image` in the list that meets their criteria.  Images given here will have a `ui_role` of `service`, as they are identifying the specific `Service` rather than the general `Brand`. If no suitable `Image` is provided here, one of the images in the adjacent `brand` should be used.   # noqa: E501

        :param images: The images of this Service.  # noqa: E501
        :type: list[ServiceImage]
        """

        self._images = images

    @property
    def color(self):
        """Gets the color of this Service.  # noqa: E501

        The basic color associated with this service, for graphical uses such as map lines.  The color is encoded as a capitalized hexadecimal RGB value starting with `#`. For instance, `#2850AD` encodes the 24-bit RGB value of (40, 80, 173).   # noqa: E501

        :return: The color of this Service.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this Service.

        The basic color associated with this service, for graphical uses such as map lines.  The color is encoded as a capitalized hexadecimal RGB value starting with `#`. For instance, `#2850AD` encodes the 24-bit RGB value of (40, 80, 173).   # noqa: E501

        :param color: The color of this Service.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def background_color(self):
        """Gets the background_color of this Service.  # noqa: E501

        A background color for use with this service, in cases where text will be shown on a colored background. Used in conjunction with `text_color`.  The color is encoded as a capitalized hexadecimal RGB value starting with `#`. For instance, `#2850AD` encodes the 24-bit RGB value of (40, 80, 173).   # noqa: E501

        :return: The background_color of this Service.  # noqa: E501
        :rtype: str
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """Sets the background_color of this Service.

        A background color for use with this service, in cases where text will be shown on a colored background. Used in conjunction with `text_color`.  The color is encoded as a capitalized hexadecimal RGB value starting with `#`. For instance, `#2850AD` encodes the 24-bit RGB value of (40, 80, 173).   # noqa: E501

        :param background_color: The background_color of this Service.  # noqa: E501
        :type: str
        """

        self._background_color = background_color

    @property
    def text_color(self):
        """Gets the text_color of this Service.  # noqa: E501

        A text color for use with this service, in cases where text will be shown on a colored background. Used in conjunction with `background_color`. If omitted, it means that white (`#FFFFFF`) has sufficient contrast against the given `background_color` or `color` values.  The color is encoded as a capitalized hexadecimal RGB value starting with `#`. For instance, `#2850AD` encodes the 24-bit RGB value of (40, 80, 173).   # noqa: E501

        :return: The text_color of this Service.  # noqa: E501
        :rtype: str
        """
        return self._text_color

    @text_color.setter
    def text_color(self, text_color):
        """Sets the text_color of this Service.

        A text color for use with this service, in cases where text will be shown on a colored background. Used in conjunction with `background_color`. If omitted, it means that white (`#FFFFFF`) has sufficient contrast against the given `background_color` or `color` values.  The color is encoded as a capitalized hexadecimal RGB value starting with `#`. For instance, `#2850AD` encodes the 24-bit RGB value of (40, 80, 173).   # noqa: E501

        :param text_color: The text_color of this Service.  # noqa: E501
        :type: str
        """

        self._text_color = text_color

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
        if issubclass(Service, dict):
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
        if not isinstance(other, Service):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
