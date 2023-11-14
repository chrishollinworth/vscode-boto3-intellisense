"""
Type annotations for finspace service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace/type_defs.html)

Usage::

    ```python
    from mypy_boto3_finspace.type_defs import AutoScalingConfigurationTypeDef

    data: AutoScalingConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ChangesetStatusType,
    ChangeTypeType,
    EnvironmentStatusType,
    ErrorDetailsType,
    FederationModeType,
    KxAzModeType,
    KxClusterCodeDeploymentStrategyType,
    KxClusterStatusType,
    KxClusterTypeType,
    KxDeploymentStrategyType,
    RuleActionType,
    dnsStatusType,
    tgwStatusType,
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
    "AutoScalingConfigurationTypeDef",
    "CapacityConfigurationTypeDef",
    "ChangeRequestTypeDef",
    "CodeConfigurationTypeDef",
    "CreateEnvironmentRequestRequestTypeDef",
    "CreateEnvironmentResponseTypeDef",
    "CreateKxChangesetRequestRequestTypeDef",
    "CreateKxChangesetResponseTypeDef",
    "CreateKxClusterRequestRequestTypeDef",
    "CreateKxClusterResponseTypeDef",
    "CreateKxDatabaseRequestRequestTypeDef",
    "CreateKxDatabaseResponseTypeDef",
    "CreateKxEnvironmentRequestRequestTypeDef",
    "CreateKxEnvironmentResponseTypeDef",
    "CreateKxUserRequestRequestTypeDef",
    "CreateKxUserResponseTypeDef",
    "CustomDNSServerTypeDef",
    "DeleteEnvironmentRequestRequestTypeDef",
    "DeleteKxClusterRequestRequestTypeDef",
    "DeleteKxDatabaseRequestRequestTypeDef",
    "DeleteKxEnvironmentRequestRequestTypeDef",
    "DeleteKxUserRequestRequestTypeDef",
    "EnvironmentTypeDef",
    "ErrorInfoTypeDef",
    "FederationParametersTypeDef",
    "GetEnvironmentRequestRequestTypeDef",
    "GetEnvironmentResponseTypeDef",
    "GetKxChangesetRequestRequestTypeDef",
    "GetKxChangesetResponseTypeDef",
    "GetKxClusterRequestRequestTypeDef",
    "GetKxClusterResponseTypeDef",
    "GetKxConnectionStringRequestRequestTypeDef",
    "GetKxConnectionStringResponseTypeDef",
    "GetKxDatabaseRequestRequestTypeDef",
    "GetKxDatabaseResponseTypeDef",
    "GetKxEnvironmentRequestRequestTypeDef",
    "GetKxEnvironmentResponseTypeDef",
    "GetKxUserRequestRequestTypeDef",
    "GetKxUserResponseTypeDef",
    "IcmpTypeCodeTypeDef",
    "KxCacheStorageConfigurationTypeDef",
    "KxChangesetListEntryTypeDef",
    "KxClusterCodeDeploymentConfigurationTypeDef",
    "KxClusterTypeDef",
    "KxCommandLineArgumentTypeDef",
    "KxDatabaseCacheConfigurationTypeDef",
    "KxDatabaseConfigurationTypeDef",
    "KxDatabaseListEntryTypeDef",
    "KxDeploymentConfigurationTypeDef",
    "KxEnvironmentTypeDef",
    "KxNodeTypeDef",
    "KxSavedownStorageConfigurationTypeDef",
    "KxUserTypeDef",
    "ListEnvironmentsRequestRequestTypeDef",
    "ListEnvironmentsResponseTypeDef",
    "ListKxChangesetsRequestRequestTypeDef",
    "ListKxChangesetsResponseTypeDef",
    "ListKxClusterNodesRequestRequestTypeDef",
    "ListKxClusterNodesResponseTypeDef",
    "ListKxClustersRequestRequestTypeDef",
    "ListKxClustersResponseTypeDef",
    "ListKxDatabasesRequestRequestTypeDef",
    "ListKxDatabasesResponseTypeDef",
    "ListKxEnvironmentsRequestRequestTypeDef",
    "ListKxEnvironmentsResponseTypeDef",
    "ListKxUsersRequestRequestTypeDef",
    "ListKxUsersResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NetworkACLEntryTypeDef",
    "PaginatorConfigTypeDef",
    "PortRangeTypeDef",
    "ResponseMetadataTypeDef",
    "SuperuserParametersTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TransitGatewayConfigurationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateEnvironmentRequestRequestTypeDef",
    "UpdateEnvironmentResponseTypeDef",
    "UpdateKxClusterCodeConfigurationRequestRequestTypeDef",
    "UpdateKxClusterDatabasesRequestRequestTypeDef",
    "UpdateKxDatabaseRequestRequestTypeDef",
    "UpdateKxDatabaseResponseTypeDef",
    "UpdateKxEnvironmentNetworkRequestRequestTypeDef",
    "UpdateKxEnvironmentNetworkResponseTypeDef",
    "UpdateKxEnvironmentRequestRequestTypeDef",
    "UpdateKxEnvironmentResponseTypeDef",
    "UpdateKxUserRequestRequestTypeDef",
    "UpdateKxUserResponseTypeDef",
    "VpcConfigurationTypeDef",
)

AutoScalingConfigurationTypeDef = TypedDict(
    "AutoScalingConfigurationTypeDef",
    {
        "minNodeCount": int,
        "maxNodeCount": int,
        "autoScalingMetric": Literal["CPU_UTILIZATION_PERCENTAGE"],
        "metricTarget": float,
        "scaleInCooldownSeconds": float,
        "scaleOutCooldownSeconds": float,
    },
    total=False,
)

CapacityConfigurationTypeDef = TypedDict(
    "CapacityConfigurationTypeDef",
    {
        "nodeType": str,
        "nodeCount": int,
    },
    total=False,
)

_RequiredChangeRequestTypeDef = TypedDict(
    "_RequiredChangeRequestTypeDef",
    {
        "changeType": ChangeTypeType,
        "dbPath": str,
    },
)
_OptionalChangeRequestTypeDef = TypedDict(
    "_OptionalChangeRequestTypeDef",
    {
        "s3Path": str,
    },
    total=False,
)

class ChangeRequestTypeDef(_RequiredChangeRequestTypeDef, _OptionalChangeRequestTypeDef):
    pass

CodeConfigurationTypeDef = TypedDict(
    "CodeConfigurationTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
        "s3ObjectVersion": str,
    },
    total=False,
)

_RequiredCreateEnvironmentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEnvironmentRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateEnvironmentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEnvironmentRequestRequestTypeDef",
    {
        "description": str,
        "kmsKeyId": str,
        "tags": Dict[str, str],
        "federationMode": FederationModeType,
        "federationParameters": "FederationParametersTypeDef",
        "superuserParameters": "SuperuserParametersTypeDef",
        "dataBundles": List[str],
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
        "environmentArn": str,
        "environmentUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateKxChangesetRequestRequestTypeDef = TypedDict(
    "CreateKxChangesetRequestRequestTypeDef",
    {
        "environmentId": str,
        "databaseName": str,
        "changeRequests": List["ChangeRequestTypeDef"],
        "clientToken": str,
    },
)

CreateKxChangesetResponseTypeDef = TypedDict(
    "CreateKxChangesetResponseTypeDef",
    {
        "changesetId": str,
        "databaseName": str,
        "environmentId": str,
        "changeRequests": List["ChangeRequestTypeDef"],
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
        "status": ChangesetStatusType,
        "errorInfo": "ErrorInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateKxClusterRequestRequestTypeDef = TypedDict(
    "_RequiredCreateKxClusterRequestRequestTypeDef",
    {
        "environmentId": str,
        "clusterName": str,
        "clusterType": KxClusterTypeType,
        "capacityConfiguration": "CapacityConfigurationTypeDef",
        "releaseLabel": str,
        "azMode": KxAzModeType,
    },
)
_OptionalCreateKxClusterRequestRequestTypeDef = TypedDict(
    "_OptionalCreateKxClusterRequestRequestTypeDef",
    {
        "clientToken": str,
        "databases": List["KxDatabaseConfigurationTypeDef"],
        "cacheStorageConfigurations": List["KxCacheStorageConfigurationTypeDef"],
        "autoScalingConfiguration": "AutoScalingConfigurationTypeDef",
        "clusterDescription": str,
        "vpcConfiguration": "VpcConfigurationTypeDef",
        "initializationScript": str,
        "commandLineArguments": List["KxCommandLineArgumentTypeDef"],
        "code": "CodeConfigurationTypeDef",
        "executionRole": str,
        "savedownStorageConfiguration": "KxSavedownStorageConfigurationTypeDef",
        "availabilityZoneId": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateKxClusterRequestRequestTypeDef(
    _RequiredCreateKxClusterRequestRequestTypeDef, _OptionalCreateKxClusterRequestRequestTypeDef
):
    pass

CreateKxClusterResponseTypeDef = TypedDict(
    "CreateKxClusterResponseTypeDef",
    {
        "environmentId": str,
        "status": KxClusterStatusType,
        "statusReason": str,
        "clusterName": str,
        "clusterType": KxClusterTypeType,
        "databases": List["KxDatabaseConfigurationTypeDef"],
        "cacheStorageConfigurations": List["KxCacheStorageConfigurationTypeDef"],
        "autoScalingConfiguration": "AutoScalingConfigurationTypeDef",
        "clusterDescription": str,
        "capacityConfiguration": "CapacityConfigurationTypeDef",
        "releaseLabel": str,
        "vpcConfiguration": "VpcConfigurationTypeDef",
        "initializationScript": str,
        "commandLineArguments": List["KxCommandLineArgumentTypeDef"],
        "code": "CodeConfigurationTypeDef",
        "executionRole": str,
        "lastModifiedTimestamp": datetime,
        "savedownStorageConfiguration": "KxSavedownStorageConfigurationTypeDef",
        "azMode": KxAzModeType,
        "availabilityZoneId": str,
        "createdTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateKxDatabaseRequestRequestTypeDef = TypedDict(
    "_RequiredCreateKxDatabaseRequestRequestTypeDef",
    {
        "environmentId": str,
        "databaseName": str,
        "clientToken": str,
    },
)
_OptionalCreateKxDatabaseRequestRequestTypeDef = TypedDict(
    "_OptionalCreateKxDatabaseRequestRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateKxDatabaseRequestRequestTypeDef(
    _RequiredCreateKxDatabaseRequestRequestTypeDef, _OptionalCreateKxDatabaseRequestRequestTypeDef
):
    pass

CreateKxDatabaseResponseTypeDef = TypedDict(
    "CreateKxDatabaseResponseTypeDef",
    {
        "databaseName": str,
        "databaseArn": str,
        "environmentId": str,
        "description": str,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateKxEnvironmentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateKxEnvironmentRequestRequestTypeDef",
    {
        "name": str,
        "kmsKeyId": str,
    },
)
_OptionalCreateKxEnvironmentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateKxEnvironmentRequestRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
        "clientToken": str,
    },
    total=False,
)

class CreateKxEnvironmentRequestRequestTypeDef(
    _RequiredCreateKxEnvironmentRequestRequestTypeDef,
    _OptionalCreateKxEnvironmentRequestRequestTypeDef,
):
    pass

CreateKxEnvironmentResponseTypeDef = TypedDict(
    "CreateKxEnvironmentResponseTypeDef",
    {
        "name": str,
        "status": EnvironmentStatusType,
        "environmentId": str,
        "description": str,
        "environmentArn": str,
        "kmsKeyId": str,
        "creationTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateKxUserRequestRequestTypeDef = TypedDict(
    "_RequiredCreateKxUserRequestRequestTypeDef",
    {
        "environmentId": str,
        "userName": str,
        "iamRole": str,
    },
)
_OptionalCreateKxUserRequestRequestTypeDef = TypedDict(
    "_OptionalCreateKxUserRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
        "clientToken": str,
    },
    total=False,
)

class CreateKxUserRequestRequestTypeDef(
    _RequiredCreateKxUserRequestRequestTypeDef, _OptionalCreateKxUserRequestRequestTypeDef
):
    pass

CreateKxUserResponseTypeDef = TypedDict(
    "CreateKxUserResponseTypeDef",
    {
        "userName": str,
        "userArn": str,
        "environmentId": str,
        "iamRole": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomDNSServerTypeDef = TypedDict(
    "CustomDNSServerTypeDef",
    {
        "customDNSServerName": str,
        "customDNSServerIP": str,
    },
)

DeleteEnvironmentRequestRequestTypeDef = TypedDict(
    "DeleteEnvironmentRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)

_RequiredDeleteKxClusterRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteKxClusterRequestRequestTypeDef",
    {
        "environmentId": str,
        "clusterName": str,
    },
)
_OptionalDeleteKxClusterRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteKxClusterRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteKxClusterRequestRequestTypeDef(
    _RequiredDeleteKxClusterRequestRequestTypeDef, _OptionalDeleteKxClusterRequestRequestTypeDef
):
    pass

DeleteKxDatabaseRequestRequestTypeDef = TypedDict(
    "DeleteKxDatabaseRequestRequestTypeDef",
    {
        "environmentId": str,
        "databaseName": str,
        "clientToken": str,
    },
)

DeleteKxEnvironmentRequestRequestTypeDef = TypedDict(
    "DeleteKxEnvironmentRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)

DeleteKxUserRequestRequestTypeDef = TypedDict(
    "DeleteKxUserRequestRequestTypeDef",
    {
        "userName": str,
        "environmentId": str,
    },
)

EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "name": str,
        "environmentId": str,
        "awsAccountId": str,
        "status": EnvironmentStatusType,
        "environmentUrl": str,
        "description": str,
        "environmentArn": str,
        "sageMakerStudioDomainUrl": str,
        "kmsKeyId": str,
        "dedicatedServiceAccountId": str,
        "federationMode": FederationModeType,
        "federationParameters": "FederationParametersTypeDef",
    },
    total=False,
)

ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef",
    {
        "errorMessage": str,
        "errorType": ErrorDetailsType,
    },
    total=False,
)

FederationParametersTypeDef = TypedDict(
    "FederationParametersTypeDef",
    {
        "samlMetadataDocument": str,
        "samlMetadataURL": str,
        "applicationCallBackURL": str,
        "federationURN": str,
        "federationProviderName": str,
        "attributeMap": Dict[str, str],
    },
    total=False,
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
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKxChangesetRequestRequestTypeDef = TypedDict(
    "GetKxChangesetRequestRequestTypeDef",
    {
        "environmentId": str,
        "databaseName": str,
        "changesetId": str,
    },
)

GetKxChangesetResponseTypeDef = TypedDict(
    "GetKxChangesetResponseTypeDef",
    {
        "changesetId": str,
        "databaseName": str,
        "environmentId": str,
        "changeRequests": List["ChangeRequestTypeDef"],
        "createdTimestamp": datetime,
        "activeFromTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
        "status": ChangesetStatusType,
        "errorInfo": "ErrorInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKxClusterRequestRequestTypeDef = TypedDict(
    "GetKxClusterRequestRequestTypeDef",
    {
        "environmentId": str,
        "clusterName": str,
    },
)

GetKxClusterResponseTypeDef = TypedDict(
    "GetKxClusterResponseTypeDef",
    {
        "status": KxClusterStatusType,
        "statusReason": str,
        "clusterName": str,
        "clusterType": KxClusterTypeType,
        "databases": List["KxDatabaseConfigurationTypeDef"],
        "cacheStorageConfigurations": List["KxCacheStorageConfigurationTypeDef"],
        "autoScalingConfiguration": "AutoScalingConfigurationTypeDef",
        "clusterDescription": str,
        "capacityConfiguration": "CapacityConfigurationTypeDef",
        "releaseLabel": str,
        "vpcConfiguration": "VpcConfigurationTypeDef",
        "initializationScript": str,
        "commandLineArguments": List["KxCommandLineArgumentTypeDef"],
        "code": "CodeConfigurationTypeDef",
        "executionRole": str,
        "lastModifiedTimestamp": datetime,
        "savedownStorageConfiguration": "KxSavedownStorageConfigurationTypeDef",
        "azMode": KxAzModeType,
        "availabilityZoneId": str,
        "createdTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKxConnectionStringRequestRequestTypeDef = TypedDict(
    "GetKxConnectionStringRequestRequestTypeDef",
    {
        "userArn": str,
        "environmentId": str,
        "clusterName": str,
    },
)

GetKxConnectionStringResponseTypeDef = TypedDict(
    "GetKxConnectionStringResponseTypeDef",
    {
        "signedConnectionString": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKxDatabaseRequestRequestTypeDef = TypedDict(
    "GetKxDatabaseRequestRequestTypeDef",
    {
        "environmentId": str,
        "databaseName": str,
    },
)

GetKxDatabaseResponseTypeDef = TypedDict(
    "GetKxDatabaseResponseTypeDef",
    {
        "databaseName": str,
        "databaseArn": str,
        "environmentId": str,
        "description": str,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
        "lastCompletedChangesetId": str,
        "numBytes": int,
        "numChangesets": int,
        "numFiles": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKxEnvironmentRequestRequestTypeDef = TypedDict(
    "GetKxEnvironmentRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)

GetKxEnvironmentResponseTypeDef = TypedDict(
    "GetKxEnvironmentResponseTypeDef",
    {
        "name": str,
        "environmentId": str,
        "awsAccountId": str,
        "status": EnvironmentStatusType,
        "tgwStatus": tgwStatusType,
        "dnsStatus": dnsStatusType,
        "errorMessage": str,
        "description": str,
        "environmentArn": str,
        "kmsKeyId": str,
        "dedicatedServiceAccountId": str,
        "transitGatewayConfiguration": "TransitGatewayConfigurationTypeDef",
        "customDNSConfiguration": List["CustomDNSServerTypeDef"],
        "creationTimestamp": datetime,
        "updateTimestamp": datetime,
        "availabilityZoneIds": List[str],
        "certificateAuthorityArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKxUserRequestRequestTypeDef = TypedDict(
    "GetKxUserRequestRequestTypeDef",
    {
        "userName": str,
        "environmentId": str,
    },
)

GetKxUserResponseTypeDef = TypedDict(
    "GetKxUserResponseTypeDef",
    {
        "userName": str,
        "userArn": str,
        "environmentId": str,
        "iamRole": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IcmpTypeCodeTypeDef = TypedDict(
    "IcmpTypeCodeTypeDef",
    {
        "type": int,
        "code": int,
    },
)

KxCacheStorageConfigurationTypeDef = TypedDict(
    "KxCacheStorageConfigurationTypeDef",
    {
        "type": str,
        "size": int,
    },
)

KxChangesetListEntryTypeDef = TypedDict(
    "KxChangesetListEntryTypeDef",
    {
        "changesetId": str,
        "createdTimestamp": datetime,
        "activeFromTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
        "status": ChangesetStatusType,
    },
    total=False,
)

KxClusterCodeDeploymentConfigurationTypeDef = TypedDict(
    "KxClusterCodeDeploymentConfigurationTypeDef",
    {
        "deploymentStrategy": KxClusterCodeDeploymentStrategyType,
    },
)

KxClusterTypeDef = TypedDict(
    "KxClusterTypeDef",
    {
        "status": KxClusterStatusType,
        "statusReason": str,
        "clusterName": str,
        "clusterType": KxClusterTypeType,
        "clusterDescription": str,
        "releaseLabel": str,
        "initializationScript": str,
        "executionRole": str,
        "azMode": KxAzModeType,
        "availabilityZoneId": str,
        "lastModifiedTimestamp": datetime,
        "createdTimestamp": datetime,
    },
    total=False,
)

KxCommandLineArgumentTypeDef = TypedDict(
    "KxCommandLineArgumentTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

KxDatabaseCacheConfigurationTypeDef = TypedDict(
    "KxDatabaseCacheConfigurationTypeDef",
    {
        "cacheType": str,
        "dbPaths": List[str],
    },
)

_RequiredKxDatabaseConfigurationTypeDef = TypedDict(
    "_RequiredKxDatabaseConfigurationTypeDef",
    {
        "databaseName": str,
    },
)
_OptionalKxDatabaseConfigurationTypeDef = TypedDict(
    "_OptionalKxDatabaseConfigurationTypeDef",
    {
        "cacheConfigurations": List["KxDatabaseCacheConfigurationTypeDef"],
        "changesetId": str,
    },
    total=False,
)

class KxDatabaseConfigurationTypeDef(
    _RequiredKxDatabaseConfigurationTypeDef, _OptionalKxDatabaseConfigurationTypeDef
):
    pass

KxDatabaseListEntryTypeDef = TypedDict(
    "KxDatabaseListEntryTypeDef",
    {
        "databaseName": str,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
    },
    total=False,
)

KxDeploymentConfigurationTypeDef = TypedDict(
    "KxDeploymentConfigurationTypeDef",
    {
        "deploymentStrategy": KxDeploymentStrategyType,
    },
)

KxEnvironmentTypeDef = TypedDict(
    "KxEnvironmentTypeDef",
    {
        "name": str,
        "environmentId": str,
        "awsAccountId": str,
        "status": EnvironmentStatusType,
        "tgwStatus": tgwStatusType,
        "dnsStatus": dnsStatusType,
        "errorMessage": str,
        "description": str,
        "environmentArn": str,
        "kmsKeyId": str,
        "dedicatedServiceAccountId": str,
        "transitGatewayConfiguration": "TransitGatewayConfigurationTypeDef",
        "customDNSConfiguration": List["CustomDNSServerTypeDef"],
        "creationTimestamp": datetime,
        "updateTimestamp": datetime,
        "availabilityZoneIds": List[str],
        "certificateAuthorityArn": str,
    },
    total=False,
)

KxNodeTypeDef = TypedDict(
    "KxNodeTypeDef",
    {
        "nodeId": str,
        "availabilityZoneId": str,
        "launchTime": datetime,
    },
    total=False,
)

KxSavedownStorageConfigurationTypeDef = TypedDict(
    "KxSavedownStorageConfigurationTypeDef",
    {
        "type": Literal["SDS01"],
        "size": int,
    },
)

KxUserTypeDef = TypedDict(
    "KxUserTypeDef",
    {
        "userArn": str,
        "userName": str,
        "iamRole": str,
        "createTimestamp": datetime,
        "updateTimestamp": datetime,
    },
    total=False,
)

ListEnvironmentsRequestRequestTypeDef = TypedDict(
    "ListEnvironmentsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListEnvironmentsResponseTypeDef = TypedDict(
    "ListEnvironmentsResponseTypeDef",
    {
        "environments": List["EnvironmentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListKxChangesetsRequestRequestTypeDef = TypedDict(
    "_RequiredListKxChangesetsRequestRequestTypeDef",
    {
        "environmentId": str,
        "databaseName": str,
    },
)
_OptionalListKxChangesetsRequestRequestTypeDef = TypedDict(
    "_OptionalListKxChangesetsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListKxChangesetsRequestRequestTypeDef(
    _RequiredListKxChangesetsRequestRequestTypeDef, _OptionalListKxChangesetsRequestRequestTypeDef
):
    pass

ListKxChangesetsResponseTypeDef = TypedDict(
    "ListKxChangesetsResponseTypeDef",
    {
        "kxChangesets": List["KxChangesetListEntryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListKxClusterNodesRequestRequestTypeDef = TypedDict(
    "_RequiredListKxClusterNodesRequestRequestTypeDef",
    {
        "environmentId": str,
        "clusterName": str,
    },
)
_OptionalListKxClusterNodesRequestRequestTypeDef = TypedDict(
    "_OptionalListKxClusterNodesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListKxClusterNodesRequestRequestTypeDef(
    _RequiredListKxClusterNodesRequestRequestTypeDef,
    _OptionalListKxClusterNodesRequestRequestTypeDef,
):
    pass

ListKxClusterNodesResponseTypeDef = TypedDict(
    "ListKxClusterNodesResponseTypeDef",
    {
        "nodes": List["KxNodeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListKxClustersRequestRequestTypeDef = TypedDict(
    "_RequiredListKxClustersRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)
_OptionalListKxClustersRequestRequestTypeDef = TypedDict(
    "_OptionalListKxClustersRequestRequestTypeDef",
    {
        "clusterType": KxClusterTypeType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListKxClustersRequestRequestTypeDef(
    _RequiredListKxClustersRequestRequestTypeDef, _OptionalListKxClustersRequestRequestTypeDef
):
    pass

ListKxClustersResponseTypeDef = TypedDict(
    "ListKxClustersResponseTypeDef",
    {
        "kxClusterSummaries": List["KxClusterTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListKxDatabasesRequestRequestTypeDef = TypedDict(
    "_RequiredListKxDatabasesRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)
_OptionalListKxDatabasesRequestRequestTypeDef = TypedDict(
    "_OptionalListKxDatabasesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListKxDatabasesRequestRequestTypeDef(
    _RequiredListKxDatabasesRequestRequestTypeDef, _OptionalListKxDatabasesRequestRequestTypeDef
):
    pass

ListKxDatabasesResponseTypeDef = TypedDict(
    "ListKxDatabasesResponseTypeDef",
    {
        "kxDatabases": List["KxDatabaseListEntryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListKxEnvironmentsRequestRequestTypeDef = TypedDict(
    "ListKxEnvironmentsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListKxEnvironmentsResponseTypeDef = TypedDict(
    "ListKxEnvironmentsResponseTypeDef",
    {
        "environments": List["KxEnvironmentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListKxUsersRequestRequestTypeDef = TypedDict(
    "_RequiredListKxUsersRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)
_OptionalListKxUsersRequestRequestTypeDef = TypedDict(
    "_OptionalListKxUsersRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListKxUsersRequestRequestTypeDef(
    _RequiredListKxUsersRequestRequestTypeDef, _OptionalListKxUsersRequestRequestTypeDef
):
    pass

ListKxUsersResponseTypeDef = TypedDict(
    "ListKxUsersResponseTypeDef",
    {
        "users": List["KxUserTypeDef"],
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

_RequiredNetworkACLEntryTypeDef = TypedDict(
    "_RequiredNetworkACLEntryTypeDef",
    {
        "ruleNumber": int,
        "protocol": str,
        "ruleAction": RuleActionType,
        "cidrBlock": str,
    },
)
_OptionalNetworkACLEntryTypeDef = TypedDict(
    "_OptionalNetworkACLEntryTypeDef",
    {
        "portRange": "PortRangeTypeDef",
        "icmpTypeCode": "IcmpTypeCodeTypeDef",
    },
    total=False,
)

class NetworkACLEntryTypeDef(_RequiredNetworkACLEntryTypeDef, _OptionalNetworkACLEntryTypeDef):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PortRangeTypeDef = TypedDict(
    "PortRangeTypeDef",
    {
        "from": int,
        "to": int,
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

SuperuserParametersTypeDef = TypedDict(
    "SuperuserParametersTypeDef",
    {
        "emailAddress": str,
        "firstName": str,
        "lastName": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

_RequiredTransitGatewayConfigurationTypeDef = TypedDict(
    "_RequiredTransitGatewayConfigurationTypeDef",
    {
        "transitGatewayID": str,
        "routableCIDRSpace": str,
    },
)
_OptionalTransitGatewayConfigurationTypeDef = TypedDict(
    "_OptionalTransitGatewayConfigurationTypeDef",
    {
        "attachmentNetworkAclConfiguration": List["NetworkACLEntryTypeDef"],
    },
    total=False,
)

class TransitGatewayConfigurationTypeDef(
    _RequiredTransitGatewayConfigurationTypeDef, _OptionalTransitGatewayConfigurationTypeDef
):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
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
        "name": str,
        "description": str,
        "federationMode": FederationModeType,
        "federationParameters": "FederationParametersTypeDef",
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
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateKxClusterCodeConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateKxClusterCodeConfigurationRequestRequestTypeDef",
    {
        "environmentId": str,
        "clusterName": str,
        "code": "CodeConfigurationTypeDef",
    },
)
_OptionalUpdateKxClusterCodeConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateKxClusterCodeConfigurationRequestRequestTypeDef",
    {
        "clientToken": str,
        "initializationScript": str,
        "commandLineArguments": List["KxCommandLineArgumentTypeDef"],
        "deploymentConfiguration": "KxClusterCodeDeploymentConfigurationTypeDef",
    },
    total=False,
)

class UpdateKxClusterCodeConfigurationRequestRequestTypeDef(
    _RequiredUpdateKxClusterCodeConfigurationRequestRequestTypeDef,
    _OptionalUpdateKxClusterCodeConfigurationRequestRequestTypeDef,
):
    pass

_RequiredUpdateKxClusterDatabasesRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateKxClusterDatabasesRequestRequestTypeDef",
    {
        "environmentId": str,
        "clusterName": str,
        "databases": List["KxDatabaseConfigurationTypeDef"],
    },
)
_OptionalUpdateKxClusterDatabasesRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateKxClusterDatabasesRequestRequestTypeDef",
    {
        "clientToken": str,
        "deploymentConfiguration": "KxDeploymentConfigurationTypeDef",
    },
    total=False,
)

class UpdateKxClusterDatabasesRequestRequestTypeDef(
    _RequiredUpdateKxClusterDatabasesRequestRequestTypeDef,
    _OptionalUpdateKxClusterDatabasesRequestRequestTypeDef,
):
    pass

_RequiredUpdateKxDatabaseRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateKxDatabaseRequestRequestTypeDef",
    {
        "environmentId": str,
        "databaseName": str,
        "clientToken": str,
    },
)
_OptionalUpdateKxDatabaseRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateKxDatabaseRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class UpdateKxDatabaseRequestRequestTypeDef(
    _RequiredUpdateKxDatabaseRequestRequestTypeDef, _OptionalUpdateKxDatabaseRequestRequestTypeDef
):
    pass

UpdateKxDatabaseResponseTypeDef = TypedDict(
    "UpdateKxDatabaseResponseTypeDef",
    {
        "databaseName": str,
        "environmentId": str,
        "description": str,
        "lastModifiedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateKxEnvironmentNetworkRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateKxEnvironmentNetworkRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)
_OptionalUpdateKxEnvironmentNetworkRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateKxEnvironmentNetworkRequestRequestTypeDef",
    {
        "transitGatewayConfiguration": "TransitGatewayConfigurationTypeDef",
        "customDNSConfiguration": List["CustomDNSServerTypeDef"],
        "clientToken": str,
    },
    total=False,
)

class UpdateKxEnvironmentNetworkRequestRequestTypeDef(
    _RequiredUpdateKxEnvironmentNetworkRequestRequestTypeDef,
    _OptionalUpdateKxEnvironmentNetworkRequestRequestTypeDef,
):
    pass

UpdateKxEnvironmentNetworkResponseTypeDef = TypedDict(
    "UpdateKxEnvironmentNetworkResponseTypeDef",
    {
        "name": str,
        "environmentId": str,
        "awsAccountId": str,
        "status": EnvironmentStatusType,
        "tgwStatus": tgwStatusType,
        "dnsStatus": dnsStatusType,
        "errorMessage": str,
        "description": str,
        "environmentArn": str,
        "kmsKeyId": str,
        "dedicatedServiceAccountId": str,
        "transitGatewayConfiguration": "TransitGatewayConfigurationTypeDef",
        "customDNSConfiguration": List["CustomDNSServerTypeDef"],
        "creationTimestamp": datetime,
        "updateTimestamp": datetime,
        "availabilityZoneIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateKxEnvironmentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateKxEnvironmentRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)
_OptionalUpdateKxEnvironmentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateKxEnvironmentRequestRequestTypeDef",
    {
        "name": str,
        "description": str,
        "clientToken": str,
    },
    total=False,
)

class UpdateKxEnvironmentRequestRequestTypeDef(
    _RequiredUpdateKxEnvironmentRequestRequestTypeDef,
    _OptionalUpdateKxEnvironmentRequestRequestTypeDef,
):
    pass

UpdateKxEnvironmentResponseTypeDef = TypedDict(
    "UpdateKxEnvironmentResponseTypeDef",
    {
        "name": str,
        "environmentId": str,
        "awsAccountId": str,
        "status": EnvironmentStatusType,
        "tgwStatus": tgwStatusType,
        "dnsStatus": dnsStatusType,
        "errorMessage": str,
        "description": str,
        "environmentArn": str,
        "kmsKeyId": str,
        "dedicatedServiceAccountId": str,
        "transitGatewayConfiguration": "TransitGatewayConfigurationTypeDef",
        "customDNSConfiguration": List["CustomDNSServerTypeDef"],
        "creationTimestamp": datetime,
        "updateTimestamp": datetime,
        "availabilityZoneIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateKxUserRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateKxUserRequestRequestTypeDef",
    {
        "environmentId": str,
        "userName": str,
        "iamRole": str,
    },
)
_OptionalUpdateKxUserRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateKxUserRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class UpdateKxUserRequestRequestTypeDef(
    _RequiredUpdateKxUserRequestRequestTypeDef, _OptionalUpdateKxUserRequestRequestTypeDef
):
    pass

UpdateKxUserResponseTypeDef = TypedDict(
    "UpdateKxUserResponseTypeDef",
    {
        "userName": str,
        "userArn": str,
        "environmentId": str,
        "iamRole": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "vpcId": str,
        "securityGroupIds": List[str],
        "subnetIds": List[str],
        "ipAddressType": Literal["IP_V4"],
    },
    total=False,
)
