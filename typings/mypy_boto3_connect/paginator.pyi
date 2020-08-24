# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for connect service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_connect import ConnectClient
    from mypy_boto3_connect.paginator import (
        GetMetricDataPaginator,
        ListContactFlowsPaginator,
        ListHoursOfOperationsPaginator,
        ListPhoneNumbersPaginator,
        ListQueuesPaginator,
        ListRoutingProfilesPaginator,
        ListSecurityProfilesPaginator,
        ListUserHierarchyGroupsPaginator,
        ListUsersPaginator,
    )

    client: ConnectClient = boto3.client("connect")

    get_metric_data_paginator: GetMetricDataPaginator = client.get_paginator("get_metric_data")
    list_contact_flows_paginator: ListContactFlowsPaginator = client.get_paginator("list_contact_flows")
    list_hours_of_operations_paginator: ListHoursOfOperationsPaginator = client.get_paginator("list_hours_of_operations")
    list_phone_numbers_paginator: ListPhoneNumbersPaginator = client.get_paginator("list_phone_numbers")
    list_queues_paginator: ListQueuesPaginator = client.get_paginator("list_queues")
    list_routing_profiles_paginator: ListRoutingProfilesPaginator = client.get_paginator("list_routing_profiles")
    list_security_profiles_paginator: ListSecurityProfilesPaginator = client.get_paginator("list_security_profiles")
    list_user_hierarchy_groups_paginator: ListUserHierarchyGroupsPaginator = client.get_paginator("list_user_hierarchy_groups")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    ```
"""
import sys
from datetime import datetime
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_connect.type_defs import (
    FiltersTypeDef,
    GetMetricDataResponseTypeDef,
    HistoricalMetricTypeDef,
    ListContactFlowsResponseTypeDef,
    ListHoursOfOperationsResponseTypeDef,
    ListPhoneNumbersResponseTypeDef,
    ListQueuesResponseTypeDef,
    ListRoutingProfilesResponseTypeDef,
    ListSecurityProfilesResponseTypeDef,
    ListUserHierarchyGroupsResponseTypeDef,
    ListUsersResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetMetricDataPaginator",
    "ListContactFlowsPaginator",
    "ListHoursOfOperationsPaginator",
    "ListPhoneNumbersPaginator",
    "ListQueuesPaginator",
    "ListRoutingProfilesPaginator",
    "ListSecurityProfilesPaginator",
    "ListUserHierarchyGroupsPaginator",
    "ListUsersPaginator",
)


class GetMetricDataPaginator(Boto3Paginator):
    """
    [Paginator.GetMetricData documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/connect.html#Connect.Paginator.GetMetricData)
    """

    def paginate(
        self,
        InstanceId: str,
        StartTime: datetime,
        EndTime: datetime,
        Filters: FiltersTypeDef,
        HistoricalMetrics: List["HistoricalMetricTypeDef"],
        Groupings: List[Literal["QUEUE", "CHANNEL"]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetMetricDataResponseTypeDef]:
        """
        [GetMetricData.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/connect.html#Connect.Paginator.GetMetricData.paginate)
        """


class ListContactFlowsPaginator(Boto3Paginator):
    """
    [Paginator.ListContactFlows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/connect.html#Connect.Paginator.ListContactFlows)
    """

    def paginate(
        self,
        InstanceId: str,
        ContactFlowTypes: List[
            Literal[
                "CONTACT_FLOW",
                "CUSTOMER_QUEUE",
                "CUSTOMER_HOLD",
                "CUSTOMER_WHISPER",
                "AGENT_HOLD",
                "AGENT_WHISPER",
                "OUTBOUND_WHISPER",
                "AGENT_TRANSFER",
                "QUEUE_TRANSFER",
            ]
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListContactFlowsResponseTypeDef]:
        """
        [ListContactFlows.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/connect.html#Connect.Paginator.ListContactFlows.paginate)
        """


class ListHoursOfOperationsPaginator(Boto3Paginator):
    """
    [Paginator.ListHoursOfOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/connect.html#Connect.Paginator.ListHoursOfOperations)
    """

    def paginate(
        self, InstanceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHoursOfOperationsResponseTypeDef]:
        """
        [ListHoursOfOperations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/connect.html#Connect.Paginator.ListHoursOfOperations.paginate)
        """


class ListPhoneNumbersPaginator(Boto3Paginator):
    """
    [Paginator.ListPhoneNumbers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/connect.html#Connect.Paginator.ListPhoneNumbers)
    """

    def paginate(
        self,
        InstanceId: str,
        PhoneNumberTypes: List[Literal["TOLL_FREE", "DID"]] = None,
        PhoneNumberCountryCodes: List[
            Literal[
                "AF",
                "AL",
                "DZ",
                "AS",
                "AD",
                "AO",
                "AI",
                "AQ",
                "AG",
                "AR",
                "AM",
                "AW",
                "AU",
                "AT",
                "AZ",
                "BS",
                "BH",
                "BD",
                "BB",
                "BY",
                "BE",
                "BZ",
                "BJ",
                "BM",
                "BT",
                "BO",
                "BA",
                "BW",
                "BR",
                "IO",
                "VG",
                "BN",
                "BG",
                "BF",
                "BI",
                "KH",
                "CM",
                "CA",
                "CV",
                "KY",
                "CF",
                "TD",
                "CL",
                "CN",
                "CX",
                "CC",
                "CO",
                "KM",
                "CK",
                "CR",
                "HR",
                "CU",
                "CW",
                "CY",
                "CZ",
                "CD",
                "DK",
                "DJ",
                "DM",
                "DO",
                "TL",
                "EC",
                "EG",
                "SV",
                "GQ",
                "ER",
                "EE",
                "ET",
                "FK",
                "FO",
                "FJ",
                "FI",
                "FR",
                "PF",
                "GA",
                "GM",
                "GE",
                "DE",
                "GH",
                "GI",
                "GR",
                "GL",
                "GD",
                "GU",
                "GT",
                "GG",
                "GN",
                "GW",
                "GY",
                "HT",
                "HN",
                "HK",
                "HU",
                "IS",
                "IN",
                "ID",
                "IR",
                "IQ",
                "IE",
                "IM",
                "IL",
                "IT",
                "CI",
                "JM",
                "JP",
                "JE",
                "JO",
                "KZ",
                "KE",
                "KI",
                "KW",
                "KG",
                "LA",
                "LV",
                "LB",
                "LS",
                "LR",
                "LY",
                "LI",
                "LT",
                "LU",
                "MO",
                "MK",
                "MG",
                "MW",
                "MY",
                "MV",
                "ML",
                "MT",
                "MH",
                "MR",
                "MU",
                "YT",
                "MX",
                "FM",
                "MD",
                "MC",
                "MN",
                "ME",
                "MS",
                "MA",
                "MZ",
                "MM",
                "NA",
                "NR",
                "NP",
                "NL",
                "AN",
                "NC",
                "NZ",
                "NI",
                "NE",
                "NG",
                "NU",
                "KP",
                "MP",
                "NO",
                "OM",
                "PK",
                "PW",
                "PA",
                "PG",
                "PY",
                "PE",
                "PH",
                "PN",
                "PL",
                "PT",
                "PR",
                "QA",
                "CG",
                "RE",
                "RO",
                "RU",
                "RW",
                "BL",
                "SH",
                "KN",
                "LC",
                "MF",
                "PM",
                "VC",
                "WS",
                "SM",
                "ST",
                "SA",
                "SN",
                "RS",
                "SC",
                "SL",
                "SG",
                "SX",
                "SK",
                "SI",
                "SB",
                "SO",
                "ZA",
                "KR",
                "ES",
                "LK",
                "SD",
                "SR",
                "SJ",
                "SZ",
                "SE",
                "CH",
                "SY",
                "TW",
                "TJ",
                "TZ",
                "TH",
                "TG",
                "TK",
                "TO",
                "TT",
                "TN",
                "TR",
                "TM",
                "TC",
                "TV",
                "VI",
                "UG",
                "UA",
                "AE",
                "GB",
                "US",
                "UY",
                "UZ",
                "VU",
                "VA",
                "VE",
                "VN",
                "WF",
                "EH",
                "YE",
                "ZM",
                "ZW",
            ]
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListPhoneNumbersResponseTypeDef]:
        """
        [ListPhoneNumbers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/connect.html#Connect.Paginator.ListPhoneNumbers.paginate)
        """


class ListQueuesPaginator(Boto3Paginator):
    """
    [Paginator.ListQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/connect.html#Connect.Paginator.ListQueues)
    """

    def paginate(
        self,
        InstanceId: str,
        QueueTypes: List[Literal["STANDARD", "AGENT"]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListQueuesResponseTypeDef]:
        """
        [ListQueues.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/connect.html#Connect.Paginator.ListQueues.paginate)
        """


class ListRoutingProfilesPaginator(Boto3Paginator):
    """
    [Paginator.ListRoutingProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/connect.html#Connect.Paginator.ListRoutingProfiles)
    """

    def paginate(
        self, InstanceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRoutingProfilesResponseTypeDef]:
        """
        [ListRoutingProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/connect.html#Connect.Paginator.ListRoutingProfiles.paginate)
        """


class ListSecurityProfilesPaginator(Boto3Paginator):
    """
    [Paginator.ListSecurityProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/connect.html#Connect.Paginator.ListSecurityProfiles)
    """

    def paginate(
        self, InstanceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSecurityProfilesResponseTypeDef]:
        """
        [ListSecurityProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/connect.html#Connect.Paginator.ListSecurityProfiles.paginate)
        """


class ListUserHierarchyGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListUserHierarchyGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/connect.html#Connect.Paginator.ListUserHierarchyGroups)
    """

    def paginate(
        self, InstanceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUserHierarchyGroupsResponseTypeDef]:
        """
        [ListUserHierarchyGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/connect.html#Connect.Paginator.ListUserHierarchyGroups.paginate)
        """


class ListUsersPaginator(Boto3Paginator):
    """
    [Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/connect.html#Connect.Paginator.ListUsers)
    """

    def paginate(
        self, InstanceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUsersResponseTypeDef]:
        """
        [ListUsers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/connect.html#Connect.Paginator.ListUsers.paginate)
        """
