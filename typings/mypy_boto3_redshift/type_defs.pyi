"""
Main interface for redshift service type definitions.

Usage::

    ```python
    from mypy_boto3_redshift.type_defs import AccountAttributeTypeDef

    data: AccountAttributeTypeDef = {...}
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
    "AccountAttributeTypeDef",
    "AccountWithRestoreAccessTypeDef",
    "AttributeValueTargetTypeDef",
    "AvailabilityZoneTypeDef",
    "ClusterAssociatedToScheduleTypeDef",
    "ClusterDbRevisionTypeDef",
    "ClusterIamRoleTypeDef",
    "ClusterNodeTypeDef",
    "ClusterParameterGroupStatusTypeDef",
    "ClusterParameterGroupTypeDef",
    "ClusterParameterStatusTypeDef",
    "ClusterSecurityGroupMembershipTypeDef",
    "ClusterSecurityGroupTypeDef",
    "ClusterSnapshotCopyStatusTypeDef",
    "ClusterSubnetGroupTypeDef",
    "ClusterTypeDef",
    "ClusterVersionTypeDef",
    "DataTransferProgressTypeDef",
    "DefaultClusterParametersTypeDef",
    "DeferredMaintenanceWindowTypeDef",
    "EC2SecurityGroupTypeDef",
    "ElasticIpStatusTypeDef",
    "EndpointTypeDef",
    "EventCategoriesMapTypeDef",
    "EventInfoMapTypeDef",
    "EventSubscriptionTypeDef",
    "EventTypeDef",
    "HsmClientCertificateTypeDef",
    "HsmConfigurationTypeDef",
    "HsmStatusTypeDef",
    "IPRangeTypeDef",
    "MaintenanceTrackTypeDef",
    "NodeConfigurationOptionTypeDef",
    "OrderableClusterOptionTypeDef",
    "ParameterTypeDef",
    "PauseClusterMessageTypeDef",
    "PendingModifiedValuesTypeDef",
    "RecurringChargeTypeDef",
    "ReservedNodeOfferingTypeDef",
    "ReservedNodeTypeDef",
    "ResizeClusterMessageTypeDef",
    "ResizeInfoTypeDef",
    "RestoreStatusTypeDef",
    "ResumeClusterMessageTypeDef",
    "RevisionTargetTypeDef",
    "ScheduledActionTypeDef",
    "ScheduledActionTypeTypeDef",
    "SnapshotCopyGrantTypeDef",
    "SnapshotErrorMessageTypeDef",
    "SnapshotScheduleTypeDef",
    "SnapshotTypeDef",
    "SubnetTypeDef",
    "SupportedOperationTypeDef",
    "SupportedPlatformTypeDef",
    "TableRestoreStatusTypeDef",
    "TagTypeDef",
    "TaggedResourceTypeDef",
    "UpdateTargetTypeDef",
    "UsageLimitTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "AcceptReservedNodeExchangeOutputMessageTypeDef",
    "AccountAttributeListTypeDef",
    "AuthorizeClusterSecurityGroupIngressResultTypeDef",
    "AuthorizeSnapshotAccessResultTypeDef",
    "BatchDeleteClusterSnapshotsResultTypeDef",
    "BatchModifyClusterSnapshotsOutputMessageTypeDef",
    "ClusterCredentialsTypeDef",
    "ClusterDbRevisionsMessageTypeDef",
    "ClusterParameterGroupDetailsTypeDef",
    "ClusterParameterGroupNameMessageTypeDef",
    "ClusterParameterGroupsMessageTypeDef",
    "ClusterSecurityGroupMessageTypeDef",
    "ClusterSubnetGroupMessageTypeDef",
    "ClusterVersionsMessageTypeDef",
    "ClustersMessageTypeDef",
    "CopyClusterSnapshotResultTypeDef",
    "CreateClusterParameterGroupResultTypeDef",
    "CreateClusterResultTypeDef",
    "CreateClusterSecurityGroupResultTypeDef",
    "CreateClusterSnapshotResultTypeDef",
    "CreateClusterSubnetGroupResultTypeDef",
    "CreateEventSubscriptionResultTypeDef",
    "CreateHsmClientCertificateResultTypeDef",
    "CreateHsmConfigurationResultTypeDef",
    "CreateSnapshotCopyGrantResultTypeDef",
    "CustomerStorageMessageTypeDef",
    "DeleteClusterResultTypeDef",
    "DeleteClusterSnapshotMessageTypeDef",
    "DeleteClusterSnapshotResultTypeDef",
    "DescribeDefaultClusterParametersResultTypeDef",
    "DescribeSnapshotSchedulesOutputMessageTypeDef",
    "DisableSnapshotCopyResultTypeDef",
    "EnableSnapshotCopyResultTypeDef",
    "EventCategoriesMessageTypeDef",
    "EventSubscriptionsMessageTypeDef",
    "EventsMessageTypeDef",
    "GetReservedNodeExchangeOfferingsOutputMessageTypeDef",
    "HsmClientCertificateMessageTypeDef",
    "HsmConfigurationMessageTypeDef",
    "LoggingStatusTypeDef",
    "ModifyClusterDbRevisionResultTypeDef",
    "ModifyClusterIamRolesResultTypeDef",
    "ModifyClusterMaintenanceResultTypeDef",
    "ModifyClusterResultTypeDef",
    "ModifyClusterSnapshotResultTypeDef",
    "ModifyClusterSubnetGroupResultTypeDef",
    "ModifyEventSubscriptionResultTypeDef",
    "ModifySnapshotCopyRetentionPeriodResultTypeDef",
    "NodeConfigurationOptionsFilterTypeDef",
    "NodeConfigurationOptionsMessageTypeDef",
    "OrderableClusterOptionsMessageTypeDef",
    "PaginatorConfigTypeDef",
    "PauseClusterResultTypeDef",
    "PurchaseReservedNodeOfferingResultTypeDef",
    "RebootClusterResultTypeDef",
    "ReservedNodeOfferingsMessageTypeDef",
    "ReservedNodesMessageTypeDef",
    "ResizeClusterResultTypeDef",
    "ResizeProgressMessageTypeDef",
    "RestoreFromClusterSnapshotResultTypeDef",
    "RestoreTableFromClusterSnapshotResultTypeDef",
    "ResumeClusterResultTypeDef",
    "RevokeClusterSecurityGroupIngressResultTypeDef",
    "RevokeSnapshotAccessResultTypeDef",
    "RotateEncryptionKeyResultTypeDef",
    "ScheduledActionFilterTypeDef",
    "ScheduledActionsMessageTypeDef",
    "SnapshotCopyGrantMessageTypeDef",
    "SnapshotMessageTypeDef",
    "SnapshotSortingEntityTypeDef",
    "TableRestoreStatusMessageTypeDef",
    "TaggedResourceListMessageTypeDef",
    "TrackListMessageTypeDef",
    "UsageLimitListTypeDef",
    "WaiterConfigTypeDef",
)

AccountAttributeTypeDef = TypedDict(
    "AccountAttributeTypeDef",
    {"AttributeName": str, "AttributeValues": List["AttributeValueTargetTypeDef"]},
    total=False,
)

AccountWithRestoreAccessTypeDef = TypedDict(
    "AccountWithRestoreAccessTypeDef", {"AccountId": str, "AccountAlias": str}, total=False
)

AttributeValueTargetTypeDef = TypedDict(
    "AttributeValueTargetTypeDef", {"AttributeValue": str}, total=False
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {"Name": str, "SupportedPlatforms": List["SupportedPlatformTypeDef"]},
    total=False,
)

ClusterAssociatedToScheduleTypeDef = TypedDict(
    "ClusterAssociatedToScheduleTypeDef",
    {
        "ClusterIdentifier": str,
        "ScheduleAssociationState": Literal["MODIFYING", "ACTIVE", "FAILED"],
    },
    total=False,
)

ClusterDbRevisionTypeDef = TypedDict(
    "ClusterDbRevisionTypeDef",
    {
        "ClusterIdentifier": str,
        "CurrentDatabaseRevision": str,
        "DatabaseRevisionReleaseDate": datetime,
        "RevisionTargets": List["RevisionTargetTypeDef"],
    },
    total=False,
)

ClusterIamRoleTypeDef = TypedDict(
    "ClusterIamRoleTypeDef", {"IamRoleArn": str, "ApplyStatus": str}, total=False
)

ClusterNodeTypeDef = TypedDict(
    "ClusterNodeTypeDef",
    {"NodeRole": str, "PrivateIPAddress": str, "PublicIPAddress": str},
    total=False,
)

ClusterParameterGroupStatusTypeDef = TypedDict(
    "ClusterParameterGroupStatusTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List["ClusterParameterStatusTypeDef"],
    },
    total=False,
)

ClusterParameterGroupTypeDef = TypedDict(
    "ClusterParameterGroupTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterGroupFamily": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ClusterParameterStatusTypeDef = TypedDict(
    "ClusterParameterStatusTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)

ClusterSecurityGroupMembershipTypeDef = TypedDict(
    "ClusterSecurityGroupMembershipTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)

ClusterSecurityGroupTypeDef = TypedDict(
    "ClusterSecurityGroupTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List["EC2SecurityGroupTypeDef"],
        "IPRanges": List["IPRangeTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ClusterSnapshotCopyStatusTypeDef = TypedDict(
    "ClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)

ClusterSubnetGroupTypeDef = TypedDict(
    "ClusterSubnetGroupTypeDef",
    {
        "ClusterSubnetGroupName": str,
        "Description": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List["SubnetTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": "EndpointTypeDef",
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List["ClusterSecurityGroupMembershipTypeDef"],
        "VpcSecurityGroups": List["VpcSecurityGroupMembershipTypeDef"],
        "ClusterParameterGroups": List["ClusterParameterGroupStatusTypeDef"],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": "PendingModifiedValuesTypeDef",
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": "RestoreStatusTypeDef",
        "DataTransferProgress": "DataTransferProgressTypeDef",
        "HsmStatus": "HsmStatusTypeDef",
        "ClusterSnapshotCopyStatus": "ClusterSnapshotCopyStatusTypeDef",
        "ClusterPublicKey": str,
        "ClusterNodes": List["ClusterNodeTypeDef"],
        "ElasticIpStatus": "ElasticIpStatusTypeDef",
        "ClusterRevisionNumber": str,
        "Tags": List["TagTypeDef"],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List["ClusterIamRoleTypeDef"],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List["DeferredMaintenanceWindowTypeDef"],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": Literal["MODIFYING", "ACTIVE", "FAILED"],
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": "ResizeInfoTypeDef",
    },
    total=False,
)

ClusterVersionTypeDef = TypedDict(
    "ClusterVersionTypeDef",
    {"ClusterVersion": str, "ClusterParameterGroupFamily": str, "Description": str},
    total=False,
)

DataTransferProgressTypeDef = TypedDict(
    "DataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)

DefaultClusterParametersTypeDef = TypedDict(
    "DefaultClusterParametersTypeDef",
    {"ParameterGroupFamily": str, "Marker": str, "Parameters": List["ParameterTypeDef"]},
    total=False,
)

DeferredMaintenanceWindowTypeDef = TypedDict(
    "DeferredMaintenanceWindowTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)

EC2SecurityGroupTypeDef = TypedDict(
    "EC2SecurityGroupTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ElasticIpStatusTypeDef = TypedDict(
    "ElasticIpStatusTypeDef", {"ElasticIp": str, "Status": str}, total=False
)

EndpointTypeDef = TypedDict("EndpointTypeDef", {"Address": str, "Port": int}, total=False)

EventCategoriesMapTypeDef = TypedDict(
    "EventCategoriesMapTypeDef",
    {"SourceType": str, "Events": List["EventInfoMapTypeDef"]},
    total=False,
)

EventInfoMapTypeDef = TypedDict(
    "EventInfoMapTypeDef",
    {"EventId": str, "EventCategories": List[str], "EventDescription": str, "Severity": str},
    total=False,
)

EventSubscriptionTypeDef = TypedDict(
    "EventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": datetime,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Severity": str,
        "Enabled": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": Literal[
            "cluster",
            "cluster-parameter-group",
            "cluster-security-group",
            "cluster-snapshot",
            "scheduled-action",
        ],
        "Message": str,
        "EventCategories": List[str],
        "Severity": str,
        "Date": datetime,
        "EventId": str,
    },
    total=False,
)

HsmClientCertificateTypeDef = TypedDict(
    "HsmClientCertificateTypeDef",
    {
        "HsmClientCertificateIdentifier": str,
        "HsmClientCertificatePublicKey": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

HsmConfigurationTypeDef = TypedDict(
    "HsmConfigurationTypeDef",
    {
        "HsmConfigurationIdentifier": str,
        "Description": str,
        "HsmIpAddress": str,
        "HsmPartitionName": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

HsmStatusTypeDef = TypedDict(
    "HsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)

IPRangeTypeDef = TypedDict(
    "IPRangeTypeDef", {"Status": str, "CIDRIP": str, "Tags": List["TagTypeDef"]}, total=False
)

MaintenanceTrackTypeDef = TypedDict(
    "MaintenanceTrackTypeDef",
    {
        "MaintenanceTrackName": str,
        "DatabaseVersion": str,
        "UpdateTargets": List["UpdateTargetTypeDef"],
    },
    total=False,
)

NodeConfigurationOptionTypeDef = TypedDict(
    "NodeConfigurationOptionTypeDef",
    {
        "NodeType": str,
        "NumberOfNodes": int,
        "EstimatedDiskUtilizationPercent": float,
        "Mode": Literal["standard", "high-performance"],
    },
    total=False,
)

OrderableClusterOptionTypeDef = TypedDict(
    "OrderableClusterOptionTypeDef",
    {
        "ClusterVersion": str,
        "ClusterType": str,
        "NodeType": str,
        "AvailabilityZones": List["AvailabilityZoneTypeDef"],
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
        "DataType": str,
        "AllowedValues": str,
        "ApplyType": Literal["static", "dynamic"],
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
    },
    total=False,
)

PauseClusterMessageTypeDef = TypedDict("PauseClusterMessageTypeDef", {"ClusterIdentifier": str})

PendingModifiedValuesTypeDef = TypedDict(
    "PendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)

RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

ReservedNodeOfferingTypeDef = TypedDict(
    "ReservedNodeOfferingTypeDef",
    {
        "ReservedNodeOfferingId": str,
        "NodeType": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "OfferingType": str,
        "RecurringCharges": List["RecurringChargeTypeDef"],
        "ReservedNodeOfferingType": Literal["Regular", "Upgradable"],
    },
    total=False,
)

ReservedNodeTypeDef = TypedDict(
    "ReservedNodeTypeDef",
    {
        "ReservedNodeId": str,
        "ReservedNodeOfferingId": str,
        "NodeType": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "NodeCount": int,
        "State": str,
        "OfferingType": str,
        "RecurringCharges": List["RecurringChargeTypeDef"],
        "ReservedNodeOfferingType": Literal["Regular", "Upgradable"],
    },
    total=False,
)

_RequiredResizeClusterMessageTypeDef = TypedDict(
    "_RequiredResizeClusterMessageTypeDef", {"ClusterIdentifier": str}
)
_OptionalResizeClusterMessageTypeDef = TypedDict(
    "_OptionalResizeClusterMessageTypeDef",
    {"ClusterType": str, "NodeType": str, "NumberOfNodes": int, "Classic": bool},
    total=False,
)


class ResizeClusterMessageTypeDef(
    _RequiredResizeClusterMessageTypeDef, _OptionalResizeClusterMessageTypeDef
):
    pass


ResizeInfoTypeDef = TypedDict(
    "ResizeInfoTypeDef", {"ResizeType": str, "AllowCancelResize": bool}, total=False
)

RestoreStatusTypeDef = TypedDict(
    "RestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)

ResumeClusterMessageTypeDef = TypedDict("ResumeClusterMessageTypeDef", {"ClusterIdentifier": str})

RevisionTargetTypeDef = TypedDict(
    "RevisionTargetTypeDef",
    {"DatabaseRevision": str, "Description": str, "DatabaseRevisionReleaseDate": datetime},
    total=False,
)

ScheduledActionTypeDef = TypedDict(
    "ScheduledActionTypeDef",
    {
        "ScheduledActionName": str,
        "TargetAction": "ScheduledActionTypeTypeDef",
        "Schedule": str,
        "IamRole": str,
        "ScheduledActionDescription": str,
        "State": Literal["ACTIVE", "DISABLED"],
        "NextInvocations": List[datetime],
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

ScheduledActionTypeTypeDef = TypedDict(
    "ScheduledActionTypeTypeDef",
    {
        "ResizeCluster": "ResizeClusterMessageTypeDef",
        "PauseCluster": "PauseClusterMessageTypeDef",
        "ResumeCluster": "ResumeClusterMessageTypeDef",
    },
    total=False,
)

SnapshotCopyGrantTypeDef = TypedDict(
    "SnapshotCopyGrantTypeDef",
    {"SnapshotCopyGrantName": str, "KmsKeyId": str, "Tags": List["TagTypeDef"]},
    total=False,
)

SnapshotErrorMessageTypeDef = TypedDict(
    "SnapshotErrorMessageTypeDef",
    {
        "SnapshotIdentifier": str,
        "SnapshotClusterIdentifier": str,
        "FailureCode": str,
        "FailureReason": str,
    },
    total=False,
)

SnapshotScheduleTypeDef = TypedDict(
    "SnapshotScheduleTypeDef",
    {
        "ScheduleDefinitions": List[str],
        "ScheduleIdentifier": str,
        "ScheduleDescription": str,
        "Tags": List["TagTypeDef"],
        "NextInvocations": List[datetime],
        "AssociatedClusterCount": int,
        "AssociatedClusters": List["ClusterAssociatedToScheduleTypeDef"],
    },
    total=False,
)

SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "SnapshotIdentifier": str,
        "ClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "ClusterVersion": str,
        "SnapshotType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "DBName": str,
        "VpcId": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "EncryptedWithHSM": bool,
        "AccountsWithRestoreAccess": List["AccountWithRestoreAccessTypeDef"],
        "OwnerAccount": str,
        "TotalBackupSizeInMegaBytes": float,
        "ActualIncrementalBackupSizeInMegaBytes": float,
        "BackupProgressInMegaBytes": float,
        "CurrentBackupRateInMegaBytesPerSecond": float,
        "EstimatedSecondsToCompletion": int,
        "ElapsedTimeInSeconds": int,
        "SourceRegion": str,
        "Tags": List["TagTypeDef"],
        "RestorableNodeTypes": List[str],
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "ManualSnapshotRetentionPeriod": int,
        "ManualSnapshotRemainingDays": int,
        "SnapshotRetentionStartTime": datetime,
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

SupportedOperationTypeDef = TypedDict(
    "SupportedOperationTypeDef", {"OperationName": str}, total=False
)

SupportedPlatformTypeDef = TypedDict("SupportedPlatformTypeDef", {"Name": str}, total=False)

TableRestoreStatusTypeDef = TypedDict(
    "TableRestoreStatusTypeDef",
    {
        "TableRestoreRequestId": str,
        "Status": Literal["PENDING", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELED"],
        "Message": str,
        "RequestTime": datetime,
        "ProgressInMegaBytes": int,
        "TotalDataInMegaBytes": int,
        "ClusterIdentifier": str,
        "SnapshotIdentifier": str,
        "SourceDatabaseName": str,
        "SourceSchemaName": str,
        "SourceTableName": str,
        "TargetDatabaseName": str,
        "TargetSchemaName": str,
        "NewTableName": str,
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

TaggedResourceTypeDef = TypedDict(
    "TaggedResourceTypeDef",
    {"Tag": "TagTypeDef", "ResourceName": str, "ResourceType": str},
    total=False,
)

UpdateTargetTypeDef = TypedDict(
    "UpdateTargetTypeDef",
    {
        "MaintenanceTrackName": str,
        "DatabaseVersion": str,
        "SupportedOperations": List["SupportedOperationTypeDef"],
    },
    total=False,
)

UsageLimitTypeDef = TypedDict(
    "UsageLimitTypeDef",
    {
        "UsageLimitId": str,
        "ClusterIdentifier": str,
        "FeatureType": Literal["spectrum", "concurrency-scaling"],
        "LimitType": Literal["time", "data-scanned"],
        "Amount": int,
        "Period": Literal["daily", "weekly", "monthly"],
        "BreachAction": Literal["log", "emit-metric", "disable"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

VpcSecurityGroupMembershipTypeDef = TypedDict(
    "VpcSecurityGroupMembershipTypeDef", {"VpcSecurityGroupId": str, "Status": str}, total=False
)

AcceptReservedNodeExchangeOutputMessageTypeDef = TypedDict(
    "AcceptReservedNodeExchangeOutputMessageTypeDef",
    {"ExchangedReservedNode": "ReservedNodeTypeDef"},
    total=False,
)

AccountAttributeListTypeDef = TypedDict(
    "AccountAttributeListTypeDef",
    {"AccountAttributes": List["AccountAttributeTypeDef"]},
    total=False,
)

AuthorizeClusterSecurityGroupIngressResultTypeDef = TypedDict(
    "AuthorizeClusterSecurityGroupIngressResultTypeDef",
    {"ClusterSecurityGroup": "ClusterSecurityGroupTypeDef"},
    total=False,
)

AuthorizeSnapshotAccessResultTypeDef = TypedDict(
    "AuthorizeSnapshotAccessResultTypeDef", {"Snapshot": "SnapshotTypeDef"}, total=False
)

BatchDeleteClusterSnapshotsResultTypeDef = TypedDict(
    "BatchDeleteClusterSnapshotsResultTypeDef",
    {"Resources": List[str], "Errors": List["SnapshotErrorMessageTypeDef"]},
    total=False,
)

BatchModifyClusterSnapshotsOutputMessageTypeDef = TypedDict(
    "BatchModifyClusterSnapshotsOutputMessageTypeDef",
    {"Resources": List[str], "Errors": List["SnapshotErrorMessageTypeDef"]},
    total=False,
)

ClusterCredentialsTypeDef = TypedDict(
    "ClusterCredentialsTypeDef",
    {"DbUser": str, "DbPassword": str, "Expiration": datetime},
    total=False,
)

ClusterDbRevisionsMessageTypeDef = TypedDict(
    "ClusterDbRevisionsMessageTypeDef",
    {"Marker": str, "ClusterDbRevisions": List["ClusterDbRevisionTypeDef"]},
    total=False,
)

ClusterParameterGroupDetailsTypeDef = TypedDict(
    "ClusterParameterGroupDetailsTypeDef",
    {"Parameters": List["ParameterTypeDef"], "Marker": str},
    total=False,
)

ClusterParameterGroupNameMessageTypeDef = TypedDict(
    "ClusterParameterGroupNameMessageTypeDef",
    {"ParameterGroupName": str, "ParameterGroupStatus": str},
    total=False,
)

ClusterParameterGroupsMessageTypeDef = TypedDict(
    "ClusterParameterGroupsMessageTypeDef",
    {"Marker": str, "ParameterGroups": List["ClusterParameterGroupTypeDef"]},
    total=False,
)

ClusterSecurityGroupMessageTypeDef = TypedDict(
    "ClusterSecurityGroupMessageTypeDef",
    {"Marker": str, "ClusterSecurityGroups": List["ClusterSecurityGroupTypeDef"]},
    total=False,
)

ClusterSubnetGroupMessageTypeDef = TypedDict(
    "ClusterSubnetGroupMessageTypeDef",
    {"Marker": str, "ClusterSubnetGroups": List["ClusterSubnetGroupTypeDef"]},
    total=False,
)

ClusterVersionsMessageTypeDef = TypedDict(
    "ClusterVersionsMessageTypeDef",
    {"Marker": str, "ClusterVersions": List["ClusterVersionTypeDef"]},
    total=False,
)

ClustersMessageTypeDef = TypedDict(
    "ClustersMessageTypeDef", {"Marker": str, "Clusters": List["ClusterTypeDef"]}, total=False
)

CopyClusterSnapshotResultTypeDef = TypedDict(
    "CopyClusterSnapshotResultTypeDef", {"Snapshot": "SnapshotTypeDef"}, total=False
)

CreateClusterParameterGroupResultTypeDef = TypedDict(
    "CreateClusterParameterGroupResultTypeDef",
    {"ClusterParameterGroup": "ClusterParameterGroupTypeDef"},
    total=False,
)

CreateClusterResultTypeDef = TypedDict(
    "CreateClusterResultTypeDef", {"Cluster": "ClusterTypeDef"}, total=False
)

CreateClusterSecurityGroupResultTypeDef = TypedDict(
    "CreateClusterSecurityGroupResultTypeDef",
    {"ClusterSecurityGroup": "ClusterSecurityGroupTypeDef"},
    total=False,
)

CreateClusterSnapshotResultTypeDef = TypedDict(
    "CreateClusterSnapshotResultTypeDef", {"Snapshot": "SnapshotTypeDef"}, total=False
)

CreateClusterSubnetGroupResultTypeDef = TypedDict(
    "CreateClusterSubnetGroupResultTypeDef",
    {"ClusterSubnetGroup": "ClusterSubnetGroupTypeDef"},
    total=False,
)

CreateEventSubscriptionResultTypeDef = TypedDict(
    "CreateEventSubscriptionResultTypeDef",
    {"EventSubscription": "EventSubscriptionTypeDef"},
    total=False,
)

CreateHsmClientCertificateResultTypeDef = TypedDict(
    "CreateHsmClientCertificateResultTypeDef",
    {"HsmClientCertificate": "HsmClientCertificateTypeDef"},
    total=False,
)

CreateHsmConfigurationResultTypeDef = TypedDict(
    "CreateHsmConfigurationResultTypeDef",
    {"HsmConfiguration": "HsmConfigurationTypeDef"},
    total=False,
)

CreateSnapshotCopyGrantResultTypeDef = TypedDict(
    "CreateSnapshotCopyGrantResultTypeDef",
    {"SnapshotCopyGrant": "SnapshotCopyGrantTypeDef"},
    total=False,
)

CustomerStorageMessageTypeDef = TypedDict(
    "CustomerStorageMessageTypeDef",
    {"TotalBackupSizeInMegaBytes": float, "TotalProvisionedStorageInMegaBytes": float},
    total=False,
)

DeleteClusterResultTypeDef = TypedDict(
    "DeleteClusterResultTypeDef", {"Cluster": "ClusterTypeDef"}, total=False
)

_RequiredDeleteClusterSnapshotMessageTypeDef = TypedDict(
    "_RequiredDeleteClusterSnapshotMessageTypeDef", {"SnapshotIdentifier": str}
)
_OptionalDeleteClusterSnapshotMessageTypeDef = TypedDict(
    "_OptionalDeleteClusterSnapshotMessageTypeDef", {"SnapshotClusterIdentifier": str}, total=False
)


class DeleteClusterSnapshotMessageTypeDef(
    _RequiredDeleteClusterSnapshotMessageTypeDef, _OptionalDeleteClusterSnapshotMessageTypeDef
):
    pass


DeleteClusterSnapshotResultTypeDef = TypedDict(
    "DeleteClusterSnapshotResultTypeDef", {"Snapshot": "SnapshotTypeDef"}, total=False
)

DescribeDefaultClusterParametersResultTypeDef = TypedDict(
    "DescribeDefaultClusterParametersResultTypeDef",
    {"DefaultClusterParameters": "DefaultClusterParametersTypeDef"},
    total=False,
)

DescribeSnapshotSchedulesOutputMessageTypeDef = TypedDict(
    "DescribeSnapshotSchedulesOutputMessageTypeDef",
    {"SnapshotSchedules": List["SnapshotScheduleTypeDef"], "Marker": str},
    total=False,
)

DisableSnapshotCopyResultTypeDef = TypedDict(
    "DisableSnapshotCopyResultTypeDef", {"Cluster": "ClusterTypeDef"}, total=False
)

EnableSnapshotCopyResultTypeDef = TypedDict(
    "EnableSnapshotCopyResultTypeDef", {"Cluster": "ClusterTypeDef"}, total=False
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

GetReservedNodeExchangeOfferingsOutputMessageTypeDef = TypedDict(
    "GetReservedNodeExchangeOfferingsOutputMessageTypeDef",
    {"Marker": str, "ReservedNodeOfferings": List["ReservedNodeOfferingTypeDef"]},
    total=False,
)

HsmClientCertificateMessageTypeDef = TypedDict(
    "HsmClientCertificateMessageTypeDef",
    {"Marker": str, "HsmClientCertificates": List["HsmClientCertificateTypeDef"]},
    total=False,
)

HsmConfigurationMessageTypeDef = TypedDict(
    "HsmConfigurationMessageTypeDef",
    {"Marker": str, "HsmConfigurations": List["HsmConfigurationTypeDef"]},
    total=False,
)

LoggingStatusTypeDef = TypedDict(
    "LoggingStatusTypeDef",
    {
        "LoggingEnabled": bool,
        "BucketName": str,
        "S3KeyPrefix": str,
        "LastSuccessfulDeliveryTime": datetime,
        "LastFailureTime": datetime,
        "LastFailureMessage": str,
    },
    total=False,
)

ModifyClusterDbRevisionResultTypeDef = TypedDict(
    "ModifyClusterDbRevisionResultTypeDef", {"Cluster": "ClusterTypeDef"}, total=False
)

ModifyClusterIamRolesResultTypeDef = TypedDict(
    "ModifyClusterIamRolesResultTypeDef", {"Cluster": "ClusterTypeDef"}, total=False
)

ModifyClusterMaintenanceResultTypeDef = TypedDict(
    "ModifyClusterMaintenanceResultTypeDef", {"Cluster": "ClusterTypeDef"}, total=False
)

ModifyClusterResultTypeDef = TypedDict(
    "ModifyClusterResultTypeDef", {"Cluster": "ClusterTypeDef"}, total=False
)

ModifyClusterSnapshotResultTypeDef = TypedDict(
    "ModifyClusterSnapshotResultTypeDef", {"Snapshot": "SnapshotTypeDef"}, total=False
)

ModifyClusterSubnetGroupResultTypeDef = TypedDict(
    "ModifyClusterSubnetGroupResultTypeDef",
    {"ClusterSubnetGroup": "ClusterSubnetGroupTypeDef"},
    total=False,
)

ModifyEventSubscriptionResultTypeDef = TypedDict(
    "ModifyEventSubscriptionResultTypeDef",
    {"EventSubscription": "EventSubscriptionTypeDef"},
    total=False,
)

ModifySnapshotCopyRetentionPeriodResultTypeDef = TypedDict(
    "ModifySnapshotCopyRetentionPeriodResultTypeDef", {"Cluster": "ClusterTypeDef"}, total=False
)

NodeConfigurationOptionsFilterTypeDef = TypedDict(
    "NodeConfigurationOptionsFilterTypeDef",
    {
        "Name": Literal["NodeType", "NumberOfNodes", "EstimatedDiskUtilizationPercent", "Mode"],
        "Operator": Literal["eq", "lt", "gt", "le", "ge", "in", "between"],
        "Values": List[str],
    },
    total=False,
)

NodeConfigurationOptionsMessageTypeDef = TypedDict(
    "NodeConfigurationOptionsMessageTypeDef",
    {"NodeConfigurationOptionList": List["NodeConfigurationOptionTypeDef"], "Marker": str},
    total=False,
)

OrderableClusterOptionsMessageTypeDef = TypedDict(
    "OrderableClusterOptionsMessageTypeDef",
    {"OrderableClusterOptions": List["OrderableClusterOptionTypeDef"], "Marker": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PauseClusterResultTypeDef = TypedDict(
    "PauseClusterResultTypeDef", {"Cluster": "ClusterTypeDef"}, total=False
)

PurchaseReservedNodeOfferingResultTypeDef = TypedDict(
    "PurchaseReservedNodeOfferingResultTypeDef",
    {"ReservedNode": "ReservedNodeTypeDef"},
    total=False,
)

RebootClusterResultTypeDef = TypedDict(
    "RebootClusterResultTypeDef", {"Cluster": "ClusterTypeDef"}, total=False
)

ReservedNodeOfferingsMessageTypeDef = TypedDict(
    "ReservedNodeOfferingsMessageTypeDef",
    {"Marker": str, "ReservedNodeOfferings": List["ReservedNodeOfferingTypeDef"]},
    total=False,
)

ReservedNodesMessageTypeDef = TypedDict(
    "ReservedNodesMessageTypeDef",
    {"Marker": str, "ReservedNodes": List["ReservedNodeTypeDef"]},
    total=False,
)

ResizeClusterResultTypeDef = TypedDict(
    "ResizeClusterResultTypeDef", {"Cluster": "ClusterTypeDef"}, total=False
)

ResizeProgressMessageTypeDef = TypedDict(
    "ResizeProgressMessageTypeDef",
    {
        "TargetNodeType": str,
        "TargetNumberOfNodes": int,
        "TargetClusterType": str,
        "Status": str,
        "ImportTablesCompleted": List[str],
        "ImportTablesInProgress": List[str],
        "ImportTablesNotStarted": List[str],
        "AvgResizeRateInMegaBytesPerSecond": float,
        "TotalResizeDataInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ResizeType": str,
        "Message": str,
        "TargetEncryptionType": str,
        "DataTransferProgressPercent": float,
    },
    total=False,
)

RestoreFromClusterSnapshotResultTypeDef = TypedDict(
    "RestoreFromClusterSnapshotResultTypeDef", {"Cluster": "ClusterTypeDef"}, total=False
)

RestoreTableFromClusterSnapshotResultTypeDef = TypedDict(
    "RestoreTableFromClusterSnapshotResultTypeDef",
    {"TableRestoreStatus": "TableRestoreStatusTypeDef"},
    total=False,
)

ResumeClusterResultTypeDef = TypedDict(
    "ResumeClusterResultTypeDef", {"Cluster": "ClusterTypeDef"}, total=False
)

RevokeClusterSecurityGroupIngressResultTypeDef = TypedDict(
    "RevokeClusterSecurityGroupIngressResultTypeDef",
    {"ClusterSecurityGroup": "ClusterSecurityGroupTypeDef"},
    total=False,
)

RevokeSnapshotAccessResultTypeDef = TypedDict(
    "RevokeSnapshotAccessResultTypeDef", {"Snapshot": "SnapshotTypeDef"}, total=False
)

RotateEncryptionKeyResultTypeDef = TypedDict(
    "RotateEncryptionKeyResultTypeDef", {"Cluster": "ClusterTypeDef"}, total=False
)

ScheduledActionFilterTypeDef = TypedDict(
    "ScheduledActionFilterTypeDef",
    {"Name": Literal["cluster-identifier", "iam-role"], "Values": List[str]},
)

ScheduledActionsMessageTypeDef = TypedDict(
    "ScheduledActionsMessageTypeDef",
    {"Marker": str, "ScheduledActions": List["ScheduledActionTypeDef"]},
    total=False,
)

SnapshotCopyGrantMessageTypeDef = TypedDict(
    "SnapshotCopyGrantMessageTypeDef",
    {"Marker": str, "SnapshotCopyGrants": List["SnapshotCopyGrantTypeDef"]},
    total=False,
)

SnapshotMessageTypeDef = TypedDict(
    "SnapshotMessageTypeDef", {"Marker": str, "Snapshots": List["SnapshotTypeDef"]}, total=False
)

_RequiredSnapshotSortingEntityTypeDef = TypedDict(
    "_RequiredSnapshotSortingEntityTypeDef",
    {"Attribute": Literal["SOURCE_TYPE", "TOTAL_SIZE", "CREATE_TIME"]},
)
_OptionalSnapshotSortingEntityTypeDef = TypedDict(
    "_OptionalSnapshotSortingEntityTypeDef", {"SortOrder": Literal["ASC", "DESC"]}, total=False
)


class SnapshotSortingEntityTypeDef(
    _RequiredSnapshotSortingEntityTypeDef, _OptionalSnapshotSortingEntityTypeDef
):
    pass


TableRestoreStatusMessageTypeDef = TypedDict(
    "TableRestoreStatusMessageTypeDef",
    {"TableRestoreStatusDetails": List["TableRestoreStatusTypeDef"], "Marker": str},
    total=False,
)

TaggedResourceListMessageTypeDef = TypedDict(
    "TaggedResourceListMessageTypeDef",
    {"TaggedResources": List["TaggedResourceTypeDef"], "Marker": str},
    total=False,
)

TrackListMessageTypeDef = TypedDict(
    "TrackListMessageTypeDef",
    {"MaintenanceTracks": List["MaintenanceTrackTypeDef"], "Marker": str},
    total=False,
)

UsageLimitListTypeDef = TypedDict(
    "UsageLimitListTypeDef", {"UsageLimits": List["UsageLimitTypeDef"], "Marker": str}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
