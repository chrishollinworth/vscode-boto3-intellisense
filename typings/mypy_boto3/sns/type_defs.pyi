"""
Type annotations for sns service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_sns.type_defs import AddPermissionInputTopicAddPermissionTypeDef

    data: AddPermissionInputTopicAddPermissionTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    LanguageCodeStringType,
    NumberCapabilityType,
    RouteTypeType,
    SMSSandboxPhoneNumberVerificationStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AddPermissionInputTopicAddPermissionTypeDef",
    "AddPermissionInputTypeDef",
    "BatchResultErrorEntryTypeDef",
    "BlobTypeDef",
    "CheckIfPhoneNumberIsOptedOutInputTypeDef",
    "CheckIfPhoneNumberIsOptedOutResponseTypeDef",
    "ConfirmSubscriptionInputTopicConfirmSubscriptionTypeDef",
    "ConfirmSubscriptionInputTypeDef",
    "ConfirmSubscriptionResponseTypeDef",
    "CreateEndpointResponseTypeDef",
    "CreatePlatformApplicationInputServiceResourceCreatePlatformApplicationTypeDef",
    "CreatePlatformApplicationInputTypeDef",
    "CreatePlatformApplicationResponseTypeDef",
    "CreatePlatformEndpointInputPlatformApplicationCreatePlatformEndpointTypeDef",
    "CreatePlatformEndpointInputTypeDef",
    "CreateSMSSandboxPhoneNumberInputTypeDef",
    "CreateTopicInputServiceResourceCreateTopicTypeDef",
    "CreateTopicInputTypeDef",
    "CreateTopicResponseTypeDef",
    "DeleteEndpointInputTypeDef",
    "DeletePlatformApplicationInputTypeDef",
    "DeleteSMSSandboxPhoneNumberInputTypeDef",
    "DeleteTopicInputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EndpointTypeDef",
    "GetDataProtectionPolicyInputTypeDef",
    "GetDataProtectionPolicyResponseTypeDef",
    "GetEndpointAttributesInputTypeDef",
    "GetEndpointAttributesResponseTypeDef",
    "GetPlatformApplicationAttributesInputTypeDef",
    "GetPlatformApplicationAttributesResponseTypeDef",
    "GetSMSAttributesInputTypeDef",
    "GetSMSAttributesResponseTypeDef",
    "GetSMSSandboxAccountStatusResultTypeDef",
    "GetSubscriptionAttributesInputTypeDef",
    "GetSubscriptionAttributesResponseTypeDef",
    "GetTopicAttributesInputTypeDef",
    "GetTopicAttributesResponseTypeDef",
    "ListEndpointsByPlatformApplicationInputPaginateTypeDef",
    "ListEndpointsByPlatformApplicationInputTypeDef",
    "ListEndpointsByPlatformApplicationResponseTypeDef",
    "ListOriginationNumbersRequestPaginateTypeDef",
    "ListOriginationNumbersRequestTypeDef",
    "ListOriginationNumbersResultTypeDef",
    "ListPhoneNumbersOptedOutInputPaginateTypeDef",
    "ListPhoneNumbersOptedOutInputTypeDef",
    "ListPhoneNumbersOptedOutResponseTypeDef",
    "ListPlatformApplicationsInputPaginateTypeDef",
    "ListPlatformApplicationsInputTypeDef",
    "ListPlatformApplicationsResponseTypeDef",
    "ListSMSSandboxPhoneNumbersInputPaginateTypeDef",
    "ListSMSSandboxPhoneNumbersInputTypeDef",
    "ListSMSSandboxPhoneNumbersResultTypeDef",
    "ListSubscriptionsByTopicInputPaginateTypeDef",
    "ListSubscriptionsByTopicInputTypeDef",
    "ListSubscriptionsByTopicResponseTypeDef",
    "ListSubscriptionsInputPaginateTypeDef",
    "ListSubscriptionsInputTypeDef",
    "ListSubscriptionsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTopicsInputPaginateTypeDef",
    "ListTopicsInputTypeDef",
    "ListTopicsResponseTypeDef",
    "MessageAttributeValueTypeDef",
    "OptInPhoneNumberInputTypeDef",
    "PaginatorConfigTypeDef",
    "PhoneNumberInformationTypeDef",
    "PlatformApplicationTypeDef",
    "PublishBatchInputTypeDef",
    "PublishBatchRequestEntryTypeDef",
    "PublishBatchResponseTypeDef",
    "PublishBatchResultEntryTypeDef",
    "PublishInputPlatformEndpointPublishTypeDef",
    "PublishInputTopicPublishTypeDef",
    "PublishInputTypeDef",
    "PublishResponseTypeDef",
    "PutDataProtectionPolicyInputTypeDef",
    "RemovePermissionInputTopicRemovePermissionTypeDef",
    "RemovePermissionInputTypeDef",
    "ResponseMetadataTypeDef",
    "SMSSandboxPhoneNumberTypeDef",
    "SetEndpointAttributesInputPlatformEndpointSetAttributesTypeDef",
    "SetEndpointAttributesInputTypeDef",
    "SetPlatformApplicationAttributesInputPlatformApplicationSetAttributesTypeDef",
    "SetPlatformApplicationAttributesInputTypeDef",
    "SetSMSAttributesInputTypeDef",
    "SetSubscriptionAttributesInputSubscriptionSetAttributesTypeDef",
    "SetSubscriptionAttributesInputTypeDef",
    "SetTopicAttributesInputTopicSetAttributesTypeDef",
    "SetTopicAttributesInputTypeDef",
    "SubscribeInputTopicSubscribeTypeDef",
    "SubscribeInputTypeDef",
    "SubscribeResponseTypeDef",
    "SubscriptionTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TopicTypeDef",
    "UnsubscribeInputTypeDef",
    "UntagResourceRequestTypeDef",
    "VerifySMSSandboxPhoneNumberInputTypeDef",
)

class AddPermissionInputTopicAddPermissionTypeDef(TypedDict):
    Label: str
    AWSAccountId: Sequence[str]
    ActionName: Sequence[str]

class AddPermissionInputTypeDef(TypedDict):
    TopicArn: str
    Label: str
    AWSAccountId: Sequence[str]
    ActionName: Sequence[str]

class BatchResultErrorEntryTypeDef(TypedDict):
    Id: str
    Code: str
    SenderFault: bool
    Message: NotRequired[str]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class CheckIfPhoneNumberIsOptedOutInputTypeDef(TypedDict):
    phoneNumber: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ConfirmSubscriptionInputTopicConfirmSubscriptionTypeDef(TypedDict):
    Token: str
    AuthenticateOnUnsubscribe: NotRequired[str]

class ConfirmSubscriptionInputTypeDef(TypedDict):
    TopicArn: str
    Token: str
    AuthenticateOnUnsubscribe: NotRequired[str]

class CreatePlatformApplicationInputServiceResourceCreatePlatformApplicationTypeDef(TypedDict):
    Name: str
    Platform: str
    Attributes: Mapping[str, str]

class CreatePlatformApplicationInputTypeDef(TypedDict):
    Name: str
    Platform: str
    Attributes: Mapping[str, str]

class CreatePlatformEndpointInputPlatformApplicationCreatePlatformEndpointTypeDef(TypedDict):
    Token: str
    CustomUserData: NotRequired[str]
    Attributes: NotRequired[Mapping[str, str]]

class CreatePlatformEndpointInputTypeDef(TypedDict):
    PlatformApplicationArn: str
    Token: str
    CustomUserData: NotRequired[str]
    Attributes: NotRequired[Mapping[str, str]]

class CreateSMSSandboxPhoneNumberInputTypeDef(TypedDict):
    PhoneNumber: str
    LanguageCode: NotRequired[LanguageCodeStringType]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class DeleteEndpointInputTypeDef(TypedDict):
    EndpointArn: str

class DeletePlatformApplicationInputTypeDef(TypedDict):
    PlatformApplicationArn: str

class DeleteSMSSandboxPhoneNumberInputTypeDef(TypedDict):
    PhoneNumber: str

class DeleteTopicInputTypeDef(TypedDict):
    TopicArn: str

class EndpointTypeDef(TypedDict):
    EndpointArn: NotRequired[str]
    Attributes: NotRequired[Dict[str, str]]

class GetDataProtectionPolicyInputTypeDef(TypedDict):
    ResourceArn: str

class GetEndpointAttributesInputTypeDef(TypedDict):
    EndpointArn: str

class GetPlatformApplicationAttributesInputTypeDef(TypedDict):
    PlatformApplicationArn: str

class GetSMSAttributesInputTypeDef(TypedDict):
    attributes: NotRequired[Sequence[str]]

class GetSubscriptionAttributesInputTypeDef(TypedDict):
    SubscriptionArn: str

class GetTopicAttributesInputTypeDef(TypedDict):
    TopicArn: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListEndpointsByPlatformApplicationInputTypeDef(TypedDict):
    PlatformApplicationArn: str
    NextToken: NotRequired[str]

class ListOriginationNumbersRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class PhoneNumberInformationTypeDef(TypedDict):
    CreatedAt: NotRequired[datetime]
    PhoneNumber: NotRequired[str]
    Status: NotRequired[str]
    Iso2CountryCode: NotRequired[str]
    RouteType: NotRequired[RouteTypeType]
    NumberCapabilities: NotRequired[List[NumberCapabilityType]]

class ListPhoneNumbersOptedOutInputTypeDef(TypedDict):
    nextToken: NotRequired[str]

class ListPlatformApplicationsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]

class PlatformApplicationTypeDef(TypedDict):
    PlatformApplicationArn: NotRequired[str]
    Attributes: NotRequired[Dict[str, str]]

class ListSMSSandboxPhoneNumbersInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class SMSSandboxPhoneNumberTypeDef(TypedDict):
    PhoneNumber: NotRequired[str]
    Status: NotRequired[SMSSandboxPhoneNumberVerificationStatusType]

class ListSubscriptionsByTopicInputTypeDef(TypedDict):
    TopicArn: str
    NextToken: NotRequired[str]

SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "SubscriptionArn": NotRequired[str],
        "Owner": NotRequired[str],
        "Protocol": NotRequired[str],
        "Endpoint": NotRequired[str],
        "TopicArn": NotRequired[str],
    },
)

class ListSubscriptionsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class ListTopicsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]

class TopicTypeDef(TypedDict):
    TopicArn: NotRequired[str]

class OptInPhoneNumberInputTypeDef(TypedDict):
    phoneNumber: str

class PublishBatchResultEntryTypeDef(TypedDict):
    Id: NotRequired[str]
    MessageId: NotRequired[str]
    SequenceNumber: NotRequired[str]

class PutDataProtectionPolicyInputTypeDef(TypedDict):
    ResourceArn: str
    DataProtectionPolicy: str

class RemovePermissionInputTopicRemovePermissionTypeDef(TypedDict):
    Label: str

class RemovePermissionInputTypeDef(TypedDict):
    TopicArn: str
    Label: str

class SetEndpointAttributesInputPlatformEndpointSetAttributesTypeDef(TypedDict):
    Attributes: Mapping[str, str]

class SetEndpointAttributesInputTypeDef(TypedDict):
    EndpointArn: str
    Attributes: Mapping[str, str]

class SetPlatformApplicationAttributesInputPlatformApplicationSetAttributesTypeDef(TypedDict):
    Attributes: Mapping[str, str]

class SetPlatformApplicationAttributesInputTypeDef(TypedDict):
    PlatformApplicationArn: str
    Attributes: Mapping[str, str]

class SetSMSAttributesInputTypeDef(TypedDict):
    attributes: Mapping[str, str]

class SetSubscriptionAttributesInputSubscriptionSetAttributesTypeDef(TypedDict):
    AttributeName: str
    AttributeValue: NotRequired[str]

class SetSubscriptionAttributesInputTypeDef(TypedDict):
    SubscriptionArn: str
    AttributeName: str
    AttributeValue: NotRequired[str]

class SetTopicAttributesInputTopicSetAttributesTypeDef(TypedDict):
    AttributeName: str
    AttributeValue: NotRequired[str]

class SetTopicAttributesInputTypeDef(TypedDict):
    TopicArn: str
    AttributeName: str
    AttributeValue: NotRequired[str]

SubscribeInputTopicSubscribeTypeDef = TypedDict(
    "SubscribeInputTopicSubscribeTypeDef",
    {
        "Protocol": str,
        "Endpoint": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, str]],
        "ReturnSubscriptionArn": NotRequired[bool],
    },
)
SubscribeInputTypeDef = TypedDict(
    "SubscribeInputTypeDef",
    {
        "TopicArn": str,
        "Protocol": str,
        "Endpoint": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, str]],
        "ReturnSubscriptionArn": NotRequired[bool],
    },
)

class UnsubscribeInputTypeDef(TypedDict):
    SubscriptionArn: str

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class VerifySMSSandboxPhoneNumberInputTypeDef(TypedDict):
    PhoneNumber: str
    OneTimePassword: str

class MessageAttributeValueTypeDef(TypedDict):
    DataType: str
    StringValue: NotRequired[str]
    BinaryValue: NotRequired[BlobTypeDef]

class CheckIfPhoneNumberIsOptedOutResponseTypeDef(TypedDict):
    isOptedOut: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ConfirmSubscriptionResponseTypeDef(TypedDict):
    SubscriptionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEndpointResponseTypeDef(TypedDict):
    EndpointArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePlatformApplicationResponseTypeDef(TypedDict):
    PlatformApplicationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTopicResponseTypeDef(TypedDict):
    TopicArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataProtectionPolicyResponseTypeDef(TypedDict):
    DataProtectionPolicy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEndpointAttributesResponseTypeDef(TypedDict):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetPlatformApplicationAttributesResponseTypeDef(TypedDict):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSMSAttributesResponseTypeDef(TypedDict):
    attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSMSSandboxAccountStatusResultTypeDef(TypedDict):
    IsInSandbox: bool
    ResponseMetadata: ResponseMetadataTypeDef

class GetSubscriptionAttributesResponseTypeDef(TypedDict):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetTopicAttributesResponseTypeDef(TypedDict):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPhoneNumbersOptedOutResponseTypeDef(TypedDict):
    phoneNumbers: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class PublishResponseTypeDef(TypedDict):
    MessageId: str
    SequenceNumber: str
    ResponseMetadata: ResponseMetadataTypeDef

class SubscribeResponseTypeDef(TypedDict):
    SubscriptionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTopicInputServiceResourceCreateTopicTypeDef(TypedDict):
    Name: str
    Attributes: NotRequired[Mapping[str, str]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    DataProtectionPolicy: NotRequired[str]

class CreateTopicInputTypeDef(TypedDict):
    Name: str
    Attributes: NotRequired[Mapping[str, str]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    DataProtectionPolicy: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class ListEndpointsByPlatformApplicationResponseTypeDef(TypedDict):
    Endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListEndpointsByPlatformApplicationInputPaginateTypeDef(TypedDict):
    PlatformApplicationArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOriginationNumbersRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPhoneNumbersOptedOutInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPlatformApplicationsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSMSSandboxPhoneNumbersInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSubscriptionsByTopicInputPaginateTypeDef(TypedDict):
    TopicArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSubscriptionsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTopicsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOriginationNumbersResultTypeDef(TypedDict):
    PhoneNumbers: List[PhoneNumberInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListPlatformApplicationsResponseTypeDef(TypedDict):
    PlatformApplications: List[PlatformApplicationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSMSSandboxPhoneNumbersResultTypeDef(TypedDict):
    PhoneNumbers: List[SMSSandboxPhoneNumberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSubscriptionsByTopicResponseTypeDef(TypedDict):
    Subscriptions: List[SubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSubscriptionsResponseTypeDef(TypedDict):
    Subscriptions: List[SubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTopicsResponseTypeDef(TypedDict):
    Topics: List[TopicTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PublishBatchResponseTypeDef(TypedDict):
    Successful: List[PublishBatchResultEntryTypeDef]
    Failed: List[BatchResultErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PublishBatchRequestEntryTypeDef(TypedDict):
    Id: str
    Message: str
    Subject: NotRequired[str]
    MessageStructure: NotRequired[str]
    MessageAttributes: NotRequired[Mapping[str, MessageAttributeValueTypeDef]]
    MessageDeduplicationId: NotRequired[str]
    MessageGroupId: NotRequired[str]

class PublishInputPlatformEndpointPublishTypeDef(TypedDict):
    Message: str
    TopicArn: NotRequired[str]
    PhoneNumber: NotRequired[str]
    Subject: NotRequired[str]
    MessageStructure: NotRequired[str]
    MessageAttributes: NotRequired[Mapping[str, MessageAttributeValueTypeDef]]
    MessageDeduplicationId: NotRequired[str]
    MessageGroupId: NotRequired[str]

class PublishInputTopicPublishTypeDef(TypedDict):
    Message: str
    TargetArn: NotRequired[str]
    PhoneNumber: NotRequired[str]
    Subject: NotRequired[str]
    MessageStructure: NotRequired[str]
    MessageAttributes: NotRequired[Mapping[str, MessageAttributeValueTypeDef]]
    MessageDeduplicationId: NotRequired[str]
    MessageGroupId: NotRequired[str]

class PublishInputTypeDef(TypedDict):
    Message: str
    TopicArn: NotRequired[str]
    TargetArn: NotRequired[str]
    PhoneNumber: NotRequired[str]
    Subject: NotRequired[str]
    MessageStructure: NotRequired[str]
    MessageAttributes: NotRequired[Mapping[str, MessageAttributeValueTypeDef]]
    MessageDeduplicationId: NotRequired[str]
    MessageGroupId: NotRequired[str]

class PublishBatchInputTypeDef(TypedDict):
    TopicArn: str
    PublishBatchRequestEntries: Sequence[PublishBatchRequestEntryTypeDef]
