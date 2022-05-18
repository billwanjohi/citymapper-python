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

class LegUpdatableDetail(object):
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
        'departures': 'list[Departure]',
        'live_departure_availability': 'str',
        'statuses': 'list[Status]',
        'leg_departure_time': 'str',
        'leg_arrival_time': 'str',
        'vehicle_pickup_places': 'list[HireVehicleLegPickup]',
        'vehicle_dropoff_places': 'list[HireVehicleStationLegDropoff]'
    }

    attribute_map = {
        'departures': 'departures',
        'live_departure_availability': 'live_departure_availability',
        'statuses': 'statuses',
        'leg_departure_time': 'leg_departure_time',
        'leg_arrival_time': 'leg_arrival_time',
        'vehicle_pickup_places': 'vehicle_pickup_places',
        'vehicle_dropoff_places': 'vehicle_dropoff_places'
    }

    def __init__(self, departures=None, live_departure_availability=None, statuses=None, leg_departure_time=None, leg_arrival_time=None, vehicle_pickup_places=None, vehicle_dropoff_places=None):  # noqa: E501
        """LegUpdatableDetail - a model defined in Swagger"""  # noqa: E501
        self._departures = None
        self._live_departure_availability = None
        self._statuses = None
        self._leg_departure_time = None
        self._leg_arrival_time = None
        self._vehicle_pickup_places = None
        self._vehicle_dropoff_places = None
        self.discriminator = None
        if departures is not None:
            self.departures = departures
        if live_departure_availability is not None:
            self.live_departure_availability = live_departure_availability
        if statuses is not None:
            self.statuses = statuses
        if leg_departure_time is not None:
            self.leg_departure_time = leg_departure_time
        if leg_arrival_time is not None:
            self.leg_arrival_time = leg_arrival_time
        if vehicle_pickup_places is not None:
            self.vehicle_pickup_places = vehicle_pickup_places
        if vehicle_dropoff_places is not None:
            self.vehicle_dropoff_places = vehicle_dropoff_places

    @property
    def departures(self):
        """Gets the departures of this LegUpdatableDetail.  # noqa: E501

        An array of Departure objects, giving alternate departures for the services in the Legs in which this property appears. The array can contain a mixture of different Departure `type`s—for example, it's common to receive `live` information for the next few departures, followed by `scheduled` information. For legs with multiple alternate Services, this array is likely to contain a mixture of departures corresponding to the different alternate services.  The number of Departures returned will depend on the availability of information.   # noqa: E501

        :return: The departures of this LegUpdatableDetail.  # noqa: E501
        :rtype: list[Departure]
        """
        return self._departures

    @departures.setter
    def departures(self, departures):
        """Sets the departures of this LegUpdatableDetail.

        An array of Departure objects, giving alternate departures for the services in the Legs in which this property appears. The array can contain a mixture of different Departure `type`s—for example, it's common to receive `live` information for the next few departures, followed by `scheduled` information. For legs with multiple alternate Services, this array is likely to contain a mixture of departures corresponding to the different alternate services.  The number of Departures returned will depend on the availability of information.   # noqa: E501

        :param departures: The departures of this LegUpdatableDetail.  # noqa: E501
        :type: list[Departure]
        """

        self._departures = departures

    @property
    def live_departure_availability(self):
        """Gets the live_departure_availability of this LegUpdatableDetail.  # noqa: E501

        This indicates the availability of live departure information for the Services used in this Leg. Live departure information is not available for all transit services, and some transit services have live information that cannot be determined quickly enough to be included in all requests. The value of this property characterizes the contents of the `departures` array in this Leg Updatable Detail, and indicates whether an additional request is likely to yield additional live times for this Leg.  | value | description | | ----- | ----------- | | unknown | The availability of live departure information can't be determined | | none_available | No live departure information is available for the services used in this leg. Typically the `departures` list will contain entries of type `scheduled` or `frequency` in this case | | included | Live departure information is available for the services in this Leg, and it is included in the `departures` list | | additional_request | Live information is available for the services in this Leg, but some of it will require an additional `/api/1/live/routeupdate` request to retrieve |   # noqa: E501

        :return: The live_departure_availability of this LegUpdatableDetail.  # noqa: E501
        :rtype: str
        """
        return self._live_departure_availability

    @live_departure_availability.setter
    def live_departure_availability(self, live_departure_availability):
        """Sets the live_departure_availability of this LegUpdatableDetail.

        This indicates the availability of live departure information for the Services used in this Leg. Live departure information is not available for all transit services, and some transit services have live information that cannot be determined quickly enough to be included in all requests. The value of this property characterizes the contents of the `departures` array in this Leg Updatable Detail, and indicates whether an additional request is likely to yield additional live times for this Leg.  | value | description | | ----- | ----------- | | unknown | The availability of live departure information can't be determined | | none_available | No live departure information is available for the services used in this leg. Typically the `departures` list will contain entries of type `scheduled` or `frequency` in this case | | included | Live departure information is available for the services in this Leg, and it is included in the `departures` list | | additional_request | Live information is available for the services in this Leg, but some of it will require an additional `/api/1/live/routeupdate` request to retrieve |   # noqa: E501

        :param live_departure_availability: The live_departure_availability of this LegUpdatableDetail.  # noqa: E501
        :type: str
        """
        allowed_values = ["unknown", "none_available", "included", "additional_request"]  # noqa: E501
        if live_departure_availability not in allowed_values:
            raise ValueError(
                "Invalid value for `live_departure_availability` ({0}), must be one of {1}"  # noqa: E501
                .format(live_departure_availability, allowed_values)
            )

        self._live_departure_availability = live_departure_availability

    @property
    def statuses(self):
        """Gets the statuses of this LegUpdatableDetail.  # noqa: E501

        An array of Status objects that relate to this Leg.   # noqa: E501

        :return: The statuses of this LegUpdatableDetail.  # noqa: E501
        :rtype: list[Status]
        """
        return self._statuses

    @statuses.setter
    def statuses(self, statuses):
        """Sets the statuses of this LegUpdatableDetail.

        An array of Status objects that relate to this Leg.   # noqa: E501

        :param statuses: The statuses of this LegUpdatableDetail.  # noqa: E501
        :type: list[Status]
        """

        self._statuses = statuses

    @property
    def leg_departure_time(self):
        """Gets the leg_departure_time of this LegUpdatableDetail.  # noqa: E501

        The time at which Citymapper thinks the user will set out on this leg, given available departure information. In the case of Legs of `travel_type` `transit`, this excludes waiting time.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone in which the event occurs. For example, `2020-08-19T08:10:42-04:00` expresses August 19, 2020 at 8:10am in Eastern Daylight Time.   # noqa: E501

        :return: The leg_departure_time of this LegUpdatableDetail.  # noqa: E501
        :rtype: str
        """
        return self._leg_departure_time

    @leg_departure_time.setter
    def leg_departure_time(self, leg_departure_time):
        """Sets the leg_departure_time of this LegUpdatableDetail.

        The time at which Citymapper thinks the user will set out on this leg, given available departure information. In the case of Legs of `travel_type` `transit`, this excludes waiting time.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone in which the event occurs. For example, `2020-08-19T08:10:42-04:00` expresses August 19, 2020 at 8:10am in Eastern Daylight Time.   # noqa: E501

        :param leg_departure_time: The leg_departure_time of this LegUpdatableDetail.  # noqa: E501
        :type: str
        """

        self._leg_departure_time = leg_departure_time

    @property
    def leg_arrival_time(self):
        """Gets the leg_arrival_time of this LegUpdatableDetail.  # noqa: E501

        The time at which Citymapper thinks the user will arrive at the end of this leg, given available departure information and expected travel speed.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone in which the event occurs. For example, `2020-08-19T08:10:42-04:00` expresses August 19, 2020 at 8:10am in Eastern Daylight Time.   # noqa: E501

        :return: The leg_arrival_time of this LegUpdatableDetail.  # noqa: E501
        :rtype: str
        """
        return self._leg_arrival_time

    @leg_arrival_time.setter
    def leg_arrival_time(self, leg_arrival_time):
        """Sets the leg_arrival_time of this LegUpdatableDetail.

        The time at which Citymapper thinks the user will arrive at the end of this leg, given available departure information and expected travel speed.  The time is expressed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, including a date, time, and time zone in which the event occurs. For example, `2020-08-19T08:10:42-04:00` expresses August 19, 2020 at 8:10am in Eastern Daylight Time.   # noqa: E501

        :param leg_arrival_time: The leg_arrival_time of this LegUpdatableDetail.  # noqa: E501
        :type: str
        """

        self._leg_arrival_time = leg_arrival_time

    @property
    def vehicle_pickup_places(self):
        """Gets the vehicle_pickup_places of this LegUpdatableDetail.  # noqa: E501

        Included in a `self_piloted` leg which involves a hire vehicle. Indicates the locations where the user can pick up a vehicle used to complete the leg. The listed places are the ones determined to be the \"best\" places to pick up a vehicle - they might not always be the closest by crow-flies distance.  The item in the list marked with `\"suggested\": true` is the one that corresponds to the rest of the data in this leg (and any preceeding walk leg). To support situations where new vehicles come available, and  extensions to this API where the user can change the selected vehicle while keeping the order stable,  the suggested location may not necessarily be at the top of the list.  One of `hire_vehicle` or `hire_vehicle_station` will be populated for each item in the list.   # noqa: E501

        :return: The vehicle_pickup_places of this LegUpdatableDetail.  # noqa: E501
        :rtype: list[HireVehicleLegPickup]
        """
        return self._vehicle_pickup_places

    @vehicle_pickup_places.setter
    def vehicle_pickup_places(self, vehicle_pickup_places):
        """Sets the vehicle_pickup_places of this LegUpdatableDetail.

        Included in a `self_piloted` leg which involves a hire vehicle. Indicates the locations where the user can pick up a vehicle used to complete the leg. The listed places are the ones determined to be the \"best\" places to pick up a vehicle - they might not always be the closest by crow-flies distance.  The item in the list marked with `\"suggested\": true` is the one that corresponds to the rest of the data in this leg (and any preceeding walk leg). To support situations where new vehicles come available, and  extensions to this API where the user can change the selected vehicle while keeping the order stable,  the suggested location may not necessarily be at the top of the list.  One of `hire_vehicle` or `hire_vehicle_station` will be populated for each item in the list.   # noqa: E501

        :param vehicle_pickup_places: The vehicle_pickup_places of this LegUpdatableDetail.  # noqa: E501
        :type: list[HireVehicleLegPickup]
        """

        self._vehicle_pickup_places = vehicle_pickup_places

    @property
    def vehicle_dropoff_places(self):
        """Gets the vehicle_dropoff_places of this LegUpdatableDetail.  # noqa: E501

        May be included in a `self_piloted` leg which involves a hire vehicle. Indicates the locations where can drop off the vehicle used to complete the leg. The listed places are the ones determined to be the \"best\" places to drop the vehicle off - they might not always be the ones closest to the eventual  destination by crow-flies distance.  The item in the list marked with `\"suggested\": true` is the one that corresponds to the rest of the data in this leg (and any subsequent walk leg). To support extensions to this API where the user can change the selected vehicle while keeping the order stable, the suggested location may not necessarily be at the top of the list.  If this drop-off location is at a vehicle docking station, the `hire_vehicle_station` property will be included with metadata about the station. Otherwise, the parking location represents either a marked area on the road or  sidewalk/pavement where vehicles of this type can be left, or simply a place within the allowed parking zone  close to the destination of this part of the Route.   # noqa: E501

        :return: The vehicle_dropoff_places of this LegUpdatableDetail.  # noqa: E501
        :rtype: list[HireVehicleStationLegDropoff]
        """
        return self._vehicle_dropoff_places

    @vehicle_dropoff_places.setter
    def vehicle_dropoff_places(self, vehicle_dropoff_places):
        """Sets the vehicle_dropoff_places of this LegUpdatableDetail.

        May be included in a `self_piloted` leg which involves a hire vehicle. Indicates the locations where can drop off the vehicle used to complete the leg. The listed places are the ones determined to be the \"best\" places to drop the vehicle off - they might not always be the ones closest to the eventual  destination by crow-flies distance.  The item in the list marked with `\"suggested\": true` is the one that corresponds to the rest of the data in this leg (and any subsequent walk leg). To support extensions to this API where the user can change the selected vehicle while keeping the order stable, the suggested location may not necessarily be at the top of the list.  If this drop-off location is at a vehicle docking station, the `hire_vehicle_station` property will be included with metadata about the station. Otherwise, the parking location represents either a marked area on the road or  sidewalk/pavement where vehicles of this type can be left, or simply a place within the allowed parking zone  close to the destination of this part of the Route.   # noqa: E501

        :param vehicle_dropoff_places: The vehicle_dropoff_places of this LegUpdatableDetail.  # noqa: E501
        :type: list[HireVehicleStationLegDropoff]
        """

        self._vehicle_dropoff_places = vehicle_dropoff_places

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
        if issubclass(LegUpdatableDetail, dict):
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
        if not isinstance(other, LegUpdatableDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
