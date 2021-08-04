"""
Type annotations for docdb service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/type_defs.html)

Usage::

    ```python
    from mypy_boto3_docdb.type_defs import AddSourceIdentifierToSubscriptionMessageRequestTypeDef

    data: AddSourceIdentifierToSubscriptionMessageRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import ApplyMethodType, SourceTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AddSourceIdentifierToSubscriptionMessageRequestTypeDef",
    "AddSourceIdentifierToSubscriptionResultTypeDef",
    "AddTagsToResourceMessageRequestTypeDef",
    "ApplyPendingMaintenanceActionMessageRequestTypeDef",
    "ApplyPendingMaintenanceActionResultTypeDef",
    "AvailabilityZoneTypeDef",
    "CertificateMessageTypeDef",
    "CertificateTypeDef",
    "CloudwatchLogsExportConfigurationTypeDef",
    "CopyDBClusterParameterGroupMessageRequestTypeDef",
    "CopyDBClusterParameterGroupResultTypeDef",
    "CopyDBClusterSnapshotMessageRequestTypeDef",
    "CopyDBClusterSnapshotResultTypeDef",
    "CreateDBClusterMessageRequestTypeDef",
    "CreateDBClusterParameterGroupMessageRequestTypeDef",
    "CreateDBClusterParameterGroupResultTypeDef",
    "CreateDBClusterResultTypeDef",
    "CreateDBClusterSnapshotMessageRequestTypeDef",
    "CreateDBClusterSnapshotResultTypeDef",
    "CreateDBInstanceMessageRequestTypeDef",
    "CreateDBInstanceResultTypeDef",
    "CreateDBSubnetGroupMessageRequestTypeDef",
    "CreateDBSubnetGroupResultTypeDef",
    "CreateEventSubscriptionMessageRequestTypeDef",
    "CreateEventSubscriptionResultTypeDef",
    "CreateGlobalClusterMessageRequestTypeDef",
    "CreateGlobalClusterResultTypeDef",
    "DBClusterMemberTypeDef",
    "DBClusterMessageTypeDef",
    "DBClusterParameterGroupDetailsTypeDef",
    "DBClusterParameterGroupNameMessageTypeDef",
    "DBClusterParameterGroupTypeDef",
    "DBClusterParameterGroupsMessageTypeDef",
    "DBClusterRoleTypeDef",
    "DBClusterSnapshotAttributeTypeDef",
    "DBClusterSnapshotAttributesResultTypeDef",
    "DBClusterSnapshotMessageTypeDef",
    "DBClusterSnapshotTypeDef",
    "DBClusterTypeDef",
    "DBEngineVersionMessageTypeDef",
    "DBEngineVersionTypeDef",
    "DBInstanceMessageTypeDef",
    "DBInstanceStatusInfoTypeDef",
    "DBInstanceTypeDef",
    "DBSubnetGroupMessageTypeDef",
    "DBSubnetGroupTypeDef",
    "DeleteDBClusterMessageRequestTypeDef",
    "DeleteDBClusterParameterGroupMessageRequestTypeDef",
    "DeleteDBClusterResultTypeDef",
    "DeleteDBClusterSnapshotMessageRequestTypeDef",
    "DeleteDBClusterSnapshotResultTypeDef",
    "DeleteDBInstanceMessageRequestTypeDef",
    "DeleteDBInstanceResultTypeDef",
    "DeleteDBSubnetGroupMessageRequestTypeDef",
    "DeleteEventSubscriptionMessageRequestTypeDef",
    "DeleteEventSubscriptionResultTypeDef",
    "DeleteGlobalClusterMessageRequestTypeDef",
    "DeleteGlobalClusterResultTypeDef",
    "DescribeCertificatesMessageRequestTypeDef",
    "DescribeDBClusterParameterGroupsMessageRequestTypeDef",
    "DescribeDBClusterParametersMessageRequestTypeDef",
    "DescribeDBClusterSnapshotAttributesMessageRequestTypeDef",
    "DescribeDBClusterSnapshotAttributesResultTypeDef",
    "DescribeDBClusterSnapshotsMessageRequestTypeDef",
    "DescribeDBClustersMessageRequestTypeDef",
    "DescribeDBEngineVersionsMessageRequestTypeDef",
    "DescribeDBInstancesMessageRequestTypeDef",
    "DescribeDBSubnetGroupsMessageRequestTypeDef",
    "DescribeEngineDefaultClusterParametersMessageRequestTypeDef",
    "DescribeEngineDefaultClusterParametersResultTypeDef",
    "DescribeEventCategoriesMessageRequestTypeDef",
    "DescribeEventSubscriptionsMessageRequestTypeDef",
    "DescribeEventsMessageRequestTypeDef",
    "DescribeGlobalClustersMessageRequestTypeDef",
    "DescribeOrderableDBInstanceOptionsMessageRequestTypeDef",
    "DescribePendingMaintenanceActionsMessageRequestTypeDef",
    "EndpointTypeDef",
    "EngineDefaultsTypeDef",
    "EventCategoriesMapTypeDef",
    "EventCategoriesMessageTypeDef",
    "EventSubscriptionTypeDef",
    "EventSubscriptionsMessageTypeDef",
    "EventTypeDef",
    "EventsMessageTypeDef",
    "FailoverDBClusterMessageRequestTypeDef",
    "FailoverDBClusterResultTypeDef",
    "FilterTypeDef",
    "GlobalClusterMemberTypeDef",
    "GlobalClusterTypeDef",
    "GlobalClustersMessageTypeDef",
    "ListTagsForResourceMessageRequestTypeDef",
    "ModifyDBClusterMessageRequestTypeDef",
    "ModifyDBClusterParameterGroupMessageRequestTypeDef",
    "ModifyDBClusterResultTypeDef",
    "ModifyDBClusterSnapshotAttributeMessageRequestTypeDef",
    "ModifyDBClusterSnapshotAttributeResultTypeDef",
    "ModifyDBInstanceMessageRequestTypeDef",
    "ModifyDBInstanceResultTypeDef",
    "ModifyDBSubnetGroupMessageRequestTypeDef",
    "ModifyDBSubnetGroupResultTypeDef",
    "ModifyEventSubscriptionMessageRequestTypeDef",
    "ModifyEventSubscriptionResultTypeDef",
    "ModifyGlobalClusterMessageRequestTypeDef",
    "ModifyGlobalClusterResultTypeDef",
    "OrderableDBInstanceOptionTypeDef",
    "OrderableDBInstanceOptionsMessageTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterTypeDef",
    "PendingCloudwatchLogsExportsTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PendingMaintenanceActionsMessageTypeDef",
    "PendingModifiedValuesTypeDef",
    "RebootDBInstanceMessageRequestTypeDef",
    "RebootDBInstanceResultTypeDef",
    "RemoveFromGlobalClusterMessageRequestTypeDef",
    "RemoveFromGlobalClusterResultTypeDef",
    "RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef",
    "RemoveSourceIdentifierFromSubscriptionResultTypeDef",
    "RemoveTagsFromResourceMessageRequestTypeDef",
    "ResetDBClusterParameterGroupMessageRequestTypeDef",
    "ResourcePendingMaintenanceActionsTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreDBClusterFromSnapshotMessageRequestTypeDef",
    "RestoreDBClusterFromSnapshotResultTypeDef",
    "RestoreDBClusterToPointInTimeMessageRequestTypeDef",
    "RestoreDBClusterToPointInTimeResultTypeDef",
    "StartDBClusterMessageRequestTypeDef",
    "StartDBClusterResultTypeDef",
    "StopDBClusterMessageRequestTypeDef",
    "StopDBClusterResultTypeDef",
    "SubnetTypeDef",
    "TagListMessageTypeDef",
    "TagTypeDef",
    "UpgradeTargetTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WaiterConfigTypeDef",
)

AddSourceIdentifierToSubscriptionMessageRequestTypeDef = TypedDict(
    "AddSourceIdentifierToSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "SourceIdentifier": str,
    },
)

AddSourceIdentifierToSubscriptionResultTypeDef = TypedDict(
    "AddSourceIdentifierToSubscriptionResultTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddTagsToResourceMessageRequestTypeDef = TypedDict(
    "AddTagsToResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
        "Tags": List["TagTypeDef"],
    },
)

ApplyPendingMaintenanceActionMessageRequestTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionMessageRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ApplyAction": str,
        "OptInType": str,
    },
)

ApplyPendingMaintenanceActionResultTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionResultTypeDef",
    {
        "ResourcePendingMaintenanceActions": "ResourcePendingMaintenanceActionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": str,
    },
    total=False,
)

CertificateMessageTypeDef = TypedDict(
    "CertificateMessageTypeDef",
    {
        "Certificates": List["CertificateTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificateType": str,
        "Thumbprint": str,
        "ValidFrom": datetime,
        "ValidTill": datetime,
        "CertificateArn": str,
    },
    total=False,
)

CloudwatchLogsExportConfigurationTypeDef = TypedDict(
    "CloudwatchLogsExportConfigurationTypeDef",
    {
        "EnableLogTypes": List[str],
        "DisableLogTypes": List[str],
    },
    total=False,
)

_RequiredCopyDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCopyDBClusterParameterGroupMessageRequestTypeDef",
    {
        "SourceDBClusterParameterGroupIdentifier": str,
        "TargetDBClusterParameterGroupIdentifier": str,
        "TargetDBClusterParameterGroupDescription": str,
    },
)
_OptionalCopyDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCopyDBClusterParameterGroupMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CopyDBClusterParameterGroupMessageRequestTypeDef(
    _RequiredCopyDBClusterParameterGroupMessageRequestTypeDef,
    _OptionalCopyDBClusterParameterGroupMessageRequestTypeDef,
):
    pass

CopyDBClusterParameterGroupResultTypeDef = TypedDict(
    "CopyDBClusterParameterGroupResultTypeDef",
    {
        "DBClusterParameterGroup": "DBClusterParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCopyDBClusterSnapshotMessageRequestTypeDef = TypedDict(
    "_RequiredCopyDBClusterSnapshotMessageRequestTypeDef",
    {
        "SourceDBClusterSnapshotIdentifier": str,
        "TargetDBClusterSnapshotIdentifier": str,
    },
)
_OptionalCopyDBClusterSnapshotMessageRequestTypeDef = TypedDict(
    "_OptionalCopyDBClusterSnapshotMessageRequestTypeDef",
    {
        "KmsKeyId": str,
        "PreSignedUrl": str,
        "CopyTags": bool,
        "Tags": List["TagTypeDef"],
        "SourceRegion": str,
    },
    total=False,
)

class CopyDBClusterSnapshotMessageRequestTypeDef(
    _RequiredCopyDBClusterSnapshotMessageRequestTypeDef,
    _OptionalCopyDBClusterSnapshotMessageRequestTypeDef,
):
    pass

CopyDBClusterSnapshotResultTypeDef = TypedDict(
    "CopyDBClusterSnapshotResultTypeDef",
    {
        "DBClusterSnapshot": "DBClusterSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDBClusterMessageRequestTypeDef = TypedDict(
    "_RequiredCreateDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "Engine": str,
    },
)
_OptionalCreateDBClusterMessageRequestTypeDef = TypedDict(
    "_OptionalCreateDBClusterMessageRequestTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterParameterGroupName": str,
        "VpcSecurityGroupIds": List[str],
        "DBSubnetGroupName": str,
        "EngineVersion": str,
        "Port": int,
        "MasterUsername": str,
        "MasterUserPassword": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "Tags": List["TagTypeDef"],
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "PreSignedUrl": str,
        "EnableCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
        "GlobalClusterIdentifier": str,
        "SourceRegion": str,
    },
    total=False,
)

class CreateDBClusterMessageRequestTypeDef(
    _RequiredCreateDBClusterMessageRequestTypeDef, _OptionalCreateDBClusterMessageRequestTypeDef
):
    pass

_RequiredCreateDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCreateDBClusterParameterGroupMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
    },
)
_OptionalCreateDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCreateDBClusterParameterGroupMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDBClusterParameterGroupMessageRequestTypeDef(
    _RequiredCreateDBClusterParameterGroupMessageRequestTypeDef,
    _OptionalCreateDBClusterParameterGroupMessageRequestTypeDef,
):
    pass

CreateDBClusterParameterGroupResultTypeDef = TypedDict(
    "CreateDBClusterParameterGroupResultTypeDef",
    {
        "DBClusterParameterGroup": "DBClusterParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDBClusterResultTypeDef = TypedDict(
    "CreateDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDBClusterSnapshotMessageRequestTypeDef = TypedDict(
    "_RequiredCreateDBClusterSnapshotMessageRequestTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
    },
)
_OptionalCreateDBClusterSnapshotMessageRequestTypeDef = TypedDict(
    "_OptionalCreateDBClusterSnapshotMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDBClusterSnapshotMessageRequestTypeDef(
    _RequiredCreateDBClusterSnapshotMessageRequestTypeDef,
    _OptionalCreateDBClusterSnapshotMessageRequestTypeDef,
):
    pass

CreateDBClusterSnapshotResultTypeDef = TypedDict(
    "CreateDBClusterSnapshotResultTypeDef",
    {
        "DBClusterSnapshot": "DBClusterSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDBInstanceMessageRequestTypeDef = TypedDict(
    "_RequiredCreateDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBClusterIdentifier": str,
    },
)
_OptionalCreateDBInstanceMessageRequestTypeDef = TypedDict(
    "_OptionalCreateDBInstanceMessageRequestTypeDef",
    {
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "AutoMinorVersionUpgrade": bool,
        "Tags": List["TagTypeDef"],
        "PromotionTier": int,
    },
    total=False,
)

class CreateDBInstanceMessageRequestTypeDef(
    _RequiredCreateDBInstanceMessageRequestTypeDef, _OptionalCreateDBInstanceMessageRequestTypeDef
):
    pass

CreateDBInstanceResultTypeDef = TypedDict(
    "CreateDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDBSubnetGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCreateDBSubnetGroupMessageRequestTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "SubnetIds": List[str],
    },
)
_OptionalCreateDBSubnetGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCreateDBSubnetGroupMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDBSubnetGroupMessageRequestTypeDef(
    _RequiredCreateDBSubnetGroupMessageRequestTypeDef,
    _OptionalCreateDBSubnetGroupMessageRequestTypeDef,
):
    pass

CreateDBSubnetGroupResultTypeDef = TypedDict(
    "CreateDBSubnetGroupResultTypeDef",
    {
        "DBSubnetGroup": "DBSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEventSubscriptionMessageRequestTypeDef = TypedDict(
    "_RequiredCreateEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "SnsTopicArn": str,
    },
)
_OptionalCreateEventSubscriptionMessageRequestTypeDef = TypedDict(
    "_OptionalCreateEventSubscriptionMessageRequestTypeDef",
    {
        "SourceType": str,
        "EventCategories": List[str],
        "SourceIds": List[str],
        "Enabled": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateEventSubscriptionMessageRequestTypeDef(
    _RequiredCreateEventSubscriptionMessageRequestTypeDef,
    _OptionalCreateEventSubscriptionMessageRequestTypeDef,
):
    pass

CreateEventSubscriptionResultTypeDef = TypedDict(
    "CreateEventSubscriptionResultTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGlobalClusterMessageRequestTypeDef = TypedDict(
    "_RequiredCreateGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
    },
)
_OptionalCreateGlobalClusterMessageRequestTypeDef = TypedDict(
    "_OptionalCreateGlobalClusterMessageRequestTypeDef",
    {
        "SourceDBClusterIdentifier": str,
        "Engine": str,
        "EngineVersion": str,
        "DeletionProtection": bool,
        "DatabaseName": str,
        "StorageEncrypted": bool,
    },
    total=False,
)

class CreateGlobalClusterMessageRequestTypeDef(
    _RequiredCreateGlobalClusterMessageRequestTypeDef,
    _OptionalCreateGlobalClusterMessageRequestTypeDef,
):
    pass

CreateGlobalClusterResultTypeDef = TypedDict(
    "CreateGlobalClusterResultTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterMemberTypeDef = TypedDict(
    "DBClusterMemberTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)

DBClusterMessageTypeDef = TypedDict(
    "DBClusterMessageTypeDef",
    {
        "Marker": str,
        "DBClusters": List["DBClusterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterParameterGroupDetailsTypeDef = TypedDict(
    "DBClusterParameterGroupDetailsTypeDef",
    {
        "Parameters": List["ParameterTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterParameterGroupNameMessageTypeDef = TypedDict(
    "DBClusterParameterGroupNameMessageTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterParameterGroupTypeDef = TypedDict(
    "DBClusterParameterGroupTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBClusterParameterGroupArn": str,
    },
    total=False,
)

DBClusterParameterGroupsMessageTypeDef = TypedDict(
    "DBClusterParameterGroupsMessageTypeDef",
    {
        "Marker": str,
        "DBClusterParameterGroups": List["DBClusterParameterGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterRoleTypeDef = TypedDict(
    "DBClusterRoleTypeDef",
    {
        "RoleArn": str,
        "Status": str,
    },
    total=False,
)

DBClusterSnapshotAttributeTypeDef = TypedDict(
    "DBClusterSnapshotAttributeTypeDef",
    {
        "AttributeName": str,
        "AttributeValues": List[str],
    },
    total=False,
)

DBClusterSnapshotAttributesResultTypeDef = TypedDict(
    "DBClusterSnapshotAttributesResultTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
        "DBClusterSnapshotAttributes": List["DBClusterSnapshotAttributeTypeDef"],
    },
    total=False,
)

DBClusterSnapshotMessageTypeDef = TypedDict(
    "DBClusterSnapshotMessageTypeDef",
    {
        "Marker": str,
        "DBClusterSnapshots": List["DBClusterSnapshotTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterSnapshotTypeDef = TypedDict(
    "DBClusterSnapshotTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
    },
    total=False,
)

DBClusterTypeDef = TypedDict(
    "DBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List["DBClusterMemberTypeDef"],
        "VpcSecurityGroups": List["VpcSecurityGroupMembershipTypeDef"],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List["DBClusterRoleTypeDef"],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)

DBEngineVersionMessageTypeDef = TypedDict(
    "DBEngineVersionMessageTypeDef",
    {
        "Marker": str,
        "DBEngineVersions": List["DBEngineVersionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBEngineVersionTypeDef = TypedDict(
    "DBEngineVersionTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBParameterGroupFamily": str,
        "DBEngineDescription": str,
        "DBEngineVersionDescription": str,
        "ValidUpgradeTarget": List["UpgradeTargetTypeDef"],
        "ExportableLogTypes": List[str],
        "SupportsLogExportsToCloudwatchLogs": bool,
    },
    total=False,
)

DBInstanceMessageTypeDef = TypedDict(
    "DBInstanceMessageTypeDef",
    {
        "Marker": str,
        "DBInstances": List["DBInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBInstanceStatusInfoTypeDef = TypedDict(
    "DBInstanceStatusInfoTypeDef",
    {
        "StatusType": str,
        "Normal": bool,
        "Status": str,
        "Message": str,
    },
    total=False,
)

DBInstanceTypeDef = TypedDict(
    "DBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "Endpoint": "EndpointTypeDef",
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "VpcSecurityGroups": List["VpcSecurityGroupMembershipTypeDef"],
        "AvailabilityZone": str,
        "DBSubnetGroup": "DBSubnetGroupTypeDef",
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": "PendingModifiedValuesTypeDef",
        "LatestRestorableTime": datetime,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "PubliclyAccessible": bool,
        "StatusInfos": List["DBInstanceStatusInfoTypeDef"],
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)

DBSubnetGroupMessageTypeDef = TypedDict(
    "DBSubnetGroupMessageTypeDef",
    {
        "Marker": str,
        "DBSubnetGroups": List["DBSubnetGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBSubnetGroupTypeDef = TypedDict(
    "DBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List["SubnetTypeDef"],
        "DBSubnetGroupArn": str,
    },
    total=False,
)

_RequiredDeleteDBClusterMessageRequestTypeDef = TypedDict(
    "_RequiredDeleteDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)
_OptionalDeleteDBClusterMessageRequestTypeDef = TypedDict(
    "_OptionalDeleteDBClusterMessageRequestTypeDef",
    {
        "SkipFinalSnapshot": bool,
        "FinalDBSnapshotIdentifier": str,
    },
    total=False,
)

class DeleteDBClusterMessageRequestTypeDef(
    _RequiredDeleteDBClusterMessageRequestTypeDef, _OptionalDeleteDBClusterMessageRequestTypeDef
):
    pass

DeleteDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "DeleteDBClusterParameterGroupMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
    },
)

DeleteDBClusterResultTypeDef = TypedDict(
    "DeleteDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDBClusterSnapshotMessageRequestTypeDef = TypedDict(
    "DeleteDBClusterSnapshotMessageRequestTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
    },
)

DeleteDBClusterSnapshotResultTypeDef = TypedDict(
    "DeleteDBClusterSnapshotResultTypeDef",
    {
        "DBClusterSnapshot": "DBClusterSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDBInstanceMessageRequestTypeDef = TypedDict(
    "DeleteDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)

DeleteDBInstanceResultTypeDef = TypedDict(
    "DeleteDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDBSubnetGroupMessageRequestTypeDef = TypedDict(
    "DeleteDBSubnetGroupMessageRequestTypeDef",
    {
        "DBSubnetGroupName": str,
    },
)

DeleteEventSubscriptionMessageRequestTypeDef = TypedDict(
    "DeleteEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
    },
)

DeleteEventSubscriptionResultTypeDef = TypedDict(
    "DeleteEventSubscriptionResultTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGlobalClusterMessageRequestTypeDef = TypedDict(
    "DeleteGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
    },
)

DeleteGlobalClusterResultTypeDef = TypedDict(
    "DeleteGlobalClusterResultTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCertificatesMessageRequestTypeDef = TypedDict(
    "DescribeCertificatesMessageRequestTypeDef",
    {
        "CertificateIdentifier": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeDBClusterParameterGroupsMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterParameterGroupsMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

_RequiredDescribeDBClusterParametersMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeDBClusterParametersMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
    },
)
_OptionalDescribeDBClusterParametersMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeDBClusterParametersMessageRequestTypeDef",
    {
        "Source": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

class DescribeDBClusterParametersMessageRequestTypeDef(
    _RequiredDescribeDBClusterParametersMessageRequestTypeDef,
    _OptionalDescribeDBClusterParametersMessageRequestTypeDef,
):
    pass

DescribeDBClusterSnapshotAttributesMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterSnapshotAttributesMessageRequestTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
    },
)

DescribeDBClusterSnapshotAttributesResultTypeDef = TypedDict(
    "DescribeDBClusterSnapshotAttributesResultTypeDef",
    {
        "DBClusterSnapshotAttributesResult": "DBClusterSnapshotAttributesResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDBClusterSnapshotsMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterSnapshotsMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "DBClusterSnapshotIdentifier": str,
        "SnapshotType": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
        "IncludeShared": bool,
        "IncludePublic": bool,
    },
    total=False,
)

DescribeDBClustersMessageRequestTypeDef = TypedDict(
    "DescribeDBClustersMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeDBEngineVersionsMessageRequestTypeDef = TypedDict(
    "DescribeDBEngineVersionsMessageRequestTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBParameterGroupFamily": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
        "DefaultOnly": bool,
        "ListSupportedCharacterSets": bool,
        "ListSupportedTimezones": bool,
    },
    total=False,
)

DescribeDBInstancesMessageRequestTypeDef = TypedDict(
    "DescribeDBInstancesMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeDBSubnetGroupsMessageRequestTypeDef = TypedDict(
    "DescribeDBSubnetGroupsMessageRequestTypeDef",
    {
        "DBSubnetGroupName": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

_RequiredDescribeEngineDefaultClusterParametersMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeEngineDefaultClusterParametersMessageRequestTypeDef",
    {
        "DBParameterGroupFamily": str,
    },
)
_OptionalDescribeEngineDefaultClusterParametersMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeEngineDefaultClusterParametersMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

class DescribeEngineDefaultClusterParametersMessageRequestTypeDef(
    _RequiredDescribeEngineDefaultClusterParametersMessageRequestTypeDef,
    _OptionalDescribeEngineDefaultClusterParametersMessageRequestTypeDef,
):
    pass

DescribeEngineDefaultClusterParametersResultTypeDef = TypedDict(
    "DescribeEngineDefaultClusterParametersResultTypeDef",
    {
        "EngineDefaults": "EngineDefaultsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventCategoriesMessageRequestTypeDef = TypedDict(
    "DescribeEventCategoriesMessageRequestTypeDef",
    {
        "SourceType": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

DescribeEventSubscriptionsMessageRequestTypeDef = TypedDict(
    "DescribeEventSubscriptionsMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeEventsMessageRequestTypeDef = TypedDict(
    "DescribeEventsMessageRequestTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": SourceTypeType,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Duration": int,
        "EventCategories": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeGlobalClustersMessageRequestTypeDef = TypedDict(
    "DescribeGlobalClustersMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

_RequiredDescribeOrderableDBInstanceOptionsMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeOrderableDBInstanceOptionsMessageRequestTypeDef",
    {
        "Engine": str,
    },
)
_OptionalDescribeOrderableDBInstanceOptionsMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeOrderableDBInstanceOptionsMessageRequestTypeDef",
    {
        "EngineVersion": str,
        "DBInstanceClass": str,
        "LicenseModel": str,
        "Vpc": bool,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

class DescribeOrderableDBInstanceOptionsMessageRequestTypeDef(
    _RequiredDescribeOrderableDBInstanceOptionsMessageRequestTypeDef,
    _OptionalDescribeOrderableDBInstanceOptionsMessageRequestTypeDef,
):
    pass

DescribePendingMaintenanceActionsMessageRequestTypeDef = TypedDict(
    "DescribePendingMaintenanceActionsMessageRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "Port": int,
        "HostedZoneId": str,
    },
    total=False,
)

EngineDefaultsTypeDef = TypedDict(
    "EngineDefaultsTypeDef",
    {
        "DBParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List["ParameterTypeDef"],
    },
    total=False,
)

EventCategoriesMapTypeDef = TypedDict(
    "EventCategoriesMapTypeDef",
    {
        "SourceType": str,
        "EventCategories": List[str],
    },
    total=False,
)

EventCategoriesMessageTypeDef = TypedDict(
    "EventCategoriesMessageTypeDef",
    {
        "EventCategoriesMapList": List["EventCategoriesMapTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EventSubscriptionTypeDef = TypedDict(
    "EventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
        "EventSubscriptionArn": str,
    },
    total=False,
)

EventSubscriptionsMessageTypeDef = TypedDict(
    "EventSubscriptionsMessageTypeDef",
    {
        "Marker": str,
        "EventSubscriptionsList": List["EventSubscriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": SourceTypeType,
        "Message": str,
        "EventCategories": List[str],
        "Date": datetime,
        "SourceArn": str,
    },
    total=False,
)

EventsMessageTypeDef = TypedDict(
    "EventsMessageTypeDef",
    {
        "Marker": str,
        "Events": List["EventTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailoverDBClusterMessageRequestTypeDef = TypedDict(
    "FailoverDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "TargetDBInstanceIdentifier": str,
    },
    total=False,
)

FailoverDBClusterResultTypeDef = TypedDict(
    "FailoverDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
)

GlobalClusterMemberTypeDef = TypedDict(
    "GlobalClusterMemberTypeDef",
    {
        "DBClusterArn": str,
        "Readers": List[str],
        "IsWriter": bool,
    },
    total=False,
)

GlobalClusterTypeDef = TypedDict(
    "GlobalClusterTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "GlobalClusterResourceId": str,
        "GlobalClusterArn": str,
        "Status": str,
        "Engine": str,
        "EngineVersion": str,
        "DatabaseName": str,
        "StorageEncrypted": bool,
        "DeletionProtection": bool,
        "GlobalClusterMembers": List["GlobalClusterMemberTypeDef"],
    },
    total=False,
)

GlobalClustersMessageTypeDef = TypedDict(
    "GlobalClustersMessageTypeDef",
    {
        "Marker": str,
        "GlobalClusters": List["GlobalClusterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceMessageRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
    },
)
_OptionalListTagsForResourceMessageRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

class ListTagsForResourceMessageRequestTypeDef(
    _RequiredListTagsForResourceMessageRequestTypeDef,
    _OptionalListTagsForResourceMessageRequestTypeDef,
):
    pass

_RequiredModifyDBClusterMessageRequestTypeDef = TypedDict(
    "_RequiredModifyDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)
_OptionalModifyDBClusterMessageRequestTypeDef = TypedDict(
    "_OptionalModifyDBClusterMessageRequestTypeDef",
    {
        "NewDBClusterIdentifier": str,
        "ApplyImmediately": bool,
        "BackupRetentionPeriod": int,
        "DBClusterParameterGroupName": str,
        "VpcSecurityGroupIds": List[str],
        "Port": int,
        "MasterUserPassword": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "CloudwatchLogsExportConfiguration": "CloudwatchLogsExportConfigurationTypeDef",
        "EngineVersion": str,
        "DeletionProtection": bool,
    },
    total=False,
)

class ModifyDBClusterMessageRequestTypeDef(
    _RequiredModifyDBClusterMessageRequestTypeDef, _OptionalModifyDBClusterMessageRequestTypeDef
):
    pass

ModifyDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "ModifyDBClusterParameterGroupMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "Parameters": List["ParameterTypeDef"],
    },
)

ModifyDBClusterResultTypeDef = TypedDict(
    "ModifyDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyDBClusterSnapshotAttributeMessageRequestTypeDef = TypedDict(
    "_RequiredModifyDBClusterSnapshotAttributeMessageRequestTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
        "AttributeName": str,
    },
)
_OptionalModifyDBClusterSnapshotAttributeMessageRequestTypeDef = TypedDict(
    "_OptionalModifyDBClusterSnapshotAttributeMessageRequestTypeDef",
    {
        "ValuesToAdd": List[str],
        "ValuesToRemove": List[str],
    },
    total=False,
)

class ModifyDBClusterSnapshotAttributeMessageRequestTypeDef(
    _RequiredModifyDBClusterSnapshotAttributeMessageRequestTypeDef,
    _OptionalModifyDBClusterSnapshotAttributeMessageRequestTypeDef,
):
    pass

ModifyDBClusterSnapshotAttributeResultTypeDef = TypedDict(
    "ModifyDBClusterSnapshotAttributeResultTypeDef",
    {
        "DBClusterSnapshotAttributesResult": "DBClusterSnapshotAttributesResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyDBInstanceMessageRequestTypeDef = TypedDict(
    "_RequiredModifyDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)
_OptionalModifyDBInstanceMessageRequestTypeDef = TypedDict(
    "_OptionalModifyDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceClass": str,
        "ApplyImmediately": bool,
        "PreferredMaintenanceWindow": str,
        "AutoMinorVersionUpgrade": bool,
        "NewDBInstanceIdentifier": str,
        "CACertificateIdentifier": str,
        "PromotionTier": int,
    },
    total=False,
)

class ModifyDBInstanceMessageRequestTypeDef(
    _RequiredModifyDBInstanceMessageRequestTypeDef, _OptionalModifyDBInstanceMessageRequestTypeDef
):
    pass

ModifyDBInstanceResultTypeDef = TypedDict(
    "ModifyDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyDBSubnetGroupMessageRequestTypeDef = TypedDict(
    "_RequiredModifyDBSubnetGroupMessageRequestTypeDef",
    {
        "DBSubnetGroupName": str,
        "SubnetIds": List[str],
    },
)
_OptionalModifyDBSubnetGroupMessageRequestTypeDef = TypedDict(
    "_OptionalModifyDBSubnetGroupMessageRequestTypeDef",
    {
        "DBSubnetGroupDescription": str,
    },
    total=False,
)

class ModifyDBSubnetGroupMessageRequestTypeDef(
    _RequiredModifyDBSubnetGroupMessageRequestTypeDef,
    _OptionalModifyDBSubnetGroupMessageRequestTypeDef,
):
    pass

ModifyDBSubnetGroupResultTypeDef = TypedDict(
    "ModifyDBSubnetGroupResultTypeDef",
    {
        "DBSubnetGroup": "DBSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyEventSubscriptionMessageRequestTypeDef = TypedDict(
    "_RequiredModifyEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
    },
)
_OptionalModifyEventSubscriptionMessageRequestTypeDef = TypedDict(
    "_OptionalModifyEventSubscriptionMessageRequestTypeDef",
    {
        "SnsTopicArn": str,
        "SourceType": str,
        "EventCategories": List[str],
        "Enabled": bool,
    },
    total=False,
)

class ModifyEventSubscriptionMessageRequestTypeDef(
    _RequiredModifyEventSubscriptionMessageRequestTypeDef,
    _OptionalModifyEventSubscriptionMessageRequestTypeDef,
):
    pass

ModifyEventSubscriptionResultTypeDef = TypedDict(
    "ModifyEventSubscriptionResultTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyGlobalClusterMessageRequestTypeDef = TypedDict(
    "_RequiredModifyGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
    },
)
_OptionalModifyGlobalClusterMessageRequestTypeDef = TypedDict(
    "_OptionalModifyGlobalClusterMessageRequestTypeDef",
    {
        "NewGlobalClusterIdentifier": str,
        "DeletionProtection": bool,
    },
    total=False,
)

class ModifyGlobalClusterMessageRequestTypeDef(
    _RequiredModifyGlobalClusterMessageRequestTypeDef,
    _OptionalModifyGlobalClusterMessageRequestTypeDef,
):
    pass

ModifyGlobalClusterResultTypeDef = TypedDict(
    "ModifyGlobalClusterResultTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OrderableDBInstanceOptionTypeDef = TypedDict(
    "OrderableDBInstanceOptionTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBInstanceClass": str,
        "LicenseModel": str,
        "AvailabilityZones": List["AvailabilityZoneTypeDef"],
        "Vpc": bool,
    },
    total=False,
)

OrderableDBInstanceOptionsMessageTypeDef = TypedDict(
    "OrderableDBInstanceOptionsMessageTypeDef",
    {
        "OrderableDBInstanceOptions": List["OrderableDBInstanceOptionTypeDef"],
        "Marker": str,
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

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": ApplyMethodType,
    },
    total=False,
)

PendingCloudwatchLogsExportsTypeDef = TypedDict(
    "PendingCloudwatchLogsExportsTypeDef",
    {
        "LogTypesToEnable": List[str],
        "LogTypesToDisable": List[str],
    },
    total=False,
)

PendingMaintenanceActionTypeDef = TypedDict(
    "PendingMaintenanceActionTypeDef",
    {
        "Action": str,
        "AutoAppliedAfterDate": datetime,
        "ForcedApplyDate": datetime,
        "OptInStatus": str,
        "CurrentApplyDate": datetime,
        "Description": str,
    },
    total=False,
)

PendingMaintenanceActionsMessageTypeDef = TypedDict(
    "PendingMaintenanceActionsMessageTypeDef",
    {
        "PendingMaintenanceActions": List["ResourcePendingMaintenanceActionsTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PendingModifiedValuesTypeDef = TypedDict(
    "PendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": "PendingCloudwatchLogsExportsTypeDef",
    },
    total=False,
)

_RequiredRebootDBInstanceMessageRequestTypeDef = TypedDict(
    "_RequiredRebootDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)
_OptionalRebootDBInstanceMessageRequestTypeDef = TypedDict(
    "_OptionalRebootDBInstanceMessageRequestTypeDef",
    {
        "ForceFailover": bool,
    },
    total=False,
)

class RebootDBInstanceMessageRequestTypeDef(
    _RequiredRebootDBInstanceMessageRequestTypeDef, _OptionalRebootDBInstanceMessageRequestTypeDef
):
    pass

RebootDBInstanceResultTypeDef = TypedDict(
    "RebootDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveFromGlobalClusterMessageRequestTypeDef = TypedDict(
    "RemoveFromGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "DbClusterIdentifier": str,
    },
)

RemoveFromGlobalClusterResultTypeDef = TypedDict(
    "RemoveFromGlobalClusterResultTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef = TypedDict(
    "RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "SourceIdentifier": str,
    },
)

RemoveSourceIdentifierFromSubscriptionResultTypeDef = TypedDict(
    "RemoveSourceIdentifierFromSubscriptionResultTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveTagsFromResourceMessageRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
        "TagKeys": List[str],
    },
)

_RequiredResetDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "_RequiredResetDBClusterParameterGroupMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
    },
)
_OptionalResetDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "_OptionalResetDBClusterParameterGroupMessageRequestTypeDef",
    {
        "ResetAllParameters": bool,
        "Parameters": List["ParameterTypeDef"],
    },
    total=False,
)

class ResetDBClusterParameterGroupMessageRequestTypeDef(
    _RequiredResetDBClusterParameterGroupMessageRequestTypeDef,
    _OptionalResetDBClusterParameterGroupMessageRequestTypeDef,
):
    pass

ResourcePendingMaintenanceActionsTypeDef = TypedDict(
    "ResourcePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List["PendingMaintenanceActionTypeDef"],
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

_RequiredRestoreDBClusterFromSnapshotMessageRequestTypeDef = TypedDict(
    "_RequiredRestoreDBClusterFromSnapshotMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "SnapshotIdentifier": str,
        "Engine": str,
    },
)
_OptionalRestoreDBClusterFromSnapshotMessageRequestTypeDef = TypedDict(
    "_OptionalRestoreDBClusterFromSnapshotMessageRequestTypeDef",
    {
        "AvailabilityZones": List[str],
        "EngineVersion": str,
        "Port": int,
        "DBSubnetGroupName": str,
        "VpcSecurityGroupIds": List[str],
        "Tags": List["TagTypeDef"],
        "KmsKeyId": str,
        "EnableCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)

class RestoreDBClusterFromSnapshotMessageRequestTypeDef(
    _RequiredRestoreDBClusterFromSnapshotMessageRequestTypeDef,
    _OptionalRestoreDBClusterFromSnapshotMessageRequestTypeDef,
):
    pass

RestoreDBClusterFromSnapshotResultTypeDef = TypedDict(
    "RestoreDBClusterFromSnapshotResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRestoreDBClusterToPointInTimeMessageRequestTypeDef = TypedDict(
    "_RequiredRestoreDBClusterToPointInTimeMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "SourceDBClusterIdentifier": str,
    },
)
_OptionalRestoreDBClusterToPointInTimeMessageRequestTypeDef = TypedDict(
    "_OptionalRestoreDBClusterToPointInTimeMessageRequestTypeDef",
    {
        "RestoreToTime": Union[datetime, str],
        "UseLatestRestorableTime": bool,
        "Port": int,
        "DBSubnetGroupName": str,
        "VpcSecurityGroupIds": List[str],
        "Tags": List["TagTypeDef"],
        "KmsKeyId": str,
        "EnableCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)

class RestoreDBClusterToPointInTimeMessageRequestTypeDef(
    _RequiredRestoreDBClusterToPointInTimeMessageRequestTypeDef,
    _OptionalRestoreDBClusterToPointInTimeMessageRequestTypeDef,
):
    pass

RestoreDBClusterToPointInTimeResultTypeDef = TypedDict(
    "RestoreDBClusterToPointInTimeResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartDBClusterMessageRequestTypeDef = TypedDict(
    "StartDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)

StartDBClusterResultTypeDef = TypedDict(
    "StartDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopDBClusterMessageRequestTypeDef = TypedDict(
    "StopDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)

StopDBClusterResultTypeDef = TypedDict(
    "StopDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": "AvailabilityZoneTypeDef",
        "SubnetStatus": str,
    },
    total=False,
)

TagListMessageTypeDef = TypedDict(
    "TagListMessageTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

UpgradeTargetTypeDef = TypedDict(
    "UpgradeTargetTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "Description": str,
        "AutoUpgrade": bool,
        "IsMajorVersionUpgrade": bool,
    },
    total=False,
)

VpcSecurityGroupMembershipTypeDef = TypedDict(
    "VpcSecurityGroupMembershipTypeDef",
    {
        "VpcSecurityGroupId": str,
        "Status": str,
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
