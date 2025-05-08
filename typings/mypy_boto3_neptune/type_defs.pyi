"""
Type annotations for neptune service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_neptune.type_defs import AddRoleToDBClusterMessageTypeDef

    data: AddRoleToDBClusterMessageTypeDef = ...
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
    "AddRoleToDBClusterMessageTypeDef",
    "AddSourceIdentifierToSubscriptionMessageTypeDef",
    "AddSourceIdentifierToSubscriptionResultTypeDef",
    "AddTagsToResourceMessageTypeDef",
    "ApplyPendingMaintenanceActionMessageTypeDef",
    "ApplyPendingMaintenanceActionResultTypeDef",
    "AvailabilityZoneTypeDef",
    "CharacterSetTypeDef",
    "CloudwatchLogsExportConfigurationTypeDef",
    "ClusterPendingModifiedValuesTypeDef",
    "CopyDBClusterParameterGroupMessageTypeDef",
    "CopyDBClusterParameterGroupResultTypeDef",
    "CopyDBClusterSnapshotMessageTypeDef",
    "CopyDBClusterSnapshotResultTypeDef",
    "CopyDBParameterGroupMessageTypeDef",
    "CopyDBParameterGroupResultTypeDef",
    "CreateDBClusterEndpointMessageTypeDef",
    "CreateDBClusterEndpointOutputTypeDef",
    "CreateDBClusterMessageTypeDef",
    "CreateDBClusterParameterGroupMessageTypeDef",
    "CreateDBClusterParameterGroupResultTypeDef",
    "CreateDBClusterResultTypeDef",
    "CreateDBClusterSnapshotMessageTypeDef",
    "CreateDBClusterSnapshotResultTypeDef",
    "CreateDBInstanceMessageTypeDef",
    "CreateDBInstanceResultTypeDef",
    "CreateDBParameterGroupMessageTypeDef",
    "CreateDBParameterGroupResultTypeDef",
    "CreateDBSubnetGroupMessageTypeDef",
    "CreateDBSubnetGroupResultTypeDef",
    "CreateEventSubscriptionMessageTypeDef",
    "CreateEventSubscriptionResultTypeDef",
    "CreateGlobalClusterMessageTypeDef",
    "CreateGlobalClusterResultTypeDef",
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
    "DeleteDBClusterEndpointMessageTypeDef",
    "DeleteDBClusterEndpointOutputTypeDef",
    "DeleteDBClusterMessageTypeDef",
    "DeleteDBClusterParameterGroupMessageTypeDef",
    "DeleteDBClusterResultTypeDef",
    "DeleteDBClusterSnapshotMessageTypeDef",
    "DeleteDBClusterSnapshotResultTypeDef",
    "DeleteDBInstanceMessageTypeDef",
    "DeleteDBInstanceResultTypeDef",
    "DeleteDBParameterGroupMessageTypeDef",
    "DeleteDBSubnetGroupMessageTypeDef",
    "DeleteEventSubscriptionMessageTypeDef",
    "DeleteEventSubscriptionResultTypeDef",
    "DeleteGlobalClusterMessageTypeDef",
    "DeleteGlobalClusterResultTypeDef",
    "DescribeDBClusterEndpointsMessagePaginateTypeDef",
    "DescribeDBClusterEndpointsMessageTypeDef",
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
    "DescribeDBParameterGroupsMessagePaginateTypeDef",
    "DescribeDBParameterGroupsMessageTypeDef",
    "DescribeDBParametersMessagePaginateTypeDef",
    "DescribeDBParametersMessageTypeDef",
    "DescribeDBSubnetGroupsMessagePaginateTypeDef",
    "DescribeDBSubnetGroupsMessageTypeDef",
    "DescribeEngineDefaultClusterParametersMessageTypeDef",
    "DescribeEngineDefaultClusterParametersResultTypeDef",
    "DescribeEngineDefaultParametersMessagePaginateTypeDef",
    "DescribeEngineDefaultParametersMessageTypeDef",
    "DescribeEngineDefaultParametersResultTypeDef",
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
    "DescribeValidDBInstanceModificationsMessageTypeDef",
    "DescribeValidDBInstanceModificationsResultTypeDef",
    "DomainMembershipTypeDef",
    "DoubleRangeTypeDef",
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
    "ModifyDBClusterEndpointMessageTypeDef",
    "ModifyDBClusterEndpointOutputTypeDef",
    "ModifyDBClusterMessageTypeDef",
    "ModifyDBClusterParameterGroupMessageTypeDef",
    "ModifyDBClusterResultTypeDef",
    "ModifyDBClusterSnapshotAttributeMessageTypeDef",
    "ModifyDBClusterSnapshotAttributeResultTypeDef",
    "ModifyDBInstanceMessageTypeDef",
    "ModifyDBInstanceResultTypeDef",
    "ModifyDBParameterGroupMessageTypeDef",
    "ModifyDBSubnetGroupMessageTypeDef",
    "ModifyDBSubnetGroupResultTypeDef",
    "ModifyEventSubscriptionMessageTypeDef",
    "ModifyEventSubscriptionResultTypeDef",
    "ModifyGlobalClusterMessageTypeDef",
    "ModifyGlobalClusterResultTypeDef",
    "OptionGroupMembershipTypeDef",
    "OrderableDBInstanceOptionTypeDef",
    "OrderableDBInstanceOptionsMessageTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterTypeDef",
    "PendingCloudwatchLogsExportsTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PendingMaintenanceActionsMessageTypeDef",
    "PendingModifiedValuesTypeDef",
    "PromoteReadReplicaDBClusterMessageTypeDef",
    "PromoteReadReplicaDBClusterResultTypeDef",
    "RangeTypeDef",
    "RebootDBInstanceMessageTypeDef",
    "RebootDBInstanceResultTypeDef",
    "RemoveFromGlobalClusterMessageTypeDef",
    "RemoveFromGlobalClusterResultTypeDef",
    "RemoveRoleFromDBClusterMessageTypeDef",
    "RemoveSourceIdentifierFromSubscriptionMessageTypeDef",
    "RemoveSourceIdentifierFromSubscriptionResultTypeDef",
    "RemoveTagsFromResourceMessageTypeDef",
    "ResetDBClusterParameterGroupMessageTypeDef",
    "ResetDBParameterGroupMessageTypeDef",
    "ResourcePendingMaintenanceActionsTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreDBClusterFromSnapshotMessageTypeDef",
    "RestoreDBClusterFromSnapshotResultTypeDef",
    "RestoreDBClusterToPointInTimeMessageTypeDef",
    "RestoreDBClusterToPointInTimeResultTypeDef",
    "ServerlessV2ScalingConfigurationInfoTypeDef",
    "ServerlessV2ScalingConfigurationTypeDef",
    "StartDBClusterMessageTypeDef",
    "StartDBClusterResultTypeDef",
    "StopDBClusterMessageTypeDef",
    "StopDBClusterResultTypeDef",
    "SubnetTypeDef",
    "TagListMessageTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "TimezoneTypeDef",
    "UpgradeTargetTypeDef",
    "ValidDBInstanceModificationsMessageTypeDef",
    "ValidStorageOptionsTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WaiterConfigTypeDef",
)

class AddRoleToDBClusterMessageTypeDef(TypedDict):
    DBClusterIdentifier: str
    RoleArn: str
    FeatureName: NotRequired[str]

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

class CharacterSetTypeDef(TypedDict):
    CharacterSetName: NotRequired[str]
    CharacterSetDescription: NotRequired[str]

class CloudwatchLogsExportConfigurationTypeDef(TypedDict):
    EnableLogTypes: NotRequired[Sequence[str]]
    DisableLogTypes: NotRequired[Sequence[str]]

class PendingCloudwatchLogsExportsTypeDef(TypedDict):
    LogTypesToEnable: NotRequired[List[str]]
    LogTypesToDisable: NotRequired[List[str]]

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
    AllocatedStorage: NotRequired[int]
    Status: NotRequired[str]
    Port: NotRequired[int]
    VpcId: NotRequired[str]
    ClusterCreateTime: NotRequired[datetime]
    MasterUsername: NotRequired[str]
    EngineVersion: NotRequired[str]
    LicenseModel: NotRequired[str]
    SnapshotType: NotRequired[str]
    PercentProgress: NotRequired[int]
    StorageEncrypted: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    DBClusterSnapshotArn: NotRequired[str]
    SourceDBClusterSnapshotArn: NotRequired[str]
    IAMDatabaseAuthenticationEnabled: NotRequired[bool]
    StorageType: NotRequired[str]

class DBParameterGroupTypeDef(TypedDict):
    DBParameterGroupName: NotRequired[str]
    DBParameterGroupFamily: NotRequired[str]
    Description: NotRequired[str]
    DBParameterGroupArn: NotRequired[str]

class ServerlessV2ScalingConfigurationTypeDef(TypedDict):
    MinCapacity: NotRequired[float]
    MaxCapacity: NotRequired[float]

class CreateGlobalClusterMessageTypeDef(TypedDict):
    GlobalClusterIdentifier: str
    SourceDBClusterIdentifier: NotRequired[str]
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    DeletionProtection: NotRequired[bool]
    StorageEncrypted: NotRequired[bool]

class DBClusterEndpointTypeDef(TypedDict):
    DBClusterEndpointIdentifier: NotRequired[str]
    DBClusterIdentifier: NotRequired[str]
    DBClusterEndpointResourceIdentifier: NotRequired[str]
    Endpoint: NotRequired[str]
    Status: NotRequired[str]
    EndpointType: NotRequired[str]
    CustomEndpointType: NotRequired[str]
    StaticMembers: NotRequired[List[str]]
    ExcludedMembers: NotRequired[List[str]]
    DBClusterEndpointArn: NotRequired[str]

class DBClusterMemberTypeDef(TypedDict):
    DBInstanceIdentifier: NotRequired[str]
    IsClusterWriter: NotRequired[bool]
    DBClusterParameterGroupStatus: NotRequired[str]
    PromotionTier: NotRequired[int]

class DBClusterOptionGroupStatusTypeDef(TypedDict):
    DBClusterOptionGroupName: NotRequired[str]
    Status: NotRequired[str]

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
    FeatureName: NotRequired[str]

class DBClusterSnapshotAttributeTypeDef(TypedDict):
    AttributeName: NotRequired[str]
    AttributeValues: NotRequired[List[str]]

class ServerlessV2ScalingConfigurationInfoTypeDef(TypedDict):
    MinCapacity: NotRequired[float]
    MaxCapacity: NotRequired[float]

class VpcSecurityGroupMembershipTypeDef(TypedDict):
    VpcSecurityGroupId: NotRequired[str]
    Status: NotRequired[str]

class TimezoneTypeDef(TypedDict):
    TimezoneName: NotRequired[str]

class UpgradeTargetTypeDef(TypedDict):
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    Description: NotRequired[str]
    AutoUpgrade: NotRequired[bool]
    IsMajorVersionUpgrade: NotRequired[bool]
    SupportsGlobalDatabases: NotRequired[bool]

class DBInstanceStatusInfoTypeDef(TypedDict):
    StatusType: NotRequired[str]
    Normal: NotRequired[bool]
    Status: NotRequired[str]
    Message: NotRequired[str]

class DBParameterGroupStatusTypeDef(TypedDict):
    DBParameterGroupName: NotRequired[str]
    ParameterApplyStatus: NotRequired[str]

class DBSecurityGroupMembershipTypeDef(TypedDict):
    DBSecurityGroupName: NotRequired[str]
    Status: NotRequired[str]

class DomainMembershipTypeDef(TypedDict):
    Domain: NotRequired[str]
    Status: NotRequired[str]
    FQDN: NotRequired[str]
    IAMRoleName: NotRequired[str]

class EndpointTypeDef(TypedDict):
    Address: NotRequired[str]
    Port: NotRequired[int]
    HostedZoneId: NotRequired[str]

class OptionGroupMembershipTypeDef(TypedDict):
    OptionGroupName: NotRequired[str]
    Status: NotRequired[str]

class DeleteDBClusterEndpointMessageTypeDef(TypedDict):
    DBClusterEndpointIdentifier: str

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
    SkipFinalSnapshot: NotRequired[bool]
    FinalDBSnapshotIdentifier: NotRequired[str]

class DeleteDBParameterGroupMessageTypeDef(TypedDict):
    DBParameterGroupName: str

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

class DescribeGlobalClustersMessageTypeDef(TypedDict):
    GlobalClusterIdentifier: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeValidDBInstanceModificationsMessageTypeDef(TypedDict):
    DBInstanceIdentifier: str

class DoubleRangeTypeDef(TypedDict):
    From: NotRequired[float]
    To: NotRequired[float]

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

class GlobalClusterMemberTypeDef(TypedDict):
    DBClusterArn: NotRequired[str]
    Readers: NotRequired[List[str]]
    IsWriter: NotRequired[bool]

class ModifyDBClusterEndpointMessageTypeDef(TypedDict):
    DBClusterEndpointIdentifier: str
    EndpointType: NotRequired[str]
    StaticMembers: NotRequired[Sequence[str]]
    ExcludedMembers: NotRequired[Sequence[str]]

class ModifyDBClusterSnapshotAttributeMessageTypeDef(TypedDict):
    DBClusterSnapshotIdentifier: str
    AttributeName: str
    ValuesToAdd: NotRequired[Sequence[str]]
    ValuesToRemove: NotRequired[Sequence[str]]

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
    EngineVersion: NotRequired[str]
    AllowMajorVersionUpgrade: NotRequired[bool]

class PendingMaintenanceActionTypeDef(TypedDict):
    Action: NotRequired[str]
    AutoAppliedAfterDate: NotRequired[datetime]
    ForcedApplyDate: NotRequired[datetime]
    OptInStatus: NotRequired[str]
    CurrentApplyDate: NotRequired[datetime]
    Description: NotRequired[str]

class PromoteReadReplicaDBClusterMessageTypeDef(TypedDict):
    DBClusterIdentifier: str

class RangeTypeDef(TypedDict):
    From: NotRequired[int]
    To: NotRequired[int]
    Step: NotRequired[int]

class RebootDBInstanceMessageTypeDef(TypedDict):
    DBInstanceIdentifier: str
    ForceFailover: NotRequired[bool]

class RemoveFromGlobalClusterMessageTypeDef(TypedDict):
    GlobalClusterIdentifier: str
    DbClusterIdentifier: str

class RemoveRoleFromDBClusterMessageTypeDef(TypedDict):
    DBClusterIdentifier: str
    RoleArn: str
    FeatureName: NotRequired[str]

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

class AddSourceIdentifierToSubscriptionResultTypeDef(TypedDict):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBClusterEndpointOutputTypeDef(TypedDict):
    DBClusterEndpointIdentifier: str
    DBClusterIdentifier: str
    DBClusterEndpointResourceIdentifier: str
    Endpoint: str
    Status: str
    EndpointType: str
    CustomEndpointType: str
    StaticMembers: List[str]
    ExcludedMembers: List[str]
    DBClusterEndpointArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventSubscriptionResultTypeDef(TypedDict):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterParameterGroupNameMessageTypeDef(TypedDict):
    DBClusterParameterGroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DBParameterGroupNameMessageTypeDef(TypedDict):
    DBParameterGroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBClusterEndpointOutputTypeDef(TypedDict):
    DBClusterEndpointIdentifier: str
    DBClusterIdentifier: str
    DBClusterEndpointResourceIdentifier: str
    Endpoint: str
    Status: str
    EndpointType: str
    CustomEndpointType: str
    StaticMembers: List[str]
    ExcludedMembers: List[str]
    DBClusterEndpointArn: str
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

class ModifyDBClusterEndpointOutputTypeDef(TypedDict):
    DBClusterEndpointIdentifier: str
    DBClusterIdentifier: str
    DBClusterEndpointResourceIdentifier: str
    Endpoint: str
    Status: str
    EndpointType: str
    CustomEndpointType: str
    StaticMembers: List[str]
    ExcludedMembers: List[str]
    DBClusterEndpointArn: str
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

class CopyDBParameterGroupMessageTypeDef(TypedDict):
    SourceDBParameterGroupIdentifier: str
    TargetDBParameterGroupIdentifier: str
    TargetDBParameterGroupDescription: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateDBClusterEndpointMessageTypeDef(TypedDict):
    DBClusterIdentifier: str
    DBClusterEndpointIdentifier: str
    EndpointType: str
    StaticMembers: NotRequired[Sequence[str]]
    ExcludedMembers: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]

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
    DBName: NotRequired[str]
    AllocatedStorage: NotRequired[int]
    MasterUsername: NotRequired[str]
    MasterUserPassword: NotRequired[str]
    DBSecurityGroups: NotRequired[Sequence[str]]
    VpcSecurityGroupIds: NotRequired[Sequence[str]]
    AvailabilityZone: NotRequired[str]
    DBSubnetGroupName: NotRequired[str]
    PreferredMaintenanceWindow: NotRequired[str]
    DBParameterGroupName: NotRequired[str]
    BackupRetentionPeriod: NotRequired[int]
    PreferredBackupWindow: NotRequired[str]
    Port: NotRequired[int]
    MultiAZ: NotRequired[bool]
    EngineVersion: NotRequired[str]
    AutoMinorVersionUpgrade: NotRequired[bool]
    LicenseModel: NotRequired[str]
    Iops: NotRequired[int]
    OptionGroupName: NotRequired[str]
    CharacterSetName: NotRequired[str]
    PubliclyAccessible: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]
    StorageType: NotRequired[str]
    TdeCredentialArn: NotRequired[str]
    TdeCredentialPassword: NotRequired[str]
    StorageEncrypted: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    Domain: NotRequired[str]
    CopyTagsToSnapshot: NotRequired[bool]
    MonitoringInterval: NotRequired[int]
    MonitoringRoleArn: NotRequired[str]
    DomainIAMRoleName: NotRequired[str]
    PromotionTier: NotRequired[int]
    Timezone: NotRequired[str]
    EnableIAMDatabaseAuthentication: NotRequired[bool]
    EnablePerformanceInsights: NotRequired[bool]
    PerformanceInsightsKMSKeyId: NotRequired[str]
    EnableCloudwatchLogsExports: NotRequired[Sequence[str]]
    DeletionProtection: NotRequired[bool]

class CreateDBParameterGroupMessageTypeDef(TypedDict):
    DBParameterGroupName: str
    DBParameterGroupFamily: str
    Description: str
    Tags: NotRequired[Sequence[TagTypeDef]]

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

class TagListMessageTypeDef(TypedDict):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class OrderableDBInstanceOptionTypeDef(TypedDict):
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    DBInstanceClass: NotRequired[str]
    LicenseModel: NotRequired[str]
    AvailabilityZones: NotRequired[List[AvailabilityZoneTypeDef]]
    MultiAZCapable: NotRequired[bool]
    ReadReplicaCapable: NotRequired[bool]
    Vpc: NotRequired[bool]
    SupportsStorageEncryption: NotRequired[bool]
    StorageType: NotRequired[str]
    SupportsIops: NotRequired[bool]
    SupportsEnhancedMonitoring: NotRequired[bool]
    SupportsIAMDatabaseAuthentication: NotRequired[bool]
    SupportsPerformanceInsights: NotRequired[bool]
    MinStorageSize: NotRequired[int]
    MaxStorageSize: NotRequired[int]
    MinIopsPerDbInstance: NotRequired[int]
    MaxIopsPerDbInstance: NotRequired[int]
    MinIopsPerGib: NotRequired[float]
    MaxIopsPerGib: NotRequired[float]
    SupportsGlobalDatabases: NotRequired[bool]

class SubnetTypeDef(TypedDict):
    SubnetIdentifier: NotRequired[str]
    SubnetAvailabilityZone: NotRequired[AvailabilityZoneTypeDef]
    SubnetStatus: NotRequired[str]

class ModifyDBInstanceMessageTypeDef(TypedDict):
    DBInstanceIdentifier: str
    AllocatedStorage: NotRequired[int]
    DBInstanceClass: NotRequired[str]
    DBSubnetGroupName: NotRequired[str]
    DBSecurityGroups: NotRequired[Sequence[str]]
    VpcSecurityGroupIds: NotRequired[Sequence[str]]
    ApplyImmediately: NotRequired[bool]
    MasterUserPassword: NotRequired[str]
    DBParameterGroupName: NotRequired[str]
    BackupRetentionPeriod: NotRequired[int]
    PreferredBackupWindow: NotRequired[str]
    PreferredMaintenanceWindow: NotRequired[str]
    MultiAZ: NotRequired[bool]
    EngineVersion: NotRequired[str]
    AllowMajorVersionUpgrade: NotRequired[bool]
    AutoMinorVersionUpgrade: NotRequired[bool]
    LicenseModel: NotRequired[str]
    Iops: NotRequired[int]
    OptionGroupName: NotRequired[str]
    NewDBInstanceIdentifier: NotRequired[str]
    StorageType: NotRequired[str]
    TdeCredentialArn: NotRequired[str]
    TdeCredentialPassword: NotRequired[str]
    CACertificateIdentifier: NotRequired[str]
    Domain: NotRequired[str]
    CopyTagsToSnapshot: NotRequired[bool]
    MonitoringInterval: NotRequired[int]
    DBPortNumber: NotRequired[int]
    PubliclyAccessible: NotRequired[bool]
    MonitoringRoleArn: NotRequired[str]
    DomainIAMRoleName: NotRequired[str]
    PromotionTier: NotRequired[int]
    EnableIAMDatabaseAuthentication: NotRequired[bool]
    EnablePerformanceInsights: NotRequired[bool]
    PerformanceInsightsKMSKeyId: NotRequired[str]
    CloudwatchLogsExportConfiguration: NotRequired[CloudwatchLogsExportConfigurationTypeDef]
    DeletionProtection: NotRequired[bool]

class ClusterPendingModifiedValuesTypeDef(TypedDict):
    PendingCloudwatchLogsExports: NotRequired[PendingCloudwatchLogsExportsTypeDef]
    DBClusterIdentifier: NotRequired[str]
    IAMDatabaseAuthenticationEnabled: NotRequired[bool]
    EngineVersion: NotRequired[str]
    BackupRetentionPeriod: NotRequired[int]
    StorageType: NotRequired[str]
    AllocatedStorage: NotRequired[int]
    Iops: NotRequired[int]

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

class CopyDBParameterGroupResultTypeDef(TypedDict):
    DBParameterGroup: DBParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBParameterGroupResultTypeDef(TypedDict):
    DBParameterGroup: DBParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBParameterGroupsMessageTypeDef(TypedDict):
    Marker: str
    DBParameterGroups: List[DBParameterGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBClusterMessageTypeDef(TypedDict):
    DBClusterIdentifier: str
    Engine: str
    AvailabilityZones: NotRequired[Sequence[str]]
    BackupRetentionPeriod: NotRequired[int]
    CharacterSetName: NotRequired[str]
    CopyTagsToSnapshot: NotRequired[bool]
    DatabaseName: NotRequired[str]
    DBClusterParameterGroupName: NotRequired[str]
    VpcSecurityGroupIds: NotRequired[Sequence[str]]
    DBSubnetGroupName: NotRequired[str]
    EngineVersion: NotRequired[str]
    Port: NotRequired[int]
    MasterUsername: NotRequired[str]
    MasterUserPassword: NotRequired[str]
    OptionGroupName: NotRequired[str]
    PreferredBackupWindow: NotRequired[str]
    PreferredMaintenanceWindow: NotRequired[str]
    ReplicationSourceIdentifier: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    StorageEncrypted: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    PreSignedUrl: NotRequired[str]
    EnableIAMDatabaseAuthentication: NotRequired[bool]
    EnableCloudwatchLogsExports: NotRequired[Sequence[str]]
    DeletionProtection: NotRequired[bool]
    ServerlessV2ScalingConfiguration: NotRequired[ServerlessV2ScalingConfigurationTypeDef]
    GlobalClusterIdentifier: NotRequired[str]
    StorageType: NotRequired[str]
    SourceRegion: NotRequired[str]

class ModifyDBClusterMessageTypeDef(TypedDict):
    DBClusterIdentifier: str
    NewDBClusterIdentifier: NotRequired[str]
    ApplyImmediately: NotRequired[bool]
    BackupRetentionPeriod: NotRequired[int]
    DBClusterParameterGroupName: NotRequired[str]
    VpcSecurityGroupIds: NotRequired[Sequence[str]]
    Port: NotRequired[int]
    MasterUserPassword: NotRequired[str]
    OptionGroupName: NotRequired[str]
    PreferredBackupWindow: NotRequired[str]
    PreferredMaintenanceWindow: NotRequired[str]
    EnableIAMDatabaseAuthentication: NotRequired[bool]
    CloudwatchLogsExportConfiguration: NotRequired[CloudwatchLogsExportConfigurationTypeDef]
    EngineVersion: NotRequired[str]
    AllowMajorVersionUpgrade: NotRequired[bool]
    DBInstanceParameterGroupName: NotRequired[str]
    DeletionProtection: NotRequired[bool]
    CopyTagsToSnapshot: NotRequired[bool]
    ServerlessV2ScalingConfiguration: NotRequired[ServerlessV2ScalingConfigurationTypeDef]
    StorageType: NotRequired[str]

class RestoreDBClusterFromSnapshotMessageTypeDef(TypedDict):
    DBClusterIdentifier: str
    SnapshotIdentifier: str
    Engine: str
    AvailabilityZones: NotRequired[Sequence[str]]
    EngineVersion: NotRequired[str]
    Port: NotRequired[int]
    DBSubnetGroupName: NotRequired[str]
    DatabaseName: NotRequired[str]
    OptionGroupName: NotRequired[str]
    VpcSecurityGroupIds: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    KmsKeyId: NotRequired[str]
    EnableIAMDatabaseAuthentication: NotRequired[bool]
    EnableCloudwatchLogsExports: NotRequired[Sequence[str]]
    DBClusterParameterGroupName: NotRequired[str]
    DeletionProtection: NotRequired[bool]
    CopyTagsToSnapshot: NotRequired[bool]
    ServerlessV2ScalingConfiguration: NotRequired[ServerlessV2ScalingConfigurationTypeDef]
    StorageType: NotRequired[str]

class DBClusterEndpointMessageTypeDef(TypedDict):
    Marker: str
    DBClusterEndpoints: List[DBClusterEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterParameterGroupDetailsTypeDef(TypedDict):
    Parameters: List[ParameterTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DBParameterGroupDetailsTypeDef(TypedDict):
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

class ModifyDBParameterGroupMessageTypeDef(TypedDict):
    DBParameterGroupName: str
    Parameters: Sequence[ParameterTypeDef]

class ResetDBClusterParameterGroupMessageTypeDef(TypedDict):
    DBClusterParameterGroupName: str
    ResetAllParameters: NotRequired[bool]
    Parameters: NotRequired[Sequence[ParameterTypeDef]]

class ResetDBParameterGroupMessageTypeDef(TypedDict):
    DBParameterGroupName: str
    ResetAllParameters: NotRequired[bool]
    Parameters: NotRequired[Sequence[ParameterTypeDef]]

class DBClusterSnapshotAttributesResultTypeDef(TypedDict):
    DBClusterSnapshotIdentifier: NotRequired[str]
    DBClusterSnapshotAttributes: NotRequired[List[DBClusterSnapshotAttributeTypeDef]]

class DBEngineVersionTypeDef(TypedDict):
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    DBParameterGroupFamily: NotRequired[str]
    DBEngineDescription: NotRequired[str]
    DBEngineVersionDescription: NotRequired[str]
    DefaultCharacterSet: NotRequired[CharacterSetTypeDef]
    SupportedCharacterSets: NotRequired[List[CharacterSetTypeDef]]
    ValidUpgradeTarget: NotRequired[List[UpgradeTargetTypeDef]]
    SupportedTimezones: NotRequired[List[TimezoneTypeDef]]
    ExportableLogTypes: NotRequired[List[str]]
    SupportsLogExportsToCloudwatchLogs: NotRequired[bool]
    SupportsReadReplica: NotRequired[bool]
    SupportsGlobalDatabases: NotRequired[bool]

class DescribeDBClusterEndpointsMessageTypeDef(TypedDict):
    DBClusterIdentifier: NotRequired[str]
    DBClusterEndpointIdentifier: NotRequired[str]
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

class DescribeDBParameterGroupsMessageTypeDef(TypedDict):
    DBParameterGroupName: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeDBParametersMessageTypeDef(TypedDict):
    DBParameterGroupName: str
    Source: NotRequired[str]
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

class DescribeEngineDefaultParametersMessageTypeDef(TypedDict):
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

class DescribeDBClusterEndpointsMessagePaginateTypeDef(TypedDict):
    DBClusterIdentifier: NotRequired[str]
    DBClusterEndpointIdentifier: NotRequired[str]
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

class DescribeDBParameterGroupsMessagePaginateTypeDef(TypedDict):
    DBParameterGroupName: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDBParametersMessagePaginateTypeDef(TypedDict):
    DBParameterGroupName: str
    Source: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDBSubnetGroupsMessagePaginateTypeDef(TypedDict):
    DBSubnetGroupName: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEngineDefaultParametersMessagePaginateTypeDef(TypedDict):
    DBParameterGroupFamily: str
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEventSubscriptionsMessagePaginateTypeDef(TypedDict):
    SubscriptionName: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeGlobalClustersMessagePaginateTypeDef(TypedDict):
    GlobalClusterIdentifier: NotRequired[str]
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
    OptionGroupName: NotRequired[str]
    VpcSecurityGroupIds: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    KmsKeyId: NotRequired[str]
    EnableIAMDatabaseAuthentication: NotRequired[bool]
    EnableCloudwatchLogsExports: NotRequired[Sequence[str]]
    DBClusterParameterGroupName: NotRequired[str]
    DeletionProtection: NotRequired[bool]
    ServerlessV2ScalingConfiguration: NotRequired[ServerlessV2ScalingConfigurationTypeDef]
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
    StorageEncrypted: NotRequired[bool]
    DeletionProtection: NotRequired[bool]
    GlobalClusterMembers: NotRequired[List[GlobalClusterMemberTypeDef]]

class ResourcePendingMaintenanceActionsTypeDef(TypedDict):
    ResourceIdentifier: NotRequired[str]
    PendingMaintenanceActionDetails: NotRequired[List[PendingMaintenanceActionTypeDef]]

class ValidStorageOptionsTypeDef(TypedDict):
    StorageType: NotRequired[str]
    StorageSize: NotRequired[List[RangeTypeDef]]
    ProvisionedIops: NotRequired[List[RangeTypeDef]]
    IopsToStorageRatio: NotRequired[List[DoubleRangeTypeDef]]

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

class DBClusterTypeDef(TypedDict):
    AllocatedStorage: NotRequired[int]
    AvailabilityZones: NotRequired[List[str]]
    BackupRetentionPeriod: NotRequired[int]
    CharacterSetName: NotRequired[str]
    DatabaseName: NotRequired[str]
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
    DBClusterOptionGroupMemberships: NotRequired[List[DBClusterOptionGroupStatusTypeDef]]
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
    IAMDatabaseAuthenticationEnabled: NotRequired[bool]
    CloneGroupId: NotRequired[str]
    ClusterCreateTime: NotRequired[datetime]
    CopyTagsToSnapshot: NotRequired[bool]
    EnabledCloudwatchLogsExports: NotRequired[List[str]]
    PendingModifiedValues: NotRequired[ClusterPendingModifiedValuesTypeDef]
    DeletionProtection: NotRequired[bool]
    CrossAccountClone: NotRequired[bool]
    AutomaticRestartTime: NotRequired[datetime]
    ServerlessV2ScalingConfiguration: NotRequired[ServerlessV2ScalingConfigurationInfoTypeDef]
    GlobalClusterIdentifier: NotRequired[str]
    IOOptimizedNextAllowedModificationTime: NotRequired[datetime]
    StorageType: NotRequired[str]

class DescribeEngineDefaultClusterParametersResultTypeDef(TypedDict):
    EngineDefaults: EngineDefaultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEngineDefaultParametersResultTypeDef(TypedDict):
    EngineDefaults: EngineDefaultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDBClusterSnapshotAttributesResultTypeDef(TypedDict):
    DBClusterSnapshotAttributesResult: DBClusterSnapshotAttributesResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBClusterSnapshotAttributeResultTypeDef(TypedDict):
    DBClusterSnapshotAttributesResult: DBClusterSnapshotAttributesResultTypeDef
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

class ApplyPendingMaintenanceActionResultTypeDef(TypedDict):
    ResourcePendingMaintenanceActions: ResourcePendingMaintenanceActionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PendingMaintenanceActionsMessageTypeDef(TypedDict):
    PendingMaintenanceActions: List[ResourcePendingMaintenanceActionsTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ValidDBInstanceModificationsMessageTypeDef(TypedDict):
    Storage: NotRequired[List[ValidStorageOptionsTypeDef]]

class CreateDBSubnetGroupResultTypeDef(TypedDict):
    DBSubnetGroup: DBSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBInstanceTypeDef(TypedDict):
    DBInstanceIdentifier: NotRequired[str]
    DBInstanceClass: NotRequired[str]
    Engine: NotRequired[str]
    DBInstanceStatus: NotRequired[str]
    MasterUsername: NotRequired[str]
    DBName: NotRequired[str]
    Endpoint: NotRequired[EndpointTypeDef]
    AllocatedStorage: NotRequired[int]
    InstanceCreateTime: NotRequired[datetime]
    PreferredBackupWindow: NotRequired[str]
    BackupRetentionPeriod: NotRequired[int]
    DBSecurityGroups: NotRequired[List[DBSecurityGroupMembershipTypeDef]]
    VpcSecurityGroups: NotRequired[List[VpcSecurityGroupMembershipTypeDef]]
    DBParameterGroups: NotRequired[List[DBParameterGroupStatusTypeDef]]
    AvailabilityZone: NotRequired[str]
    DBSubnetGroup: NotRequired[DBSubnetGroupTypeDef]
    PreferredMaintenanceWindow: NotRequired[str]
    PendingModifiedValues: NotRequired[PendingModifiedValuesTypeDef]
    LatestRestorableTime: NotRequired[datetime]
    MultiAZ: NotRequired[bool]
    EngineVersion: NotRequired[str]
    AutoMinorVersionUpgrade: NotRequired[bool]
    ReadReplicaSourceDBInstanceIdentifier: NotRequired[str]
    ReadReplicaDBInstanceIdentifiers: NotRequired[List[str]]
    ReadReplicaDBClusterIdentifiers: NotRequired[List[str]]
    LicenseModel: NotRequired[str]
    Iops: NotRequired[int]
    OptionGroupMemberships: NotRequired[List[OptionGroupMembershipTypeDef]]
    CharacterSetName: NotRequired[str]
    SecondaryAvailabilityZone: NotRequired[str]
    PubliclyAccessible: NotRequired[bool]
    StatusInfos: NotRequired[List[DBInstanceStatusInfoTypeDef]]
    StorageType: NotRequired[str]
    TdeCredentialArn: NotRequired[str]
    DbInstancePort: NotRequired[int]
    DBClusterIdentifier: NotRequired[str]
    StorageEncrypted: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    DbiResourceId: NotRequired[str]
    CACertificateIdentifier: NotRequired[str]
    DomainMemberships: NotRequired[List[DomainMembershipTypeDef]]
    CopyTagsToSnapshot: NotRequired[bool]
    MonitoringInterval: NotRequired[int]
    EnhancedMonitoringResourceArn: NotRequired[str]
    MonitoringRoleArn: NotRequired[str]
    PromotionTier: NotRequired[int]
    DBInstanceArn: NotRequired[str]
    Timezone: NotRequired[str]
    IAMDatabaseAuthenticationEnabled: NotRequired[bool]
    PerformanceInsightsEnabled: NotRequired[bool]
    PerformanceInsightsKMSKeyId: NotRequired[str]
    EnabledCloudwatchLogsExports: NotRequired[List[str]]
    DeletionProtection: NotRequired[bool]

class DBSubnetGroupMessageTypeDef(TypedDict):
    Marker: str
    DBSubnetGroups: List[DBSubnetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBSubnetGroupResultTypeDef(TypedDict):
    DBSubnetGroup: DBSubnetGroupTypeDef
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

class PromoteReadReplicaDBClusterResultTypeDef(TypedDict):
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

class DescribeValidDBInstanceModificationsResultTypeDef(TypedDict):
    ValidDBInstanceModificationsMessage: ValidDBInstanceModificationsMessageTypeDef
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
