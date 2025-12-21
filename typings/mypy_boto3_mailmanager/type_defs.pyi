"""
Type annotations for mailmanager service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_mailmanager.type_defs import AddHeaderActionTypeDef

    data: AddHeaderActionTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    AcceptActionType,
    ActionFailurePolicyType,
    ArchiveBooleanOperatorType,
    ArchiveStateType,
    ArchiveStringEmailAttributeType,
    ExportStateType,
    ImportDataTypeType,
    ImportJobStatusType,
    IngressBooleanOperatorType,
    IngressIpOperatorType,
    IngressPointStatusToUpdateType,
    IngressPointStatusType,
    IngressPointTypeType,
    IngressStringOperatorType,
    IngressTlsProtocolAttributeType,
    IngressTlsProtocolOperatorType,
    IpTypeType,
    MailFromType,
    RetentionPeriodType,
    RuleAddressListEmailAttributeType,
    RuleBooleanEmailAttributeType,
    RuleBooleanOperatorType,
    RuleDmarcOperatorType,
    RuleDmarcPolicyType,
    RuleIpOperatorType,
    RuleNumberOperatorType,
    RuleStringEmailAttributeType,
    RuleStringOperatorType,
    RuleVerdictAttributeType,
    RuleVerdictOperatorType,
    RuleVerdictType,
    SearchStateType,
    SnsNotificationEncodingType,
    SnsNotificationPayloadTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AddHeaderActionTypeDef",
    "AddonInstanceTypeDef",
    "AddonSubscriptionTypeDef",
    "AddressFilterTypeDef",
    "AddressListTypeDef",
    "AnalysisTypeDef",
    "ArchiveActionTypeDef",
    "ArchiveBooleanExpressionTypeDef",
    "ArchiveBooleanToEvaluateTypeDef",
    "ArchiveFilterConditionOutputTypeDef",
    "ArchiveFilterConditionTypeDef",
    "ArchiveFiltersOutputTypeDef",
    "ArchiveFiltersTypeDef",
    "ArchiveFiltersUnionTypeDef",
    "ArchiveRetentionTypeDef",
    "ArchiveStringExpressionOutputTypeDef",
    "ArchiveStringExpressionTypeDef",
    "ArchiveStringToEvaluateTypeDef",
    "ArchiveTypeDef",
    "CreateAddonInstanceRequestTypeDef",
    "CreateAddonInstanceResponseTypeDef",
    "CreateAddonSubscriptionRequestTypeDef",
    "CreateAddonSubscriptionResponseTypeDef",
    "CreateAddressListImportJobRequestTypeDef",
    "CreateAddressListImportJobResponseTypeDef",
    "CreateAddressListRequestTypeDef",
    "CreateAddressListResponseTypeDef",
    "CreateArchiveRequestTypeDef",
    "CreateArchiveResponseTypeDef",
    "CreateIngressPointRequestTypeDef",
    "CreateIngressPointResponseTypeDef",
    "CreateRelayRequestTypeDef",
    "CreateRelayResponseTypeDef",
    "CreateRuleSetRequestTypeDef",
    "CreateRuleSetResponseTypeDef",
    "CreateTrafficPolicyRequestTypeDef",
    "CreateTrafficPolicyResponseTypeDef",
    "DeleteAddonInstanceRequestTypeDef",
    "DeleteAddonSubscriptionRequestTypeDef",
    "DeleteAddressListRequestTypeDef",
    "DeleteArchiveRequestTypeDef",
    "DeleteIngressPointRequestTypeDef",
    "DeleteRelayRequestTypeDef",
    "DeleteRuleSetRequestTypeDef",
    "DeleteTrafficPolicyRequestTypeDef",
    "DeliverToMailboxActionTypeDef",
    "DeliverToQBusinessActionTypeDef",
    "DeregisterMemberFromAddressListRequestTypeDef",
    "EnvelopeTypeDef",
    "ExportDestinationConfigurationTypeDef",
    "ExportStatusTypeDef",
    "ExportSummaryTypeDef",
    "GetAddonInstanceRequestTypeDef",
    "GetAddonInstanceResponseTypeDef",
    "GetAddonSubscriptionRequestTypeDef",
    "GetAddonSubscriptionResponseTypeDef",
    "GetAddressListImportJobRequestTypeDef",
    "GetAddressListImportJobResponseTypeDef",
    "GetAddressListRequestTypeDef",
    "GetAddressListResponseTypeDef",
    "GetArchiveExportRequestTypeDef",
    "GetArchiveExportResponseTypeDef",
    "GetArchiveMessageContentRequestTypeDef",
    "GetArchiveMessageContentResponseTypeDef",
    "GetArchiveMessageRequestTypeDef",
    "GetArchiveMessageResponseTypeDef",
    "GetArchiveRequestTypeDef",
    "GetArchiveResponseTypeDef",
    "GetArchiveSearchRequestTypeDef",
    "GetArchiveSearchResponseTypeDef",
    "GetArchiveSearchResultsRequestTypeDef",
    "GetArchiveSearchResultsResponseTypeDef",
    "GetIngressPointRequestTypeDef",
    "GetIngressPointResponseTypeDef",
    "GetMemberOfAddressListRequestTypeDef",
    "GetMemberOfAddressListResponseTypeDef",
    "GetRelayRequestTypeDef",
    "GetRelayResponseTypeDef",
    "GetRuleSetRequestTypeDef",
    "GetRuleSetResponseTypeDef",
    "GetTrafficPolicyRequestTypeDef",
    "GetTrafficPolicyResponseTypeDef",
    "ImportDataFormatTypeDef",
    "ImportJobTypeDef",
    "IngressAnalysisTypeDef",
    "IngressBooleanExpressionOutputTypeDef",
    "IngressBooleanExpressionTypeDef",
    "IngressBooleanExpressionUnionTypeDef",
    "IngressBooleanToEvaluateOutputTypeDef",
    "IngressBooleanToEvaluateTypeDef",
    "IngressBooleanToEvaluateUnionTypeDef",
    "IngressIpToEvaluateTypeDef",
    "IngressIpv4ExpressionOutputTypeDef",
    "IngressIpv4ExpressionTypeDef",
    "IngressIpv4ExpressionUnionTypeDef",
    "IngressIpv6ExpressionOutputTypeDef",
    "IngressIpv6ExpressionTypeDef",
    "IngressIpv6ExpressionUnionTypeDef",
    "IngressIpv6ToEvaluateTypeDef",
    "IngressIsInAddressListOutputTypeDef",
    "IngressIsInAddressListTypeDef",
    "IngressIsInAddressListUnionTypeDef",
    "IngressPointAuthConfigurationTypeDef",
    "IngressPointConfigurationTypeDef",
    "IngressPointPasswordConfigurationTypeDef",
    "IngressPointTypeDef",
    "IngressStringExpressionOutputTypeDef",
    "IngressStringExpressionTypeDef",
    "IngressStringExpressionUnionTypeDef",
    "IngressStringToEvaluateTypeDef",
    "IngressTlsProtocolExpressionTypeDef",
    "IngressTlsProtocolToEvaluateTypeDef",
    "ListAddonInstancesRequestPaginateTypeDef",
    "ListAddonInstancesRequestTypeDef",
    "ListAddonInstancesResponseTypeDef",
    "ListAddonSubscriptionsRequestPaginateTypeDef",
    "ListAddonSubscriptionsRequestTypeDef",
    "ListAddonSubscriptionsResponseTypeDef",
    "ListAddressListImportJobsRequestPaginateTypeDef",
    "ListAddressListImportJobsRequestTypeDef",
    "ListAddressListImportJobsResponseTypeDef",
    "ListAddressListsRequestPaginateTypeDef",
    "ListAddressListsRequestTypeDef",
    "ListAddressListsResponseTypeDef",
    "ListArchiveExportsRequestPaginateTypeDef",
    "ListArchiveExportsRequestTypeDef",
    "ListArchiveExportsResponseTypeDef",
    "ListArchiveSearchesRequestPaginateTypeDef",
    "ListArchiveSearchesRequestTypeDef",
    "ListArchiveSearchesResponseTypeDef",
    "ListArchivesRequestPaginateTypeDef",
    "ListArchivesRequestTypeDef",
    "ListArchivesResponseTypeDef",
    "ListIngressPointsRequestPaginateTypeDef",
    "ListIngressPointsRequestTypeDef",
    "ListIngressPointsResponseTypeDef",
    "ListMembersOfAddressListRequestPaginateTypeDef",
    "ListMembersOfAddressListRequestTypeDef",
    "ListMembersOfAddressListResponseTypeDef",
    "ListRelaysRequestPaginateTypeDef",
    "ListRelaysRequestTypeDef",
    "ListRelaysResponseTypeDef",
    "ListRuleSetsRequestPaginateTypeDef",
    "ListRuleSetsRequestTypeDef",
    "ListRuleSetsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTrafficPoliciesRequestPaginateTypeDef",
    "ListTrafficPoliciesRequestTypeDef",
    "ListTrafficPoliciesResponseTypeDef",
    "MessageBodyTypeDef",
    "MetadataTypeDef",
    "NetworkConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PolicyConditionOutputTypeDef",
    "PolicyConditionTypeDef",
    "PolicyConditionUnionTypeDef",
    "PolicyStatementOutputTypeDef",
    "PolicyStatementTypeDef",
    "PolicyStatementUnionTypeDef",
    "PrivateNetworkConfigurationTypeDef",
    "PublicNetworkConfigurationTypeDef",
    "RegisterMemberToAddressListRequestTypeDef",
    "RelayActionTypeDef",
    "RelayAuthenticationOutputTypeDef",
    "RelayAuthenticationTypeDef",
    "RelayAuthenticationUnionTypeDef",
    "RelayTypeDef",
    "ReplaceRecipientActionOutputTypeDef",
    "ReplaceRecipientActionTypeDef",
    "ReplaceRecipientActionUnionTypeDef",
    "ResponseMetadataTypeDef",
    "RowTypeDef",
    "RuleActionOutputTypeDef",
    "RuleActionTypeDef",
    "RuleActionUnionTypeDef",
    "RuleBooleanExpressionOutputTypeDef",
    "RuleBooleanExpressionTypeDef",
    "RuleBooleanExpressionUnionTypeDef",
    "RuleBooleanToEvaluateOutputTypeDef",
    "RuleBooleanToEvaluateTypeDef",
    "RuleBooleanToEvaluateUnionTypeDef",
    "RuleConditionOutputTypeDef",
    "RuleConditionTypeDef",
    "RuleConditionUnionTypeDef",
    "RuleDmarcExpressionOutputTypeDef",
    "RuleDmarcExpressionTypeDef",
    "RuleDmarcExpressionUnionTypeDef",
    "RuleIpExpressionOutputTypeDef",
    "RuleIpExpressionTypeDef",
    "RuleIpExpressionUnionTypeDef",
    "RuleIpToEvaluateTypeDef",
    "RuleIsInAddressListOutputTypeDef",
    "RuleIsInAddressListTypeDef",
    "RuleIsInAddressListUnionTypeDef",
    "RuleNumberExpressionTypeDef",
    "RuleNumberToEvaluateTypeDef",
    "RuleOutputTypeDef",
    "RuleSetTypeDef",
    "RuleStringExpressionOutputTypeDef",
    "RuleStringExpressionTypeDef",
    "RuleStringExpressionUnionTypeDef",
    "RuleStringToEvaluateTypeDef",
    "RuleTypeDef",
    "RuleUnionTypeDef",
    "RuleVerdictExpressionOutputTypeDef",
    "RuleVerdictExpressionTypeDef",
    "RuleVerdictExpressionUnionTypeDef",
    "RuleVerdictToEvaluateTypeDef",
    "S3ActionTypeDef",
    "S3ExportDestinationConfigurationTypeDef",
    "SavedAddressTypeDef",
    "SearchStatusTypeDef",
    "SearchSummaryTypeDef",
    "SendActionTypeDef",
    "SnsActionTypeDef",
    "StartAddressListImportJobRequestTypeDef",
    "StartArchiveExportRequestTypeDef",
    "StartArchiveExportResponseTypeDef",
    "StartArchiveSearchRequestTypeDef",
    "StartArchiveSearchResponseTypeDef",
    "StopAddressListImportJobRequestTypeDef",
    "StopArchiveExportRequestTypeDef",
    "StopArchiveSearchRequestTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "TrafficPolicyTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateArchiveRequestTypeDef",
    "UpdateIngressPointRequestTypeDef",
    "UpdateRelayRequestTypeDef",
    "UpdateRuleSetRequestTypeDef",
    "UpdateTrafficPolicyRequestTypeDef",
)

class AddHeaderActionTypeDef(TypedDict):
    HeaderName: str
    HeaderValue: str

class AddonInstanceTypeDef(TypedDict):
    AddonInstanceId: NotRequired[str]
    AddonSubscriptionId: NotRequired[str]
    AddonName: NotRequired[str]
    AddonInstanceArn: NotRequired[str]
    CreatedTimestamp: NotRequired[datetime]

class AddonSubscriptionTypeDef(TypedDict):
    AddonSubscriptionId: NotRequired[str]
    AddonName: NotRequired[str]
    AddonSubscriptionArn: NotRequired[str]
    CreatedTimestamp: NotRequired[datetime]

class AddressFilterTypeDef(TypedDict):
    AddressPrefix: NotRequired[str]

class AddressListTypeDef(TypedDict):
    AddressListId: str
    AddressListArn: str
    AddressListName: str
    CreatedTimestamp: datetime
    LastUpdatedTimestamp: datetime

class AnalysisTypeDef(TypedDict):
    Analyzer: str
    ResultField: str

class ArchiveActionTypeDef(TypedDict):
    TargetArchive: str
    ActionFailurePolicy: NotRequired[ActionFailurePolicyType]

class ArchiveBooleanToEvaluateTypeDef(TypedDict):
    Attribute: NotRequired[Literal["HAS_ATTACHMENTS"]]

class ArchiveRetentionTypeDef(TypedDict):
    RetentionPeriod: NotRequired[RetentionPeriodType]

class ArchiveStringToEvaluateTypeDef(TypedDict):
    Attribute: NotRequired[ArchiveStringEmailAttributeType]

class ArchiveTypeDef(TypedDict):
    ArchiveId: str
    ArchiveName: NotRequired[str]
    ArchiveState: NotRequired[ArchiveStateType]
    LastUpdatedTimestamp: NotRequired[datetime]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ImportDataFormatTypeDef(TypedDict):
    ImportDataType: ImportDataTypeType

class IngressPointConfigurationTypeDef(TypedDict):
    SmtpPassword: NotRequired[str]
    SecretArn: NotRequired[str]

class DeleteAddonInstanceRequestTypeDef(TypedDict):
    AddonInstanceId: str

class DeleteAddonSubscriptionRequestTypeDef(TypedDict):
    AddonSubscriptionId: str

class DeleteAddressListRequestTypeDef(TypedDict):
    AddressListId: str

class DeleteArchiveRequestTypeDef(TypedDict):
    ArchiveId: str

class DeleteIngressPointRequestTypeDef(TypedDict):
    IngressPointId: str

class DeleteRelayRequestTypeDef(TypedDict):
    RelayId: str

class DeleteRuleSetRequestTypeDef(TypedDict):
    RuleSetId: str

class DeleteTrafficPolicyRequestTypeDef(TypedDict):
    TrafficPolicyId: str

class DeliverToMailboxActionTypeDef(TypedDict):
    MailboxArn: str
    RoleArn: str
    ActionFailurePolicy: NotRequired[ActionFailurePolicyType]

class DeliverToQBusinessActionTypeDef(TypedDict):
    ApplicationId: str
    IndexId: str
    RoleArn: str
    ActionFailurePolicy: NotRequired[ActionFailurePolicyType]

class DeregisterMemberFromAddressListRequestTypeDef(TypedDict):
    AddressListId: str
    Address: str

class EnvelopeTypeDef(TypedDict):
    Helo: NotRequired[str]
    From: NotRequired[str]
    To: NotRequired[List[str]]

class S3ExportDestinationConfigurationTypeDef(TypedDict):
    S3Location: NotRequired[str]

class ExportStatusTypeDef(TypedDict):
    SubmissionTimestamp: NotRequired[datetime]
    CompletionTimestamp: NotRequired[datetime]
    State: NotRequired[ExportStateType]
    ErrorMessage: NotRequired[str]

class GetAddonInstanceRequestTypeDef(TypedDict):
    AddonInstanceId: str

class GetAddonSubscriptionRequestTypeDef(TypedDict):
    AddonSubscriptionId: str

class GetAddressListImportJobRequestTypeDef(TypedDict):
    JobId: str

class GetAddressListRequestTypeDef(TypedDict):
    AddressListId: str

class GetArchiveExportRequestTypeDef(TypedDict):
    ExportId: str

class GetArchiveMessageContentRequestTypeDef(TypedDict):
    ArchivedMessageId: str

MessageBodyTypeDef = TypedDict(
    "MessageBodyTypeDef",
    {
        "Text": NotRequired[str],
        "Html": NotRequired[str],
        "MessageMalformed": NotRequired[bool],
    },
)

class GetArchiveMessageRequestTypeDef(TypedDict):
    ArchivedMessageId: str

class MetadataTypeDef(TypedDict):
    Timestamp: NotRequired[datetime]
    IngressPointId: NotRequired[str]
    TrafficPolicyId: NotRequired[str]
    RuleSetId: NotRequired[str]
    SenderHostname: NotRequired[str]
    SenderIpAddress: NotRequired[str]
    TlsCipherSuite: NotRequired[str]
    TlsProtocol: NotRequired[str]
    SendingMethod: NotRequired[str]
    SourceIdentity: NotRequired[str]
    SendingPool: NotRequired[str]
    ConfigurationSet: NotRequired[str]
    SourceArn: NotRequired[str]

class GetArchiveRequestTypeDef(TypedDict):
    ArchiveId: str

class GetArchiveSearchRequestTypeDef(TypedDict):
    SearchId: str

class SearchStatusTypeDef(TypedDict):
    SubmissionTimestamp: NotRequired[datetime]
    CompletionTimestamp: NotRequired[datetime]
    State: NotRequired[SearchStateType]
    ErrorMessage: NotRequired[str]

class GetArchiveSearchResultsRequestTypeDef(TypedDict):
    SearchId: str

class GetIngressPointRequestTypeDef(TypedDict):
    IngressPointId: str

class GetMemberOfAddressListRequestTypeDef(TypedDict):
    AddressListId: str
    Address: str

class GetRelayRequestTypeDef(TypedDict):
    RelayId: str

class RelayAuthenticationOutputTypeDef(TypedDict):
    SecretArn: NotRequired[str]
    NoAuthentication: NotRequired[Dict[str, Any]]

class GetRuleSetRequestTypeDef(TypedDict):
    RuleSetId: str

class GetTrafficPolicyRequestTypeDef(TypedDict):
    TrafficPolicyId: str

class IngressAnalysisTypeDef(TypedDict):
    Analyzer: str
    ResultField: str

class IngressIsInAddressListOutputTypeDef(TypedDict):
    Attribute: Literal["RECIPIENT"]
    AddressLists: List[str]

class IngressIpToEvaluateTypeDef(TypedDict):
    Attribute: NotRequired[Literal["SENDER_IP"]]

class IngressIpv6ToEvaluateTypeDef(TypedDict):
    Attribute: NotRequired[Literal["SENDER_IPV6"]]

class IngressIsInAddressListTypeDef(TypedDict):
    Attribute: Literal["RECIPIENT"]
    AddressLists: Sequence[str]

class IngressPointPasswordConfigurationTypeDef(TypedDict):
    SmtpPasswordVersion: NotRequired[str]
    PreviousSmtpPasswordVersion: NotRequired[str]
    PreviousSmtpPasswordExpiryTimestamp: NotRequired[datetime]

IngressPointTypeDef = TypedDict(
    "IngressPointTypeDef",
    {
        "IngressPointName": str,
        "IngressPointId": str,
        "Status": IngressPointStatusType,
        "Type": IngressPointTypeType,
        "ARecord": NotRequired[str],
    },
)

class IngressTlsProtocolToEvaluateTypeDef(TypedDict):
    Attribute: NotRequired[Literal["TLS_PROTOCOL"]]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAddonInstancesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    PageSize: NotRequired[int]

class ListAddonSubscriptionsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    PageSize: NotRequired[int]

class ListAddressListImportJobsRequestTypeDef(TypedDict):
    AddressListId: str
    NextToken: NotRequired[str]
    PageSize: NotRequired[int]

class ListAddressListsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    PageSize: NotRequired[int]

class ListArchiveExportsRequestTypeDef(TypedDict):
    ArchiveId: str
    NextToken: NotRequired[str]
    PageSize: NotRequired[int]

class ListArchiveSearchesRequestTypeDef(TypedDict):
    ArchiveId: str
    NextToken: NotRequired[str]
    PageSize: NotRequired[int]

class ListArchivesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    PageSize: NotRequired[int]

class ListIngressPointsRequestTypeDef(TypedDict):
    PageSize: NotRequired[int]
    NextToken: NotRequired[str]

class SavedAddressTypeDef(TypedDict):
    Address: str
    CreatedTimestamp: datetime

class ListRelaysRequestTypeDef(TypedDict):
    PageSize: NotRequired[int]
    NextToken: NotRequired[str]

class RelayTypeDef(TypedDict):
    RelayId: NotRequired[str]
    RelayName: NotRequired[str]
    LastModifiedTimestamp: NotRequired[datetime]

class ListRuleSetsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    PageSize: NotRequired[int]

class RuleSetTypeDef(TypedDict):
    RuleSetId: NotRequired[str]
    RuleSetName: NotRequired[str]
    LastModificationDate: NotRequired[datetime]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class ListTrafficPoliciesRequestTypeDef(TypedDict):
    PageSize: NotRequired[int]
    NextToken: NotRequired[str]

class TrafficPolicyTypeDef(TypedDict):
    TrafficPolicyName: str
    TrafficPolicyId: str
    DefaultAction: AcceptActionType

class PrivateNetworkConfigurationTypeDef(TypedDict):
    VpcEndpointId: str

class PublicNetworkConfigurationTypeDef(TypedDict):
    IpType: IpTypeType

class RegisterMemberToAddressListRequestTypeDef(TypedDict):
    AddressListId: str
    Address: str

class RelayActionTypeDef(TypedDict):
    Relay: str
    ActionFailurePolicy: NotRequired[ActionFailurePolicyType]
    MailFrom: NotRequired[MailFromType]

class RelayAuthenticationTypeDef(TypedDict):
    SecretArn: NotRequired[str]
    NoAuthentication: NotRequired[Mapping[str, Any]]

class ReplaceRecipientActionOutputTypeDef(TypedDict):
    ReplaceWith: NotRequired[List[str]]

class ReplaceRecipientActionTypeDef(TypedDict):
    ReplaceWith: NotRequired[Sequence[str]]

class S3ActionTypeDef(TypedDict):
    RoleArn: str
    S3Bucket: str
    ActionFailurePolicy: NotRequired[ActionFailurePolicyType]
    S3Prefix: NotRequired[str]
    S3SseKmsKeyId: NotRequired[str]

class SendActionTypeDef(TypedDict):
    RoleArn: str
    ActionFailurePolicy: NotRequired[ActionFailurePolicyType]

class SnsActionTypeDef(TypedDict):
    TopicArn: str
    RoleArn: str
    ActionFailurePolicy: NotRequired[ActionFailurePolicyType]
    Encoding: NotRequired[SnsNotificationEncodingType]
    PayloadType: NotRequired[SnsNotificationPayloadTypeType]

class RuleIsInAddressListOutputTypeDef(TypedDict):
    Attribute: RuleAddressListEmailAttributeType
    AddressLists: List[str]

class RuleDmarcExpressionOutputTypeDef(TypedDict):
    Operator: RuleDmarcOperatorType
    Values: List[RuleDmarcPolicyType]

class RuleDmarcExpressionTypeDef(TypedDict):
    Operator: RuleDmarcOperatorType
    Values: Sequence[RuleDmarcPolicyType]

class RuleIpToEvaluateTypeDef(TypedDict):
    Attribute: NotRequired[Literal["SOURCE_IP"]]

class RuleIsInAddressListTypeDef(TypedDict):
    Attribute: RuleAddressListEmailAttributeType
    AddressLists: Sequence[str]

class RuleNumberToEvaluateTypeDef(TypedDict):
    Attribute: NotRequired[Literal["MESSAGE_SIZE"]]

class StartAddressListImportJobRequestTypeDef(TypedDict):
    JobId: str

TimestampTypeDef = Union[datetime, str]

class StopAddressListImportJobRequestTypeDef(TypedDict):
    JobId: str

class StopArchiveExportRequestTypeDef(TypedDict):
    ExportId: str

class StopArchiveSearchRequestTypeDef(TypedDict):
    SearchId: str

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class ListMembersOfAddressListRequestTypeDef(TypedDict):
    AddressListId: str
    Filter: NotRequired[AddressFilterTypeDef]
    NextToken: NotRequired[str]
    PageSize: NotRequired[int]

class RuleStringToEvaluateTypeDef(TypedDict):
    Attribute: NotRequired[RuleStringEmailAttributeType]
    MimeHeaderAttribute: NotRequired[str]
    Analysis: NotRequired[AnalysisTypeDef]

class RuleVerdictToEvaluateTypeDef(TypedDict):
    Attribute: NotRequired[RuleVerdictAttributeType]
    Analysis: NotRequired[AnalysisTypeDef]

class ArchiveBooleanExpressionTypeDef(TypedDict):
    Evaluate: ArchiveBooleanToEvaluateTypeDef
    Operator: ArchiveBooleanOperatorType

class UpdateArchiveRequestTypeDef(TypedDict):
    ArchiveId: str
    ArchiveName: NotRequired[str]
    Retention: NotRequired[ArchiveRetentionTypeDef]

class ArchiveStringExpressionOutputTypeDef(TypedDict):
    Evaluate: ArchiveStringToEvaluateTypeDef
    Operator: Literal["CONTAINS"]
    Values: List[str]

class ArchiveStringExpressionTypeDef(TypedDict):
    Evaluate: ArchiveStringToEvaluateTypeDef
    Operator: Literal["CONTAINS"]
    Values: Sequence[str]

class CreateAddonInstanceRequestTypeDef(TypedDict):
    AddonSubscriptionId: str
    ClientToken: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateAddonSubscriptionRequestTypeDef(TypedDict):
    AddonName: str
    ClientToken: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateAddressListRequestTypeDef(TypedDict):
    AddressListName: str
    ClientToken: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateArchiveRequestTypeDef(TypedDict):
    ArchiveName: str
    ClientToken: NotRequired[str]
    Retention: NotRequired[ArchiveRetentionTypeDef]
    KmsKeyArn: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateAddonInstanceResponseTypeDef(TypedDict):
    AddonInstanceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAddonSubscriptionResponseTypeDef(TypedDict):
    AddonSubscriptionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAddressListImportJobResponseTypeDef(TypedDict):
    JobId: str
    PreSignedUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAddressListResponseTypeDef(TypedDict):
    AddressListId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateArchiveResponseTypeDef(TypedDict):
    ArchiveId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIngressPointResponseTypeDef(TypedDict):
    IngressPointId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRelayResponseTypeDef(TypedDict):
    RelayId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleSetResponseTypeDef(TypedDict):
    RuleSetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrafficPolicyResponseTypeDef(TypedDict):
    TrafficPolicyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAddonInstanceResponseTypeDef(TypedDict):
    AddonSubscriptionId: str
    AddonName: str
    AddonInstanceArn: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetAddonSubscriptionResponseTypeDef(TypedDict):
    AddonName: str
    AddonSubscriptionArn: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetAddressListResponseTypeDef(TypedDict):
    AddressListId: str
    AddressListArn: str
    AddressListName: str
    CreatedTimestamp: datetime
    LastUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetArchiveResponseTypeDef(TypedDict):
    ArchiveId: str
    ArchiveName: str
    ArchiveArn: str
    ArchiveState: ArchiveStateType
    Retention: ArchiveRetentionTypeDef
    CreatedTimestamp: datetime
    LastUpdatedTimestamp: datetime
    KmsKeyArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMemberOfAddressListResponseTypeDef(TypedDict):
    Address: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListAddonInstancesResponseTypeDef(TypedDict):
    AddonInstances: List[AddonInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListAddonSubscriptionsResponseTypeDef(TypedDict):
    AddonSubscriptions: List[AddonSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListAddressListsResponseTypeDef(TypedDict):
    AddressLists: List[AddressListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListArchivesResponseTypeDef(TypedDict):
    Archives: List[ArchiveTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartArchiveExportResponseTypeDef(TypedDict):
    ExportId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartArchiveSearchResponseTypeDef(TypedDict):
    SearchId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAddressListImportJobRequestTypeDef(TypedDict):
    AddressListId: str
    Name: str
    ImportDataFormat: ImportDataFormatTypeDef
    ClientToken: NotRequired[str]

class GetAddressListImportJobResponseTypeDef(TypedDict):
    JobId: str
    Name: str
    Status: ImportJobStatusType
    PreSignedUrl: str
    ImportedItemsCount: int
    FailedItemsCount: int
    ImportDataFormat: ImportDataFormatTypeDef
    AddressListId: str
    CreatedTimestamp: datetime
    StartTimestamp: datetime
    CompletedTimestamp: datetime
    Error: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportJobTypeDef(TypedDict):
    JobId: str
    Name: str
    Status: ImportJobStatusType
    PreSignedUrl: str
    ImportDataFormat: ImportDataFormatTypeDef
    AddressListId: str
    CreatedTimestamp: datetime
    ImportedItemsCount: NotRequired[int]
    FailedItemsCount: NotRequired[int]
    StartTimestamp: NotRequired[datetime]
    CompletedTimestamp: NotRequired[datetime]
    Error: NotRequired[str]

class UpdateIngressPointRequestTypeDef(TypedDict):
    IngressPointId: str
    IngressPointName: NotRequired[str]
    StatusToUpdate: NotRequired[IngressPointStatusToUpdateType]
    RuleSetId: NotRequired[str]
    TrafficPolicyId: NotRequired[str]
    IngressPointConfiguration: NotRequired[IngressPointConfigurationTypeDef]

class RowTypeDef(TypedDict):
    ArchivedMessageId: NotRequired[str]
    ReceivedTimestamp: NotRequired[datetime]
    Date: NotRequired[str]
    To: NotRequired[str]
    From: NotRequired[str]
    Cc: NotRequired[str]
    Subject: NotRequired[str]
    MessageId: NotRequired[str]
    HasAttachments: NotRequired[bool]
    ReceivedHeaders: NotRequired[List[str]]
    InReplyTo: NotRequired[str]
    XMailer: NotRequired[str]
    XOriginalMailer: NotRequired[str]
    XPriority: NotRequired[str]
    IngressPointId: NotRequired[str]
    SenderHostname: NotRequired[str]
    SenderIpAddress: NotRequired[str]
    Envelope: NotRequired[EnvelopeTypeDef]
    SourceArn: NotRequired[str]

class ExportDestinationConfigurationTypeDef(TypedDict):
    S3: NotRequired[S3ExportDestinationConfigurationTypeDef]

class ExportSummaryTypeDef(TypedDict):
    ExportId: NotRequired[str]
    Status: NotRequired[ExportStatusTypeDef]

class GetArchiveMessageContentResponseTypeDef(TypedDict):
    Body: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetArchiveMessageResponseTypeDef(TypedDict):
    MessageDownloadLink: str
    Metadata: MetadataTypeDef
    Envelope: EnvelopeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchSummaryTypeDef(TypedDict):
    SearchId: NotRequired[str]
    Status: NotRequired[SearchStatusTypeDef]

class GetRelayResponseTypeDef(TypedDict):
    RelayId: str
    RelayArn: str
    RelayName: str
    ServerName: str
    ServerPort: int
    Authentication: RelayAuthenticationOutputTypeDef
    CreatedTimestamp: datetime
    LastModifiedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class IngressStringToEvaluateTypeDef(TypedDict):
    Attribute: NotRequired[Literal["RECIPIENT"]]
    Analysis: NotRequired[IngressAnalysisTypeDef]

class IngressBooleanToEvaluateOutputTypeDef(TypedDict):
    Analysis: NotRequired[IngressAnalysisTypeDef]
    IsInAddressList: NotRequired[IngressIsInAddressListOutputTypeDef]

class IngressIpv4ExpressionOutputTypeDef(TypedDict):
    Evaluate: IngressIpToEvaluateTypeDef
    Operator: IngressIpOperatorType
    Values: List[str]

class IngressIpv4ExpressionTypeDef(TypedDict):
    Evaluate: IngressIpToEvaluateTypeDef
    Operator: IngressIpOperatorType
    Values: Sequence[str]

class IngressIpv6ExpressionOutputTypeDef(TypedDict):
    Evaluate: IngressIpv6ToEvaluateTypeDef
    Operator: IngressIpOperatorType
    Values: List[str]

class IngressIpv6ExpressionTypeDef(TypedDict):
    Evaluate: IngressIpv6ToEvaluateTypeDef
    Operator: IngressIpOperatorType
    Values: Sequence[str]

IngressIsInAddressListUnionTypeDef = Union[
    IngressIsInAddressListTypeDef, IngressIsInAddressListOutputTypeDef
]

class IngressPointAuthConfigurationTypeDef(TypedDict):
    IngressPointPasswordConfiguration: NotRequired[IngressPointPasswordConfigurationTypeDef]
    SecretArn: NotRequired[str]

class ListIngressPointsResponseTypeDef(TypedDict):
    IngressPoints: List[IngressPointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class IngressTlsProtocolExpressionTypeDef(TypedDict):
    Evaluate: IngressTlsProtocolToEvaluateTypeDef
    Operator: IngressTlsProtocolOperatorType
    Value: IngressTlsProtocolAttributeType

class ListAddonInstancesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAddonSubscriptionsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAddressListImportJobsRequestPaginateTypeDef(TypedDict):
    AddressListId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAddressListsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListArchiveExportsRequestPaginateTypeDef(TypedDict):
    ArchiveId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListArchiveSearchesRequestPaginateTypeDef(TypedDict):
    ArchiveId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListArchivesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListIngressPointsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMembersOfAddressListRequestPaginateTypeDef(TypedDict):
    AddressListId: str
    Filter: NotRequired[AddressFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRelaysRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRuleSetsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTrafficPoliciesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMembersOfAddressListResponseTypeDef(TypedDict):
    Addresses: List[SavedAddressTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListRelaysResponseTypeDef(TypedDict):
    Relays: List[RelayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListRuleSetsResponseTypeDef(TypedDict):
    RuleSets: List[RuleSetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTrafficPoliciesResponseTypeDef(TypedDict):
    TrafficPolicies: List[TrafficPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class NetworkConfigurationTypeDef(TypedDict):
    PublicNetworkConfiguration: NotRequired[PublicNetworkConfigurationTypeDef]
    PrivateNetworkConfiguration: NotRequired[PrivateNetworkConfigurationTypeDef]

RelayAuthenticationUnionTypeDef = Union[
    RelayAuthenticationTypeDef, RelayAuthenticationOutputTypeDef
]
ReplaceRecipientActionUnionTypeDef = Union[
    ReplaceRecipientActionTypeDef, ReplaceRecipientActionOutputTypeDef
]

class RuleActionOutputTypeDef(TypedDict):
    Drop: NotRequired[Dict[str, Any]]
    Relay: NotRequired[RelayActionTypeDef]
    Archive: NotRequired[ArchiveActionTypeDef]
    WriteToS3: NotRequired[S3ActionTypeDef]
    Send: NotRequired[SendActionTypeDef]
    AddHeader: NotRequired[AddHeaderActionTypeDef]
    ReplaceRecipient: NotRequired[ReplaceRecipientActionOutputTypeDef]
    DeliverToMailbox: NotRequired[DeliverToMailboxActionTypeDef]
    DeliverToQBusiness: NotRequired[DeliverToQBusinessActionTypeDef]
    PublishToSns: NotRequired[SnsActionTypeDef]

class RuleBooleanToEvaluateOutputTypeDef(TypedDict):
    Attribute: NotRequired[RuleBooleanEmailAttributeType]
    Analysis: NotRequired[AnalysisTypeDef]
    IsInAddressList: NotRequired[RuleIsInAddressListOutputTypeDef]

RuleDmarcExpressionUnionTypeDef = Union[
    RuleDmarcExpressionTypeDef, RuleDmarcExpressionOutputTypeDef
]

class RuleIpExpressionOutputTypeDef(TypedDict):
    Evaluate: RuleIpToEvaluateTypeDef
    Operator: RuleIpOperatorType
    Values: List[str]

class RuleIpExpressionTypeDef(TypedDict):
    Evaluate: RuleIpToEvaluateTypeDef
    Operator: RuleIpOperatorType
    Values: Sequence[str]

RuleIsInAddressListUnionTypeDef = Union[
    RuleIsInAddressListTypeDef, RuleIsInAddressListOutputTypeDef
]

class RuleNumberExpressionTypeDef(TypedDict):
    Evaluate: RuleNumberToEvaluateTypeDef
    Operator: RuleNumberOperatorType
    Value: float

class RuleStringExpressionOutputTypeDef(TypedDict):
    Evaluate: RuleStringToEvaluateTypeDef
    Operator: RuleStringOperatorType
    Values: List[str]

class RuleStringExpressionTypeDef(TypedDict):
    Evaluate: RuleStringToEvaluateTypeDef
    Operator: RuleStringOperatorType
    Values: Sequence[str]

class RuleVerdictExpressionOutputTypeDef(TypedDict):
    Evaluate: RuleVerdictToEvaluateTypeDef
    Operator: RuleVerdictOperatorType
    Values: List[RuleVerdictType]

class RuleVerdictExpressionTypeDef(TypedDict):
    Evaluate: RuleVerdictToEvaluateTypeDef
    Operator: RuleVerdictOperatorType
    Values: Sequence[RuleVerdictType]

class ArchiveFilterConditionOutputTypeDef(TypedDict):
    StringExpression: NotRequired[ArchiveStringExpressionOutputTypeDef]
    BooleanExpression: NotRequired[ArchiveBooleanExpressionTypeDef]

class ArchiveFilterConditionTypeDef(TypedDict):
    StringExpression: NotRequired[ArchiveStringExpressionTypeDef]
    BooleanExpression: NotRequired[ArchiveBooleanExpressionTypeDef]

class ListAddressListImportJobsResponseTypeDef(TypedDict):
    ImportJobs: List[ImportJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetArchiveSearchResultsResponseTypeDef(TypedDict):
    Rows: List[RowTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListArchiveExportsResponseTypeDef(TypedDict):
    Exports: List[ExportSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListArchiveSearchesResponseTypeDef(TypedDict):
    Searches: List[SearchSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class IngressStringExpressionOutputTypeDef(TypedDict):
    Evaluate: IngressStringToEvaluateTypeDef
    Operator: IngressStringOperatorType
    Values: List[str]

class IngressStringExpressionTypeDef(TypedDict):
    Evaluate: IngressStringToEvaluateTypeDef
    Operator: IngressStringOperatorType
    Values: Sequence[str]

class IngressBooleanExpressionOutputTypeDef(TypedDict):
    Evaluate: IngressBooleanToEvaluateOutputTypeDef
    Operator: IngressBooleanOperatorType

IngressIpv4ExpressionUnionTypeDef = Union[
    IngressIpv4ExpressionTypeDef, IngressIpv4ExpressionOutputTypeDef
]
IngressIpv6ExpressionUnionTypeDef = Union[
    IngressIpv6ExpressionTypeDef, IngressIpv6ExpressionOutputTypeDef
]

class IngressBooleanToEvaluateTypeDef(TypedDict):
    Analysis: NotRequired[IngressAnalysisTypeDef]
    IsInAddressList: NotRequired[IngressIsInAddressListUnionTypeDef]

CreateIngressPointRequestTypeDef = TypedDict(
    "CreateIngressPointRequestTypeDef",
    {
        "IngressPointName": str,
        "Type": IngressPointTypeType,
        "RuleSetId": str,
        "TrafficPolicyId": str,
        "ClientToken": NotRequired[str],
        "IngressPointConfiguration": NotRequired[IngressPointConfigurationTypeDef],
        "NetworkConfiguration": NotRequired[NetworkConfigurationTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
GetIngressPointResponseTypeDef = TypedDict(
    "GetIngressPointResponseTypeDef",
    {
        "IngressPointId": str,
        "IngressPointName": str,
        "IngressPointArn": str,
        "Status": IngressPointStatusType,
        "Type": IngressPointTypeType,
        "ARecord": str,
        "RuleSetId": str,
        "TrafficPolicyId": str,
        "IngressPointAuthConfiguration": IngressPointAuthConfigurationTypeDef,
        "NetworkConfiguration": NetworkConfigurationTypeDef,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateRelayRequestTypeDef(TypedDict):
    RelayName: str
    ServerName: str
    ServerPort: int
    Authentication: RelayAuthenticationUnionTypeDef
    ClientToken: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class UpdateRelayRequestTypeDef(TypedDict):
    RelayId: str
    RelayName: NotRequired[str]
    ServerName: NotRequired[str]
    ServerPort: NotRequired[int]
    Authentication: NotRequired[RelayAuthenticationUnionTypeDef]

class RuleActionTypeDef(TypedDict):
    Drop: NotRequired[Mapping[str, Any]]
    Relay: NotRequired[RelayActionTypeDef]
    Archive: NotRequired[ArchiveActionTypeDef]
    WriteToS3: NotRequired[S3ActionTypeDef]
    Send: NotRequired[SendActionTypeDef]
    AddHeader: NotRequired[AddHeaderActionTypeDef]
    ReplaceRecipient: NotRequired[ReplaceRecipientActionUnionTypeDef]
    DeliverToMailbox: NotRequired[DeliverToMailboxActionTypeDef]
    DeliverToQBusiness: NotRequired[DeliverToQBusinessActionTypeDef]
    PublishToSns: NotRequired[SnsActionTypeDef]

class RuleBooleanExpressionOutputTypeDef(TypedDict):
    Evaluate: RuleBooleanToEvaluateOutputTypeDef
    Operator: RuleBooleanOperatorType

RuleIpExpressionUnionTypeDef = Union[RuleIpExpressionTypeDef, RuleIpExpressionOutputTypeDef]

class RuleBooleanToEvaluateTypeDef(TypedDict):
    Attribute: NotRequired[RuleBooleanEmailAttributeType]
    Analysis: NotRequired[AnalysisTypeDef]
    IsInAddressList: NotRequired[RuleIsInAddressListUnionTypeDef]

RuleStringExpressionUnionTypeDef = Union[
    RuleStringExpressionTypeDef, RuleStringExpressionOutputTypeDef
]
RuleVerdictExpressionUnionTypeDef = Union[
    RuleVerdictExpressionTypeDef, RuleVerdictExpressionOutputTypeDef
]

class ArchiveFiltersOutputTypeDef(TypedDict):
    Include: NotRequired[List[ArchiveFilterConditionOutputTypeDef]]
    Unless: NotRequired[List[ArchiveFilterConditionOutputTypeDef]]

class ArchiveFiltersTypeDef(TypedDict):
    Include: NotRequired[Sequence[ArchiveFilterConditionTypeDef]]
    Unless: NotRequired[Sequence[ArchiveFilterConditionTypeDef]]

IngressStringExpressionUnionTypeDef = Union[
    IngressStringExpressionTypeDef, IngressStringExpressionOutputTypeDef
]

class PolicyConditionOutputTypeDef(TypedDict):
    StringExpression: NotRequired[IngressStringExpressionOutputTypeDef]
    IpExpression: NotRequired[IngressIpv4ExpressionOutputTypeDef]
    Ipv6Expression: NotRequired[IngressIpv6ExpressionOutputTypeDef]
    TlsExpression: NotRequired[IngressTlsProtocolExpressionTypeDef]
    BooleanExpression: NotRequired[IngressBooleanExpressionOutputTypeDef]

IngressBooleanToEvaluateUnionTypeDef = Union[
    IngressBooleanToEvaluateTypeDef, IngressBooleanToEvaluateOutputTypeDef
]
RuleActionUnionTypeDef = Union[RuleActionTypeDef, RuleActionOutputTypeDef]

class RuleConditionOutputTypeDef(TypedDict):
    BooleanExpression: NotRequired[RuleBooleanExpressionOutputTypeDef]
    StringExpression: NotRequired[RuleStringExpressionOutputTypeDef]
    NumberExpression: NotRequired[RuleNumberExpressionTypeDef]
    IpExpression: NotRequired[RuleIpExpressionOutputTypeDef]
    VerdictExpression: NotRequired[RuleVerdictExpressionOutputTypeDef]
    DmarcExpression: NotRequired[RuleDmarcExpressionOutputTypeDef]

RuleBooleanToEvaluateUnionTypeDef = Union[
    RuleBooleanToEvaluateTypeDef, RuleBooleanToEvaluateOutputTypeDef
]

class GetArchiveExportResponseTypeDef(TypedDict):
    ArchiveId: str
    Filters: ArchiveFiltersOutputTypeDef
    FromTimestamp: datetime
    ToTimestamp: datetime
    MaxResults: int
    ExportDestinationConfiguration: ExportDestinationConfigurationTypeDef
    Status: ExportStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetArchiveSearchResponseTypeDef(TypedDict):
    ArchiveId: str
    Filters: ArchiveFiltersOutputTypeDef
    FromTimestamp: datetime
    ToTimestamp: datetime
    MaxResults: int
    Status: SearchStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

ArchiveFiltersUnionTypeDef = Union[ArchiveFiltersTypeDef, ArchiveFiltersOutputTypeDef]

class PolicyStatementOutputTypeDef(TypedDict):
    Conditions: List[PolicyConditionOutputTypeDef]
    Action: AcceptActionType

class IngressBooleanExpressionTypeDef(TypedDict):
    Evaluate: IngressBooleanToEvaluateUnionTypeDef
    Operator: IngressBooleanOperatorType

class RuleOutputTypeDef(TypedDict):
    Actions: List[RuleActionOutputTypeDef]
    Name: NotRequired[str]
    Conditions: NotRequired[List[RuleConditionOutputTypeDef]]
    Unless: NotRequired[List[RuleConditionOutputTypeDef]]

class RuleBooleanExpressionTypeDef(TypedDict):
    Evaluate: RuleBooleanToEvaluateUnionTypeDef
    Operator: RuleBooleanOperatorType

class StartArchiveExportRequestTypeDef(TypedDict):
    ArchiveId: str
    FromTimestamp: TimestampTypeDef
    ToTimestamp: TimestampTypeDef
    ExportDestinationConfiguration: ExportDestinationConfigurationTypeDef
    Filters: NotRequired[ArchiveFiltersUnionTypeDef]
    MaxResults: NotRequired[int]
    IncludeMetadata: NotRequired[bool]

class StartArchiveSearchRequestTypeDef(TypedDict):
    ArchiveId: str
    FromTimestamp: TimestampTypeDef
    ToTimestamp: TimestampTypeDef
    MaxResults: int
    Filters: NotRequired[ArchiveFiltersUnionTypeDef]

class GetTrafficPolicyResponseTypeDef(TypedDict):
    TrafficPolicyName: str
    TrafficPolicyId: str
    TrafficPolicyArn: str
    PolicyStatements: List[PolicyStatementOutputTypeDef]
    MaxMessageSizeBytes: int
    DefaultAction: AcceptActionType
    CreatedTimestamp: datetime
    LastUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

IngressBooleanExpressionUnionTypeDef = Union[
    IngressBooleanExpressionTypeDef, IngressBooleanExpressionOutputTypeDef
]

class GetRuleSetResponseTypeDef(TypedDict):
    RuleSetId: str
    RuleSetArn: str
    RuleSetName: str
    CreatedDate: datetime
    LastModificationDate: datetime
    Rules: List[RuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

RuleBooleanExpressionUnionTypeDef = Union[
    RuleBooleanExpressionTypeDef, RuleBooleanExpressionOutputTypeDef
]

class PolicyConditionTypeDef(TypedDict):
    StringExpression: NotRequired[IngressStringExpressionUnionTypeDef]
    IpExpression: NotRequired[IngressIpv4ExpressionUnionTypeDef]
    Ipv6Expression: NotRequired[IngressIpv6ExpressionUnionTypeDef]
    TlsExpression: NotRequired[IngressTlsProtocolExpressionTypeDef]
    BooleanExpression: NotRequired[IngressBooleanExpressionUnionTypeDef]

class RuleConditionTypeDef(TypedDict):
    BooleanExpression: NotRequired[RuleBooleanExpressionUnionTypeDef]
    StringExpression: NotRequired[RuleStringExpressionUnionTypeDef]
    NumberExpression: NotRequired[RuleNumberExpressionTypeDef]
    IpExpression: NotRequired[RuleIpExpressionUnionTypeDef]
    VerdictExpression: NotRequired[RuleVerdictExpressionUnionTypeDef]
    DmarcExpression: NotRequired[RuleDmarcExpressionUnionTypeDef]

PolicyConditionUnionTypeDef = Union[PolicyConditionTypeDef, PolicyConditionOutputTypeDef]
RuleConditionUnionTypeDef = Union[RuleConditionTypeDef, RuleConditionOutputTypeDef]

class PolicyStatementTypeDef(TypedDict):
    Conditions: Sequence[PolicyConditionUnionTypeDef]
    Action: AcceptActionType

class RuleTypeDef(TypedDict):
    Actions: Sequence[RuleActionUnionTypeDef]
    Name: NotRequired[str]
    Conditions: NotRequired[Sequence[RuleConditionUnionTypeDef]]
    Unless: NotRequired[Sequence[RuleConditionUnionTypeDef]]

PolicyStatementUnionTypeDef = Union[PolicyStatementTypeDef, PolicyStatementOutputTypeDef]
RuleUnionTypeDef = Union[RuleTypeDef, RuleOutputTypeDef]

class CreateTrafficPolicyRequestTypeDef(TypedDict):
    TrafficPolicyName: str
    PolicyStatements: Sequence[PolicyStatementUnionTypeDef]
    DefaultAction: AcceptActionType
    ClientToken: NotRequired[str]
    MaxMessageSizeBytes: NotRequired[int]
    Tags: NotRequired[Sequence[TagTypeDef]]

class UpdateTrafficPolicyRequestTypeDef(TypedDict):
    TrafficPolicyId: str
    TrafficPolicyName: NotRequired[str]
    PolicyStatements: NotRequired[Sequence[PolicyStatementUnionTypeDef]]
    DefaultAction: NotRequired[AcceptActionType]
    MaxMessageSizeBytes: NotRequired[int]

class CreateRuleSetRequestTypeDef(TypedDict):
    RuleSetName: str
    Rules: Sequence[RuleUnionTypeDef]
    ClientToken: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class UpdateRuleSetRequestTypeDef(TypedDict):
    RuleSetId: str
    RuleSetName: NotRequired[str]
    Rules: NotRequired[Sequence[RuleUnionTypeDef]]
