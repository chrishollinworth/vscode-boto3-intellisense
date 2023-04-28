"""
Type annotations for m2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_m2.type_defs import AlternateKeyTypeDef

    data: AlternateKeyTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ApplicationDeploymentLifecycleType,
    ApplicationLifecycleType,
    ApplicationVersionLifecycleType,
    BatchJobExecutionStatusType,
    BatchJobTypeType,
    DataSetTaskLifecycleType,
    DeploymentLifecycleType,
    EngineTypeType,
    EnvironmentLifecycleType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AlternateKeyTypeDef",
    "ApplicationSummaryTypeDef",
    "ApplicationVersionSummaryTypeDef",
    "BatchJobDefinitionTypeDef",
    "BatchJobExecutionSummaryTypeDef",
    "BatchJobIdentifierTypeDef",
    "CancelBatchJobExecutionRequestRequestTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateDataSetImportTaskRequestRequestTypeDef",
    "CreateDataSetImportTaskResponseTypeDef",
    "CreateDeploymentRequestRequestTypeDef",
    "CreateDeploymentResponseTypeDef",
    "CreateEnvironmentRequestRequestTypeDef",
    "CreateEnvironmentResponseTypeDef",
    "DataSetImportConfigTypeDef",
    "DataSetImportItemTypeDef",
    "DataSetImportSummaryTypeDef",
    "DataSetImportTaskTypeDef",
    "DataSetSummaryTypeDef",
    "DataSetTypeDef",
    "DatasetDetailOrgAttributesTypeDef",
    "DatasetOrgAttributesTypeDef",
    "DefinitionTypeDef",
    "DeleteApplicationFromEnvironmentRequestRequestTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteEnvironmentRequestRequestTypeDef",
    "DeployedVersionSummaryTypeDef",
    "DeploymentSummaryTypeDef",
    "EfsStorageConfigurationTypeDef",
    "EngineVersionsSummaryTypeDef",
    "EnvironmentSummaryTypeDef",
    "ExternalLocationTypeDef",
    "FileBatchJobDefinitionTypeDef",
    "FileBatchJobIdentifierTypeDef",
    "FsxStorageConfigurationTypeDef",
    "GdgAttributesTypeDef",
    "GdgDetailAttributesTypeDef",
    "GetApplicationRequestRequestTypeDef",
    "GetApplicationResponseTypeDef",
    "GetApplicationVersionRequestRequestTypeDef",
    "GetApplicationVersionResponseTypeDef",
    "GetBatchJobExecutionRequestRequestTypeDef",
    "GetBatchJobExecutionResponseTypeDef",
    "GetDataSetDetailsRequestRequestTypeDef",
    "GetDataSetDetailsResponseTypeDef",
    "GetDataSetImportTaskRequestRequestTypeDef",
    "GetDataSetImportTaskResponseTypeDef",
    "GetDeploymentRequestRequestTypeDef",
    "GetDeploymentResponseTypeDef",
    "GetEnvironmentRequestRequestTypeDef",
    "GetEnvironmentResponseTypeDef",
    "HighAvailabilityConfigTypeDef",
    "ListApplicationVersionsRequestRequestTypeDef",
    "ListApplicationVersionsResponseTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListBatchJobDefinitionsRequestRequestTypeDef",
    "ListBatchJobDefinitionsResponseTypeDef",
    "ListBatchJobExecutionsRequestRequestTypeDef",
    "ListBatchJobExecutionsResponseTypeDef",
    "ListDataSetImportHistoryRequestRequestTypeDef",
    "ListDataSetImportHistoryResponseTypeDef",
    "ListDataSetsRequestRequestTypeDef",
    "ListDataSetsResponseTypeDef",
    "ListDeploymentsRequestRequestTypeDef",
    "ListDeploymentsResponseTypeDef",
    "ListEngineVersionsRequestRequestTypeDef",
    "ListEngineVersionsResponseTypeDef",
    "ListEnvironmentsRequestRequestTypeDef",
    "ListEnvironmentsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LogGroupSummaryTypeDef",
    "MaintenanceScheduleTypeDef",
    "PaginatorConfigTypeDef",
    "PendingMaintenanceTypeDef",
    "PrimaryKeyTypeDef",
    "RecordLengthTypeDef",
    "ResponseMetadataTypeDef",
    "ScriptBatchJobDefinitionTypeDef",
    "ScriptBatchJobIdentifierTypeDef",
    "StartApplicationRequestRequestTypeDef",
    "StartBatchJobRequestRequestTypeDef",
    "StartBatchJobResponseTypeDef",
    "StopApplicationRequestRequestTypeDef",
    "StorageConfigurationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "UpdateApplicationResponseTypeDef",
    "UpdateEnvironmentRequestRequestTypeDef",
    "UpdateEnvironmentResponseTypeDef",
    "VsamAttributesTypeDef",
    "VsamDetailAttributesTypeDef",
)

_RequiredAlternateKeyTypeDef = TypedDict(
    "_RequiredAlternateKeyTypeDef",
    {
        "length": int,
        "offset": int,
    },
)
_OptionalAlternateKeyTypeDef = TypedDict(
    "_OptionalAlternateKeyTypeDef",
    {
        "allowDuplicates": bool,
        "name": str,
    },
    total=False,
)

class AlternateKeyTypeDef(_RequiredAlternateKeyTypeDef, _OptionalAlternateKeyTypeDef):
    pass

_RequiredApplicationSummaryTypeDef = TypedDict(
    "_RequiredApplicationSummaryTypeDef",
    {
        "applicationArn": str,
        "applicationId": str,
        "applicationVersion": int,
        "creationTime": datetime,
        "engineType": EngineTypeType,
        "name": str,
        "status": ApplicationLifecycleType,
    },
)
_OptionalApplicationSummaryTypeDef = TypedDict(
    "_OptionalApplicationSummaryTypeDef",
    {
        "deploymentStatus": ApplicationDeploymentLifecycleType,
        "description": str,
        "environmentId": str,
        "lastStartTime": datetime,
        "versionStatus": ApplicationVersionLifecycleType,
    },
    total=False,
)

class ApplicationSummaryTypeDef(
    _RequiredApplicationSummaryTypeDef, _OptionalApplicationSummaryTypeDef
):
    pass

_RequiredApplicationVersionSummaryTypeDef = TypedDict(
    "_RequiredApplicationVersionSummaryTypeDef",
    {
        "applicationVersion": int,
        "creationTime": datetime,
        "status": ApplicationVersionLifecycleType,
    },
)
_OptionalApplicationVersionSummaryTypeDef = TypedDict(
    "_OptionalApplicationVersionSummaryTypeDef",
    {
        "statusReason": str,
    },
    total=False,
)

class ApplicationVersionSummaryTypeDef(
    _RequiredApplicationVersionSummaryTypeDef, _OptionalApplicationVersionSummaryTypeDef
):
    pass

BatchJobDefinitionTypeDef = TypedDict(
    "BatchJobDefinitionTypeDef",
    {
        "fileBatchJobDefinition": "FileBatchJobDefinitionTypeDef",
        "scriptBatchJobDefinition": "ScriptBatchJobDefinitionTypeDef",
    },
    total=False,
)

_RequiredBatchJobExecutionSummaryTypeDef = TypedDict(
    "_RequiredBatchJobExecutionSummaryTypeDef",
    {
        "applicationId": str,
        "executionId": str,
        "startTime": datetime,
        "status": BatchJobExecutionStatusType,
    },
)
_OptionalBatchJobExecutionSummaryTypeDef = TypedDict(
    "_OptionalBatchJobExecutionSummaryTypeDef",
    {
        "batchJobIdentifier": "BatchJobIdentifierTypeDef",
        "endTime": datetime,
        "jobId": str,
        "jobName": str,
        "jobType": BatchJobTypeType,
        "returnCode": str,
    },
    total=False,
)

class BatchJobExecutionSummaryTypeDef(
    _RequiredBatchJobExecutionSummaryTypeDef, _OptionalBatchJobExecutionSummaryTypeDef
):
    pass

BatchJobIdentifierTypeDef = TypedDict(
    "BatchJobIdentifierTypeDef",
    {
        "fileBatchJobIdentifier": "FileBatchJobIdentifierTypeDef",
        "scriptBatchJobIdentifier": "ScriptBatchJobIdentifierTypeDef",
    },
    total=False,
)

CancelBatchJobExecutionRequestRequestTypeDef = TypedDict(
    "CancelBatchJobExecutionRequestRequestTypeDef",
    {
        "applicationId": str,
        "executionId": str,
    },
)

_RequiredCreateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestRequestTypeDef",
    {
        "definition": "DefinitionTypeDef",
        "engineType": EngineTypeType,
        "name": str,
    },
)
_OptionalCreateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "kmsKeyId": str,
        "tags": Dict[str, str],
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
        "applicationArn": str,
        "applicationId": str,
        "applicationVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataSetImportTaskRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataSetImportTaskRequestRequestTypeDef",
    {
        "applicationId": str,
        "importConfig": "DataSetImportConfigTypeDef",
    },
)
_OptionalCreateDataSetImportTaskRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataSetImportTaskRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateDataSetImportTaskRequestRequestTypeDef(
    _RequiredCreateDataSetImportTaskRequestRequestTypeDef,
    _OptionalCreateDataSetImportTaskRequestRequestTypeDef,
):
    pass

CreateDataSetImportTaskResponseTypeDef = TypedDict(
    "CreateDataSetImportTaskResponseTypeDef",
    {
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDeploymentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDeploymentRequestRequestTypeDef",
    {
        "applicationId": str,
        "applicationVersion": int,
        "environmentId": str,
    },
)
_OptionalCreateDeploymentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDeploymentRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateDeploymentRequestRequestTypeDef(
    _RequiredCreateDeploymentRequestRequestTypeDef, _OptionalCreateDeploymentRequestRequestTypeDef
):
    pass

CreateDeploymentResponseTypeDef = TypedDict(
    "CreateDeploymentResponseTypeDef",
    {
        "deploymentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEnvironmentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEnvironmentRequestRequestTypeDef",
    {
        "engineType": EngineTypeType,
        "instanceType": str,
        "name": str,
    },
)
_OptionalCreateEnvironmentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEnvironmentRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "engineVersion": str,
        "highAvailabilityConfig": "HighAvailabilityConfigTypeDef",
        "kmsKeyId": str,
        "preferredMaintenanceWindow": str,
        "publiclyAccessible": bool,
        "securityGroupIds": List[str],
        "storageConfigurations": List["StorageConfigurationTypeDef"],
        "subnetIds": List[str],
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateEnvironmentRequestRequestTypeDef(
    _RequiredCreateEnvironmentRequestRequestTypeDef, _OptionalCreateEnvironmentRequestRequestTypeDef
):
    pass

CreateEnvironmentResponseTypeDef = TypedDict(
    "CreateEnvironmentResponseTypeDef",
    {
        "environmentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSetImportConfigTypeDef = TypedDict(
    "DataSetImportConfigTypeDef",
    {
        "dataSets": List["DataSetImportItemTypeDef"],
        "s3Location": str,
    },
    total=False,
)

DataSetImportItemTypeDef = TypedDict(
    "DataSetImportItemTypeDef",
    {
        "dataSet": "DataSetTypeDef",
        "externalLocation": "ExternalLocationTypeDef",
    },
)

DataSetImportSummaryTypeDef = TypedDict(
    "DataSetImportSummaryTypeDef",
    {
        "failed": int,
        "inProgress": int,
        "pending": int,
        "succeeded": int,
        "total": int,
    },
)

DataSetImportTaskTypeDef = TypedDict(
    "DataSetImportTaskTypeDef",
    {
        "status": DataSetTaskLifecycleType,
        "summary": "DataSetImportSummaryTypeDef",
        "taskId": str,
    },
)

_RequiredDataSetSummaryTypeDef = TypedDict(
    "_RequiredDataSetSummaryTypeDef",
    {
        "dataSetName": str,
    },
)
_OptionalDataSetSummaryTypeDef = TypedDict(
    "_OptionalDataSetSummaryTypeDef",
    {
        "creationTime": datetime,
        "dataSetOrg": str,
        "format": str,
        "lastReferencedTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
)

class DataSetSummaryTypeDef(_RequiredDataSetSummaryTypeDef, _OptionalDataSetSummaryTypeDef):
    pass

_RequiredDataSetTypeDef = TypedDict(
    "_RequiredDataSetTypeDef",
    {
        "datasetName": str,
        "datasetOrg": "DatasetOrgAttributesTypeDef",
        "recordLength": "RecordLengthTypeDef",
    },
)
_OptionalDataSetTypeDef = TypedDict(
    "_OptionalDataSetTypeDef",
    {
        "relativePath": str,
        "storageType": str,
    },
    total=False,
)

class DataSetTypeDef(_RequiredDataSetTypeDef, _OptionalDataSetTypeDef):
    pass

DatasetDetailOrgAttributesTypeDef = TypedDict(
    "DatasetDetailOrgAttributesTypeDef",
    {
        "gdg": "GdgDetailAttributesTypeDef",
        "vsam": "VsamDetailAttributesTypeDef",
    },
    total=False,
)

DatasetOrgAttributesTypeDef = TypedDict(
    "DatasetOrgAttributesTypeDef",
    {
        "gdg": "GdgAttributesTypeDef",
        "vsam": "VsamAttributesTypeDef",
    },
    total=False,
)

DefinitionTypeDef = TypedDict(
    "DefinitionTypeDef",
    {
        "content": str,
        "s3Location": str,
    },
    total=False,
)

DeleteApplicationFromEnvironmentRequestRequestTypeDef = TypedDict(
    "DeleteApplicationFromEnvironmentRequestRequestTypeDef",
    {
        "applicationId": str,
        "environmentId": str,
    },
)

DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)

DeleteEnvironmentRequestRequestTypeDef = TypedDict(
    "DeleteEnvironmentRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)

_RequiredDeployedVersionSummaryTypeDef = TypedDict(
    "_RequiredDeployedVersionSummaryTypeDef",
    {
        "applicationVersion": int,
        "status": DeploymentLifecycleType,
    },
)
_OptionalDeployedVersionSummaryTypeDef = TypedDict(
    "_OptionalDeployedVersionSummaryTypeDef",
    {
        "statusReason": str,
    },
    total=False,
)

class DeployedVersionSummaryTypeDef(
    _RequiredDeployedVersionSummaryTypeDef, _OptionalDeployedVersionSummaryTypeDef
):
    pass

_RequiredDeploymentSummaryTypeDef = TypedDict(
    "_RequiredDeploymentSummaryTypeDef",
    {
        "applicationId": str,
        "applicationVersion": int,
        "creationTime": datetime,
        "deploymentId": str,
        "environmentId": str,
        "status": DeploymentLifecycleType,
    },
)
_OptionalDeploymentSummaryTypeDef = TypedDict(
    "_OptionalDeploymentSummaryTypeDef",
    {
        "statusReason": str,
    },
    total=False,
)

class DeploymentSummaryTypeDef(
    _RequiredDeploymentSummaryTypeDef, _OptionalDeploymentSummaryTypeDef
):
    pass

EfsStorageConfigurationTypeDef = TypedDict(
    "EfsStorageConfigurationTypeDef",
    {
        "fileSystemId": str,
        "mountPoint": str,
    },
)

EngineVersionsSummaryTypeDef = TypedDict(
    "EngineVersionsSummaryTypeDef",
    {
        "engineType": str,
        "engineVersion": str,
    },
)

EnvironmentSummaryTypeDef = TypedDict(
    "EnvironmentSummaryTypeDef",
    {
        "creationTime": datetime,
        "engineType": EngineTypeType,
        "engineVersion": str,
        "environmentArn": str,
        "environmentId": str,
        "instanceType": str,
        "name": str,
        "status": EnvironmentLifecycleType,
    },
)

ExternalLocationTypeDef = TypedDict(
    "ExternalLocationTypeDef",
    {
        "s3Location": str,
    },
    total=False,
)

_RequiredFileBatchJobDefinitionTypeDef = TypedDict(
    "_RequiredFileBatchJobDefinitionTypeDef",
    {
        "fileName": str,
    },
)
_OptionalFileBatchJobDefinitionTypeDef = TypedDict(
    "_OptionalFileBatchJobDefinitionTypeDef",
    {
        "folderPath": str,
    },
    total=False,
)

class FileBatchJobDefinitionTypeDef(
    _RequiredFileBatchJobDefinitionTypeDef, _OptionalFileBatchJobDefinitionTypeDef
):
    pass

_RequiredFileBatchJobIdentifierTypeDef = TypedDict(
    "_RequiredFileBatchJobIdentifierTypeDef",
    {
        "fileName": str,
    },
)
_OptionalFileBatchJobIdentifierTypeDef = TypedDict(
    "_OptionalFileBatchJobIdentifierTypeDef",
    {
        "folderPath": str,
    },
    total=False,
)

class FileBatchJobIdentifierTypeDef(
    _RequiredFileBatchJobIdentifierTypeDef, _OptionalFileBatchJobIdentifierTypeDef
):
    pass

FsxStorageConfigurationTypeDef = TypedDict(
    "FsxStorageConfigurationTypeDef",
    {
        "fileSystemId": str,
        "mountPoint": str,
    },
)

GdgAttributesTypeDef = TypedDict(
    "GdgAttributesTypeDef",
    {
        "limit": int,
        "rollDisposition": str,
    },
    total=False,
)

GdgDetailAttributesTypeDef = TypedDict(
    "GdgDetailAttributesTypeDef",
    {
        "limit": int,
        "rollDisposition": str,
    },
    total=False,
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
        "applicationArn": str,
        "applicationId": str,
        "creationTime": datetime,
        "deployedVersion": "DeployedVersionSummaryTypeDef",
        "description": str,
        "engineType": EngineTypeType,
        "environmentId": str,
        "kmsKeyId": str,
        "lastStartTime": datetime,
        "latestVersion": "ApplicationVersionSummaryTypeDef",
        "listenerArns": List[str],
        "listenerPorts": List[int],
        "loadBalancerDnsName": str,
        "logGroups": List["LogGroupSummaryTypeDef"],
        "name": str,
        "status": ApplicationLifecycleType,
        "statusReason": str,
        "tags": Dict[str, str],
        "targetGroupArns": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApplicationVersionRequestRequestTypeDef = TypedDict(
    "GetApplicationVersionRequestRequestTypeDef",
    {
        "applicationId": str,
        "applicationVersion": int,
    },
)

GetApplicationVersionResponseTypeDef = TypedDict(
    "GetApplicationVersionResponseTypeDef",
    {
        "applicationVersion": int,
        "creationTime": datetime,
        "definitionContent": str,
        "description": str,
        "name": str,
        "status": ApplicationVersionLifecycleType,
        "statusReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBatchJobExecutionRequestRequestTypeDef = TypedDict(
    "GetBatchJobExecutionRequestRequestTypeDef",
    {
        "applicationId": str,
        "executionId": str,
    },
)

GetBatchJobExecutionResponseTypeDef = TypedDict(
    "GetBatchJobExecutionResponseTypeDef",
    {
        "applicationId": str,
        "batchJobIdentifier": "BatchJobIdentifierTypeDef",
        "endTime": datetime,
        "executionId": str,
        "jobId": str,
        "jobName": str,
        "jobType": BatchJobTypeType,
        "jobUser": str,
        "returnCode": str,
        "startTime": datetime,
        "status": BatchJobExecutionStatusType,
        "statusReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataSetDetailsRequestRequestTypeDef = TypedDict(
    "GetDataSetDetailsRequestRequestTypeDef",
    {
        "applicationId": str,
        "dataSetName": str,
    },
)

GetDataSetDetailsResponseTypeDef = TypedDict(
    "GetDataSetDetailsResponseTypeDef",
    {
        "blocksize": int,
        "creationTime": datetime,
        "dataSetName": str,
        "dataSetOrg": "DatasetDetailOrgAttributesTypeDef",
        "lastReferencedTime": datetime,
        "lastUpdatedTime": datetime,
        "location": str,
        "recordLength": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataSetImportTaskRequestRequestTypeDef = TypedDict(
    "GetDataSetImportTaskRequestRequestTypeDef",
    {
        "applicationId": str,
        "taskId": str,
    },
)

GetDataSetImportTaskResponseTypeDef = TypedDict(
    "GetDataSetImportTaskResponseTypeDef",
    {
        "status": DataSetTaskLifecycleType,
        "summary": "DataSetImportSummaryTypeDef",
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentRequestRequestTypeDef = TypedDict(
    "GetDeploymentRequestRequestTypeDef",
    {
        "applicationId": str,
        "deploymentId": str,
    },
)

GetDeploymentResponseTypeDef = TypedDict(
    "GetDeploymentResponseTypeDef",
    {
        "applicationId": str,
        "applicationVersion": int,
        "creationTime": datetime,
        "deploymentId": str,
        "environmentId": str,
        "status": DeploymentLifecycleType,
        "statusReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnvironmentRequestRequestTypeDef = TypedDict(
    "GetEnvironmentRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)

GetEnvironmentResponseTypeDef = TypedDict(
    "GetEnvironmentResponseTypeDef",
    {
        "actualCapacity": int,
        "creationTime": datetime,
        "description": str,
        "engineType": EngineTypeType,
        "engineVersion": str,
        "environmentArn": str,
        "environmentId": str,
        "highAvailabilityConfig": "HighAvailabilityConfigTypeDef",
        "instanceType": str,
        "kmsKeyId": str,
        "loadBalancerArn": str,
        "name": str,
        "pendingMaintenance": "PendingMaintenanceTypeDef",
        "preferredMaintenanceWindow": str,
        "publiclyAccessible": bool,
        "securityGroupIds": List[str],
        "status": EnvironmentLifecycleType,
        "statusReason": str,
        "storageConfigurations": List["StorageConfigurationTypeDef"],
        "subnetIds": List[str],
        "tags": Dict[str, str],
        "vpcId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HighAvailabilityConfigTypeDef = TypedDict(
    "HighAvailabilityConfigTypeDef",
    {
        "desiredCapacity": int,
    },
)

_RequiredListApplicationVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListApplicationVersionsRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
_OptionalListApplicationVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListApplicationVersionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListApplicationVersionsRequestRequestTypeDef(
    _RequiredListApplicationVersionsRequestRequestTypeDef,
    _OptionalListApplicationVersionsRequestRequestTypeDef,
):
    pass

ListApplicationVersionsResponseTypeDef = TypedDict(
    "ListApplicationVersionsResponseTypeDef",
    {
        "applicationVersions": List["ApplicationVersionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "environmentId": str,
        "maxResults": int,
        "names": List[str],
        "nextToken": str,
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

_RequiredListBatchJobDefinitionsRequestRequestTypeDef = TypedDict(
    "_RequiredListBatchJobDefinitionsRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
_OptionalListBatchJobDefinitionsRequestRequestTypeDef = TypedDict(
    "_OptionalListBatchJobDefinitionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "prefix": str,
    },
    total=False,
)

class ListBatchJobDefinitionsRequestRequestTypeDef(
    _RequiredListBatchJobDefinitionsRequestRequestTypeDef,
    _OptionalListBatchJobDefinitionsRequestRequestTypeDef,
):
    pass

ListBatchJobDefinitionsResponseTypeDef = TypedDict(
    "ListBatchJobDefinitionsResponseTypeDef",
    {
        "batchJobDefinitions": List["BatchJobDefinitionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBatchJobExecutionsRequestRequestTypeDef = TypedDict(
    "_RequiredListBatchJobExecutionsRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
_OptionalListBatchJobExecutionsRequestRequestTypeDef = TypedDict(
    "_OptionalListBatchJobExecutionsRequestRequestTypeDef",
    {
        "executionIds": List[str],
        "jobName": str,
        "maxResults": int,
        "nextToken": str,
        "startedAfter": Union[datetime, str],
        "startedBefore": Union[datetime, str],
        "status": BatchJobExecutionStatusType,
    },
    total=False,
)

class ListBatchJobExecutionsRequestRequestTypeDef(
    _RequiredListBatchJobExecutionsRequestRequestTypeDef,
    _OptionalListBatchJobExecutionsRequestRequestTypeDef,
):
    pass

ListBatchJobExecutionsResponseTypeDef = TypedDict(
    "ListBatchJobExecutionsResponseTypeDef",
    {
        "batchJobExecutions": List["BatchJobExecutionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDataSetImportHistoryRequestRequestTypeDef = TypedDict(
    "_RequiredListDataSetImportHistoryRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
_OptionalListDataSetImportHistoryRequestRequestTypeDef = TypedDict(
    "_OptionalListDataSetImportHistoryRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListDataSetImportHistoryRequestRequestTypeDef(
    _RequiredListDataSetImportHistoryRequestRequestTypeDef,
    _OptionalListDataSetImportHistoryRequestRequestTypeDef,
):
    pass

ListDataSetImportHistoryResponseTypeDef = TypedDict(
    "ListDataSetImportHistoryResponseTypeDef",
    {
        "dataSetImportTasks": List["DataSetImportTaskTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDataSetsRequestRequestTypeDef = TypedDict(
    "_RequiredListDataSetsRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
_OptionalListDataSetsRequestRequestTypeDef = TypedDict(
    "_OptionalListDataSetsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "prefix": str,
    },
    total=False,
)

class ListDataSetsRequestRequestTypeDef(
    _RequiredListDataSetsRequestRequestTypeDef, _OptionalListDataSetsRequestRequestTypeDef
):
    pass

ListDataSetsResponseTypeDef = TypedDict(
    "ListDataSetsResponseTypeDef",
    {
        "dataSets": List["DataSetSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDeploymentsRequestRequestTypeDef = TypedDict(
    "_RequiredListDeploymentsRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
_OptionalListDeploymentsRequestRequestTypeDef = TypedDict(
    "_OptionalListDeploymentsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListDeploymentsRequestRequestTypeDef(
    _RequiredListDeploymentsRequestRequestTypeDef, _OptionalListDeploymentsRequestRequestTypeDef
):
    pass

ListDeploymentsResponseTypeDef = TypedDict(
    "ListDeploymentsResponseTypeDef",
    {
        "deployments": List["DeploymentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEngineVersionsRequestRequestTypeDef = TypedDict(
    "ListEngineVersionsRequestRequestTypeDef",
    {
        "engineType": EngineTypeType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListEngineVersionsResponseTypeDef = TypedDict(
    "ListEngineVersionsResponseTypeDef",
    {
        "engineVersions": List["EngineVersionsSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEnvironmentsRequestRequestTypeDef = TypedDict(
    "ListEnvironmentsRequestRequestTypeDef",
    {
        "engineType": EngineTypeType,
        "maxResults": int,
        "names": List[str],
        "nextToken": str,
    },
    total=False,
)

ListEnvironmentsResponseTypeDef = TypedDict(
    "ListEnvironmentsResponseTypeDef",
    {
        "environments": List["EnvironmentSummaryTypeDef"],
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

LogGroupSummaryTypeDef = TypedDict(
    "LogGroupSummaryTypeDef",
    {
        "logGroupName": str,
        "logType": str,
    },
)

MaintenanceScheduleTypeDef = TypedDict(
    "MaintenanceScheduleTypeDef",
    {
        "endTime": datetime,
        "startTime": datetime,
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

PendingMaintenanceTypeDef = TypedDict(
    "PendingMaintenanceTypeDef",
    {
        "engineVersion": str,
        "schedule": "MaintenanceScheduleTypeDef",
    },
    total=False,
)

_RequiredPrimaryKeyTypeDef = TypedDict(
    "_RequiredPrimaryKeyTypeDef",
    {
        "length": int,
        "offset": int,
    },
)
_OptionalPrimaryKeyTypeDef = TypedDict(
    "_OptionalPrimaryKeyTypeDef",
    {
        "name": str,
    },
    total=False,
)

class PrimaryKeyTypeDef(_RequiredPrimaryKeyTypeDef, _OptionalPrimaryKeyTypeDef):
    pass

RecordLengthTypeDef = TypedDict(
    "RecordLengthTypeDef",
    {
        "max": int,
        "min": int,
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

ScriptBatchJobDefinitionTypeDef = TypedDict(
    "ScriptBatchJobDefinitionTypeDef",
    {
        "scriptName": str,
    },
)

ScriptBatchJobIdentifierTypeDef = TypedDict(
    "ScriptBatchJobIdentifierTypeDef",
    {
        "scriptName": str,
    },
)

StartApplicationRequestRequestTypeDef = TypedDict(
    "StartApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)

_RequiredStartBatchJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartBatchJobRequestRequestTypeDef",
    {
        "applicationId": str,
        "batchJobIdentifier": "BatchJobIdentifierTypeDef",
    },
)
_OptionalStartBatchJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartBatchJobRequestRequestTypeDef",
    {
        "jobParams": Dict[str, str],
    },
    total=False,
)

class StartBatchJobRequestRequestTypeDef(
    _RequiredStartBatchJobRequestRequestTypeDef, _OptionalStartBatchJobRequestRequestTypeDef
):
    pass

StartBatchJobResponseTypeDef = TypedDict(
    "StartBatchJobResponseTypeDef",
    {
        "executionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStopApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredStopApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
_OptionalStopApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalStopApplicationRequestRequestTypeDef",
    {
        "forceStop": bool,
    },
    total=False,
)

class StopApplicationRequestRequestTypeDef(
    _RequiredStopApplicationRequestRequestTypeDef, _OptionalStopApplicationRequestRequestTypeDef
):
    pass

StorageConfigurationTypeDef = TypedDict(
    "StorageConfigurationTypeDef",
    {
        "efs": "EfsStorageConfigurationTypeDef",
        "fsx": "FsxStorageConfigurationTypeDef",
    },
    total=False,
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

_RequiredUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
        "currentApplicationVersion": int,
    },
)
_OptionalUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationRequestRequestTypeDef",
    {
        "definition": "DefinitionTypeDef",
        "description": str,
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
        "applicationVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEnvironmentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEnvironmentRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)
_OptionalUpdateEnvironmentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEnvironmentRequestRequestTypeDef",
    {
        "applyDuringMaintenanceWindow": bool,
        "desiredCapacity": int,
        "engineVersion": str,
        "instanceType": str,
        "preferredMaintenanceWindow": str,
    },
    total=False,
)

class UpdateEnvironmentRequestRequestTypeDef(
    _RequiredUpdateEnvironmentRequestRequestTypeDef, _OptionalUpdateEnvironmentRequestRequestTypeDef
):
    pass

UpdateEnvironmentResponseTypeDef = TypedDict(
    "UpdateEnvironmentResponseTypeDef",
    {
        "environmentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredVsamAttributesTypeDef = TypedDict(
    "_RequiredVsamAttributesTypeDef",
    {
        "format": str,
    },
)
_OptionalVsamAttributesTypeDef = TypedDict(
    "_OptionalVsamAttributesTypeDef",
    {
        "alternateKeys": List["AlternateKeyTypeDef"],
        "compressed": bool,
        "encoding": str,
        "primaryKey": "PrimaryKeyTypeDef",
    },
    total=False,
)

class VsamAttributesTypeDef(_RequiredVsamAttributesTypeDef, _OptionalVsamAttributesTypeDef):
    pass

VsamDetailAttributesTypeDef = TypedDict(
    "VsamDetailAttributesTypeDef",
    {
        "alternateKeys": List["AlternateKeyTypeDef"],
        "cacheAtStartup": bool,
        "compressed": bool,
        "encoding": str,
        "primaryKey": "PrimaryKeyTypeDef",
        "recordFormat": str,
    },
    total=False,
)
