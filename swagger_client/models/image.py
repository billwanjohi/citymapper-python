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

class Image(object):
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
        'url': 'str',
        'ui_role': 'str',
        'width': 'float',
        'height': 'float',
        'pixel_ratio': 'float',
        'format': 'str'
    }

    attribute_map = {
        'url': 'url',
        'ui_role': 'ui_role',
        'width': 'width',
        'height': 'height',
        'pixel_ratio': 'pixel_ratio',
        'format': 'format'
    }

    def __init__(self, url=None, ui_role=None, width=None, height=None, pixel_ratio=2, format='png'):  # noqa: E501
        """Image - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._ui_role = None
        self._width = None
        self._height = None
        self._pixel_ratio = None
        self._format = None
        self.discriminator = None
        self.url = url
        self.ui_role = ui_role
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if pixel_ratio is not None:
            self.pixel_ratio = pixel_ratio
        if format is not None:
            self.format = format

    @property
    def url(self):
        """Gets the url of this Image.  # noqa: E501

        The URL from which this `Image` can be retrieved. The image will be encoded in PNG format unless the `format` field indicates otherwise.   # noqa: E501

        :return: The url of this Image.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Image.

        The URL from which this `Image` can be retrieved. The image will be encoded in PNG format unless the `format` field indicates otherwise.   # noqa: E501

        :param url: The url of this Image.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def ui_role(self):
        """Gets the ui_role of this Image.  # noqa: E501

        Indicates the role that this image plays in a user interface. New values may be added at any time. See the parent object in the response for valid values in this context.   # noqa: E501

        :return: The ui_role of this Image.  # noqa: E501
        :rtype: str
        """
        return self._ui_role

    @ui_role.setter
    def ui_role(self, ui_role):
        """Sets the ui_role of this Image.

        Indicates the role that this image plays in a user interface. New values may be added at any time. See the parent object in the response for valid values in this context.   # noqa: E501

        :param ui_role: The ui_role of this Image.  # noqa: E501
        :type: str
        """
        if ui_role is None:
            raise ValueError("Invalid value for `ui_role`, must not be `None`")  # noqa: E501

        self._ui_role = ui_role

    @property
    def width(self):
        """Gets the width of this Image.  # noqa: E501

        The width of the image in screen units. This corresponds to `px` in CSS, \"points\" on iOS, and \"density-independent pixels\" on Android.   # noqa: E501

        :return: The width of this Image.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Image.

        The width of the image in screen units. This corresponds to `px` in CSS, \"points\" on iOS, and \"density-independent pixels\" on Android.   # noqa: E501

        :param width: The width of this Image.  # noqa: E501
        :type: float
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this Image.  # noqa: E501

        The height of the image in screen units. This corresponds to `px` in CSS, \"points\" on iOS, and \"density-independent pixels\" on Android.   # noqa: E501

        :return: The height of this Image.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Image.

        The height of the image in screen units. This corresponds to `px` in CSS, \"points\" on iOS, and \"density-independent pixels\" on Android.   # noqa: E501

        :param height: The height of this Image.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def pixel_ratio(self):
        """Gets the pixel_ratio of this Image.  # noqa: E501

        Indicates the ratio of image pixels to screen units. When not provided, `2` should be assumed. For instance, an `Image` with a `width` of `38`, `height` of `41`, and `pixel_ratio` of `2` has image pixel dimensions of 76 x 82.   # noqa: E501

        :return: The pixel_ratio of this Image.  # noqa: E501
        :rtype: float
        """
        return self._pixel_ratio

    @pixel_ratio.setter
    def pixel_ratio(self, pixel_ratio):
        """Sets the pixel_ratio of this Image.

        Indicates the ratio of image pixels to screen units. When not provided, `2` should be assumed. For instance, an `Image` with a `width` of `38`, `height` of `41`, and `pixel_ratio` of `2` has image pixel dimensions of 76 x 82.   # noqa: E501

        :param pixel_ratio: The pixel_ratio of this Image.  # noqa: E501
        :type: float
        """

        self._pixel_ratio = pixel_ratio

    @property
    def format(self):
        """Gets the format of this Image.  # noqa: E501

        Indicates the file format of the image. The default value is `png`, indicating Portable Network Graphics bitmap format. At time of writing, all `Images` returned are in `png` format, and therefore this field will usually be omitted. However, in the future, additional `format` types may be provided in responses.   # noqa: E501

        :return: The format of this Image.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Image.

        Indicates the file format of the image. The default value is `png`, indicating Portable Network Graphics bitmap format. At time of writing, all `Images` returned are in `png` format, and therefore this field will usually be omitted. However, in the future, additional `format` types may be provided in responses.   # noqa: E501

        :param format: The format of this Image.  # noqa: E501
        :type: str
        """
        allowed_values = ["png"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

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
        if issubclass(Image, dict):
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
        if not isinstance(other, Image):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
