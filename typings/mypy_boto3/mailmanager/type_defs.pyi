"""
Type annotations for mailmanager service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mailmanager.type_defs import AddHeaderActionTypeDef

    data: AddHeaderActionTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AcceptActionType,
    ActionFailurePolicyType,
    ArchiveBooleanOperatorType,
    ArchiveStateType,
    ArchiveStringEmailAttributeType,
    ExportStateType,
    IngressBooleanOperatorType,
    IngressIpOperatorType,
    IngressPointStatusToUpdateType,
    IngressPointStatusType,
    IngressPointTypeType,
    IngressStringOperatorType,
    IngressTlsProtocolAttributeType,
    IngressTlsProtocolOperatorType,
    MailFromType,
    RetentionPeriodType,
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
    "AddHeaderActionTypeDef",
    "AddonInstanceTypeDef",
    "AddonSubscriptionTypeDef",
    "AnalysisTypeDef",
    "ArchiveActionTypeDef",
    "ArchiveBooleanExpressionTypeDef",
    "ArchiveBooleanToEvaluateTypeDef",
    "ArchiveFilterConditionTypeDef",
    "ArchiveFiltersTypeDef",
    "ArchiveRetentionTypeDef",
    "ArchiveStringExpressionTypeDef",
    "ArchiveStringToEvaluateTypeDef",
    "ArchiveTypeDef",
    "CreateAddonInstanceRequestRequestTypeDef",
    "CreateAddonInstanceResponseTypeDef",
    "CreateAddonSubscriptionRequestRequestTypeDef",
    "CreateAddonSubscriptionResponseTypeDef",
    "CreateArchiveRequestRequestTypeDef",
    "CreateArchiveResponseTypeDef",
    "CreateIngressPointRequestRequestTypeDef",
    "CreateIngressPointResponseTypeDef",
    "CreateRelayRequestRequestTypeDef",
    "CreateRelayResponseTypeDef",
    "CreateRuleSetRequestRequestTypeDef",
    "CreateRuleSetResponseTypeDef",
    "CreateTrafficPolicyRequestRequestTypeDef",
    "CreateTrafficPolicyResponseTypeDef",
    "DeleteAddonInstanceRequestRequestTypeDef",
    "DeleteAddonSubscriptionRequestRequestTypeDef",
    "DeleteArchiveRequestRequestTypeDef",
    "DeleteIngressPointRequestRequestTypeDef",
    "DeleteRelayRequestRequestTypeDef",
    "DeleteRuleSetRequestRequestTypeDef",
    "DeleteTrafficPolicyRequestRequestTypeDef",
    "DeliverToMailboxActionTypeDef",
    "ExportDestinationConfigurationTypeDef",
    "ExportStatusTypeDef",
    "ExportSummaryTypeDef",
    "GetAddonInstanceRequestRequestTypeDef",
    "GetAddonInstanceResponseTypeDef",
    "GetAddonSubscriptionRequestRequestTypeDef",
    "GetAddonSubscriptionResponseTypeDef",
    "GetArchiveExportRequestRequestTypeDef",
    "GetArchiveExportResponseTypeDef",
    "GetArchiveMessageContentRequestRequestTypeDef",
    "GetArchiveMessageContentResponseTypeDef",
    "GetArchiveMessageRequestRequestTypeDef",
    "GetArchiveMessageResponseTypeDef",
    "GetArchiveRequestRequestTypeDef",
    "GetArchiveResponseTypeDef",
    "GetArchiveSearchRequestRequestTypeDef",
    "GetArchiveSearchResponseTypeDef",
    "GetArchiveSearchResultsRequestRequestTypeDef",
    "GetArchiveSearchResultsResponseTypeDef",
    "GetIngressPointRequestRequestTypeDef",
    "GetIngressPointResponseTypeDef",
    "GetRelayRequestRequestTypeDef",
    "GetRelayResponseTypeDef",
    "GetRuleSetRequestRequestTypeDef",
    "GetRuleSetResponseTypeDef",
    "GetTrafficPolicyRequestRequestTypeDef",
    "GetTrafficPolicyResponseTypeDef",
    "IngressAnalysisTypeDef",
    "IngressBooleanExpressionTypeDef",
    "IngressBooleanToEvaluateTypeDef",
    "IngressIpToEvaluateTypeDef",
    "IngressIpv4ExpressionTypeDef",
    "IngressPointAuthConfigurationTypeDef",
    "IngressPointConfigurationTypeDef",
    "IngressPointPasswordConfigurationTypeDef",
    "IngressPointTypeDef",
    "IngressStringExpressionTypeDef",
    "IngressStringToEvaluateTypeDef",
    "IngressTlsProtocolExpressionTypeDef",
    "IngressTlsProtocolToEvaluateTypeDef",
    "ListAddonInstancesRequestRequestTypeDef",
    "ListAddonInstancesResponseTypeDef",
    "ListAddonSubscriptionsRequestRequestTypeDef",
    "ListAddonSubscriptionsResponseTypeDef",
    "ListArchiveExportsRequestRequestTypeDef",
    "ListArchiveExportsResponseTypeDef",
    "ListArchiveSearchesRequestRequestTypeDef",
    "ListArchiveSearchesResponseTypeDef",
    "ListArchivesRequestRequestTypeDef",
    "ListArchivesResponseTypeDef",
    "ListIngressPointsRequestRequestTypeDef",
    "ListIngressPointsResponseTypeDef",
    "ListRelaysRequestRequestTypeDef",
    "ListRelaysResponseTypeDef",
    "ListRuleSetsRequestRequestTypeDef",
    "ListRuleSetsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTrafficPoliciesRequestRequestTypeDef",
    "ListTrafficPoliciesResponseTypeDef",
    "MessageBodyTypeDef",
    "PaginatorConfigTypeDef",
    "PolicyConditionTypeDef",
    "PolicyStatementTypeDef",
    "RelayActionTypeDef",
    "RelayAuthenticationTypeDef",
    "RelayTypeDef",
    "ReplaceRecipientActionTypeDef",
    "ResponseMetadataTypeDef",
    "RowTypeDef",
    "RuleActionTypeDef",
    "RuleBooleanExpressionTypeDef",
    "RuleBooleanToEvaluateTypeDef",
    "RuleConditionTypeDef",
    "RuleDmarcExpressionTypeDef",
    "RuleIpExpressionTypeDef",
    "RuleIpToEvaluateTypeDef",
    "RuleNumberExpressionTypeDef",
    "RuleNumberToEvaluateTypeDef",
    "RuleSetTypeDef",
    "RuleStringExpressionTypeDef",
    "RuleStringToEvaluateTypeDef",
    "RuleTypeDef",
    "RuleVerdictExpressionTypeDef",
    "RuleVerdictToEvaluateTypeDef",
    "S3ActionTypeDef",
    "S3ExportDestinationConfigurationTypeDef",
    "SearchStatusTypeDef",
    "SearchSummaryTypeDef",
    "SendActionTypeDef",
    "StartArchiveExportRequestRequestTypeDef",
    "StartArchiveExportResponseTypeDef",
    "StartArchiveSearchRequestRequestTypeDef",
    "StartArchiveSearchResponseTypeDef",
    "StopArchiveExportRequestRequestTypeDef",
    "StopArchiveSearchRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TrafficPolicyTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateArchiveRequestRequestTypeDef",
    "UpdateIngressPointRequestRequestTypeDef",
    "UpdateRelayRequestRequestTypeDef",
    "UpdateRuleSetRequestRequestTypeDef",
    "UpdateTrafficPolicyRequestRequestTypeDef",
)

AddHeaderActionTypeDef = TypedDict(
    "AddHeaderActionTypeDef",
    {
        "HeaderName": str,
        "HeaderValue": str,
    },
)

AddonInstanceTypeDef = TypedDict(
    "AddonInstanceTypeDef",
    {
        "AddonInstanceArn": str,
        "AddonInstanceId": str,
        "AddonName": str,
        "AddonSubscriptionId": str,
        "CreatedTimestamp": datetime,
    },
    total=False,
)

AddonSubscriptionTypeDef = TypedDict(
    "AddonSubscriptionTypeDef",
    {
        "AddonName": str,
        "AddonSubscriptionArn": str,
        "AddonSubscriptionId": str,
        "CreatedTimestamp": datetime,
    },
    total=False,
)

AnalysisTypeDef = TypedDict(
    "AnalysisTypeDef",
    {
        "Analyzer": str,
        "ResultField": str,
    },
)

_RequiredArchiveActionTypeDef = TypedDict(
    "_RequiredArchiveActionTypeDef",
    {
        "TargetArchive": str,
    },
)
_OptionalArchiveActionTypeDef = TypedDict(
    "_OptionalArchiveActionTypeDef",
    {
        "ActionFailurePolicy": ActionFailurePolicyType,
    },
    total=False,
)

class ArchiveActionTypeDef(_RequiredArchiveActionTypeDef, _OptionalArchiveActionTypeDef):
    pass

ArchiveBooleanExpressionTypeDef = TypedDict(
    "ArchiveBooleanExpressionTypeDef",
    {
        "Evaluate": "ArchiveBooleanToEvaluateTypeDef",
        "Operator": ArchiveBooleanOperatorType,
    },
)

ArchiveBooleanToEvaluateTypeDef = TypedDict(
    "ArchiveBooleanToEvaluateTypeDef",
    {
        "Attribute": Literal["HAS_ATTACHMENTS"],
    },
    total=False,
)

ArchiveFilterConditionTypeDef = TypedDict(
    "ArchiveFilterConditionTypeDef",
    {
        "BooleanExpression": "ArchiveBooleanExpressionTypeDef",
        "StringExpression": "ArchiveStringExpressionTypeDef",
    },
    total=False,
)

ArchiveFiltersTypeDef = TypedDict(
    "ArchiveFiltersTypeDef",
    {
        "Include": List["ArchiveFilterConditionTypeDef"],
        "Unless": List["ArchiveFilterConditionTypeDef"],
    },
    total=False,
)

ArchiveRetentionTypeDef = TypedDict(
    "ArchiveRetentionTypeDef",
    {
        "RetentionPeriod": RetentionPeriodType,
    },
    total=False,
)

ArchiveStringExpressionTypeDef = TypedDict(
    "ArchiveStringExpressionTypeDef",
    {
        "Evaluate": "ArchiveStringToEvaluateTypeDef",
        "Operator": Literal["CONTAINS"],
        "Values": List[str],
    },
)

ArchiveStringToEvaluateTypeDef = TypedDict(
    "ArchiveStringToEvaluateTypeDef",
    {
        "Attribute": ArchiveStringEmailAttributeType,
    },
    total=False,
)

_RequiredArchiveTypeDef = TypedDict(
    "_RequiredArchiveTypeDef",
    {
        "ArchiveId": str,
    },
)
_OptionalArchiveTypeDef = TypedDict(
    "_OptionalArchiveTypeDef",
    {
        "ArchiveName": str,
        "ArchiveState": ArchiveStateType,
        "LastUpdatedTimestamp": datetime,
    },
    total=False,
)

class ArchiveTypeDef(_RequiredArchiveTypeDef, _OptionalArchiveTypeDef):
    pass

_RequiredCreateAddonInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAddonInstanceRequestRequestTypeDef",
    {
        "AddonSubscriptionId": str,
    },
)
_OptionalCreateAddonInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAddonInstanceRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateAddonInstanceRequestRequestTypeDef(
    _RequiredCreateAddonInstanceRequestRequestTypeDef,
    _OptionalCreateAddonInstanceRequestRequestTypeDef,
):
    pass

CreateAddonInstanceResponseTypeDef = TypedDict(
    "CreateAddonInstanceResponseTypeDef",
    {
        "AddonInstanceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAddonSubscriptionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAddonSubscriptionRequestRequestTypeDef",
    {
        "AddonName": str,
    },
)
_OptionalCreateAddonSubscriptionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAddonSubscriptionRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateAddonSubscriptionRequestRequestTypeDef(
    _RequiredCreateAddonSubscriptionRequestRequestTypeDef,
    _OptionalCreateAddonSubscriptionRequestRequestTypeDef,
):
    pass

CreateAddonSubscriptionResponseTypeDef = TypedDict(
    "CreateAddonSubscriptionResponseTypeDef",
    {
        "AddonSubscriptionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateArchiveRequestRequestTypeDef = TypedDict(
    "_RequiredCreateArchiveRequestRequestTypeDef",
    {
        "ArchiveName": str,
    },
)
_OptionalCreateArchiveRequestRequestTypeDef = TypedDict(
    "_OptionalCreateArchiveRequestRequestTypeDef",
    {
        "ClientToken": str,
        "KmsKeyArn": str,
        "Retention": "ArchiveRetentionTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateArchiveRequestRequestTypeDef(
    _RequiredCreateArchiveRequestRequestTypeDef, _OptionalCreateArchiveRequestRequestTypeDef
):
    pass

CreateArchiveResponseTypeDef = TypedDict(
    "CreateArchiveResponseTypeDef",
    {
        "ArchiveId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIngressPointRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIngressPointRequestRequestTypeDef",
    {
        "IngressPointName": str,
        "RuleSetId": str,
        "TrafficPolicyId": str,
        "Type": IngressPointTypeType,
    },
)
_OptionalCreateIngressPointRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIngressPointRequestRequestTypeDef",
    {
        "ClientToken": str,
        "IngressPointConfiguration": "IngressPointConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateIngressPointRequestRequestTypeDef(
    _RequiredCreateIngressPointRequestRequestTypeDef,
    _OptionalCreateIngressPointRequestRequestTypeDef,
):
    pass

CreateIngressPointResponseTypeDef = TypedDict(
    "CreateIngressPointResponseTypeDef",
    {
        "IngressPointId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRelayRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRelayRequestRequestTypeDef",
    {
        "Authentication": "RelayAuthenticationTypeDef",
        "RelayName": str,
        "ServerName": str,
        "ServerPort": int,
    },
)
_OptionalCreateRelayRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRelayRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateRelayRequestRequestTypeDef(
    _RequiredCreateRelayRequestRequestTypeDef, _OptionalCreateRelayRequestRequestTypeDef
):
    pass

CreateRelayResponseTypeDef = TypedDict(
    "CreateRelayResponseTypeDef",
    {
        "RelayId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRuleSetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRuleSetRequestRequestTypeDef",
    {
        "RuleSetName": str,
        "Rules": List["RuleTypeDef"],
    },
)
_OptionalCreateRuleSetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRuleSetRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateRuleSetRequestRequestTypeDef(
    _RequiredCreateRuleSetRequestRequestTypeDef, _OptionalCreateRuleSetRequestRequestTypeDef
):
    pass

CreateRuleSetResponseTypeDef = TypedDict(
    "CreateRuleSetResponseTypeDef",
    {
        "RuleSetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrafficPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrafficPolicyRequestRequestTypeDef",
    {
        "DefaultAction": AcceptActionType,
        "PolicyStatements": List["PolicyStatementTypeDef"],
        "TrafficPolicyName": str,
    },
)
_OptionalCreateTrafficPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrafficPolicyRequestRequestTypeDef",
    {
        "ClientToken": str,
        "MaxMessageSizeBytes": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateTrafficPolicyRequestRequestTypeDef(
    _RequiredCreateTrafficPolicyRequestRequestTypeDef,
    _OptionalCreateTrafficPolicyRequestRequestTypeDef,
):
    pass

CreateTrafficPolicyResponseTypeDef = TypedDict(
    "CreateTrafficPolicyResponseTypeDef",
    {
        "TrafficPolicyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAddonInstanceRequestRequestTypeDef = TypedDict(
    "DeleteAddonInstanceRequestRequestTypeDef",
    {
        "AddonInstanceId": str,
    },
)

DeleteAddonSubscriptionRequestRequestTypeDef = TypedDict(
    "DeleteAddonSubscriptionRequestRequestTypeDef",
    {
        "AddonSubscriptionId": str,
    },
)

DeleteArchiveRequestRequestTypeDef = TypedDict(
    "DeleteArchiveRequestRequestTypeDef",
    {
        "ArchiveId": str,
    },
)

DeleteIngressPointRequestRequestTypeDef = TypedDict(
    "DeleteIngressPointRequestRequestTypeDef",
    {
        "IngressPointId": str,
    },
)

DeleteRelayRequestRequestTypeDef = TypedDict(
    "DeleteRelayRequestRequestTypeDef",
    {
        "RelayId": str,
    },
)

DeleteRuleSetRequestRequestTypeDef = TypedDict(
    "DeleteRuleSetRequestRequestTypeDef",
    {
        "RuleSetId": str,
    },
)

DeleteTrafficPolicyRequestRequestTypeDef = TypedDict(
    "DeleteTrafficPolicyRequestRequestTypeDef",
    {
        "TrafficPolicyId": str,
    },
)

_RequiredDeliverToMailboxActionTypeDef = TypedDict(
    "_RequiredDeliverToMailboxActionTypeDef",
    {
        "MailboxArn": str,
        "RoleArn": str,
    },
)
_OptionalDeliverToMailboxActionTypeDef = TypedDict(
    "_OptionalDeliverToMailboxActionTypeDef",
    {
        "ActionFailurePolicy": ActionFailurePolicyType,
    },
    total=False,
)

class DeliverToMailboxActionTypeDef(
    _RequiredDeliverToMailboxActionTypeDef, _OptionalDeliverToMailboxActionTypeDef
):
    pass

ExportDestinationConfigurationTypeDef = TypedDict(
    "ExportDestinationConfigurationTypeDef",
    {
        "S3": "S3ExportDestinationConfigurationTypeDef",
    },
    total=False,
)

ExportStatusTypeDef = TypedDict(
    "ExportStatusTypeDef",
    {
        "CompletionTimestamp": datetime,
        "ErrorMessage": str,
        "State": ExportStateType,
        "SubmissionTimestamp": datetime,
    },
    total=False,
)

ExportSummaryTypeDef = TypedDict(
    "ExportSummaryTypeDef",
    {
        "ExportId": str,
        "Status": "ExportStatusTypeDef",
    },
    total=False,
)

GetAddonInstanceRequestRequestTypeDef = TypedDict(
    "GetAddonInstanceRequestRequestTypeDef",
    {
        "AddonInstanceId": str,
    },
)

GetAddonInstanceResponseTypeDef = TypedDict(
    "GetAddonInstanceResponseTypeDef",
    {
        "AddonInstanceArn": str,
        "AddonName": str,
        "AddonSubscriptionId": str,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAddonSubscriptionRequestRequestTypeDef = TypedDict(
    "GetAddonSubscriptionRequestRequestTypeDef",
    {
        "AddonSubscriptionId": str,
    },
)

GetAddonSubscriptionResponseTypeDef = TypedDict(
    "GetAddonSubscriptionResponseTypeDef",
    {
        "AddonName": str,
        "AddonSubscriptionArn": str,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetArchiveExportRequestRequestTypeDef = TypedDict(
    "GetArchiveExportRequestRequestTypeDef",
    {
        "ExportId": str,
    },
)

GetArchiveExportResponseTypeDef = TypedDict(
    "GetArchiveExportResponseTypeDef",
    {
        "ArchiveId": str,
        "ExportDestinationConfiguration": "ExportDestinationConfigurationTypeDef",
        "Filters": "ArchiveFiltersTypeDef",
        "FromTimestamp": datetime,
        "MaxResults": int,
        "Status": "ExportStatusTypeDef",
        "ToTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetArchiveMessageContentRequestRequestTypeDef = TypedDict(
    "GetArchiveMessageContentRequestRequestTypeDef",
    {
        "ArchivedMessageId": str,
    },
)

GetArchiveMessageContentResponseTypeDef = TypedDict(
    "GetArchiveMessageContentResponseTypeDef",
    {
        "Body": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetArchiveMessageRequestRequestTypeDef = TypedDict(
    "GetArchiveMessageRequestRequestTypeDef",
    {
        "ArchivedMessageId": str,
    },
)

GetArchiveMessageResponseTypeDef = TypedDict(
    "GetArchiveMessageResponseTypeDef",
    {
        "MessageDownloadLink": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetArchiveRequestRequestTypeDef = TypedDict(
    "GetArchiveRequestRequestTypeDef",
    {
        "ArchiveId": str,
    },
)

GetArchiveResponseTypeDef = TypedDict(
    "GetArchiveResponseTypeDef",
    {
        "ArchiveArn": str,
        "ArchiveId": str,
        "ArchiveName": str,
        "ArchiveState": ArchiveStateType,
        "CreatedTimestamp": datetime,
        "KmsKeyArn": str,
        "LastUpdatedTimestamp": datetime,
        "Retention": "ArchiveRetentionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetArchiveSearchRequestRequestTypeDef = TypedDict(
    "GetArchiveSearchRequestRequestTypeDef",
    {
        "SearchId": str,
    },
)

GetArchiveSearchResponseTypeDef = TypedDict(
    "GetArchiveSearchResponseTypeDef",
    {
        "ArchiveId": str,
        "Filters": "ArchiveFiltersTypeDef",
        "FromTimestamp": datetime,
        "MaxResults": int,
        "Status": "SearchStatusTypeDef",
        "ToTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetArchiveSearchResultsRequestRequestTypeDef = TypedDict(
    "GetArchiveSearchResultsRequestRequestTypeDef",
    {
        "SearchId": str,
    },
)

GetArchiveSearchResultsResponseTypeDef = TypedDict(
    "GetArchiveSearchResultsResponseTypeDef",
    {
        "Rows": List["RowTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIngressPointRequestRequestTypeDef = TypedDict(
    "GetIngressPointRequestRequestTypeDef",
    {
        "IngressPointId": str,
    },
)

GetIngressPointResponseTypeDef = TypedDict(
    "GetIngressPointResponseTypeDef",
    {
        "ARecord": str,
        "CreatedTimestamp": datetime,
        "IngressPointArn": str,
        "IngressPointAuthConfiguration": "IngressPointAuthConfigurationTypeDef",
        "IngressPointId": str,
        "IngressPointName": str,
        "LastUpdatedTimestamp": datetime,
        "RuleSetId": str,
        "Status": IngressPointStatusType,
        "TrafficPolicyId": str,
        "Type": IngressPointTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelayRequestRequestTypeDef = TypedDict(
    "GetRelayRequestRequestTypeDef",
    {
        "RelayId": str,
    },
)

GetRelayResponseTypeDef = TypedDict(
    "GetRelayResponseTypeDef",
    {
        "Authentication": "RelayAuthenticationTypeDef",
        "CreatedTimestamp": datetime,
        "LastModifiedTimestamp": datetime,
        "RelayArn": str,
        "RelayId": str,
        "RelayName": str,
        "ServerName": str,
        "ServerPort": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRuleSetRequestRequestTypeDef = TypedDict(
    "GetRuleSetRequestRequestTypeDef",
    {
        "RuleSetId": str,
    },
)

GetRuleSetResponseTypeDef = TypedDict(
    "GetRuleSetResponseTypeDef",
    {
        "CreatedDate": datetime,
        "LastModificationDate": datetime,
        "RuleSetArn": str,
        "RuleSetId": str,
        "RuleSetName": str,
        "Rules": List["RuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrafficPolicyRequestRequestTypeDef = TypedDict(
    "GetTrafficPolicyRequestRequestTypeDef",
    {
        "TrafficPolicyId": str,
    },
)

GetTrafficPolicyResponseTypeDef = TypedDict(
    "GetTrafficPolicyResponseTypeDef",
    {
        "CreatedTimestamp": datetime,
        "DefaultAction": AcceptActionType,
        "LastUpdatedTimestamp": datetime,
        "MaxMessageSizeBytes": int,
        "PolicyStatements": List["PolicyStatementTypeDef"],
        "TrafficPolicyArn": str,
        "TrafficPolicyId": str,
        "TrafficPolicyName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IngressAnalysisTypeDef = TypedDict(
    "IngressAnalysisTypeDef",
    {
        "Analyzer": str,
        "ResultField": str,
    },
)

IngressBooleanExpressionTypeDef = TypedDict(
    "IngressBooleanExpressionTypeDef",
    {
        "Evaluate": "IngressBooleanToEvaluateTypeDef",
        "Operator": IngressBooleanOperatorType,
    },
)

IngressBooleanToEvaluateTypeDef = TypedDict(
    "IngressBooleanToEvaluateTypeDef",
    {
        "Analysis": "IngressAnalysisTypeDef",
    },
    total=False,
)

IngressIpToEvaluateTypeDef = TypedDict(
    "IngressIpToEvaluateTypeDef",
    {
        "Attribute": Literal["SENDER_IP"],
    },
    total=False,
)

IngressIpv4ExpressionTypeDef = TypedDict(
    "IngressIpv4ExpressionTypeDef",
    {
        "Evaluate": "IngressIpToEvaluateTypeDef",
        "Operator": IngressIpOperatorType,
        "Values": List[str],
    },
)

IngressPointAuthConfigurationTypeDef = TypedDict(
    "IngressPointAuthConfigurationTypeDef",
    {
        "IngressPointPasswordConfiguration": "IngressPointPasswordConfigurationTypeDef",
        "SecretArn": str,
    },
    total=False,
)

IngressPointConfigurationTypeDef = TypedDict(
    "IngressPointConfigurationTypeDef",
    {
        "SecretArn": str,
        "SmtpPassword": str,
    },
    total=False,
)

IngressPointPasswordConfigurationTypeDef = TypedDict(
    "IngressPointPasswordConfigurationTypeDef",
    {
        "PreviousSmtpPasswordExpiryTimestamp": datetime,
        "PreviousSmtpPasswordVersion": str,
        "SmtpPasswordVersion": str,
    },
    total=False,
)

_RequiredIngressPointTypeDef = TypedDict(
    "_RequiredIngressPointTypeDef",
    {
        "IngressPointId": str,
        "IngressPointName": str,
        "Status": IngressPointStatusType,
        "Type": IngressPointTypeType,
    },
)
_OptionalIngressPointTypeDef = TypedDict(
    "_OptionalIngressPointTypeDef",
    {
        "ARecord": str,
    },
    total=False,
)

class IngressPointTypeDef(_RequiredIngressPointTypeDef, _OptionalIngressPointTypeDef):
    pass

IngressStringExpressionTypeDef = TypedDict(
    "IngressStringExpressionTypeDef",
    {
        "Evaluate": "IngressStringToEvaluateTypeDef",
        "Operator": IngressStringOperatorType,
        "Values": List[str],
    },
)

IngressStringToEvaluateTypeDef = TypedDict(
    "IngressStringToEvaluateTypeDef",
    {
        "Attribute": Literal["RECIPIENT"],
    },
    total=False,
)

IngressTlsProtocolExpressionTypeDef = TypedDict(
    "IngressTlsProtocolExpressionTypeDef",
    {
        "Evaluate": "IngressTlsProtocolToEvaluateTypeDef",
        "Operator": IngressTlsProtocolOperatorType,
        "Value": IngressTlsProtocolAttributeType,
    },
)

IngressTlsProtocolToEvaluateTypeDef = TypedDict(
    "IngressTlsProtocolToEvaluateTypeDef",
    {
        "Attribute": Literal["TLS_PROTOCOL"],
    },
    total=False,
)

ListAddonInstancesRequestRequestTypeDef = TypedDict(
    "ListAddonInstancesRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListAddonInstancesResponseTypeDef = TypedDict(
    "ListAddonInstancesResponseTypeDef",
    {
        "AddonInstances": List["AddonInstanceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAddonSubscriptionsRequestRequestTypeDef = TypedDict(
    "ListAddonSubscriptionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListAddonSubscriptionsResponseTypeDef = TypedDict(
    "ListAddonSubscriptionsResponseTypeDef",
    {
        "AddonSubscriptions": List["AddonSubscriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListArchiveExportsRequestRequestTypeDef = TypedDict(
    "_RequiredListArchiveExportsRequestRequestTypeDef",
    {
        "ArchiveId": str,
    },
)
_OptionalListArchiveExportsRequestRequestTypeDef = TypedDict(
    "_OptionalListArchiveExportsRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

class ListArchiveExportsRequestRequestTypeDef(
    _RequiredListArchiveExportsRequestRequestTypeDef,
    _OptionalListArchiveExportsRequestRequestTypeDef,
):
    pass

ListArchiveExportsResponseTypeDef = TypedDict(
    "ListArchiveExportsResponseTypeDef",
    {
        "Exports": List["ExportSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListArchiveSearchesRequestRequestTypeDef = TypedDict(
    "_RequiredListArchiveSearchesRequestRequestTypeDef",
    {
        "ArchiveId": str,
    },
)
_OptionalListArchiveSearchesRequestRequestTypeDef = TypedDict(
    "_OptionalListArchiveSearchesRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

class ListArchiveSearchesRequestRequestTypeDef(
    _RequiredListArchiveSearchesRequestRequestTypeDef,
    _OptionalListArchiveSearchesRequestRequestTypeDef,
):
    pass

ListArchiveSearchesResponseTypeDef = TypedDict(
    "ListArchiveSearchesResponseTypeDef",
    {
        "NextToken": str,
        "Searches": List["SearchSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListArchivesRequestRequestTypeDef = TypedDict(
    "ListArchivesRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListArchivesResponseTypeDef = TypedDict(
    "ListArchivesResponseTypeDef",
    {
        "Archives": List["ArchiveTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIngressPointsRequestRequestTypeDef = TypedDict(
    "ListIngressPointsRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListIngressPointsResponseTypeDef = TypedDict(
    "ListIngressPointsResponseTypeDef",
    {
        "IngressPoints": List["IngressPointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRelaysRequestRequestTypeDef = TypedDict(
    "ListRelaysRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListRelaysResponseTypeDef = TypedDict(
    "ListRelaysResponseTypeDef",
    {
        "NextToken": str,
        "Relays": List["RelayTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRuleSetsRequestRequestTypeDef = TypedDict(
    "ListRuleSetsRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListRuleSetsResponseTypeDef = TypedDict(
    "ListRuleSetsResponseTypeDef",
    {
        "NextToken": str,
        "RuleSets": List["RuleSetTypeDef"],
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

ListTrafficPoliciesRequestRequestTypeDef = TypedDict(
    "ListTrafficPoliciesRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListTrafficPoliciesResponseTypeDef = TypedDict(
    "ListTrafficPoliciesResponseTypeDef",
    {
        "NextToken": str,
        "TrafficPolicies": List["TrafficPolicyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MessageBodyTypeDef = TypedDict(
    "MessageBodyTypeDef",
    {
        "Html": str,
        "MessageMalformed": bool,
        "Text": str,
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

PolicyConditionTypeDef = TypedDict(
    "PolicyConditionTypeDef",
    {
        "BooleanExpression": "IngressBooleanExpressionTypeDef",
        "IpExpression": "IngressIpv4ExpressionTypeDef",
        "StringExpression": "IngressStringExpressionTypeDef",
        "TlsExpression": "IngressTlsProtocolExpressionTypeDef",
    },
    total=False,
)

PolicyStatementTypeDef = TypedDict(
    "PolicyStatementTypeDef",
    {
        "Action": AcceptActionType,
        "Conditions": List["PolicyConditionTypeDef"],
    },
)

_RequiredRelayActionTypeDef = TypedDict(
    "_RequiredRelayActionTypeDef",
    {
        "Relay": str,
    },
)
_OptionalRelayActionTypeDef = TypedDict(
    "_OptionalRelayActionTypeDef",
    {
        "ActionFailurePolicy": ActionFailurePolicyType,
        "MailFrom": MailFromType,
    },
    total=False,
)

class RelayActionTypeDef(_RequiredRelayActionTypeDef, _OptionalRelayActionTypeDef):
    pass

RelayAuthenticationTypeDef = TypedDict(
    "RelayAuthenticationTypeDef",
    {
        "NoAuthentication": Dict[str, Any],
        "SecretArn": str,
    },
    total=False,
)

RelayTypeDef = TypedDict(
    "RelayTypeDef",
    {
        "LastModifiedTimestamp": datetime,
        "RelayId": str,
        "RelayName": str,
    },
    total=False,
)

ReplaceRecipientActionTypeDef = TypedDict(
    "ReplaceRecipientActionTypeDef",
    {
        "ReplaceWith": List[str],
    },
    total=False,
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

RowTypeDef = TypedDict(
    "RowTypeDef",
    {
        "ArchivedMessageId": str,
        "Cc": str,
        "Date": str,
        "From": str,
        "HasAttachments": bool,
        "InReplyTo": str,
        "MessageId": str,
        "ReceivedHeaders": List[str],
        "ReceivedTimestamp": datetime,
        "Subject": str,
        "To": str,
        "XMailer": str,
        "XOriginalMailer": str,
        "XPriority": str,
    },
    total=False,
)

RuleActionTypeDef = TypedDict(
    "RuleActionTypeDef",
    {
        "AddHeader": "AddHeaderActionTypeDef",
        "Archive": "ArchiveActionTypeDef",
        "DeliverToMailbox": "DeliverToMailboxActionTypeDef",
        "Drop": Dict[str, Any],
        "Relay": "RelayActionTypeDef",
        "ReplaceRecipient": "ReplaceRecipientActionTypeDef",
        "Send": "SendActionTypeDef",
        "WriteToS3": "S3ActionTypeDef",
    },
    total=False,
)

RuleBooleanExpressionTypeDef = TypedDict(
    "RuleBooleanExpressionTypeDef",
    {
        "Evaluate": "RuleBooleanToEvaluateTypeDef",
        "Operator": RuleBooleanOperatorType,
    },
)

RuleBooleanToEvaluateTypeDef = TypedDict(
    "RuleBooleanToEvaluateTypeDef",
    {
        "Attribute": RuleBooleanEmailAttributeType,
    },
    total=False,
)

RuleConditionTypeDef = TypedDict(
    "RuleConditionTypeDef",
    {
        "BooleanExpression": "RuleBooleanExpressionTypeDef",
        "DmarcExpression": "RuleDmarcExpressionTypeDef",
        "IpExpression": "RuleIpExpressionTypeDef",
        "NumberExpression": "RuleNumberExpressionTypeDef",
        "StringExpression": "RuleStringExpressionTypeDef",
        "VerdictExpression": "RuleVerdictExpressionTypeDef",
    },
    total=False,
)

RuleDmarcExpressionTypeDef = TypedDict(
    "RuleDmarcExpressionTypeDef",
    {
        "Operator": RuleDmarcOperatorType,
        "Values": List[RuleDmarcPolicyType],
    },
)

RuleIpExpressionTypeDef = TypedDict(
    "RuleIpExpressionTypeDef",
    {
        "Evaluate": "RuleIpToEvaluateTypeDef",
        "Operator": RuleIpOperatorType,
        "Values": List[str],
    },
)

RuleIpToEvaluateTypeDef = TypedDict(
    "RuleIpToEvaluateTypeDef",
    {
        "Attribute": Literal["SOURCE_IP"],
    },
    total=False,
)

RuleNumberExpressionTypeDef = TypedDict(
    "RuleNumberExpressionTypeDef",
    {
        "Evaluate": "RuleNumberToEvaluateTypeDef",
        "Operator": RuleNumberOperatorType,
        "Value": float,
    },
)

RuleNumberToEvaluateTypeDef = TypedDict(
    "RuleNumberToEvaluateTypeDef",
    {
        "Attribute": Literal["MESSAGE_SIZE"],
    },
    total=False,
)

RuleSetTypeDef = TypedDict(
    "RuleSetTypeDef",
    {
        "LastModificationDate": datetime,
        "RuleSetId": str,
        "RuleSetName": str,
    },
    total=False,
)

RuleStringExpressionTypeDef = TypedDict(
    "RuleStringExpressionTypeDef",
    {
        "Evaluate": "RuleStringToEvaluateTypeDef",
        "Operator": RuleStringOperatorType,
        "Values": List[str],
    },
)

RuleStringToEvaluateTypeDef = TypedDict(
    "RuleStringToEvaluateTypeDef",
    {
        "Attribute": RuleStringEmailAttributeType,
    },
    total=False,
)

_RequiredRuleTypeDef = TypedDict(
    "_RequiredRuleTypeDef",
    {
        "Actions": List["RuleActionTypeDef"],
    },
)
_OptionalRuleTypeDef = TypedDict(
    "_OptionalRuleTypeDef",
    {
        "Conditions": List["RuleConditionTypeDef"],
        "Name": str,
        "Unless": List["RuleConditionTypeDef"],
    },
    total=False,
)

class RuleTypeDef(_RequiredRuleTypeDef, _OptionalRuleTypeDef):
    pass

RuleVerdictExpressionTypeDef = TypedDict(
    "RuleVerdictExpressionTypeDef",
    {
        "Evaluate": "RuleVerdictToEvaluateTypeDef",
        "Operator": RuleVerdictOperatorType,
        "Values": List[RuleVerdictType],
    },
)

RuleVerdictToEvaluateTypeDef = TypedDict(
    "RuleVerdictToEvaluateTypeDef",
    {
        "Analysis": "AnalysisTypeDef",
        "Attribute": RuleVerdictAttributeType,
    },
    total=False,
)

_RequiredS3ActionTypeDef = TypedDict(
    "_RequiredS3ActionTypeDef",
    {
        "RoleArn": str,
        "S3Bucket": str,
    },
)
_OptionalS3ActionTypeDef = TypedDict(
    "_OptionalS3ActionTypeDef",
    {
        "ActionFailurePolicy": ActionFailurePolicyType,
        "S3Prefix": str,
        "S3SseKmsKeyId": str,
    },
    total=False,
)

class S3ActionTypeDef(_RequiredS3ActionTypeDef, _OptionalS3ActionTypeDef):
    pass

S3ExportDestinationConfigurationTypeDef = TypedDict(
    "S3ExportDestinationConfigurationTypeDef",
    {
        "S3Location": str,
    },
    total=False,
)

SearchStatusTypeDef = TypedDict(
    "SearchStatusTypeDef",
    {
        "CompletionTimestamp": datetime,
        "ErrorMessage": str,
        "State": SearchStateType,
        "SubmissionTimestamp": datetime,
    },
    total=False,
)

SearchSummaryTypeDef = TypedDict(
    "SearchSummaryTypeDef",
    {
        "SearchId": str,
        "Status": "SearchStatusTypeDef",
    },
    total=False,
)

_RequiredSendActionTypeDef = TypedDict(
    "_RequiredSendActionTypeDef",
    {
        "RoleArn": str,
    },
)
_OptionalSendActionTypeDef = TypedDict(
    "_OptionalSendActionTypeDef",
    {
        "ActionFailurePolicy": ActionFailurePolicyType,
    },
    total=False,
)

class SendActionTypeDef(_RequiredSendActionTypeDef, _OptionalSendActionTypeDef):
    pass

_RequiredStartArchiveExportRequestRequestTypeDef = TypedDict(
    "_RequiredStartArchiveExportRequestRequestTypeDef",
    {
        "ArchiveId": str,
        "ExportDestinationConfiguration": "ExportDestinationConfigurationTypeDef",
        "FromTimestamp": Union[datetime, str],
        "ToTimestamp": Union[datetime, str],
    },
)
_OptionalStartArchiveExportRequestRequestTypeDef = TypedDict(
    "_OptionalStartArchiveExportRequestRequestTypeDef",
    {
        "Filters": "ArchiveFiltersTypeDef",
        "MaxResults": int,
    },
    total=False,
)

class StartArchiveExportRequestRequestTypeDef(
    _RequiredStartArchiveExportRequestRequestTypeDef,
    _OptionalStartArchiveExportRequestRequestTypeDef,
):
    pass

StartArchiveExportResponseTypeDef = TypedDict(
    "StartArchiveExportResponseTypeDef",
    {
        "ExportId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartArchiveSearchRequestRequestTypeDef = TypedDict(
    "_RequiredStartArchiveSearchRequestRequestTypeDef",
    {
        "ArchiveId": str,
        "FromTimestamp": Union[datetime, str],
        "MaxResults": int,
        "ToTimestamp": Union[datetime, str],
    },
)
_OptionalStartArchiveSearchRequestRequestTypeDef = TypedDict(
    "_OptionalStartArchiveSearchRequestRequestTypeDef",
    {
        "Filters": "ArchiveFiltersTypeDef",
    },
    total=False,
)

class StartArchiveSearchRequestRequestTypeDef(
    _RequiredStartArchiveSearchRequestRequestTypeDef,
    _OptionalStartArchiveSearchRequestRequestTypeDef,
):
    pass

StartArchiveSearchResponseTypeDef = TypedDict(
    "StartArchiveSearchResponseTypeDef",
    {
        "SearchId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopArchiveExportRequestRequestTypeDef = TypedDict(
    "StopArchiveExportRequestRequestTypeDef",
    {
        "ExportId": str,
    },
)

StopArchiveSearchRequestRequestTypeDef = TypedDict(
    "StopArchiveSearchRequestRequestTypeDef",
    {
        "SearchId": str,
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

TrafficPolicyTypeDef = TypedDict(
    "TrafficPolicyTypeDef",
    {
        "DefaultAction": AcceptActionType,
        "TrafficPolicyId": str,
        "TrafficPolicyName": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateArchiveRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateArchiveRequestRequestTypeDef",
    {
        "ArchiveId": str,
    },
)
_OptionalUpdateArchiveRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateArchiveRequestRequestTypeDef",
    {
        "ArchiveName": str,
        "Retention": "ArchiveRetentionTypeDef",
    },
    total=False,
)

class UpdateArchiveRequestRequestTypeDef(
    _RequiredUpdateArchiveRequestRequestTypeDef, _OptionalUpdateArchiveRequestRequestTypeDef
):
    pass

_RequiredUpdateIngressPointRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateIngressPointRequestRequestTypeDef",
    {
        "IngressPointId": str,
    },
)
_OptionalUpdateIngressPointRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIngressPointRequestRequestTypeDef",
    {
        "IngressPointConfiguration": "IngressPointConfigurationTypeDef",
        "IngressPointName": str,
        "RuleSetId": str,
        "StatusToUpdate": IngressPointStatusToUpdateType,
        "TrafficPolicyId": str,
    },
    total=False,
)

class UpdateIngressPointRequestRequestTypeDef(
    _RequiredUpdateIngressPointRequestRequestTypeDef,
    _OptionalUpdateIngressPointRequestRequestTypeDef,
):
    pass

_RequiredUpdateRelayRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRelayRequestRequestTypeDef",
    {
        "RelayId": str,
    },
)
_OptionalUpdateRelayRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRelayRequestRequestTypeDef",
    {
        "Authentication": "RelayAuthenticationTypeDef",
        "RelayName": str,
        "ServerName": str,
        "ServerPort": int,
    },
    total=False,
)

class UpdateRelayRequestRequestTypeDef(
    _RequiredUpdateRelayRequestRequestTypeDef, _OptionalUpdateRelayRequestRequestTypeDef
):
    pass

_RequiredUpdateRuleSetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRuleSetRequestRequestTypeDef",
    {
        "RuleSetId": str,
    },
)
_OptionalUpdateRuleSetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRuleSetRequestRequestTypeDef",
    {
        "RuleSetName": str,
        "Rules": List["RuleTypeDef"],
    },
    total=False,
)

class UpdateRuleSetRequestRequestTypeDef(
    _RequiredUpdateRuleSetRequestRequestTypeDef, _OptionalUpdateRuleSetRequestRequestTypeDef
):
    pass

_RequiredUpdateTrafficPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTrafficPolicyRequestRequestTypeDef",
    {
        "TrafficPolicyId": str,
    },
)
_OptionalUpdateTrafficPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTrafficPolicyRequestRequestTypeDef",
    {
        "DefaultAction": AcceptActionType,
        "MaxMessageSizeBytes": int,
        "PolicyStatements": List["PolicyStatementTypeDef"],
        "TrafficPolicyName": str,
    },
    total=False,
)

class UpdateTrafficPolicyRequestRequestTypeDef(
    _RequiredUpdateTrafficPolicyRequestRequestTypeDef,
    _OptionalUpdateTrafficPolicyRequestRequestTypeDef,
):
    pass
