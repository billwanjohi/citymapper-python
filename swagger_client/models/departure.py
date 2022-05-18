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

class Departure(object):
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
        'service_id': 'str',
        'suggested_departure': 'str',
        'headsign': 'str',
        'time_name': 'str',
        'short_name': 'str',
        'live_time': 'str',
        'scheduled_time': 'str',
        'frequency_seconds_range': 'list[int]',
        'frequency_start_time': 'str',
        'frequency_end_time': 'str',
        'time_status': 'str',
        'platform_short_name': 'str'
    }

    attribute_map = {
        'type': 'type',
        'service_id': 'service_id',
        'suggested_departure': 'suggested_departure',
        'headsign': 'headsign',
        'time_name': 'time_name',
        'short_name': 'short_name',
        'live_time': 'live_time',
        'scheduled_time': 'scheduled_time',
        'frequency_seconds_range': 'frequency_seconds_range',
        'frequency_start_time': 'frequency_start_time',
        'frequency_end_time': 'frequency_end_time',
        'time_status': 'time_status',
        'platform_short_name': 'platform_short_name'
    }

    def __init__(self, type=None, service_id=None, suggested_departure=None, headsign=None, time_name=None, short_name=None, live_time=None, scheduled_time=None, frequency_seconds_range=None, frequency_start_time=None, frequency_end_time=None, time_status=None, platform_short_name=None):  # noqa: E501
        """Departure - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._service_id = None
        self._suggested_departure = None
        self._headsign = None
        self._time_name = None
        self._short_name = None
        self._live_time = None
        self._scheduled_time = None
        self._frequency_seconds_range = None
        self._frequency_start_time = None
        self._frequency_end_time = None
        self._time_status = None
        self._platform_short_name = None
        self.discriminator = None
        self.type = type
        self.service_id = service_id
        if suggested_departure is not None:
            self.suggested_departure = suggested_departure
        if headsign is not None:
            self.headsign = headsign
        if time_name is not None:
            self.time_name = time_name
        if short_name is not None:
            self.short_name = short_name
        if live_time is not None:
            self.live_time = live_time
        if scheduled_time is not None:
            self.scheduled_time = scheduled_time
        if frequency_seconds_range is not None:
            self.frequency_seconds_range = frequency_seconds_range
        if frequency_start_time is not None:
            self.frequency_start_time = frequency_start_time
        if frequency_end_time is not None:
            self.frequency_end_time = frequency_end_time
        if time_status is not None:
            self.time_status = time_status
        if platform_short_name is not None:
            self.platform_short_name = platform_short_name

    @property
    def type(self):
        """Gets the type of this Departure.  # noqa: E501

        Indicates what type of departure this object represents:    | value | description | | ----- | ----------- | | scheduled | A scheduled departure at an exact time according to the published timetable, does not include real-time/live information | | frequency | An approximate departure frequency such as \"every 7 minutes\" or \"every 10-12 minutes\" | | live | Real-time information determined from vehicle tracking systems |   # noqa: E501

        :return: The type of this Departure.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Departure.

        Indicates what type of departure this object represents:    | value | description | | ----- | ----------- | | scheduled | A scheduled departure at an exact time according to the published timetable, does not include real-time/live information | | frequency | An approximate departure frequency such as \"every 7 minutes\" or \"every 10-12 minutes\" | | live | Real-time information determined from vehicle tracking systems |   # noqa: E501

        :param type: The type of this Departure.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["scheduled", "frequency", "live"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def service_id(self):
        """Gets the service_id of this Departure.  # noqa: E501

        Indicates which Service in the Leg this Departure refers to, in order to indicate Service and Brand naming and imagery. This is redundant in single-Service Legs, but it's essential in Legs that have alternate equivalent services.   # noqa: E501

        :return: The service_id of this Departure.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this Departure.

        Indicates which Service in the Leg this Departure refers to, in order to indicate Service and Brand naming and imagery. This is redundant in single-Service Legs, but it's essential in Legs that have alternate equivalent services.   # noqa: E501

        :param service_id: The service_id of this Departure.  # noqa: E501
        :type: str
        """
        if service_id is None:
            raise ValueError("Invalid value for `service_id`, must not be `None`")  # noqa: E501

        self._service_id = service_id

    @property
    def suggested_departure(self):
        """Gets the suggested_departure of this Departure.  # noqa: E501

        When Departures are given as part of a transit directions response in a Leg, the suggested_departure flag indicates whether Citymapper thinks this departure should be caught, following the estimated `route_departure_time` and subsequent `leg_departure_time` and `leg_arrival_time`s. Note that these times assume the user is at the start of the Route.  A value of `suggested` indicates that this departure is the one used to calculate the `leg_{depart,arrive}_time`, while `alternative` indicates that taking this departure would still result in arriving at the same final `route_arrival_time`.  This means that departures before the first one with this `suggested_departure` field are likely too early for the user to be able to catch, while those after could be taken but would result in a later arrival time than the estimated `route_arrival_time`.  If there are no estimated times (the Leg and Route don't have the `*_time` fields) then no Departures will have a `suggested_departure` field. In this case it is likely that the user cannot successfully complete this Route at this time.   # noqa: E501

        :return: The suggested_departure of this Departure.  # noqa: E501
        :rtype: str
        """
        return self._suggested_departure

    @suggested_departure.setter
    def suggested_departure(self, suggested_departure):
        """Sets the suggested_departure of this Departure.

        When Departures are given as part of a transit directions response in a Leg, the suggested_departure flag indicates whether Citymapper thinks this departure should be caught, following the estimated `route_departure_time` and subsequent `leg_departure_time` and `leg_arrival_time`s. Note that these times assume the user is at the start of the Route.  A value of `suggested` indicates that this departure is the one used to calculate the `leg_{depart,arrive}_time`, while `alternative` indicates that taking this departure would still result in arriving at the same final `route_arrival_time`.  This means that departures before the first one with this `suggested_departure` field are likely too early for the user to be able to catch, while those after could be taken but would result in a later arrival time than the estimated `route_arrival_time`.  If there are no estimated times (the Leg and Route don't have the `*_time` fields) then no Departures will have a `suggested_departure` field. In this case it is likely that the user cannot successfully complete this Route at this time.   # noqa: E501

        :param suggested_departure: The suggested_departure of this Departure.  # noqa: E501
        :type: str
        """
        allowed_values = ["suggested", "alternative"]  # noqa: E501
        if suggested_departure not in allowed_values:
            raise ValueError(
                "Invalid value for `suggested_departure` ({0}), must be one of {1}"  # noqa: E501
                .format(suggested_departure, allowed_values)
            )

        self._suggested_departure = suggested_departure

    @property
    def headsign(self):
        """Gets the headsign of this Departure.  # noqa: E501

        Text identifying the destination or pattern of this departure. This generally corresponds to text shown on the front of a transit vehicle. It will not include the Service or Brand name.   # noqa: E501

        :return: The headsign of this Departure.  # noqa: E501
        :rtype: str
        """
        return self._headsign

    @headsign.setter
    def headsign(self, headsign):
        """Sets the headsign of this Departure.

        Text identifying the destination or pattern of this departure. This generally corresponds to text shown on the front of a transit vehicle. It will not include the Service or Brand name.   # noqa: E501

        :param headsign: The headsign of this Departure.  # noqa: E501
        :type: str
        """

        self._headsign = headsign

    @property
    def time_name(self):
        """Gets the time_name of this Departure.  # noqa: E501

        A user-facing identifier for the scheduled time of this departure, effectively  the original time of the departure in the local format. It will only be present  where the scheduled time is commonly used as part of the name (typically along with the headsign) when referring to this departure in e.g. station announcements. A concrete example of this type of departure in an announcement might be the \"10:45 to Liverpool Street\", where \"10:45\" is the time_name, and \"Liverpool Street\" is the headsign  Most often used in rail systems, but can appear in other contexts like some intercity coach services   # noqa: E501

        :return: The time_name of this Departure.  # noqa: E501
        :rtype: str
        """
        return self._time_name

    @time_name.setter
    def time_name(self, time_name):
        """Sets the time_name of this Departure.

        A user-facing identifier for the scheduled time of this departure, effectively  the original time of the departure in the local format. It will only be present  where the scheduled time is commonly used as part of the name (typically along with the headsign) when referring to this departure in e.g. station announcements. A concrete example of this type of departure in an announcement might be the \"10:45 to Liverpool Street\", where \"10:45\" is the time_name, and \"Liverpool Street\" is the headsign  Most often used in rail systems, but can appear in other contexts like some intercity coach services   # noqa: E501

        :param time_name: The time_name of this Departure.  # noqa: E501
        :type: str
        """

        self._time_name = time_name

    @property
    def short_name(self):
        """Gets the short_name of this Departure.  # noqa: E501

        A user-facing identifier for this specific departure or class of departures. This is generally used in commuter rail systems as a train number.   # noqa: E501

        :return: The short_name of this Departure.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this Departure.

        A user-facing identifier for this specific departure or class of departures. This is generally used in commuter rail systems as a train number.   # noqa: E501

        :param short_name: The short_name of this Departure.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def live_time(self):
        """Gets the live_time of this Departure.  # noqa: E501

        (Only included when `type` is `live`.)  The current time when the service is expected to depart, based on live vehicle tracking.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone in which the event occurs. For example, `2020-08-19T08:10:42-04:00` expresses August 19, 2020 at 8:10am in Eastern Daylight Time.   # noqa: E501

        :return: The live_time of this Departure.  # noqa: E501
        :rtype: str
        """
        return self._live_time

    @live_time.setter
    def live_time(self, live_time):
        """Sets the live_time of this Departure.

        (Only included when `type` is `live`.)  The current time when the service is expected to depart, based on live vehicle tracking.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone in which the event occurs. For example, `2020-08-19T08:10:42-04:00` expresses August 19, 2020 at 8:10am in Eastern Daylight Time.   # noqa: E501

        :param live_time: The live_time of this Departure.  # noqa: E501
        :type: str
        """

        self._live_time = live_time

    @property
    def scheduled_time(self):
        """Gets the scheduled_time of this Departure.  # noqa: E501

        (Included when `type` is `scheduled` and sometimes `live`.)  The time when the service is expected to depart, according to the pre-published timetable. In departures with `type` of `live`, the `scheduled_time` is included when possible to indicate which timetabled departure the Citymapper service has associated the live departure with.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone in which the event occurs. For example, `2020-08-19T08:10:42-04:00` expresses August 19, 2020 at 8:10am in Eastern Daylight Time.   # noqa: E501

        :return: The scheduled_time of this Departure.  # noqa: E501
        :rtype: str
        """
        return self._scheduled_time

    @scheduled_time.setter
    def scheduled_time(self, scheduled_time):
        """Sets the scheduled_time of this Departure.

        (Included when `type` is `scheduled` and sometimes `live`.)  The time when the service is expected to depart, according to the pre-published timetable. In departures with `type` of `live`, the `scheduled_time` is included when possible to indicate which timetabled departure the Citymapper service has associated the live departure with.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone in which the event occurs. For example, `2020-08-19T08:10:42-04:00` expresses August 19, 2020 at 8:10am in Eastern Daylight Time.   # noqa: E501

        :param scheduled_time: The scheduled_time of this Departure.  # noqa: E501
        :type: str
        """

        self._scheduled_time = scheduled_time

    @property
    def frequency_seconds_range(self):
        """Gets the frequency_seconds_range of this Departure.  # noqa: E501

        (Included when `type` is `frequency`.)  The approximate time between departures during the time of day specified by `frequency_start_time` and `frequency_end_time`. The frequency is expressed as an array of two integers, which encode a range of  [headways](https://en.wikipedia.org/wiki/Headway).  For instance, a value of `[180, 300]` means that vehicles are expected to depart roughly every 3-5 minutes. Providing the same number twice indicates a simple headway rather than a range. For instance, the value `[750, 750]` means that the headway is every 12.5 minutes.  Multiple Departures with `type` of `frequency` can be returned in the same array, indicating how the frequency changes during different parts of the day. In this case, each Departure of `type` `frequency` will have a distinct `frequency_start_time` and `frequency_end_time` to indicate the time of day, along with the `frequency_seconds_range` expressing the service frequencies during that period.   # noqa: E501

        :return: The frequency_seconds_range of this Departure.  # noqa: E501
        :rtype: list[int]
        """
        return self._frequency_seconds_range

    @frequency_seconds_range.setter
    def frequency_seconds_range(self, frequency_seconds_range):
        """Sets the frequency_seconds_range of this Departure.

        (Included when `type` is `frequency`.)  The approximate time between departures during the time of day specified by `frequency_start_time` and `frequency_end_time`. The frequency is expressed as an array of two integers, which encode a range of  [headways](https://en.wikipedia.org/wiki/Headway).  For instance, a value of `[180, 300]` means that vehicles are expected to depart roughly every 3-5 minutes. Providing the same number twice indicates a simple headway rather than a range. For instance, the value `[750, 750]` means that the headway is every 12.5 minutes.  Multiple Departures with `type` of `frequency` can be returned in the same array, indicating how the frequency changes during different parts of the day. In this case, each Departure of `type` `frequency` will have a distinct `frequency_start_time` and `frequency_end_time` to indicate the time of day, along with the `frequency_seconds_range` expressing the service frequencies during that period.   # noqa: E501

        :param frequency_seconds_range: The frequency_seconds_range of this Departure.  # noqa: E501
        :type: list[int]
        """

        self._frequency_seconds_range = frequency_seconds_range

    @property
    def frequency_start_time(self):
        """Gets the frequency_start_time of this Departure.  # noqa: E501

        (Included when `type` is `frequency`.)  The beginning of the period in the day in which this service has the frequency expressed by `frequency_seconds_range`.   # noqa: E501

        :return: The frequency_start_time of this Departure.  # noqa: E501
        :rtype: str
        """
        return self._frequency_start_time

    @frequency_start_time.setter
    def frequency_start_time(self, frequency_start_time):
        """Sets the frequency_start_time of this Departure.

        (Included when `type` is `frequency`.)  The beginning of the period in the day in which this service has the frequency expressed by `frequency_seconds_range`.   # noqa: E501

        :param frequency_start_time: The frequency_start_time of this Departure.  # noqa: E501
        :type: str
        """

        self._frequency_start_time = frequency_start_time

    @property
    def frequency_end_time(self):
        """Gets the frequency_end_time of this Departure.  # noqa: E501

        (Included when `type` is `frequency`.)  The end of the period in the day in which this service has the frequency expressed by `frequency_seconds_range`.   # noqa: E501

        :return: The frequency_end_time of this Departure.  # noqa: E501
        :rtype: str
        """
        return self._frequency_end_time

    @frequency_end_time.setter
    def frequency_end_time(self, frequency_end_time):
        """Sets the frequency_end_time of this Departure.

        (Included when `type` is `frequency`.)  The end of the period in the day in which this service has the frequency expressed by `frequency_seconds_range`.   # noqa: E501

        :param frequency_end_time: The frequency_end_time of this Departure.  # noqa: E501
        :type: str
        """

        self._frequency_end_time = frequency_end_time

    @property
    def time_status(self):
        """Gets the time_status of this Departure.  # noqa: E501

        Indicates whether or not the service is on time. This is generally only provided for services where this information is commonly provided to the rider, for instance commuter trains.  | value | description | | ----- | ----------- | | unknown | The status of this departure is unknown (also signaled by the `time_status` property being omitted). | | on_time | This departure is on time. | | delay | This departure is running behind schedule. In this case, the amount of delay can be determined from the difference between `live_time` and `scheduled_time`. | | cancellation | This departure has been canceled and will no longer arrive. |   # noqa: E501

        :return: The time_status of this Departure.  # noqa: E501
        :rtype: str
        """
        return self._time_status

    @time_status.setter
    def time_status(self, time_status):
        """Sets the time_status of this Departure.

        Indicates whether or not the service is on time. This is generally only provided for services where this information is commonly provided to the rider, for instance commuter trains.  | value | description | | ----- | ----------- | | unknown | The status of this departure is unknown (also signaled by the `time_status` property being omitted). | | on_time | This departure is on time. | | delay | This departure is running behind schedule. In this case, the amount of delay can be determined from the difference between `live_time` and `scheduled_time`. | | cancellation | This departure has been canceled and will no longer arrive. |   # noqa: E501

        :param time_status: The time_status of this Departure.  # noqa: E501
        :type: str
        """
        allowed_values = ["unknown", "on_time", "delay", "cancellation"]  # noqa: E501
        if time_status not in allowed_values:
            raise ValueError(
                "Invalid value for `time_status` ({0}), must be one of {1}"  # noqa: E501
                .format(time_status, allowed_values)
            )

        self._time_status = time_status

    @property
    def platform_short_name(self):
        """Gets the platform_short_name of this Departure.  # noqa: E501

        A short string indicating the \"platform\" or \"track\", such as `18` or `A`, when available. This is only used for short identifiers that would appear next to the word \"Platform\" or \"Track\"; longer platform names that can be shown on their own will be passed in `direction_description` on TransitLeg instead.   # noqa: E501

        :return: The platform_short_name of this Departure.  # noqa: E501
        :rtype: str
        """
        return self._platform_short_name

    @platform_short_name.setter
    def platform_short_name(self, platform_short_name):
        """Sets the platform_short_name of this Departure.

        A short string indicating the \"platform\" or \"track\", such as `18` or `A`, when available. This is only used for short identifiers that would appear next to the word \"Platform\" or \"Track\"; longer platform names that can be shown on their own will be passed in `direction_description` on TransitLeg instead.   # noqa: E501

        :param platform_short_name: The platform_short_name of this Departure.  # noqa: E501
        :type: str
        """

        self._platform_short_name = platform_short_name

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
        if issubclass(Departure, dict):
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
        if not isinstance(other, Departure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
