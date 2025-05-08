"""
Type annotations for docdb service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_docdb.type_defs import AddSourceIdentifierToSubscriptionMessageTypeDef

    data: AddSourceIdentifierToSubscriptionMessageTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import ApplyMethodType, SourceTypeType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AddSourceIdentifierToSubscriptionMessageTypeDef",
    "AddSourceIdentifierToSubscriptionResultTypeDef",
    "AddTagsToResourceMessageTypeDef",
    "ApplyPendingMaintenanceActionMessageTypeDef",
    "ApplyPendingMaintenanceActionResultTypeDef",
    "AvailabilityZoneTypeDef",
    "CertificateDetailsTypeDef",
    "CertificateMessageTypeDef",
    "CertificateTypeDef",
    "CloudwatchLogsExportConfigurationTypeDef",
    "ClusterMasterUserSecretTypeDef",
    "CopyDBClusterParameterGroupMessageTypeDef",
    "CopyDBClusterParameterGroupResultTypeDef",
    "CopyDBClusterSnapshotMessageTypeDef",
    "CopyDBClusterSnapshotResultTypeDef",
    "CreateDBClusterMessageTypeDef",
    "CreateDBClusterParameterGroupMessageTypeDef",
    "CreateDBClusterParameterGroupResultTypeDef",
    "CreateDBClusterResultTypeDef",
    "CreateDBClusterSnapshotMessageTypeDef",
    "CreateDBClusterSnapshotResultTypeDef",
    "CreateDBInstanceMessageTypeDef",
    "CreateDBInstanceResultTypeDef",
    "CreateDBSubnetGroupMessageTypeDef",
    "CreateDBSubnetGroupResultTypeDef",
    "CreateEventSubscriptionMessageTypeDef",
    "CreateEventSubscriptionResultTypeDef",
    "CreateGlobalClusterMessageTypeDef",
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
    "DeleteDBClusterMessageTypeDef",
    "DeleteDBClusterParameterGroupMessageTypeDef",
    "DeleteDBClusterResultTypeDef",
    "DeleteDBClusterSnapshotMessageTypeDef",
    "DeleteDBClusterSnapshotResultTypeDef",
    "DeleteDBInstanceMessageTypeDef",
    "DeleteDBInstanceResultTypeDef",
    "DeleteDBSubnetGroupMessageTypeDef",
    "DeleteEventSubscriptionMessageTypeDef",
    "DeleteEventSubscriptionResultTypeDef",
    "DeleteGlobalClusterMessageTypeDef",
    "DeleteGlobalClusterResultTypeDef",
    "DescribeCertificatesMessagePaginateTypeDef",
    "DescribeCertificatesMessageTypeDef",
    "DescribeDBClusterParameterGroupsMessagePaginateTypeDef",
    "DescribeDBClusterParameterGroupsMessageTypeDef",
    "DescribeDBClusterParametersMessagePaginateTypeDef",
    "DescribeDBClusterParametersMessageTypeDef",
    "DescribeDBClusterSnapshotAttributesMessageTypeDef",
    "DescribeDBClusterSnapshotAttributesResultTypeDef",
    "DescribeDBClusterSnapshotsMessagePaginateTypeDef",
    "DescribeDBClusterSnapshotsMessageTypeDef",
    "DescribeDBClustersMessagePaginateTypeDef",
    "DescribeDBClustersMessageTypeDef",
    "DescribeDBEngineVersionsMessagePaginateTypeDef",
    "DescribeDBEngineVersionsMessageTypeDef",
    "DescribeDBInstancesMessagePaginateTypeDef",
    "DescribeDBInstancesMessageTypeDef",
    "DescribeDBInstancesMessageWaitExtraTypeDef",
    "DescribeDBInstancesMessageWaitTypeDef",
    "DescribeDBSubnetGroupsMessagePaginateTypeDef",
    "DescribeDBSubnetGroupsMessageTypeDef",
    "DescribeEngineDefaultClusterParametersMessageTypeDef",
    "DescribeEngineDefaultClusterParametersResultTypeDef",
    "DescribeEventCategoriesMessageTypeDef",
    "DescribeEventSubscriptionsMessagePaginateTypeDef",
    "DescribeEventSubscriptionsMessageTypeDef",
    "DescribeEventsMessagePaginateTypeDef",
    "DescribeEventsMessageTypeDef",
    "DescribeGlobalClustersMessagePaginateTypeDef",
    "DescribeGlobalClustersMessageTypeDef",
    "DescribeOrderableDBInstanceOptionsMessagePaginateTypeDef",
    "DescribeOrderableDBInstanceOptionsMessageTypeDef",
    "DescribePendingMaintenanceActionsMessagePaginateTypeDef",
    "DescribePendingMaintenanceActionsMessageTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EndpointTypeDef",
    "EngineDefaultsTypeDef",
    "EventCategoriesMapTypeDef",
    "EventCategoriesMessageTypeDef",
    "EventSubscriptionTypeDef",
    "EventSubscriptionsMessageTypeDef",
    "EventTypeDef",
    "EventsMessageTypeDef",
    "FailoverDBClusterMessageTypeDef",
    "FailoverDBClusterResultTypeDef",
    "FailoverGlobalClusterMessageTypeDef",
    "FailoverGlobalClusterResultTypeDef",
    "FilterTypeDef",
    "GlobalClusterMemberTypeDef",
    "GlobalClusterTypeDef",
    "GlobalClustersMessageTypeDef",
    "ListTagsForResourceMessageTypeDef",
    "ModifyDBClusterMessageTypeDef",
    "ModifyDBClusterParameterGroupMessageTypeDef",
    "ModifyDBClusterResultTypeDef",
    "ModifyDBClusterSnapshotAttributeMessageTypeDef",
    "ModifyDBClusterSnapshotAttributeResultTypeDef",
    "ModifyDBInstanceMessageTypeDef",
    "ModifyDBInstanceResultTypeDef",
    "ModifyDBSubnetGroupMessageTypeDef",
    "ModifyDBSubnetGroupResultTypeDef",
    "ModifyEventSubscriptionMessageTypeDef",
    "ModifyEventSubscriptionResultTypeDef",
    "ModifyGlobalClusterMessageTypeDef",
    "ModifyGlobalClusterResultTypeDef",
    "OrderableDBInstanceOptionTypeDef",
    "OrderableDBInstanceOptionsMessageTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterTypeDef",
    "PendingCloudwatchLogsExportsTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PendingMaintenanceActionsMessageTypeDef",
    "PendingModifiedValuesTypeDef",
    "RebootDBInstanceMessageTypeDef",
    "RebootDBInstanceResultTypeDef",
    "RemoveFromGlobalClusterMessageTypeDef",
    "RemoveFromGlobalClusterResultTypeDef",
    "RemoveSourceIdentifierFromSubscriptionMessageTypeDef",
    "RemoveSourceIdentifierFromSubscriptionResultTypeDef",
    "RemoveTagsFromResourceMessageTypeDef",
    "ResetDBClusterParameterGroupMessageTypeDef",
    "ResourcePendingMaintenanceActionsTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreDBClusterFromSnapshotMessageTypeDef",
    "RestoreDBClusterFromSnapshotResultTypeDef",
    "RestoreDBClusterToPointInTimeMessageTypeDef",
    "RestoreDBClusterToPointInTimeResultTypeDef",
    "StartDBClusterMessageTypeDef",
    "StartDBClusterResultTypeDef",
    "StopDBClusterMessageTypeDef",
    "StopDBClusterResultTypeDef",
    "SubnetTypeDef",
    "SwitchoverGlobalClusterMessageTypeDef",
    "SwitchoverGlobalClusterResultTypeDef",
    "TagListMessageTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "UpgradeTargetTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WaiterConfigTypeDef",
)

class AddSourceIdentifierToSubscriptionMessageTypeDef(TypedDict):
    SubscriptionName: str
    SourceIdentifier: str

class EventSubscriptionTypeDef(TypedDict):
    CustomerAwsId: NotRequired[str]
    CustSubscriptionId: NotRequired[str]
    SnsTopicArn: NotRequired[str]
    Status: NotRequired[str]
    SubscriptionCreationTime: NotRequired[str]
    SourceType: NotRequired[str]
    SourceIdsList: NotRequired[List[str]]
    EventCategoriesList: NotRequired[List[str]]
    Enabled: NotRequired[bool]
    EventSubscriptionArn: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class ApplyPendingMaintenanceActionMessageTypeDef(TypedDict):
    ResourceIdentifier: str
    ApplyAction: str
    OptInType: str

class AvailabilityZoneTypeDef(TypedDict):
    Name: NotRequired[str]

class CertificateDetailsTypeDef(TypedDict):
    CAIdentifier: NotRequired[str]
    ValidTill: NotRequired[datetime]

class CertificateTypeDef(TypedDict):
    CertificateIdentifier: NotRequired[str]
    CertificateType: NotRequired[str]
    Thumbprint: NotRequired[str]
    ValidFrom: NotRequired[datetime]
    ValidTill: NotRequired[datetime]
    CertificateArn: NotRequired[str]

class CloudwatchLogsExportConfigurationTypeDef(TypedDict):
    EnableLogTypes: NotRequired[Sequence[str]]
    DisableLogTypes: NotRequired[Sequence[str]]

class ClusterMasterUserSecretTypeDef(TypedDict):
    SecretArn: NotRequired[str]
    SecretStatus: NotRequired[str]
    KmsKeyId: NotRequired[str]

class DBClusterParameterGroupTypeDef(TypedDict):
    DBClusterParameterGroupName: NotRequired[str]
    DBParameterGroupFamily: NotRequired[str]
    Description: NotRequired[str]
    DBClusterParameterGroupArn: NotRequired[str]

class DBClusterSnapshotTypeDef(TypedDict):
    AvailabilityZones: NotRequired[List[str]]
    DBClusterSnapshotIdentifier: NotRequired[str]
    DBClusterIdentifier: NotRequired[str]
    SnapshotCreateTime: NotRequired[datetime]
    Engine: NotRequired[str]
    Status: NotRequired[str]
    Port: NotRequired[int]
    VpcId: NotRequired[str]
    ClusterCreateTime: NotRequired[datetime]
    MasterUsername: NotRequired[str]
    EngineVersion: NotRequired[str]
    SnapshotType: NotRequired[str]
    PercentProgress: NotRequired[int]
    StorageEncrypted: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    DBClusterSnapshotArn: NotRequired[str]
    SourceDBClusterSnapshotArn: NotRequired[str]
    StorageType: NotRequired[str]

class CreateGlobalClusterMessageTypeDef(TypedDict):
    GlobalClusterIdentifier: str
    SourceDBClusterIdentifier: NotRequired[str]
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    DeletionProtection: NotRequired[bool]
    DatabaseName: NotRequired[str]
    StorageEncrypted: NotRequired[bool]

class DBClusterMemberTypeDef(TypedDict):
    DBInstanceIdentifier: NotRequired[str]
    IsClusterWriter: NotRequired[bool]
    DBClusterParameterGroupStatus: NotRequired[str]
    PromotionTier: NotRequired[int]

class ParameterTypeDef(TypedDict):
    ParameterName: NotRequired[str]
    ParameterValue: NotRequired[str]
    Description: NotRequired[str]
    Source: NotRequired[str]
    ApplyType: NotRequired[str]
    DataType: NotRequired[str]
    AllowedValues: NotRequired[str]
    IsModifiable: NotRequired[bool]
    MinimumEngineVersion: NotRequired[str]
    ApplyMethod: NotRequired[ApplyMethodType]

class DBClusterRoleTypeDef(TypedDict):
    RoleArn: NotRequired[str]
    Status: NotRequired[str]

class DBClusterSnapshotAttributeTypeDef(TypedDict):
    AttributeName: NotRequired[str]
    AttributeValues: NotRequired[List[str]]

class VpcSecurityGroupMembershipTypeDef(TypedDict):
    VpcSecurityGroupId: NotRequired[str]
    Status: NotRequired[str]

class UpgradeTargetTypeDef(TypedDict):
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    Description: NotRequired[str]
    AutoUpgrade: NotRequired[bool]
    IsMajorVersionUpgrade: NotRequired[bool]

class DBInstanceStatusInfoTypeDef(TypedDict):
    StatusType: NotRequired[str]
    Normal: NotRequired[bool]
    Status: NotRequired[str]
    Message: NotRequired[str]

class EndpointTypeDef(TypedDict):
    Address: NotRequired[str]
    Port: NotRequired[int]
    HostedZoneId: NotRequired[str]

class DeleteDBClusterMessageTypeDef(TypedDict):
    DBClusterIdentifier: str
    SkipFinalSnapshot: NotRequired[bool]
    FinalDBSnapshotIdentifier: NotRequired[str]

class DeleteDBClusterParameterGroupMessageTypeDef(TypedDict):
    DBClusterParameterGroupName: str

class DeleteDBClusterSnapshotMessageTypeDef(TypedDict):
    DBClusterSnapshotIdentifier: str

class DeleteDBInstanceMessageTypeDef(TypedDict):
    DBInstanceIdentifier: str

class DeleteDBSubnetGroupMessageTypeDef(TypedDict):
    DBSubnetGroupName: str

class DeleteEventSubscriptionMessageTypeDef(TypedDict):
    SubscriptionName: str

class DeleteGlobalClusterMessageTypeDef(TypedDict):
    GlobalClusterIdentifier: str

class FilterTypeDef(TypedDict):
    Name: str
    Values: Sequence[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeDBClusterSnapshotAttributesMessageTypeDef(TypedDict):
    DBClusterSnapshotIdentifier: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

TimestampTypeDef = Union[datetime, str]

class EventCategoriesMapTypeDef(TypedDict):
    SourceType: NotRequired[str]
    EventCategories: NotRequired[List[str]]

class EventTypeDef(TypedDict):
    SourceIdentifier: NotRequired[str]
    SourceType: NotRequired[SourceTypeType]
    Message: NotRequired[str]
    EventCategories: NotRequired[List[str]]
    Date: NotRequired[datetime]
    SourceArn: NotRequired[str]

class FailoverDBClusterMessageTypeDef(TypedDict):
    DBClusterIdentifier: NotRequired[str]
    TargetDBInstanceIdentifier: NotRequired[str]

class FailoverGlobalClusterMessageTypeDef(TypedDict):
    GlobalClusterIdentifier: str
    TargetDbClusterIdentifier: str
    AllowDataLoss: NotRequired[bool]
    Switchover: NotRequired[bool]

class GlobalClusterMemberTypeDef(TypedDict):
    DBClusterArn: NotRequired[str]
    Readers: NotRequired[List[str]]
    IsWriter: NotRequired[bool]

class ModifyDBClusterSnapshotAttributeMessageTypeDef(TypedDict):
    DBClusterSnapshotIdentifier: str
    AttributeName: str
    ValuesToAdd: NotRequired[Sequence[str]]
    ValuesToRemove: NotRequired[Sequence[str]]

class ModifyDBInstanceMessageTypeDef(TypedDict):
    DBInstanceIdentifier: str
    DBInstanceClass: NotRequired[str]
    ApplyImmediately: NotRequired[bool]
    PreferredMaintenanceWindow: NotRequired[str]
    AutoMinorVersionUpgrade: NotRequired[bool]
    NewDBInstanceIdentifier: NotRequired[str]
    CACertificateIdentifier: NotRequired[str]
    CopyTagsToSnapshot: NotRequired[bool]
    PromotionTier: NotRequired[int]
    EnablePerformanceInsights: NotRequired[bool]
    PerformanceInsightsKMSKeyId: NotRequired[str]
    CertificateRotationRestart: NotRequired[bool]

class ModifyDBSubnetGroupMessageTypeDef(TypedDict):
    DBSubnetGroupName: str
    SubnetIds: Sequence[str]
    DBSubnetGroupDescription: NotRequired[str]

class ModifyEventSubscriptionMessageTypeDef(TypedDict):
    SubscriptionName: str
    SnsTopicArn: NotRequired[str]
    SourceType: NotRequired[str]
    EventCategories: NotRequired[Sequence[str]]
    Enabled: NotRequired[bool]

class ModifyGlobalClusterMessageTypeDef(TypedDict):
    GlobalClusterIdentifier: str
    NewGlobalClusterIdentifier: NotRequired[str]
    DeletionProtection: NotRequired[bool]

class PendingCloudwatchLogsExportsTypeDef(TypedDict):
    LogTypesToEnable: NotRequired[List[str]]
    LogTypesToDisable: NotRequired[List[str]]

class PendingMaintenanceActionTypeDef(TypedDict):
    Action: NotRequired[str]
    AutoAppliedAfterDate: NotRequired[datetime]
    ForcedApplyDate: NotRequired[datetime]
    OptInStatus: NotRequired[str]
    CurrentApplyDate: NotRequired[datetime]
    Description: NotRequired[str]

class RebootDBInstanceMessageTypeDef(TypedDict):
    DBInstanceIdentifier: str
    ForceFailover: NotRequired[bool]

class RemoveFromGlobalClusterMessageTypeDef(TypedDict):
    GlobalClusterIdentifier: str
    DbClusterIdentifier: str

class RemoveSourceIdentifierFromSubscriptionMessageTypeDef(TypedDict):
    SubscriptionName: str
    SourceIdentifier: str

class RemoveTagsFromResourceMessageTypeDef(TypedDict):
    ResourceName: str
    TagKeys: Sequence[str]

class StartDBClusterMessageTypeDef(TypedDict):
    DBClusterIdentifier: str

class StopDBClusterMessageTypeDef(TypedDict):
    DBClusterIdentifier: str

class SwitchoverGlobalClusterMessageTypeDef(TypedDict):
    GlobalClusterIdentifier: str
    TargetDbClusterIdentifier: str

class AddSourceIdentifierToSubscriptionResultTypeDef(TypedDict):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventSubscriptionResultTypeDef(TypedDict):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterParameterGroupNameMessageTypeDef(TypedDict):
    DBClusterParameterGroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEventSubscriptionResultTypeDef(TypedDict):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class EventSubscriptionsMessageTypeDef(TypedDict):
    Marker: str
    EventSubscriptionsList: List[EventSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyEventSubscriptionResultTypeDef(TypedDict):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveSourceIdentifierFromSubscriptionResultTypeDef(TypedDict):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddTagsToResourceMessageTypeDef(TypedDict):
    ResourceName: str
    Tags: Sequence[TagTypeDef]

class CopyDBClusterParameterGroupMessageTypeDef(TypedDict):
    SourceDBClusterParameterGroupIdentifier: str
    TargetDBClusterParameterGroupIdentifier: str
    TargetDBClusterParameterGroupDescription: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class CopyDBClusterSnapshotMessageTypeDef(TypedDict):
    SourceDBClusterSnapshotIdentifier: str
    TargetDBClusterSnapshotIdentifier: str
    KmsKeyId: NotRequired[str]
    PreSignedUrl: NotRequired[str]
    CopyTags: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]
    SourceRegion: NotRequired[str]

class CreateDBClusterMessageTypeDef(TypedDict):
    DBClusterIdentifier: str
    Engine: str
    AvailabilityZones: NotRequired[Sequence[str]]
    BackupRetentionPeriod: NotRequired[int]
    DBClusterParameterGroupName: NotRequired[str]
    VpcSecurityGroupIds: NotRequired[Sequence[str]]
    DBSubnetGroupName: NotRequired[str]
    EngineVersion: NotRequired[str]
    Port: NotRequired[int]
    MasterUsername: NotRequired[str]
    MasterUserPassword: NotRequired[str]
    PreferredBackupWindow: NotRequired[str]
    PreferredMaintenanceWindow: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    StorageEncrypted: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    PreSignedUrl: NotRequired[str]
    EnableCloudwatchLogsExports: NotRequired[Sequence[str]]
    DeletionProtection: NotRequired[bool]
    GlobalClusterIdentifier: NotRequired[str]
    StorageType: NotRequired[str]
    ManageMasterUserPassword: NotRequired[bool]
    MasterUserSecretKmsKeyId: NotRequired[str]
    SourceRegion: NotRequired[str]

class CreateDBClusterParameterGroupMessageTypeDef(TypedDict):
    DBClusterParameterGroupName: str
    DBParameterGroupFamily: str
    Description: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateDBClusterSnapshotMessageTypeDef(TypedDict):
    DBClusterSnapshotIdentifier: str
    DBClusterIdentifier: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateDBInstanceMessageTypeDef(TypedDict):
    DBInstanceIdentifier: str
    DBInstanceClass: str
    Engine: str
    DBClusterIdentifier: str
    AvailabilityZone: NotRequired[str]
    PreferredMaintenanceWindow: NotRequired[str]
    AutoMinorVersionUpgrade: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]
    CopyTagsToSnapshot: NotRequired[bool]
    PromotionTier: NotRequired[int]
    EnablePerformanceInsights: NotRequired[bool]
    PerformanceInsightsKMSKeyId: NotRequired[str]
    CACertificateIdentifier: NotRequired[str]

class CreateDBSubnetGroupMessageTypeDef(TypedDict):
    DBSubnetGroupName: str
    DBSubnetGroupDescription: str
    SubnetIds: Sequence[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateEventSubscriptionMessageTypeDef(TypedDict):
    SubscriptionName: str
    SnsTopicArn: str
    SourceType: NotRequired[str]
    EventCategories: NotRequired[Sequence[str]]
    SourceIds: NotRequired[Sequence[str]]
    Enabled: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]

class RestoreDBClusterFromSnapshotMessageTypeDef(TypedDict):
    DBClusterIdentifier: str
    SnapshotIdentifier: str
    Engine: str
    AvailabilityZones: NotRequired[Sequence[str]]
    EngineVersion: NotRequired[str]
    Port: NotRequired[int]
    DBSubnetGroupName: NotRequired[str]
    VpcSecurityGroupIds: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    KmsKeyId: NotRequired[str]
    EnableCloudwatchLogsExports: NotRequired[Sequence[str]]
    DeletionProtection: NotRequired[bool]
    DBClusterParameterGroupName: NotRequired[str]
    StorageType: NotRequired[str]

class TagListMessageTypeDef(TypedDict):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class OrderableDBInstanceOptionTypeDef(TypedDict):
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    DBInstanceClass: NotRequired[str]
    LicenseModel: NotRequired[str]
    AvailabilityZones: NotRequired[List[AvailabilityZoneTypeDef]]
    Vpc: NotRequired[bool]
    StorageType: NotRequired[str]

class SubnetTypeDef(TypedDict):
    SubnetIdentifier: NotRequired[str]
    SubnetAvailabilityZone: NotRequired[AvailabilityZoneTypeDef]
    SubnetStatus: NotRequired[str]

class CertificateMessageTypeDef(TypedDict):
    Certificates: List[CertificateTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBClusterMessageTypeDef(TypedDict):
    DBClusterIdentifier: str
    NewDBClusterIdentifier: NotRequired[str]
    ApplyImmediately: NotRequired[bool]
    BackupRetentionPeriod: NotRequired[int]
    DBClusterParameterGroupName: NotRequired[str]
    VpcSecurityGroupIds: NotRequired[Sequence[str]]
    Port: NotRequired[int]
    MasterUserPassword: NotRequired[str]
    PreferredBackupWindow: NotRequired[str]
    PreferredMaintenanceWindow: NotRequired[str]
    CloudwatchLogsExportConfiguration: NotRequired[CloudwatchLogsExportConfigurationTypeDef]
    EngineVersion: NotRequired[str]
    AllowMajorVersionUpgrade: NotRequired[bool]
    DeletionProtection: NotRequired[bool]
    StorageType: NotRequired[str]
    ManageMasterUserPassword: NotRequired[bool]
    MasterUserSecretKmsKeyId: NotRequired[str]
    RotateMasterUserPassword: NotRequired[bool]

class CopyDBClusterParameterGroupResultTypeDef(TypedDict):
    DBClusterParameterGroup: DBClusterParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBClusterParameterGroupResultTypeDef(TypedDict):
    DBClusterParameterGroup: DBClusterParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterParameterGroupsMessageTypeDef(TypedDict):
    Marker: str
    DBClusterParameterGroups: List[DBClusterParameterGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CopyDBClusterSnapshotResultTypeDef(TypedDict):
    DBClusterSnapshot: DBClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBClusterSnapshotResultTypeDef(TypedDict):
    DBClusterSnapshot: DBClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterSnapshotMessageTypeDef(TypedDict):
    Marker: str
    DBClusterSnapshots: List[DBClusterSnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBClusterSnapshotResultTypeDef(TypedDict):
    DBClusterSnapshot: DBClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterParameterGroupDetailsTypeDef(TypedDict):
    Parameters: List[ParameterTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class EngineDefaultsTypeDef(TypedDict):
    DBParameterGroupFamily: NotRequired[str]
    Marker: NotRequired[str]
    Parameters: NotRequired[List[ParameterTypeDef]]

class ModifyDBClusterParameterGroupMessageTypeDef(TypedDict):
    DBClusterParameterGroupName: str
    Parameters: Sequence[ParameterTypeDef]

class ResetDBClusterParameterGroupMessageTypeDef(TypedDict):
    DBClusterParameterGroupName: str
    ResetAllParameters: NotRequired[bool]
    Parameters: NotRequired[Sequence[ParameterTypeDef]]

class DBClusterSnapshotAttributesResultTypeDef(TypedDict):
    DBClusterSnapshotIdentifier: NotRequired[str]
    DBClusterSnapshotAttributes: NotRequired[List[DBClusterSnapshotAttributeTypeDef]]

class DBClusterTypeDef(TypedDict):
    AvailabilityZones: NotRequired[List[str]]
    BackupRetentionPeriod: NotRequired[int]
    DBClusterIdentifier: NotRequired[str]
    DBClusterParameterGroup: NotRequired[str]
    DBSubnetGroup: NotRequired[str]
    Status: NotRequired[str]
    PercentProgress: NotRequired[str]
    EarliestRestorableTime: NotRequired[datetime]
    Endpoint: NotRequired[str]
    ReaderEndpoint: NotRequired[str]
    MultiAZ: NotRequired[bool]
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    LatestRestorableTime: NotRequired[datetime]
    Port: NotRequired[int]
    MasterUsername: NotRequired[str]
    PreferredBackupWindow: NotRequired[str]
    PreferredMaintenanceWindow: NotRequired[str]
    ReplicationSourceIdentifier: NotRequired[str]
    ReadReplicaIdentifiers: NotRequired[List[str]]
    DBClusterMembers: NotRequired[List[DBClusterMemberTypeDef]]
    VpcSecurityGroups: NotRequired[List[VpcSecurityGroupMembershipTypeDef]]
    HostedZoneId: NotRequired[str]
    StorageEncrypted: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    DbClusterResourceId: NotRequired[str]
    DBClusterArn: NotRequired[str]
    AssociatedRoles: NotRequired[List[DBClusterRoleTypeDef]]
    CloneGroupId: NotRequired[str]
    ClusterCreateTime: NotRequired[datetime]
    EnabledCloudwatchLogsExports: NotRequired[List[str]]
    DeletionProtection: NotRequired[bool]
    StorageType: NotRequired[str]
    MasterUserSecret: NotRequired[ClusterMasterUserSecretTypeDef]

class DBEngineVersionTypeDef(TypedDict):
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    DBParameterGroupFamily: NotRequired[str]
    DBEngineDescription: NotRequired[str]
    DBEngineVersionDescription: NotRequired[str]
    ValidUpgradeTarget: NotRequired[List[UpgradeTargetTypeDef]]
    ExportableLogTypes: NotRequired[List[str]]
    SupportsLogExportsToCloudwatchLogs: NotRequired[bool]
    SupportedCACertificateIdentifiers: NotRequired[List[str]]
    SupportsCertificateRotationWithoutRestart: NotRequired[bool]

class DescribeCertificatesMessageTypeDef(TypedDict):
    CertificateIdentifier: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeDBClusterParameterGroupsMessageTypeDef(TypedDict):
    DBClusterParameterGroupName: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeDBClusterParametersMessageTypeDef(TypedDict):
    DBClusterParameterGroupName: str
    Source: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeDBClusterSnapshotsMessageTypeDef(TypedDict):
    DBClusterIdentifier: NotRequired[str]
    DBClusterSnapshotIdentifier: NotRequired[str]
    SnapshotType: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    IncludeShared: NotRequired[bool]
    IncludePublic: NotRequired[bool]

class DescribeDBClustersMessageTypeDef(TypedDict):
    DBClusterIdentifier: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeDBEngineVersionsMessageTypeDef(TypedDict):
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    DBParameterGroupFamily: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    DefaultOnly: NotRequired[bool]
    ListSupportedCharacterSets: NotRequired[bool]
    ListSupportedTimezones: NotRequired[bool]

class DescribeDBInstancesMessageTypeDef(TypedDict):
    DBInstanceIdentifier: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeDBSubnetGroupsMessageTypeDef(TypedDict):
    DBSubnetGroupName: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeEngineDefaultClusterParametersMessageTypeDef(TypedDict):
    DBParameterGroupFamily: str
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeEventCategoriesMessageTypeDef(TypedDict):
    SourceType: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class DescribeEventSubscriptionsMessageTypeDef(TypedDict):
    SubscriptionName: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeGlobalClustersMessageTypeDef(TypedDict):
    GlobalClusterIdentifier: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeOrderableDBInstanceOptionsMessageTypeDef(TypedDict):
    Engine: str
    EngineVersion: NotRequired[str]
    DBInstanceClass: NotRequired[str]
    LicenseModel: NotRequired[str]
    Vpc: NotRequired[bool]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribePendingMaintenanceActionsMessageTypeDef(TypedDict):
    ResourceIdentifier: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    Marker: NotRequired[str]
    MaxRecords: NotRequired[int]

class ListTagsForResourceMessageTypeDef(TypedDict):
    ResourceName: str
    Filters: NotRequired[Sequence[FilterTypeDef]]

class DescribeCertificatesMessagePaginateTypeDef(TypedDict):
    CertificateIdentifier: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDBClusterParameterGroupsMessagePaginateTypeDef(TypedDict):
    DBClusterParameterGroupName: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDBClusterParametersMessagePaginateTypeDef(TypedDict):
    DBClusterParameterGroupName: str
    Source: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDBClusterSnapshotsMessagePaginateTypeDef(TypedDict):
    DBClusterIdentifier: NotRequired[str]
    DBClusterSnapshotIdentifier: NotRequired[str]
    SnapshotType: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    IncludeShared: NotRequired[bool]
    IncludePublic: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDBClustersMessagePaginateTypeDef(TypedDict):
    DBClusterIdentifier: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDBEngineVersionsMessagePaginateTypeDef(TypedDict):
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    DBParameterGroupFamily: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    DefaultOnly: NotRequired[bool]
    ListSupportedCharacterSets: NotRequired[bool]
    ListSupportedTimezones: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDBInstancesMessagePaginateTypeDef(TypedDict):
    DBInstanceIdentifier: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDBSubnetGroupsMessagePaginateTypeDef(TypedDict):
    DBSubnetGroupName: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEventSubscriptionsMessagePaginateTypeDef(TypedDict):
    SubscriptionName: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeGlobalClustersMessagePaginateTypeDef(TypedDict):
    GlobalClusterIdentifier: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeOrderableDBInstanceOptionsMessagePaginateTypeDef(TypedDict):
    Engine: str
    EngineVersion: NotRequired[str]
    DBInstanceClass: NotRequired[str]
    LicenseModel: NotRequired[str]
    Vpc: NotRequired[bool]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribePendingMaintenanceActionsMessagePaginateTypeDef(TypedDict):
    ResourceIdentifier: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDBInstancesMessageWaitExtraTypeDef(TypedDict):
    DBInstanceIdentifier: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeDBInstancesMessageWaitTypeDef(TypedDict):
    DBInstanceIdentifier: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeEventsMessagePaginateTypeDef(TypedDict):
    SourceIdentifier: NotRequired[str]
    SourceType: NotRequired[SourceTypeType]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    Duration: NotRequired[int]
    EventCategories: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEventsMessageTypeDef(TypedDict):
    SourceIdentifier: NotRequired[str]
    SourceType: NotRequired[SourceTypeType]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    Duration: NotRequired[int]
    EventCategories: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class RestoreDBClusterToPointInTimeMessageTypeDef(TypedDict):
    DBClusterIdentifier: str
    SourceDBClusterIdentifier: str
    RestoreType: NotRequired[str]
    RestoreToTime: NotRequired[TimestampTypeDef]
    UseLatestRestorableTime: NotRequired[bool]
    Port: NotRequired[int]
    DBSubnetGroupName: NotRequired[str]
    VpcSecurityGroupIds: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    KmsKeyId: NotRequired[str]
    EnableCloudwatchLogsExports: NotRequired[Sequence[str]]
    DeletionProtection: NotRequired[bool]
    StorageType: NotRequired[str]

class EventCategoriesMessageTypeDef(TypedDict):
    EventCategoriesMapList: List[EventCategoriesMapTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EventsMessageTypeDef(TypedDict):
    Marker: str
    Events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GlobalClusterTypeDef(TypedDict):
    GlobalClusterIdentifier: NotRequired[str]
    GlobalClusterResourceId: NotRequired[str]
    GlobalClusterArn: NotRequired[str]
    Status: NotRequired[str]
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    DatabaseName: NotRequired[str]
    StorageEncrypted: NotRequired[bool]
    DeletionProtection: NotRequired[bool]
    GlobalClusterMembers: NotRequired[List[GlobalClusterMemberTypeDef]]

class PendingModifiedValuesTypeDef(TypedDict):
    DBInstanceClass: NotRequired[str]
    AllocatedStorage: NotRequired[int]
    MasterUserPassword: NotRequired[str]
    Port: NotRequired[int]
    BackupRetentionPeriod: NotRequired[int]
    MultiAZ: NotRequired[bool]
    EngineVersion: NotRequired[str]
    LicenseModel: NotRequired[str]
    Iops: NotRequired[int]
    DBInstanceIdentifier: NotRequired[str]
    StorageType: NotRequired[str]
    CACertificateIdentifier: NotRequired[str]
    DBSubnetGroupName: NotRequired[str]
    PendingCloudwatchLogsExports: NotRequired[PendingCloudwatchLogsExportsTypeDef]

class ResourcePendingMaintenanceActionsTypeDef(TypedDict):
    ResourceIdentifier: NotRequired[str]
    PendingMaintenanceActionDetails: NotRequired[List[PendingMaintenanceActionTypeDef]]

class OrderableDBInstanceOptionsMessageTypeDef(TypedDict):
    OrderableDBInstanceOptions: List[OrderableDBInstanceOptionTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DBSubnetGroupTypeDef(TypedDict):
    DBSubnetGroupName: NotRequired[str]
    DBSubnetGroupDescription: NotRequired[str]
    VpcId: NotRequired[str]
    SubnetGroupStatus: NotRequired[str]
    Subnets: NotRequired[List[SubnetTypeDef]]
    DBSubnetGroupArn: NotRequired[str]

class DescribeEngineDefaultClusterParametersResultTypeDef(TypedDict):
    EngineDefaults: EngineDefaultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDBClusterSnapshotAttributesResultTypeDef(TypedDict):
    DBClusterSnapshotAttributesResult: DBClusterSnapshotAttributesResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBClusterSnapshotAttributeResultTypeDef(TypedDict):
    DBClusterSnapshotAttributesResult: DBClusterSnapshotAttributesResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBClusterResultTypeDef(TypedDict):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterMessageTypeDef(TypedDict):
    Marker: str
    DBClusters: List[DBClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBClusterResultTypeDef(TypedDict):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FailoverDBClusterResultTypeDef(TypedDict):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBClusterResultTypeDef(TypedDict):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreDBClusterFromSnapshotResultTypeDef(TypedDict):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreDBClusterToPointInTimeResultTypeDef(TypedDict):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartDBClusterResultTypeDef(TypedDict):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopDBClusterResultTypeDef(TypedDict):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBEngineVersionMessageTypeDef(TypedDict):
    Marker: str
    DBEngineVersions: List[DBEngineVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGlobalClusterResultTypeDef(TypedDict):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGlobalClusterResultTypeDef(TypedDict):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FailoverGlobalClusterResultTypeDef(TypedDict):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GlobalClustersMessageTypeDef(TypedDict):
    Marker: str
    GlobalClusters: List[GlobalClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyGlobalClusterResultTypeDef(TypedDict):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveFromGlobalClusterResultTypeDef(TypedDict):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SwitchoverGlobalClusterResultTypeDef(TypedDict):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ApplyPendingMaintenanceActionResultTypeDef(TypedDict):
    ResourcePendingMaintenanceActions: ResourcePendingMaintenanceActionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PendingMaintenanceActionsMessageTypeDef(TypedDict):
    PendingMaintenanceActions: List[ResourcePendingMaintenanceActionsTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBSubnetGroupResultTypeDef(TypedDict):
    DBSubnetGroup: DBSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBInstanceTypeDef(TypedDict):
    DBInstanceIdentifier: NotRequired[str]
    DBInstanceClass: NotRequired[str]
    Engine: NotRequired[str]
    DBInstanceStatus: NotRequired[str]
    Endpoint: NotRequired[EndpointTypeDef]
    InstanceCreateTime: NotRequired[datetime]
    PreferredBackupWindow: NotRequired[str]
    BackupRetentionPeriod: NotRequired[int]
    VpcSecurityGroups: NotRequired[List[VpcSecurityGroupMembershipTypeDef]]
    AvailabilityZone: NotRequired[str]
    DBSubnetGroup: NotRequired[DBSubnetGroupTypeDef]
    PreferredMaintenanceWindow: NotRequired[str]
    PendingModifiedValues: NotRequired[PendingModifiedValuesTypeDef]
    LatestRestorableTime: NotRequired[datetime]
    EngineVersion: NotRequired[str]
    AutoMinorVersionUpgrade: NotRequired[bool]
    PubliclyAccessible: NotRequired[bool]
    StatusInfos: NotRequired[List[DBInstanceStatusInfoTypeDef]]
    DBClusterIdentifier: NotRequired[str]
    StorageEncrypted: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    DbiResourceId: NotRequired[str]
    CACertificateIdentifier: NotRequired[str]
    CopyTagsToSnapshot: NotRequired[bool]
    PromotionTier: NotRequired[int]
    DBInstanceArn: NotRequired[str]
    EnabledCloudwatchLogsExports: NotRequired[List[str]]
    CertificateDetails: NotRequired[CertificateDetailsTypeDef]
    PerformanceInsightsEnabled: NotRequired[bool]
    PerformanceInsightsKMSKeyId: NotRequired[str]

class DBSubnetGroupMessageTypeDef(TypedDict):
    Marker: str
    DBSubnetGroups: List[DBSubnetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBSubnetGroupResultTypeDef(TypedDict):
    DBSubnetGroup: DBSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBInstanceResultTypeDef(TypedDict):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBInstanceMessageTypeDef(TypedDict):
    Marker: str
    DBInstances: List[DBInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBInstanceResultTypeDef(TypedDict):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBInstanceResultTypeDef(TypedDict):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RebootDBInstanceResultTypeDef(TypedDict):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
