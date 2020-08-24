"""
Main interface for connect service type definitions.

Usage::

    ```python
    from mypy_boto3_connect.type_defs import ContactFlowSummaryTypeDef

    data: ContactFlowSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ContactFlowSummaryTypeDef",
    "CredentialsTypeDef",
    "CurrentMetricDataTypeDef",
    "CurrentMetricResultTypeDef",
    "CurrentMetricTypeDef",
    "DimensionsTypeDef",
    "HierarchyGroupSummaryTypeDef",
    "HierarchyGroupTypeDef",
    "HierarchyLevelTypeDef",
    "HierarchyPathTypeDef",
    "HierarchyStructureTypeDef",
    "HistoricalMetricDataTypeDef",
    "HistoricalMetricResultTypeDef",
    "HistoricalMetricTypeDef",
    "HoursOfOperationSummaryTypeDef",
    "PhoneNumberSummaryTypeDef",
    "QueueReferenceTypeDef",
    "QueueSummaryTypeDef",
    "RoutingProfileSummaryTypeDef",
    "SecurityProfileSummaryTypeDef",
    "ThresholdTypeDef",
    "UserIdentityInfoTypeDef",
    "UserPhoneConfigTypeDef",
    "UserSummaryTypeDef",
    "UserTypeDef",
    "ChatMessageTypeDef",
    "CreateUserResponseTypeDef",
    "DescribeUserHierarchyGroupResponseTypeDef",
    "DescribeUserHierarchyStructureResponseTypeDef",
    "DescribeUserResponseTypeDef",
    "FiltersTypeDef",
    "GetContactAttributesResponseTypeDef",
    "GetCurrentMetricDataResponseTypeDef",
    "GetFederationTokenResponseTypeDef",
    "GetMetricDataResponseTypeDef",
    "ListContactFlowsResponseTypeDef",
    "ListHoursOfOperationsResponseTypeDef",
    "ListPhoneNumbersResponseTypeDef",
    "ListQueuesResponseTypeDef",
    "ListRoutingProfilesResponseTypeDef",
    "ListSecurityProfilesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUserHierarchyGroupsResponseTypeDef",
    "ListUsersResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipantDetailsTypeDef",
    "StartChatContactResponseTypeDef",
    "StartOutboundVoiceContactResponseTypeDef",
    "VoiceRecordingConfigurationTypeDef",
)

ContactFlowSummaryTypeDef = TypedDict(
    "ContactFlowSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "ContactFlowType": Literal[
            "CONTACT_FLOW",
            "CUSTOMER_QUEUE",
            "CUSTOMER_HOLD",
            "CUSTOMER_WHISPER",
            "AGENT_HOLD",
            "AGENT_WHISPER",
            "OUTBOUND_WHISPER",
            "AGENT_TRANSFER",
            "QUEUE_TRANSFER",
        ],
    },
    total=False,
)

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "AccessToken": str,
        "AccessTokenExpiration": datetime,
        "RefreshToken": str,
        "RefreshTokenExpiration": datetime,
    },
    total=False,
)

CurrentMetricDataTypeDef = TypedDict(
    "CurrentMetricDataTypeDef", {"Metric": "CurrentMetricTypeDef", "Value": float}, total=False
)

CurrentMetricResultTypeDef = TypedDict(
    "CurrentMetricResultTypeDef",
    {"Dimensions": "DimensionsTypeDef", "Collections": List["CurrentMetricDataTypeDef"]},
    total=False,
)

CurrentMetricTypeDef = TypedDict(
    "CurrentMetricTypeDef",
    {
        "Name": Literal[
            "AGENTS_ONLINE",
            "AGENTS_AVAILABLE",
            "AGENTS_ON_CALL",
            "AGENTS_NON_PRODUCTIVE",
            "AGENTS_AFTER_CONTACT_WORK",
            "AGENTS_ERROR",
            "AGENTS_STAFFED",
            "CONTACTS_IN_QUEUE",
            "OLDEST_CONTACT_AGE",
            "CONTACTS_SCHEDULED",
            "AGENTS_ON_CONTACT",
            "SLOTS_ACTIVE",
            "SLOTS_AVAILABLE",
        ],
        "Unit": Literal["SECONDS", "COUNT", "PERCENT"],
    },
    total=False,
)

DimensionsTypeDef = TypedDict(
    "DimensionsTypeDef",
    {"Queue": "QueueReferenceTypeDef", "Channel": Literal["VOICE", "CHAT"]},
    total=False,
)

HierarchyGroupSummaryTypeDef = TypedDict(
    "HierarchyGroupSummaryTypeDef", {"Id": str, "Arn": str, "Name": str}, total=False
)

HierarchyGroupTypeDef = TypedDict(
    "HierarchyGroupTypeDef",
    {"Id": str, "Arn": str, "Name": str, "LevelId": str, "HierarchyPath": "HierarchyPathTypeDef"},
    total=False,
)

HierarchyLevelTypeDef = TypedDict(
    "HierarchyLevelTypeDef", {"Id": str, "Arn": str, "Name": str}, total=False
)

HierarchyPathTypeDef = TypedDict(
    "HierarchyPathTypeDef",
    {
        "LevelOne": "HierarchyGroupSummaryTypeDef",
        "LevelTwo": "HierarchyGroupSummaryTypeDef",
        "LevelThree": "HierarchyGroupSummaryTypeDef",
        "LevelFour": "HierarchyGroupSummaryTypeDef",
        "LevelFive": "HierarchyGroupSummaryTypeDef",
    },
    total=False,
)

HierarchyStructureTypeDef = TypedDict(
    "HierarchyStructureTypeDef",
    {
        "LevelOne": "HierarchyLevelTypeDef",
        "LevelTwo": "HierarchyLevelTypeDef",
        "LevelThree": "HierarchyLevelTypeDef",
        "LevelFour": "HierarchyLevelTypeDef",
        "LevelFive": "HierarchyLevelTypeDef",
    },
    total=False,
)

HistoricalMetricDataTypeDef = TypedDict(
    "HistoricalMetricDataTypeDef",
    {"Metric": "HistoricalMetricTypeDef", "Value": float},
    total=False,
)

HistoricalMetricResultTypeDef = TypedDict(
    "HistoricalMetricResultTypeDef",
    {"Dimensions": "DimensionsTypeDef", "Collections": List["HistoricalMetricDataTypeDef"]},
    total=False,
)

HistoricalMetricTypeDef = TypedDict(
    "HistoricalMetricTypeDef",
    {
        "Name": Literal[
            "CONTACTS_QUEUED",
            "CONTACTS_HANDLED",
            "CONTACTS_ABANDONED",
            "CONTACTS_CONSULTED",
            "CONTACTS_AGENT_HUNG_UP_FIRST",
            "CONTACTS_HANDLED_INCOMING",
            "CONTACTS_HANDLED_OUTBOUND",
            "CONTACTS_HOLD_ABANDONS",
            "CONTACTS_TRANSFERRED_IN",
            "CONTACTS_TRANSFERRED_OUT",
            "CONTACTS_TRANSFERRED_IN_FROM_QUEUE",
            "CONTACTS_TRANSFERRED_OUT_FROM_QUEUE",
            "CONTACTS_MISSED",
            "CALLBACK_CONTACTS_HANDLED",
            "API_CONTACTS_HANDLED",
            "OCCUPANCY",
            "HANDLE_TIME",
            "AFTER_CONTACT_WORK_TIME",
            "QUEUED_TIME",
            "ABANDON_TIME",
            "QUEUE_ANSWER_TIME",
            "HOLD_TIME",
            "INTERACTION_TIME",
            "INTERACTION_AND_HOLD_TIME",
            "SERVICE_LEVEL",
        ],
        "Threshold": "ThresholdTypeDef",
        "Statistic": Literal["SUM", "MAX", "AVG"],
        "Unit": Literal["SECONDS", "COUNT", "PERCENT"],
    },
    total=False,
)

HoursOfOperationSummaryTypeDef = TypedDict(
    "HoursOfOperationSummaryTypeDef", {"Id": str, "Arn": str, "Name": str}, total=False
)

PhoneNumberSummaryTypeDef = TypedDict(
    "PhoneNumberSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "PhoneNumber": str,
        "PhoneNumberType": Literal["TOLL_FREE", "DID"],
        "PhoneNumberCountryCode": Literal[
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
        ],
    },
    total=False,
)

QueueReferenceTypeDef = TypedDict("QueueReferenceTypeDef", {"Id": str, "Arn": str}, total=False)

QueueSummaryTypeDef = TypedDict(
    "QueueSummaryTypeDef",
    {"Id": str, "Arn": str, "Name": str, "QueueType": Literal["STANDARD", "AGENT"]},
    total=False,
)

RoutingProfileSummaryTypeDef = TypedDict(
    "RoutingProfileSummaryTypeDef", {"Id": str, "Arn": str, "Name": str}, total=False
)

SecurityProfileSummaryTypeDef = TypedDict(
    "SecurityProfileSummaryTypeDef", {"Id": str, "Arn": str, "Name": str}, total=False
)

ThresholdTypeDef = TypedDict(
    "ThresholdTypeDef", {"Comparison": Literal["LT"], "ThresholdValue": float}, total=False
)

UserIdentityInfoTypeDef = TypedDict(
    "UserIdentityInfoTypeDef", {"FirstName": str, "LastName": str, "Email": str}, total=False
)

_RequiredUserPhoneConfigTypeDef = TypedDict(
    "_RequiredUserPhoneConfigTypeDef", {"PhoneType": Literal["SOFT_PHONE", "DESK_PHONE"]}
)
_OptionalUserPhoneConfigTypeDef = TypedDict(
    "_OptionalUserPhoneConfigTypeDef",
    {"AutoAccept": bool, "AfterContactWorkTimeLimit": int, "DeskPhoneNumber": str},
    total=False,
)


class UserPhoneConfigTypeDef(_RequiredUserPhoneConfigTypeDef, _OptionalUserPhoneConfigTypeDef):
    pass


UserSummaryTypeDef = TypedDict(
    "UserSummaryTypeDef", {"Id": str, "Arn": str, "Username": str}, total=False
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Username": str,
        "IdentityInfo": "UserIdentityInfoTypeDef",
        "PhoneConfig": "UserPhoneConfigTypeDef",
        "DirectoryUserId": str,
        "SecurityProfileIds": List[str],
        "RoutingProfileId": str,
        "HierarchyGroupId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ChatMessageTypeDef = TypedDict("ChatMessageTypeDef", {"ContentType": str, "Content": str})

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef", {"UserId": str, "UserArn": str}, total=False
)

DescribeUserHierarchyGroupResponseTypeDef = TypedDict(
    "DescribeUserHierarchyGroupResponseTypeDef",
    {"HierarchyGroup": "HierarchyGroupTypeDef"},
    total=False,
)

DescribeUserHierarchyStructureResponseTypeDef = TypedDict(
    "DescribeUserHierarchyStructureResponseTypeDef",
    {"HierarchyStructure": "HierarchyStructureTypeDef"},
    total=False,
)

DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef", {"User": "UserTypeDef"}, total=False
)

FiltersTypeDef = TypedDict(
    "FiltersTypeDef", {"Queues": List[str], "Channels": List[Literal["VOICE", "CHAT"]]}, total=False
)

GetContactAttributesResponseTypeDef = TypedDict(
    "GetContactAttributesResponseTypeDef", {"Attributes": Dict[str, str]}, total=False
)

GetCurrentMetricDataResponseTypeDef = TypedDict(
    "GetCurrentMetricDataResponseTypeDef",
    {
        "NextToken": str,
        "MetricResults": List["CurrentMetricResultTypeDef"],
        "DataSnapshotTime": datetime,
    },
    total=False,
)

GetFederationTokenResponseTypeDef = TypedDict(
    "GetFederationTokenResponseTypeDef", {"Credentials": "CredentialsTypeDef"}, total=False
)

GetMetricDataResponseTypeDef = TypedDict(
    "GetMetricDataResponseTypeDef",
    {"NextToken": str, "MetricResults": List["HistoricalMetricResultTypeDef"]},
    total=False,
)

ListContactFlowsResponseTypeDef = TypedDict(
    "ListContactFlowsResponseTypeDef",
    {"ContactFlowSummaryList": List["ContactFlowSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListHoursOfOperationsResponseTypeDef = TypedDict(
    "ListHoursOfOperationsResponseTypeDef",
    {"HoursOfOperationSummaryList": List["HoursOfOperationSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListPhoneNumbersResponseTypeDef = TypedDict(
    "ListPhoneNumbersResponseTypeDef",
    {"PhoneNumberSummaryList": List["PhoneNumberSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListQueuesResponseTypeDef = TypedDict(
    "ListQueuesResponseTypeDef",
    {"QueueSummaryList": List["QueueSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListRoutingProfilesResponseTypeDef = TypedDict(
    "ListRoutingProfilesResponseTypeDef",
    {"RoutingProfileSummaryList": List["RoutingProfileSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListSecurityProfilesResponseTypeDef = TypedDict(
    "ListSecurityProfilesResponseTypeDef",
    {"SecurityProfileSummaryList": List["SecurityProfileSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ListUserHierarchyGroupsResponseTypeDef = TypedDict(
    "ListUserHierarchyGroupsResponseTypeDef",
    {"UserHierarchyGroupSummaryList": List["HierarchyGroupSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {"UserSummaryList": List["UserSummaryTypeDef"], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

ParticipantDetailsTypeDef = TypedDict("ParticipantDetailsTypeDef", {"DisplayName": str})

StartChatContactResponseTypeDef = TypedDict(
    "StartChatContactResponseTypeDef",
    {"ContactId": str, "ParticipantId": str, "ParticipantToken": str},
    total=False,
)

StartOutboundVoiceContactResponseTypeDef = TypedDict(
    "StartOutboundVoiceContactResponseTypeDef", {"ContactId": str}, total=False
)

VoiceRecordingConfigurationTypeDef = TypedDict(
    "VoiceRecordingConfigurationTypeDef",
    {"VoiceRecordingTrack": Literal["FROM_AGENT", "TO_AGENT", "ALL"]},
    total=False,
)
