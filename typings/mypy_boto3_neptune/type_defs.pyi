"""
Main interface for neptune service type definitions.

Usage::

    ```python
    from mypy_boto3_neptune.type_defs import AvailabilityZoneTypeDef

    data: AvailabilityZoneTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AvailabilityZoneTypeDef",
    "CharacterSetTypeDef",
    "DBClusterMemberTypeDef",
    "DBClusterOptionGroupStatusTypeDef",
    "DBClusterParameterGroupTypeDef",
    "DBClusterRoleTypeDef",
    "DBClusterSnapshotAttributeTypeDef",
    "DBClusterSnapshotAttributesResultTypeDef",
    "DBClusterSnapshotTypeDef",
    "DBClusterTypeDef",
    "DBEngineVersionTypeDef",
    "DBInstanceStatusInfoTypeDef",
    "DBInstanceTypeDef",
    "DBParameterGroupStatusTypeDef",
    "DBParameterGroupTypeDef",
    "DBSecurityGroupMembershipTypeDef",
    "DBSubnetGroupTypeDef",
    "DomainMembershipTypeDef",
    "DoubleRangeTypeDef",
    "EndpointTypeDef",
    "EngineDefaultsTypeDef",
    "EventCategoriesMapTypeDef",
    "EventSubscriptionTypeDef",
    "EventTypeDef",
    "OptionGroupMembershipTypeDef",
    "OrderableDBInstanceOptionTypeDef",
    "ParameterTypeDef",
    "PendingCloudwatchLogsExportsTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PendingModifiedValuesTypeDef",
    "RangeTypeDef",
    "ResourcePendingMaintenanceActionsTypeDef",
    "SubnetTypeDef",
    "TagTypeDef",
    "TimezoneTypeDef",
    "UpgradeTargetTypeDef",
    "ValidDBInstanceModificationsMessageTypeDef",
    "ValidStorageOptionsTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "AddSourceIdentifierToSubscriptionResultTypeDef",
    "ApplyPendingMaintenanceActionResultTypeDef",
    "CloudwatchLogsExportConfigurationTypeDef",
    "CopyDBClusterParameterGroupResultTypeDef",
    "CopyDBClusterSnapshotResultTypeDef",
    "CopyDBParameterGroupResultTypeDef",
    "CreateDBClusterParameterGroupResultTypeDef",
    "CreateDBClusterResultTypeDef",
    "CreateDBClusterSnapshotResultTypeDef",
    "CreateDBInstanceResultTypeDef",
    "CreateDBParameterGroupResultTypeDef",
    "CreateDBSubnetGroupResultTypeDef",
    "CreateEventSubscriptionResultTypeDef",
    "DBClusterMessageTypeDef",
    "DBClusterParameterGroupDetailsTypeDef",
    "DBClusterParameterGroupNameMessageTypeDef",
    "DBClusterParameterGroupsMessageTypeDef",
    "DBClusterSnapshotMessageTypeDef",
    "DBEngineVersionMessageTypeDef",
    "DBInstanceMessageTypeDef",
    "DBParameterGroupDetailsTypeDef",
    "DBParameterGroupNameMessageTypeDef",
    "DBParameterGroupsMessageTypeDef",
    "DBSubnetGroupMessageTypeDef",
    "DeleteDBClusterResultTypeDef",
    "DeleteDBClusterSnapshotResultTypeDef",
    "DeleteDBInstanceResultTypeDef",
    "DeleteEventSubscriptionResultTypeDef",
    "DescribeDBClusterSnapshotAttributesResultTypeDef",
    "DescribeEngineDefaultClusterParametersResultTypeDef",
    "DescribeEngineDefaultParametersResultTypeDef",
    "DescribeValidDBInstanceModificationsResultTypeDef",
    "EventCategoriesMessageTypeDef",
    "EventSubscriptionsMessageTypeDef",
    "EventsMessageTypeDef",
    "FailoverDBClusterResultTypeDef",
    "FilterTypeDef",
    "ModifyDBClusterResultTypeDef",
    "ModifyDBClusterSnapshotAttributeResultTypeDef",
    "ModifyDBInstanceResultTypeDef",
    "ModifyDBSubnetGroupResultTypeDef",
    "ModifyEventSubscriptionResultTypeDef",
    "OrderableDBInstanceOptionsMessageTypeDef",
    "PaginatorConfigTypeDef",
    "PendingMaintenanceActionsMessageTypeDef",
    "PromoteReadReplicaDBClusterResultTypeDef",
    "RebootDBInstanceResultTypeDef",
    "RemoveSourceIdentifierFromSubscriptionResultTypeDef",
    "RestoreDBClusterFromSnapshotResultTypeDef",
    "RestoreDBClusterToPointInTimeResultTypeDef",
    "StartDBClusterResultTypeDef",
    "StopDBClusterResultTypeDef",
    "TagListMessageTypeDef",
    "WaiterConfigTypeDef",
)

AvailabilityZoneTypeDef = TypedDict("AvailabilityZoneTypeDef", {"Name": str}, total=False)

CharacterSetTypeDef = TypedDict(
    "CharacterSetTypeDef", {"CharacterSetName": str, "CharacterSetDescription": str}, total=False
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

DBClusterOptionGroupStatusTypeDef = TypedDict(
    "DBClusterOptionGroupStatusTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
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

DBClusterRoleTypeDef = TypedDict(
    "DBClusterRoleTypeDef", {"RoleArn": str, "Status": str}, total=False
)

DBClusterSnapshotAttributeTypeDef = TypedDict(
    "DBClusterSnapshotAttributeTypeDef",
    {"AttributeName": str, "AttributeValues": List[str]},
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
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
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

DBInstanceStatusInfoTypeDef = TypedDict(
    "DBInstanceStatusInfoTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
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

DBParameterGroupStatusTypeDef = TypedDict(
    "DBParameterGroupStatusTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
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

DBSecurityGroupMembershipTypeDef = TypedDict(
    "DBSecurityGroupMembershipTypeDef", {"DBSecurityGroupName": str, "Status": str}, total=False
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

DomainMembershipTypeDef = TypedDict(
    "DomainMembershipTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)

DoubleRangeTypeDef = TypedDict("DoubleRangeTypeDef", {"From": float, "To": float}, total=False)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef", {"Address": str, "Port": int, "HostedZoneId": str}, total=False
)

EngineDefaultsTypeDef = TypedDict(
    "EngineDefaultsTypeDef",
    {"DBParameterGroupFamily": str, "Marker": str, "Parameters": List["ParameterTypeDef"]},
    total=False,
)

EventCategoriesMapTypeDef = TypedDict(
    "EventCategoriesMapTypeDef", {"SourceType": str, "EventCategories": List[str]}, total=False
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

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": Literal[
            "db-instance",
            "db-parameter-group",
            "db-security-group",
            "db-snapshot",
            "db-cluster",
            "db-cluster-snapshot",
        ],
        "Message": str,
        "EventCategories": List[str],
        "Date": datetime,
        "SourceArn": str,
    },
    total=False,
)

OptionGroupMembershipTypeDef = TypedDict(
    "OptionGroupMembershipTypeDef", {"OptionGroupName": str, "Status": str}, total=False
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
        "ApplyMethod": Literal["immediate", "pending-reboot"],
    },
    total=False,
)

PendingCloudwatchLogsExportsTypeDef = TypedDict(
    "PendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
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

RangeTypeDef = TypedDict("RangeTypeDef", {"From": int, "To": int, "Step": int}, total=False)

ResourcePendingMaintenanceActionsTypeDef = TypedDict(
    "ResourcePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List["PendingMaintenanceActionTypeDef"],
    },
    total=False,
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

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

TimezoneTypeDef = TypedDict("TimezoneTypeDef", {"TimezoneName": str}, total=False)

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
    {"Storage": List["ValidStorageOptionsTypeDef"]},
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
    "VpcSecurityGroupMembershipTypeDef", {"VpcSecurityGroupId": str, "Status": str}, total=False
)

AddSourceIdentifierToSubscriptionResultTypeDef = TypedDict(
    "AddSourceIdentifierToSubscriptionResultTypeDef",
    {"EventSubscription": "EventSubscriptionTypeDef"},
    total=False,
)

ApplyPendingMaintenanceActionResultTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionResultTypeDef",
    {"ResourcePendingMaintenanceActions": "ResourcePendingMaintenanceActionsTypeDef"},
    total=False,
)

CloudwatchLogsExportConfigurationTypeDef = TypedDict(
    "CloudwatchLogsExportConfigurationTypeDef",
    {"EnableLogTypes": List[str], "DisableLogTypes": List[str]},
    total=False,
)

CopyDBClusterParameterGroupResultTypeDef = TypedDict(
    "CopyDBClusterParameterGroupResultTypeDef",
    {"DBClusterParameterGroup": "DBClusterParameterGroupTypeDef"},
    total=False,
)

CopyDBClusterSnapshotResultTypeDef = TypedDict(
    "CopyDBClusterSnapshotResultTypeDef",
    {"DBClusterSnapshot": "DBClusterSnapshotTypeDef"},
    total=False,
)

CopyDBParameterGroupResultTypeDef = TypedDict(
    "CopyDBParameterGroupResultTypeDef",
    {"DBParameterGroup": "DBParameterGroupTypeDef"},
    total=False,
)

CreateDBClusterParameterGroupResultTypeDef = TypedDict(
    "CreateDBClusterParameterGroupResultTypeDef",
    {"DBClusterParameterGroup": "DBClusterParameterGroupTypeDef"},
    total=False,
)

CreateDBClusterResultTypeDef = TypedDict(
    "CreateDBClusterResultTypeDef", {"DBCluster": "DBClusterTypeDef"}, total=False
)

CreateDBClusterSnapshotResultTypeDef = TypedDict(
    "CreateDBClusterSnapshotResultTypeDef",
    {"DBClusterSnapshot": "DBClusterSnapshotTypeDef"},
    total=False,
)

CreateDBInstanceResultTypeDef = TypedDict(
    "CreateDBInstanceResultTypeDef", {"DBInstance": "DBInstanceTypeDef"}, total=False
)

CreateDBParameterGroupResultTypeDef = TypedDict(
    "CreateDBParameterGroupResultTypeDef",
    {"DBParameterGroup": "DBParameterGroupTypeDef"},
    total=False,
)

CreateDBSubnetGroupResultTypeDef = TypedDict(
    "CreateDBSubnetGroupResultTypeDef", {"DBSubnetGroup": "DBSubnetGroupTypeDef"}, total=False
)

CreateEventSubscriptionResultTypeDef = TypedDict(
    "CreateEventSubscriptionResultTypeDef",
    {"EventSubscription": "EventSubscriptionTypeDef"},
    total=False,
)

DBClusterMessageTypeDef = TypedDict(
    "DBClusterMessageTypeDef", {"Marker": str, "DBClusters": List["DBClusterTypeDef"]}, total=False
)

DBClusterParameterGroupDetailsTypeDef = TypedDict(
    "DBClusterParameterGroupDetailsTypeDef",
    {"Parameters": List["ParameterTypeDef"], "Marker": str},
    total=False,
)

DBClusterParameterGroupNameMessageTypeDef = TypedDict(
    "DBClusterParameterGroupNameMessageTypeDef", {"DBClusterParameterGroupName": str}, total=False
)

DBClusterParameterGroupsMessageTypeDef = TypedDict(
    "DBClusterParameterGroupsMessageTypeDef",
    {"Marker": str, "DBClusterParameterGroups": List["DBClusterParameterGroupTypeDef"]},
    total=False,
)

DBClusterSnapshotMessageTypeDef = TypedDict(
    "DBClusterSnapshotMessageTypeDef",
    {"Marker": str, "DBClusterSnapshots": List["DBClusterSnapshotTypeDef"]},
    total=False,
)

DBEngineVersionMessageTypeDef = TypedDict(
    "DBEngineVersionMessageTypeDef",
    {"Marker": str, "DBEngineVersions": List["DBEngineVersionTypeDef"]},
    total=False,
)

DBInstanceMessageTypeDef = TypedDict(
    "DBInstanceMessageTypeDef",
    {"Marker": str, "DBInstances": List["DBInstanceTypeDef"]},
    total=False,
)

DBParameterGroupDetailsTypeDef = TypedDict(
    "DBParameterGroupDetailsTypeDef",
    {"Parameters": List["ParameterTypeDef"], "Marker": str},
    total=False,
)

DBParameterGroupNameMessageTypeDef = TypedDict(
    "DBParameterGroupNameMessageTypeDef", {"DBParameterGroupName": str}, total=False
)

DBParameterGroupsMessageTypeDef = TypedDict(
    "DBParameterGroupsMessageTypeDef",
    {"Marker": str, "DBParameterGroups": List["DBParameterGroupTypeDef"]},
    total=False,
)

DBSubnetGroupMessageTypeDef = TypedDict(
    "DBSubnetGroupMessageTypeDef",
    {"Marker": str, "DBSubnetGroups": List["DBSubnetGroupTypeDef"]},
    total=False,
)

DeleteDBClusterResultTypeDef = TypedDict(
    "DeleteDBClusterResultTypeDef", {"DBCluster": "DBClusterTypeDef"}, total=False
)

DeleteDBClusterSnapshotResultTypeDef = TypedDict(
    "DeleteDBClusterSnapshotResultTypeDef",
    {"DBClusterSnapshot": "DBClusterSnapshotTypeDef"},
    total=False,
)

DeleteDBInstanceResultTypeDef = TypedDict(
    "DeleteDBInstanceResultTypeDef", {"DBInstance": "DBInstanceTypeDef"}, total=False
)

DeleteEventSubscriptionResultTypeDef = TypedDict(
    "DeleteEventSubscriptionResultTypeDef",
    {"EventSubscription": "EventSubscriptionTypeDef"},
    total=False,
)

DescribeDBClusterSnapshotAttributesResultTypeDef = TypedDict(
    "DescribeDBClusterSnapshotAttributesResultTypeDef",
    {"DBClusterSnapshotAttributesResult": "DBClusterSnapshotAttributesResultTypeDef"},
    total=False,
)

DescribeEngineDefaultClusterParametersResultTypeDef = TypedDict(
    "DescribeEngineDefaultClusterParametersResultTypeDef",
    {"EngineDefaults": "EngineDefaultsTypeDef"},
    total=False,
)

DescribeEngineDefaultParametersResultTypeDef = TypedDict(
    "DescribeEngineDefaultParametersResultTypeDef",
    {"EngineDefaults": "EngineDefaultsTypeDef"},
    total=False,
)

DescribeValidDBInstanceModificationsResultTypeDef = TypedDict(
    "DescribeValidDBInstanceModificationsResultTypeDef",
    {"ValidDBInstanceModificationsMessage": "ValidDBInstanceModificationsMessageTypeDef"},
    total=False,
)

EventCategoriesMessageTypeDef = TypedDict(
    "EventCategoriesMessageTypeDef",
    {"EventCategoriesMapList": List["EventCategoriesMapTypeDef"]},
    total=False,
)

EventSubscriptionsMessageTypeDef = TypedDict(
    "EventSubscriptionsMessageTypeDef",
    {"Marker": str, "EventSubscriptionsList": List["EventSubscriptionTypeDef"]},
    total=False,
)

EventsMessageTypeDef = TypedDict(
    "EventsMessageTypeDef", {"Marker": str, "Events": List["EventTypeDef"]}, total=False
)

FailoverDBClusterResultTypeDef = TypedDict(
    "FailoverDBClusterResultTypeDef", {"DBCluster": "DBClusterTypeDef"}, total=False
)

FilterTypeDef = TypedDict("FilterTypeDef", {"Name": str, "Values": List[str]})

ModifyDBClusterResultTypeDef = TypedDict(
    "ModifyDBClusterResultTypeDef", {"DBCluster": "DBClusterTypeDef"}, total=False
)

ModifyDBClusterSnapshotAttributeResultTypeDef = TypedDict(
    "ModifyDBClusterSnapshotAttributeResultTypeDef",
    {"DBClusterSnapshotAttributesResult": "DBClusterSnapshotAttributesResultTypeDef"},
    total=False,
)

ModifyDBInstanceResultTypeDef = TypedDict(
    "ModifyDBInstanceResultTypeDef", {"DBInstance": "DBInstanceTypeDef"}, total=False
)

ModifyDBSubnetGroupResultTypeDef = TypedDict(
    "ModifyDBSubnetGroupResultTypeDef", {"DBSubnetGroup": "DBSubnetGroupTypeDef"}, total=False
)

ModifyEventSubscriptionResultTypeDef = TypedDict(
    "ModifyEventSubscriptionResultTypeDef",
    {"EventSubscription": "EventSubscriptionTypeDef"},
    total=False,
)

OrderableDBInstanceOptionsMessageTypeDef = TypedDict(
    "OrderableDBInstanceOptionsMessageTypeDef",
    {"OrderableDBInstanceOptions": List["OrderableDBInstanceOptionTypeDef"], "Marker": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PendingMaintenanceActionsMessageTypeDef = TypedDict(
    "PendingMaintenanceActionsMessageTypeDef",
    {"PendingMaintenanceActions": List["ResourcePendingMaintenanceActionsTypeDef"], "Marker": str},
    total=False,
)

PromoteReadReplicaDBClusterResultTypeDef = TypedDict(
    "PromoteReadReplicaDBClusterResultTypeDef", {"DBCluster": "DBClusterTypeDef"}, total=False
)

RebootDBInstanceResultTypeDef = TypedDict(
    "RebootDBInstanceResultTypeDef", {"DBInstance": "DBInstanceTypeDef"}, total=False
)

RemoveSourceIdentifierFromSubscriptionResultTypeDef = TypedDict(
    "RemoveSourceIdentifierFromSubscriptionResultTypeDef",
    {"EventSubscription": "EventSubscriptionTypeDef"},
    total=False,
)

RestoreDBClusterFromSnapshotResultTypeDef = TypedDict(
    "RestoreDBClusterFromSnapshotResultTypeDef", {"DBCluster": "DBClusterTypeDef"}, total=False
)

RestoreDBClusterToPointInTimeResultTypeDef = TypedDict(
    "RestoreDBClusterToPointInTimeResultTypeDef", {"DBCluster": "DBClusterTypeDef"}, total=False
)

StartDBClusterResultTypeDef = TypedDict(
    "StartDBClusterResultTypeDef", {"DBCluster": "DBClusterTypeDef"}, total=False
)

StopDBClusterResultTypeDef = TypedDict(
    "StopDBClusterResultTypeDef", {"DBCluster": "DBClusterTypeDef"}, total=False
)

TagListMessageTypeDef = TypedDict(
    "TagListMessageTypeDef", {"TagList": List["TagTypeDef"]}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
