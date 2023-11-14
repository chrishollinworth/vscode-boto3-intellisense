"""
Type annotations for osis service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_osis/type_defs.html)

Usage::

    ```python
    from mypy_boto3_osis.type_defs import ChangeProgressStageTypeDef

    data: ChangeProgressStageTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ChangeProgressStageStatusesType,
    ChangeProgressStatusesType,
    PipelineStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ChangeProgressStageTypeDef",
    "ChangeProgressStatusTypeDef",
    "CloudWatchLogDestinationTypeDef",
    "CreatePipelineRequestRequestTypeDef",
    "CreatePipelineResponseTypeDef",
    "DeletePipelineRequestRequestTypeDef",
    "GetPipelineBlueprintRequestRequestTypeDef",
    "GetPipelineBlueprintResponseTypeDef",
    "GetPipelineChangeProgressRequestRequestTypeDef",
    "GetPipelineChangeProgressResponseTypeDef",
    "GetPipelineRequestRequestTypeDef",
    "GetPipelineResponseTypeDef",
    "ListPipelineBlueprintsResponseTypeDef",
    "ListPipelinesRequestRequestTypeDef",
    "ListPipelinesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LogPublishingOptionsTypeDef",
    "PipelineBlueprintSummaryTypeDef",
    "PipelineBlueprintTypeDef",
    "PipelineStatusReasonTypeDef",
    "PipelineSummaryTypeDef",
    "PipelineTypeDef",
    "ResponseMetadataTypeDef",
    "StartPipelineRequestRequestTypeDef",
    "StartPipelineResponseTypeDef",
    "StopPipelineRequestRequestTypeDef",
    "StopPipelineResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdatePipelineRequestRequestTypeDef",
    "UpdatePipelineResponseTypeDef",
    "ValidatePipelineRequestRequestTypeDef",
    "ValidatePipelineResponseTypeDef",
    "ValidationMessageTypeDef",
    "VpcEndpointTypeDef",
    "VpcOptionsTypeDef",
)

ChangeProgressStageTypeDef = TypedDict(
    "ChangeProgressStageTypeDef",
    {
        "Name": str,
        "Status": ChangeProgressStageStatusesType,
        "Description": str,
        "LastUpdatedAt": datetime,
    },
    total=False,
)

ChangeProgressStatusTypeDef = TypedDict(
    "ChangeProgressStatusTypeDef",
    {
        "StartTime": datetime,
        "Status": ChangeProgressStatusesType,
        "TotalNumberOfStages": int,
        "ChangeProgressStages": List["ChangeProgressStageTypeDef"],
    },
    total=False,
)

CloudWatchLogDestinationTypeDef = TypedDict(
    "CloudWatchLogDestinationTypeDef",
    {
        "LogGroup": str,
    },
)

_RequiredCreatePipelineRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePipelineRequestRequestTypeDef",
    {
        "PipelineName": str,
        "MinUnits": int,
        "MaxUnits": int,
        "PipelineConfigurationBody": str,
    },
)
_OptionalCreatePipelineRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePipelineRequestRequestTypeDef",
    {
        "LogPublishingOptions": "LogPublishingOptionsTypeDef",
        "VpcOptions": "VpcOptionsTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreatePipelineRequestRequestTypeDef(
    _RequiredCreatePipelineRequestRequestTypeDef, _OptionalCreatePipelineRequestRequestTypeDef
):
    pass

CreatePipelineResponseTypeDef = TypedDict(
    "CreatePipelineResponseTypeDef",
    {
        "Pipeline": "PipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePipelineRequestRequestTypeDef = TypedDict(
    "DeletePipelineRequestRequestTypeDef",
    {
        "PipelineName": str,
    },
)

GetPipelineBlueprintRequestRequestTypeDef = TypedDict(
    "GetPipelineBlueprintRequestRequestTypeDef",
    {
        "BlueprintName": str,
    },
)

GetPipelineBlueprintResponseTypeDef = TypedDict(
    "GetPipelineBlueprintResponseTypeDef",
    {
        "Blueprint": "PipelineBlueprintTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPipelineChangeProgressRequestRequestTypeDef = TypedDict(
    "GetPipelineChangeProgressRequestRequestTypeDef",
    {
        "PipelineName": str,
    },
)

GetPipelineChangeProgressResponseTypeDef = TypedDict(
    "GetPipelineChangeProgressResponseTypeDef",
    {
        "ChangeProgressStatuses": List["ChangeProgressStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPipelineRequestRequestTypeDef = TypedDict(
    "GetPipelineRequestRequestTypeDef",
    {
        "PipelineName": str,
    },
)

GetPipelineResponseTypeDef = TypedDict(
    "GetPipelineResponseTypeDef",
    {
        "Pipeline": "PipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPipelineBlueprintsResponseTypeDef = TypedDict(
    "ListPipelineBlueprintsResponseTypeDef",
    {
        "Blueprints": List["PipelineBlueprintSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPipelinesRequestRequestTypeDef = TypedDict(
    "ListPipelinesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListPipelinesResponseTypeDef = TypedDict(
    "ListPipelinesResponseTypeDef",
    {
        "NextToken": str,
        "Pipelines": List["PipelineSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "Arn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogPublishingOptionsTypeDef = TypedDict(
    "LogPublishingOptionsTypeDef",
    {
        "IsLoggingEnabled": bool,
        "CloudWatchLogDestination": "CloudWatchLogDestinationTypeDef",
    },
    total=False,
)

PipelineBlueprintSummaryTypeDef = TypedDict(
    "PipelineBlueprintSummaryTypeDef",
    {
        "BlueprintName": str,
    },
    total=False,
)

PipelineBlueprintTypeDef = TypedDict(
    "PipelineBlueprintTypeDef",
    {
        "BlueprintName": str,
        "PipelineConfigurationBody": str,
    },
    total=False,
)

PipelineStatusReasonTypeDef = TypedDict(
    "PipelineStatusReasonTypeDef",
    {
        "Description": str,
    },
    total=False,
)

PipelineSummaryTypeDef = TypedDict(
    "PipelineSummaryTypeDef",
    {
        "Status": PipelineStatusType,
        "StatusReason": "PipelineStatusReasonTypeDef",
        "PipelineName": str,
        "PipelineArn": str,
        "MinUnits": int,
        "MaxUnits": int,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
    total=False,
)

PipelineTypeDef = TypedDict(
    "PipelineTypeDef",
    {
        "PipelineName": str,
        "PipelineArn": str,
        "MinUnits": int,
        "MaxUnits": int,
        "Status": PipelineStatusType,
        "StatusReason": "PipelineStatusReasonTypeDef",
        "PipelineConfigurationBody": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "IngestEndpointUrls": List[str],
        "LogPublishingOptions": "LogPublishingOptionsTypeDef",
        "VpcEndpoints": List["VpcEndpointTypeDef"],
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

StartPipelineRequestRequestTypeDef = TypedDict(
    "StartPipelineRequestRequestTypeDef",
    {
        "PipelineName": str,
    },
)

StartPipelineResponseTypeDef = TypedDict(
    "StartPipelineResponseTypeDef",
    {
        "Pipeline": "PipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopPipelineRequestRequestTypeDef = TypedDict(
    "StopPipelineRequestRequestTypeDef",
    {
        "PipelineName": str,
    },
)

StopPipelineResponseTypeDef = TypedDict(
    "StopPipelineResponseTypeDef",
    {
        "Pipeline": "PipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "Arn": str,
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
        "Arn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdatePipelineRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePipelineRequestRequestTypeDef",
    {
        "PipelineName": str,
    },
)
_OptionalUpdatePipelineRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePipelineRequestRequestTypeDef",
    {
        "MinUnits": int,
        "MaxUnits": int,
        "PipelineConfigurationBody": str,
        "LogPublishingOptions": "LogPublishingOptionsTypeDef",
    },
    total=False,
)

class UpdatePipelineRequestRequestTypeDef(
    _RequiredUpdatePipelineRequestRequestTypeDef, _OptionalUpdatePipelineRequestRequestTypeDef
):
    pass

UpdatePipelineResponseTypeDef = TypedDict(
    "UpdatePipelineResponseTypeDef",
    {
        "Pipeline": "PipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValidatePipelineRequestRequestTypeDef = TypedDict(
    "ValidatePipelineRequestRequestTypeDef",
    {
        "PipelineConfigurationBody": str,
    },
)

ValidatePipelineResponseTypeDef = TypedDict(
    "ValidatePipelineResponseTypeDef",
    {
        "isValid": bool,
        "Errors": List["ValidationMessageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValidationMessageTypeDef = TypedDict(
    "ValidationMessageTypeDef",
    {
        "Message": str,
    },
    total=False,
)

VpcEndpointTypeDef = TypedDict(
    "VpcEndpointTypeDef",
    {
        "VpcEndpointId": str,
        "VpcId": str,
        "VpcOptions": "VpcOptionsTypeDef",
    },
    total=False,
)

_RequiredVpcOptionsTypeDef = TypedDict(
    "_RequiredVpcOptionsTypeDef",
    {
        "SubnetIds": List[str],
    },
)
_OptionalVpcOptionsTypeDef = TypedDict(
    "_OptionalVpcOptionsTypeDef",
    {
        "SecurityGroupIds": List[str],
    },
    total=False,
)

class VpcOptionsTypeDef(_RequiredVpcOptionsTypeDef, _OptionalVpcOptionsTypeDef):
    pass
