"""
Type annotations for timestream-influxdb service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/type_defs.html)

Usage::

    ```python
    from mypy_boto3_timestream_influxdb.type_defs import CreateDbInstanceInputRequestTypeDef

    data: CreateDbInstanceInputRequestTypeDef = {...}
    ```
"""

import sys
from typing import Any, Dict, List

from .literals import (
    DbInstanceTypeType,
    DbStorageTypeType,
    DeploymentTypeType,
    LogLevelType,
    StatusType,
    TracingTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateDbInstanceInputRequestTypeDef",
    "CreateDbInstanceOutputTypeDef",
    "CreateDbParameterGroupInputRequestTypeDef",
    "CreateDbParameterGroupOutputTypeDef",
    "DbInstanceSummaryTypeDef",
    "DbParameterGroupSummaryTypeDef",
    "DeleteDbInstanceInputRequestTypeDef",
    "DeleteDbInstanceOutputTypeDef",
    "GetDbInstanceInputRequestTypeDef",
    "GetDbInstanceOutputTypeDef",
    "GetDbParameterGroupInputRequestTypeDef",
    "GetDbParameterGroupOutputTypeDef",
    "InfluxDBv2ParametersTypeDef",
    "ListDbInstancesInputRequestTypeDef",
    "ListDbInstancesOutputTypeDef",
    "ListDbParameterGroupsInputRequestTypeDef",
    "ListDbParameterGroupsOutputTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LogDeliveryConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ParametersTypeDef",
    "ResponseMetadataTypeDef",
    "S3ConfigurationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDbInstanceInputRequestTypeDef",
    "UpdateDbInstanceOutputTypeDef",
)

_RequiredCreateDbInstanceInputRequestTypeDef = TypedDict(
    "_RequiredCreateDbInstanceInputRequestTypeDef",
    {
        "name": str,
        "password": str,
        "dbInstanceType": DbInstanceTypeType,
        "vpcSubnetIds": List[str],
        "vpcSecurityGroupIds": List[str],
        "allocatedStorage": int,
    },
)
_OptionalCreateDbInstanceInputRequestTypeDef = TypedDict(
    "_OptionalCreateDbInstanceInputRequestTypeDef",
    {
        "username": str,
        "organization": str,
        "bucket": str,
        "publiclyAccessible": bool,
        "dbStorageType": DbStorageTypeType,
        "dbParameterGroupIdentifier": str,
        "deploymentType": DeploymentTypeType,
        "logDeliveryConfiguration": "LogDeliveryConfigurationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateDbInstanceInputRequestTypeDef(
    _RequiredCreateDbInstanceInputRequestTypeDef, _OptionalCreateDbInstanceInputRequestTypeDef
):
    pass

CreateDbInstanceOutputTypeDef = TypedDict(
    "CreateDbInstanceOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": StatusType,
        "endpoint": str,
        "dbInstanceType": DbInstanceTypeType,
        "dbStorageType": DbStorageTypeType,
        "allocatedStorage": int,
        "deploymentType": DeploymentTypeType,
        "vpcSubnetIds": List[str],
        "publiclyAccessible": bool,
        "vpcSecurityGroupIds": List[str],
        "dbParameterGroupIdentifier": str,
        "availabilityZone": str,
        "secondaryAvailabilityZone": str,
        "logDeliveryConfiguration": "LogDeliveryConfigurationTypeDef",
        "influxAuthParametersSecretArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDbParameterGroupInputRequestTypeDef = TypedDict(
    "_RequiredCreateDbParameterGroupInputRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateDbParameterGroupInputRequestTypeDef = TypedDict(
    "_OptionalCreateDbParameterGroupInputRequestTypeDef",
    {
        "description": str,
        "parameters": "ParametersTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateDbParameterGroupInputRequestTypeDef(
    _RequiredCreateDbParameterGroupInputRequestTypeDef,
    _OptionalCreateDbParameterGroupInputRequestTypeDef,
):
    pass

CreateDbParameterGroupOutputTypeDef = TypedDict(
    "CreateDbParameterGroupOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "description": str,
        "parameters": "ParametersTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDbInstanceSummaryTypeDef = TypedDict(
    "_RequiredDbInstanceSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
    },
)
_OptionalDbInstanceSummaryTypeDef = TypedDict(
    "_OptionalDbInstanceSummaryTypeDef",
    {
        "status": StatusType,
        "endpoint": str,
        "dbInstanceType": DbInstanceTypeType,
        "dbStorageType": DbStorageTypeType,
        "allocatedStorage": int,
        "deploymentType": DeploymentTypeType,
    },
    total=False,
)

class DbInstanceSummaryTypeDef(
    _RequiredDbInstanceSummaryTypeDef, _OptionalDbInstanceSummaryTypeDef
):
    pass

_RequiredDbParameterGroupSummaryTypeDef = TypedDict(
    "_RequiredDbParameterGroupSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
    },
)
_OptionalDbParameterGroupSummaryTypeDef = TypedDict(
    "_OptionalDbParameterGroupSummaryTypeDef",
    {
        "description": str,
    },
    total=False,
)

class DbParameterGroupSummaryTypeDef(
    _RequiredDbParameterGroupSummaryTypeDef, _OptionalDbParameterGroupSummaryTypeDef
):
    pass

DeleteDbInstanceInputRequestTypeDef = TypedDict(
    "DeleteDbInstanceInputRequestTypeDef",
    {
        "identifier": str,
    },
)

DeleteDbInstanceOutputTypeDef = TypedDict(
    "DeleteDbInstanceOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": StatusType,
        "endpoint": str,
        "dbInstanceType": DbInstanceTypeType,
        "dbStorageType": DbStorageTypeType,
        "allocatedStorage": int,
        "deploymentType": DeploymentTypeType,
        "vpcSubnetIds": List[str],
        "publiclyAccessible": bool,
        "vpcSecurityGroupIds": List[str],
        "dbParameterGroupIdentifier": str,
        "availabilityZone": str,
        "secondaryAvailabilityZone": str,
        "logDeliveryConfiguration": "LogDeliveryConfigurationTypeDef",
        "influxAuthParametersSecretArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDbInstanceInputRequestTypeDef = TypedDict(
    "GetDbInstanceInputRequestTypeDef",
    {
        "identifier": str,
    },
)

GetDbInstanceOutputTypeDef = TypedDict(
    "GetDbInstanceOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": StatusType,
        "endpoint": str,
        "dbInstanceType": DbInstanceTypeType,
        "dbStorageType": DbStorageTypeType,
        "allocatedStorage": int,
        "deploymentType": DeploymentTypeType,
        "vpcSubnetIds": List[str],
        "publiclyAccessible": bool,
        "vpcSecurityGroupIds": List[str],
        "dbParameterGroupIdentifier": str,
        "availabilityZone": str,
        "secondaryAvailabilityZone": str,
        "logDeliveryConfiguration": "LogDeliveryConfigurationTypeDef",
        "influxAuthParametersSecretArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDbParameterGroupInputRequestTypeDef = TypedDict(
    "GetDbParameterGroupInputRequestTypeDef",
    {
        "identifier": str,
    },
)

GetDbParameterGroupOutputTypeDef = TypedDict(
    "GetDbParameterGroupOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "description": str,
        "parameters": "ParametersTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InfluxDBv2ParametersTypeDef = TypedDict(
    "InfluxDBv2ParametersTypeDef",
    {
        "fluxLogEnabled": bool,
        "logLevel": LogLevelType,
        "noTasks": bool,
        "queryConcurrency": int,
        "queryQueueSize": int,
        "tracingType": TracingTypeType,
        "metricsDisabled": bool,
    },
    total=False,
)

ListDbInstancesInputRequestTypeDef = TypedDict(
    "ListDbInstancesInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDbInstancesOutputTypeDef = TypedDict(
    "ListDbInstancesOutputTypeDef",
    {
        "items": List["DbInstanceSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDbParameterGroupsInputRequestTypeDef = TypedDict(
    "ListDbParameterGroupsInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDbParameterGroupsOutputTypeDef = TypedDict(
    "ListDbParameterGroupsOutputTypeDef",
    {
        "items": List["DbParameterGroupSummaryTypeDef"],
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

LogDeliveryConfigurationTypeDef = TypedDict(
    "LogDeliveryConfigurationTypeDef",
    {
        "s3Configuration": "S3ConfigurationTypeDef",
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

ParametersTypeDef = TypedDict(
    "ParametersTypeDef",
    {
        "InfluxDBv2": "InfluxDBv2ParametersTypeDef",
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

S3ConfigurationTypeDef = TypedDict(
    "S3ConfigurationTypeDef",
    {
        "bucketName": str,
        "enabled": bool,
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

_RequiredUpdateDbInstanceInputRequestTypeDef = TypedDict(
    "_RequiredUpdateDbInstanceInputRequestTypeDef",
    {
        "identifier": str,
    },
)
_OptionalUpdateDbInstanceInputRequestTypeDef = TypedDict(
    "_OptionalUpdateDbInstanceInputRequestTypeDef",
    {
        "logDeliveryConfiguration": "LogDeliveryConfigurationTypeDef",
        "dbParameterGroupIdentifier": str,
    },
    total=False,
)

class UpdateDbInstanceInputRequestTypeDef(
    _RequiredUpdateDbInstanceInputRequestTypeDef, _OptionalUpdateDbInstanceInputRequestTypeDef
):
    pass

UpdateDbInstanceOutputTypeDef = TypedDict(
    "UpdateDbInstanceOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": StatusType,
        "endpoint": str,
        "dbInstanceType": DbInstanceTypeType,
        "dbStorageType": DbStorageTypeType,
        "allocatedStorage": int,
        "deploymentType": DeploymentTypeType,
        "vpcSubnetIds": List[str],
        "publiclyAccessible": bool,
        "vpcSecurityGroupIds": List[str],
        "dbParameterGroupIdentifier": str,
        "availabilityZone": str,
        "secondaryAvailabilityZone": str,
        "logDeliveryConfiguration": "LogDeliveryConfigurationTypeDef",
        "influxAuthParametersSecretArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
