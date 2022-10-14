"""
Type annotations for emr-serverless service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/type_defs.html)

Usage::

    ```python
    from mypy_boto3_emr_serverless.type_defs import ApplicationSummaryTypeDef

    data: ApplicationSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import ApplicationStateType, JobRunStateType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ApplicationSummaryTypeDef",
    "ApplicationTypeDef",
    "AutoStartConfigTypeDef",
    "AutoStopConfigTypeDef",
    "CancelJobRunRequestRequestTypeDef",
    "CancelJobRunResponseTypeDef",
    "ConfigurationOverridesTypeDef",
    "ConfigurationTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "GetApplicationRequestRequestTypeDef",
    "GetApplicationResponseTypeDef",
    "GetDashboardForJobRunRequestRequestTypeDef",
    "GetDashboardForJobRunResponseTypeDef",
    "GetJobRunRequestRequestTypeDef",
    "GetJobRunResponseTypeDef",
    "HiveTypeDef",
    "InitialCapacityConfigTypeDef",
    "JobDriverTypeDef",
    "JobRunSummaryTypeDef",
    "JobRunTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListJobRunsRequestRequestTypeDef",
    "ListJobRunsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ManagedPersistenceMonitoringConfigurationTypeDef",
    "MaximumAllowedResourcesTypeDef",
    "MonitoringConfigurationTypeDef",
    "NetworkConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "S3MonitoringConfigurationTypeDef",
    "SparkSubmitTypeDef",
    "StartApplicationRequestRequestTypeDef",
    "StartJobRunRequestRequestTypeDef",
    "StartJobRunResponseTypeDef",
    "StopApplicationRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TotalResourceUtilizationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "UpdateApplicationResponseTypeDef",
    "WorkerResourceConfigTypeDef",
)

_RequiredApplicationSummaryTypeDef = TypedDict(
    "_RequiredApplicationSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "releaseLabel": str,
        "type": str,
        "state": ApplicationStateType,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
)
_OptionalApplicationSummaryTypeDef = TypedDict(
    "_OptionalApplicationSummaryTypeDef",
    {
        "name": str,
        "stateDetails": str,
    },
    total=False,
)

class ApplicationSummaryTypeDef(
    _RequiredApplicationSummaryTypeDef, _OptionalApplicationSummaryTypeDef
):
    pass

_RequiredApplicationTypeDef = TypedDict(
    "_RequiredApplicationTypeDef",
    {
        "applicationId": str,
        "arn": str,
        "releaseLabel": str,
        "type": str,
        "state": ApplicationStateType,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
)
_OptionalApplicationTypeDef = TypedDict(
    "_OptionalApplicationTypeDef",
    {
        "name": str,
        "stateDetails": str,
        "initialCapacity": Dict[str, "InitialCapacityConfigTypeDef"],
        "maximumCapacity": "MaximumAllowedResourcesTypeDef",
        "tags": Dict[str, str],
        "autoStartConfiguration": "AutoStartConfigTypeDef",
        "autoStopConfiguration": "AutoStopConfigTypeDef",
        "networkConfiguration": "NetworkConfigurationTypeDef",
    },
    total=False,
)

class ApplicationTypeDef(_RequiredApplicationTypeDef, _OptionalApplicationTypeDef):
    pass

AutoStartConfigTypeDef = TypedDict(
    "AutoStartConfigTypeDef",
    {
        "enabled": bool,
    },
    total=False,
)

AutoStopConfigTypeDef = TypedDict(
    "AutoStopConfigTypeDef",
    {
        "enabled": bool,
        "idleTimeoutMinutes": int,
    },
    total=False,
)

CancelJobRunRequestRequestTypeDef = TypedDict(
    "CancelJobRunRequestRequestTypeDef",
    {
        "applicationId": str,
        "jobRunId": str,
    },
)

CancelJobRunResponseTypeDef = TypedDict(
    "CancelJobRunResponseTypeDef",
    {
        "applicationId": str,
        "jobRunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfigurationOverridesTypeDef = TypedDict(
    "ConfigurationOverridesTypeDef",
    {
        "applicationConfiguration": List["ConfigurationTypeDef"],
        "monitoringConfiguration": "MonitoringConfigurationTypeDef",
    },
    total=False,
)

_RequiredConfigurationTypeDef = TypedDict(
    "_RequiredConfigurationTypeDef",
    {
        "classification": str,
    },
)
_OptionalConfigurationTypeDef = TypedDict(
    "_OptionalConfigurationTypeDef",
    {
        "properties": Dict[str, str],
        "configurations": List[Dict[str, Any]],
    },
    total=False,
)

class ConfigurationTypeDef(_RequiredConfigurationTypeDef, _OptionalConfigurationTypeDef):
    pass

_RequiredCreateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestRequestTypeDef",
    {
        "releaseLabel": str,
        "type": str,
        "clientToken": str,
    },
)
_OptionalCreateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestRequestTypeDef",
    {
        "name": str,
        "initialCapacity": Dict[str, "InitialCapacityConfigTypeDef"],
        "maximumCapacity": "MaximumAllowedResourcesTypeDef",
        "tags": Dict[str, str],
        "autoStartConfiguration": "AutoStartConfigTypeDef",
        "autoStopConfiguration": "AutoStopConfigTypeDef",
        "networkConfiguration": "NetworkConfigurationTypeDef",
    },
    total=False,
)

class CreateApplicationRequestRequestTypeDef(
    _RequiredCreateApplicationRequestRequestTypeDef, _OptionalCreateApplicationRequestRequestTypeDef
):
    pass

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "applicationId": str,
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)

GetApplicationRequestRequestTypeDef = TypedDict(
    "GetApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)

GetApplicationResponseTypeDef = TypedDict(
    "GetApplicationResponseTypeDef",
    {
        "application": "ApplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDashboardForJobRunRequestRequestTypeDef = TypedDict(
    "GetDashboardForJobRunRequestRequestTypeDef",
    {
        "applicationId": str,
        "jobRunId": str,
    },
)

GetDashboardForJobRunResponseTypeDef = TypedDict(
    "GetDashboardForJobRunResponseTypeDef",
    {
        "url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobRunRequestRequestTypeDef = TypedDict(
    "GetJobRunRequestRequestTypeDef",
    {
        "applicationId": str,
        "jobRunId": str,
    },
)

GetJobRunResponseTypeDef = TypedDict(
    "GetJobRunResponseTypeDef",
    {
        "jobRun": "JobRunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredHiveTypeDef = TypedDict(
    "_RequiredHiveTypeDef",
    {
        "query": str,
    },
)
_OptionalHiveTypeDef = TypedDict(
    "_OptionalHiveTypeDef",
    {
        "initQueryFile": str,
        "parameters": str,
    },
    total=False,
)

class HiveTypeDef(_RequiredHiveTypeDef, _OptionalHiveTypeDef):
    pass

_RequiredInitialCapacityConfigTypeDef = TypedDict(
    "_RequiredInitialCapacityConfigTypeDef",
    {
        "workerCount": int,
    },
)
_OptionalInitialCapacityConfigTypeDef = TypedDict(
    "_OptionalInitialCapacityConfigTypeDef",
    {
        "workerConfiguration": "WorkerResourceConfigTypeDef",
    },
    total=False,
)

class InitialCapacityConfigTypeDef(
    _RequiredInitialCapacityConfigTypeDef, _OptionalInitialCapacityConfigTypeDef
):
    pass

JobDriverTypeDef = TypedDict(
    "JobDriverTypeDef",
    {
        "sparkSubmit": "SparkSubmitTypeDef",
        "hive": "HiveTypeDef",
    },
    total=False,
)

_RequiredJobRunSummaryTypeDef = TypedDict(
    "_RequiredJobRunSummaryTypeDef",
    {
        "applicationId": str,
        "id": str,
        "arn": str,
        "createdBy": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "executionRole": str,
        "state": JobRunStateType,
        "stateDetails": str,
        "releaseLabel": str,
    },
)
_OptionalJobRunSummaryTypeDef = TypedDict(
    "_OptionalJobRunSummaryTypeDef",
    {
        "name": str,
        "type": str,
    },
    total=False,
)

class JobRunSummaryTypeDef(_RequiredJobRunSummaryTypeDef, _OptionalJobRunSummaryTypeDef):
    pass

_RequiredJobRunTypeDef = TypedDict(
    "_RequiredJobRunTypeDef",
    {
        "applicationId": str,
        "jobRunId": str,
        "arn": str,
        "createdBy": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "executionRole": str,
        "state": JobRunStateType,
        "stateDetails": str,
        "releaseLabel": str,
        "jobDriver": "JobDriverTypeDef",
    },
)
_OptionalJobRunTypeDef = TypedDict(
    "_OptionalJobRunTypeDef",
    {
        "name": str,
        "configurationOverrides": "ConfigurationOverridesTypeDef",
        "tags": Dict[str, str],
        "totalResourceUtilization": "TotalResourceUtilizationTypeDef",
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "totalExecutionDurationSeconds": int,
    },
    total=False,
)

class JobRunTypeDef(_RequiredJobRunTypeDef, _OptionalJobRunTypeDef):
    pass

ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "states": List[ApplicationStateType],
    },
    total=False,
)

ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "applications": List["ApplicationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListJobRunsRequestRequestTypeDef = TypedDict(
    "_RequiredListJobRunsRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
_OptionalListJobRunsRequestRequestTypeDef = TypedDict(
    "_OptionalListJobRunsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "createdAtAfter": Union[datetime, str],
        "createdAtBefore": Union[datetime, str],
        "states": List[JobRunStateType],
    },
    total=False,
)

class ListJobRunsRequestRequestTypeDef(
    _RequiredListJobRunsRequestRequestTypeDef, _OptionalListJobRunsRequestRequestTypeDef
):
    pass

ListJobRunsResponseTypeDef = TypedDict(
    "ListJobRunsResponseTypeDef",
    {
        "jobRuns": List["JobRunSummaryTypeDef"],
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
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ManagedPersistenceMonitoringConfigurationTypeDef = TypedDict(
    "ManagedPersistenceMonitoringConfigurationTypeDef",
    {
        "enabled": bool,
        "encryptionKeyArn": str,
    },
    total=False,
)

_RequiredMaximumAllowedResourcesTypeDef = TypedDict(
    "_RequiredMaximumAllowedResourcesTypeDef",
    {
        "cpu": str,
        "memory": str,
    },
)
_OptionalMaximumAllowedResourcesTypeDef = TypedDict(
    "_OptionalMaximumAllowedResourcesTypeDef",
    {
        "disk": str,
    },
    total=False,
)

class MaximumAllowedResourcesTypeDef(
    _RequiredMaximumAllowedResourcesTypeDef, _OptionalMaximumAllowedResourcesTypeDef
):
    pass

MonitoringConfigurationTypeDef = TypedDict(
    "MonitoringConfigurationTypeDef",
    {
        "s3MonitoringConfiguration": "S3MonitoringConfigurationTypeDef",
        "managedPersistenceMonitoringConfiguration": "ManagedPersistenceMonitoringConfigurationTypeDef",
    },
    total=False,
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
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

S3MonitoringConfigurationTypeDef = TypedDict(
    "S3MonitoringConfigurationTypeDef",
    {
        "logUri": str,
        "encryptionKeyArn": str,
    },
    total=False,
)

_RequiredSparkSubmitTypeDef = TypedDict(
    "_RequiredSparkSubmitTypeDef",
    {
        "entryPoint": str,
    },
)
_OptionalSparkSubmitTypeDef = TypedDict(
    "_OptionalSparkSubmitTypeDef",
    {
        "entryPointArguments": List[str],
        "sparkSubmitParameters": str,
    },
    total=False,
)

class SparkSubmitTypeDef(_RequiredSparkSubmitTypeDef, _OptionalSparkSubmitTypeDef):
    pass

StartApplicationRequestRequestTypeDef = TypedDict(
    "StartApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)

_RequiredStartJobRunRequestRequestTypeDef = TypedDict(
    "_RequiredStartJobRunRequestRequestTypeDef",
    {
        "applicationId": str,
        "clientToken": str,
        "executionRoleArn": str,
    },
)
_OptionalStartJobRunRequestRequestTypeDef = TypedDict(
    "_OptionalStartJobRunRequestRequestTypeDef",
    {
        "jobDriver": "JobDriverTypeDef",
        "configurationOverrides": "ConfigurationOverridesTypeDef",
        "tags": Dict[str, str],
        "executionTimeoutMinutes": int,
        "name": str,
    },
    total=False,
)

class StartJobRunRequestRequestTypeDef(
    _RequiredStartJobRunRequestRequestTypeDef, _OptionalStartJobRunRequestRequestTypeDef
):
    pass

StartJobRunResponseTypeDef = TypedDict(
    "StartJobRunResponseTypeDef",
    {
        "applicationId": str,
        "jobRunId": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopApplicationRequestRequestTypeDef = TypedDict(
    "StopApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TotalResourceUtilizationTypeDef = TypedDict(
    "TotalResourceUtilizationTypeDef",
    {
        "vCPUHour": float,
        "memoryGBHour": float,
        "storageGBHour": float,
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

_RequiredUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
        "clientToken": str,
    },
)
_OptionalUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationRequestRequestTypeDef",
    {
        "initialCapacity": Dict[str, "InitialCapacityConfigTypeDef"],
        "maximumCapacity": "MaximumAllowedResourcesTypeDef",
        "autoStartConfiguration": "AutoStartConfigTypeDef",
        "autoStopConfiguration": "AutoStopConfigTypeDef",
        "networkConfiguration": "NetworkConfigurationTypeDef",
    },
    total=False,
)

class UpdateApplicationRequestRequestTypeDef(
    _RequiredUpdateApplicationRequestRequestTypeDef, _OptionalUpdateApplicationRequestRequestTypeDef
):
    pass

UpdateApplicationResponseTypeDef = TypedDict(
    "UpdateApplicationResponseTypeDef",
    {
        "application": "ApplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredWorkerResourceConfigTypeDef = TypedDict(
    "_RequiredWorkerResourceConfigTypeDef",
    {
        "cpu": str,
        "memory": str,
    },
)
_OptionalWorkerResourceConfigTypeDef = TypedDict(
    "_OptionalWorkerResourceConfigTypeDef",
    {
        "disk": str,
    },
    total=False,
)

class WorkerResourceConfigTypeDef(
    _RequiredWorkerResourceConfigTypeDef, _OptionalWorkerResourceConfigTypeDef
):
    pass
