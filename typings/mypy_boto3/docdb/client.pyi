"""
Type annotations for docdb service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_docdb import DocDBClient

    client: DocDBClient = boto3.client("docdb")
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import SourceTypeType
from .paginator import (
    DescribeCertificatesPaginator,
    DescribeDBClusterParameterGroupsPaginator,
    DescribeDBClusterParametersPaginator,
    DescribeDBClusterSnapshotsPaginator,
    DescribeDBClustersPaginator,
    DescribeDBEngineVersionsPaginator,
    DescribeDBInstancesPaginator,
    DescribeDBSubnetGroupsPaginator,
    DescribeEventsPaginator,
    DescribeEventSubscriptionsPaginator,
    DescribeGlobalClustersPaginator,
    DescribeOrderableDBInstanceOptionsPaginator,
    DescribePendingMaintenanceActionsPaginator,
)
from .type_defs import (
    AddSourceIdentifierToSubscriptionResultTypeDef,
    ApplyPendingMaintenanceActionResultTypeDef,
    CertificateMessageTypeDef,
    CloudwatchLogsExportConfigurationTypeDef,
    CopyDBClusterParameterGroupResultTypeDef,
    CopyDBClusterSnapshotResultTypeDef,
    CreateDBClusterParameterGroupResultTypeDef,
    CreateDBClusterResultTypeDef,
    CreateDBClusterSnapshotResultTypeDef,
    CreateDBInstanceResultTypeDef,
    CreateDBSubnetGroupResultTypeDef,
    CreateEventSubscriptionResultTypeDef,
    CreateGlobalClusterResultTypeDef,
    DBClusterMessageTypeDef,
    DBClusterParameterGroupDetailsTypeDef,
    DBClusterParameterGroupNameMessageTypeDef,
    DBClusterParameterGroupsMessageTypeDef,
    DBClusterSnapshotMessageTypeDef,
    DBEngineVersionMessageTypeDef,
    DBInstanceMessageTypeDef,
    DBSubnetGroupMessageTypeDef,
    DeleteDBClusterResultTypeDef,
    DeleteDBClusterSnapshotResultTypeDef,
    DeleteDBInstanceResultTypeDef,
    DeleteEventSubscriptionResultTypeDef,
    DeleteGlobalClusterResultTypeDef,
    DescribeDBClusterSnapshotAttributesResultTypeDef,
    DescribeEngineDefaultClusterParametersResultTypeDef,
    EventCategoriesMessageTypeDef,
    EventsMessageTypeDef,
    EventSubscriptionsMessageTypeDef,
    FailoverDBClusterResultTypeDef,
    FilterTypeDef,
    GlobalClustersMessageTypeDef,
    ModifyDBClusterResultTypeDef,
    ModifyDBClusterSnapshotAttributeResultTypeDef,
    ModifyDBInstanceResultTypeDef,
    ModifyDBSubnetGroupResultTypeDef,
    ModifyEventSubscriptionResultTypeDef,
    ModifyGlobalClusterResultTypeDef,
    OrderableDBInstanceOptionsMessageTypeDef,
    ParameterTypeDef,
    PendingMaintenanceActionsMessageTypeDef,
    RebootDBInstanceResultTypeDef,
    RemoveFromGlobalClusterResultTypeDef,
    RemoveSourceIdentifierFromSubscriptionResultTypeDef,
    RestoreDBClusterFromSnapshotResultTypeDef,
    RestoreDBClusterToPointInTimeResultTypeDef,
    StartDBClusterResultTypeDef,
    StopDBClusterResultTypeDef,
    SwitchoverGlobalClusterResultTypeDef,
    TagListMessageTypeDef,
    TagTypeDef,
)
from .waiter import DBInstanceAvailableWaiter, DBInstanceDeletedWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("DocDBClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AuthorizationNotFoundFault: Type[BotocoreClientError]
    CertificateNotFoundFault: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DBClusterAlreadyExistsFault: Type[BotocoreClientError]
    DBClusterNotFoundFault: Type[BotocoreClientError]
    DBClusterParameterGroupNotFoundFault: Type[BotocoreClientError]
    DBClusterQuotaExceededFault: Type[BotocoreClientError]
    DBClusterSnapshotAlreadyExistsFault: Type[BotocoreClientError]
    DBClusterSnapshotNotFoundFault: Type[BotocoreClientError]
    DBInstanceAlreadyExistsFault: Type[BotocoreClientError]
    DBInstanceNotFoundFault: Type[BotocoreClientError]
    DBParameterGroupAlreadyExistsFault: Type[BotocoreClientError]
    DBParameterGroupNotFoundFault: Type[BotocoreClientError]
    DBParameterGroupQuotaExceededFault: Type[BotocoreClientError]
    DBSecurityGroupNotFoundFault: Type[BotocoreClientError]
    DBSnapshotAlreadyExistsFault: Type[BotocoreClientError]
    DBSnapshotNotFoundFault: Type[BotocoreClientError]
    DBSubnetGroupAlreadyExistsFault: Type[BotocoreClientError]
    DBSubnetGroupDoesNotCoverEnoughAZs: Type[BotocoreClientError]
    DBSubnetGroupNotFoundFault: Type[BotocoreClientError]
    DBSubnetGroupQuotaExceededFault: Type[BotocoreClientError]
    DBSubnetQuotaExceededFault: Type[BotocoreClientError]
    DBUpgradeDependencyFailureFault: Type[BotocoreClientError]
    EventSubscriptionQuotaExceededFault: Type[BotocoreClientError]
    GlobalClusterAlreadyExistsFault: Type[BotocoreClientError]
    GlobalClusterNotFoundFault: Type[BotocoreClientError]
    GlobalClusterQuotaExceededFault: Type[BotocoreClientError]
    InstanceQuotaExceededFault: Type[BotocoreClientError]
    InsufficientDBClusterCapacityFault: Type[BotocoreClientError]
    InsufficientDBInstanceCapacityFault: Type[BotocoreClientError]
    InsufficientStorageClusterCapacityFault: Type[BotocoreClientError]
    InvalidDBClusterSnapshotStateFault: Type[BotocoreClientError]
    InvalidDBClusterStateFault: Type[BotocoreClientError]
    InvalidDBInstanceStateFault: Type[BotocoreClientError]
    InvalidDBParameterGroupStateFault: Type[BotocoreClientError]
    InvalidDBSecurityGroupStateFault: Type[BotocoreClientError]
    InvalidDBSnapshotStateFault: Type[BotocoreClientError]
    InvalidDBSubnetGroupStateFault: Type[BotocoreClientError]
    InvalidDBSubnetStateFault: Type[BotocoreClientError]
    InvalidEventSubscriptionStateFault: Type[BotocoreClientError]
    InvalidGlobalClusterStateFault: Type[BotocoreClientError]
    InvalidRestoreFault: Type[BotocoreClientError]
    InvalidSubnet: Type[BotocoreClientError]
    InvalidVPCNetworkStateFault: Type[BotocoreClientError]
    KMSKeyNotAccessibleFault: Type[BotocoreClientError]
    ResourceNotFoundFault: Type[BotocoreClientError]
    SNSInvalidTopicFault: Type[BotocoreClientError]
    SNSNoAuthorizationFault: Type[BotocoreClientError]
    SNSTopicArnNotFoundFault: Type[BotocoreClientError]
    SharedSnapshotQuotaExceededFault: Type[BotocoreClientError]
    SnapshotQuotaExceededFault: Type[BotocoreClientError]
    SourceNotFoundFault: Type[BotocoreClientError]
    StorageQuotaExceededFault: Type[BotocoreClientError]
    StorageTypeNotSupportedFault: Type[BotocoreClientError]
    SubnetAlreadyInUse: Type[BotocoreClientError]
    SubscriptionAlreadyExistFault: Type[BotocoreClientError]
    SubscriptionCategoryNotFoundFault: Type[BotocoreClientError]
    SubscriptionNotFoundFault: Type[BotocoreClientError]

class DocDBClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DocDBClient exceptions.
        """

    def add_source_identifier_to_subscription(
        self, *, SubscriptionName: str, SourceIdentifier: str
    ) -> AddSourceIdentifierToSubscriptionResultTypeDef:
        """
        Adds a source identifier to an existing event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.add_source_identifier_to_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#add_source_identifier_to_subscription)
        """

    def add_tags_to_resource(self, *, ResourceName: str, Tags: List["TagTypeDef"]) -> None:
        """
        Adds metadata tags to an Amazon DocumentDB resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.add_tags_to_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#add_tags_to_resource)
        """

    def apply_pending_maintenance_action(
        self, *, ResourceIdentifier: str, ApplyAction: str, OptInType: str
    ) -> ApplyPendingMaintenanceActionResultTypeDef:
        """
        Applies a pending maintenance action to a resource (for example, to an Amazon
        DocumentDB instance).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.apply_pending_maintenance_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#apply_pending_maintenance_action)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#close)
        """

    def copy_db_cluster_parameter_group(
        self,
        *,
        SourceDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupDescription: str,
        Tags: List["TagTypeDef"] = None
    ) -> CopyDBClusterParameterGroupResultTypeDef:
        """
        Copies the specified cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.copy_db_cluster_parameter_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#copy_db_cluster_parameter_group)
        """

    def copy_db_cluster_snapshot(
        self,
        *,
        SourceDBClusterSnapshotIdentifier: str,
        TargetDBClusterSnapshotIdentifier: str,
        KmsKeyId: str = None,
        PreSignedUrl: str = None,
        CopyTags: bool = None,
        Tags: List["TagTypeDef"] = None,
        SourceRegion: str = None
    ) -> CopyDBClusterSnapshotResultTypeDef:
        """
        Copies a snapshot of a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.copy_db_cluster_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#copy_db_cluster_snapshot)
        """

    def create_db_cluster(
        self,
        *,
        DBClusterIdentifier: str,
        Engine: str,
        AvailabilityZones: List[str] = None,
        BackupRetentionPeriod: int = None,
        DBClusterParameterGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        DBSubnetGroupName: str = None,
        EngineVersion: str = None,
        Port: int = None,
        MasterUsername: str = None,
        MasterUserPassword: str = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        Tags: List["TagTypeDef"] = None,
        StorageEncrypted: bool = None,
        KmsKeyId: str = None,
        PreSignedUrl: str = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DeletionProtection: bool = None,
        GlobalClusterIdentifier: str = None,
        StorageType: str = None,
        SourceRegion: str = None
    ) -> CreateDBClusterResultTypeDef:
        """
        Creates a new Amazon DocumentDB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.create_db_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#create_db_cluster)
        """

    def create_db_cluster_parameter_group(
        self,
        *,
        DBClusterParameterGroupName: str,
        DBParameterGroupFamily: str,
        Description: str,
        Tags: List["TagTypeDef"] = None
    ) -> CreateDBClusterParameterGroupResultTypeDef:
        """
        Creates a new cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.create_db_cluster_parameter_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#create_db_cluster_parameter_group)
        """

    def create_db_cluster_snapshot(
        self,
        *,
        DBClusterSnapshotIdentifier: str,
        DBClusterIdentifier: str,
        Tags: List["TagTypeDef"] = None
    ) -> CreateDBClusterSnapshotResultTypeDef:
        """
        Creates a snapshot of a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.create_db_cluster_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#create_db_cluster_snapshot)
        """

    def create_db_instance(
        self,
        *,
        DBInstanceIdentifier: str,
        DBInstanceClass: str,
        Engine: str,
        DBClusterIdentifier: str,
        AvailabilityZone: str = None,
        PreferredMaintenanceWindow: str = None,
        AutoMinorVersionUpgrade: bool = None,
        Tags: List["TagTypeDef"] = None,
        CopyTagsToSnapshot: bool = None,
        PromotionTier: int = None,
        EnablePerformanceInsights: bool = None,
        PerformanceInsightsKMSKeyId: str = None,
        CACertificateIdentifier: str = None
    ) -> CreateDBInstanceResultTypeDef:
        """
        Creates a new instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.create_db_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#create_db_instance)
        """

    def create_db_subnet_group(
        self,
        *,
        DBSubnetGroupName: str,
        DBSubnetGroupDescription: str,
        SubnetIds: List[str],
        Tags: List["TagTypeDef"] = None
    ) -> CreateDBSubnetGroupResultTypeDef:
        """
        Creates a new subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.create_db_subnet_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#create_db_subnet_group)
        """

    def create_event_subscription(
        self,
        *,
        SubscriptionName: str,
        SnsTopicArn: str,
        SourceType: str = None,
        EventCategories: List[str] = None,
        SourceIds: List[str] = None,
        Enabled: bool = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateEventSubscriptionResultTypeDef:
        """
        Creates an Amazon DocumentDB event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.create_event_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#create_event_subscription)
        """

    def create_global_cluster(
        self,
        *,
        GlobalClusterIdentifier: str,
        SourceDBClusterIdentifier: str = None,
        Engine: str = None,
        EngineVersion: str = None,
        DeletionProtection: bool = None,
        DatabaseName: str = None,
        StorageEncrypted: bool = None
    ) -> CreateGlobalClusterResultTypeDef:
        """
        Creates an Amazon DocumentDB global cluster that can span multiple multiple
        Amazon Web Services Regions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.create_global_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#create_global_cluster)
        """

    def delete_db_cluster(
        self,
        *,
        DBClusterIdentifier: str,
        SkipFinalSnapshot: bool = None,
        FinalDBSnapshotIdentifier: str = None
    ) -> DeleteDBClusterResultTypeDef:
        """
        Deletes a previously provisioned cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.delete_db_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#delete_db_cluster)
        """

    def delete_db_cluster_parameter_group(self, *, DBClusterParameterGroupName: str) -> None:
        """
        Deletes a specified cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.delete_db_cluster_parameter_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#delete_db_cluster_parameter_group)
        """

    def delete_db_cluster_snapshot(
        self, *, DBClusterSnapshotIdentifier: str
    ) -> DeleteDBClusterSnapshotResultTypeDef:
        """
        Deletes a cluster snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.delete_db_cluster_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#delete_db_cluster_snapshot)
        """

    def delete_db_instance(self, *, DBInstanceIdentifier: str) -> DeleteDBInstanceResultTypeDef:
        """
        Deletes a previously provisioned instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.delete_db_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#delete_db_instance)
        """

    def delete_db_subnet_group(self, *, DBSubnetGroupName: str) -> None:
        """
        Deletes a subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.delete_db_subnet_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#delete_db_subnet_group)
        """

    def delete_event_subscription(
        self, *, SubscriptionName: str
    ) -> DeleteEventSubscriptionResultTypeDef:
        """
        Deletes an Amazon DocumentDB event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.delete_event_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#delete_event_subscription)
        """

    def delete_global_cluster(
        self, *, GlobalClusterIdentifier: str
    ) -> DeleteGlobalClusterResultTypeDef:
        """
        Deletes a global cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.delete_global_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#delete_global_cluster)
        """

    def describe_certificates(
        self,
        *,
        CertificateIdentifier: str = None,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> CertificateMessageTypeDef:
        """
        Returns a list of certificate authority (CA) certificates provided by Amazon
        DocumentDB for this Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.describe_certificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#describe_certificates)
        """

    def describe_db_cluster_parameter_groups(
        self,
        *,
        DBClusterParameterGroupName: str = None,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> DBClusterParameterGroupsMessageTypeDef:
        """
        Returns a list of `DBClusterParameterGroup` descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.describe_db_cluster_parameter_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#describe_db_cluster_parameter_groups)
        """

    def describe_db_cluster_parameters(
        self,
        *,
        DBClusterParameterGroupName: str,
        Source: str = None,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> DBClusterParameterGroupDetailsTypeDef:
        """
        Returns the detailed parameter list for a particular cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.describe_db_cluster_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#describe_db_cluster_parameters)
        """

    def describe_db_cluster_snapshot_attributes(
        self, *, DBClusterSnapshotIdentifier: str
    ) -> DescribeDBClusterSnapshotAttributesResultTypeDef:
        """
        Returns a list of cluster snapshot attribute names and values for a manual DB
        cluster snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.describe_db_cluster_snapshot_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#describe_db_cluster_snapshot_attributes)
        """

    def describe_db_cluster_snapshots(
        self,
        *,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None
    ) -> DBClusterSnapshotMessageTypeDef:
        """
        Returns information about cluster snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.describe_db_cluster_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#describe_db_cluster_snapshots)
        """

    def describe_db_clusters(
        self,
        *,
        DBClusterIdentifier: str = None,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> DBClusterMessageTypeDef:
        """
        Returns information about provisioned Amazon DocumentDB clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.describe_db_clusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#describe_db_clusters)
        """

    def describe_db_engine_versions(
        self,
        *,
        Engine: str = None,
        EngineVersion: str = None,
        DBParameterGroupFamily: str = None,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        Marker: str = None,
        DefaultOnly: bool = None,
        ListSupportedCharacterSets: bool = None,
        ListSupportedTimezones: bool = None
    ) -> DBEngineVersionMessageTypeDef:
        """
        Returns a list of the available engines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.describe_db_engine_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#describe_db_engine_versions)
        """

    def describe_db_instances(
        self,
        *,
        DBInstanceIdentifier: str = None,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> DBInstanceMessageTypeDef:
        """
        Returns information about provisioned Amazon DocumentDB instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.describe_db_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#describe_db_instances)
        """

    def describe_db_subnet_groups(
        self,
        *,
        DBSubnetGroupName: str = None,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> DBSubnetGroupMessageTypeDef:
        """
        Returns a list of `DBSubnetGroup` descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.describe_db_subnet_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#describe_db_subnet_groups)
        """

    def describe_engine_default_cluster_parameters(
        self,
        *,
        DBParameterGroupFamily: str,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> DescribeEngineDefaultClusterParametersResultTypeDef:
        """
        Returns the default engine and system parameter information for the cluster
        database engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.describe_engine_default_cluster_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#describe_engine_default_cluster_parameters)
        """

    def describe_event_categories(
        self, *, SourceType: str = None, Filters: List["FilterTypeDef"] = None
    ) -> EventCategoriesMessageTypeDef:
        """
        Displays a list of categories for all event source types, or, if specified, for
        a specified source type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.describe_event_categories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#describe_event_categories)
        """

    def describe_event_subscriptions(
        self,
        *,
        SubscriptionName: str = None,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> EventSubscriptionsMessageTypeDef:
        """
        Lists all the subscription descriptions for a customer account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.describe_event_subscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#describe_event_subscriptions)
        """

    def describe_events(
        self,
        *,
        SourceIdentifier: str = None,
        SourceType: SourceTypeType = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> EventsMessageTypeDef:
        """
        Returns events related to instances, security groups, snapshots, and DB
        parameter groups for the past 14 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.describe_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#describe_events)
        """

    def describe_global_clusters(
        self,
        *,
        GlobalClusterIdentifier: str = None,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> GlobalClustersMessageTypeDef:
        """
        Returns information about Amazon DocumentDB global clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.describe_global_clusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#describe_global_clusters)
        """

    def describe_orderable_db_instance_options(
        self,
        *,
        Engine: str,
        EngineVersion: str = None,
        DBInstanceClass: str = None,
        LicenseModel: str = None,
        Vpc: bool = None,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> OrderableDBInstanceOptionsMessageTypeDef:
        """
        Returns a list of orderable instance options for the specified engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.describe_orderable_db_instance_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#describe_orderable_db_instance_options)
        """

    def describe_pending_maintenance_actions(
        self,
        *,
        ResourceIdentifier: str = None,
        Filters: List["FilterTypeDef"] = None,
        Marker: str = None,
        MaxRecords: int = None
    ) -> PendingMaintenanceActionsMessageTypeDef:
        """
        Returns a list of resources (for example, instances) that have at least one
        pending maintenance action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.describe_pending_maintenance_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#describe_pending_maintenance_actions)
        """

    def failover_db_cluster(
        self, *, DBClusterIdentifier: str = None, TargetDBInstanceIdentifier: str = None
    ) -> FailoverDBClusterResultTypeDef:
        """
        Forces a failover for a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.failover_db_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#failover_db_cluster)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#generate_presigned_url)
        """

    def list_tags_for_resource(
        self, *, ResourceName: str, Filters: List["FilterTypeDef"] = None
    ) -> TagListMessageTypeDef:
        """
        Lists all tags on an Amazon DocumentDB resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#list_tags_for_resource)
        """

    def modify_db_cluster(
        self,
        *,
        DBClusterIdentifier: str,
        NewDBClusterIdentifier: str = None,
        ApplyImmediately: bool = None,
        BackupRetentionPeriod: int = None,
        DBClusterParameterGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Port: int = None,
        MasterUserPassword: str = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        CloudwatchLogsExportConfiguration: "CloudwatchLogsExportConfigurationTypeDef" = None,
        EngineVersion: str = None,
        AllowMajorVersionUpgrade: bool = None,
        DeletionProtection: bool = None,
        StorageType: str = None
    ) -> ModifyDBClusterResultTypeDef:
        """
        Modifies a setting for an Amazon DocumentDB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.modify_db_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#modify_db_cluster)
        """

    def modify_db_cluster_parameter_group(
        self, *, DBClusterParameterGroupName: str, Parameters: List["ParameterTypeDef"]
    ) -> DBClusterParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.modify_db_cluster_parameter_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#modify_db_cluster_parameter_group)
        """

    def modify_db_cluster_snapshot_attribute(
        self,
        *,
        DBClusterSnapshotIdentifier: str,
        AttributeName: str,
        ValuesToAdd: List[str] = None,
        ValuesToRemove: List[str] = None
    ) -> ModifyDBClusterSnapshotAttributeResultTypeDef:
        """
        Adds an attribute and values to, or removes an attribute and values from, a
        manual cluster snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.modify_db_cluster_snapshot_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#modify_db_cluster_snapshot_attribute)
        """

    def modify_db_instance(
        self,
        *,
        DBInstanceIdentifier: str,
        DBInstanceClass: str = None,
        ApplyImmediately: bool = None,
        PreferredMaintenanceWindow: str = None,
        AutoMinorVersionUpgrade: bool = None,
        NewDBInstanceIdentifier: str = None,
        CACertificateIdentifier: str = None,
        CopyTagsToSnapshot: bool = None,
        PromotionTier: int = None,
        EnablePerformanceInsights: bool = None,
        PerformanceInsightsKMSKeyId: str = None,
        CertificateRotationRestart: bool = None
    ) -> ModifyDBInstanceResultTypeDef:
        """
        Modifies settings for an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.modify_db_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#modify_db_instance)
        """

    def modify_db_subnet_group(
        self, *, DBSubnetGroupName: str, SubnetIds: List[str], DBSubnetGroupDescription: str = None
    ) -> ModifyDBSubnetGroupResultTypeDef:
        """
        Modifies an existing subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.modify_db_subnet_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#modify_db_subnet_group)
        """

    def modify_event_subscription(
        self,
        *,
        SubscriptionName: str,
        SnsTopicArn: str = None,
        SourceType: str = None,
        EventCategories: List[str] = None,
        Enabled: bool = None
    ) -> ModifyEventSubscriptionResultTypeDef:
        """
        Modifies an existing Amazon DocumentDB event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.modify_event_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#modify_event_subscription)
        """

    def modify_global_cluster(
        self,
        *,
        GlobalClusterIdentifier: str,
        NewGlobalClusterIdentifier: str = None,
        DeletionProtection: bool = None
    ) -> ModifyGlobalClusterResultTypeDef:
        """
        Modify a setting for an Amazon DocumentDB global cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.modify_global_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#modify_global_cluster)
        """

    def reboot_db_instance(
        self, *, DBInstanceIdentifier: str, ForceFailover: bool = None
    ) -> RebootDBInstanceResultTypeDef:
        """
        You might need to reboot your instance, usually for maintenance reasons.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.reboot_db_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#reboot_db_instance)
        """

    def remove_from_global_cluster(
        self, *, GlobalClusterIdentifier: str, DbClusterIdentifier: str
    ) -> RemoveFromGlobalClusterResultTypeDef:
        """
        Detaches an Amazon DocumentDB secondary cluster from a global cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.remove_from_global_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#remove_from_global_cluster)
        """

    def remove_source_identifier_from_subscription(
        self, *, SubscriptionName: str, SourceIdentifier: str
    ) -> RemoveSourceIdentifierFromSubscriptionResultTypeDef:
        """
        Removes a source identifier from an existing Amazon DocumentDB event
        notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.remove_source_identifier_from_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#remove_source_identifier_from_subscription)
        """

    def remove_tags_from_resource(self, *, ResourceName: str, TagKeys: List[str]) -> None:
        """
        Removes metadata tags from an Amazon DocumentDB resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.remove_tags_from_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#remove_tags_from_resource)
        """

    def reset_db_cluster_parameter_group(
        self,
        *,
        DBClusterParameterGroupName: str,
        ResetAllParameters: bool = None,
        Parameters: List["ParameterTypeDef"] = None
    ) -> DBClusterParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a cluster parameter group to the default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.reset_db_cluster_parameter_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#reset_db_cluster_parameter_group)
        """

    def restore_db_cluster_from_snapshot(
        self,
        *,
        DBClusterIdentifier: str,
        SnapshotIdentifier: str,
        Engine: str,
        AvailabilityZones: List[str] = None,
        EngineVersion: str = None,
        Port: int = None,
        DBSubnetGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        KmsKeyId: str = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DeletionProtection: bool = None,
        DBClusterParameterGroupName: str = None,
        StorageType: str = None
    ) -> RestoreDBClusterFromSnapshotResultTypeDef:
        """
        Creates a new cluster from a snapshot or cluster snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.restore_db_cluster_from_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#restore_db_cluster_from_snapshot)
        """

    def restore_db_cluster_to_point_in_time(
        self,
        *,
        DBClusterIdentifier: str,
        SourceDBClusterIdentifier: str,
        RestoreType: str = None,
        RestoreToTime: Union[datetime, str] = None,
        UseLatestRestorableTime: bool = None,
        Port: int = None,
        DBSubnetGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        KmsKeyId: str = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DeletionProtection: bool = None,
        StorageType: str = None
    ) -> RestoreDBClusterToPointInTimeResultTypeDef:
        """
        Restores a cluster to an arbitrary point in time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.restore_db_cluster_to_point_in_time)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#restore_db_cluster_to_point_in_time)
        """

    def start_db_cluster(self, *, DBClusterIdentifier: str) -> StartDBClusterResultTypeDef:
        """
        Restarts the stopped cluster that is specified by `DBClusterIdentifier`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.start_db_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#start_db_cluster)
        """

    def stop_db_cluster(self, *, DBClusterIdentifier: str) -> StopDBClusterResultTypeDef:
        """
        Stops the running cluster that is specified by `DBClusterIdentifier`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.stop_db_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#stop_db_cluster)
        """

    def switchover_global_cluster(
        self, *, GlobalClusterIdentifier: str, TargetDbClusterIdentifier: str
    ) -> SwitchoverGlobalClusterResultTypeDef:
        """
        Switches over the specified secondary Amazon DocumentDB cluster to be the new
        primary Amazon DocumentDB cluster in the global database cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Client.switchover_global_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/client.html#switchover_global_cluster)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_certificates"]
    ) -> DescribeCertificatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Paginator.DescribeCertificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators.html#describecertificatespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_parameter_groups"]
    ) -> DescribeDBClusterParameterGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Paginator.DescribeDBClusterParameterGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators.html#describedbclusterparametergroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_parameters"]
    ) -> DescribeDBClusterParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Paginator.DescribeDBClusterParameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators.html#describedbclusterparameterspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_snapshots"]
    ) -> DescribeDBClusterSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Paginator.DescribeDBClusterSnapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators.html#describedbclustersnapshotspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_clusters"]
    ) -> DescribeDBClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Paginator.DescribeDBClusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators.html#describedbclusterspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_engine_versions"]
    ) -> DescribeDBEngineVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Paginator.DescribeDBEngineVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators.html#describedbengineversionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_instances"]
    ) -> DescribeDBInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Paginator.DescribeDBInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators.html#describedbinstancespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_subnet_groups"]
    ) -> DescribeDBSubnetGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Paginator.DescribeDBSubnetGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators.html#describedbsubnetgroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_event_subscriptions"]
    ) -> DescribeEventSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Paginator.DescribeEventSubscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators.html#describeeventsubscriptionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_events"]) -> DescribeEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Paginator.DescribeEvents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators.html#describeeventspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_global_clusters"]
    ) -> DescribeGlobalClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Paginator.DescribeGlobalClusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators.html#describeglobalclusterspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_orderable_db_instance_options"]
    ) -> DescribeOrderableDBInstanceOptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Paginator.DescribeOrderableDBInstanceOptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators.html#describeorderabledbinstanceoptionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_pending_maintenance_actions"]
    ) -> DescribePendingMaintenanceActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Paginator.DescribePendingMaintenanceActions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators.html#describependingmaintenanceactionspaginator)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["db_instance_available"]
    ) -> DBInstanceAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Waiter.DBInstanceAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/waiters.html#dbinstanceavailablewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["db_instance_deleted"]) -> DBInstanceDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/docdb.html#DocDB.Waiter.DBInstanceDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/waiters.html#dbinstancedeletedwaiter)
        """
