"""
Type annotations for launch-wizard service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/type_defs.html)

Usage::

    ```python
    from mypy_boto3_launch_wizard.type_defs import CreateDeploymentInputRequestTypeDef

    data: CreateDeploymentInputRequestTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    DeploymentFilterKeyType,
    DeploymentStatusType,
    EventStatusType,
    WorkloadDeploymentPatternStatusType,
    WorkloadStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateDeploymentInputRequestTypeDef",
    "CreateDeploymentOutputTypeDef",
    "DeleteDeploymentInputRequestTypeDef",
    "DeleteDeploymentOutputTypeDef",
    "DeploymentConditionalFieldTypeDef",
    "DeploymentDataSummaryTypeDef",
    "DeploymentDataTypeDef",
    "DeploymentEventDataSummaryTypeDef",
    "DeploymentFilterTypeDef",
    "DeploymentSpecificationsFieldTypeDef",
    "GetDeploymentInputRequestTypeDef",
    "GetDeploymentOutputTypeDef",
    "GetWorkloadDeploymentPatternInputRequestTypeDef",
    "GetWorkloadDeploymentPatternOutputTypeDef",
    "GetWorkloadInputRequestTypeDef",
    "GetWorkloadOutputTypeDef",
    "ListDeploymentEventsInputRequestTypeDef",
    "ListDeploymentEventsOutputTypeDef",
    "ListDeploymentsInputRequestTypeDef",
    "ListDeploymentsOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListWorkloadDeploymentPatternsInputRequestTypeDef",
    "ListWorkloadDeploymentPatternsOutputTypeDef",
    "ListWorkloadsInputRequestTypeDef",
    "ListWorkloadsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "WorkloadDataSummaryTypeDef",
    "WorkloadDataTypeDef",
    "WorkloadDeploymentPatternDataSummaryTypeDef",
    "WorkloadDeploymentPatternDataTypeDef",
)

_RequiredCreateDeploymentInputRequestTypeDef = TypedDict(
    "_RequiredCreateDeploymentInputRequestTypeDef",
    {
        "deploymentPatternName": str,
        "name": str,
        "specifications": Dict[str, str],
        "workloadName": str,
    },
)
_OptionalCreateDeploymentInputRequestTypeDef = TypedDict(
    "_OptionalCreateDeploymentInputRequestTypeDef",
    {
        "dryRun": bool,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateDeploymentInputRequestTypeDef(
    _RequiredCreateDeploymentInputRequestTypeDef, _OptionalCreateDeploymentInputRequestTypeDef
):
    pass

CreateDeploymentOutputTypeDef = TypedDict(
    "CreateDeploymentOutputTypeDef",
    {
        "deploymentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDeploymentInputRequestTypeDef = TypedDict(
    "DeleteDeploymentInputRequestTypeDef",
    {
        "deploymentId": str,
    },
)

DeleteDeploymentOutputTypeDef = TypedDict(
    "DeleteDeploymentOutputTypeDef",
    {
        "status": DeploymentStatusType,
        "statusReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeploymentConditionalFieldTypeDef = TypedDict(
    "DeploymentConditionalFieldTypeDef",
    {
        "comparator": str,
        "name": str,
        "value": str,
    },
    total=False,
)

DeploymentDataSummaryTypeDef = TypedDict(
    "DeploymentDataSummaryTypeDef",
    {
        "createdAt": datetime,
        "id": str,
        "name": str,
        "patternName": str,
        "status": DeploymentStatusType,
        "workloadName": str,
    },
    total=False,
)

DeploymentDataTypeDef = TypedDict(
    "DeploymentDataTypeDef",
    {
        "createdAt": datetime,
        "deletedAt": datetime,
        "deploymentArn": str,
        "id": str,
        "name": str,
        "patternName": str,
        "resourceGroup": str,
        "specifications": Dict[str, str],
        "status": DeploymentStatusType,
        "tags": Dict[str, str],
        "workloadName": str,
    },
    total=False,
)

DeploymentEventDataSummaryTypeDef = TypedDict(
    "DeploymentEventDataSummaryTypeDef",
    {
        "description": str,
        "name": str,
        "status": EventStatusType,
        "statusReason": str,
        "timestamp": datetime,
    },
    total=False,
)

DeploymentFilterTypeDef = TypedDict(
    "DeploymentFilterTypeDef",
    {
        "name": DeploymentFilterKeyType,
        "values": List[str],
    },
    total=False,
)

DeploymentSpecificationsFieldTypeDef = TypedDict(
    "DeploymentSpecificationsFieldTypeDef",
    {
        "allowedValues": List[str],
        "conditionals": List["DeploymentConditionalFieldTypeDef"],
        "description": str,
        "name": str,
        "required": str,
    },
    total=False,
)

GetDeploymentInputRequestTypeDef = TypedDict(
    "GetDeploymentInputRequestTypeDef",
    {
        "deploymentId": str,
    },
)

GetDeploymentOutputTypeDef = TypedDict(
    "GetDeploymentOutputTypeDef",
    {
        "deployment": "DeploymentDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkloadDeploymentPatternInputRequestTypeDef = TypedDict(
    "GetWorkloadDeploymentPatternInputRequestTypeDef",
    {
        "deploymentPatternName": str,
        "workloadName": str,
    },
)

GetWorkloadDeploymentPatternOutputTypeDef = TypedDict(
    "GetWorkloadDeploymentPatternOutputTypeDef",
    {
        "workloadDeploymentPattern": "WorkloadDeploymentPatternDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkloadInputRequestTypeDef = TypedDict(
    "GetWorkloadInputRequestTypeDef",
    {
        "workloadName": str,
    },
)

GetWorkloadOutputTypeDef = TypedDict(
    "GetWorkloadOutputTypeDef",
    {
        "workload": "WorkloadDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDeploymentEventsInputRequestTypeDef = TypedDict(
    "_RequiredListDeploymentEventsInputRequestTypeDef",
    {
        "deploymentId": str,
    },
)
_OptionalListDeploymentEventsInputRequestTypeDef = TypedDict(
    "_OptionalListDeploymentEventsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListDeploymentEventsInputRequestTypeDef(
    _RequiredListDeploymentEventsInputRequestTypeDef,
    _OptionalListDeploymentEventsInputRequestTypeDef,
):
    pass

ListDeploymentEventsOutputTypeDef = TypedDict(
    "ListDeploymentEventsOutputTypeDef",
    {
        "deploymentEvents": List["DeploymentEventDataSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeploymentsInputRequestTypeDef = TypedDict(
    "ListDeploymentsInputRequestTypeDef",
    {
        "filters": List["DeploymentFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListDeploymentsOutputTypeDef = TypedDict(
    "ListDeploymentsOutputTypeDef",
    {
        "deployments": List["DeploymentDataSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListWorkloadDeploymentPatternsInputRequestTypeDef = TypedDict(
    "_RequiredListWorkloadDeploymentPatternsInputRequestTypeDef",
    {
        "workloadName": str,
    },
)
_OptionalListWorkloadDeploymentPatternsInputRequestTypeDef = TypedDict(
    "_OptionalListWorkloadDeploymentPatternsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListWorkloadDeploymentPatternsInputRequestTypeDef(
    _RequiredListWorkloadDeploymentPatternsInputRequestTypeDef,
    _OptionalListWorkloadDeploymentPatternsInputRequestTypeDef,
):
    pass

ListWorkloadDeploymentPatternsOutputTypeDef = TypedDict(
    "ListWorkloadDeploymentPatternsOutputTypeDef",
    {
        "nextToken": str,
        "workloadDeploymentPatterns": List["WorkloadDeploymentPatternDataSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkloadsInputRequestTypeDef = TypedDict(
    "ListWorkloadsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListWorkloadsOutputTypeDef = TypedDict(
    "ListWorkloadsOutputTypeDef",
    {
        "nextToken": str,
        "workloads": List["WorkloadDataSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

WorkloadDataSummaryTypeDef = TypedDict(
    "WorkloadDataSummaryTypeDef",
    {
        "displayName": str,
        "workloadName": str,
    },
    total=False,
)

WorkloadDataTypeDef = TypedDict(
    "WorkloadDataTypeDef",
    {
        "description": str,
        "displayName": str,
        "documentationUrl": str,
        "iconUrl": str,
        "status": WorkloadStatusType,
        "statusMessage": str,
        "workloadName": str,
    },
    total=False,
)

WorkloadDeploymentPatternDataSummaryTypeDef = TypedDict(
    "WorkloadDeploymentPatternDataSummaryTypeDef",
    {
        "deploymentPatternName": str,
        "description": str,
        "displayName": str,
        "status": WorkloadDeploymentPatternStatusType,
        "statusMessage": str,
        "workloadName": str,
        "workloadVersionName": str,
    },
    total=False,
)

WorkloadDeploymentPatternDataTypeDef = TypedDict(
    "WorkloadDeploymentPatternDataTypeDef",
    {
        "deploymentPatternName": str,
        "description": str,
        "displayName": str,
        "specifications": List["DeploymentSpecificationsFieldTypeDef"],
        "status": WorkloadDeploymentPatternStatusType,
        "statusMessage": str,
        "workloadName": str,
        "workloadVersionName": str,
    },
    total=False,
)
