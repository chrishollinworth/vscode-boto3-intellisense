"""
Type annotations for sns service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sns.type_defs import AddPermissionInputRequestTypeDef

    data: AddPermissionInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    LanguageCodeStringType,
    NumberCapabilityType,
    RouteTypeType,
    SMSSandboxPhoneNumberVerificationStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AddPermissionInputRequestTypeDef",
    "AddPermissionInputTopicTypeDef",
    "CheckIfPhoneNumberIsOptedOutInputRequestTypeDef",
    "CheckIfPhoneNumberIsOptedOutResponseTypeDef",
    "ConfirmSubscriptionInputRequestTypeDef",
    "ConfirmSubscriptionInputTopicTypeDef",
    "ConfirmSubscriptionResponseTypeDef",
    "CreateEndpointResponseTypeDef",
    "CreatePlatformApplicationInputRequestTypeDef",
    "CreatePlatformApplicationInputServiceResourceTypeDef",
    "CreatePlatformApplicationResponseTypeDef",
    "CreatePlatformEndpointInputPlatformApplicationTypeDef",
    "CreatePlatformEndpointInputRequestTypeDef",
    "CreateSMSSandboxPhoneNumberInputRequestTypeDef",
    "CreateTopicInputRequestTypeDef",
    "CreateTopicInputServiceResourceTypeDef",
    "CreateTopicResponseTypeDef",
    "DeleteEndpointInputRequestTypeDef",
    "DeletePlatformApplicationInputRequestTypeDef",
    "DeleteSMSSandboxPhoneNumberInputRequestTypeDef",
    "DeleteTopicInputRequestTypeDef",
    "EndpointTypeDef",
    "GetEndpointAttributesInputRequestTypeDef",
    "GetEndpointAttributesResponseTypeDef",
    "GetPlatformApplicationAttributesInputRequestTypeDef",
    "GetPlatformApplicationAttributesResponseTypeDef",
    "GetSMSAttributesInputRequestTypeDef",
    "GetSMSAttributesResponseTypeDef",
    "GetSMSSandboxAccountStatusResultTypeDef",
    "GetSubscriptionAttributesInputRequestTypeDef",
    "GetSubscriptionAttributesResponseTypeDef",
    "GetTopicAttributesInputRequestTypeDef",
    "GetTopicAttributesResponseTypeDef",
    "ListEndpointsByPlatformApplicationInputRequestTypeDef",
    "ListEndpointsByPlatformApplicationResponseTypeDef",
    "ListOriginationNumbersRequestRequestTypeDef",
    "ListOriginationNumbersResultTypeDef",
    "ListPhoneNumbersOptedOutInputRequestTypeDef",
    "ListPhoneNumbersOptedOutResponseTypeDef",
    "ListPlatformApplicationsInputRequestTypeDef",
    "ListPlatformApplicationsResponseTypeDef",
    "ListSMSSandboxPhoneNumbersInputRequestTypeDef",
    "ListSMSSandboxPhoneNumbersResultTypeDef",
    "ListSubscriptionsByTopicInputRequestTypeDef",
    "ListSubscriptionsByTopicResponseTypeDef",
    "ListSubscriptionsInputRequestTypeDef",
    "ListSubscriptionsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTopicsInputRequestTypeDef",
    "ListTopicsResponseTypeDef",
    "MessageAttributeValueTypeDef",
    "OptInPhoneNumberInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "PhoneNumberInformationTypeDef",
    "PlatformApplicationTypeDef",
    "PublishInputPlatformEndpointTypeDef",
    "PublishInputRequestTypeDef",
    "PublishInputTopicTypeDef",
    "PublishResponseTypeDef",
    "RemovePermissionInputRequestTypeDef",
    "RemovePermissionInputTopicTypeDef",
    "ResponseMetadataTypeDef",
    "SMSSandboxPhoneNumberTypeDef",
    "ServiceResourcePlatformApplicationRequestTypeDef",
    "ServiceResourcePlatformEndpointRequestTypeDef",
    "ServiceResourceSubscriptionRequestTypeDef",
    "ServiceResourceTopicRequestTypeDef",
    "SetEndpointAttributesInputPlatformEndpointTypeDef",
    "SetEndpointAttributesInputRequestTypeDef",
    "SetPlatformApplicationAttributesInputPlatformApplicationTypeDef",
    "SetPlatformApplicationAttributesInputRequestTypeDef",
    "SetSMSAttributesInputRequestTypeDef",
    "SetSubscriptionAttributesInputRequestTypeDef",
    "SetSubscriptionAttributesInputSubscriptionTypeDef",
    "SetTopicAttributesInputRequestTypeDef",
    "SetTopicAttributesInputTopicTypeDef",
    "SubscribeInputRequestTypeDef",
    "SubscribeInputTopicTypeDef",
    "SubscribeResponseTypeDef",
    "SubscriptionTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TopicTypeDef",
    "UnsubscribeInputRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "VerifySMSSandboxPhoneNumberInputRequestTypeDef",
)

AddPermissionInputRequestTypeDef = TypedDict(
    "AddPermissionInputRequestTypeDef",
    {
        "TopicArn": str,
        "Label": str,
        "AWSAccountId": List[str],
        "ActionName": List[str],
    },
)

AddPermissionInputTopicTypeDef = TypedDict(
    "AddPermissionInputTopicTypeDef",
    {
        "Label": str,
        "AWSAccountId": List[str],
        "ActionName": List[str],
    },
)

CheckIfPhoneNumberIsOptedOutInputRequestTypeDef = TypedDict(
    "CheckIfPhoneNumberIsOptedOutInputRequestTypeDef",
    {
        "phoneNumber": str,
    },
)

CheckIfPhoneNumberIsOptedOutResponseTypeDef = TypedDict(
    "CheckIfPhoneNumberIsOptedOutResponseTypeDef",
    {
        "isOptedOut": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredConfirmSubscriptionInputRequestTypeDef = TypedDict(
    "_RequiredConfirmSubscriptionInputRequestTypeDef",
    {
        "TopicArn": str,
        "Token": str,
    },
)
_OptionalConfirmSubscriptionInputRequestTypeDef = TypedDict(
    "_OptionalConfirmSubscriptionInputRequestTypeDef",
    {
        "AuthenticateOnUnsubscribe": str,
    },
    total=False,
)

class ConfirmSubscriptionInputRequestTypeDef(
    _RequiredConfirmSubscriptionInputRequestTypeDef, _OptionalConfirmSubscriptionInputRequestTypeDef
):
    pass

_RequiredConfirmSubscriptionInputTopicTypeDef = TypedDict(
    "_RequiredConfirmSubscriptionInputTopicTypeDef",
    {
        "Token": str,
    },
)
_OptionalConfirmSubscriptionInputTopicTypeDef = TypedDict(
    "_OptionalConfirmSubscriptionInputTopicTypeDef",
    {
        "AuthenticateOnUnsubscribe": str,
    },
    total=False,
)

class ConfirmSubscriptionInputTopicTypeDef(
    _RequiredConfirmSubscriptionInputTopicTypeDef, _OptionalConfirmSubscriptionInputTopicTypeDef
):
    pass

ConfirmSubscriptionResponseTypeDef = TypedDict(
    "ConfirmSubscriptionResponseTypeDef",
    {
        "SubscriptionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEndpointResponseTypeDef = TypedDict(
    "CreateEndpointResponseTypeDef",
    {
        "EndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePlatformApplicationInputRequestTypeDef = TypedDict(
    "CreatePlatformApplicationInputRequestTypeDef",
    {
        "Name": str,
        "Platform": str,
        "Attributes": Dict[str, str],
    },
)

CreatePlatformApplicationInputServiceResourceTypeDef = TypedDict(
    "CreatePlatformApplicationInputServiceResourceTypeDef",
    {
        "Name": str,
        "Platform": str,
        "Attributes": Dict[str, str],
    },
)

CreatePlatformApplicationResponseTypeDef = TypedDict(
    "CreatePlatformApplicationResponseTypeDef",
    {
        "PlatformApplicationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePlatformEndpointInputPlatformApplicationTypeDef = TypedDict(
    "_RequiredCreatePlatformEndpointInputPlatformApplicationTypeDef",
    {
        "Token": str,
    },
)
_OptionalCreatePlatformEndpointInputPlatformApplicationTypeDef = TypedDict(
    "_OptionalCreatePlatformEndpointInputPlatformApplicationTypeDef",
    {
        "CustomUserData": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)

class CreatePlatformEndpointInputPlatformApplicationTypeDef(
    _RequiredCreatePlatformEndpointInputPlatformApplicationTypeDef,
    _OptionalCreatePlatformEndpointInputPlatformApplicationTypeDef,
):
    pass

_RequiredCreatePlatformEndpointInputRequestTypeDef = TypedDict(
    "_RequiredCreatePlatformEndpointInputRequestTypeDef",
    {
        "PlatformApplicationArn": str,
        "Token": str,
    },
)
_OptionalCreatePlatformEndpointInputRequestTypeDef = TypedDict(
    "_OptionalCreatePlatformEndpointInputRequestTypeDef",
    {
        "CustomUserData": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)

class CreatePlatformEndpointInputRequestTypeDef(
    _RequiredCreatePlatformEndpointInputRequestTypeDef,
    _OptionalCreatePlatformEndpointInputRequestTypeDef,
):
    pass

_RequiredCreateSMSSandboxPhoneNumberInputRequestTypeDef = TypedDict(
    "_RequiredCreateSMSSandboxPhoneNumberInputRequestTypeDef",
    {
        "PhoneNumber": str,
    },
)
_OptionalCreateSMSSandboxPhoneNumberInputRequestTypeDef = TypedDict(
    "_OptionalCreateSMSSandboxPhoneNumberInputRequestTypeDef",
    {
        "LanguageCode": LanguageCodeStringType,
    },
    total=False,
)

class CreateSMSSandboxPhoneNumberInputRequestTypeDef(
    _RequiredCreateSMSSandboxPhoneNumberInputRequestTypeDef,
    _OptionalCreateSMSSandboxPhoneNumberInputRequestTypeDef,
):
    pass

_RequiredCreateTopicInputRequestTypeDef = TypedDict(
    "_RequiredCreateTopicInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateTopicInputRequestTypeDef = TypedDict(
    "_OptionalCreateTopicInputRequestTypeDef",
    {
        "Attributes": Dict[str, str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateTopicInputRequestTypeDef(
    _RequiredCreateTopicInputRequestTypeDef, _OptionalCreateTopicInputRequestTypeDef
):
    pass

_RequiredCreateTopicInputServiceResourceTypeDef = TypedDict(
    "_RequiredCreateTopicInputServiceResourceTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateTopicInputServiceResourceTypeDef = TypedDict(
    "_OptionalCreateTopicInputServiceResourceTypeDef",
    {
        "Attributes": Dict[str, str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateTopicInputServiceResourceTypeDef(
    _RequiredCreateTopicInputServiceResourceTypeDef, _OptionalCreateTopicInputServiceResourceTypeDef
):
    pass

CreateTopicResponseTypeDef = TypedDict(
    "CreateTopicResponseTypeDef",
    {
        "TopicArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEndpointInputRequestTypeDef = TypedDict(
    "DeleteEndpointInputRequestTypeDef",
    {
        "EndpointArn": str,
    },
)

DeletePlatformApplicationInputRequestTypeDef = TypedDict(
    "DeletePlatformApplicationInputRequestTypeDef",
    {
        "PlatformApplicationArn": str,
    },
)

DeleteSMSSandboxPhoneNumberInputRequestTypeDef = TypedDict(
    "DeleteSMSSandboxPhoneNumberInputRequestTypeDef",
    {
        "PhoneNumber": str,
    },
)

DeleteTopicInputRequestTypeDef = TypedDict(
    "DeleteTopicInputRequestTypeDef",
    {
        "TopicArn": str,
    },
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "EndpointArn": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)

GetEndpointAttributesInputRequestTypeDef = TypedDict(
    "GetEndpointAttributesInputRequestTypeDef",
    {
        "EndpointArn": str,
    },
)

GetEndpointAttributesResponseTypeDef = TypedDict(
    "GetEndpointAttributesResponseTypeDef",
    {
        "Attributes": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPlatformApplicationAttributesInputRequestTypeDef = TypedDict(
    "GetPlatformApplicationAttributesInputRequestTypeDef",
    {
        "PlatformApplicationArn": str,
    },
)

GetPlatformApplicationAttributesResponseTypeDef = TypedDict(
    "GetPlatformApplicationAttributesResponseTypeDef",
    {
        "Attributes": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSMSAttributesInputRequestTypeDef = TypedDict(
    "GetSMSAttributesInputRequestTypeDef",
    {
        "attributes": List[str],
    },
    total=False,
)

GetSMSAttributesResponseTypeDef = TypedDict(
    "GetSMSAttributesResponseTypeDef",
    {
        "attributes": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSMSSandboxAccountStatusResultTypeDef = TypedDict(
    "GetSMSSandboxAccountStatusResultTypeDef",
    {
        "IsInSandbox": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSubscriptionAttributesInputRequestTypeDef = TypedDict(
    "GetSubscriptionAttributesInputRequestTypeDef",
    {
        "SubscriptionArn": str,
    },
)

GetSubscriptionAttributesResponseTypeDef = TypedDict(
    "GetSubscriptionAttributesResponseTypeDef",
    {
        "Attributes": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTopicAttributesInputRequestTypeDef = TypedDict(
    "GetTopicAttributesInputRequestTypeDef",
    {
        "TopicArn": str,
    },
)

GetTopicAttributesResponseTypeDef = TypedDict(
    "GetTopicAttributesResponseTypeDef",
    {
        "Attributes": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEndpointsByPlatformApplicationInputRequestTypeDef = TypedDict(
    "_RequiredListEndpointsByPlatformApplicationInputRequestTypeDef",
    {
        "PlatformApplicationArn": str,
    },
)
_OptionalListEndpointsByPlatformApplicationInputRequestTypeDef = TypedDict(
    "_OptionalListEndpointsByPlatformApplicationInputRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListEndpointsByPlatformApplicationInputRequestTypeDef(
    _RequiredListEndpointsByPlatformApplicationInputRequestTypeDef,
    _OptionalListEndpointsByPlatformApplicationInputRequestTypeDef,
):
    pass

ListEndpointsByPlatformApplicationResponseTypeDef = TypedDict(
    "ListEndpointsByPlatformApplicationResponseTypeDef",
    {
        "Endpoints": List["EndpointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOriginationNumbersRequestRequestTypeDef = TypedDict(
    "ListOriginationNumbersRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListOriginationNumbersResultTypeDef = TypedDict(
    "ListOriginationNumbersResultTypeDef",
    {
        "NextToken": str,
        "PhoneNumbers": List["PhoneNumberInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPhoneNumbersOptedOutInputRequestTypeDef = TypedDict(
    "ListPhoneNumbersOptedOutInputRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

ListPhoneNumbersOptedOutResponseTypeDef = TypedDict(
    "ListPhoneNumbersOptedOutResponseTypeDef",
    {
        "phoneNumbers": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPlatformApplicationsInputRequestTypeDef = TypedDict(
    "ListPlatformApplicationsInputRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

ListPlatformApplicationsResponseTypeDef = TypedDict(
    "ListPlatformApplicationsResponseTypeDef",
    {
        "PlatformApplications": List["PlatformApplicationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSMSSandboxPhoneNumbersInputRequestTypeDef = TypedDict(
    "ListSMSSandboxPhoneNumbersInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListSMSSandboxPhoneNumbersResultTypeDef = TypedDict(
    "ListSMSSandboxPhoneNumbersResultTypeDef",
    {
        "PhoneNumbers": List["SMSSandboxPhoneNumberTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSubscriptionsByTopicInputRequestTypeDef = TypedDict(
    "_RequiredListSubscriptionsByTopicInputRequestTypeDef",
    {
        "TopicArn": str,
    },
)
_OptionalListSubscriptionsByTopicInputRequestTypeDef = TypedDict(
    "_OptionalListSubscriptionsByTopicInputRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListSubscriptionsByTopicInputRequestTypeDef(
    _RequiredListSubscriptionsByTopicInputRequestTypeDef,
    _OptionalListSubscriptionsByTopicInputRequestTypeDef,
):
    pass

ListSubscriptionsByTopicResponseTypeDef = TypedDict(
    "ListSubscriptionsByTopicResponseTypeDef",
    {
        "Subscriptions": List["SubscriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSubscriptionsInputRequestTypeDef = TypedDict(
    "ListSubscriptionsInputRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

ListSubscriptionsResponseTypeDef = TypedDict(
    "ListSubscriptionsResponseTypeDef",
    {
        "Subscriptions": List["SubscriptionTypeDef"],
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

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTopicsInputRequestTypeDef = TypedDict(
    "ListTopicsInputRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

ListTopicsResponseTypeDef = TypedDict(
    "ListTopicsResponseTypeDef",
    {
        "Topics": List["TopicTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMessageAttributeValueTypeDef = TypedDict(
    "_RequiredMessageAttributeValueTypeDef",
    {
        "DataType": str,
    },
)
_OptionalMessageAttributeValueTypeDef = TypedDict(
    "_OptionalMessageAttributeValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

class MessageAttributeValueTypeDef(
    _RequiredMessageAttributeValueTypeDef, _OptionalMessageAttributeValueTypeDef
):
    pass

OptInPhoneNumberInputRequestTypeDef = TypedDict(
    "OptInPhoneNumberInputRequestTypeDef",
    {
        "phoneNumber": str,
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

PhoneNumberInformationTypeDef = TypedDict(
    "PhoneNumberInformationTypeDef",
    {
        "CreatedAt": datetime,
        "PhoneNumber": str,
        "Status": str,
        "Iso2CountryCode": str,
        "RouteType": RouteTypeType,
        "NumberCapabilities": List[NumberCapabilityType],
    },
    total=False,
)

PlatformApplicationTypeDef = TypedDict(
    "PlatformApplicationTypeDef",
    {
        "PlatformApplicationArn": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)

_RequiredPublishInputPlatformEndpointTypeDef = TypedDict(
    "_RequiredPublishInputPlatformEndpointTypeDef",
    {
        "Message": str,
    },
)
_OptionalPublishInputPlatformEndpointTypeDef = TypedDict(
    "_OptionalPublishInputPlatformEndpointTypeDef",
    {
        "TopicArn": str,
        "PhoneNumber": str,
        "Subject": str,
        "MessageStructure": str,
        "MessageAttributes": Dict[str, "MessageAttributeValueTypeDef"],
        "MessageDeduplicationId": str,
        "MessageGroupId": str,
    },
    total=False,
)

class PublishInputPlatformEndpointTypeDef(
    _RequiredPublishInputPlatformEndpointTypeDef, _OptionalPublishInputPlatformEndpointTypeDef
):
    pass

_RequiredPublishInputRequestTypeDef = TypedDict(
    "_RequiredPublishInputRequestTypeDef",
    {
        "Message": str,
    },
)
_OptionalPublishInputRequestTypeDef = TypedDict(
    "_OptionalPublishInputRequestTypeDef",
    {
        "TopicArn": str,
        "TargetArn": str,
        "PhoneNumber": str,
        "Subject": str,
        "MessageStructure": str,
        "MessageAttributes": Dict[str, "MessageAttributeValueTypeDef"],
        "MessageDeduplicationId": str,
        "MessageGroupId": str,
    },
    total=False,
)

class PublishInputRequestTypeDef(
    _RequiredPublishInputRequestTypeDef, _OptionalPublishInputRequestTypeDef
):
    pass

_RequiredPublishInputTopicTypeDef = TypedDict(
    "_RequiredPublishInputTopicTypeDef",
    {
        "Message": str,
    },
)
_OptionalPublishInputTopicTypeDef = TypedDict(
    "_OptionalPublishInputTopicTypeDef",
    {
        "TargetArn": str,
        "PhoneNumber": str,
        "Subject": str,
        "MessageStructure": str,
        "MessageAttributes": Dict[str, "MessageAttributeValueTypeDef"],
        "MessageDeduplicationId": str,
        "MessageGroupId": str,
    },
    total=False,
)

class PublishInputTopicTypeDef(
    _RequiredPublishInputTopicTypeDef, _OptionalPublishInputTopicTypeDef
):
    pass

PublishResponseTypeDef = TypedDict(
    "PublishResponseTypeDef",
    {
        "MessageId": str,
        "SequenceNumber": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemovePermissionInputRequestTypeDef = TypedDict(
    "RemovePermissionInputRequestTypeDef",
    {
        "TopicArn": str,
        "Label": str,
    },
)

RemovePermissionInputTopicTypeDef = TypedDict(
    "RemovePermissionInputTopicTypeDef",
    {
        "Label": str,
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

SMSSandboxPhoneNumberTypeDef = TypedDict(
    "SMSSandboxPhoneNumberTypeDef",
    {
        "PhoneNumber": str,
        "Status": SMSSandboxPhoneNumberVerificationStatusType,
    },
    total=False,
)

ServiceResourcePlatformApplicationRequestTypeDef = TypedDict(
    "ServiceResourcePlatformApplicationRequestTypeDef",
    {
        "arn": str,
    },
)

ServiceResourcePlatformEndpointRequestTypeDef = TypedDict(
    "ServiceResourcePlatformEndpointRequestTypeDef",
    {
        "arn": str,
    },
)

ServiceResourceSubscriptionRequestTypeDef = TypedDict(
    "ServiceResourceSubscriptionRequestTypeDef",
    {
        "arn": str,
    },
)

ServiceResourceTopicRequestTypeDef = TypedDict(
    "ServiceResourceTopicRequestTypeDef",
    {
        "arn": str,
    },
)

SetEndpointAttributesInputPlatformEndpointTypeDef = TypedDict(
    "SetEndpointAttributesInputPlatformEndpointTypeDef",
    {
        "Attributes": Dict[str, str],
    },
)

SetEndpointAttributesInputRequestTypeDef = TypedDict(
    "SetEndpointAttributesInputRequestTypeDef",
    {
        "EndpointArn": str,
        "Attributes": Dict[str, str],
    },
)

SetPlatformApplicationAttributesInputPlatformApplicationTypeDef = TypedDict(
    "SetPlatformApplicationAttributesInputPlatformApplicationTypeDef",
    {
        "Attributes": Dict[str, str],
    },
)

SetPlatformApplicationAttributesInputRequestTypeDef = TypedDict(
    "SetPlatformApplicationAttributesInputRequestTypeDef",
    {
        "PlatformApplicationArn": str,
        "Attributes": Dict[str, str],
    },
)

SetSMSAttributesInputRequestTypeDef = TypedDict(
    "SetSMSAttributesInputRequestTypeDef",
    {
        "attributes": Dict[str, str],
    },
)

_RequiredSetSubscriptionAttributesInputRequestTypeDef = TypedDict(
    "_RequiredSetSubscriptionAttributesInputRequestTypeDef",
    {
        "SubscriptionArn": str,
        "AttributeName": str,
    },
)
_OptionalSetSubscriptionAttributesInputRequestTypeDef = TypedDict(
    "_OptionalSetSubscriptionAttributesInputRequestTypeDef",
    {
        "AttributeValue": str,
    },
    total=False,
)

class SetSubscriptionAttributesInputRequestTypeDef(
    _RequiredSetSubscriptionAttributesInputRequestTypeDef,
    _OptionalSetSubscriptionAttributesInputRequestTypeDef,
):
    pass

_RequiredSetSubscriptionAttributesInputSubscriptionTypeDef = TypedDict(
    "_RequiredSetSubscriptionAttributesInputSubscriptionTypeDef",
    {
        "AttributeName": str,
    },
)
_OptionalSetSubscriptionAttributesInputSubscriptionTypeDef = TypedDict(
    "_OptionalSetSubscriptionAttributesInputSubscriptionTypeDef",
    {
        "AttributeValue": str,
    },
    total=False,
)

class SetSubscriptionAttributesInputSubscriptionTypeDef(
    _RequiredSetSubscriptionAttributesInputSubscriptionTypeDef,
    _OptionalSetSubscriptionAttributesInputSubscriptionTypeDef,
):
    pass

_RequiredSetTopicAttributesInputRequestTypeDef = TypedDict(
    "_RequiredSetTopicAttributesInputRequestTypeDef",
    {
        "TopicArn": str,
        "AttributeName": str,
    },
)
_OptionalSetTopicAttributesInputRequestTypeDef = TypedDict(
    "_OptionalSetTopicAttributesInputRequestTypeDef",
    {
        "AttributeValue": str,
    },
    total=False,
)

class SetTopicAttributesInputRequestTypeDef(
    _RequiredSetTopicAttributesInputRequestTypeDef, _OptionalSetTopicAttributesInputRequestTypeDef
):
    pass

_RequiredSetTopicAttributesInputTopicTypeDef = TypedDict(
    "_RequiredSetTopicAttributesInputTopicTypeDef",
    {
        "AttributeName": str,
    },
)
_OptionalSetTopicAttributesInputTopicTypeDef = TypedDict(
    "_OptionalSetTopicAttributesInputTopicTypeDef",
    {
        "AttributeValue": str,
    },
    total=False,
)

class SetTopicAttributesInputTopicTypeDef(
    _RequiredSetTopicAttributesInputTopicTypeDef, _OptionalSetTopicAttributesInputTopicTypeDef
):
    pass

_RequiredSubscribeInputRequestTypeDef = TypedDict(
    "_RequiredSubscribeInputRequestTypeDef",
    {
        "TopicArn": str,
        "Protocol": str,
    },
)
_OptionalSubscribeInputRequestTypeDef = TypedDict(
    "_OptionalSubscribeInputRequestTypeDef",
    {
        "Endpoint": str,
        "Attributes": Dict[str, str],
        "ReturnSubscriptionArn": bool,
    },
    total=False,
)

class SubscribeInputRequestTypeDef(
    _RequiredSubscribeInputRequestTypeDef, _OptionalSubscribeInputRequestTypeDef
):
    pass

_RequiredSubscribeInputTopicTypeDef = TypedDict(
    "_RequiredSubscribeInputTopicTypeDef",
    {
        "Protocol": str,
    },
)
_OptionalSubscribeInputTopicTypeDef = TypedDict(
    "_OptionalSubscribeInputTopicTypeDef",
    {
        "Endpoint": str,
        "Attributes": Dict[str, str],
        "ReturnSubscriptionArn": bool,
    },
    total=False,
)

class SubscribeInputTopicTypeDef(
    _RequiredSubscribeInputTopicTypeDef, _OptionalSubscribeInputTopicTypeDef
):
    pass

SubscribeResponseTypeDef = TypedDict(
    "SubscribeResponseTypeDef",
    {
        "SubscriptionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "SubscriptionArn": str,
        "Owner": str,
        "Protocol": str,
        "Endpoint": str,
        "TopicArn": str,
    },
    total=False,
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

TopicTypeDef = TypedDict(
    "TopicTypeDef",
    {
        "TopicArn": str,
    },
    total=False,
)

UnsubscribeInputRequestTypeDef = TypedDict(
    "UnsubscribeInputRequestTypeDef",
    {
        "SubscriptionArn": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

VerifySMSSandboxPhoneNumberInputRequestTypeDef = TypedDict(
    "VerifySMSSandboxPhoneNumberInputRequestTypeDef",
    {
        "PhoneNumber": str,
        "OneTimePassword": str,
    },
)
