"""
Type annotations for docdb service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_docdb.client import DocDBClient

    session = Session()
    client: DocDBClient = session.client("docdb")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

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
    AddSourceIdentifierToSubscriptionMessageTypeDef,
    AddSourceIdentifierToSubscriptionResultTypeDef,
    AddTagsToResourceMessageTypeDef,
    ApplyPendingMaintenanceActionMessageTypeDef,
    ApplyPendingMaintenanceActionResultTypeDef,
    CertificateMessageTypeDef,
    CopyDBClusterParameterGroupMessageTypeDef,
    CopyDBClusterParameterGroupResultTypeDef,
    CopyDBClusterSnapshotMessageTypeDef,
    CopyDBClusterSnapshotResultTypeDef,
    CreateDBClusterMessageTypeDef,
    CreateDBClusterParameterGroupMessageTypeDef,
    CreateDBClusterParameterGroupResultTypeDef,
    CreateDBClusterResultTypeDef,
    CreateDBClusterSnapshotMessageTypeDef,
    CreateDBClusterSnapshotResultTypeDef,
    CreateDBInstanceMessageTypeDef,
    CreateDBInstanceResultTypeDef,
    CreateDBSubnetGroupMessageTypeDef,
    CreateDBSubnetGroupResultTypeDef,
    CreateEventSubscriptionMessageTypeDef,
    CreateEventSubscriptionResultTypeDef,
    CreateGlobalClusterMessageTypeDef,
    CreateGlobalClusterResultTypeDef,
    DBClusterMessageTypeDef,
    DBClusterParameterGroupDetailsTypeDef,
    DBClusterParameterGroupNameMessageTypeDef,
    DBClusterParameterGroupsMessageTypeDef,
    DBClusterSnapshotMessageTypeDef,
    DBEngineVersionMessageTypeDef,
    DBInstanceMessageTypeDef,
    DBSubnetGroupMessageTypeDef,
    DeleteDBClusterMessageTypeDef,
    DeleteDBClusterParameterGroupMessageTypeDef,
    DeleteDBClusterResultTypeDef,
    DeleteDBClusterSnapshotMessageTypeDef,
    DeleteDBClusterSnapshotResultTypeDef,
    DeleteDBInstanceMessageTypeDef,
    DeleteDBInstanceResultTypeDef,
    DeleteDBSubnetGroupMessageTypeDef,
    DeleteEventSubscriptionMessageTypeDef,
    DeleteEventSubscriptionResultTypeDef,
    DeleteGlobalClusterMessageTypeDef,
    DeleteGlobalClusterResultTypeDef,
    DescribeCertificatesMessageTypeDef,
    DescribeDBClusterParameterGroupsMessageTypeDef,
    DescribeDBClusterParametersMessageTypeDef,
    DescribeDBClustersMessageTypeDef,
    DescribeDBClusterSnapshotAttributesMessageTypeDef,
    DescribeDBClusterSnapshotAttributesResultTypeDef,
    DescribeDBClusterSnapshotsMessageTypeDef,
    DescribeDBEngineVersionsMessageTypeDef,
    DescribeDBInstancesMessageTypeDef,
    DescribeDBSubnetGroupsMessageTypeDef,
    DescribeEngineDefaultClusterParametersMessageTypeDef,
    DescribeEngineDefaultClusterParametersResultTypeDef,
    DescribeEventCategoriesMessageTypeDef,
    DescribeEventsMessageTypeDef,
    DescribeEventSubscriptionsMessageTypeDef,
    DescribeGlobalClustersMessageTypeDef,
    DescribeOrderableDBInstanceOptionsMessageTypeDef,
    DescribePendingMaintenanceActionsMessageTypeDef,
    EmptyResponseMetadataTypeDef,
    EventCategoriesMessageTypeDef,
    EventsMessageTypeDef,
    EventSubscriptionsMessageTypeDef,
    FailoverDBClusterMessageTypeDef,
    FailoverDBClusterResultTypeDef,
    FailoverGlobalClusterMessageTypeDef,
    FailoverGlobalClusterResultTypeDef,
    GlobalClustersMessageTypeDef,
    ListTagsForResourceMessageTypeDef,
    ModifyDBClusterMessageTypeDef,
    ModifyDBClusterParameterGroupMessageTypeDef,
    ModifyDBClusterResultTypeDef,
    ModifyDBClusterSnapshotAttributeMessageTypeDef,
    ModifyDBClusterSnapshotAttributeResultTypeDef,
    ModifyDBInstanceMessageTypeDef,
    ModifyDBInstanceResultTypeDef,
    ModifyDBSubnetGroupMessageTypeDef,
    ModifyDBSubnetGroupResultTypeDef,
    ModifyEventSubscriptionMessageTypeDef,
    ModifyEventSubscriptionResultTypeDef,
    ModifyGlobalClusterMessageTypeDef,
    ModifyGlobalClusterResultTypeDef,
    OrderableDBInstanceOptionsMessageTypeDef,
    PendingMaintenanceActionsMessageTypeDef,
    RebootDBInstanceMessageTypeDef,
    RebootDBInstanceResultTypeDef,
    RemoveFromGlobalClusterMessageTypeDef,
    RemoveFromGlobalClusterResultTypeDef,
    RemoveSourceIdentifierFromSubscriptionMessageTypeDef,
    RemoveSourceIdentifierFromSubscriptionResultTypeDef,
    RemoveTagsFromResourceMessageTypeDef,
    ResetDBClusterParameterGroupMessageTypeDef,
    RestoreDBClusterFromSnapshotMessageTypeDef,
    RestoreDBClusterFromSnapshotResultTypeDef,
    RestoreDBClusterToPointInTimeMessageTypeDef,
    RestoreDBClusterToPointInTimeResultTypeDef,
    StartDBClusterMessageTypeDef,
    StartDBClusterResultTypeDef,
    StopDBClusterMessageTypeDef,
    StopDBClusterResultTypeDef,
    SwitchoverGlobalClusterMessageTypeDef,
    SwitchoverGlobalClusterResultTypeDef,
    TagListMessageTypeDef,
)
from .waiter import DBInstanceAvailableWaiter, DBInstanceDeletedWaiter

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("DocDBClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb.html#DocDB.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DocDBClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb.html#DocDB.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#generate_presigned_url)
        """

    def add_source_identifier_to_subscription(
        self, **kwargs: Unpack[AddSourceIdentifierToSubscriptionMessageTypeDef]
    ) -> AddSourceIdentifierToSubscriptionResultTypeDef:
        """
        Adds a source identifier to an existing event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/add_source_identifier_to_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#add_source_identifier_to_subscription)
        """

    def add_tags_to_resource(
        self, **kwargs: Unpack[AddTagsToResourceMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds metadata tags to an Amazon DocumentDB resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/add_tags_to_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#add_tags_to_resource)
        """

    def apply_pending_maintenance_action(
        self, **kwargs: Unpack[ApplyPendingMaintenanceActionMessageTypeDef]
    ) -> ApplyPendingMaintenanceActionResultTypeDef:
        """
        Applies a pending maintenance action to a resource (for example, to an Amazon
        DocumentDB instance).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/apply_pending_maintenance_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#apply_pending_maintenance_action)
        """

    def copy_db_cluster_parameter_group(
        self, **kwargs: Unpack[CopyDBClusterParameterGroupMessageTypeDef]
    ) -> CopyDBClusterParameterGroupResultTypeDef:
        """
        Copies the specified cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/copy_db_cluster_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#copy_db_cluster_parameter_group)
        """

    def copy_db_cluster_snapshot(
        self, **kwargs: Unpack[CopyDBClusterSnapshotMessageTypeDef]
    ) -> CopyDBClusterSnapshotResultTypeDef:
        """
        Copies a snapshot of a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/copy_db_cluster_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#copy_db_cluster_snapshot)
        """

    def create_db_cluster(
        self, **kwargs: Unpack[CreateDBClusterMessageTypeDef]
    ) -> CreateDBClusterResultTypeDef:
        """
        Creates a new Amazon DocumentDB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/create_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#create_db_cluster)
        """

    def create_db_cluster_parameter_group(
        self, **kwargs: Unpack[CreateDBClusterParameterGroupMessageTypeDef]
    ) -> CreateDBClusterParameterGroupResultTypeDef:
        """
        Creates a new cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/create_db_cluster_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#create_db_cluster_parameter_group)
        """

    def create_db_cluster_snapshot(
        self, **kwargs: Unpack[CreateDBClusterSnapshotMessageTypeDef]
    ) -> CreateDBClusterSnapshotResultTypeDef:
        """
        Creates a snapshot of a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/create_db_cluster_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#create_db_cluster_snapshot)
        """

    def create_db_instance(
        self, **kwargs: Unpack[CreateDBInstanceMessageTypeDef]
    ) -> CreateDBInstanceResultTypeDef:
        """
        Creates a new instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/create_db_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#create_db_instance)
        """

    def create_db_subnet_group(
        self, **kwargs: Unpack[CreateDBSubnetGroupMessageTypeDef]
    ) -> CreateDBSubnetGroupResultTypeDef:
        """
        Creates a new subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/create_db_subnet_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#create_db_subnet_group)
        """

    def create_event_subscription(
        self, **kwargs: Unpack[CreateEventSubscriptionMessageTypeDef]
    ) -> CreateEventSubscriptionResultTypeDef:
        """
        Creates an Amazon DocumentDB event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/create_event_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#create_event_subscription)
        """

    def create_global_cluster(
        self, **kwargs: Unpack[CreateGlobalClusterMessageTypeDef]
    ) -> CreateGlobalClusterResultTypeDef:
        """
        Creates an Amazon DocumentDB global cluster that can span multiple multiple
        Amazon Web Services Regions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/create_global_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#create_global_cluster)
        """

    def delete_db_cluster(
        self, **kwargs: Unpack[DeleteDBClusterMessageTypeDef]
    ) -> DeleteDBClusterResultTypeDef:
        """
        Deletes a previously provisioned cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/delete_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#delete_db_cluster)
        """

    def delete_db_cluster_parameter_group(
        self, **kwargs: Unpack[DeleteDBClusterParameterGroupMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a specified cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/delete_db_cluster_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#delete_db_cluster_parameter_group)
        """

    def delete_db_cluster_snapshot(
        self, **kwargs: Unpack[DeleteDBClusterSnapshotMessageTypeDef]
    ) -> DeleteDBClusterSnapshotResultTypeDef:
        """
        Deletes a cluster snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/delete_db_cluster_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#delete_db_cluster_snapshot)
        """

    def delete_db_instance(
        self, **kwargs: Unpack[DeleteDBInstanceMessageTypeDef]
    ) -> DeleteDBInstanceResultTypeDef:
        """
        Deletes a previously provisioned instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/delete_db_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#delete_db_instance)
        """

    def delete_db_subnet_group(
        self, **kwargs: Unpack[DeleteDBSubnetGroupMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/delete_db_subnet_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#delete_db_subnet_group)
        """

    def delete_event_subscription(
        self, **kwargs: Unpack[DeleteEventSubscriptionMessageTypeDef]
    ) -> DeleteEventSubscriptionResultTypeDef:
        """
        Deletes an Amazon DocumentDB event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/delete_event_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#delete_event_subscription)
        """

    def delete_global_cluster(
        self, **kwargs: Unpack[DeleteGlobalClusterMessageTypeDef]
    ) -> DeleteGlobalClusterResultTypeDef:
        """
        Deletes a global cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/delete_global_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#delete_global_cluster)
        """

    def describe_certificates(
        self, **kwargs: Unpack[DescribeCertificatesMessageTypeDef]
    ) -> CertificateMessageTypeDef:
        """
        Returns a list of certificate authority (CA) certificates provided by Amazon
        DocumentDB for this Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/describe_certificates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#describe_certificates)
        """

    def describe_db_cluster_parameter_groups(
        self, **kwargs: Unpack[DescribeDBClusterParameterGroupsMessageTypeDef]
    ) -> DBClusterParameterGroupsMessageTypeDef:
        """
        Returns a list of <code>DBClusterParameterGroup</code> descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/describe_db_cluster_parameter_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#describe_db_cluster_parameter_groups)
        """

    def describe_db_cluster_parameters(
        self, **kwargs: Unpack[DescribeDBClusterParametersMessageTypeDef]
    ) -> DBClusterParameterGroupDetailsTypeDef:
        """
        Returns the detailed parameter list for a particular cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/describe_db_cluster_parameters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#describe_db_cluster_parameters)
        """

    def describe_db_cluster_snapshot_attributes(
        self, **kwargs: Unpack[DescribeDBClusterSnapshotAttributesMessageTypeDef]
    ) -> DescribeDBClusterSnapshotAttributesResultTypeDef:
        """
        Returns a list of cluster snapshot attribute names and values for a manual DB
        cluster snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/describe_db_cluster_snapshot_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#describe_db_cluster_snapshot_attributes)
        """

    def describe_db_cluster_snapshots(
        self, **kwargs: Unpack[DescribeDBClusterSnapshotsMessageTypeDef]
    ) -> DBClusterSnapshotMessageTypeDef:
        """
        Returns information about cluster snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/describe_db_cluster_snapshots.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#describe_db_cluster_snapshots)
        """

    def describe_db_clusters(
        self, **kwargs: Unpack[DescribeDBClustersMessageTypeDef]
    ) -> DBClusterMessageTypeDef:
        """
        Returns information about provisioned Amazon DocumentDB clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/describe_db_clusters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#describe_db_clusters)
        """

    def describe_db_engine_versions(
        self, **kwargs: Unpack[DescribeDBEngineVersionsMessageTypeDef]
    ) -> DBEngineVersionMessageTypeDef:
        """
        Returns a list of the available engines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/describe_db_engine_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#describe_db_engine_versions)
        """

    def describe_db_instances(
        self, **kwargs: Unpack[DescribeDBInstancesMessageTypeDef]
    ) -> DBInstanceMessageTypeDef:
        """
        Returns information about provisioned Amazon DocumentDB instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/describe_db_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#describe_db_instances)
        """

    def describe_db_subnet_groups(
        self, **kwargs: Unpack[DescribeDBSubnetGroupsMessageTypeDef]
    ) -> DBSubnetGroupMessageTypeDef:
        """
        Returns a list of <code>DBSubnetGroup</code> descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/describe_db_subnet_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#describe_db_subnet_groups)
        """

    def describe_engine_default_cluster_parameters(
        self, **kwargs: Unpack[DescribeEngineDefaultClusterParametersMessageTypeDef]
    ) -> DescribeEngineDefaultClusterParametersResultTypeDef:
        """
        Returns the default engine and system parameter information for the cluster
        database engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/describe_engine_default_cluster_parameters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#describe_engine_default_cluster_parameters)
        """

    def describe_event_categories(
        self, **kwargs: Unpack[DescribeEventCategoriesMessageTypeDef]
    ) -> EventCategoriesMessageTypeDef:
        """
        Displays a list of categories for all event source types, or, if specified, for
        a specified source type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/describe_event_categories.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#describe_event_categories)
        """

    def describe_event_subscriptions(
        self, **kwargs: Unpack[DescribeEventSubscriptionsMessageTypeDef]
    ) -> EventSubscriptionsMessageTypeDef:
        """
        Lists all the subscription descriptions for a customer account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/describe_event_subscriptions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#describe_event_subscriptions)
        """

    def describe_events(
        self, **kwargs: Unpack[DescribeEventsMessageTypeDef]
    ) -> EventsMessageTypeDef:
        """
        Returns events related to instances, security groups, snapshots, and DB
        parameter groups for the past 14 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/describe_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#describe_events)
        """

    def describe_global_clusters(
        self, **kwargs: Unpack[DescribeGlobalClustersMessageTypeDef]
    ) -> GlobalClustersMessageTypeDef:
        """
        Returns information about Amazon DocumentDB global clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/describe_global_clusters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#describe_global_clusters)
        """

    def describe_orderable_db_instance_options(
        self, **kwargs: Unpack[DescribeOrderableDBInstanceOptionsMessageTypeDef]
    ) -> OrderableDBInstanceOptionsMessageTypeDef:
        """
        Returns a list of orderable instance options for the specified engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/describe_orderable_db_instance_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#describe_orderable_db_instance_options)
        """

    def describe_pending_maintenance_actions(
        self, **kwargs: Unpack[DescribePendingMaintenanceActionsMessageTypeDef]
    ) -> PendingMaintenanceActionsMessageTypeDef:
        """
        Returns a list of resources (for example, instances) that have at least one
        pending maintenance action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/describe_pending_maintenance_actions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#describe_pending_maintenance_actions)
        """

    def failover_db_cluster(
        self, **kwargs: Unpack[FailoverDBClusterMessageTypeDef]
    ) -> FailoverDBClusterResultTypeDef:
        """
        Forces a failover for a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/failover_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#failover_db_cluster)
        """

    def failover_global_cluster(
        self, **kwargs: Unpack[FailoverGlobalClusterMessageTypeDef]
    ) -> FailoverGlobalClusterResultTypeDef:
        """
        Promotes the specified secondary DB cluster to be the primary DB cluster in the
        global cluster when failing over a global cluster occurs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/failover_global_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#failover_global_cluster)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceMessageTypeDef]
    ) -> TagListMessageTypeDef:
        """
        Lists all tags on an Amazon DocumentDB resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#list_tags_for_resource)
        """

    def modify_db_cluster(
        self, **kwargs: Unpack[ModifyDBClusterMessageTypeDef]
    ) -> ModifyDBClusterResultTypeDef:
        """
        Modifies a setting for an Amazon DocumentDB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/modify_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#modify_db_cluster)
        """

    def modify_db_cluster_parameter_group(
        self, **kwargs: Unpack[ModifyDBClusterParameterGroupMessageTypeDef]
    ) -> DBClusterParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/modify_db_cluster_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#modify_db_cluster_parameter_group)
        """

    def modify_db_cluster_snapshot_attribute(
        self, **kwargs: Unpack[ModifyDBClusterSnapshotAttributeMessageTypeDef]
    ) -> ModifyDBClusterSnapshotAttributeResultTypeDef:
        """
        Adds an attribute and values to, or removes an attribute and values from, a
        manual cluster snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/modify_db_cluster_snapshot_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#modify_db_cluster_snapshot_attribute)
        """

    def modify_db_instance(
        self, **kwargs: Unpack[ModifyDBInstanceMessageTypeDef]
    ) -> ModifyDBInstanceResultTypeDef:
        """
        Modifies settings for an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/modify_db_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#modify_db_instance)
        """

    def modify_db_subnet_group(
        self, **kwargs: Unpack[ModifyDBSubnetGroupMessageTypeDef]
    ) -> ModifyDBSubnetGroupResultTypeDef:
        """
        Modifies an existing subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/modify_db_subnet_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#modify_db_subnet_group)
        """

    def modify_event_subscription(
        self, **kwargs: Unpack[ModifyEventSubscriptionMessageTypeDef]
    ) -> ModifyEventSubscriptionResultTypeDef:
        """
        Modifies an existing Amazon DocumentDB event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/modify_event_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#modify_event_subscription)
        """

    def modify_global_cluster(
        self, **kwargs: Unpack[ModifyGlobalClusterMessageTypeDef]
    ) -> ModifyGlobalClusterResultTypeDef:
        """
        Modify a setting for an Amazon DocumentDB global cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/modify_global_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#modify_global_cluster)
        """

    def reboot_db_instance(
        self, **kwargs: Unpack[RebootDBInstanceMessageTypeDef]
    ) -> RebootDBInstanceResultTypeDef:
        """
        You might need to reboot your instance, usually for maintenance reasons.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/reboot_db_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#reboot_db_instance)
        """

    def remove_from_global_cluster(
        self, **kwargs: Unpack[RemoveFromGlobalClusterMessageTypeDef]
    ) -> RemoveFromGlobalClusterResultTypeDef:
        """
        Detaches an Amazon DocumentDB secondary cluster from a global cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/remove_from_global_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#remove_from_global_cluster)
        """

    def remove_source_identifier_from_subscription(
        self, **kwargs: Unpack[RemoveSourceIdentifierFromSubscriptionMessageTypeDef]
    ) -> RemoveSourceIdentifierFromSubscriptionResultTypeDef:
        """
        Removes a source identifier from an existing Amazon DocumentDB event
        notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/remove_source_identifier_from_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#remove_source_identifier_from_subscription)
        """

    def remove_tags_from_resource(
        self, **kwargs: Unpack[RemoveTagsFromResourceMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes metadata tags from an Amazon DocumentDB resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/remove_tags_from_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#remove_tags_from_resource)
        """

    def reset_db_cluster_parameter_group(
        self, **kwargs: Unpack[ResetDBClusterParameterGroupMessageTypeDef]
    ) -> DBClusterParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a cluster parameter group to the default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/reset_db_cluster_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#reset_db_cluster_parameter_group)
        """

    def restore_db_cluster_from_snapshot(
        self, **kwargs: Unpack[RestoreDBClusterFromSnapshotMessageTypeDef]
    ) -> RestoreDBClusterFromSnapshotResultTypeDef:
        """
        Creates a new cluster from a snapshot or cluster snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/restore_db_cluster_from_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#restore_db_cluster_from_snapshot)
        """

    def restore_db_cluster_to_point_in_time(
        self, **kwargs: Unpack[RestoreDBClusterToPointInTimeMessageTypeDef]
    ) -> RestoreDBClusterToPointInTimeResultTypeDef:
        """
        Restores a cluster to an arbitrary point in time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/restore_db_cluster_to_point_in_time.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#restore_db_cluster_to_point_in_time)
        """

    def start_db_cluster(
        self, **kwargs: Unpack[StartDBClusterMessageTypeDef]
    ) -> StartDBClusterResultTypeDef:
        """
        Restarts the stopped cluster that is specified by
        <code>DBClusterIdentifier</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/start_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#start_db_cluster)
        """

    def stop_db_cluster(
        self, **kwargs: Unpack[StopDBClusterMessageTypeDef]
    ) -> StopDBClusterResultTypeDef:
        """
        Stops the running cluster that is specified by <code>DBClusterIdentifier</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/stop_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#stop_db_cluster)
        """

    def switchover_global_cluster(
        self, **kwargs: Unpack[SwitchoverGlobalClusterMessageTypeDef]
    ) -> SwitchoverGlobalClusterResultTypeDef:
        """
        Switches over the specified secondary Amazon DocumentDB cluster to be the new
        primary Amazon DocumentDB cluster in the global database cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/switchover_global_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#switchover_global_cluster)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_certificates"]
    ) -> DescribeCertificatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_cluster_parameter_groups"]
    ) -> DescribeDBClusterParameterGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_cluster_parameters"]
    ) -> DescribeDBClusterParametersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_cluster_snapshots"]
    ) -> DescribeDBClusterSnapshotsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_clusters"]
    ) -> DescribeDBClustersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_engine_versions"]
    ) -> DescribeDBEngineVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_instances"]
    ) -> DescribeDBInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_subnet_groups"]
    ) -> DescribeDBSubnetGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_event_subscriptions"]
    ) -> DescribeEventSubscriptionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_events"]
    ) -> DescribeEventsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_global_clusters"]
    ) -> DescribeGlobalClustersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_orderable_db_instance_options"]
    ) -> DescribeOrderableDBInstanceOptionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_pending_maintenance_actions"]
    ) -> DescribePendingMaintenanceActionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["db_instance_available"]
    ) -> DBInstanceAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["db_instance_deleted"]
    ) -> DBInstanceDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/client/#get_waiter)
        """
