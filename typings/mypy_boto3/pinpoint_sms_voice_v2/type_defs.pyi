"""
Type annotations for pinpoint-sms-voice-v2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_pinpoint_sms_voice_v2.type_defs import AccountAttributeTypeDef

    data: AccountAttributeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AccountLimitNameType,
    ConfigurationSetFilterNameType,
    DestinationCountryParameterKeyType,
    EventTypeType,
    KeywordActionType,
    MessageTypeType,
    NumberCapabilityType,
    NumberStatusType,
    NumberTypeType,
    PhoneNumberFilterNameType,
    PoolFilterNameType,
    PoolOriginationIdentitiesFilterNameType,
    PoolStatusType,
    RequestableNumberTypeType,
    SenderIdFilterNameType,
    SpendLimitNameType,
    VoiceIdType,
    VoiceMessageBodyTextTypeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountAttributeTypeDef",
    "AccountLimitTypeDef",
    "AssociateOriginationIdentityRequestRequestTypeDef",
    "AssociateOriginationIdentityResultTypeDef",
    "CloudWatchLogsDestinationTypeDef",
    "ConfigurationSetFilterTypeDef",
    "ConfigurationSetInformationTypeDef",
    "CreateConfigurationSetRequestRequestTypeDef",
    "CreateConfigurationSetResultTypeDef",
    "CreateEventDestinationRequestRequestTypeDef",
    "CreateEventDestinationResultTypeDef",
    "CreateOptOutListRequestRequestTypeDef",
    "CreateOptOutListResultTypeDef",
    "CreatePoolRequestRequestTypeDef",
    "CreatePoolResultTypeDef",
    "DeleteConfigurationSetRequestRequestTypeDef",
    "DeleteConfigurationSetResultTypeDef",
    "DeleteDefaultMessageTypeRequestRequestTypeDef",
    "DeleteDefaultMessageTypeResultTypeDef",
    "DeleteDefaultSenderIdRequestRequestTypeDef",
    "DeleteDefaultSenderIdResultTypeDef",
    "DeleteEventDestinationRequestRequestTypeDef",
    "DeleteEventDestinationResultTypeDef",
    "DeleteKeywordRequestRequestTypeDef",
    "DeleteKeywordResultTypeDef",
    "DeleteOptOutListRequestRequestTypeDef",
    "DeleteOptOutListResultTypeDef",
    "DeleteOptedOutNumberRequestRequestTypeDef",
    "DeleteOptedOutNumberResultTypeDef",
    "DeletePoolRequestRequestTypeDef",
    "DeletePoolResultTypeDef",
    "DeleteTextMessageSpendLimitOverrideResultTypeDef",
    "DeleteVoiceMessageSpendLimitOverrideResultTypeDef",
    "DescribeAccountAttributesRequestRequestTypeDef",
    "DescribeAccountAttributesResultTypeDef",
    "DescribeAccountLimitsRequestRequestTypeDef",
    "DescribeAccountLimitsResultTypeDef",
    "DescribeConfigurationSetsRequestRequestTypeDef",
    "DescribeConfigurationSetsResultTypeDef",
    "DescribeKeywordsRequestRequestTypeDef",
    "DescribeKeywordsResultTypeDef",
    "DescribeOptOutListsRequestRequestTypeDef",
    "DescribeOptOutListsResultTypeDef",
    "DescribeOptedOutNumbersRequestRequestTypeDef",
    "DescribeOptedOutNumbersResultTypeDef",
    "DescribePhoneNumbersRequestRequestTypeDef",
    "DescribePhoneNumbersResultTypeDef",
    "DescribePoolsRequestRequestTypeDef",
    "DescribePoolsResultTypeDef",
    "DescribeSenderIdsRequestRequestTypeDef",
    "DescribeSenderIdsResultTypeDef",
    "DescribeSpendLimitsRequestRequestTypeDef",
    "DescribeSpendLimitsResultTypeDef",
    "DisassociateOriginationIdentityRequestRequestTypeDef",
    "DisassociateOriginationIdentityResultTypeDef",
    "EventDestinationTypeDef",
    "KeywordFilterTypeDef",
    "KeywordInformationTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "ListPoolOriginationIdentitiesRequestRequestTypeDef",
    "ListPoolOriginationIdentitiesResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "OptOutListInformationTypeDef",
    "OptedOutFilterTypeDef",
    "OptedOutNumberInformationTypeDef",
    "OriginationIdentityMetadataTypeDef",
    "PaginatorConfigTypeDef",
    "PhoneNumberFilterTypeDef",
    "PhoneNumberInformationTypeDef",
    "PoolFilterTypeDef",
    "PoolInformationTypeDef",
    "PoolOriginationIdentitiesFilterTypeDef",
    "PutKeywordRequestRequestTypeDef",
    "PutKeywordResultTypeDef",
    "PutOptedOutNumberRequestRequestTypeDef",
    "PutOptedOutNumberResultTypeDef",
    "ReleasePhoneNumberRequestRequestTypeDef",
    "ReleasePhoneNumberResultTypeDef",
    "RequestPhoneNumberRequestRequestTypeDef",
    "RequestPhoneNumberResultTypeDef",
    "ResponseMetadataTypeDef",
    "SendTextMessageRequestRequestTypeDef",
    "SendTextMessageResultTypeDef",
    "SendVoiceMessageRequestRequestTypeDef",
    "SendVoiceMessageResultTypeDef",
    "SenderIdAndCountryTypeDef",
    "SenderIdFilterTypeDef",
    "SenderIdInformationTypeDef",
    "SetDefaultMessageTypeRequestRequestTypeDef",
    "SetDefaultMessageTypeResultTypeDef",
    "SetDefaultSenderIdRequestRequestTypeDef",
    "SetDefaultSenderIdResultTypeDef",
    "SetTextMessageSpendLimitOverrideRequestRequestTypeDef",
    "SetTextMessageSpendLimitOverrideResultTypeDef",
    "SetVoiceMessageSpendLimitOverrideRequestRequestTypeDef",
    "SetVoiceMessageSpendLimitOverrideResultTypeDef",
    "SnsDestinationTypeDef",
    "SpendLimitTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateEventDestinationRequestRequestTypeDef",
    "UpdateEventDestinationResultTypeDef",
    "UpdatePhoneNumberRequestRequestTypeDef",
    "UpdatePhoneNumberResultTypeDef",
    "UpdatePoolRequestRequestTypeDef",
    "UpdatePoolResultTypeDef",
)

AccountAttributeTypeDef = TypedDict(
    "AccountAttributeTypeDef",
    {
        "Name": Literal["ACCOUNT_TIER"],
        "Value": str,
    },
)

AccountLimitTypeDef = TypedDict(
    "AccountLimitTypeDef",
    {
        "Name": AccountLimitNameType,
        "Used": int,
        "Max": int,
    },
)

_RequiredAssociateOriginationIdentityRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateOriginationIdentityRequestRequestTypeDef",
    {
        "PoolId": str,
        "OriginationIdentity": str,
        "IsoCountryCode": str,
    },
)
_OptionalAssociateOriginationIdentityRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateOriginationIdentityRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class AssociateOriginationIdentityRequestRequestTypeDef(
    _RequiredAssociateOriginationIdentityRequestRequestTypeDef,
    _OptionalAssociateOriginationIdentityRequestRequestTypeDef,
):
    pass

AssociateOriginationIdentityResultTypeDef = TypedDict(
    "AssociateOriginationIdentityResultTypeDef",
    {
        "PoolArn": str,
        "PoolId": str,
        "OriginationIdentityArn": str,
        "OriginationIdentity": str,
        "IsoCountryCode": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CloudWatchLogsDestinationTypeDef = TypedDict(
    "CloudWatchLogsDestinationTypeDef",
    {
        "IamRoleArn": str,
        "LogGroupArn": str,
    },
)

ConfigurationSetFilterTypeDef = TypedDict(
    "ConfigurationSetFilterTypeDef",
    {
        "Name": ConfigurationSetFilterNameType,
        "Values": List[str],
    },
)

_RequiredConfigurationSetInformationTypeDef = TypedDict(
    "_RequiredConfigurationSetInformationTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "EventDestinations": List["EventDestinationTypeDef"],
        "CreatedTimestamp": datetime,
    },
)
_OptionalConfigurationSetInformationTypeDef = TypedDict(
    "_OptionalConfigurationSetInformationTypeDef",
    {
        "DefaultMessageType": MessageTypeType,
        "DefaultSenderId": str,
    },
    total=False,
)

class ConfigurationSetInformationTypeDef(
    _RequiredConfigurationSetInformationTypeDef, _OptionalConfigurationSetInformationTypeDef
):
    pass

_RequiredCreateConfigurationSetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
_OptionalCreateConfigurationSetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConfigurationSetRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

class CreateConfigurationSetRequestRequestTypeDef(
    _RequiredCreateConfigurationSetRequestRequestTypeDef,
    _OptionalCreateConfigurationSetRequestRequestTypeDef,
):
    pass

CreateConfigurationSetResultTypeDef = TypedDict(
    "CreateConfigurationSetResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "Tags": List["TagTypeDef"],
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEventDestinationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
        "MatchingEventTypes": List[EventTypeType],
    },
)
_OptionalCreateEventDestinationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEventDestinationRequestRequestTypeDef",
    {
        "CloudWatchLogsDestination": "CloudWatchLogsDestinationTypeDef",
        "KinesisFirehoseDestination": "KinesisFirehoseDestinationTypeDef",
        "SnsDestination": "SnsDestinationTypeDef",
        "ClientToken": str,
    },
    total=False,
)

class CreateEventDestinationRequestRequestTypeDef(
    _RequiredCreateEventDestinationRequestRequestTypeDef,
    _OptionalCreateEventDestinationRequestRequestTypeDef,
):
    pass

CreateEventDestinationResultTypeDef = TypedDict(
    "CreateEventDestinationResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "EventDestination": "EventDestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateOptOutListRequestRequestTypeDef = TypedDict(
    "_RequiredCreateOptOutListRequestRequestTypeDef",
    {
        "OptOutListName": str,
    },
)
_OptionalCreateOptOutListRequestRequestTypeDef = TypedDict(
    "_OptionalCreateOptOutListRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

class CreateOptOutListRequestRequestTypeDef(
    _RequiredCreateOptOutListRequestRequestTypeDef, _OptionalCreateOptOutListRequestRequestTypeDef
):
    pass

CreateOptOutListResultTypeDef = TypedDict(
    "CreateOptOutListResultTypeDef",
    {
        "OptOutListArn": str,
        "OptOutListName": str,
        "Tags": List["TagTypeDef"],
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePoolRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePoolRequestRequestTypeDef",
    {
        "OriginationIdentity": str,
        "IsoCountryCode": str,
        "MessageType": MessageTypeType,
    },
)
_OptionalCreatePoolRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePoolRequestRequestTypeDef",
    {
        "DeletionProtectionEnabled": bool,
        "Tags": List["TagTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

class CreatePoolRequestRequestTypeDef(
    _RequiredCreatePoolRequestRequestTypeDef, _OptionalCreatePoolRequestRequestTypeDef
):
    pass

CreatePoolResultTypeDef = TypedDict(
    "CreatePoolResultTypeDef",
    {
        "PoolArn": str,
        "PoolId": str,
        "Status": PoolStatusType,
        "MessageType": MessageTypeType,
        "TwoWayEnabled": bool,
        "TwoWayChannelArn": str,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "SharedRoutesEnabled": bool,
        "DeletionProtectionEnabled": bool,
        "Tags": List["TagTypeDef"],
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConfigurationSetRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

DeleteConfigurationSetResultTypeDef = TypedDict(
    "DeleteConfigurationSetResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "EventDestinations": List["EventDestinationTypeDef"],
        "DefaultMessageType": MessageTypeType,
        "DefaultSenderId": str,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDefaultMessageTypeRequestRequestTypeDef = TypedDict(
    "DeleteDefaultMessageTypeRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

DeleteDefaultMessageTypeResultTypeDef = TypedDict(
    "DeleteDefaultMessageTypeResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "MessageType": MessageTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDefaultSenderIdRequestRequestTypeDef = TypedDict(
    "DeleteDefaultSenderIdRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

DeleteDefaultSenderIdResultTypeDef = TypedDict(
    "DeleteDefaultSenderIdResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "SenderId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEventDestinationRequestRequestTypeDef = TypedDict(
    "DeleteEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
    },
)

DeleteEventDestinationResultTypeDef = TypedDict(
    "DeleteEventDestinationResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "EventDestination": "EventDestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteKeywordRequestRequestTypeDef = TypedDict(
    "DeleteKeywordRequestRequestTypeDef",
    {
        "OriginationIdentity": str,
        "Keyword": str,
    },
)

DeleteKeywordResultTypeDef = TypedDict(
    "DeleteKeywordResultTypeDef",
    {
        "OriginationIdentityArn": str,
        "OriginationIdentity": str,
        "Keyword": str,
        "KeywordMessage": str,
        "KeywordAction": KeywordActionType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteOptOutListRequestRequestTypeDef = TypedDict(
    "DeleteOptOutListRequestRequestTypeDef",
    {
        "OptOutListName": str,
    },
)

DeleteOptOutListResultTypeDef = TypedDict(
    "DeleteOptOutListResultTypeDef",
    {
        "OptOutListArn": str,
        "OptOutListName": str,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteOptedOutNumberRequestRequestTypeDef = TypedDict(
    "DeleteOptedOutNumberRequestRequestTypeDef",
    {
        "OptOutListName": str,
        "OptedOutNumber": str,
    },
)

DeleteOptedOutNumberResultTypeDef = TypedDict(
    "DeleteOptedOutNumberResultTypeDef",
    {
        "OptOutListArn": str,
        "OptOutListName": str,
        "OptedOutNumber": str,
        "OptedOutTimestamp": datetime,
        "EndUserOptedOut": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePoolRequestRequestTypeDef = TypedDict(
    "DeletePoolRequestRequestTypeDef",
    {
        "PoolId": str,
    },
)

DeletePoolResultTypeDef = TypedDict(
    "DeletePoolResultTypeDef",
    {
        "PoolArn": str,
        "PoolId": str,
        "Status": PoolStatusType,
        "MessageType": MessageTypeType,
        "TwoWayEnabled": bool,
        "TwoWayChannelArn": str,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "SharedRoutesEnabled": bool,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTextMessageSpendLimitOverrideResultTypeDef = TypedDict(
    "DeleteTextMessageSpendLimitOverrideResultTypeDef",
    {
        "MonthlyLimit": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVoiceMessageSpendLimitOverrideResultTypeDef = TypedDict(
    "DeleteVoiceMessageSpendLimitOverrideResultTypeDef",
    {
        "MonthlyLimit": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountAttributesRequestRequestTypeDef = TypedDict(
    "DescribeAccountAttributesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeAccountAttributesResultTypeDef = TypedDict(
    "DescribeAccountAttributesResultTypeDef",
    {
        "AccountAttributes": List["AccountAttributeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountLimitsRequestRequestTypeDef = TypedDict(
    "DescribeAccountLimitsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeAccountLimitsResultTypeDef = TypedDict(
    "DescribeAccountLimitsResultTypeDef",
    {
        "AccountLimits": List["AccountLimitTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationSetsRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationSetsRequestRequestTypeDef",
    {
        "ConfigurationSetNames": List[str],
        "Filters": List["ConfigurationSetFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeConfigurationSetsResultTypeDef = TypedDict(
    "DescribeConfigurationSetsResultTypeDef",
    {
        "ConfigurationSets": List["ConfigurationSetInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeKeywordsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeKeywordsRequestRequestTypeDef",
    {
        "OriginationIdentity": str,
    },
)
_OptionalDescribeKeywordsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeKeywordsRequestRequestTypeDef",
    {
        "Keywords": List[str],
        "Filters": List["KeywordFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class DescribeKeywordsRequestRequestTypeDef(
    _RequiredDescribeKeywordsRequestRequestTypeDef, _OptionalDescribeKeywordsRequestRequestTypeDef
):
    pass

DescribeKeywordsResultTypeDef = TypedDict(
    "DescribeKeywordsResultTypeDef",
    {
        "OriginationIdentityArn": str,
        "OriginationIdentity": str,
        "Keywords": List["KeywordInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOptOutListsRequestRequestTypeDef = TypedDict(
    "DescribeOptOutListsRequestRequestTypeDef",
    {
        "OptOutListNames": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeOptOutListsResultTypeDef = TypedDict(
    "DescribeOptOutListsResultTypeDef",
    {
        "OptOutLists": List["OptOutListInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeOptedOutNumbersRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeOptedOutNumbersRequestRequestTypeDef",
    {
        "OptOutListName": str,
    },
)
_OptionalDescribeOptedOutNumbersRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeOptedOutNumbersRequestRequestTypeDef",
    {
        "OptedOutNumbers": List[str],
        "Filters": List["OptedOutFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class DescribeOptedOutNumbersRequestRequestTypeDef(
    _RequiredDescribeOptedOutNumbersRequestRequestTypeDef,
    _OptionalDescribeOptedOutNumbersRequestRequestTypeDef,
):
    pass

DescribeOptedOutNumbersResultTypeDef = TypedDict(
    "DescribeOptedOutNumbersResultTypeDef",
    {
        "OptOutListArn": str,
        "OptOutListName": str,
        "OptedOutNumbers": List["OptedOutNumberInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePhoneNumbersRequestRequestTypeDef = TypedDict(
    "DescribePhoneNumbersRequestRequestTypeDef",
    {
        "PhoneNumberIds": List[str],
        "Filters": List["PhoneNumberFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribePhoneNumbersResultTypeDef = TypedDict(
    "DescribePhoneNumbersResultTypeDef",
    {
        "PhoneNumbers": List["PhoneNumberInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePoolsRequestRequestTypeDef = TypedDict(
    "DescribePoolsRequestRequestTypeDef",
    {
        "PoolIds": List[str],
        "Filters": List["PoolFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribePoolsResultTypeDef = TypedDict(
    "DescribePoolsResultTypeDef",
    {
        "Pools": List["PoolInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSenderIdsRequestRequestTypeDef = TypedDict(
    "DescribeSenderIdsRequestRequestTypeDef",
    {
        "SenderIds": List["SenderIdAndCountryTypeDef"],
        "Filters": List["SenderIdFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeSenderIdsResultTypeDef = TypedDict(
    "DescribeSenderIdsResultTypeDef",
    {
        "SenderIds": List["SenderIdInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSpendLimitsRequestRequestTypeDef = TypedDict(
    "DescribeSpendLimitsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeSpendLimitsResultTypeDef = TypedDict(
    "DescribeSpendLimitsResultTypeDef",
    {
        "SpendLimits": List["SpendLimitTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateOriginationIdentityRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateOriginationIdentityRequestRequestTypeDef",
    {
        "PoolId": str,
        "OriginationIdentity": str,
        "IsoCountryCode": str,
    },
)
_OptionalDisassociateOriginationIdentityRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateOriginationIdentityRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class DisassociateOriginationIdentityRequestRequestTypeDef(
    _RequiredDisassociateOriginationIdentityRequestRequestTypeDef,
    _OptionalDisassociateOriginationIdentityRequestRequestTypeDef,
):
    pass

DisassociateOriginationIdentityResultTypeDef = TypedDict(
    "DisassociateOriginationIdentityResultTypeDef",
    {
        "PoolArn": str,
        "PoolId": str,
        "OriginationIdentityArn": str,
        "OriginationIdentity": str,
        "IsoCountryCode": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEventDestinationTypeDef = TypedDict(
    "_RequiredEventDestinationTypeDef",
    {
        "EventDestinationName": str,
        "Enabled": bool,
        "MatchingEventTypes": List[EventTypeType],
    },
)
_OptionalEventDestinationTypeDef = TypedDict(
    "_OptionalEventDestinationTypeDef",
    {
        "CloudWatchLogsDestination": "CloudWatchLogsDestinationTypeDef",
        "KinesisFirehoseDestination": "KinesisFirehoseDestinationTypeDef",
        "SnsDestination": "SnsDestinationTypeDef",
    },
    total=False,
)

class EventDestinationTypeDef(_RequiredEventDestinationTypeDef, _OptionalEventDestinationTypeDef):
    pass

KeywordFilterTypeDef = TypedDict(
    "KeywordFilterTypeDef",
    {
        "Name": Literal["keyword-action"],
        "Values": List[str],
    },
)

KeywordInformationTypeDef = TypedDict(
    "KeywordInformationTypeDef",
    {
        "Keyword": str,
        "KeywordMessage": str,
        "KeywordAction": KeywordActionType,
    },
)

KinesisFirehoseDestinationTypeDef = TypedDict(
    "KinesisFirehoseDestinationTypeDef",
    {
        "IamRoleArn": str,
        "DeliveryStreamArn": str,
    },
)

_RequiredListPoolOriginationIdentitiesRequestRequestTypeDef = TypedDict(
    "_RequiredListPoolOriginationIdentitiesRequestRequestTypeDef",
    {
        "PoolId": str,
    },
)
_OptionalListPoolOriginationIdentitiesRequestRequestTypeDef = TypedDict(
    "_OptionalListPoolOriginationIdentitiesRequestRequestTypeDef",
    {
        "Filters": List["PoolOriginationIdentitiesFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListPoolOriginationIdentitiesRequestRequestTypeDef(
    _RequiredListPoolOriginationIdentitiesRequestRequestTypeDef,
    _OptionalListPoolOriginationIdentitiesRequestRequestTypeDef,
):
    pass

ListPoolOriginationIdentitiesResultTypeDef = TypedDict(
    "ListPoolOriginationIdentitiesResultTypeDef",
    {
        "PoolArn": str,
        "PoolId": str,
        "OriginationIdentities": List["OriginationIdentityMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OptOutListInformationTypeDef = TypedDict(
    "OptOutListInformationTypeDef",
    {
        "OptOutListArn": str,
        "OptOutListName": str,
        "CreatedTimestamp": datetime,
    },
)

OptedOutFilterTypeDef = TypedDict(
    "OptedOutFilterTypeDef",
    {
        "Name": Literal["end-user-opted-out"],
        "Values": List[str],
    },
)

OptedOutNumberInformationTypeDef = TypedDict(
    "OptedOutNumberInformationTypeDef",
    {
        "OptedOutNumber": str,
        "OptedOutTimestamp": datetime,
        "EndUserOptedOut": bool,
    },
)

OriginationIdentityMetadataTypeDef = TypedDict(
    "OriginationIdentityMetadataTypeDef",
    {
        "OriginationIdentityArn": str,
        "OriginationIdentity": str,
        "IsoCountryCode": str,
        "NumberCapabilities": List[NumberCapabilityType],
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PhoneNumberFilterTypeDef = TypedDict(
    "PhoneNumberFilterTypeDef",
    {
        "Name": PhoneNumberFilterNameType,
        "Values": List[str],
    },
)

_RequiredPhoneNumberInformationTypeDef = TypedDict(
    "_RequiredPhoneNumberInformationTypeDef",
    {
        "PhoneNumberArn": str,
        "PhoneNumber": str,
        "Status": NumberStatusType,
        "IsoCountryCode": str,
        "MessageType": MessageTypeType,
        "NumberCapabilities": List[NumberCapabilityType],
        "NumberType": NumberTypeType,
        "MonthlyLeasingPrice": str,
        "TwoWayEnabled": bool,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "DeletionProtectionEnabled": bool,
        "CreatedTimestamp": datetime,
    },
)
_OptionalPhoneNumberInformationTypeDef = TypedDict(
    "_OptionalPhoneNumberInformationTypeDef",
    {
        "PhoneNumberId": str,
        "TwoWayChannelArn": str,
        "PoolId": str,
    },
    total=False,
)

class PhoneNumberInformationTypeDef(
    _RequiredPhoneNumberInformationTypeDef, _OptionalPhoneNumberInformationTypeDef
):
    pass

PoolFilterTypeDef = TypedDict(
    "PoolFilterTypeDef",
    {
        "Name": PoolFilterNameType,
        "Values": List[str],
    },
)

_RequiredPoolInformationTypeDef = TypedDict(
    "_RequiredPoolInformationTypeDef",
    {
        "PoolArn": str,
        "PoolId": str,
        "Status": PoolStatusType,
        "MessageType": MessageTypeType,
        "TwoWayEnabled": bool,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "SharedRoutesEnabled": bool,
        "DeletionProtectionEnabled": bool,
        "CreatedTimestamp": datetime,
    },
)
_OptionalPoolInformationTypeDef = TypedDict(
    "_OptionalPoolInformationTypeDef",
    {
        "TwoWayChannelArn": str,
    },
    total=False,
)

class PoolInformationTypeDef(_RequiredPoolInformationTypeDef, _OptionalPoolInformationTypeDef):
    pass

PoolOriginationIdentitiesFilterTypeDef = TypedDict(
    "PoolOriginationIdentitiesFilterTypeDef",
    {
        "Name": PoolOriginationIdentitiesFilterNameType,
        "Values": List[str],
    },
)

_RequiredPutKeywordRequestRequestTypeDef = TypedDict(
    "_RequiredPutKeywordRequestRequestTypeDef",
    {
        "OriginationIdentity": str,
        "Keyword": str,
        "KeywordMessage": str,
    },
)
_OptionalPutKeywordRequestRequestTypeDef = TypedDict(
    "_OptionalPutKeywordRequestRequestTypeDef",
    {
        "KeywordAction": KeywordActionType,
    },
    total=False,
)

class PutKeywordRequestRequestTypeDef(
    _RequiredPutKeywordRequestRequestTypeDef, _OptionalPutKeywordRequestRequestTypeDef
):
    pass

PutKeywordResultTypeDef = TypedDict(
    "PutKeywordResultTypeDef",
    {
        "OriginationIdentityArn": str,
        "OriginationIdentity": str,
        "Keyword": str,
        "KeywordMessage": str,
        "KeywordAction": KeywordActionType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutOptedOutNumberRequestRequestTypeDef = TypedDict(
    "PutOptedOutNumberRequestRequestTypeDef",
    {
        "OptOutListName": str,
        "OptedOutNumber": str,
    },
)

PutOptedOutNumberResultTypeDef = TypedDict(
    "PutOptedOutNumberResultTypeDef",
    {
        "OptOutListArn": str,
        "OptOutListName": str,
        "OptedOutNumber": str,
        "OptedOutTimestamp": datetime,
        "EndUserOptedOut": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReleasePhoneNumberRequestRequestTypeDef = TypedDict(
    "ReleasePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)

ReleasePhoneNumberResultTypeDef = TypedDict(
    "ReleasePhoneNumberResultTypeDef",
    {
        "PhoneNumberArn": str,
        "PhoneNumberId": str,
        "PhoneNumber": str,
        "Status": NumberStatusType,
        "IsoCountryCode": str,
        "MessageType": MessageTypeType,
        "NumberCapabilities": List[NumberCapabilityType],
        "NumberType": NumberTypeType,
        "MonthlyLeasingPrice": str,
        "TwoWayEnabled": bool,
        "TwoWayChannelArn": str,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRequestPhoneNumberRequestRequestTypeDef = TypedDict(
    "_RequiredRequestPhoneNumberRequestRequestTypeDef",
    {
        "IsoCountryCode": str,
        "MessageType": MessageTypeType,
        "NumberCapabilities": List[NumberCapabilityType],
        "NumberType": RequestableNumberTypeType,
    },
)
_OptionalRequestPhoneNumberRequestRequestTypeDef = TypedDict(
    "_OptionalRequestPhoneNumberRequestRequestTypeDef",
    {
        "OptOutListName": str,
        "PoolId": str,
        "RegistrationId": str,
        "DeletionProtectionEnabled": bool,
        "Tags": List["TagTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

class RequestPhoneNumberRequestRequestTypeDef(
    _RequiredRequestPhoneNumberRequestRequestTypeDef,
    _OptionalRequestPhoneNumberRequestRequestTypeDef,
):
    pass

RequestPhoneNumberResultTypeDef = TypedDict(
    "RequestPhoneNumberResultTypeDef",
    {
        "PhoneNumberArn": str,
        "PhoneNumberId": str,
        "PhoneNumber": str,
        "Status": NumberStatusType,
        "IsoCountryCode": str,
        "MessageType": MessageTypeType,
        "NumberCapabilities": List[NumberCapabilityType],
        "NumberType": RequestableNumberTypeType,
        "MonthlyLeasingPrice": str,
        "TwoWayEnabled": bool,
        "TwoWayChannelArn": str,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "DeletionProtectionEnabled": bool,
        "PoolId": str,
        "Tags": List["TagTypeDef"],
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredSendTextMessageRequestRequestTypeDef = TypedDict(
    "_RequiredSendTextMessageRequestRequestTypeDef",
    {
        "DestinationPhoneNumber": str,
    },
)
_OptionalSendTextMessageRequestRequestTypeDef = TypedDict(
    "_OptionalSendTextMessageRequestRequestTypeDef",
    {
        "OriginationIdentity": str,
        "MessageBody": str,
        "MessageType": MessageTypeType,
        "Keyword": str,
        "ConfigurationSetName": str,
        "MaxPrice": str,
        "TimeToLive": int,
        "Context": Dict[str, str],
        "DestinationCountryParameters": Dict[DestinationCountryParameterKeyType, str],
        "DryRun": bool,
    },
    total=False,
)

class SendTextMessageRequestRequestTypeDef(
    _RequiredSendTextMessageRequestRequestTypeDef, _OptionalSendTextMessageRequestRequestTypeDef
):
    pass

SendTextMessageResultTypeDef = TypedDict(
    "SendTextMessageResultTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendVoiceMessageRequestRequestTypeDef = TypedDict(
    "_RequiredSendVoiceMessageRequestRequestTypeDef",
    {
        "DestinationPhoneNumber": str,
        "OriginationIdentity": str,
    },
)
_OptionalSendVoiceMessageRequestRequestTypeDef = TypedDict(
    "_OptionalSendVoiceMessageRequestRequestTypeDef",
    {
        "MessageBody": str,
        "MessageBodyTextType": VoiceMessageBodyTextTypeType,
        "VoiceId": VoiceIdType,
        "ConfigurationSetName": str,
        "MaxPricePerMinute": str,
        "TimeToLive": int,
        "Context": Dict[str, str],
        "DryRun": bool,
    },
    total=False,
)

class SendVoiceMessageRequestRequestTypeDef(
    _RequiredSendVoiceMessageRequestRequestTypeDef, _OptionalSendVoiceMessageRequestRequestTypeDef
):
    pass

SendVoiceMessageResultTypeDef = TypedDict(
    "SendVoiceMessageResultTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SenderIdAndCountryTypeDef = TypedDict(
    "SenderIdAndCountryTypeDef",
    {
        "SenderId": str,
        "IsoCountryCode": str,
    },
)

SenderIdFilterTypeDef = TypedDict(
    "SenderIdFilterTypeDef",
    {
        "Name": SenderIdFilterNameType,
        "Values": List[str],
    },
)

SenderIdInformationTypeDef = TypedDict(
    "SenderIdInformationTypeDef",
    {
        "SenderIdArn": str,
        "SenderId": str,
        "IsoCountryCode": str,
        "MessageTypes": List[MessageTypeType],
        "MonthlyLeasingPrice": str,
    },
)

SetDefaultMessageTypeRequestRequestTypeDef = TypedDict(
    "SetDefaultMessageTypeRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "MessageType": MessageTypeType,
    },
)

SetDefaultMessageTypeResultTypeDef = TypedDict(
    "SetDefaultMessageTypeResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "MessageType": MessageTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetDefaultSenderIdRequestRequestTypeDef = TypedDict(
    "SetDefaultSenderIdRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "SenderId": str,
    },
)

SetDefaultSenderIdResultTypeDef = TypedDict(
    "SetDefaultSenderIdResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "SenderId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetTextMessageSpendLimitOverrideRequestRequestTypeDef = TypedDict(
    "SetTextMessageSpendLimitOverrideRequestRequestTypeDef",
    {
        "MonthlyLimit": int,
    },
)

SetTextMessageSpendLimitOverrideResultTypeDef = TypedDict(
    "SetTextMessageSpendLimitOverrideResultTypeDef",
    {
        "MonthlyLimit": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetVoiceMessageSpendLimitOverrideRequestRequestTypeDef = TypedDict(
    "SetVoiceMessageSpendLimitOverrideRequestRequestTypeDef",
    {
        "MonthlyLimit": int,
    },
)

SetVoiceMessageSpendLimitOverrideResultTypeDef = TypedDict(
    "SetVoiceMessageSpendLimitOverrideResultTypeDef",
    {
        "MonthlyLimit": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SnsDestinationTypeDef = TypedDict(
    "SnsDestinationTypeDef",
    {
        "TopicArn": str,
    },
)

SpendLimitTypeDef = TypedDict(
    "SpendLimitTypeDef",
    {
        "Name": SpendLimitNameType,
        "EnforcedLimit": int,
        "MaxLimit": int,
        "Overridden": bool,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateEventDestinationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
    },
)
_OptionalUpdateEventDestinationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEventDestinationRequestRequestTypeDef",
    {
        "Enabled": bool,
        "MatchingEventTypes": List[EventTypeType],
        "CloudWatchLogsDestination": "CloudWatchLogsDestinationTypeDef",
        "KinesisFirehoseDestination": "KinesisFirehoseDestinationTypeDef",
        "SnsDestination": "SnsDestinationTypeDef",
    },
    total=False,
)

class UpdateEventDestinationRequestRequestTypeDef(
    _RequiredUpdateEventDestinationRequestRequestTypeDef,
    _OptionalUpdateEventDestinationRequestRequestTypeDef,
):
    pass

UpdateEventDestinationResultTypeDef = TypedDict(
    "UpdateEventDestinationResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "EventDestination": "EventDestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePhoneNumberRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)
_OptionalUpdatePhoneNumberRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePhoneNumberRequestRequestTypeDef",
    {
        "TwoWayEnabled": bool,
        "TwoWayChannelArn": str,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "DeletionProtectionEnabled": bool,
    },
    total=False,
)

class UpdatePhoneNumberRequestRequestTypeDef(
    _RequiredUpdatePhoneNumberRequestRequestTypeDef, _OptionalUpdatePhoneNumberRequestRequestTypeDef
):
    pass

UpdatePhoneNumberResultTypeDef = TypedDict(
    "UpdatePhoneNumberResultTypeDef",
    {
        "PhoneNumberArn": str,
        "PhoneNumberId": str,
        "PhoneNumber": str,
        "Status": NumberStatusType,
        "IsoCountryCode": str,
        "MessageType": MessageTypeType,
        "NumberCapabilities": List[NumberCapabilityType],
        "NumberType": NumberTypeType,
        "MonthlyLeasingPrice": str,
        "TwoWayEnabled": bool,
        "TwoWayChannelArn": str,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "DeletionProtectionEnabled": bool,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePoolRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePoolRequestRequestTypeDef",
    {
        "PoolId": str,
    },
)
_OptionalUpdatePoolRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePoolRequestRequestTypeDef",
    {
        "TwoWayEnabled": bool,
        "TwoWayChannelArn": str,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "SharedRoutesEnabled": bool,
        "DeletionProtectionEnabled": bool,
    },
    total=False,
)

class UpdatePoolRequestRequestTypeDef(
    _RequiredUpdatePoolRequestRequestTypeDef, _OptionalUpdatePoolRequestRequestTypeDef
):
    pass

UpdatePoolResultTypeDef = TypedDict(
    "UpdatePoolResultTypeDef",
    {
        "PoolArn": str,
        "PoolId": str,
        "Status": PoolStatusType,
        "MessageType": MessageTypeType,
        "TwoWayEnabled": bool,
        "TwoWayChannelArn": str,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "SharedRoutesEnabled": bool,
        "DeletionProtectionEnabled": bool,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
