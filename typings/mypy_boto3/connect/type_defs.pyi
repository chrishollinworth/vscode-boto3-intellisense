"""
Type annotations for connect service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/type_defs.html)

Usage::

    ```python
    from mypy_boto3_connect.type_defs import AssociateApprovedOriginRequestRequestTypeDef

    data: AssociateApprovedOriginRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ChannelType,
    ContactFlowTypeType,
    CurrentMetricNameType,
    DirectoryTypeType,
    GroupingType,
    HistoricalMetricNameType,
    HoursOfOperationDaysType,
    InstanceAttributeTypeType,
    InstanceStatusType,
    InstanceStorageResourceTypeType,
    LexVersionType,
    PhoneNumberCountryCodeType,
    PhoneNumberTypeType,
    PhoneTypeType,
    QueueStatusType,
    QueueTypeType,
    QuickConnectTypeType,
    SourceTypeType,
    StatisticType,
    StorageTypeType,
    UnitType,
    VoiceRecordingTrackType,
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
    "AssociateApprovedOriginRequestRequestTypeDef",
    "AssociateBotRequestRequestTypeDef",
    "AssociateInstanceStorageConfigRequestRequestTypeDef",
    "AssociateInstanceStorageConfigResponseTypeDef",
    "AssociateLambdaFunctionRequestRequestTypeDef",
    "AssociateLexBotRequestRequestTypeDef",
    "AssociateQueueQuickConnectsRequestRequestTypeDef",
    "AssociateRoutingProfileQueuesRequestRequestTypeDef",
    "AssociateSecurityKeyRequestRequestTypeDef",
    "AssociateSecurityKeyResponseTypeDef",
    "AttributeTypeDef",
    "ChatMessageTypeDef",
    "ContactFlowSummaryTypeDef",
    "ContactFlowTypeDef",
    "CreateContactFlowRequestRequestTypeDef",
    "CreateContactFlowResponseTypeDef",
    "CreateInstanceRequestRequestTypeDef",
    "CreateInstanceResponseTypeDef",
    "CreateIntegrationAssociationRequestRequestTypeDef",
    "CreateIntegrationAssociationResponseTypeDef",
    "CreateQueueRequestRequestTypeDef",
    "CreateQueueResponseTypeDef",
    "CreateQuickConnectRequestRequestTypeDef",
    "CreateQuickConnectResponseTypeDef",
    "CreateRoutingProfileRequestRequestTypeDef",
    "CreateRoutingProfileResponseTypeDef",
    "CreateUseCaseRequestRequestTypeDef",
    "CreateUseCaseResponseTypeDef",
    "CreateUserHierarchyGroupRequestRequestTypeDef",
    "CreateUserHierarchyGroupResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CreateUserResponseTypeDef",
    "CredentialsTypeDef",
    "CurrentMetricDataTypeDef",
    "CurrentMetricResultTypeDef",
    "CurrentMetricTypeDef",
    "DeleteInstanceRequestRequestTypeDef",
    "DeleteIntegrationAssociationRequestRequestTypeDef",
    "DeleteQuickConnectRequestRequestTypeDef",
    "DeleteUseCaseRequestRequestTypeDef",
    "DeleteUserHierarchyGroupRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DescribeContactFlowRequestRequestTypeDef",
    "DescribeContactFlowResponseTypeDef",
    "DescribeHoursOfOperationRequestRequestTypeDef",
    "DescribeHoursOfOperationResponseTypeDef",
    "DescribeInstanceAttributeRequestRequestTypeDef",
    "DescribeInstanceAttributeResponseTypeDef",
    "DescribeInstanceRequestRequestTypeDef",
    "DescribeInstanceResponseTypeDef",
    "DescribeInstanceStorageConfigRequestRequestTypeDef",
    "DescribeInstanceStorageConfigResponseTypeDef",
    "DescribeQueueRequestRequestTypeDef",
    "DescribeQueueResponseTypeDef",
    "DescribeQuickConnectRequestRequestTypeDef",
    "DescribeQuickConnectResponseTypeDef",
    "DescribeRoutingProfileRequestRequestTypeDef",
    "DescribeRoutingProfileResponseTypeDef",
    "DescribeUserHierarchyGroupRequestRequestTypeDef",
    "DescribeUserHierarchyGroupResponseTypeDef",
    "DescribeUserHierarchyStructureRequestRequestTypeDef",
    "DescribeUserHierarchyStructureResponseTypeDef",
    "DescribeUserRequestRequestTypeDef",
    "DescribeUserResponseTypeDef",
    "DimensionsTypeDef",
    "DisassociateApprovedOriginRequestRequestTypeDef",
    "DisassociateBotRequestRequestTypeDef",
    "DisassociateInstanceStorageConfigRequestRequestTypeDef",
    "DisassociateLambdaFunctionRequestRequestTypeDef",
    "DisassociateLexBotRequestRequestTypeDef",
    "DisassociateQueueQuickConnectsRequestRequestTypeDef",
    "DisassociateRoutingProfileQueuesRequestRequestTypeDef",
    "DisassociateSecurityKeyRequestRequestTypeDef",
    "EncryptionConfigTypeDef",
    "FiltersTypeDef",
    "GetContactAttributesRequestRequestTypeDef",
    "GetContactAttributesResponseTypeDef",
    "GetCurrentMetricDataRequestRequestTypeDef",
    "GetCurrentMetricDataResponseTypeDef",
    "GetFederationTokenRequestRequestTypeDef",
    "GetFederationTokenResponseTypeDef",
    "GetMetricDataRequestRequestTypeDef",
    "GetMetricDataResponseTypeDef",
    "HierarchyGroupSummaryTypeDef",
    "HierarchyGroupTypeDef",
    "HierarchyLevelTypeDef",
    "HierarchyLevelUpdateTypeDef",
    "HierarchyPathTypeDef",
    "HierarchyStructureTypeDef",
    "HierarchyStructureUpdateTypeDef",
    "HistoricalMetricDataTypeDef",
    "HistoricalMetricResultTypeDef",
    "HistoricalMetricTypeDef",
    "HoursOfOperationConfigTypeDef",
    "HoursOfOperationSummaryTypeDef",
    "HoursOfOperationTimeSliceTypeDef",
    "HoursOfOperationTypeDef",
    "InstanceStatusReasonTypeDef",
    "InstanceStorageConfigTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTypeDef",
    "IntegrationAssociationSummaryTypeDef",
    "KinesisFirehoseConfigTypeDef",
    "KinesisStreamConfigTypeDef",
    "KinesisVideoStreamConfigTypeDef",
    "LexBotConfigTypeDef",
    "LexBotTypeDef",
    "LexV2BotTypeDef",
    "ListApprovedOriginsRequestRequestTypeDef",
    "ListApprovedOriginsResponseTypeDef",
    "ListBotsRequestRequestTypeDef",
    "ListBotsResponseTypeDef",
    "ListContactFlowsRequestRequestTypeDef",
    "ListContactFlowsResponseTypeDef",
    "ListHoursOfOperationsRequestRequestTypeDef",
    "ListHoursOfOperationsResponseTypeDef",
    "ListInstanceAttributesRequestRequestTypeDef",
    "ListInstanceAttributesResponseTypeDef",
    "ListInstanceStorageConfigsRequestRequestTypeDef",
    "ListInstanceStorageConfigsResponseTypeDef",
    "ListInstancesRequestRequestTypeDef",
    "ListInstancesResponseTypeDef",
    "ListIntegrationAssociationsRequestRequestTypeDef",
    "ListIntegrationAssociationsResponseTypeDef",
    "ListLambdaFunctionsRequestRequestTypeDef",
    "ListLambdaFunctionsResponseTypeDef",
    "ListLexBotsRequestRequestTypeDef",
    "ListLexBotsResponseTypeDef",
    "ListPhoneNumbersRequestRequestTypeDef",
    "ListPhoneNumbersResponseTypeDef",
    "ListPromptsRequestRequestTypeDef",
    "ListPromptsResponseTypeDef",
    "ListQueueQuickConnectsRequestRequestTypeDef",
    "ListQueueQuickConnectsResponseTypeDef",
    "ListQueuesRequestRequestTypeDef",
    "ListQueuesResponseTypeDef",
    "ListQuickConnectsRequestRequestTypeDef",
    "ListQuickConnectsResponseTypeDef",
    "ListRoutingProfileQueuesRequestRequestTypeDef",
    "ListRoutingProfileQueuesResponseTypeDef",
    "ListRoutingProfilesRequestRequestTypeDef",
    "ListRoutingProfilesResponseTypeDef",
    "ListSecurityKeysRequestRequestTypeDef",
    "ListSecurityKeysResponseTypeDef",
    "ListSecurityProfilesRequestRequestTypeDef",
    "ListSecurityProfilesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUseCasesRequestRequestTypeDef",
    "ListUseCasesResponseTypeDef",
    "ListUserHierarchyGroupsRequestRequestTypeDef",
    "ListUserHierarchyGroupsResponseTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "MediaConcurrencyTypeDef",
    "OutboundCallerConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipantDetailsTypeDef",
    "PhoneNumberQuickConnectConfigTypeDef",
    "PhoneNumberSummaryTypeDef",
    "PromptSummaryTypeDef",
    "QueueQuickConnectConfigTypeDef",
    "QueueReferenceTypeDef",
    "QueueSummaryTypeDef",
    "QueueTypeDef",
    "QuickConnectConfigTypeDef",
    "QuickConnectSummaryTypeDef",
    "QuickConnectTypeDef",
    "ReferenceTypeDef",
    "ResponseMetadataTypeDef",
    "ResumeContactRecordingRequestRequestTypeDef",
    "RoutingProfileQueueConfigSummaryTypeDef",
    "RoutingProfileQueueConfigTypeDef",
    "RoutingProfileQueueReferenceTypeDef",
    "RoutingProfileSummaryTypeDef",
    "RoutingProfileTypeDef",
    "S3ConfigTypeDef",
    "SecurityKeyTypeDef",
    "SecurityProfileSummaryTypeDef",
    "StartChatContactRequestRequestTypeDef",
    "StartChatContactResponseTypeDef",
    "StartContactRecordingRequestRequestTypeDef",
    "StartOutboundVoiceContactRequestRequestTypeDef",
    "StartOutboundVoiceContactResponseTypeDef",
    "StartTaskContactRequestRequestTypeDef",
    "StartTaskContactResponseTypeDef",
    "StopContactRecordingRequestRequestTypeDef",
    "StopContactRequestRequestTypeDef",
    "SuspendContactRecordingRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ThresholdTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateContactAttributesRequestRequestTypeDef",
    "UpdateContactFlowContentRequestRequestTypeDef",
    "UpdateContactFlowNameRequestRequestTypeDef",
    "UpdateInstanceAttributeRequestRequestTypeDef",
    "UpdateInstanceStorageConfigRequestRequestTypeDef",
    "UpdateQueueHoursOfOperationRequestRequestTypeDef",
    "UpdateQueueMaxContactsRequestRequestTypeDef",
    "UpdateQueueNameRequestRequestTypeDef",
    "UpdateQueueOutboundCallerConfigRequestRequestTypeDef",
    "UpdateQueueStatusRequestRequestTypeDef",
    "UpdateQuickConnectConfigRequestRequestTypeDef",
    "UpdateQuickConnectNameRequestRequestTypeDef",
    "UpdateRoutingProfileConcurrencyRequestRequestTypeDef",
    "UpdateRoutingProfileDefaultOutboundQueueRequestRequestTypeDef",
    "UpdateRoutingProfileNameRequestRequestTypeDef",
    "UpdateRoutingProfileQueuesRequestRequestTypeDef",
    "UpdateUserHierarchyGroupNameRequestRequestTypeDef",
    "UpdateUserHierarchyRequestRequestTypeDef",
    "UpdateUserHierarchyStructureRequestRequestTypeDef",
    "UpdateUserIdentityInfoRequestRequestTypeDef",
    "UpdateUserPhoneConfigRequestRequestTypeDef",
    "UpdateUserRoutingProfileRequestRequestTypeDef",
    "UpdateUserSecurityProfilesRequestRequestTypeDef",
    "UseCaseTypeDef",
    "UserIdentityInfoTypeDef",
    "UserPhoneConfigTypeDef",
    "UserQuickConnectConfigTypeDef",
    "UserSummaryTypeDef",
    "UserTypeDef",
    "VoiceRecordingConfigurationTypeDef",
)

AssociateApprovedOriginRequestRequestTypeDef = TypedDict(
    "AssociateApprovedOriginRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Origin": str,
    },
)

_RequiredAssociateBotRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateBotRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalAssociateBotRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateBotRequestRequestTypeDef",
    {
        "LexBot": "LexBotTypeDef",
        "LexV2Bot": "LexV2BotTypeDef",
    },
    total=False,
)

class AssociateBotRequestRequestTypeDef(
    _RequiredAssociateBotRequestRequestTypeDef, _OptionalAssociateBotRequestRequestTypeDef
):
    pass

AssociateInstanceStorageConfigRequestRequestTypeDef = TypedDict(
    "AssociateInstanceStorageConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ResourceType": InstanceStorageResourceTypeType,
        "StorageConfig": "InstanceStorageConfigTypeDef",
    },
)

AssociateInstanceStorageConfigResponseTypeDef = TypedDict(
    "AssociateInstanceStorageConfigResponseTypeDef",
    {
        "AssociationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateLambdaFunctionRequestRequestTypeDef = TypedDict(
    "AssociateLambdaFunctionRequestRequestTypeDef",
    {
        "InstanceId": str,
        "FunctionArn": str,
    },
)

AssociateLexBotRequestRequestTypeDef = TypedDict(
    "AssociateLexBotRequestRequestTypeDef",
    {
        "InstanceId": str,
        "LexBot": "LexBotTypeDef",
    },
)

AssociateQueueQuickConnectsRequestRequestTypeDef = TypedDict(
    "AssociateQueueQuickConnectsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "QuickConnectIds": List[str],
    },
)

AssociateRoutingProfileQueuesRequestRequestTypeDef = TypedDict(
    "AssociateRoutingProfileQueuesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "QueueConfigs": List["RoutingProfileQueueConfigTypeDef"],
    },
)

AssociateSecurityKeyRequestRequestTypeDef = TypedDict(
    "AssociateSecurityKeyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Key": str,
    },
)

AssociateSecurityKeyResponseTypeDef = TypedDict(
    "AssociateSecurityKeyResponseTypeDef",
    {
        "AssociationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "AttributeType": InstanceAttributeTypeType,
        "Value": str,
    },
    total=False,
)

ChatMessageTypeDef = TypedDict(
    "ChatMessageTypeDef",
    {
        "ContentType": str,
        "Content": str,
    },
)

ContactFlowSummaryTypeDef = TypedDict(
    "ContactFlowSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "ContactFlowType": ContactFlowTypeType,
    },
    total=False,
)

ContactFlowTypeDef = TypedDict(
    "ContactFlowTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Type": ContactFlowTypeType,
        "Description": str,
        "Content": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredCreateContactFlowRequestRequestTypeDef = TypedDict(
    "_RequiredCreateContactFlowRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "Type": ContactFlowTypeType,
        "Content": str,
    },
)
_OptionalCreateContactFlowRequestRequestTypeDef = TypedDict(
    "_OptionalCreateContactFlowRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateContactFlowRequestRequestTypeDef(
    _RequiredCreateContactFlowRequestRequestTypeDef, _OptionalCreateContactFlowRequestRequestTypeDef
):
    pass

CreateContactFlowResponseTypeDef = TypedDict(
    "CreateContactFlowResponseTypeDef",
    {
        "ContactFlowId": str,
        "ContactFlowArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateInstanceRequestRequestTypeDef",
    {
        "IdentityManagementType": DirectoryTypeType,
        "InboundCallsEnabled": bool,
        "OutboundCallsEnabled": bool,
    },
)
_OptionalCreateInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateInstanceRequestRequestTypeDef",
    {
        "ClientToken": str,
        "InstanceAlias": str,
        "DirectoryId": str,
    },
    total=False,
)

class CreateInstanceRequestRequestTypeDef(
    _RequiredCreateInstanceRequestRequestTypeDef, _OptionalCreateInstanceRequestRequestTypeDef
):
    pass

CreateInstanceResponseTypeDef = TypedDict(
    "CreateInstanceResponseTypeDef",
    {
        "Id": str,
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIntegrationAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIntegrationAssociationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationType": Literal["EVENT"],
        "IntegrationArn": str,
        "SourceApplicationUrl": str,
        "SourceApplicationName": str,
        "SourceType": SourceTypeType,
    },
)
_OptionalCreateIntegrationAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIntegrationAssociationRequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateIntegrationAssociationRequestRequestTypeDef(
    _RequiredCreateIntegrationAssociationRequestRequestTypeDef,
    _OptionalCreateIntegrationAssociationRequestRequestTypeDef,
):
    pass

CreateIntegrationAssociationResponseTypeDef = TypedDict(
    "CreateIntegrationAssociationResponseTypeDef",
    {
        "IntegrationAssociationId": str,
        "IntegrationAssociationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateQueueRequestRequestTypeDef = TypedDict(
    "_RequiredCreateQueueRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "HoursOfOperationId": str,
    },
)
_OptionalCreateQueueRequestRequestTypeDef = TypedDict(
    "_OptionalCreateQueueRequestRequestTypeDef",
    {
        "Description": str,
        "OutboundCallerConfig": "OutboundCallerConfigTypeDef",
        "MaxContacts": int,
        "QuickConnectIds": List[str],
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateQueueRequestRequestTypeDef(
    _RequiredCreateQueueRequestRequestTypeDef, _OptionalCreateQueueRequestRequestTypeDef
):
    pass

CreateQueueResponseTypeDef = TypedDict(
    "CreateQueueResponseTypeDef",
    {
        "QueueArn": str,
        "QueueId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateQuickConnectRequestRequestTypeDef = TypedDict(
    "_RequiredCreateQuickConnectRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "QuickConnectConfig": "QuickConnectConfigTypeDef",
    },
)
_OptionalCreateQuickConnectRequestRequestTypeDef = TypedDict(
    "_OptionalCreateQuickConnectRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateQuickConnectRequestRequestTypeDef(
    _RequiredCreateQuickConnectRequestRequestTypeDef,
    _OptionalCreateQuickConnectRequestRequestTypeDef,
):
    pass

CreateQuickConnectResponseTypeDef = TypedDict(
    "CreateQuickConnectResponseTypeDef",
    {
        "QuickConnectARN": str,
        "QuickConnectId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRoutingProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRoutingProfileRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "Description": str,
        "DefaultOutboundQueueId": str,
        "MediaConcurrencies": List["MediaConcurrencyTypeDef"],
    },
)
_OptionalCreateRoutingProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRoutingProfileRequestRequestTypeDef",
    {
        "QueueConfigs": List["RoutingProfileQueueConfigTypeDef"],
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateRoutingProfileRequestRequestTypeDef(
    _RequiredCreateRoutingProfileRequestRequestTypeDef,
    _OptionalCreateRoutingProfileRequestRequestTypeDef,
):
    pass

CreateRoutingProfileResponseTypeDef = TypedDict(
    "CreateRoutingProfileResponseTypeDef",
    {
        "RoutingProfileArn": str,
        "RoutingProfileId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUseCaseRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUseCaseRequestRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationAssociationId": str,
        "UseCaseType": Literal["RULES_EVALUATION"],
    },
)
_OptionalCreateUseCaseRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUseCaseRequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateUseCaseRequestRequestTypeDef(
    _RequiredCreateUseCaseRequestRequestTypeDef, _OptionalCreateUseCaseRequestRequestTypeDef
):
    pass

CreateUseCaseResponseTypeDef = TypedDict(
    "CreateUseCaseResponseTypeDef",
    {
        "UseCaseId": str,
        "UseCaseArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserHierarchyGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserHierarchyGroupRequestRequestTypeDef",
    {
        "Name": str,
        "InstanceId": str,
    },
)
_OptionalCreateUserHierarchyGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserHierarchyGroupRequestRequestTypeDef",
    {
        "ParentGroupId": str,
    },
    total=False,
)

class CreateUserHierarchyGroupRequestRequestTypeDef(
    _RequiredCreateUserHierarchyGroupRequestRequestTypeDef,
    _OptionalCreateUserHierarchyGroupRequestRequestTypeDef,
):
    pass

CreateUserHierarchyGroupResponseTypeDef = TypedDict(
    "CreateUserHierarchyGroupResponseTypeDef",
    {
        "HierarchyGroupId": str,
        "HierarchyGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserRequestRequestTypeDef",
    {
        "Username": str,
        "PhoneConfig": "UserPhoneConfigTypeDef",
        "SecurityProfileIds": List[str],
        "RoutingProfileId": str,
        "InstanceId": str,
    },
)
_OptionalCreateUserRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserRequestRequestTypeDef",
    {
        "Password": str,
        "IdentityInfo": "UserIdentityInfoTypeDef",
        "DirectoryUserId": str,
        "HierarchyGroupId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateUserRequestRequestTypeDef(
    _RequiredCreateUserRequestRequestTypeDef, _OptionalCreateUserRequestRequestTypeDef
):
    pass

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "UserId": str,
        "UserArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
    "CurrentMetricDataTypeDef",
    {
        "Metric": "CurrentMetricTypeDef",
        "Value": float,
    },
    total=False,
)

CurrentMetricResultTypeDef = TypedDict(
    "CurrentMetricResultTypeDef",
    {
        "Dimensions": "DimensionsTypeDef",
        "Collections": List["CurrentMetricDataTypeDef"],
    },
    total=False,
)

CurrentMetricTypeDef = TypedDict(
    "CurrentMetricTypeDef",
    {
        "Name": CurrentMetricNameType,
        "Unit": UnitType,
    },
    total=False,
)

DeleteInstanceRequestRequestTypeDef = TypedDict(
    "DeleteInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)

DeleteIntegrationAssociationRequestRequestTypeDef = TypedDict(
    "DeleteIntegrationAssociationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationAssociationId": str,
    },
)

DeleteQuickConnectRequestRequestTypeDef = TypedDict(
    "DeleteQuickConnectRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QuickConnectId": str,
    },
)

DeleteUseCaseRequestRequestTypeDef = TypedDict(
    "DeleteUseCaseRequestRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationAssociationId": str,
        "UseCaseId": str,
    },
)

DeleteUserHierarchyGroupRequestRequestTypeDef = TypedDict(
    "DeleteUserHierarchyGroupRequestRequestTypeDef",
    {
        "HierarchyGroupId": str,
        "InstanceId": str,
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "InstanceId": str,
        "UserId": str,
    },
)

DescribeContactFlowRequestRequestTypeDef = TypedDict(
    "DescribeContactFlowRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
    },
)

DescribeContactFlowResponseTypeDef = TypedDict(
    "DescribeContactFlowResponseTypeDef",
    {
        "ContactFlow": "ContactFlowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHoursOfOperationRequestRequestTypeDef = TypedDict(
    "DescribeHoursOfOperationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "HoursOfOperationId": str,
    },
)

DescribeHoursOfOperationResponseTypeDef = TypedDict(
    "DescribeHoursOfOperationResponseTypeDef",
    {
        "HoursOfOperation": "HoursOfOperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceAttributeRequestRequestTypeDef = TypedDict(
    "DescribeInstanceAttributeRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AttributeType": InstanceAttributeTypeType,
    },
)

DescribeInstanceAttributeResponseTypeDef = TypedDict(
    "DescribeInstanceAttributeResponseTypeDef",
    {
        "Attribute": "AttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceRequestRequestTypeDef = TypedDict(
    "DescribeInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)

DescribeInstanceResponseTypeDef = TypedDict(
    "DescribeInstanceResponseTypeDef",
    {
        "Instance": "InstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceStorageConfigRequestRequestTypeDef = TypedDict(
    "DescribeInstanceStorageConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AssociationId": str,
        "ResourceType": InstanceStorageResourceTypeType,
    },
)

DescribeInstanceStorageConfigResponseTypeDef = TypedDict(
    "DescribeInstanceStorageConfigResponseTypeDef",
    {
        "StorageConfig": "InstanceStorageConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeQueueRequestRequestTypeDef = TypedDict(
    "DescribeQueueRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
    },
)

DescribeQueueResponseTypeDef = TypedDict(
    "DescribeQueueResponseTypeDef",
    {
        "Queue": "QueueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeQuickConnectRequestRequestTypeDef = TypedDict(
    "DescribeQuickConnectRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QuickConnectId": str,
    },
)

DescribeQuickConnectResponseTypeDef = TypedDict(
    "DescribeQuickConnectResponseTypeDef",
    {
        "QuickConnect": "QuickConnectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRoutingProfileRequestRequestTypeDef = TypedDict(
    "DescribeRoutingProfileRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
    },
)

DescribeRoutingProfileResponseTypeDef = TypedDict(
    "DescribeRoutingProfileResponseTypeDef",
    {
        "RoutingProfile": "RoutingProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserHierarchyGroupRequestRequestTypeDef = TypedDict(
    "DescribeUserHierarchyGroupRequestRequestTypeDef",
    {
        "HierarchyGroupId": str,
        "InstanceId": str,
    },
)

DescribeUserHierarchyGroupResponseTypeDef = TypedDict(
    "DescribeUserHierarchyGroupResponseTypeDef",
    {
        "HierarchyGroup": "HierarchyGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserHierarchyStructureRequestRequestTypeDef = TypedDict(
    "DescribeUserHierarchyStructureRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)

DescribeUserHierarchyStructureResponseTypeDef = TypedDict(
    "DescribeUserHierarchyStructureResponseTypeDef",
    {
        "HierarchyStructure": "HierarchyStructureTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserRequestRequestTypeDef = TypedDict(
    "DescribeUserRequestRequestTypeDef",
    {
        "UserId": str,
        "InstanceId": str,
    },
)

DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DimensionsTypeDef = TypedDict(
    "DimensionsTypeDef",
    {
        "Queue": "QueueReferenceTypeDef",
        "Channel": ChannelType,
    },
    total=False,
)

DisassociateApprovedOriginRequestRequestTypeDef = TypedDict(
    "DisassociateApprovedOriginRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Origin": str,
    },
)

_RequiredDisassociateBotRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateBotRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalDisassociateBotRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateBotRequestRequestTypeDef",
    {
        "LexBot": "LexBotTypeDef",
        "LexV2Bot": "LexV2BotTypeDef",
    },
    total=False,
)

class DisassociateBotRequestRequestTypeDef(
    _RequiredDisassociateBotRequestRequestTypeDef, _OptionalDisassociateBotRequestRequestTypeDef
):
    pass

DisassociateInstanceStorageConfigRequestRequestTypeDef = TypedDict(
    "DisassociateInstanceStorageConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AssociationId": str,
        "ResourceType": InstanceStorageResourceTypeType,
    },
)

DisassociateLambdaFunctionRequestRequestTypeDef = TypedDict(
    "DisassociateLambdaFunctionRequestRequestTypeDef",
    {
        "InstanceId": str,
        "FunctionArn": str,
    },
)

DisassociateLexBotRequestRequestTypeDef = TypedDict(
    "DisassociateLexBotRequestRequestTypeDef",
    {
        "InstanceId": str,
        "BotName": str,
        "LexRegion": str,
    },
)

DisassociateQueueQuickConnectsRequestRequestTypeDef = TypedDict(
    "DisassociateQueueQuickConnectsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "QuickConnectIds": List[str],
    },
)

DisassociateRoutingProfileQueuesRequestRequestTypeDef = TypedDict(
    "DisassociateRoutingProfileQueuesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "QueueReferences": List["RoutingProfileQueueReferenceTypeDef"],
    },
)

DisassociateSecurityKeyRequestRequestTypeDef = TypedDict(
    "DisassociateSecurityKeyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AssociationId": str,
    },
)

EncryptionConfigTypeDef = TypedDict(
    "EncryptionConfigTypeDef",
    {
        "EncryptionType": Literal["KMS"],
        "KeyId": str,
    },
)

FiltersTypeDef = TypedDict(
    "FiltersTypeDef",
    {
        "Queues": List[str],
        "Channels": List[ChannelType],
    },
    total=False,
)

GetContactAttributesRequestRequestTypeDef = TypedDict(
    "GetContactAttributesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "InitialContactId": str,
    },
)

GetContactAttributesResponseTypeDef = TypedDict(
    "GetContactAttributesResponseTypeDef",
    {
        "Attributes": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCurrentMetricDataRequestRequestTypeDef = TypedDict(
    "_RequiredGetCurrentMetricDataRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Filters": "FiltersTypeDef",
        "CurrentMetrics": List["CurrentMetricTypeDef"],
    },
)
_OptionalGetCurrentMetricDataRequestRequestTypeDef = TypedDict(
    "_OptionalGetCurrentMetricDataRequestRequestTypeDef",
    {
        "Groupings": List[GroupingType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetCurrentMetricDataRequestRequestTypeDef(
    _RequiredGetCurrentMetricDataRequestRequestTypeDef,
    _OptionalGetCurrentMetricDataRequestRequestTypeDef,
):
    pass

GetCurrentMetricDataResponseTypeDef = TypedDict(
    "GetCurrentMetricDataResponseTypeDef",
    {
        "NextToken": str,
        "MetricResults": List["CurrentMetricResultTypeDef"],
        "DataSnapshotTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFederationTokenRequestRequestTypeDef = TypedDict(
    "GetFederationTokenRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)

GetFederationTokenResponseTypeDef = TypedDict(
    "GetFederationTokenResponseTypeDef",
    {
        "Credentials": "CredentialsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMetricDataRequestRequestTypeDef = TypedDict(
    "_RequiredGetMetricDataRequestRequestTypeDef",
    {
        "InstanceId": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Filters": "FiltersTypeDef",
        "HistoricalMetrics": List["HistoricalMetricTypeDef"],
    },
)
_OptionalGetMetricDataRequestRequestTypeDef = TypedDict(
    "_OptionalGetMetricDataRequestRequestTypeDef",
    {
        "Groupings": List[GroupingType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetMetricDataRequestRequestTypeDef(
    _RequiredGetMetricDataRequestRequestTypeDef, _OptionalGetMetricDataRequestRequestTypeDef
):
    pass

GetMetricDataResponseTypeDef = TypedDict(
    "GetMetricDataResponseTypeDef",
    {
        "NextToken": str,
        "MetricResults": List["HistoricalMetricResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HierarchyGroupSummaryTypeDef = TypedDict(
    "HierarchyGroupSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

HierarchyGroupTypeDef = TypedDict(
    "HierarchyGroupTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "LevelId": str,
        "HierarchyPath": "HierarchyPathTypeDef",
    },
    total=False,
)

HierarchyLevelTypeDef = TypedDict(
    "HierarchyLevelTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

HierarchyLevelUpdateTypeDef = TypedDict(
    "HierarchyLevelUpdateTypeDef",
    {
        "Name": str,
    },
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

HierarchyStructureUpdateTypeDef = TypedDict(
    "HierarchyStructureUpdateTypeDef",
    {
        "LevelOne": "HierarchyLevelUpdateTypeDef",
        "LevelTwo": "HierarchyLevelUpdateTypeDef",
        "LevelThree": "HierarchyLevelUpdateTypeDef",
        "LevelFour": "HierarchyLevelUpdateTypeDef",
        "LevelFive": "HierarchyLevelUpdateTypeDef",
    },
    total=False,
)

HistoricalMetricDataTypeDef = TypedDict(
    "HistoricalMetricDataTypeDef",
    {
        "Metric": "HistoricalMetricTypeDef",
        "Value": float,
    },
    total=False,
)

HistoricalMetricResultTypeDef = TypedDict(
    "HistoricalMetricResultTypeDef",
    {
        "Dimensions": "DimensionsTypeDef",
        "Collections": List["HistoricalMetricDataTypeDef"],
    },
    total=False,
)

HistoricalMetricTypeDef = TypedDict(
    "HistoricalMetricTypeDef",
    {
        "Name": HistoricalMetricNameType,
        "Threshold": "ThresholdTypeDef",
        "Statistic": StatisticType,
        "Unit": UnitType,
    },
    total=False,
)

HoursOfOperationConfigTypeDef = TypedDict(
    "HoursOfOperationConfigTypeDef",
    {
        "Day": HoursOfOperationDaysType,
        "StartTime": "HoursOfOperationTimeSliceTypeDef",
        "EndTime": "HoursOfOperationTimeSliceTypeDef",
    },
    total=False,
)

HoursOfOperationSummaryTypeDef = TypedDict(
    "HoursOfOperationSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

HoursOfOperationTimeSliceTypeDef = TypedDict(
    "HoursOfOperationTimeSliceTypeDef",
    {
        "Hours": int,
        "Minutes": int,
    },
    total=False,
)

HoursOfOperationTypeDef = TypedDict(
    "HoursOfOperationTypeDef",
    {
        "HoursOfOperationId": str,
        "HoursOfOperationArn": str,
        "Name": str,
        "Description": str,
        "TimeZone": str,
        "Config": List["HoursOfOperationConfigTypeDef"],
        "Tags": Dict[str, str],
    },
    total=False,
)

InstanceStatusReasonTypeDef = TypedDict(
    "InstanceStatusReasonTypeDef",
    {
        "Message": str,
    },
    total=False,
)

_RequiredInstanceStorageConfigTypeDef = TypedDict(
    "_RequiredInstanceStorageConfigTypeDef",
    {
        "StorageType": StorageTypeType,
    },
)
_OptionalInstanceStorageConfigTypeDef = TypedDict(
    "_OptionalInstanceStorageConfigTypeDef",
    {
        "AssociationId": str,
        "S3Config": "S3ConfigTypeDef",
        "KinesisVideoStreamConfig": "KinesisVideoStreamConfigTypeDef",
        "KinesisStreamConfig": "KinesisStreamConfigTypeDef",
        "KinesisFirehoseConfig": "KinesisFirehoseConfigTypeDef",
    },
    total=False,
)

class InstanceStorageConfigTypeDef(
    _RequiredInstanceStorageConfigTypeDef, _OptionalInstanceStorageConfigTypeDef
):
    pass

InstanceSummaryTypeDef = TypedDict(
    "InstanceSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "IdentityManagementType": DirectoryTypeType,
        "InstanceAlias": str,
        "CreatedTime": datetime,
        "ServiceRole": str,
        "InstanceStatus": InstanceStatusType,
        "InboundCallsEnabled": bool,
        "OutboundCallsEnabled": bool,
    },
    total=False,
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "Id": str,
        "Arn": str,
        "IdentityManagementType": DirectoryTypeType,
        "InstanceAlias": str,
        "CreatedTime": datetime,
        "ServiceRole": str,
        "InstanceStatus": InstanceStatusType,
        "StatusReason": "InstanceStatusReasonTypeDef",
        "InboundCallsEnabled": bool,
        "OutboundCallsEnabled": bool,
    },
    total=False,
)

IntegrationAssociationSummaryTypeDef = TypedDict(
    "IntegrationAssociationSummaryTypeDef",
    {
        "IntegrationAssociationId": str,
        "IntegrationAssociationArn": str,
        "InstanceId": str,
        "IntegrationType": Literal["EVENT"],
        "IntegrationArn": str,
        "SourceApplicationUrl": str,
        "SourceApplicationName": str,
        "SourceType": SourceTypeType,
    },
    total=False,
)

KinesisFirehoseConfigTypeDef = TypedDict(
    "KinesisFirehoseConfigTypeDef",
    {
        "FirehoseArn": str,
    },
)

KinesisStreamConfigTypeDef = TypedDict(
    "KinesisStreamConfigTypeDef",
    {
        "StreamArn": str,
    },
)

KinesisVideoStreamConfigTypeDef = TypedDict(
    "KinesisVideoStreamConfigTypeDef",
    {
        "Prefix": str,
        "RetentionPeriodHours": int,
        "EncryptionConfig": "EncryptionConfigTypeDef",
    },
)

LexBotConfigTypeDef = TypedDict(
    "LexBotConfigTypeDef",
    {
        "LexBot": "LexBotTypeDef",
        "LexV2Bot": "LexV2BotTypeDef",
    },
    total=False,
)

LexBotTypeDef = TypedDict(
    "LexBotTypeDef",
    {
        "Name": str,
        "LexRegion": str,
    },
    total=False,
)

LexV2BotTypeDef = TypedDict(
    "LexV2BotTypeDef",
    {
        "AliasArn": str,
    },
    total=False,
)

_RequiredListApprovedOriginsRequestRequestTypeDef = TypedDict(
    "_RequiredListApprovedOriginsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListApprovedOriginsRequestRequestTypeDef = TypedDict(
    "_OptionalListApprovedOriginsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListApprovedOriginsRequestRequestTypeDef(
    _RequiredListApprovedOriginsRequestRequestTypeDef,
    _OptionalListApprovedOriginsRequestRequestTypeDef,
):
    pass

ListApprovedOriginsResponseTypeDef = TypedDict(
    "ListApprovedOriginsResponseTypeDef",
    {
        "Origins": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBotsRequestRequestTypeDef = TypedDict(
    "_RequiredListBotsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "LexVersion": LexVersionType,
    },
)
_OptionalListBotsRequestRequestTypeDef = TypedDict(
    "_OptionalListBotsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListBotsRequestRequestTypeDef(
    _RequiredListBotsRequestRequestTypeDef, _OptionalListBotsRequestRequestTypeDef
):
    pass

ListBotsResponseTypeDef = TypedDict(
    "ListBotsResponseTypeDef",
    {
        "LexBots": List["LexBotConfigTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListContactFlowsRequestRequestTypeDef = TypedDict(
    "_RequiredListContactFlowsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListContactFlowsRequestRequestTypeDef = TypedDict(
    "_OptionalListContactFlowsRequestRequestTypeDef",
    {
        "ContactFlowTypes": List[ContactFlowTypeType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListContactFlowsRequestRequestTypeDef(
    _RequiredListContactFlowsRequestRequestTypeDef, _OptionalListContactFlowsRequestRequestTypeDef
):
    pass

ListContactFlowsResponseTypeDef = TypedDict(
    "ListContactFlowsResponseTypeDef",
    {
        "ContactFlowSummaryList": List["ContactFlowSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListHoursOfOperationsRequestRequestTypeDef = TypedDict(
    "_RequiredListHoursOfOperationsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListHoursOfOperationsRequestRequestTypeDef = TypedDict(
    "_OptionalListHoursOfOperationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListHoursOfOperationsRequestRequestTypeDef(
    _RequiredListHoursOfOperationsRequestRequestTypeDef,
    _OptionalListHoursOfOperationsRequestRequestTypeDef,
):
    pass

ListHoursOfOperationsResponseTypeDef = TypedDict(
    "ListHoursOfOperationsResponseTypeDef",
    {
        "HoursOfOperationSummaryList": List["HoursOfOperationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInstanceAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredListInstanceAttributesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListInstanceAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalListInstanceAttributesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListInstanceAttributesRequestRequestTypeDef(
    _RequiredListInstanceAttributesRequestRequestTypeDef,
    _OptionalListInstanceAttributesRequestRequestTypeDef,
):
    pass

ListInstanceAttributesResponseTypeDef = TypedDict(
    "ListInstanceAttributesResponseTypeDef",
    {
        "Attributes": List["AttributeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInstanceStorageConfigsRequestRequestTypeDef = TypedDict(
    "_RequiredListInstanceStorageConfigsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ResourceType": InstanceStorageResourceTypeType,
    },
)
_OptionalListInstanceStorageConfigsRequestRequestTypeDef = TypedDict(
    "_OptionalListInstanceStorageConfigsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListInstanceStorageConfigsRequestRequestTypeDef(
    _RequiredListInstanceStorageConfigsRequestRequestTypeDef,
    _OptionalListInstanceStorageConfigsRequestRequestTypeDef,
):
    pass

ListInstanceStorageConfigsResponseTypeDef = TypedDict(
    "ListInstanceStorageConfigsResponseTypeDef",
    {
        "StorageConfigs": List["InstanceStorageConfigTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstancesRequestRequestTypeDef = TypedDict(
    "ListInstancesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListInstancesResponseTypeDef = TypedDict(
    "ListInstancesResponseTypeDef",
    {
        "InstanceSummaryList": List["InstanceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIntegrationAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredListIntegrationAssociationsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListIntegrationAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalListIntegrationAssociationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListIntegrationAssociationsRequestRequestTypeDef(
    _RequiredListIntegrationAssociationsRequestRequestTypeDef,
    _OptionalListIntegrationAssociationsRequestRequestTypeDef,
):
    pass

ListIntegrationAssociationsResponseTypeDef = TypedDict(
    "ListIntegrationAssociationsResponseTypeDef",
    {
        "IntegrationAssociationSummaryList": List["IntegrationAssociationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLambdaFunctionsRequestRequestTypeDef = TypedDict(
    "_RequiredListLambdaFunctionsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListLambdaFunctionsRequestRequestTypeDef = TypedDict(
    "_OptionalListLambdaFunctionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListLambdaFunctionsRequestRequestTypeDef(
    _RequiredListLambdaFunctionsRequestRequestTypeDef,
    _OptionalListLambdaFunctionsRequestRequestTypeDef,
):
    pass

ListLambdaFunctionsResponseTypeDef = TypedDict(
    "ListLambdaFunctionsResponseTypeDef",
    {
        "LambdaFunctions": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLexBotsRequestRequestTypeDef = TypedDict(
    "_RequiredListLexBotsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListLexBotsRequestRequestTypeDef = TypedDict(
    "_OptionalListLexBotsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListLexBotsRequestRequestTypeDef(
    _RequiredListLexBotsRequestRequestTypeDef, _OptionalListLexBotsRequestRequestTypeDef
):
    pass

ListLexBotsResponseTypeDef = TypedDict(
    "ListLexBotsResponseTypeDef",
    {
        "LexBots": List["LexBotTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPhoneNumbersRequestRequestTypeDef = TypedDict(
    "_RequiredListPhoneNumbersRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListPhoneNumbersRequestRequestTypeDef = TypedDict(
    "_OptionalListPhoneNumbersRequestRequestTypeDef",
    {
        "PhoneNumberTypes": List[PhoneNumberTypeType],
        "PhoneNumberCountryCodes": List[PhoneNumberCountryCodeType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListPhoneNumbersRequestRequestTypeDef(
    _RequiredListPhoneNumbersRequestRequestTypeDef, _OptionalListPhoneNumbersRequestRequestTypeDef
):
    pass

ListPhoneNumbersResponseTypeDef = TypedDict(
    "ListPhoneNumbersResponseTypeDef",
    {
        "PhoneNumberSummaryList": List["PhoneNumberSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPromptsRequestRequestTypeDef = TypedDict(
    "_RequiredListPromptsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListPromptsRequestRequestTypeDef = TypedDict(
    "_OptionalListPromptsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListPromptsRequestRequestTypeDef(
    _RequiredListPromptsRequestRequestTypeDef, _OptionalListPromptsRequestRequestTypeDef
):
    pass

ListPromptsResponseTypeDef = TypedDict(
    "ListPromptsResponseTypeDef",
    {
        "PromptSummaryList": List["PromptSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListQueueQuickConnectsRequestRequestTypeDef = TypedDict(
    "_RequiredListQueueQuickConnectsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
    },
)
_OptionalListQueueQuickConnectsRequestRequestTypeDef = TypedDict(
    "_OptionalListQueueQuickConnectsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListQueueQuickConnectsRequestRequestTypeDef(
    _RequiredListQueueQuickConnectsRequestRequestTypeDef,
    _OptionalListQueueQuickConnectsRequestRequestTypeDef,
):
    pass

ListQueueQuickConnectsResponseTypeDef = TypedDict(
    "ListQueueQuickConnectsResponseTypeDef",
    {
        "NextToken": str,
        "QuickConnectSummaryList": List["QuickConnectSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListQueuesRequestRequestTypeDef = TypedDict(
    "_RequiredListQueuesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListQueuesRequestRequestTypeDef = TypedDict(
    "_OptionalListQueuesRequestRequestTypeDef",
    {
        "QueueTypes": List[QueueTypeType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListQueuesRequestRequestTypeDef(
    _RequiredListQueuesRequestRequestTypeDef, _OptionalListQueuesRequestRequestTypeDef
):
    pass

ListQueuesResponseTypeDef = TypedDict(
    "ListQueuesResponseTypeDef",
    {
        "QueueSummaryList": List["QueueSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListQuickConnectsRequestRequestTypeDef = TypedDict(
    "_RequiredListQuickConnectsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListQuickConnectsRequestRequestTypeDef = TypedDict(
    "_OptionalListQuickConnectsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "QuickConnectTypes": List[QuickConnectTypeType],
    },
    total=False,
)

class ListQuickConnectsRequestRequestTypeDef(
    _RequiredListQuickConnectsRequestRequestTypeDef, _OptionalListQuickConnectsRequestRequestTypeDef
):
    pass

ListQuickConnectsResponseTypeDef = TypedDict(
    "ListQuickConnectsResponseTypeDef",
    {
        "QuickConnectSummaryList": List["QuickConnectSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRoutingProfileQueuesRequestRequestTypeDef = TypedDict(
    "_RequiredListRoutingProfileQueuesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
    },
)
_OptionalListRoutingProfileQueuesRequestRequestTypeDef = TypedDict(
    "_OptionalListRoutingProfileQueuesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListRoutingProfileQueuesRequestRequestTypeDef(
    _RequiredListRoutingProfileQueuesRequestRequestTypeDef,
    _OptionalListRoutingProfileQueuesRequestRequestTypeDef,
):
    pass

ListRoutingProfileQueuesResponseTypeDef = TypedDict(
    "ListRoutingProfileQueuesResponseTypeDef",
    {
        "NextToken": str,
        "RoutingProfileQueueConfigSummaryList": List["RoutingProfileQueueConfigSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRoutingProfilesRequestRequestTypeDef = TypedDict(
    "_RequiredListRoutingProfilesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListRoutingProfilesRequestRequestTypeDef = TypedDict(
    "_OptionalListRoutingProfilesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListRoutingProfilesRequestRequestTypeDef(
    _RequiredListRoutingProfilesRequestRequestTypeDef,
    _OptionalListRoutingProfilesRequestRequestTypeDef,
):
    pass

ListRoutingProfilesResponseTypeDef = TypedDict(
    "ListRoutingProfilesResponseTypeDef",
    {
        "RoutingProfileSummaryList": List["RoutingProfileSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSecurityKeysRequestRequestTypeDef = TypedDict(
    "_RequiredListSecurityKeysRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListSecurityKeysRequestRequestTypeDef = TypedDict(
    "_OptionalListSecurityKeysRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListSecurityKeysRequestRequestTypeDef(
    _RequiredListSecurityKeysRequestRequestTypeDef, _OptionalListSecurityKeysRequestRequestTypeDef
):
    pass

ListSecurityKeysResponseTypeDef = TypedDict(
    "ListSecurityKeysResponseTypeDef",
    {
        "SecurityKeys": List["SecurityKeyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSecurityProfilesRequestRequestTypeDef = TypedDict(
    "_RequiredListSecurityProfilesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListSecurityProfilesRequestRequestTypeDef = TypedDict(
    "_OptionalListSecurityProfilesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListSecurityProfilesRequestRequestTypeDef(
    _RequiredListSecurityProfilesRequestRequestTypeDef,
    _OptionalListSecurityProfilesRequestRequestTypeDef,
):
    pass

ListSecurityProfilesResponseTypeDef = TypedDict(
    "ListSecurityProfilesResponseTypeDef",
    {
        "SecurityProfileSummaryList": List["SecurityProfileSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUseCasesRequestRequestTypeDef = TypedDict(
    "_RequiredListUseCasesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationAssociationId": str,
    },
)
_OptionalListUseCasesRequestRequestTypeDef = TypedDict(
    "_OptionalListUseCasesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListUseCasesRequestRequestTypeDef(
    _RequiredListUseCasesRequestRequestTypeDef, _OptionalListUseCasesRequestRequestTypeDef
):
    pass

ListUseCasesResponseTypeDef = TypedDict(
    "ListUseCasesResponseTypeDef",
    {
        "UseCaseSummaryList": List["UseCaseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUserHierarchyGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListUserHierarchyGroupsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListUserHierarchyGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListUserHierarchyGroupsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListUserHierarchyGroupsRequestRequestTypeDef(
    _RequiredListUserHierarchyGroupsRequestRequestTypeDef,
    _OptionalListUserHierarchyGroupsRequestRequestTypeDef,
):
    pass

ListUserHierarchyGroupsResponseTypeDef = TypedDict(
    "ListUserHierarchyGroupsResponseTypeDef",
    {
        "UserHierarchyGroupSummaryList": List["HierarchyGroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsersRequestRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListUsersRequestRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListUsersRequestRequestTypeDef(
    _RequiredListUsersRequestRequestTypeDef, _OptionalListUsersRequestRequestTypeDef
):
    pass

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "UserSummaryList": List["UserSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MediaConcurrencyTypeDef = TypedDict(
    "MediaConcurrencyTypeDef",
    {
        "Channel": ChannelType,
        "Concurrency": int,
    },
)

OutboundCallerConfigTypeDef = TypedDict(
    "OutboundCallerConfigTypeDef",
    {
        "OutboundCallerIdName": str,
        "OutboundCallerIdNumberId": str,
        "OutboundFlowId": str,
    },
    total=False,
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

ParticipantDetailsTypeDef = TypedDict(
    "ParticipantDetailsTypeDef",
    {
        "DisplayName": str,
    },
)

PhoneNumberQuickConnectConfigTypeDef = TypedDict(
    "PhoneNumberQuickConnectConfigTypeDef",
    {
        "PhoneNumber": str,
    },
)

PhoneNumberSummaryTypeDef = TypedDict(
    "PhoneNumberSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "PhoneNumber": str,
        "PhoneNumberType": PhoneNumberTypeType,
        "PhoneNumberCountryCode": PhoneNumberCountryCodeType,
    },
    total=False,
)

PromptSummaryTypeDef = TypedDict(
    "PromptSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

QueueQuickConnectConfigTypeDef = TypedDict(
    "QueueQuickConnectConfigTypeDef",
    {
        "QueueId": str,
        "ContactFlowId": str,
    },
)

QueueReferenceTypeDef = TypedDict(
    "QueueReferenceTypeDef",
    {
        "Id": str,
        "Arn": str,
    },
    total=False,
)

QueueSummaryTypeDef = TypedDict(
    "QueueSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "QueueType": QueueTypeType,
    },
    total=False,
)

QueueTypeDef = TypedDict(
    "QueueTypeDef",
    {
        "Name": str,
        "QueueArn": str,
        "QueueId": str,
        "Description": str,
        "OutboundCallerConfig": "OutboundCallerConfigTypeDef",
        "HoursOfOperationId": str,
        "MaxContacts": int,
        "Status": QueueStatusType,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredQuickConnectConfigTypeDef = TypedDict(
    "_RequiredQuickConnectConfigTypeDef",
    {
        "QuickConnectType": QuickConnectTypeType,
    },
)
_OptionalQuickConnectConfigTypeDef = TypedDict(
    "_OptionalQuickConnectConfigTypeDef",
    {
        "UserConfig": "UserQuickConnectConfigTypeDef",
        "QueueConfig": "QueueQuickConnectConfigTypeDef",
        "PhoneConfig": "PhoneNumberQuickConnectConfigTypeDef",
    },
    total=False,
)

class QuickConnectConfigTypeDef(
    _RequiredQuickConnectConfigTypeDef, _OptionalQuickConnectConfigTypeDef
):
    pass

QuickConnectSummaryTypeDef = TypedDict(
    "QuickConnectSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "QuickConnectType": QuickConnectTypeType,
    },
    total=False,
)

QuickConnectTypeDef = TypedDict(
    "QuickConnectTypeDef",
    {
        "QuickConnectARN": str,
        "QuickConnectId": str,
        "Name": str,
        "Description": str,
        "QuickConnectConfig": "QuickConnectConfigTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

ReferenceTypeDef = TypedDict(
    "ReferenceTypeDef",
    {
        "Value": str,
        "Type": Literal["URL"],
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

ResumeContactRecordingRequestRequestTypeDef = TypedDict(
    "ResumeContactRecordingRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "InitialContactId": str,
    },
)

RoutingProfileQueueConfigSummaryTypeDef = TypedDict(
    "RoutingProfileQueueConfigSummaryTypeDef",
    {
        "QueueId": str,
        "QueueArn": str,
        "QueueName": str,
        "Priority": int,
        "Delay": int,
        "Channel": ChannelType,
    },
)

RoutingProfileQueueConfigTypeDef = TypedDict(
    "RoutingProfileQueueConfigTypeDef",
    {
        "QueueReference": "RoutingProfileQueueReferenceTypeDef",
        "Priority": int,
        "Delay": int,
    },
)

RoutingProfileQueueReferenceTypeDef = TypedDict(
    "RoutingProfileQueueReferenceTypeDef",
    {
        "QueueId": str,
        "Channel": ChannelType,
    },
)

RoutingProfileSummaryTypeDef = TypedDict(
    "RoutingProfileSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

RoutingProfileTypeDef = TypedDict(
    "RoutingProfileTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "RoutingProfileArn": str,
        "RoutingProfileId": str,
        "Description": str,
        "MediaConcurrencies": List["MediaConcurrencyTypeDef"],
        "DefaultOutboundQueueId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredS3ConfigTypeDef = TypedDict(
    "_RequiredS3ConfigTypeDef",
    {
        "BucketName": str,
        "BucketPrefix": str,
    },
)
_OptionalS3ConfigTypeDef = TypedDict(
    "_OptionalS3ConfigTypeDef",
    {
        "EncryptionConfig": "EncryptionConfigTypeDef",
    },
    total=False,
)

class S3ConfigTypeDef(_RequiredS3ConfigTypeDef, _OptionalS3ConfigTypeDef):
    pass

SecurityKeyTypeDef = TypedDict(
    "SecurityKeyTypeDef",
    {
        "AssociationId": str,
        "Key": str,
        "CreationTime": datetime,
    },
    total=False,
)

SecurityProfileSummaryTypeDef = TypedDict(
    "SecurityProfileSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

_RequiredStartChatContactRequestRequestTypeDef = TypedDict(
    "_RequiredStartChatContactRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
        "ParticipantDetails": "ParticipantDetailsTypeDef",
    },
)
_OptionalStartChatContactRequestRequestTypeDef = TypedDict(
    "_OptionalStartChatContactRequestRequestTypeDef",
    {
        "Attributes": Dict[str, str],
        "InitialMessage": "ChatMessageTypeDef",
        "ClientToken": str,
    },
    total=False,
)

class StartChatContactRequestRequestTypeDef(
    _RequiredStartChatContactRequestRequestTypeDef, _OptionalStartChatContactRequestRequestTypeDef
):
    pass

StartChatContactResponseTypeDef = TypedDict(
    "StartChatContactResponseTypeDef",
    {
        "ContactId": str,
        "ParticipantId": str,
        "ParticipantToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartContactRecordingRequestRequestTypeDef = TypedDict(
    "StartContactRecordingRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "InitialContactId": str,
        "VoiceRecordingConfiguration": "VoiceRecordingConfigurationTypeDef",
    },
)

_RequiredStartOutboundVoiceContactRequestRequestTypeDef = TypedDict(
    "_RequiredStartOutboundVoiceContactRequestRequestTypeDef",
    {
        "DestinationPhoneNumber": str,
        "ContactFlowId": str,
        "InstanceId": str,
    },
)
_OptionalStartOutboundVoiceContactRequestRequestTypeDef = TypedDict(
    "_OptionalStartOutboundVoiceContactRequestRequestTypeDef",
    {
        "ClientToken": str,
        "SourcePhoneNumber": str,
        "QueueId": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)

class StartOutboundVoiceContactRequestRequestTypeDef(
    _RequiredStartOutboundVoiceContactRequestRequestTypeDef,
    _OptionalStartOutboundVoiceContactRequestRequestTypeDef,
):
    pass

StartOutboundVoiceContactResponseTypeDef = TypedDict(
    "StartOutboundVoiceContactResponseTypeDef",
    {
        "ContactId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartTaskContactRequestRequestTypeDef = TypedDict(
    "_RequiredStartTaskContactRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
        "Name": str,
    },
)
_OptionalStartTaskContactRequestRequestTypeDef = TypedDict(
    "_OptionalStartTaskContactRequestRequestTypeDef",
    {
        "PreviousContactId": str,
        "Attributes": Dict[str, str],
        "References": Dict[str, "ReferenceTypeDef"],
        "Description": str,
        "ClientToken": str,
    },
    total=False,
)

class StartTaskContactRequestRequestTypeDef(
    _RequiredStartTaskContactRequestRequestTypeDef, _OptionalStartTaskContactRequestRequestTypeDef
):
    pass

StartTaskContactResponseTypeDef = TypedDict(
    "StartTaskContactResponseTypeDef",
    {
        "ContactId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopContactRecordingRequestRequestTypeDef = TypedDict(
    "StopContactRecordingRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "InitialContactId": str,
    },
)

StopContactRequestRequestTypeDef = TypedDict(
    "StopContactRequestRequestTypeDef",
    {
        "ContactId": str,
        "InstanceId": str,
    },
)

SuspendContactRecordingRequestRequestTypeDef = TypedDict(
    "SuspendContactRecordingRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "InitialContactId": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

ThresholdTypeDef = TypedDict(
    "ThresholdTypeDef",
    {
        "Comparison": Literal["LT"],
        "ThresholdValue": float,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateContactAttributesRequestRequestTypeDef = TypedDict(
    "UpdateContactAttributesRequestRequestTypeDef",
    {
        "InitialContactId": str,
        "InstanceId": str,
        "Attributes": Dict[str, str],
    },
)

UpdateContactFlowContentRequestRequestTypeDef = TypedDict(
    "UpdateContactFlowContentRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
        "Content": str,
    },
)

_RequiredUpdateContactFlowNameRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateContactFlowNameRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
    },
)
_OptionalUpdateContactFlowNameRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateContactFlowNameRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)

class UpdateContactFlowNameRequestRequestTypeDef(
    _RequiredUpdateContactFlowNameRequestRequestTypeDef,
    _OptionalUpdateContactFlowNameRequestRequestTypeDef,
):
    pass

UpdateInstanceAttributeRequestRequestTypeDef = TypedDict(
    "UpdateInstanceAttributeRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AttributeType": InstanceAttributeTypeType,
        "Value": str,
    },
)

UpdateInstanceStorageConfigRequestRequestTypeDef = TypedDict(
    "UpdateInstanceStorageConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AssociationId": str,
        "ResourceType": InstanceStorageResourceTypeType,
        "StorageConfig": "InstanceStorageConfigTypeDef",
    },
)

UpdateQueueHoursOfOperationRequestRequestTypeDef = TypedDict(
    "UpdateQueueHoursOfOperationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "HoursOfOperationId": str,
    },
)

_RequiredUpdateQueueMaxContactsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateQueueMaxContactsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
    },
)
_OptionalUpdateQueueMaxContactsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateQueueMaxContactsRequestRequestTypeDef",
    {
        "MaxContacts": int,
    },
    total=False,
)

class UpdateQueueMaxContactsRequestRequestTypeDef(
    _RequiredUpdateQueueMaxContactsRequestRequestTypeDef,
    _OptionalUpdateQueueMaxContactsRequestRequestTypeDef,
):
    pass

_RequiredUpdateQueueNameRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateQueueNameRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
    },
)
_OptionalUpdateQueueNameRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateQueueNameRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)

class UpdateQueueNameRequestRequestTypeDef(
    _RequiredUpdateQueueNameRequestRequestTypeDef, _OptionalUpdateQueueNameRequestRequestTypeDef
):
    pass

UpdateQueueOutboundCallerConfigRequestRequestTypeDef = TypedDict(
    "UpdateQueueOutboundCallerConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "OutboundCallerConfig": "OutboundCallerConfigTypeDef",
    },
)

UpdateQueueStatusRequestRequestTypeDef = TypedDict(
    "UpdateQueueStatusRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "Status": QueueStatusType,
    },
)

UpdateQuickConnectConfigRequestRequestTypeDef = TypedDict(
    "UpdateQuickConnectConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QuickConnectId": str,
        "QuickConnectConfig": "QuickConnectConfigTypeDef",
    },
)

_RequiredUpdateQuickConnectNameRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateQuickConnectNameRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QuickConnectId": str,
    },
)
_OptionalUpdateQuickConnectNameRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateQuickConnectNameRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)

class UpdateQuickConnectNameRequestRequestTypeDef(
    _RequiredUpdateQuickConnectNameRequestRequestTypeDef,
    _OptionalUpdateQuickConnectNameRequestRequestTypeDef,
):
    pass

UpdateRoutingProfileConcurrencyRequestRequestTypeDef = TypedDict(
    "UpdateRoutingProfileConcurrencyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "MediaConcurrencies": List["MediaConcurrencyTypeDef"],
    },
)

UpdateRoutingProfileDefaultOutboundQueueRequestRequestTypeDef = TypedDict(
    "UpdateRoutingProfileDefaultOutboundQueueRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "DefaultOutboundQueueId": str,
    },
)

_RequiredUpdateRoutingProfileNameRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRoutingProfileNameRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
    },
)
_OptionalUpdateRoutingProfileNameRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRoutingProfileNameRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)

class UpdateRoutingProfileNameRequestRequestTypeDef(
    _RequiredUpdateRoutingProfileNameRequestRequestTypeDef,
    _OptionalUpdateRoutingProfileNameRequestRequestTypeDef,
):
    pass

UpdateRoutingProfileQueuesRequestRequestTypeDef = TypedDict(
    "UpdateRoutingProfileQueuesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "QueueConfigs": List["RoutingProfileQueueConfigTypeDef"],
    },
)

UpdateUserHierarchyGroupNameRequestRequestTypeDef = TypedDict(
    "UpdateUserHierarchyGroupNameRequestRequestTypeDef",
    {
        "Name": str,
        "HierarchyGroupId": str,
        "InstanceId": str,
    },
)

_RequiredUpdateUserHierarchyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserHierarchyRequestRequestTypeDef",
    {
        "UserId": str,
        "InstanceId": str,
    },
)
_OptionalUpdateUserHierarchyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserHierarchyRequestRequestTypeDef",
    {
        "HierarchyGroupId": str,
    },
    total=False,
)

class UpdateUserHierarchyRequestRequestTypeDef(
    _RequiredUpdateUserHierarchyRequestRequestTypeDef,
    _OptionalUpdateUserHierarchyRequestRequestTypeDef,
):
    pass

UpdateUserHierarchyStructureRequestRequestTypeDef = TypedDict(
    "UpdateUserHierarchyStructureRequestRequestTypeDef",
    {
        "HierarchyStructure": "HierarchyStructureUpdateTypeDef",
        "InstanceId": str,
    },
)

UpdateUserIdentityInfoRequestRequestTypeDef = TypedDict(
    "UpdateUserIdentityInfoRequestRequestTypeDef",
    {
        "IdentityInfo": "UserIdentityInfoTypeDef",
        "UserId": str,
        "InstanceId": str,
    },
)

UpdateUserPhoneConfigRequestRequestTypeDef = TypedDict(
    "UpdateUserPhoneConfigRequestRequestTypeDef",
    {
        "PhoneConfig": "UserPhoneConfigTypeDef",
        "UserId": str,
        "InstanceId": str,
    },
)

UpdateUserRoutingProfileRequestRequestTypeDef = TypedDict(
    "UpdateUserRoutingProfileRequestRequestTypeDef",
    {
        "RoutingProfileId": str,
        "UserId": str,
        "InstanceId": str,
    },
)

UpdateUserSecurityProfilesRequestRequestTypeDef = TypedDict(
    "UpdateUserSecurityProfilesRequestRequestTypeDef",
    {
        "SecurityProfileIds": List[str],
        "UserId": str,
        "InstanceId": str,
    },
)

UseCaseTypeDef = TypedDict(
    "UseCaseTypeDef",
    {
        "UseCaseId": str,
        "UseCaseArn": str,
        "UseCaseType": Literal["RULES_EVALUATION"],
    },
    total=False,
)

UserIdentityInfoTypeDef = TypedDict(
    "UserIdentityInfoTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "Email": str,
    },
    total=False,
)

_RequiredUserPhoneConfigTypeDef = TypedDict(
    "_RequiredUserPhoneConfigTypeDef",
    {
        "PhoneType": PhoneTypeType,
    },
)
_OptionalUserPhoneConfigTypeDef = TypedDict(
    "_OptionalUserPhoneConfigTypeDef",
    {
        "AutoAccept": bool,
        "AfterContactWorkTimeLimit": int,
        "DeskPhoneNumber": str,
    },
    total=False,
)

class UserPhoneConfigTypeDef(_RequiredUserPhoneConfigTypeDef, _OptionalUserPhoneConfigTypeDef):
    pass

UserQuickConnectConfigTypeDef = TypedDict(
    "UserQuickConnectConfigTypeDef",
    {
        "UserId": str,
        "ContactFlowId": str,
    },
)

UserSummaryTypeDef = TypedDict(
    "UserSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Username": str,
    },
    total=False,
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

VoiceRecordingConfigurationTypeDef = TypedDict(
    "VoiceRecordingConfigurationTypeDef",
    {
        "VoiceRecordingTrack": VoiceRecordingTrackType,
    },
    total=False,
)
