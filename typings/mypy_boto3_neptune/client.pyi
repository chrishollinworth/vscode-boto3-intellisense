# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for neptune service client

Usage::

    ```python
    import boto3
    from mypy_boto3_neptune import NeptuneClient

    client: NeptuneClient = boto3.client("neptune")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_neptune.paginator import (
    DescribeDBClusterParameterGroupsPaginator,
    DescribeDBClusterParametersPaginator,
    DescribeDBClusterSnapshotsPaginator,
    DescribeDBClustersPaginator,
    DescribeDBEngineVersionsPaginator,
    DescribeDBInstancesPaginator,
    DescribeDBParameterGroupsPaginator,
    DescribeDBParametersPaginator,
    DescribeDBSubnetGroupsPaginator,
    DescribeEngineDefaultParametersPaginator,
    DescribeEventsPaginator,
    DescribeEventSubscriptionsPaginator,
    DescribeOrderableDBInstanceOptionsPaginator,
    DescribePendingMaintenanceActionsPaginator,
)
from mypy_boto3_neptune.type_defs import (
    AddSourceIdentifierToSubscriptionResultTypeDef,
    ApplyPendingMaintenanceActionResultTypeDef,
    CloudwatchLogsExportConfigurationTypeDef,
    CopyDBClusterParameterGroupResultTypeDef,
    CopyDBClusterSnapshotResultTypeDef,
    CopyDBParameterGroupResultTypeDef,
    CreateDBClusterParameterGroupResultTypeDef,
    CreateDBClusterResultTypeDef,
    CreateDBClusterSnapshotResultTypeDef,
    CreateDBInstanceResultTypeDef,
    CreateDBParameterGroupResultTypeDef,
    CreateDBSubnetGroupResultTypeDef,
    CreateEventSubscriptionResultTypeDef,
    DBClusterMessageTypeDef,
    DBClusterParameterGroupDetailsTypeDef,
    DBClusterParameterGroupNameMessageTypeDef,
    DBClusterParameterGroupsMessageTypeDef,
    DBClusterSnapshotMessageTypeDef,
    DBEngineVersionMessageTypeDef,
    DBInstanceMessageTypeDef,
    DBParameterGroupDetailsTypeDef,
    DBParameterGroupNameMessageTypeDef,
    DBParameterGroupsMessageTypeDef,
    DBSubnetGroupMessageTypeDef,
    DeleteDBClusterResultTypeDef,
    DeleteDBClusterSnapshotResultTypeDef,
    DeleteDBInstanceResultTypeDef,
    DeleteEventSubscriptionResultTypeDef,
    DescribeDBClusterSnapshotAttributesResultTypeDef,
    DescribeEngineDefaultClusterParametersResultTypeDef,
    DescribeEngineDefaultParametersResultTypeDef,
    DescribeValidDBInstanceModificationsResultTypeDef,
    EventCategoriesMessageTypeDef,
    EventsMessageTypeDef,
    EventSubscriptionsMessageTypeDef,
    FailoverDBClusterResultTypeDef,
    FilterTypeDef,
    ModifyDBClusterResultTypeDef,
    ModifyDBClusterSnapshotAttributeResultTypeDef,
    ModifyDBInstanceResultTypeDef,
    ModifyDBSubnetGroupResultTypeDef,
    ModifyEventSubscriptionResultTypeDef,
    OrderableDBInstanceOptionsMessageTypeDef,
    ParameterTypeDef,
    PendingMaintenanceActionsMessageTypeDef,
    PromoteReadReplicaDBClusterResultTypeDef,
    RebootDBInstanceResultTypeDef,
    RemoveSourceIdentifierFromSubscriptionResultTypeDef,
    RestoreDBClusterFromSnapshotResultTypeDef,
    RestoreDBClusterToPointInTimeResultTypeDef,
    StartDBClusterResultTypeDef,
    StopDBClusterResultTypeDef,
    TagListMessageTypeDef,
    TagTypeDef,
)
from mypy_boto3_neptune.waiter import DBInstanceAvailableWaiter, DBInstanceDeletedWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("NeptuneClient",)


class Exceptions:
    AuthorizationNotFoundFault: Type[Boto3ClientError]
    CertificateNotFoundFault: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    DBClusterAlreadyExistsFault: Type[Boto3ClientError]
    DBClusterNotFoundFault: Type[Boto3ClientError]
    DBClusterParameterGroupNotFoundFault: Type[Boto3ClientError]
    DBClusterQuotaExceededFault: Type[Boto3ClientError]
    DBClusterRoleAlreadyExistsFault: Type[Boto3ClientError]
    DBClusterRoleNotFoundFault: Type[Boto3ClientError]
    DBClusterRoleQuotaExceededFault: Type[Boto3ClientError]
    DBClusterSnapshotAlreadyExistsFault: Type[Boto3ClientError]
    DBClusterSnapshotNotFoundFault: Type[Boto3ClientError]
    DBInstanceAlreadyExistsFault: Type[Boto3ClientError]
    DBInstanceNotFoundFault: Type[Boto3ClientError]
    DBParameterGroupAlreadyExistsFault: Type[Boto3ClientError]
    DBParameterGroupNotFoundFault: Type[Boto3ClientError]
    DBParameterGroupQuotaExceededFault: Type[Boto3ClientError]
    DBSecurityGroupNotFoundFault: Type[Boto3ClientError]
    DBSnapshotAlreadyExistsFault: Type[Boto3ClientError]
    DBSnapshotNotFoundFault: Type[Boto3ClientError]
    DBSubnetGroupAlreadyExistsFault: Type[Boto3ClientError]
    DBSubnetGroupDoesNotCoverEnoughAZs: Type[Boto3ClientError]
    DBSubnetGroupNotFoundFault: Type[Boto3ClientError]
    DBSubnetGroupQuotaExceededFault: Type[Boto3ClientError]
    DBSubnetQuotaExceededFault: Type[Boto3ClientError]
    DBUpgradeDependencyFailureFault: Type[Boto3ClientError]
    DomainNotFoundFault: Type[Boto3ClientError]
    EventSubscriptionQuotaExceededFault: Type[Boto3ClientError]
    InstanceQuotaExceededFault: Type[Boto3ClientError]
    InsufficientDBClusterCapacityFault: Type[Boto3ClientError]
    InsufficientDBInstanceCapacityFault: Type[Boto3ClientError]
    InsufficientStorageClusterCapacityFault: Type[Boto3ClientError]
    InvalidDBClusterSnapshotStateFault: Type[Boto3ClientError]
    InvalidDBClusterStateFault: Type[Boto3ClientError]
    InvalidDBInstanceStateFault: Type[Boto3ClientError]
    InvalidDBParameterGroupStateFault: Type[Boto3ClientError]
    InvalidDBSecurityGroupStateFault: Type[Boto3ClientError]
    InvalidDBSnapshotStateFault: Type[Boto3ClientError]
    InvalidDBSubnetGroupStateFault: Type[Boto3ClientError]
    InvalidDBSubnetStateFault: Type[Boto3ClientError]
    InvalidEventSubscriptionStateFault: Type[Boto3ClientError]
    InvalidRestoreFault: Type[Boto3ClientError]
    InvalidSubnet: Type[Boto3ClientError]
    InvalidVPCNetworkStateFault: Type[Boto3ClientError]
    KMSKeyNotAccessibleFault: Type[Boto3ClientError]
    OptionGroupNotFoundFault: Type[Boto3ClientError]
    ProvisionedIopsNotAvailableInAZFault: Type[Boto3ClientError]
    ResourceNotFoundFault: Type[Boto3ClientError]
    SNSInvalidTopicFault: Type[Boto3ClientError]
    SNSNoAuthorizationFault: Type[Boto3ClientError]
    SNSTopicArnNotFoundFault: Type[Boto3ClientError]
    SharedSnapshotQuotaExceededFault: Type[Boto3ClientError]
    SnapshotQuotaExceededFault: Type[Boto3ClientError]
    SourceNotFoundFault: Type[Boto3ClientError]
    StorageQuotaExceededFault: Type[Boto3ClientError]
    StorageTypeNotSupportedFault: Type[Boto3ClientError]
    SubnetAlreadyInUse: Type[Boto3ClientError]
    SubscriptionAlreadyExistFault: Type[Boto3ClientError]
    SubscriptionCategoryNotFoundFault: Type[Boto3ClientError]
    SubscriptionNotFoundFault: Type[Boto3ClientError]


class NeptuneClient:
    """
    [Neptune.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client)
    """

    exceptions: Exceptions

    def add_role_to_db_cluster(self, DBClusterIdentifier: str, RoleArn: str) -> None:
        """
        [Client.add_role_to_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.add_role_to_db_cluster)
        """

    def add_source_identifier_to_subscription(
        self, SubscriptionName: str, SourceIdentifier: str
    ) -> AddSourceIdentifierToSubscriptionResultTypeDef:
        """
        [Client.add_source_identifier_to_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.add_source_identifier_to_subscription)
        """

    def add_tags_to_resource(self, ResourceName: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.add_tags_to_resource)
        """

    def apply_pending_maintenance_action(
        self, ResourceIdentifier: str, ApplyAction: str, OptInType: str
    ) -> ApplyPendingMaintenanceActionResultTypeDef:
        """
        [Client.apply_pending_maintenance_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.apply_pending_maintenance_action)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.can_paginate)
        """

    def copy_db_cluster_parameter_group(
        self,
        SourceDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupDescription: str,
        Tags: List["TagTypeDef"] = None,
    ) -> CopyDBClusterParameterGroupResultTypeDef:
        """
        [Client.copy_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.copy_db_cluster_parameter_group)
        """

    def copy_db_cluster_snapshot(
        self,
        SourceDBClusterSnapshotIdentifier: str,
        TargetDBClusterSnapshotIdentifier: str,
        KmsKeyId: str = None,
        PreSignedUrl: str = None,
        CopyTags: bool = None,
        Tags: List["TagTypeDef"] = None,
        SourceRegion: str = None,
    ) -> CopyDBClusterSnapshotResultTypeDef:
        """
        [Client.copy_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.copy_db_cluster_snapshot)
        """

    def copy_db_parameter_group(
        self,
        SourceDBParameterGroupIdentifier: str,
        TargetDBParameterGroupIdentifier: str,
        TargetDBParameterGroupDescription: str,
        Tags: List["TagTypeDef"] = None,
    ) -> CopyDBParameterGroupResultTypeDef:
        """
        [Client.copy_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.copy_db_parameter_group)
        """

    def create_db_cluster(
        self,
        DBClusterIdentifier: str,
        Engine: str,
        AvailabilityZones: List[str] = None,
        BackupRetentionPeriod: int = None,
        CharacterSetName: str = None,
        DatabaseName: str = None,
        DBClusterParameterGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        DBSubnetGroupName: str = None,
        EngineVersion: str = None,
        Port: int = None,
        MasterUsername: str = None,
        MasterUserPassword: str = None,
        OptionGroupName: str = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        ReplicationSourceIdentifier: str = None,
        Tags: List["TagTypeDef"] = None,
        StorageEncrypted: bool = None,
        KmsKeyId: str = None,
        PreSignedUrl: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DeletionProtection: bool = None,
        SourceRegion: str = None,
    ) -> CreateDBClusterResultTypeDef:
        """
        [Client.create_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.create_db_cluster)
        """

    def create_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
        DBParameterGroupFamily: str,
        Description: str,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDBClusterParameterGroupResultTypeDef:
        """
        [Client.create_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.create_db_cluster_parameter_group)
        """

    def create_db_cluster_snapshot(
        self,
        DBClusterSnapshotIdentifier: str,
        DBClusterIdentifier: str,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDBClusterSnapshotResultTypeDef:
        """
        [Client.create_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.create_db_cluster_snapshot)
        """

    def create_db_instance(
        self,
        DBInstanceIdentifier: str,
        DBInstanceClass: str,
        Engine: str,
        DBName: str = None,
        AllocatedStorage: int = None,
        MasterUsername: str = None,
        MasterUserPassword: str = None,
        DBSecurityGroups: List[str] = None,
        VpcSecurityGroupIds: List[str] = None,
        AvailabilityZone: str = None,
        DBSubnetGroupName: str = None,
        PreferredMaintenanceWindow: str = None,
        DBParameterGroupName: str = None,
        BackupRetentionPeriod: int = None,
        PreferredBackupWindow: str = None,
        Port: int = None,
        MultiAZ: bool = None,
        EngineVersion: str = None,
        AutoMinorVersionUpgrade: bool = None,
        LicenseModel: str = None,
        Iops: int = None,
        OptionGroupName: str = None,
        CharacterSetName: str = None,
        PubliclyAccessible: bool = None,
        Tags: List["TagTypeDef"] = None,
        DBClusterIdentifier: str = None,
        StorageType: str = None,
        TdeCredentialArn: str = None,
        TdeCredentialPassword: str = None,
        StorageEncrypted: bool = None,
        KmsKeyId: str = None,
        Domain: str = None,
        CopyTagsToSnapshot: bool = None,
        MonitoringInterval: int = None,
        MonitoringRoleArn: str = None,
        DomainIAMRoleName: str = None,
        PromotionTier: int = None,
        Timezone: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnablePerformanceInsights: bool = None,
        PerformanceInsightsKMSKeyId: str = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DeletionProtection: bool = None,
    ) -> CreateDBInstanceResultTypeDef:
        """
        [Client.create_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.create_db_instance)
        """

    def create_db_parameter_group(
        self,
        DBParameterGroupName: str,
        DBParameterGroupFamily: str,
        Description: str,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDBParameterGroupResultTypeDef:
        """
        [Client.create_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.create_db_parameter_group)
        """

    def create_db_subnet_group(
        self,
        DBSubnetGroupName: str,
        DBSubnetGroupDescription: str,
        SubnetIds: List[str],
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDBSubnetGroupResultTypeDef:
        """
        [Client.create_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.create_db_subnet_group)
        """

    def create_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str,
        SourceType: str = None,
        EventCategories: List[str] = None,
        SourceIds: List[str] = None,
        Enabled: bool = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateEventSubscriptionResultTypeDef:
        """
        [Client.create_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.create_event_subscription)
        """

    def delete_db_cluster(
        self,
        DBClusterIdentifier: str,
        SkipFinalSnapshot: bool = None,
        FinalDBSnapshotIdentifier: str = None,
    ) -> DeleteDBClusterResultTypeDef:
        """
        [Client.delete_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.delete_db_cluster)
        """

    def delete_db_cluster_parameter_group(self, DBClusterParameterGroupName: str) -> None:
        """
        [Client.delete_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.delete_db_cluster_parameter_group)
        """

    def delete_db_cluster_snapshot(
        self, DBClusterSnapshotIdentifier: str
    ) -> DeleteDBClusterSnapshotResultTypeDef:
        """
        [Client.delete_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.delete_db_cluster_snapshot)
        """

    def delete_db_instance(
        self,
        DBInstanceIdentifier: str,
        SkipFinalSnapshot: bool = None,
        FinalDBSnapshotIdentifier: str = None,
    ) -> DeleteDBInstanceResultTypeDef:
        """
        [Client.delete_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.delete_db_instance)
        """

    def delete_db_parameter_group(self, DBParameterGroupName: str) -> None:
        """
        [Client.delete_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.delete_db_parameter_group)
        """

    def delete_db_subnet_group(self, DBSubnetGroupName: str) -> None:
        """
        [Client.delete_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.delete_db_subnet_group)
        """

    def delete_event_subscription(
        self, SubscriptionName: str
    ) -> DeleteEventSubscriptionResultTypeDef:
        """
        [Client.delete_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.delete_event_subscription)
        """

    def describe_db_cluster_parameter_groups(
        self,
        DBClusterParameterGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBClusterParameterGroupsMessageTypeDef:
        """
        [Client.describe_db_cluster_parameter_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.describe_db_cluster_parameter_groups)
        """

    def describe_db_cluster_parameters(
        self,
        DBClusterParameterGroupName: str,
        Source: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBClusterParameterGroupDetailsTypeDef:
        """
        [Client.describe_db_cluster_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.describe_db_cluster_parameters)
        """

    def describe_db_cluster_snapshot_attributes(
        self, DBClusterSnapshotIdentifier: str
    ) -> DescribeDBClusterSnapshotAttributesResultTypeDef:
        """
        [Client.describe_db_cluster_snapshot_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.describe_db_cluster_snapshot_attributes)
        """

    def describe_db_cluster_snapshots(
        self,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
    ) -> DBClusterSnapshotMessageTypeDef:
        """
        [Client.describe_db_cluster_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.describe_db_cluster_snapshots)
        """

    def describe_db_clusters(
        self,
        DBClusterIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBClusterMessageTypeDef:
        """
        [Client.describe_db_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.describe_db_clusters)
        """

    def describe_db_engine_versions(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        DBParameterGroupFamily: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        DefaultOnly: bool = None,
        ListSupportedCharacterSets: bool = None,
        ListSupportedTimezones: bool = None,
    ) -> DBEngineVersionMessageTypeDef:
        """
        [Client.describe_db_engine_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.describe_db_engine_versions)
        """

    def describe_db_instances(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBInstanceMessageTypeDef:
        """
        [Client.describe_db_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.describe_db_instances)
        """

    def describe_db_parameter_groups(
        self,
        DBParameterGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBParameterGroupsMessageTypeDef:
        """
        [Client.describe_db_parameter_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.describe_db_parameter_groups)
        """

    def describe_db_parameters(
        self,
        DBParameterGroupName: str,
        Source: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBParameterGroupDetailsTypeDef:
        """
        [Client.describe_db_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.describe_db_parameters)
        """

    def describe_db_subnet_groups(
        self,
        DBSubnetGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBSubnetGroupMessageTypeDef:
        """
        [Client.describe_db_subnet_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.describe_db_subnet_groups)
        """

    def describe_engine_default_cluster_parameters(
        self,
        DBParameterGroupFamily: str,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DescribeEngineDefaultClusterParametersResultTypeDef:
        """
        [Client.describe_engine_default_cluster_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.describe_engine_default_cluster_parameters)
        """

    def describe_engine_default_parameters(
        self,
        DBParameterGroupFamily: str,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DescribeEngineDefaultParametersResultTypeDef:
        """
        [Client.describe_engine_default_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.describe_engine_default_parameters)
        """

    def describe_event_categories(
        self, SourceType: str = None, Filters: List[FilterTypeDef] = None
    ) -> EventCategoriesMessageTypeDef:
        """
        [Client.describe_event_categories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.describe_event_categories)
        """

    def describe_event_subscriptions(
        self,
        SubscriptionName: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> EventSubscriptionsMessageTypeDef:
        """
        [Client.describe_event_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.describe_event_subscriptions)
        """

    def describe_events(
        self,
        SourceIdentifier: str = None,
        SourceType: Literal[
            "db-instance",
            "db-parameter-group",
            "db-security-group",
            "db-snapshot",
            "db-cluster",
            "db-cluster-snapshot",
        ] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> EventsMessageTypeDef:
        """
        [Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.describe_events)
        """

    def describe_orderable_db_instance_options(
        self,
        Engine: str,
        EngineVersion: str = None,
        DBInstanceClass: str = None,
        LicenseModel: str = None,
        Vpc: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> OrderableDBInstanceOptionsMessageTypeDef:
        """
        [Client.describe_orderable_db_instance_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.describe_orderable_db_instance_options)
        """

    def describe_pending_maintenance_actions(
        self,
        ResourceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> PendingMaintenanceActionsMessageTypeDef:
        """
        [Client.describe_pending_maintenance_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.describe_pending_maintenance_actions)
        """

    def describe_valid_db_instance_modifications(
        self, DBInstanceIdentifier: str
    ) -> DescribeValidDBInstanceModificationsResultTypeDef:
        """
        [Client.describe_valid_db_instance_modifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.describe_valid_db_instance_modifications)
        """

    def failover_db_cluster(
        self, DBClusterIdentifier: str = None, TargetDBInstanceIdentifier: str = None
    ) -> FailoverDBClusterResultTypeDef:
        """
        [Client.failover_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.failover_db_cluster)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.generate_presigned_url)
        """

    def list_tags_for_resource(
        self, ResourceName: str, Filters: List[FilterTypeDef] = None
    ) -> TagListMessageTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.list_tags_for_resource)
        """

    def modify_db_cluster(
        self,
        DBClusterIdentifier: str,
        NewDBClusterIdentifier: str = None,
        ApplyImmediately: bool = None,
        BackupRetentionPeriod: int = None,
        DBClusterParameterGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Port: int = None,
        MasterUserPassword: str = None,
        OptionGroupName: str = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        CloudwatchLogsExportConfiguration: CloudwatchLogsExportConfigurationTypeDef = None,
        EngineVersion: str = None,
        DeletionProtection: bool = None,
    ) -> ModifyDBClusterResultTypeDef:
        """
        [Client.modify_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.modify_db_cluster)
        """

    def modify_db_cluster_parameter_group(
        self, DBClusterParameterGroupName: str, Parameters: List["ParameterTypeDef"]
    ) -> DBClusterParameterGroupNameMessageTypeDef:
        """
        [Client.modify_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.modify_db_cluster_parameter_group)
        """

    def modify_db_cluster_snapshot_attribute(
        self,
        DBClusterSnapshotIdentifier: str,
        AttributeName: str,
        ValuesToAdd: List[str] = None,
        ValuesToRemove: List[str] = None,
    ) -> ModifyDBClusterSnapshotAttributeResultTypeDef:
        """
        [Client.modify_db_cluster_snapshot_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.modify_db_cluster_snapshot_attribute)
        """

    def modify_db_instance(
        self,
        DBInstanceIdentifier: str,
        AllocatedStorage: int = None,
        DBInstanceClass: str = None,
        DBSubnetGroupName: str = None,
        DBSecurityGroups: List[str] = None,
        VpcSecurityGroupIds: List[str] = None,
        ApplyImmediately: bool = None,
        MasterUserPassword: str = None,
        DBParameterGroupName: str = None,
        BackupRetentionPeriod: int = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        MultiAZ: bool = None,
        EngineVersion: str = None,
        AllowMajorVersionUpgrade: bool = None,
        AutoMinorVersionUpgrade: bool = None,
        LicenseModel: str = None,
        Iops: int = None,
        OptionGroupName: str = None,
        NewDBInstanceIdentifier: str = None,
        StorageType: str = None,
        TdeCredentialArn: str = None,
        TdeCredentialPassword: str = None,
        CACertificateIdentifier: str = None,
        Domain: str = None,
        CopyTagsToSnapshot: bool = None,
        MonitoringInterval: int = None,
        DBPortNumber: int = None,
        PubliclyAccessible: bool = None,
        MonitoringRoleArn: str = None,
        DomainIAMRoleName: str = None,
        PromotionTier: int = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnablePerformanceInsights: bool = None,
        PerformanceInsightsKMSKeyId: str = None,
        CloudwatchLogsExportConfiguration: CloudwatchLogsExportConfigurationTypeDef = None,
        DeletionProtection: bool = None,
    ) -> ModifyDBInstanceResultTypeDef:
        """
        [Client.modify_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.modify_db_instance)
        """

    def modify_db_parameter_group(
        self, DBParameterGroupName: str, Parameters: List["ParameterTypeDef"]
    ) -> DBParameterGroupNameMessageTypeDef:
        """
        [Client.modify_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.modify_db_parameter_group)
        """

    def modify_db_subnet_group(
        self, DBSubnetGroupName: str, SubnetIds: List[str], DBSubnetGroupDescription: str = None
    ) -> ModifyDBSubnetGroupResultTypeDef:
        """
        [Client.modify_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.modify_db_subnet_group)
        """

    def modify_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str = None,
        SourceType: str = None,
        EventCategories: List[str] = None,
        Enabled: bool = None,
    ) -> ModifyEventSubscriptionResultTypeDef:
        """
        [Client.modify_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.modify_event_subscription)
        """

    def promote_read_replica_db_cluster(
        self, DBClusterIdentifier: str
    ) -> PromoteReadReplicaDBClusterResultTypeDef:
        """
        [Client.promote_read_replica_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.promote_read_replica_db_cluster)
        """

    def reboot_db_instance(
        self, DBInstanceIdentifier: str, ForceFailover: bool = None
    ) -> RebootDBInstanceResultTypeDef:
        """
        [Client.reboot_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.reboot_db_instance)
        """

    def remove_role_from_db_cluster(self, DBClusterIdentifier: str, RoleArn: str) -> None:
        """
        [Client.remove_role_from_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.remove_role_from_db_cluster)
        """

    def remove_source_identifier_from_subscription(
        self, SubscriptionName: str, SourceIdentifier: str
    ) -> RemoveSourceIdentifierFromSubscriptionResultTypeDef:
        """
        [Client.remove_source_identifier_from_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.remove_source_identifier_from_subscription)
        """

    def remove_tags_from_resource(self, ResourceName: str, TagKeys: List[str]) -> None:
        """
        [Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.remove_tags_from_resource)
        """

    def reset_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
        ResetAllParameters: bool = None,
        Parameters: List["ParameterTypeDef"] = None,
    ) -> DBClusterParameterGroupNameMessageTypeDef:
        """
        [Client.reset_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.reset_db_cluster_parameter_group)
        """

    def reset_db_parameter_group(
        self,
        DBParameterGroupName: str,
        ResetAllParameters: bool = None,
        Parameters: List["ParameterTypeDef"] = None,
    ) -> DBParameterGroupNameMessageTypeDef:
        """
        [Client.reset_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.reset_db_parameter_group)
        """

    def restore_db_cluster_from_snapshot(
        self,
        DBClusterIdentifier: str,
        SnapshotIdentifier: str,
        Engine: str,
        AvailabilityZones: List[str] = None,
        EngineVersion: str = None,
        Port: int = None,
        DBSubnetGroupName: str = None,
        DatabaseName: str = None,
        OptionGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        KmsKeyId: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DBClusterParameterGroupName: str = None,
        DeletionProtection: bool = None,
    ) -> RestoreDBClusterFromSnapshotResultTypeDef:
        """
        [Client.restore_db_cluster_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.restore_db_cluster_from_snapshot)
        """

    def restore_db_cluster_to_point_in_time(
        self,
        DBClusterIdentifier: str,
        SourceDBClusterIdentifier: str,
        RestoreType: str = None,
        RestoreToTime: datetime = None,
        UseLatestRestorableTime: bool = None,
        Port: int = None,
        DBSubnetGroupName: str = None,
        OptionGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        KmsKeyId: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DBClusterParameterGroupName: str = None,
        DeletionProtection: bool = None,
    ) -> RestoreDBClusterToPointInTimeResultTypeDef:
        """
        [Client.restore_db_cluster_to_point_in_time documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.restore_db_cluster_to_point_in_time)
        """

    def start_db_cluster(self, DBClusterIdentifier: str) -> StartDBClusterResultTypeDef:
        """
        [Client.start_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.start_db_cluster)
        """

    def stop_db_cluster(self, DBClusterIdentifier: str) -> StopDBClusterResultTypeDef:
        """
        [Client.stop_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Client.stop_db_cluster)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_parameter_groups"]
    ) -> DescribeDBClusterParameterGroupsPaginator:
        """
        [Paginator.DescribeDBClusterParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterParameterGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_parameters"]
    ) -> DescribeDBClusterParametersPaginator:
        """
        [Paginator.DescribeDBClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterParameters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_snapshots"]
    ) -> DescribeDBClusterSnapshotsPaginator:
        """
        [Paginator.DescribeDBClusterSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterSnapshots)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_clusters"]
    ) -> DescribeDBClustersPaginator:
        """
        [Paginator.DescribeDBClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_engine_versions"]
    ) -> DescribeDBEngineVersionsPaginator:
        """
        [Paginator.DescribeDBEngineVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Paginator.DescribeDBEngineVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_instances"]
    ) -> DescribeDBInstancesPaginator:
        """
        [Paginator.DescribeDBInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Paginator.DescribeDBInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_parameter_groups"]
    ) -> DescribeDBParameterGroupsPaginator:
        """
        [Paginator.DescribeDBParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Paginator.DescribeDBParameterGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_parameters"]
    ) -> DescribeDBParametersPaginator:
        """
        [Paginator.DescribeDBParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Paginator.DescribeDBParameters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_subnet_groups"]
    ) -> DescribeDBSubnetGroupsPaginator:
        """
        [Paginator.DescribeDBSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Paginator.DescribeDBSubnetGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_engine_default_parameters"]
    ) -> DescribeEngineDefaultParametersPaginator:
        """
        [Paginator.DescribeEngineDefaultParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Paginator.DescribeEngineDefaultParameters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_event_subscriptions"]
    ) -> DescribeEventSubscriptionsPaginator:
        """
        [Paginator.DescribeEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Paginator.DescribeEventSubscriptions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_events"]) -> DescribeEventsPaginator:
        """
        [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Paginator.DescribeEvents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_orderable_db_instance_options"]
    ) -> DescribeOrderableDBInstanceOptionsPaginator:
        """
        [Paginator.DescribeOrderableDBInstanceOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Paginator.DescribeOrderableDBInstanceOptions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_pending_maintenance_actions"]
    ) -> DescribePendingMaintenanceActionsPaginator:
        """
        [Paginator.DescribePendingMaintenanceActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Paginator.DescribePendingMaintenanceActions)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass

    @overload
    def get_waiter(
        self, waiter_name: Literal["db_instance_available"]
    ) -> DBInstanceAvailableWaiter:
        """
        [Waiter.DBInstanceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Waiter.DBInstanceAvailable)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["db_instance_deleted"]) -> DBInstanceDeletedWaiter:
        """
        [Waiter.DBInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/neptune.html#Neptune.Waiter.DBInstanceDeleted)
        """

    def get_waiter(self, waiter_name: str) -> Boto3Waiter:
        pass
