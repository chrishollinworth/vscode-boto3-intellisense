"""
Type annotations for neptune service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/type_defs.html)

Usage::

    ```python
    from mypy_boto3_neptune.type_defs import AddRoleToDBClusterMessageRequestTypeDef

    data: AddRoleToDBClusterMessageRequestTypeDef = {...}
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
    "AddRoleToDBClusterMessageRequestTypeDef",
    "AddSourceIdentifierToSubscriptionMessageRequestTypeDef",
    "AddSourceIdentifierToSubscriptionResultTypeDef",
    "AddTagsToResourceMessageRequestTypeDef",
    "ApplyPendingMaintenanceActionMessageRequestTypeDef",
    "ApplyPendingMaintenanceActionResultTypeDef",
    "AvailabilityZoneTypeDef",
    "CharacterSetTypeDef",
    "CloudwatchLogsExportConfigurationTypeDef",
    "CopyDBClusterParameterGroupMessageRequestTypeDef",
    "CopyDBClusterParameterGroupResultTypeDef",
    "CopyDBClusterSnapshotMessageRequestTypeDef",
    "CopyDBClusterSnapshotResultTypeDef",
    "CopyDBParameterGroupMessageRequestTypeDef",
    "CopyDBParameterGroupResultTypeDef",
    "CreateDBClusterEndpointMessageRequestTypeDef",
    "CreateDBClusterEndpointOutputTypeDef",
    "CreateDBClusterMessageRequestTypeDef",
    "CreateDBClusterParameterGroupMessageRequestTypeDef",
    "CreateDBClusterParameterGroupResultTypeDef",
    "CreateDBClusterResultTypeDef",
    "CreateDBClusterSnapshotMessageRequestTypeDef",
    "CreateDBClusterSnapshotResultTypeDef",
    "CreateDBInstanceMessageRequestTypeDef",
    "CreateDBInstanceResultTypeDef",
    "CreateDBParameterGroupMessageRequestTypeDef",
    "CreateDBParameterGroupResultTypeDef",
    "CreateDBSubnetGroupMessageRequestTypeDef",
    "CreateDBSubnetGroupResultTypeDef",
    "CreateEventSubscriptionMessageRequestTypeDef",
    "CreateEventSubscriptionResultTypeDef",
    "DBClusterEndpointMessageTypeDef",
    "DBClusterEndpointTypeDef",
    "DBClusterMemberTypeDef",
    "DBClusterMessageTypeDef",
    "DBClusterOptionGroupStatusTypeDef",
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
    "DBParameterGroupDetailsTypeDef",
    "DBParameterGroupNameMessageTypeDef",
    "DBParameterGroupStatusTypeDef",
    "DBParameterGroupTypeDef",
    "DBParameterGroupsMessageTypeDef",
    "DBSecurityGroupMembershipTypeDef",
    "DBSubnetGroupMessageTypeDef",
    "DBSubnetGroupTypeDef",
    "DeleteDBClusterEndpointMessageRequestTypeDef",
    "DeleteDBClusterEndpointOutputTypeDef",
    "DeleteDBClusterMessageRequestTypeDef",
    "DeleteDBClusterParameterGroupMessageRequestTypeDef",
    "DeleteDBClusterResultTypeDef",
    "DeleteDBClusterSnapshotMessageRequestTypeDef",
    "DeleteDBClusterSnapshotResultTypeDef",
    "DeleteDBInstanceMessageRequestTypeDef",
    "DeleteDBInstanceResultTypeDef",
    "DeleteDBParameterGroupMessageRequestTypeDef",
    "DeleteDBSubnetGroupMessageRequestTypeDef",
    "DeleteEventSubscriptionMessageRequestTypeDef",
    "DeleteEventSubscriptionResultTypeDef",
    "DescribeDBClusterEndpointsMessageRequestTypeDef",
    "DescribeDBClusterParameterGroupsMessageRequestTypeDef",
    "DescribeDBClusterParametersMessageRequestTypeDef",
    "DescribeDBClusterSnapshotAttributesMessageRequestTypeDef",
    "DescribeDBClusterSnapshotAttributesResultTypeDef",
    "DescribeDBClusterSnapshotsMessageRequestTypeDef",
    "DescribeDBClustersMessageRequestTypeDef",
    "DescribeDBEngineVersionsMessageRequestTypeDef",
    "DescribeDBInstancesMessageRequestTypeDef",
    "DescribeDBParameterGroupsMessageRequestTypeDef",
    "DescribeDBParametersMessageRequestTypeDef",
    "DescribeDBSubnetGroupsMessageRequestTypeDef",
    "DescribeEngineDefaultClusterParametersMessageRequestTypeDef",
    "DescribeEngineDefaultClusterParametersResultTypeDef",
    "DescribeEngineDefaultParametersMessageRequestTypeDef",
    "DescribeEngineDefaultParametersResultTypeDef",
    "DescribeEventCategoriesMessageRequestTypeDef",
    "DescribeEventSubscriptionsMessageRequestTypeDef",
    "DescribeEventsMessageRequestTypeDef",
    "DescribeOrderableDBInstanceOptionsMessageRequestTypeDef",
    "DescribePendingMaintenanceActionsMessageRequestTypeDef",
    "DescribeValidDBInstanceModificationsMessageRequestTypeDef",
    "DescribeValidDBInstanceModificationsResultTypeDef",
    "DomainMembershipTypeDef",
    "DoubleRangeTypeDef",
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
    "ListTagsForResourceMessageRequestTypeDef",
    "ModifyDBClusterEndpointMessageRequestTypeDef",
    "ModifyDBClusterEndpointOutputTypeDef",
    "ModifyDBClusterMessageRequestTypeDef",
    "ModifyDBClusterParameterGroupMessageRequestTypeDef",
    "ModifyDBClusterResultTypeDef",
    "ModifyDBClusterSnapshotAttributeMessageRequestTypeDef",
    "ModifyDBClusterSnapshotAttributeResultTypeDef",
    "ModifyDBInstanceMessageRequestTypeDef",
    "ModifyDBInstanceResultTypeDef",
    "ModifyDBParameterGroupMessageRequestTypeDef",
    "ModifyDBSubnetGroupMessageRequestTypeDef",
    "ModifyDBSubnetGroupResultTypeDef",
    "ModifyEventSubscriptionMessageRequestTypeDef",
    "ModifyEventSubscriptionResultTypeDef",
    "OptionGroupMembershipTypeDef",
    "OrderableDBInstanceOptionTypeDef",
    "OrderableDBInstanceOptionsMessageTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterTypeDef",
    "PendingCloudwatchLogsExportsTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PendingMaintenanceActionsMessageTypeDef",
    "PendingModifiedValuesTypeDef",
    "PromoteReadReplicaDBClusterMessageRequestTypeDef",
    "PromoteReadReplicaDBClusterResultTypeDef",
    "RangeTypeDef",
    "RebootDBInstanceMessageRequestTypeDef",
    "RebootDBInstanceResultTypeDef",
    "RemoveRoleFromDBClusterMessageRequestTypeDef",
    "RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef",
    "RemoveSourceIdentifierFromSubscriptionResultTypeDef",
    "RemoveTagsFromResourceMessageRequestTypeDef",
    "ResetDBClusterParameterGroupMessageRequestTypeDef",
    "ResetDBParameterGroupMessageRequestTypeDef",
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
    "TimezoneTypeDef",
    "UpgradeTargetTypeDef",
    "ValidDBInstanceModificationsMessageTypeDef",
    "ValidStorageOptionsTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredAddRoleToDBClusterMessageRequestTypeDef = TypedDict(
    "_RequiredAddRoleToDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "RoleArn": str,
    },
)
_OptionalAddRoleToDBClusterMessageRequestTypeDef = TypedDict(
    "_OptionalAddRoleToDBClusterMessageRequestTypeDef",
    {
        "FeatureName": str,
    },
    total=False,
)

class AddRoleToDBClusterMessageRequestTypeDef(
    _RequiredAddRoleToDBClusterMessageRequestTypeDef,
    _OptionalAddRoleToDBClusterMessageRequestTypeDef,
):
    pass

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

CharacterSetTypeDef = TypedDict(
    "CharacterSetTypeDef",
    {
        "CharacterSetName": str,
        "CharacterSetDescription": str,
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

_RequiredCopyDBParameterGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCopyDBParameterGroupMessageRequestTypeDef",
    {
        "SourceDBParameterGroupIdentifier": str,
        "TargetDBParameterGroupIdentifier": str,
        "TargetDBParameterGroupDescription": str,
    },
)
_OptionalCopyDBParameterGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCopyDBParameterGroupMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CopyDBParameterGroupMessageRequestTypeDef(
    _RequiredCopyDBParameterGroupMessageRequestTypeDef,
    _OptionalCopyDBParameterGroupMessageRequestTypeDef,
):
    pass

CopyDBParameterGroupResultTypeDef = TypedDict(
    "CopyDBParameterGroupResultTypeDef",
    {
        "DBParameterGroup": "DBParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDBClusterEndpointMessageRequestTypeDef = TypedDict(
    "_RequiredCreateDBClusterEndpointMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "DBClusterEndpointIdentifier": str,
        "EndpointType": str,
    },
)
_OptionalCreateDBClusterEndpointMessageRequestTypeDef = TypedDict(
    "_OptionalCreateDBClusterEndpointMessageRequestTypeDef",
    {
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDBClusterEndpointMessageRequestTypeDef(
    _RequiredCreateDBClusterEndpointMessageRequestTypeDef,
    _OptionalCreateDBClusterEndpointMessageRequestTypeDef,
):
    pass

CreateDBClusterEndpointOutputTypeDef = TypedDict(
    "CreateDBClusterEndpointOutputTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "DBClusterIdentifier": str,
        "DBClusterEndpointResourceIdentifier": str,
        "Endpoint": str,
        "Status": str,
        "EndpointType": str,
        "CustomEndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "DBClusterEndpointArn": str,
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
        "CharacterSetName": str,
        "CopyTagsToSnapshot": bool,
        "DatabaseName": str,
        "DBClusterParameterGroupName": str,
        "VpcSecurityGroupIds": List[str],
        "DBSubnetGroupName": str,
        "EngineVersion": str,
        "Port": int,
        "MasterUsername": str,
        "MasterUserPassword": str,
        "OptionGroupName": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "Tags": List["TagTypeDef"],
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "PreSignedUrl": str,
        "EnableIAMDatabaseAuthentication": bool,
        "EnableCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
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
    },
)
_OptionalCreateDBInstanceMessageRequestTypeDef = TypedDict(
    "_OptionalCreateDBInstanceMessageRequestTypeDef",
    {
        "DBName": str,
        "AllocatedStorage": int,
        "MasterUsername": str,
        "MasterUserPassword": str,
        "DBSecurityGroups": List[str],
        "VpcSecurityGroupIds": List[str],
        "AvailabilityZone": str,
        "DBSubnetGroupName": str,
        "PreferredMaintenanceWindow": str,
        "DBParameterGroupName": str,
        "BackupRetentionPeriod": int,
        "PreferredBackupWindow": str,
        "Port": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupName": str,
        "CharacterSetName": str,
        "PubliclyAccessible": bool,
        "Tags": List["TagTypeDef"],
        "DBClusterIdentifier": str,
        "StorageType": str,
        "TdeCredentialArn": str,
        "TdeCredentialPassword": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "Domain": str,
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "MonitoringRoleArn": str,
        "DomainIAMRoleName": str,
        "PromotionTier": int,
        "Timezone": str,
        "EnableIAMDatabaseAuthentication": bool,
        "EnablePerformanceInsights": bool,
        "PerformanceInsightsKMSKeyId": str,
        "EnableCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
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

_RequiredCreateDBParameterGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCreateDBParameterGroupMessageRequestTypeDef",
    {
        "DBParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
    },
)
_OptionalCreateDBParameterGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCreateDBParameterGroupMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDBParameterGroupMessageRequestTypeDef(
    _RequiredCreateDBParameterGroupMessageRequestTypeDef,
    _OptionalCreateDBParameterGroupMessageRequestTypeDef,
):
    pass

CreateDBParameterGroupResultTypeDef = TypedDict(
    "CreateDBParameterGroupResultTypeDef",
    {
        "DBParameterGroup": "DBParameterGroupTypeDef",
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

DBClusterEndpointMessageTypeDef = TypedDict(
    "DBClusterEndpointMessageTypeDef",
    {
        "Marker": str,
        "DBClusterEndpoints": List["DBClusterEndpointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterEndpointTypeDef = TypedDict(
    "DBClusterEndpointTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "DBClusterIdentifier": str,
        "DBClusterEndpointResourceIdentifier": str,
        "Endpoint": str,
        "Status": str,
        "EndpointType": str,
        "CustomEndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "DBClusterEndpointArn": str,
    },
    total=False,
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

DBClusterOptionGroupStatusTypeDef = TypedDict(
    "DBClusterOptionGroupStatusTypeDef",
    {
        "DBClusterOptionGroupName": str,
        "Status": str,
    },
    total=False,
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
        "FeatureName": str,
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
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
        "IAMDatabaseAuthenticationEnabled": bool,
    },
    total=False,
)

DBClusterTypeDef = TypedDict(
    "DBClusterTypeDef",
    {
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
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
        "DBClusterOptionGroupMemberships": List["DBClusterOptionGroupStatusTypeDef"],
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
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "CopyTagsToSnapshot": bool,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
        "CrossAccountClone": bool,
        "AutomaticRestartTime": datetime,
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
        "DefaultCharacterSet": "CharacterSetTypeDef",
        "SupportedCharacterSets": List["CharacterSetTypeDef"],
        "ValidUpgradeTarget": List["UpgradeTargetTypeDef"],
        "SupportedTimezones": List["TimezoneTypeDef"],
        "ExportableLogTypes": List[str],
        "SupportsLogExportsToCloudwatchLogs": bool,
        "SupportsReadReplica": bool,
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
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": "EndpointTypeDef",
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List["DBSecurityGroupMembershipTypeDef"],
        "VpcSecurityGroups": List["VpcSecurityGroupMembershipTypeDef"],
        "DBParameterGroups": List["DBParameterGroupStatusTypeDef"],
        "AvailabilityZone": str,
        "DBSubnetGroup": "DBSubnetGroupTypeDef",
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": "PendingModifiedValuesTypeDef",
        "LatestRestorableTime": datetime,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "ReadReplicaSourceDBInstanceIdentifier": str,
        "ReadReplicaDBInstanceIdentifiers": List[str],
        "ReadReplicaDBClusterIdentifiers": List[str],
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": List["OptionGroupMembershipTypeDef"],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List["DBInstanceStatusInfoTypeDef"],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List["DomainMembershipTypeDef"],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "EnhancedMonitoringResourceArn": str,
        "MonitoringRoleArn": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKMSKeyId": str,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)

DBParameterGroupDetailsTypeDef = TypedDict(
    "DBParameterGroupDetailsTypeDef",
    {
        "Parameters": List["ParameterTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBParameterGroupNameMessageTypeDef = TypedDict(
    "DBParameterGroupNameMessageTypeDef",
    {
        "DBParameterGroupName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBParameterGroupStatusTypeDef = TypedDict(
    "DBParameterGroupStatusTypeDef",
    {
        "DBParameterGroupName": str,
        "ParameterApplyStatus": str,
    },
    total=False,
)

DBParameterGroupTypeDef = TypedDict(
    "DBParameterGroupTypeDef",
    {
        "DBParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBParameterGroupArn": str,
    },
    total=False,
)

DBParameterGroupsMessageTypeDef = TypedDict(
    "DBParameterGroupsMessageTypeDef",
    {
        "Marker": str,
        "DBParameterGroups": List["DBParameterGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBSecurityGroupMembershipTypeDef = TypedDict(
    "DBSecurityGroupMembershipTypeDef",
    {
        "DBSecurityGroupName": str,
        "Status": str,
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

DeleteDBClusterEndpointMessageRequestTypeDef = TypedDict(
    "DeleteDBClusterEndpointMessageRequestTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
    },
)

DeleteDBClusterEndpointOutputTypeDef = TypedDict(
    "DeleteDBClusterEndpointOutputTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "DBClusterIdentifier": str,
        "DBClusterEndpointResourceIdentifier": str,
        "Endpoint": str,
        "Status": str,
        "EndpointType": str,
        "CustomEndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "DBClusterEndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredDeleteDBInstanceMessageRequestTypeDef = TypedDict(
    "_RequiredDeleteDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)
_OptionalDeleteDBInstanceMessageRequestTypeDef = TypedDict(
    "_OptionalDeleteDBInstanceMessageRequestTypeDef",
    {
        "SkipFinalSnapshot": bool,
        "FinalDBSnapshotIdentifier": str,
    },
    total=False,
)

class DeleteDBInstanceMessageRequestTypeDef(
    _RequiredDeleteDBInstanceMessageRequestTypeDef, _OptionalDeleteDBInstanceMessageRequestTypeDef
):
    pass

DeleteDBInstanceResultTypeDef = TypedDict(
    "DeleteDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDBParameterGroupMessageRequestTypeDef = TypedDict(
    "DeleteDBParameterGroupMessageRequestTypeDef",
    {
        "DBParameterGroupName": str,
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

DescribeDBClusterEndpointsMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterEndpointsMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "DBClusterEndpointIdentifier": str,
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

DescribeDBParameterGroupsMessageRequestTypeDef = TypedDict(
    "DescribeDBParameterGroupsMessageRequestTypeDef",
    {
        "DBParameterGroupName": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

_RequiredDescribeDBParametersMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeDBParametersMessageRequestTypeDef",
    {
        "DBParameterGroupName": str,
    },
)
_OptionalDescribeDBParametersMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeDBParametersMessageRequestTypeDef",
    {
        "Source": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

class DescribeDBParametersMessageRequestTypeDef(
    _RequiredDescribeDBParametersMessageRequestTypeDef,
    _OptionalDescribeDBParametersMessageRequestTypeDef,
):
    pass

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

_RequiredDescribeEngineDefaultParametersMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeEngineDefaultParametersMessageRequestTypeDef",
    {
        "DBParameterGroupFamily": str,
    },
)
_OptionalDescribeEngineDefaultParametersMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeEngineDefaultParametersMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

class DescribeEngineDefaultParametersMessageRequestTypeDef(
    _RequiredDescribeEngineDefaultParametersMessageRequestTypeDef,
    _OptionalDescribeEngineDefaultParametersMessageRequestTypeDef,
):
    pass

DescribeEngineDefaultParametersResultTypeDef = TypedDict(
    "DescribeEngineDefaultParametersResultTypeDef",
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

DescribeValidDBInstanceModificationsMessageRequestTypeDef = TypedDict(
    "DescribeValidDBInstanceModificationsMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)

DescribeValidDBInstanceModificationsResultTypeDef = TypedDict(
    "DescribeValidDBInstanceModificationsResultTypeDef",
    {
        "ValidDBInstanceModificationsMessage": "ValidDBInstanceModificationsMessageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainMembershipTypeDef = TypedDict(
    "DomainMembershipTypeDef",
    {
        "Domain": str,
        "Status": str,
        "FQDN": str,
        "IAMRoleName": str,
    },
    total=False,
)

DoubleRangeTypeDef = TypedDict(
    "DoubleRangeTypeDef",
    {
        "From": float,
        "To": float,
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

_RequiredModifyDBClusterEndpointMessageRequestTypeDef = TypedDict(
    "_RequiredModifyDBClusterEndpointMessageRequestTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
    },
)
_OptionalModifyDBClusterEndpointMessageRequestTypeDef = TypedDict(
    "_OptionalModifyDBClusterEndpointMessageRequestTypeDef",
    {
        "EndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
    },
    total=False,
)

class ModifyDBClusterEndpointMessageRequestTypeDef(
    _RequiredModifyDBClusterEndpointMessageRequestTypeDef,
    _OptionalModifyDBClusterEndpointMessageRequestTypeDef,
):
    pass

ModifyDBClusterEndpointOutputTypeDef = TypedDict(
    "ModifyDBClusterEndpointOutputTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "DBClusterIdentifier": str,
        "DBClusterEndpointResourceIdentifier": str,
        "Endpoint": str,
        "Status": str,
        "EndpointType": str,
        "CustomEndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "DBClusterEndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

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
        "OptionGroupName": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "EnableIAMDatabaseAuthentication": bool,
        "CloudwatchLogsExportConfiguration": "CloudwatchLogsExportConfigurationTypeDef",
        "EngineVersion": str,
        "DeletionProtection": bool,
        "CopyTagsToSnapshot": bool,
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
        "AllocatedStorage": int,
        "DBInstanceClass": str,
        "DBSubnetGroupName": str,
        "DBSecurityGroups": List[str],
        "VpcSecurityGroupIds": List[str],
        "ApplyImmediately": bool,
        "MasterUserPassword": str,
        "DBParameterGroupName": str,
        "BackupRetentionPeriod": int,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AllowMajorVersionUpgrade": bool,
        "AutoMinorVersionUpgrade": bool,
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupName": str,
        "NewDBInstanceIdentifier": str,
        "StorageType": str,
        "TdeCredentialArn": str,
        "TdeCredentialPassword": str,
        "CACertificateIdentifier": str,
        "Domain": str,
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "DBPortNumber": int,
        "PubliclyAccessible": bool,
        "MonitoringRoleArn": str,
        "DomainIAMRoleName": str,
        "PromotionTier": int,
        "EnableIAMDatabaseAuthentication": bool,
        "EnablePerformanceInsights": bool,
        "PerformanceInsightsKMSKeyId": str,
        "CloudwatchLogsExportConfiguration": "CloudwatchLogsExportConfigurationTypeDef",
        "DeletionProtection": bool,
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

ModifyDBParameterGroupMessageRequestTypeDef = TypedDict(
    "ModifyDBParameterGroupMessageRequestTypeDef",
    {
        "DBParameterGroupName": str,
        "Parameters": List["ParameterTypeDef"],
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

OptionGroupMembershipTypeDef = TypedDict(
    "OptionGroupMembershipTypeDef",
    {
        "OptionGroupName": str,
        "Status": str,
    },
    total=False,
)

OrderableDBInstanceOptionTypeDef = TypedDict(
    "OrderableDBInstanceOptionTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBInstanceClass": str,
        "LicenseModel": str,
        "AvailabilityZones": List["AvailabilityZoneTypeDef"],
        "MultiAZCapable": bool,
        "ReadReplicaCapable": bool,
        "Vpc": bool,
        "SupportsStorageEncryption": bool,
        "StorageType": str,
        "SupportsIops": bool,
        "SupportsEnhancedMonitoring": bool,
        "SupportsIAMDatabaseAuthentication": bool,
        "SupportsPerformanceInsights": bool,
        "MinStorageSize": int,
        "MaxStorageSize": int,
        "MinIopsPerDbInstance": int,
        "MaxIopsPerDbInstance": int,
        "MinIopsPerGib": float,
        "MaxIopsPerGib": float,
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

PromoteReadReplicaDBClusterMessageRequestTypeDef = TypedDict(
    "PromoteReadReplicaDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)

PromoteReadReplicaDBClusterResultTypeDef = TypedDict(
    "PromoteReadReplicaDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "From": int,
        "To": int,
        "Step": int,
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

_RequiredRemoveRoleFromDBClusterMessageRequestTypeDef = TypedDict(
    "_RequiredRemoveRoleFromDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "RoleArn": str,
    },
)
_OptionalRemoveRoleFromDBClusterMessageRequestTypeDef = TypedDict(
    "_OptionalRemoveRoleFromDBClusterMessageRequestTypeDef",
    {
        "FeatureName": str,
    },
    total=False,
)

class RemoveRoleFromDBClusterMessageRequestTypeDef(
    _RequiredRemoveRoleFromDBClusterMessageRequestTypeDef,
    _OptionalRemoveRoleFromDBClusterMessageRequestTypeDef,
):
    pass

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

_RequiredResetDBParameterGroupMessageRequestTypeDef = TypedDict(
    "_RequiredResetDBParameterGroupMessageRequestTypeDef",
    {
        "DBParameterGroupName": str,
    },
)
_OptionalResetDBParameterGroupMessageRequestTypeDef = TypedDict(
    "_OptionalResetDBParameterGroupMessageRequestTypeDef",
    {
        "ResetAllParameters": bool,
        "Parameters": List["ParameterTypeDef"],
    },
    total=False,
)

class ResetDBParameterGroupMessageRequestTypeDef(
    _RequiredResetDBParameterGroupMessageRequestTypeDef,
    _OptionalResetDBParameterGroupMessageRequestTypeDef,
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
        "DatabaseName": str,
        "OptionGroupName": str,
        "VpcSecurityGroupIds": List[str],
        "Tags": List["TagTypeDef"],
        "KmsKeyId": str,
        "EnableIAMDatabaseAuthentication": bool,
        "EnableCloudwatchLogsExports": List[str],
        "DBClusterParameterGroupName": str,
        "DeletionProtection": bool,
        "CopyTagsToSnapshot": bool,
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
        "RestoreType": str,
        "RestoreToTime": Union[datetime, str],
        "UseLatestRestorableTime": bool,
        "Port": int,
        "DBSubnetGroupName": str,
        "OptionGroupName": str,
        "VpcSecurityGroupIds": List[str],
        "Tags": List["TagTypeDef"],
        "KmsKeyId": str,
        "EnableIAMDatabaseAuthentication": bool,
        "EnableCloudwatchLogsExports": List[str],
        "DBClusterParameterGroupName": str,
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

TimezoneTypeDef = TypedDict(
    "TimezoneTypeDef",
    {
        "TimezoneName": str,
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

ValidDBInstanceModificationsMessageTypeDef = TypedDict(
    "ValidDBInstanceModificationsMessageTypeDef",
    {
        "Storage": List["ValidStorageOptionsTypeDef"],
    },
    total=False,
)

ValidStorageOptionsTypeDef = TypedDict(
    "ValidStorageOptionsTypeDef",
    {
        "StorageType": str,
        "StorageSize": List["RangeTypeDef"],
        "ProvisionedIops": List["RangeTypeDef"],
        "IopsToStorageRatio": List["DoubleRangeTypeDef"],
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
