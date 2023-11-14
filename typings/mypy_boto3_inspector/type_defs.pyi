"""
Type annotations for inspector service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector/type_defs.html)

Usage::

    ```python
    from mypy_boto3_inspector.type_defs import AddAttributesToFindingsRequestRequestTypeDef

    data: AddAttributesToFindingsRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AgentHealthCodeType,
    AgentHealthType,
    AssessmentRunNotificationSnsStatusCodeType,
    AssessmentRunStateType,
    FailedItemErrorCodeType,
    InspectorEventType,
    PreviewStatusType,
    ReportFileFormatType,
    ReportStatusType,
    ReportTypeType,
    ScopeTypeType,
    SeverityType,
    StopActionType,
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
    "AddAttributesToFindingsRequestRequestTypeDef",
    "AddAttributesToFindingsResponseTypeDef",
    "AgentFilterTypeDef",
    "AgentPreviewTypeDef",
    "AssessmentRunAgentTypeDef",
    "AssessmentRunFilterTypeDef",
    "AssessmentRunNotificationTypeDef",
    "AssessmentRunStateChangeTypeDef",
    "AssessmentRunTypeDef",
    "AssessmentTargetFilterTypeDef",
    "AssessmentTargetTypeDef",
    "AssessmentTemplateFilterTypeDef",
    "AssessmentTemplateTypeDef",
    "AssetAttributesTypeDef",
    "AttributeTypeDef",
    "CreateAssessmentTargetRequestRequestTypeDef",
    "CreateAssessmentTargetResponseTypeDef",
    "CreateAssessmentTemplateRequestRequestTypeDef",
    "CreateAssessmentTemplateResponseTypeDef",
    "CreateExclusionsPreviewRequestRequestTypeDef",
    "CreateExclusionsPreviewResponseTypeDef",
    "CreateResourceGroupRequestRequestTypeDef",
    "CreateResourceGroupResponseTypeDef",
    "DeleteAssessmentRunRequestRequestTypeDef",
    "DeleteAssessmentTargetRequestRequestTypeDef",
    "DeleteAssessmentTemplateRequestRequestTypeDef",
    "DescribeAssessmentRunsRequestRequestTypeDef",
    "DescribeAssessmentRunsResponseTypeDef",
    "DescribeAssessmentTargetsRequestRequestTypeDef",
    "DescribeAssessmentTargetsResponseTypeDef",
    "DescribeAssessmentTemplatesRequestRequestTypeDef",
    "DescribeAssessmentTemplatesResponseTypeDef",
    "DescribeCrossAccountAccessRoleResponseTypeDef",
    "DescribeExclusionsRequestRequestTypeDef",
    "DescribeExclusionsResponseTypeDef",
    "DescribeFindingsRequestRequestTypeDef",
    "DescribeFindingsResponseTypeDef",
    "DescribeResourceGroupsRequestRequestTypeDef",
    "DescribeResourceGroupsResponseTypeDef",
    "DescribeRulesPackagesRequestRequestTypeDef",
    "DescribeRulesPackagesResponseTypeDef",
    "DurationRangeTypeDef",
    "EventSubscriptionTypeDef",
    "ExclusionPreviewTypeDef",
    "ExclusionTypeDef",
    "FailedItemDetailsTypeDef",
    "FindingFilterTypeDef",
    "FindingTypeDef",
    "GetAssessmentReportRequestRequestTypeDef",
    "GetAssessmentReportResponseTypeDef",
    "GetExclusionsPreviewRequestRequestTypeDef",
    "GetExclusionsPreviewResponseTypeDef",
    "GetTelemetryMetadataRequestRequestTypeDef",
    "GetTelemetryMetadataResponseTypeDef",
    "InspectorServiceAttributesTypeDef",
    "ListAssessmentRunAgentsRequestRequestTypeDef",
    "ListAssessmentRunAgentsResponseTypeDef",
    "ListAssessmentRunsRequestRequestTypeDef",
    "ListAssessmentRunsResponseTypeDef",
    "ListAssessmentTargetsRequestRequestTypeDef",
    "ListAssessmentTargetsResponseTypeDef",
    "ListAssessmentTemplatesRequestRequestTypeDef",
    "ListAssessmentTemplatesResponseTypeDef",
    "ListEventSubscriptionsRequestRequestTypeDef",
    "ListEventSubscriptionsResponseTypeDef",
    "ListExclusionsRequestRequestTypeDef",
    "ListExclusionsResponseTypeDef",
    "ListFindingsRequestRequestTypeDef",
    "ListFindingsResponseTypeDef",
    "ListRulesPackagesRequestRequestTypeDef",
    "ListRulesPackagesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NetworkInterfaceTypeDef",
    "PaginatorConfigTypeDef",
    "PreviewAgentsRequestRequestTypeDef",
    "PreviewAgentsResponseTypeDef",
    "PrivateIpTypeDef",
    "RegisterCrossAccountAccessRoleRequestRequestTypeDef",
    "RemoveAttributesFromFindingsRequestRequestTypeDef",
    "RemoveAttributesFromFindingsResponseTypeDef",
    "ResourceGroupTagTypeDef",
    "ResourceGroupTypeDef",
    "ResponseMetadataTypeDef",
    "RulesPackageTypeDef",
    "ScopeTypeDef",
    "SecurityGroupTypeDef",
    "SetTagsForResourceRequestRequestTypeDef",
    "StartAssessmentRunRequestRequestTypeDef",
    "StartAssessmentRunResponseTypeDef",
    "StopAssessmentRunRequestRequestTypeDef",
    "SubscribeToEventRequestRequestTypeDef",
    "SubscriptionTypeDef",
    "TagTypeDef",
    "TelemetryMetadataTypeDef",
    "TimestampRangeTypeDef",
    "UnsubscribeFromEventRequestRequestTypeDef",
    "UpdateAssessmentTargetRequestRequestTypeDef",
)

AddAttributesToFindingsRequestRequestTypeDef = TypedDict(
    "AddAttributesToFindingsRequestRequestTypeDef",
    {
        "findingArns": List[str],
        "attributes": List["AttributeTypeDef"],
    },
)

AddAttributesToFindingsResponseTypeDef = TypedDict(
    "AddAttributesToFindingsResponseTypeDef",
    {
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AgentFilterTypeDef = TypedDict(
    "AgentFilterTypeDef",
    {
        "agentHealths": List[AgentHealthType],
        "agentHealthCodes": List[AgentHealthCodeType],
    },
)

_RequiredAgentPreviewTypeDef = TypedDict(
    "_RequiredAgentPreviewTypeDef",
    {
        "agentId": str,
    },
)
_OptionalAgentPreviewTypeDef = TypedDict(
    "_OptionalAgentPreviewTypeDef",
    {
        "hostname": str,
        "autoScalingGroup": str,
        "agentHealth": AgentHealthType,
        "agentVersion": str,
        "operatingSystem": str,
        "kernelVersion": str,
        "ipv4Address": str,
    },
    total=False,
)

class AgentPreviewTypeDef(_RequiredAgentPreviewTypeDef, _OptionalAgentPreviewTypeDef):
    pass

_RequiredAssessmentRunAgentTypeDef = TypedDict(
    "_RequiredAssessmentRunAgentTypeDef",
    {
        "agentId": str,
        "assessmentRunArn": str,
        "agentHealth": AgentHealthType,
        "agentHealthCode": AgentHealthCodeType,
        "telemetryMetadata": List["TelemetryMetadataTypeDef"],
    },
)
_OptionalAssessmentRunAgentTypeDef = TypedDict(
    "_OptionalAssessmentRunAgentTypeDef",
    {
        "agentHealthDetails": str,
        "autoScalingGroup": str,
    },
    total=False,
)

class AssessmentRunAgentTypeDef(
    _RequiredAssessmentRunAgentTypeDef, _OptionalAssessmentRunAgentTypeDef
):
    pass

AssessmentRunFilterTypeDef = TypedDict(
    "AssessmentRunFilterTypeDef",
    {
        "namePattern": str,
        "states": List[AssessmentRunStateType],
        "durationRange": "DurationRangeTypeDef",
        "rulesPackageArns": List[str],
        "startTimeRange": "TimestampRangeTypeDef",
        "completionTimeRange": "TimestampRangeTypeDef",
        "stateChangeTimeRange": "TimestampRangeTypeDef",
    },
    total=False,
)

_RequiredAssessmentRunNotificationTypeDef = TypedDict(
    "_RequiredAssessmentRunNotificationTypeDef",
    {
        "date": datetime,
        "event": InspectorEventType,
        "error": bool,
    },
)
_OptionalAssessmentRunNotificationTypeDef = TypedDict(
    "_OptionalAssessmentRunNotificationTypeDef",
    {
        "message": str,
        "snsTopicArn": str,
        "snsPublishStatusCode": AssessmentRunNotificationSnsStatusCodeType,
    },
    total=False,
)

class AssessmentRunNotificationTypeDef(
    _RequiredAssessmentRunNotificationTypeDef, _OptionalAssessmentRunNotificationTypeDef
):
    pass

AssessmentRunStateChangeTypeDef = TypedDict(
    "AssessmentRunStateChangeTypeDef",
    {
        "stateChangedAt": datetime,
        "state": AssessmentRunStateType,
    },
)

_RequiredAssessmentRunTypeDef = TypedDict(
    "_RequiredAssessmentRunTypeDef",
    {
        "arn": str,
        "name": str,
        "assessmentTemplateArn": str,
        "state": AssessmentRunStateType,
        "durationInSeconds": int,
        "rulesPackageArns": List[str],
        "userAttributesForFindings": List["AttributeTypeDef"],
        "createdAt": datetime,
        "stateChangedAt": datetime,
        "dataCollected": bool,
        "stateChanges": List["AssessmentRunStateChangeTypeDef"],
        "notifications": List["AssessmentRunNotificationTypeDef"],
        "findingCounts": Dict[SeverityType, int],
    },
)
_OptionalAssessmentRunTypeDef = TypedDict(
    "_OptionalAssessmentRunTypeDef",
    {
        "startedAt": datetime,
        "completedAt": datetime,
    },
    total=False,
)

class AssessmentRunTypeDef(_RequiredAssessmentRunTypeDef, _OptionalAssessmentRunTypeDef):
    pass

AssessmentTargetFilterTypeDef = TypedDict(
    "AssessmentTargetFilterTypeDef",
    {
        "assessmentTargetNamePattern": str,
    },
    total=False,
)

_RequiredAssessmentTargetTypeDef = TypedDict(
    "_RequiredAssessmentTargetTypeDef",
    {
        "arn": str,
        "name": str,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
)
_OptionalAssessmentTargetTypeDef = TypedDict(
    "_OptionalAssessmentTargetTypeDef",
    {
        "resourceGroupArn": str,
    },
    total=False,
)

class AssessmentTargetTypeDef(_RequiredAssessmentTargetTypeDef, _OptionalAssessmentTargetTypeDef):
    pass

AssessmentTemplateFilterTypeDef = TypedDict(
    "AssessmentTemplateFilterTypeDef",
    {
        "namePattern": str,
        "durationRange": "DurationRangeTypeDef",
        "rulesPackageArns": List[str],
    },
    total=False,
)

_RequiredAssessmentTemplateTypeDef = TypedDict(
    "_RequiredAssessmentTemplateTypeDef",
    {
        "arn": str,
        "name": str,
        "assessmentTargetArn": str,
        "durationInSeconds": int,
        "rulesPackageArns": List[str],
        "userAttributesForFindings": List["AttributeTypeDef"],
        "assessmentRunCount": int,
        "createdAt": datetime,
    },
)
_OptionalAssessmentTemplateTypeDef = TypedDict(
    "_OptionalAssessmentTemplateTypeDef",
    {
        "lastAssessmentRunArn": str,
    },
    total=False,
)

class AssessmentTemplateTypeDef(
    _RequiredAssessmentTemplateTypeDef, _OptionalAssessmentTemplateTypeDef
):
    pass

_RequiredAssetAttributesTypeDef = TypedDict(
    "_RequiredAssetAttributesTypeDef",
    {
        "schemaVersion": int,
    },
)
_OptionalAssetAttributesTypeDef = TypedDict(
    "_OptionalAssetAttributesTypeDef",
    {
        "agentId": str,
        "autoScalingGroup": str,
        "amiId": str,
        "hostname": str,
        "ipv4Addresses": List[str],
        "tags": List["TagTypeDef"],
        "networkInterfaces": List["NetworkInterfaceTypeDef"],
    },
    total=False,
)

class AssetAttributesTypeDef(_RequiredAssetAttributesTypeDef, _OptionalAssetAttributesTypeDef):
    pass

_RequiredAttributeTypeDef = TypedDict(
    "_RequiredAttributeTypeDef",
    {
        "key": str,
    },
)
_OptionalAttributeTypeDef = TypedDict(
    "_OptionalAttributeTypeDef",
    {
        "value": str,
    },
    total=False,
)

class AttributeTypeDef(_RequiredAttributeTypeDef, _OptionalAttributeTypeDef):
    pass

_RequiredCreateAssessmentTargetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAssessmentTargetRequestRequestTypeDef",
    {
        "assessmentTargetName": str,
    },
)
_OptionalCreateAssessmentTargetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAssessmentTargetRequestRequestTypeDef",
    {
        "resourceGroupArn": str,
    },
    total=False,
)

class CreateAssessmentTargetRequestRequestTypeDef(
    _RequiredCreateAssessmentTargetRequestRequestTypeDef,
    _OptionalCreateAssessmentTargetRequestRequestTypeDef,
):
    pass

CreateAssessmentTargetResponseTypeDef = TypedDict(
    "CreateAssessmentTargetResponseTypeDef",
    {
        "assessmentTargetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAssessmentTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAssessmentTemplateRequestRequestTypeDef",
    {
        "assessmentTargetArn": str,
        "assessmentTemplateName": str,
        "durationInSeconds": int,
        "rulesPackageArns": List[str],
    },
)
_OptionalCreateAssessmentTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAssessmentTemplateRequestRequestTypeDef",
    {
        "userAttributesForFindings": List["AttributeTypeDef"],
    },
    total=False,
)

class CreateAssessmentTemplateRequestRequestTypeDef(
    _RequiredCreateAssessmentTemplateRequestRequestTypeDef,
    _OptionalCreateAssessmentTemplateRequestRequestTypeDef,
):
    pass

CreateAssessmentTemplateResponseTypeDef = TypedDict(
    "CreateAssessmentTemplateResponseTypeDef",
    {
        "assessmentTemplateArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateExclusionsPreviewRequestRequestTypeDef = TypedDict(
    "CreateExclusionsPreviewRequestRequestTypeDef",
    {
        "assessmentTemplateArn": str,
    },
)

CreateExclusionsPreviewResponseTypeDef = TypedDict(
    "CreateExclusionsPreviewResponseTypeDef",
    {
        "previewToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResourceGroupRequestRequestTypeDef = TypedDict(
    "CreateResourceGroupRequestRequestTypeDef",
    {
        "resourceGroupTags": List["ResourceGroupTagTypeDef"],
    },
)

CreateResourceGroupResponseTypeDef = TypedDict(
    "CreateResourceGroupResponseTypeDef",
    {
        "resourceGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAssessmentRunRequestRequestTypeDef = TypedDict(
    "DeleteAssessmentRunRequestRequestTypeDef",
    {
        "assessmentRunArn": str,
    },
)

DeleteAssessmentTargetRequestRequestTypeDef = TypedDict(
    "DeleteAssessmentTargetRequestRequestTypeDef",
    {
        "assessmentTargetArn": str,
    },
)

DeleteAssessmentTemplateRequestRequestTypeDef = TypedDict(
    "DeleteAssessmentTemplateRequestRequestTypeDef",
    {
        "assessmentTemplateArn": str,
    },
)

DescribeAssessmentRunsRequestRequestTypeDef = TypedDict(
    "DescribeAssessmentRunsRequestRequestTypeDef",
    {
        "assessmentRunArns": List[str],
    },
)

DescribeAssessmentRunsResponseTypeDef = TypedDict(
    "DescribeAssessmentRunsResponseTypeDef",
    {
        "assessmentRuns": List["AssessmentRunTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAssessmentTargetsRequestRequestTypeDef = TypedDict(
    "DescribeAssessmentTargetsRequestRequestTypeDef",
    {
        "assessmentTargetArns": List[str],
    },
)

DescribeAssessmentTargetsResponseTypeDef = TypedDict(
    "DescribeAssessmentTargetsResponseTypeDef",
    {
        "assessmentTargets": List["AssessmentTargetTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAssessmentTemplatesRequestRequestTypeDef = TypedDict(
    "DescribeAssessmentTemplatesRequestRequestTypeDef",
    {
        "assessmentTemplateArns": List[str],
    },
)

DescribeAssessmentTemplatesResponseTypeDef = TypedDict(
    "DescribeAssessmentTemplatesResponseTypeDef",
    {
        "assessmentTemplates": List["AssessmentTemplateTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCrossAccountAccessRoleResponseTypeDef = TypedDict(
    "DescribeCrossAccountAccessRoleResponseTypeDef",
    {
        "roleArn": str,
        "valid": bool,
        "registeredAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeExclusionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeExclusionsRequestRequestTypeDef",
    {
        "exclusionArns": List[str],
    },
)
_OptionalDescribeExclusionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeExclusionsRequestRequestTypeDef",
    {
        "locale": Literal["EN_US"],
    },
    total=False,
)

class DescribeExclusionsRequestRequestTypeDef(
    _RequiredDescribeExclusionsRequestRequestTypeDef,
    _OptionalDescribeExclusionsRequestRequestTypeDef,
):
    pass

DescribeExclusionsResponseTypeDef = TypedDict(
    "DescribeExclusionsResponseTypeDef",
    {
        "exclusions": Dict[str, "ExclusionTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeFindingsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeFindingsRequestRequestTypeDef",
    {
        "findingArns": List[str],
    },
)
_OptionalDescribeFindingsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeFindingsRequestRequestTypeDef",
    {
        "locale": Literal["EN_US"],
    },
    total=False,
)

class DescribeFindingsRequestRequestTypeDef(
    _RequiredDescribeFindingsRequestRequestTypeDef, _OptionalDescribeFindingsRequestRequestTypeDef
):
    pass

DescribeFindingsResponseTypeDef = TypedDict(
    "DescribeFindingsResponseTypeDef",
    {
        "findings": List["FindingTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeResourceGroupsRequestRequestTypeDef = TypedDict(
    "DescribeResourceGroupsRequestRequestTypeDef",
    {
        "resourceGroupArns": List[str],
    },
)

DescribeResourceGroupsResponseTypeDef = TypedDict(
    "DescribeResourceGroupsResponseTypeDef",
    {
        "resourceGroups": List["ResourceGroupTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRulesPackagesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeRulesPackagesRequestRequestTypeDef",
    {
        "rulesPackageArns": List[str],
    },
)
_OptionalDescribeRulesPackagesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeRulesPackagesRequestRequestTypeDef",
    {
        "locale": Literal["EN_US"],
    },
    total=False,
)

class DescribeRulesPackagesRequestRequestTypeDef(
    _RequiredDescribeRulesPackagesRequestRequestTypeDef,
    _OptionalDescribeRulesPackagesRequestRequestTypeDef,
):
    pass

DescribeRulesPackagesResponseTypeDef = TypedDict(
    "DescribeRulesPackagesResponseTypeDef",
    {
        "rulesPackages": List["RulesPackageTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DurationRangeTypeDef = TypedDict(
    "DurationRangeTypeDef",
    {
        "minSeconds": int,
        "maxSeconds": int,
    },
    total=False,
)

EventSubscriptionTypeDef = TypedDict(
    "EventSubscriptionTypeDef",
    {
        "event": InspectorEventType,
        "subscribedAt": datetime,
    },
)

_RequiredExclusionPreviewTypeDef = TypedDict(
    "_RequiredExclusionPreviewTypeDef",
    {
        "title": str,
        "description": str,
        "recommendation": str,
        "scopes": List["ScopeTypeDef"],
    },
)
_OptionalExclusionPreviewTypeDef = TypedDict(
    "_OptionalExclusionPreviewTypeDef",
    {
        "attributes": List["AttributeTypeDef"],
    },
    total=False,
)

class ExclusionPreviewTypeDef(_RequiredExclusionPreviewTypeDef, _OptionalExclusionPreviewTypeDef):
    pass

_RequiredExclusionTypeDef = TypedDict(
    "_RequiredExclusionTypeDef",
    {
        "arn": str,
        "title": str,
        "description": str,
        "recommendation": str,
        "scopes": List["ScopeTypeDef"],
    },
)
_OptionalExclusionTypeDef = TypedDict(
    "_OptionalExclusionTypeDef",
    {
        "attributes": List["AttributeTypeDef"],
    },
    total=False,
)

class ExclusionTypeDef(_RequiredExclusionTypeDef, _OptionalExclusionTypeDef):
    pass

FailedItemDetailsTypeDef = TypedDict(
    "FailedItemDetailsTypeDef",
    {
        "failureCode": FailedItemErrorCodeType,
        "retryable": bool,
    },
)

FindingFilterTypeDef = TypedDict(
    "FindingFilterTypeDef",
    {
        "agentIds": List[str],
        "autoScalingGroups": List[str],
        "ruleNames": List[str],
        "severities": List[SeverityType],
        "rulesPackageArns": List[str],
        "attributes": List["AttributeTypeDef"],
        "userAttributes": List["AttributeTypeDef"],
        "creationTimeRange": "TimestampRangeTypeDef",
    },
    total=False,
)

_RequiredFindingTypeDef = TypedDict(
    "_RequiredFindingTypeDef",
    {
        "arn": str,
        "attributes": List["AttributeTypeDef"],
        "userAttributes": List["AttributeTypeDef"],
        "createdAt": datetime,
        "updatedAt": datetime,
    },
)
_OptionalFindingTypeDef = TypedDict(
    "_OptionalFindingTypeDef",
    {
        "schemaVersion": int,
        "service": str,
        "serviceAttributes": "InspectorServiceAttributesTypeDef",
        "assetType": Literal["ec2-instance"],
        "assetAttributes": "AssetAttributesTypeDef",
        "id": str,
        "title": str,
        "description": str,
        "recommendation": str,
        "severity": SeverityType,
        "numericSeverity": float,
        "confidence": int,
        "indicatorOfCompromise": bool,
    },
    total=False,
)

class FindingTypeDef(_RequiredFindingTypeDef, _OptionalFindingTypeDef):
    pass

GetAssessmentReportRequestRequestTypeDef = TypedDict(
    "GetAssessmentReportRequestRequestTypeDef",
    {
        "assessmentRunArn": str,
        "reportFileFormat": ReportFileFormatType,
        "reportType": ReportTypeType,
    },
)

GetAssessmentReportResponseTypeDef = TypedDict(
    "GetAssessmentReportResponseTypeDef",
    {
        "status": ReportStatusType,
        "url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetExclusionsPreviewRequestRequestTypeDef = TypedDict(
    "_RequiredGetExclusionsPreviewRequestRequestTypeDef",
    {
        "assessmentTemplateArn": str,
        "previewToken": str,
    },
)
_OptionalGetExclusionsPreviewRequestRequestTypeDef = TypedDict(
    "_OptionalGetExclusionsPreviewRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "locale": Literal["EN_US"],
    },
    total=False,
)

class GetExclusionsPreviewRequestRequestTypeDef(
    _RequiredGetExclusionsPreviewRequestRequestTypeDef,
    _OptionalGetExclusionsPreviewRequestRequestTypeDef,
):
    pass

GetExclusionsPreviewResponseTypeDef = TypedDict(
    "GetExclusionsPreviewResponseTypeDef",
    {
        "previewStatus": PreviewStatusType,
        "exclusionPreviews": List["ExclusionPreviewTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTelemetryMetadataRequestRequestTypeDef = TypedDict(
    "GetTelemetryMetadataRequestRequestTypeDef",
    {
        "assessmentRunArn": str,
    },
)

GetTelemetryMetadataResponseTypeDef = TypedDict(
    "GetTelemetryMetadataResponseTypeDef",
    {
        "telemetryMetadata": List["TelemetryMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredInspectorServiceAttributesTypeDef = TypedDict(
    "_RequiredInspectorServiceAttributesTypeDef",
    {
        "schemaVersion": int,
    },
)
_OptionalInspectorServiceAttributesTypeDef = TypedDict(
    "_OptionalInspectorServiceAttributesTypeDef",
    {
        "assessmentRunArn": str,
        "rulesPackageArn": str,
    },
    total=False,
)

class InspectorServiceAttributesTypeDef(
    _RequiredInspectorServiceAttributesTypeDef, _OptionalInspectorServiceAttributesTypeDef
):
    pass

_RequiredListAssessmentRunAgentsRequestRequestTypeDef = TypedDict(
    "_RequiredListAssessmentRunAgentsRequestRequestTypeDef",
    {
        "assessmentRunArn": str,
    },
)
_OptionalListAssessmentRunAgentsRequestRequestTypeDef = TypedDict(
    "_OptionalListAssessmentRunAgentsRequestRequestTypeDef",
    {
        "filter": "AgentFilterTypeDef",
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListAssessmentRunAgentsRequestRequestTypeDef(
    _RequiredListAssessmentRunAgentsRequestRequestTypeDef,
    _OptionalListAssessmentRunAgentsRequestRequestTypeDef,
):
    pass

ListAssessmentRunAgentsResponseTypeDef = TypedDict(
    "ListAssessmentRunAgentsResponseTypeDef",
    {
        "assessmentRunAgents": List["AssessmentRunAgentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssessmentRunsRequestRequestTypeDef = TypedDict(
    "ListAssessmentRunsRequestRequestTypeDef",
    {
        "assessmentTemplateArns": List[str],
        "filter": "AssessmentRunFilterTypeDef",
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListAssessmentRunsResponseTypeDef = TypedDict(
    "ListAssessmentRunsResponseTypeDef",
    {
        "assessmentRunArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssessmentTargetsRequestRequestTypeDef = TypedDict(
    "ListAssessmentTargetsRequestRequestTypeDef",
    {
        "filter": "AssessmentTargetFilterTypeDef",
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListAssessmentTargetsResponseTypeDef = TypedDict(
    "ListAssessmentTargetsResponseTypeDef",
    {
        "assessmentTargetArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssessmentTemplatesRequestRequestTypeDef = TypedDict(
    "ListAssessmentTemplatesRequestRequestTypeDef",
    {
        "assessmentTargetArns": List[str],
        "filter": "AssessmentTemplateFilterTypeDef",
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListAssessmentTemplatesResponseTypeDef = TypedDict(
    "ListAssessmentTemplatesResponseTypeDef",
    {
        "assessmentTemplateArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventSubscriptionsRequestRequestTypeDef = TypedDict(
    "ListEventSubscriptionsRequestRequestTypeDef",
    {
        "resourceArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListEventSubscriptionsResponseTypeDef = TypedDict(
    "ListEventSubscriptionsResponseTypeDef",
    {
        "subscriptions": List["SubscriptionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListExclusionsRequestRequestTypeDef = TypedDict(
    "_RequiredListExclusionsRequestRequestTypeDef",
    {
        "assessmentRunArn": str,
    },
)
_OptionalListExclusionsRequestRequestTypeDef = TypedDict(
    "_OptionalListExclusionsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListExclusionsRequestRequestTypeDef(
    _RequiredListExclusionsRequestRequestTypeDef, _OptionalListExclusionsRequestRequestTypeDef
):
    pass

ListExclusionsResponseTypeDef = TypedDict(
    "ListExclusionsResponseTypeDef",
    {
        "exclusionArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFindingsRequestRequestTypeDef = TypedDict(
    "ListFindingsRequestRequestTypeDef",
    {
        "assessmentRunArns": List[str],
        "filter": "FindingFilterTypeDef",
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListFindingsResponseTypeDef = TypedDict(
    "ListFindingsResponseTypeDef",
    {
        "findingArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRulesPackagesRequestRequestTypeDef = TypedDict(
    "ListRulesPackagesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListRulesPackagesResponseTypeDef = TypedDict(
    "ListRulesPackagesResponseTypeDef",
    {
        "rulesPackageArns": List[str],
        "nextToken": str,
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
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "networkInterfaceId": str,
        "subnetId": str,
        "vpcId": str,
        "privateDnsName": str,
        "privateIpAddress": str,
        "privateIpAddresses": List["PrivateIpTypeDef"],
        "publicDnsName": str,
        "publicIp": str,
        "ipv6Addresses": List[str],
        "securityGroups": List["SecurityGroupTypeDef"],
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

_RequiredPreviewAgentsRequestRequestTypeDef = TypedDict(
    "_RequiredPreviewAgentsRequestRequestTypeDef",
    {
        "previewAgentsArn": str,
    },
)
_OptionalPreviewAgentsRequestRequestTypeDef = TypedDict(
    "_OptionalPreviewAgentsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class PreviewAgentsRequestRequestTypeDef(
    _RequiredPreviewAgentsRequestRequestTypeDef, _OptionalPreviewAgentsRequestRequestTypeDef
):
    pass

PreviewAgentsResponseTypeDef = TypedDict(
    "PreviewAgentsResponseTypeDef",
    {
        "agentPreviews": List["AgentPreviewTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PrivateIpTypeDef = TypedDict(
    "PrivateIpTypeDef",
    {
        "privateDnsName": str,
        "privateIpAddress": str,
    },
    total=False,
)

RegisterCrossAccountAccessRoleRequestRequestTypeDef = TypedDict(
    "RegisterCrossAccountAccessRoleRequestRequestTypeDef",
    {
        "roleArn": str,
    },
)

RemoveAttributesFromFindingsRequestRequestTypeDef = TypedDict(
    "RemoveAttributesFromFindingsRequestRequestTypeDef",
    {
        "findingArns": List[str],
        "attributeKeys": List[str],
    },
)

RemoveAttributesFromFindingsResponseTypeDef = TypedDict(
    "RemoveAttributesFromFindingsResponseTypeDef",
    {
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredResourceGroupTagTypeDef = TypedDict(
    "_RequiredResourceGroupTagTypeDef",
    {
        "key": str,
    },
)
_OptionalResourceGroupTagTypeDef = TypedDict(
    "_OptionalResourceGroupTagTypeDef",
    {
        "value": str,
    },
    total=False,
)

class ResourceGroupTagTypeDef(_RequiredResourceGroupTagTypeDef, _OptionalResourceGroupTagTypeDef):
    pass

ResourceGroupTypeDef = TypedDict(
    "ResourceGroupTypeDef",
    {
        "arn": str,
        "tags": List["ResourceGroupTagTypeDef"],
        "createdAt": datetime,
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

_RequiredRulesPackageTypeDef = TypedDict(
    "_RequiredRulesPackageTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "provider": str,
    },
)
_OptionalRulesPackageTypeDef = TypedDict(
    "_OptionalRulesPackageTypeDef",
    {
        "description": str,
    },
    total=False,
)

class RulesPackageTypeDef(_RequiredRulesPackageTypeDef, _OptionalRulesPackageTypeDef):
    pass

ScopeTypeDef = TypedDict(
    "ScopeTypeDef",
    {
        "key": ScopeTypeType,
        "value": str,
    },
    total=False,
)

SecurityGroupTypeDef = TypedDict(
    "SecurityGroupTypeDef",
    {
        "groupName": str,
        "groupId": str,
    },
    total=False,
)

_RequiredSetTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredSetTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalSetTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalSetTagsForResourceRequestRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class SetTagsForResourceRequestRequestTypeDef(
    _RequiredSetTagsForResourceRequestRequestTypeDef,
    _OptionalSetTagsForResourceRequestRequestTypeDef,
):
    pass

_RequiredStartAssessmentRunRequestRequestTypeDef = TypedDict(
    "_RequiredStartAssessmentRunRequestRequestTypeDef",
    {
        "assessmentTemplateArn": str,
    },
)
_OptionalStartAssessmentRunRequestRequestTypeDef = TypedDict(
    "_OptionalStartAssessmentRunRequestRequestTypeDef",
    {
        "assessmentRunName": str,
    },
    total=False,
)

class StartAssessmentRunRequestRequestTypeDef(
    _RequiredStartAssessmentRunRequestRequestTypeDef,
    _OptionalStartAssessmentRunRequestRequestTypeDef,
):
    pass

StartAssessmentRunResponseTypeDef = TypedDict(
    "StartAssessmentRunResponseTypeDef",
    {
        "assessmentRunArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStopAssessmentRunRequestRequestTypeDef = TypedDict(
    "_RequiredStopAssessmentRunRequestRequestTypeDef",
    {
        "assessmentRunArn": str,
    },
)
_OptionalStopAssessmentRunRequestRequestTypeDef = TypedDict(
    "_OptionalStopAssessmentRunRequestRequestTypeDef",
    {
        "stopAction": StopActionType,
    },
    total=False,
)

class StopAssessmentRunRequestRequestTypeDef(
    _RequiredStopAssessmentRunRequestRequestTypeDef, _OptionalStopAssessmentRunRequestRequestTypeDef
):
    pass

SubscribeToEventRequestRequestTypeDef = TypedDict(
    "SubscribeToEventRequestRequestTypeDef",
    {
        "resourceArn": str,
        "event": InspectorEventType,
        "topicArn": str,
    },
)

SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "resourceArn": str,
        "topicArn": str,
        "eventSubscriptions": List["EventSubscriptionTypeDef"],
    },
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "value": str,
    },
    total=False,
)

class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass

_RequiredTelemetryMetadataTypeDef = TypedDict(
    "_RequiredTelemetryMetadataTypeDef",
    {
        "messageType": str,
        "count": int,
    },
)
_OptionalTelemetryMetadataTypeDef = TypedDict(
    "_OptionalTelemetryMetadataTypeDef",
    {
        "dataSize": int,
    },
    total=False,
)

class TelemetryMetadataTypeDef(
    _RequiredTelemetryMetadataTypeDef, _OptionalTelemetryMetadataTypeDef
):
    pass

TimestampRangeTypeDef = TypedDict(
    "TimestampRangeTypeDef",
    {
        "beginDate": Union[datetime, str],
        "endDate": Union[datetime, str],
    },
    total=False,
)

UnsubscribeFromEventRequestRequestTypeDef = TypedDict(
    "UnsubscribeFromEventRequestRequestTypeDef",
    {
        "resourceArn": str,
        "event": InspectorEventType,
        "topicArn": str,
    },
)

_RequiredUpdateAssessmentTargetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAssessmentTargetRequestRequestTypeDef",
    {
        "assessmentTargetArn": str,
        "assessmentTargetName": str,
    },
)
_OptionalUpdateAssessmentTargetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAssessmentTargetRequestRequestTypeDef",
    {
        "resourceGroupArn": str,
    },
    total=False,
)

class UpdateAssessmentTargetRequestRequestTypeDef(
    _RequiredUpdateAssessmentTargetRequestRequestTypeDef,
    _OptionalUpdateAssessmentTargetRequestRequestTypeDef,
):
    pass
