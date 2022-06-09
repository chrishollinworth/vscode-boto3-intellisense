"""
Type annotations for braket service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/type_defs.html)

Usage::

    ```python
    from mypy_boto3_braket.type_defs import AlgorithmSpecificationTypeDef

    data: AlgorithmSpecificationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    CancellationStatusType,
    CompressionTypeType,
    DeviceStatusType,
    DeviceTypeType,
    InstanceTypeType,
    JobEventTypeType,
    JobPrimaryStatusType,
    QuantumTaskStatusType,
    SearchJobsFilterOperatorType,
    SearchQuantumTasksFilterOperatorType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AlgorithmSpecificationTypeDef",
    "CancelJobRequestRequestTypeDef",
    "CancelJobResponseTypeDef",
    "CancelQuantumTaskRequestRequestTypeDef",
    "CancelQuantumTaskResponseTypeDef",
    "ContainerImageTypeDef",
    "CreateJobRequestRequestTypeDef",
    "CreateJobResponseTypeDef",
    "CreateQuantumTaskRequestRequestTypeDef",
    "CreateQuantumTaskResponseTypeDef",
    "DataSourceTypeDef",
    "DeviceConfigTypeDef",
    "DeviceSummaryTypeDef",
    "GetDeviceRequestRequestTypeDef",
    "GetDeviceResponseTypeDef",
    "GetJobRequestRequestTypeDef",
    "GetJobResponseTypeDef",
    "GetQuantumTaskRequestRequestTypeDef",
    "GetQuantumTaskResponseTypeDef",
    "InputFileConfigTypeDef",
    "InstanceConfigTypeDef",
    "JobCheckpointConfigTypeDef",
    "JobEventDetailsTypeDef",
    "JobOutputDataConfigTypeDef",
    "JobStoppingConditionTypeDef",
    "JobSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "QuantumTaskSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "S3DataSourceTypeDef",
    "ScriptModeConfigTypeDef",
    "SearchDevicesFilterTypeDef",
    "SearchDevicesRequestRequestTypeDef",
    "SearchDevicesResponseTypeDef",
    "SearchJobsFilterTypeDef",
    "SearchJobsRequestRequestTypeDef",
    "SearchJobsResponseTypeDef",
    "SearchQuantumTasksFilterTypeDef",
    "SearchQuantumTasksRequestRequestTypeDef",
    "SearchQuantumTasksResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
)

AlgorithmSpecificationTypeDef = TypedDict(
    "AlgorithmSpecificationTypeDef",
    {
        "containerImage": "ContainerImageTypeDef",
        "scriptModeConfig": "ScriptModeConfigTypeDef",
    },
    total=False,
)

CancelJobRequestRequestTypeDef = TypedDict(
    "CancelJobRequestRequestTypeDef",
    {
        "jobArn": str,
    },
)

CancelJobResponseTypeDef = TypedDict(
    "CancelJobResponseTypeDef",
    {
        "cancellationStatus": CancellationStatusType,
        "jobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelQuantumTaskRequestRequestTypeDef = TypedDict(
    "CancelQuantumTaskRequestRequestTypeDef",
    {
        "clientToken": str,
        "quantumTaskArn": str,
    },
)

CancelQuantumTaskResponseTypeDef = TypedDict(
    "CancelQuantumTaskResponseTypeDef",
    {
        "cancellationStatus": CancellationStatusType,
        "quantumTaskArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ContainerImageTypeDef = TypedDict(
    "ContainerImageTypeDef",
    {
        "uri": str,
    },
)

_RequiredCreateJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateJobRequestRequestTypeDef",
    {
        "algorithmSpecification": "AlgorithmSpecificationTypeDef",
        "clientToken": str,
        "deviceConfig": "DeviceConfigTypeDef",
        "instanceConfig": "InstanceConfigTypeDef",
        "jobName": str,
        "outputDataConfig": "JobOutputDataConfigTypeDef",
        "roleArn": str,
    },
)
_OptionalCreateJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateJobRequestRequestTypeDef",
    {
        "checkpointConfig": "JobCheckpointConfigTypeDef",
        "hyperParameters": Dict[str, str],
        "inputDataConfig": List["InputFileConfigTypeDef"],
        "stoppingCondition": "JobStoppingConditionTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateJobRequestRequestTypeDef(
    _RequiredCreateJobRequestRequestTypeDef, _OptionalCreateJobRequestRequestTypeDef
):
    pass

CreateJobResponseTypeDef = TypedDict(
    "CreateJobResponseTypeDef",
    {
        "jobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateQuantumTaskRequestRequestTypeDef = TypedDict(
    "_RequiredCreateQuantumTaskRequestRequestTypeDef",
    {
        "action": str,
        "clientToken": str,
        "deviceArn": str,
        "outputS3Bucket": str,
        "outputS3KeyPrefix": str,
        "shots": int,
    },
)
_OptionalCreateQuantumTaskRequestRequestTypeDef = TypedDict(
    "_OptionalCreateQuantumTaskRequestRequestTypeDef",
    {
        "deviceParameters": str,
        "jobToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateQuantumTaskRequestRequestTypeDef(
    _RequiredCreateQuantumTaskRequestRequestTypeDef, _OptionalCreateQuantumTaskRequestRequestTypeDef
):
    pass

CreateQuantumTaskResponseTypeDef = TypedDict(
    "CreateQuantumTaskResponseTypeDef",
    {
        "quantumTaskArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "s3DataSource": "S3DataSourceTypeDef",
    },
)

DeviceConfigTypeDef = TypedDict(
    "DeviceConfigTypeDef",
    {
        "device": str,
    },
)

DeviceSummaryTypeDef = TypedDict(
    "DeviceSummaryTypeDef",
    {
        "deviceArn": str,
        "deviceName": str,
        "deviceStatus": DeviceStatusType,
        "deviceType": DeviceTypeType,
        "providerName": str,
    },
)

GetDeviceRequestRequestTypeDef = TypedDict(
    "GetDeviceRequestRequestTypeDef",
    {
        "deviceArn": str,
    },
)

GetDeviceResponseTypeDef = TypedDict(
    "GetDeviceResponseTypeDef",
    {
        "deviceArn": str,
        "deviceCapabilities": str,
        "deviceName": str,
        "deviceStatus": DeviceStatusType,
        "deviceType": DeviceTypeType,
        "providerName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobRequestRequestTypeDef = TypedDict(
    "GetJobRequestRequestTypeDef",
    {
        "jobArn": str,
    },
)

GetJobResponseTypeDef = TypedDict(
    "GetJobResponseTypeDef",
    {
        "algorithmSpecification": "AlgorithmSpecificationTypeDef",
        "billableDuration": int,
        "checkpointConfig": "JobCheckpointConfigTypeDef",
        "createdAt": datetime,
        "deviceConfig": "DeviceConfigTypeDef",
        "endedAt": datetime,
        "events": List["JobEventDetailsTypeDef"],
        "failureReason": str,
        "hyperParameters": Dict[str, str],
        "inputDataConfig": List["InputFileConfigTypeDef"],
        "instanceConfig": "InstanceConfigTypeDef",
        "jobArn": str,
        "jobName": str,
        "outputDataConfig": "JobOutputDataConfigTypeDef",
        "roleArn": str,
        "startedAt": datetime,
        "status": JobPrimaryStatusType,
        "stoppingCondition": "JobStoppingConditionTypeDef",
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQuantumTaskRequestRequestTypeDef = TypedDict(
    "GetQuantumTaskRequestRequestTypeDef",
    {
        "quantumTaskArn": str,
    },
)

GetQuantumTaskResponseTypeDef = TypedDict(
    "GetQuantumTaskResponseTypeDef",
    {
        "createdAt": datetime,
        "deviceArn": str,
        "deviceParameters": str,
        "endedAt": datetime,
        "failureReason": str,
        "jobArn": str,
        "outputS3Bucket": str,
        "outputS3Directory": str,
        "quantumTaskArn": str,
        "shots": int,
        "status": QuantumTaskStatusType,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredInputFileConfigTypeDef = TypedDict(
    "_RequiredInputFileConfigTypeDef",
    {
        "channelName": str,
        "dataSource": "DataSourceTypeDef",
    },
)
_OptionalInputFileConfigTypeDef = TypedDict(
    "_OptionalInputFileConfigTypeDef",
    {
        "contentType": str,
    },
    total=False,
)

class InputFileConfigTypeDef(_RequiredInputFileConfigTypeDef, _OptionalInputFileConfigTypeDef):
    pass

_RequiredInstanceConfigTypeDef = TypedDict(
    "_RequiredInstanceConfigTypeDef",
    {
        "instanceType": InstanceTypeType,
        "volumeSizeInGb": int,
    },
)
_OptionalInstanceConfigTypeDef = TypedDict(
    "_OptionalInstanceConfigTypeDef",
    {
        "instanceCount": int,
    },
    total=False,
)

class InstanceConfigTypeDef(_RequiredInstanceConfigTypeDef, _OptionalInstanceConfigTypeDef):
    pass

_RequiredJobCheckpointConfigTypeDef = TypedDict(
    "_RequiredJobCheckpointConfigTypeDef",
    {
        "s3Uri": str,
    },
)
_OptionalJobCheckpointConfigTypeDef = TypedDict(
    "_OptionalJobCheckpointConfigTypeDef",
    {
        "localPath": str,
    },
    total=False,
)

class JobCheckpointConfigTypeDef(
    _RequiredJobCheckpointConfigTypeDef, _OptionalJobCheckpointConfigTypeDef
):
    pass

JobEventDetailsTypeDef = TypedDict(
    "JobEventDetailsTypeDef",
    {
        "eventType": JobEventTypeType,
        "message": str,
        "timeOfEvent": datetime,
    },
    total=False,
)

_RequiredJobOutputDataConfigTypeDef = TypedDict(
    "_RequiredJobOutputDataConfigTypeDef",
    {
        "s3Path": str,
    },
)
_OptionalJobOutputDataConfigTypeDef = TypedDict(
    "_OptionalJobOutputDataConfigTypeDef",
    {
        "kmsKeyId": str,
    },
    total=False,
)

class JobOutputDataConfigTypeDef(
    _RequiredJobOutputDataConfigTypeDef, _OptionalJobOutputDataConfigTypeDef
):
    pass

JobStoppingConditionTypeDef = TypedDict(
    "JobStoppingConditionTypeDef",
    {
        "maxRuntimeInSeconds": int,
    },
    total=False,
)

_RequiredJobSummaryTypeDef = TypedDict(
    "_RequiredJobSummaryTypeDef",
    {
        "createdAt": datetime,
        "device": str,
        "jobArn": str,
        "jobName": str,
        "status": JobPrimaryStatusType,
    },
)
_OptionalJobSummaryTypeDef = TypedDict(
    "_OptionalJobSummaryTypeDef",
    {
        "endedAt": datetime,
        "startedAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

class JobSummaryTypeDef(_RequiredJobSummaryTypeDef, _OptionalJobSummaryTypeDef):
    pass

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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredQuantumTaskSummaryTypeDef = TypedDict(
    "_RequiredQuantumTaskSummaryTypeDef",
    {
        "createdAt": datetime,
        "deviceArn": str,
        "outputS3Bucket": str,
        "outputS3Directory": str,
        "quantumTaskArn": str,
        "shots": int,
        "status": QuantumTaskStatusType,
    },
)
_OptionalQuantumTaskSummaryTypeDef = TypedDict(
    "_OptionalQuantumTaskSummaryTypeDef",
    {
        "endedAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

class QuantumTaskSummaryTypeDef(
    _RequiredQuantumTaskSummaryTypeDef, _OptionalQuantumTaskSummaryTypeDef
):
    pass

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

S3DataSourceTypeDef = TypedDict(
    "S3DataSourceTypeDef",
    {
        "s3Uri": str,
    },
)

_RequiredScriptModeConfigTypeDef = TypedDict(
    "_RequiredScriptModeConfigTypeDef",
    {
        "entryPoint": str,
        "s3Uri": str,
    },
)
_OptionalScriptModeConfigTypeDef = TypedDict(
    "_OptionalScriptModeConfigTypeDef",
    {
        "compressionType": CompressionTypeType,
    },
    total=False,
)

class ScriptModeConfigTypeDef(_RequiredScriptModeConfigTypeDef, _OptionalScriptModeConfigTypeDef):
    pass

SearchDevicesFilterTypeDef = TypedDict(
    "SearchDevicesFilterTypeDef",
    {
        "name": str,
        "values": List[str],
    },
)

_RequiredSearchDevicesRequestRequestTypeDef = TypedDict(
    "_RequiredSearchDevicesRequestRequestTypeDef",
    {
        "filters": List["SearchDevicesFilterTypeDef"],
    },
)
_OptionalSearchDevicesRequestRequestTypeDef = TypedDict(
    "_OptionalSearchDevicesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class SearchDevicesRequestRequestTypeDef(
    _RequiredSearchDevicesRequestRequestTypeDef, _OptionalSearchDevicesRequestRequestTypeDef
):
    pass

SearchDevicesResponseTypeDef = TypedDict(
    "SearchDevicesResponseTypeDef",
    {
        "devices": List["DeviceSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchJobsFilterTypeDef = TypedDict(
    "SearchJobsFilterTypeDef",
    {
        "name": str,
        "operator": SearchJobsFilterOperatorType,
        "values": List[str],
    },
)

_RequiredSearchJobsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchJobsRequestRequestTypeDef",
    {
        "filters": List["SearchJobsFilterTypeDef"],
    },
)
_OptionalSearchJobsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchJobsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class SearchJobsRequestRequestTypeDef(
    _RequiredSearchJobsRequestRequestTypeDef, _OptionalSearchJobsRequestRequestTypeDef
):
    pass

SearchJobsResponseTypeDef = TypedDict(
    "SearchJobsResponseTypeDef",
    {
        "jobs": List["JobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchQuantumTasksFilterTypeDef = TypedDict(
    "SearchQuantumTasksFilterTypeDef",
    {
        "name": str,
        "operator": SearchQuantumTasksFilterOperatorType,
        "values": List[str],
    },
)

_RequiredSearchQuantumTasksRequestRequestTypeDef = TypedDict(
    "_RequiredSearchQuantumTasksRequestRequestTypeDef",
    {
        "filters": List["SearchQuantumTasksFilterTypeDef"],
    },
)
_OptionalSearchQuantumTasksRequestRequestTypeDef = TypedDict(
    "_OptionalSearchQuantumTasksRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class SearchQuantumTasksRequestRequestTypeDef(
    _RequiredSearchQuantumTasksRequestRequestTypeDef,
    _OptionalSearchQuantumTasksRequestRequestTypeDef,
):
    pass

SearchQuantumTasksResponseTypeDef = TypedDict(
    "SearchQuantumTasksResponseTypeDef",
    {
        "nextToken": str,
        "quantumTasks": List["QuantumTaskSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)
