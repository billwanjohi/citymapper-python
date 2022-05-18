# coding: utf-8

# flake8: noqa
"""
    Citymapper API

    # Introduction  ### Add journey planning and turn-by-turn navigation to your products with our APIs.  Our APIs are powered by our industry-leading global transport data and custom routing algorithms trained on billions of trips.  With our journey planning APIs you can:  - Calculate public transport routes and travel times - Retrieve live departure information for public transport routes - Calculate walk, cycling, e-scooter and motor scooter routes and travel times, including turn-by-turn instructions  Developing a mobile app? See our iOS and Android SDK [here](/).  <div class=\"cta\">  Ready to start?  <a class=\"button\" href=\"https://enterprise.citymapper.com/signup\">Get Access&ensp;&rarr;</a>  </div>  &nbsp;  ### Other resources  [SDK Docs](/)  [Deep Links](https://citymapper.com/news/2386/launch-citymapper-for-directions)  [Learn more about Powered by Citymapper](https://citymapper.com/enterprise)  # Support  ### Have questions?  Check out our FAQ [here](/support/faq.html).  ### Have product feedback or suggestions?  We'd love to hear about your experiences using our APIs, and features you'd like to see next. Please contribute feedback [here](https://form.jotform.com/213393057055353), and keep an eye out for future product releases.  ### Have a sales question?  If you are an enterprise user, or require functionality not available in our public APIs, our sales team are here to help.  Please [contact us](https://citymapper.com/contact/powered) with a description of your project or business need and we'll be in touch.  # Pricing  ### Get started for free  Get 5,000 monthly [requests](#requests) for free across all our products, making it easy to start building with our API or SDK.  <div class=\"cta\">  <a class=\"button\" href=\"https://enterprise.citymapper.com/signup\">Sign up&ensp;&rarr;</a>  </div>  &nbsp;  ### **Pay as you go**  Ready to launch? Scale quickly and flexibly with our pay-as-you-go plan.  Pick the products you need and only get charged for what you use – plus enjoy £100 free credit allowance from us each month.  To switch to the pay-as-you-go plan, please visit the [enterprise dashboard](https://enterprise.citymapper.com) and add a payment method. It’s that simple.  See below for our API pricing:  | Travel Time API           | Unit             | Price per Unit | | ------------------------- | ---------------- | -------------- | | Walk Travel Time          | per 1000 results | £0.40          | | Cycle Travel Time         | per 1000 results | £0.80          | | E-Scooter Travel Time     | per 1000 results | £0.80          | | Motor Scooter Travel Time | per 1000 results | £0.80          | | Transit Travel Time       | per 1000 results | £1.00          |  | Directions API                        | Unit                       | Price per Unit                     | | ------------------------------------- | -------------------------- | ---------------------------------- | | Walk Directions: Fast Profile         | per 1000 results           | £0.50                              | | Walk Directions: Main Roads Profile   | per 1000 results           | £0.50                              | | Cycle Directions: Quiet Profile       | per 1000 results           | £1.00                              | | Cycle Directions: Regular Profile     | per 1000 results           | £1.00                              | | Cycle Directions: Fast Profile        | per 1000 results           | £1.00                              | | E-Scooter Directions                  | per 1000 results           | £1.00                              | | Motor Scooter Directions              | per 1000 results           | £1.00                              | | Transit Directions                    | per 1000 routes\\*          | £1.20                              | | Transit Directions: Real-Time Updates | per 1000 route updates\\*\\* | Available on Enterprise plans only | | Hire Vehicle Directions               | per 1000 results           | Available on Enterprise plans only |  \\* Up to 5 transit routes can be returned in a single result  \\*\\* One update applies to a single transit route. Updates are refreshed every minute  ### Enterprise plans to help you grow  Looking for additional features or have higher volume requirements? Please [contact our sales team](https://citymapper.com/contact/powered).  ### Terms of service  Read the full [terms of service](https://citymapper.com/developer-terms).  ### Requests  A request is defined as a single call which successfully returns a travel time, directions or navigation result. Monthly requests are aggregated across all Powered by Citymapper products. If you're not on a paid plan, you’ll be notified via email once you exceed the free usage allowance in a given month (the month-long period aligns with the calendar month). Further requests will no longer return results for the remainder of that month, and your free usage allowance will reset at the start of the next month.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    OpenAPI spec version: v1.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from swagger_client.models.all_of_route_price import AllOfRoutePrice
from swagger_client.models.all_of_service_brand import AllOfServiceBrand
from swagger_client.models.all_of_station_exit_coordinates import AllOfStationExitCoordinates
from swagger_client.models.all_of_station_walk_details_recommended_exit import AllOfStationWalkDetailsRecommendedExit
from swagger_client.models.brand import Brand
from swagger_client.models.brand_image import BrandImage
from swagger_client.models.coordinates import Coordinates
from swagger_client.models.departure import Departure
from swagger_client.models.directions_response import DirectionsResponse
from swagger_client.models.duration_accuracy import DurationAccuracy
from swagger_client.models.error_response import ErrorResponse
from swagger_client.models.gateway_error import GatewayError
from swagger_client.models.hire_vehicle_leg_pickup import HireVehicleLegPickup
from swagger_client.models.hire_vehicle_metadata import HireVehicleMetadata
from swagger_client.models.hire_vehicle_station_leg_dropoff import HireVehicleStationLegDropoff
from swagger_client.models.hire_vehicle_station_metadata import HireVehicleStationMetadata
from swagger_client.models.image import Image
from swagger_client.models.inline_response200 import InlineResponse200
from swagger_client.models.instruction import Instruction
from swagger_client.models.instruction_description_format_replacements import InstructionDescriptionFormatReplacements
from swagger_client.models.leg import Leg
from swagger_client.models.leg_updatable_detail import LegUpdatableDetail
from swagger_client.models.leg_variant_self_piloted import LegVariantSelfPiloted
from swagger_client.models.leg_variant_services import LegVariantServices
from swagger_client.models.leg_variant_transit import LegVariantTransit
from swagger_client.models.leg_variant_transit_best_boarding_sections import LegVariantTransitBestBoardingSections
from swagger_client.models.leg_variant_walk import LegVariantWalk
from swagger_client.models.live_route_update_multiple_response import LiveRouteUpdateMultipleResponse
from swagger_client.models.live_route_update_response import LiveRouteUpdateResponse
from swagger_client.models.live_routeupdates_body import LiveRouteupdatesBody
from swagger_client.models.path_annotation import PathAnnotation
from swagger_client.models.price import Price
from swagger_client.models.route import Route
from swagger_client.models.route_group import RouteGroup
from swagger_client.models.route_metadata import RouteMetadata
from swagger_client.models.route_update import RouteUpdate
from swagger_client.models.service import Service
from swagger_client.models.service_image import ServiceImage
from swagger_client.models.station_exit import StationExit
from swagger_client.models.station_walk_details import StationWalkDetails
from swagger_client.models.status import Status
from swagger_client.models.status_service_stop_ranges import StatusServiceStopRanges
from swagger_client.models.stop import Stop
from swagger_client.models.vehicle_type import VehicleType
from swagger_client.models.waypoint import Waypoint
