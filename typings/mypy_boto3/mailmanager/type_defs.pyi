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
    AddonInstanceArn: NotRequired[str]
    AddonInstanceId: NotRequired[str]
    AddonName: NotRequired[str]
    AddonSubscriptionId: NotRequired[str]
    CreatedTimestamp: NotRequired[datetime]

class AddonSubscriptionTypeDef(TypedDict):
    AddonName: NotRequired[str]
    AddonSubscriptionArn: NotRequired[str]
    AddonSubscriptionId: NotRequired[str]
    CreatedTimestamp: NotRequired[datetime]

class AddressFilterTypeDef(TypedDict):
    AddressPrefix: NotRequired[str]

class AddressListTypeDef(TypedDict):
    AddressListArn: str
    AddressListId: str
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
    SecretArn: NotRequired[str]
    SmtpPassword: NotRequired[str]

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
    Address: str
    AddressListId: str

class EnvelopeTypeDef(TypedDict):
    From: NotRequired[str]
    Helo: NotRequired[str]
    To: NotRequired[List[str]]

class S3ExportDestinationConfigurationTypeDef(TypedDict):
    S3Location: NotRequired[str]

class ExportStatusTypeDef(TypedDict):
    CompletionTimestamp: NotRequired[datetime]
    ErrorMessage: NotRequired[str]
    State: NotRequired[ExportStateType]
    SubmissionTimestamp: NotRequired[datetime]

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
        "Html": NotRequired[str],
        "MessageMalformed": NotRequired[bool],
        "Text": NotRequired[str],
    },
)

class GetArchiveMessageRequestTypeDef(TypedDict):
    ArchivedMessageId: str

class MetadataTypeDef(TypedDict):
    ConfigurationSet: NotRequired[str]
    IngressPointId: NotRequired[str]
    RuleSetId: NotRequired[str]
    SenderHostname: NotRequired[str]
    SenderIpAddress: NotRequired[str]
    SendingMethod: NotRequired[str]
    SendingPool: NotRequired[str]
    SourceArn: NotRequired[str]
    SourceIdentity: NotRequired[str]
    Timestamp: NotRequired[datetime]
    TlsCipherSuite: NotRequired[str]
    TlsProtocol: NotRequired[str]
    TrafficPolicyId: NotRequired[str]

class GetArchiveRequestTypeDef(TypedDict):
    ArchiveId: str

class GetArchiveSearchRequestTypeDef(TypedDict):
    SearchId: str

class SearchStatusTypeDef(TypedDict):
    CompletionTimestamp: NotRequired[datetime]
    ErrorMessage: NotRequired[str]
    State: NotRequired[SearchStateType]
    SubmissionTimestamp: NotRequired[datetime]

class GetArchiveSearchResultsRequestTypeDef(TypedDict):
    SearchId: str

class GetIngressPointRequestTypeDef(TypedDict):
    IngressPointId: str

class GetMemberOfAddressListRequestTypeDef(TypedDict):
    Address: str
    AddressListId: str

class GetRelayRequestTypeDef(TypedDict):
    RelayId: str

class RelayAuthenticationOutputTypeDef(TypedDict):
    NoAuthentication: NotRequired[Dict[str, Any]]
    SecretArn: NotRequired[str]

class GetRuleSetRequestTypeDef(TypedDict):
    RuleSetId: str

class GetTrafficPolicyRequestTypeDef(TypedDict):
    TrafficPolicyId: str

class IngressAnalysisTypeDef(TypedDict):
    Analyzer: str
    ResultField: str

class IngressIsInAddressListOutputTypeDef(TypedDict):
    AddressLists: List[str]
    Attribute: Literal["RECIPIENT"]

class IngressIpToEvaluateTypeDef(TypedDict):
    Attribute: NotRequired[Literal["SENDER_IP"]]

class IngressIpv6ToEvaluateTypeDef(TypedDict):
    Attribute: NotRequired[Literal["SENDER_IPV6"]]

class IngressIsInAddressListTypeDef(TypedDict):
    AddressLists: Sequence[str]
    Attribute: Literal["RECIPIENT"]

class IngressPointPasswordConfigurationTypeDef(TypedDict):
    PreviousSmtpPasswordExpiryTimestamp: NotRequired[datetime]
    PreviousSmtpPasswordVersion: NotRequired[str]
    SmtpPasswordVersion: NotRequired[str]

IngressPointTypeDef = TypedDict(
    "IngressPointTypeDef",
    {
        "IngressPointId": str,
        "IngressPointName": str,
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
    NextToken: NotRequired[str]
    PageSize: NotRequired[int]

class SavedAddressTypeDef(TypedDict):
    Address: str
    CreatedTimestamp: datetime

class ListRelaysRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    PageSize: NotRequired[int]

class RelayTypeDef(TypedDict):
    LastModifiedTimestamp: NotRequired[datetime]
    RelayId: NotRequired[str]
    RelayName: NotRequired[str]

class ListRuleSetsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    PageSize: NotRequired[int]

class RuleSetTypeDef(TypedDict):
    LastModificationDate: NotRequired[datetime]
    RuleSetId: NotRequired[str]
    RuleSetName: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class ListTrafficPoliciesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    PageSize: NotRequired[int]

class TrafficPolicyTypeDef(TypedDict):
    DefaultAction: AcceptActionType
    TrafficPolicyId: str
    TrafficPolicyName: str

class PrivateNetworkConfigurationTypeDef(TypedDict):
    VpcEndpointId: str

class PublicNetworkConfigurationTypeDef(TypedDict):
    IpType: IpTypeType

class RegisterMemberToAddressListRequestTypeDef(TypedDict):
    Address: str
    AddressListId: str

class RelayActionTypeDef(TypedDict):
    Relay: str
    ActionFailurePolicy: NotRequired[ActionFailurePolicyType]
    MailFrom: NotRequired[MailFromType]

class RelayAuthenticationTypeDef(TypedDict):
    NoAuthentication: NotRequired[Mapping[str, Any]]
    SecretArn: NotRequired[str]

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
    RoleArn: str
    TopicArn: str
    ActionFailurePolicy: NotRequired[ActionFailurePolicyType]
    Encoding: NotRequired[SnsNotificationEncodingType]
    PayloadType: NotRequired[SnsNotificationPayloadTypeType]

class RuleIsInAddressListOutputTypeDef(TypedDict):
    AddressLists: List[str]
    Attribute: RuleAddressListEmailAttributeType

class RuleDmarcExpressionOutputTypeDef(TypedDict):
    Operator: RuleDmarcOperatorType
    Values: List[RuleDmarcPolicyType]

class RuleDmarcExpressionTypeDef(TypedDict):
    Operator: RuleDmarcOperatorType
    Values: Sequence[RuleDmarcPolicyType]

class RuleIpToEvaluateTypeDef(TypedDict):
    Attribute: NotRequired[Literal["SOURCE_IP"]]

class RuleIsInAddressListTypeDef(TypedDict):
    AddressLists: Sequence[str]
    Attribute: RuleAddressListEmailAttributeType

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
    Analysis: NotRequired[AnalysisTypeDef]
    Attribute: NotRequired[RuleStringEmailAttributeType]
    MimeHeaderAttribute: NotRequired[str]

class RuleVerdictToEvaluateTypeDef(TypedDict):
    Analysis: NotRequired[AnalysisTypeDef]
    Attribute: NotRequired[RuleVerdictAttributeType]

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
    KmsKeyArn: NotRequired[str]
    Retention: NotRequired[ArchiveRetentionTypeDef]
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
    AddonInstanceArn: str
    AddonName: str
    AddonSubscriptionId: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetAddonSubscriptionResponseTypeDef(TypedDict):
    AddonName: str
    AddonSubscriptionArn: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetAddressListResponseTypeDef(TypedDict):
    AddressListArn: str
    AddressListId: str
    AddressListName: str
    CreatedTimestamp: datetime
    LastUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetArchiveResponseTypeDef(TypedDict):
    ArchiveArn: str
    ArchiveId: str
    ArchiveName: str
    ArchiveState: ArchiveStateType
    CreatedTimestamp: datetime
    KmsKeyArn: str
    LastUpdatedTimestamp: datetime
    Retention: ArchiveRetentionTypeDef
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
    ImportDataFormat: ImportDataFormatTypeDef
    Name: str
    ClientToken: NotRequired[str]

class GetAddressListImportJobResponseTypeDef(TypedDict):
    AddressListId: str
    CompletedTimestamp: datetime
    CreatedTimestamp: datetime
    Error: str
    FailedItemsCount: int
    ImportDataFormat: ImportDataFormatTypeDef
    ImportedItemsCount: int
    JobId: str
    Name: str
    PreSignedUrl: str
    StartTimestamp: datetime
    Status: ImportJobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ImportJobTypeDef(TypedDict):
    AddressListId: str
    CreatedTimestamp: datetime
    ImportDataFormat: ImportDataFormatTypeDef
    JobId: str
    Name: str
    PreSignedUrl: str
    Status: ImportJobStatusType
    CompletedTimestamp: NotRequired[datetime]
    Error: NotRequired[str]
    FailedItemsCount: NotRequired[int]
    ImportedItemsCount: NotRequired[int]
    StartTimestamp: NotRequired[datetime]

class UpdateIngressPointRequestTypeDef(TypedDict):
    IngressPointId: str
    IngressPointConfiguration: NotRequired[IngressPointConfigurationTypeDef]
    IngressPointName: NotRequired[str]
    RuleSetId: NotRequired[str]
    StatusToUpdate: NotRequired[IngressPointStatusToUpdateType]
    TrafficPolicyId: NotRequired[str]

class RowTypeDef(TypedDict):
    ArchivedMessageId: NotRequired[str]
    Cc: NotRequired[str]
    Date: NotRequired[str]
    Envelope: NotRequired[EnvelopeTypeDef]
    From: NotRequired[str]
    HasAttachments: NotRequired[bool]
    InReplyTo: NotRequired[str]
    IngressPointId: NotRequired[str]
    MessageId: NotRequired[str]
    ReceivedHeaders: NotRequired[List[str]]
    ReceivedTimestamp: NotRequired[datetime]
    SenderHostname: NotRequired[str]
    SenderIpAddress: NotRequired[str]
    SourceArn: NotRequired[str]
    Subject: NotRequired[str]
    To: NotRequired[str]
    XMailer: NotRequired[str]
    XOriginalMailer: NotRequired[str]
    XPriority: NotRequired[str]

class ExportDestinationConfigurationTypeDef(TypedDict):
    S3: NotRequired[S3ExportDestinationConfigurationTypeDef]

class ExportSummaryTypeDef(TypedDict):
    ExportId: NotRequired[str]
    Status: NotRequired[ExportStatusTypeDef]

class GetArchiveMessageContentResponseTypeDef(TypedDict):
    Body: MessageBodyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetArchiveMessageResponseTypeDef(TypedDict):
    Envelope: EnvelopeTypeDef
    MessageDownloadLink: str
    Metadata: MetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchSummaryTypeDef(TypedDict):
    SearchId: NotRequired[str]
    Status: NotRequired[SearchStatusTypeDef]

class GetRelayResponseTypeDef(TypedDict):
    Authentication: RelayAuthenticationOutputTypeDef
    CreatedTimestamp: datetime
    LastModifiedTimestamp: datetime
    RelayArn: str
    RelayId: str
    RelayName: str
    ServerName: str
    ServerPort: int
    ResponseMetadata: ResponseMetadataTypeDef

class IngressStringToEvaluateTypeDef(TypedDict):
    Analysis: NotRequired[IngressAnalysisTypeDef]
    Attribute: NotRequired[Literal["RECIPIENT"]]

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
    PrivateNetworkConfiguration: NotRequired[PrivateNetworkConfigurationTypeDef]
    PublicNetworkConfiguration: NotRequired[PublicNetworkConfigurationTypeDef]

RelayAuthenticationUnionTypeDef = Union[
    RelayAuthenticationTypeDef, RelayAuthenticationOutputTypeDef
]
ReplaceRecipientActionUnionTypeDef = Union[
    ReplaceRecipientActionTypeDef, ReplaceRecipientActionOutputTypeDef
]

class RuleActionOutputTypeDef(TypedDict):
    AddHeader: NotRequired[AddHeaderActionTypeDef]
    Archive: NotRequired[ArchiveActionTypeDef]
    DeliverToMailbox: NotRequired[DeliverToMailboxActionTypeDef]
    DeliverToQBusiness: NotRequired[DeliverToQBusinessActionTypeDef]
    Drop: NotRequired[Dict[str, Any]]
    PublishToSns: NotRequired[SnsActionTypeDef]
    Relay: NotRequired[RelayActionTypeDef]
    ReplaceRecipient: NotRequired[ReplaceRecipientActionOutputTypeDef]
    Send: NotRequired[SendActionTypeDef]
    WriteToS3: NotRequired[S3ActionTypeDef]

class RuleBooleanToEvaluateOutputTypeDef(TypedDict):
    Analysis: NotRequired[AnalysisTypeDef]
    Attribute: NotRequired[RuleBooleanEmailAttributeType]
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
    BooleanExpression: NotRequired[ArchiveBooleanExpressionTypeDef]
    StringExpression: NotRequired[ArchiveStringExpressionOutputTypeDef]

class ArchiveFilterConditionTypeDef(TypedDict):
    BooleanExpression: NotRequired[ArchiveBooleanExpressionTypeDef]
    StringExpression: NotRequired[ArchiveStringExpressionTypeDef]

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
        "RuleSetId": str,
        "TrafficPolicyId": str,
        "Type": IngressPointTypeType,
        "ClientToken": NotRequired[str],
        "IngressPointConfiguration": NotRequired[IngressPointConfigurationTypeDef],
        "NetworkConfiguration": NotRequired[NetworkConfigurationTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
GetIngressPointResponseTypeDef = TypedDict(
    "GetIngressPointResponseTypeDef",
    {
        "ARecord": str,
        "CreatedTimestamp": datetime,
        "IngressPointArn": str,
        "IngressPointAuthConfiguration": IngressPointAuthConfigurationTypeDef,
        "IngressPointId": str,
        "IngressPointName": str,
        "LastUpdatedTimestamp": datetime,
        "NetworkConfiguration": NetworkConfigurationTypeDef,
        "RuleSetId": str,
        "Status": IngressPointStatusType,
        "TrafficPolicyId": str,
        "Type": IngressPointTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateRelayRequestTypeDef(TypedDict):
    Authentication: RelayAuthenticationUnionTypeDef
    RelayName: str
    ServerName: str
    ServerPort: int
    ClientToken: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class UpdateRelayRequestTypeDef(TypedDict):
    RelayId: str
    Authentication: NotRequired[RelayAuthenticationUnionTypeDef]
    RelayName: NotRequired[str]
    ServerName: NotRequired[str]
    ServerPort: NotRequired[int]

class RuleActionTypeDef(TypedDict):
    AddHeader: NotRequired[AddHeaderActionTypeDef]
    Archive: NotRequired[ArchiveActionTypeDef]
    DeliverToMailbox: NotRequired[DeliverToMailboxActionTypeDef]
    DeliverToQBusiness: NotRequired[DeliverToQBusinessActionTypeDef]
    Drop: NotRequired[Mapping[str, Any]]
    PublishToSns: NotRequired[SnsActionTypeDef]
    Relay: NotRequired[RelayActionTypeDef]
    ReplaceRecipient: NotRequired[ReplaceRecipientActionUnionTypeDef]
    Send: NotRequired[SendActionTypeDef]
    WriteToS3: NotRequired[S3ActionTypeDef]

class RuleBooleanExpressionOutputTypeDef(TypedDict):
    Evaluate: RuleBooleanToEvaluateOutputTypeDef
    Operator: RuleBooleanOperatorType

RuleIpExpressionUnionTypeDef = Union[RuleIpExpressionTypeDef, RuleIpExpressionOutputTypeDef]

class RuleBooleanToEvaluateTypeDef(TypedDict):
    Analysis: NotRequired[AnalysisTypeDef]
    Attribute: NotRequired[RuleBooleanEmailAttributeType]
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
    BooleanExpression: NotRequired[IngressBooleanExpressionOutputTypeDef]
    IpExpression: NotRequired[IngressIpv4ExpressionOutputTypeDef]
    Ipv6Expression: NotRequired[IngressIpv6ExpressionOutputTypeDef]
    StringExpression: NotRequired[IngressStringExpressionOutputTypeDef]
    TlsExpression: NotRequired[IngressTlsProtocolExpressionTypeDef]

IngressBooleanToEvaluateUnionTypeDef = Union[
    IngressBooleanToEvaluateTypeDef, IngressBooleanToEvaluateOutputTypeDef
]
RuleActionUnionTypeDef = Union[RuleActionTypeDef, RuleActionOutputTypeDef]

class RuleConditionOutputTypeDef(TypedDict):
    BooleanExpression: NotRequired[RuleBooleanExpressionOutputTypeDef]
    DmarcExpression: NotRequired[RuleDmarcExpressionOutputTypeDef]
    IpExpression: NotRequired[RuleIpExpressionOutputTypeDef]
    NumberExpression: NotRequired[RuleNumberExpressionTypeDef]
    StringExpression: NotRequired[RuleStringExpressionOutputTypeDef]
    VerdictExpression: NotRequired[RuleVerdictExpressionOutputTypeDef]

RuleBooleanToEvaluateUnionTypeDef = Union[
    RuleBooleanToEvaluateTypeDef, RuleBooleanToEvaluateOutputTypeDef
]

class GetArchiveExportResponseTypeDef(TypedDict):
    ArchiveId: str
    ExportDestinationConfiguration: ExportDestinationConfigurationTypeDef
    Filters: ArchiveFiltersOutputTypeDef
    FromTimestamp: datetime
    MaxResults: int
    Status: ExportStatusTypeDef
    ToTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetArchiveSearchResponseTypeDef(TypedDict):
    ArchiveId: str
    Filters: ArchiveFiltersOutputTypeDef
    FromTimestamp: datetime
    MaxResults: int
    Status: SearchStatusTypeDef
    ToTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

ArchiveFiltersUnionTypeDef = Union[ArchiveFiltersTypeDef, ArchiveFiltersOutputTypeDef]

class PolicyStatementOutputTypeDef(TypedDict):
    Action: AcceptActionType
    Conditions: List[PolicyConditionOutputTypeDef]

class IngressBooleanExpressionTypeDef(TypedDict):
    Evaluate: IngressBooleanToEvaluateUnionTypeDef
    Operator: IngressBooleanOperatorType

class RuleOutputTypeDef(TypedDict):
    Actions: List[RuleActionOutputTypeDef]
    Conditions: NotRequired[List[RuleConditionOutputTypeDef]]
    Name: NotRequired[str]
    Unless: NotRequired[List[RuleConditionOutputTypeDef]]

class RuleBooleanExpressionTypeDef(TypedDict):
    Evaluate: RuleBooleanToEvaluateUnionTypeDef
    Operator: RuleBooleanOperatorType

class StartArchiveExportRequestTypeDef(TypedDict):
    ArchiveId: str
    ExportDestinationConfiguration: ExportDestinationConfigurationTypeDef
    FromTimestamp: TimestampTypeDef
    ToTimestamp: TimestampTypeDef
    Filters: NotRequired[ArchiveFiltersUnionTypeDef]
    IncludeMetadata: NotRequired[bool]
    MaxResults: NotRequired[int]

class StartArchiveSearchRequestTypeDef(TypedDict):
    ArchiveId: str
    FromTimestamp: TimestampTypeDef
    MaxResults: int
    ToTimestamp: TimestampTypeDef
    Filters: NotRequired[ArchiveFiltersUnionTypeDef]

class GetTrafficPolicyResponseTypeDef(TypedDict):
    CreatedTimestamp: datetime
    DefaultAction: AcceptActionType
    LastUpdatedTimestamp: datetime
    MaxMessageSizeBytes: int
    PolicyStatements: List[PolicyStatementOutputTypeDef]
    TrafficPolicyArn: str
    TrafficPolicyId: str
    TrafficPolicyName: str
    ResponseMetadata: ResponseMetadataTypeDef

IngressBooleanExpressionUnionTypeDef = Union[
    IngressBooleanExpressionTypeDef, IngressBooleanExpressionOutputTypeDef
]

class GetRuleSetResponseTypeDef(TypedDict):
    CreatedDate: datetime
    LastModificationDate: datetime
    RuleSetArn: str
    RuleSetId: str
    RuleSetName: str
    Rules: List[RuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

RuleBooleanExpressionUnionTypeDef = Union[
    RuleBooleanExpressionTypeDef, RuleBooleanExpressionOutputTypeDef
]

class PolicyConditionTypeDef(TypedDict):
    BooleanExpression: NotRequired[IngressBooleanExpressionUnionTypeDef]
    IpExpression: NotRequired[IngressIpv4ExpressionUnionTypeDef]
    Ipv6Expression: NotRequired[IngressIpv6ExpressionUnionTypeDef]
    StringExpression: NotRequired[IngressStringExpressionUnionTypeDef]
    TlsExpression: NotRequired[IngressTlsProtocolExpressionTypeDef]

class RuleConditionTypeDef(TypedDict):
    BooleanExpression: NotRequired[RuleBooleanExpressionUnionTypeDef]
    DmarcExpression: NotRequired[RuleDmarcExpressionUnionTypeDef]
    IpExpression: NotRequired[RuleIpExpressionUnionTypeDef]
    NumberExpression: NotRequired[RuleNumberExpressionTypeDef]
    StringExpression: NotRequired[RuleStringExpressionUnionTypeDef]
    VerdictExpression: NotRequired[RuleVerdictExpressionUnionTypeDef]

PolicyConditionUnionTypeDef = Union[PolicyConditionTypeDef, PolicyConditionOutputTypeDef]
RuleConditionUnionTypeDef = Union[RuleConditionTypeDef, RuleConditionOutputTypeDef]

class PolicyStatementTypeDef(TypedDict):
    Action: AcceptActionType
    Conditions: Sequence[PolicyConditionUnionTypeDef]

class RuleTypeDef(TypedDict):
    Actions: Sequence[RuleActionUnionTypeDef]
    Conditions: NotRequired[Sequence[RuleConditionUnionTypeDef]]
    Name: NotRequired[str]
    Unless: NotRequired[Sequence[RuleConditionUnionTypeDef]]

PolicyStatementUnionTypeDef = Union[PolicyStatementTypeDef, PolicyStatementOutputTypeDef]
RuleUnionTypeDef = Union[RuleTypeDef, RuleOutputTypeDef]

class CreateTrafficPolicyRequestTypeDef(TypedDict):
    DefaultAction: AcceptActionType
    PolicyStatements: Sequence[PolicyStatementUnionTypeDef]
    TrafficPolicyName: str
    ClientToken: NotRequired[str]
    MaxMessageSizeBytes: NotRequired[int]
    Tags: NotRequired[Sequence[TagTypeDef]]

class UpdateTrafficPolicyRequestTypeDef(TypedDict):
    TrafficPolicyId: str
    DefaultAction: NotRequired[AcceptActionType]
    MaxMessageSizeBytes: NotRequired[int]
    PolicyStatements: NotRequired[Sequence[PolicyStatementUnionTypeDef]]
    TrafficPolicyName: NotRequired[str]

class CreateRuleSetRequestTypeDef(TypedDict):
    RuleSetName: str
    Rules: Sequence[RuleUnionTypeDef]
    ClientToken: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class UpdateRuleSetRequestTypeDef(TypedDict):
    RuleSetId: str
    RuleSetName: NotRequired[str]
    Rules: NotRequired[Sequence[RuleUnionTypeDef]]
