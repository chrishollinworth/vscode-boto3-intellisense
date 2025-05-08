"""
Type annotations for neptune service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_neptune.client import NeptuneClient

    session = Session()
    client: NeptuneClient = session.client("neptune")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeDBClusterEndpointsPaginator,
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
    DescribeGlobalClustersPaginator,
    DescribeOrderableDBInstanceOptionsPaginator,
    DescribePendingMaintenanceActionsPaginator,
)
from .type_defs import (
    AddRoleToDBClusterMessageTypeDef,
    AddSourceIdentifierToSubscriptionMessageTypeDef,
    AddSourceIdentifierToSubscriptionResultTypeDef,
    AddTagsToResourceMessageTypeDef,
    ApplyPendingMaintenanceActionMessageTypeDef,
    ApplyPendingMaintenanceActionResultTypeDef,
    CopyDBClusterParameterGroupMessageTypeDef,
    CopyDBClusterParameterGroupResultTypeDef,
    CopyDBClusterSnapshotMessageTypeDef,
    CopyDBClusterSnapshotResultTypeDef,
    CopyDBParameterGroupMessageTypeDef,
    CopyDBParameterGroupResultTypeDef,
    CreateDBClusterEndpointMessageTypeDef,
    CreateDBClusterEndpointOutputTypeDef,
    CreateDBClusterMessageTypeDef,
    CreateDBClusterParameterGroupMessageTypeDef,
    CreateDBClusterParameterGroupResultTypeDef,
    CreateDBClusterResultTypeDef,
    CreateDBClusterSnapshotMessageTypeDef,
    CreateDBClusterSnapshotResultTypeDef,
    CreateDBInstanceMessageTypeDef,
    CreateDBInstanceResultTypeDef,
    CreateDBParameterGroupMessageTypeDef,
    CreateDBParameterGroupResultTypeDef,
    CreateDBSubnetGroupMessageTypeDef,
    CreateDBSubnetGroupResultTypeDef,
    CreateEventSubscriptionMessageTypeDef,
    CreateEventSubscriptionResultTypeDef,
    CreateGlobalClusterMessageTypeDef,
    CreateGlobalClusterResultTypeDef,
    DBClusterEndpointMessageTypeDef,
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
    DeleteDBClusterEndpointMessageTypeDef,
    DeleteDBClusterEndpointOutputTypeDef,
    DeleteDBClusterMessageTypeDef,
    DeleteDBClusterParameterGroupMessageTypeDef,
    DeleteDBClusterResultTypeDef,
    DeleteDBClusterSnapshotMessageTypeDef,
    DeleteDBClusterSnapshotResultTypeDef,
    DeleteDBInstanceMessageTypeDef,
    DeleteDBInstanceResultTypeDef,
    DeleteDBParameterGroupMessageTypeDef,
    DeleteDBSubnetGroupMessageTypeDef,
    DeleteEventSubscriptionMessageTypeDef,
    DeleteEventSubscriptionResultTypeDef,
    DeleteGlobalClusterMessageTypeDef,
    DeleteGlobalClusterResultTypeDef,
    DescribeDBClusterEndpointsMessageTypeDef,
    DescribeDBClusterParameterGroupsMessageTypeDef,
    DescribeDBClusterParametersMessageTypeDef,
    DescribeDBClustersMessageTypeDef,
    DescribeDBClusterSnapshotAttributesMessageTypeDef,
    DescribeDBClusterSnapshotAttributesResultTypeDef,
    DescribeDBClusterSnapshotsMessageTypeDef,
    DescribeDBEngineVersionsMessageTypeDef,
    DescribeDBInstancesMessageTypeDef,
    DescribeDBParameterGroupsMessageTypeDef,
    DescribeDBParametersMessageTypeDef,
    DescribeDBSubnetGroupsMessageTypeDef,
    DescribeEngineDefaultClusterParametersMessageTypeDef,
    DescribeEngineDefaultClusterParametersResultTypeDef,
    DescribeEngineDefaultParametersMessageTypeDef,
    DescribeEngineDefaultParametersResultTypeDef,
    DescribeEventCategoriesMessageTypeDef,
    DescribeEventsMessageTypeDef,
    DescribeEventSubscriptionsMessageTypeDef,
    DescribeGlobalClustersMessageTypeDef,
    DescribeOrderableDBInstanceOptionsMessageTypeDef,
    DescribePendingMaintenanceActionsMessageTypeDef,
    DescribeValidDBInstanceModificationsMessageTypeDef,
    DescribeValidDBInstanceModificationsResultTypeDef,
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
    ModifyDBClusterEndpointMessageTypeDef,
    ModifyDBClusterEndpointOutputTypeDef,
    ModifyDBClusterMessageTypeDef,
    ModifyDBClusterParameterGroupMessageTypeDef,
    ModifyDBClusterResultTypeDef,
    ModifyDBClusterSnapshotAttributeMessageTypeDef,
    ModifyDBClusterSnapshotAttributeResultTypeDef,
    ModifyDBInstanceMessageTypeDef,
    ModifyDBInstanceResultTypeDef,
    ModifyDBParameterGroupMessageTypeDef,
    ModifyDBSubnetGroupMessageTypeDef,
    ModifyDBSubnetGroupResultTypeDef,
    ModifyEventSubscriptionMessageTypeDef,
    ModifyEventSubscriptionResultTypeDef,
    ModifyGlobalClusterMessageTypeDef,
    ModifyGlobalClusterResultTypeDef,
    OrderableDBInstanceOptionsMessageTypeDef,
    PendingMaintenanceActionsMessageTypeDef,
    PromoteReadReplicaDBClusterMessageTypeDef,
    PromoteReadReplicaDBClusterResultTypeDef,
    RebootDBInstanceMessageTypeDef,
    RebootDBInstanceResultTypeDef,
    RemoveFromGlobalClusterMessageTypeDef,
    RemoveFromGlobalClusterResultTypeDef,
    RemoveRoleFromDBClusterMessageTypeDef,
    RemoveSourceIdentifierFromSubscriptionMessageTypeDef,
    RemoveSourceIdentifierFromSubscriptionResultTypeDef,
    RemoveTagsFromResourceMessageTypeDef,
    ResetDBClusterParameterGroupMessageTypeDef,
    ResetDBParameterGroupMessageTypeDef,
    RestoreDBClusterFromSnapshotMessageTypeDef,
    RestoreDBClusterFromSnapshotResultTypeDef,
    RestoreDBClusterToPointInTimeMessageTypeDef,
    RestoreDBClusterToPointInTimeResultTypeDef,
    StartDBClusterMessageTypeDef,
    StartDBClusterResultTypeDef,
    StopDBClusterMessageTypeDef,
    StopDBClusterResultTypeDef,
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

__all__ = ("NeptuneClient",)

class Exceptions(BaseClientExceptions):
    AuthorizationNotFoundFault: Type[BotocoreClientError]
    CertificateNotFoundFault: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DBClusterAlreadyExistsFault: Type[BotocoreClientError]
    DBClusterEndpointAlreadyExistsFault: Type[BotocoreClientError]
    DBClusterEndpointNotFoundFault: Type[BotocoreClientError]
    DBClusterEndpointQuotaExceededFault: Type[BotocoreClientError]
    DBClusterNotFoundFault: Type[BotocoreClientError]
    DBClusterParameterGroupNotFoundFault: Type[BotocoreClientError]
    DBClusterQuotaExceededFault: Type[BotocoreClientError]
    DBClusterRoleAlreadyExistsFault: Type[BotocoreClientError]
    DBClusterRoleNotFoundFault: Type[BotocoreClientError]
    DBClusterRoleQuotaExceededFault: Type[BotocoreClientError]
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
    DomainNotFoundFault: Type[BotocoreClientError]
    EventSubscriptionQuotaExceededFault: Type[BotocoreClientError]
    GlobalClusterAlreadyExistsFault: Type[BotocoreClientError]
    GlobalClusterNotFoundFault: Type[BotocoreClientError]
    GlobalClusterQuotaExceededFault: Type[BotocoreClientError]
    InstanceQuotaExceededFault: Type[BotocoreClientError]
    InsufficientDBClusterCapacityFault: Type[BotocoreClientError]
    InsufficientDBInstanceCapacityFault: Type[BotocoreClientError]
    InsufficientStorageClusterCapacityFault: Type[BotocoreClientError]
    InvalidDBClusterEndpointStateFault: Type[BotocoreClientError]
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
    OptionGroupNotFoundFault: Type[BotocoreClientError]
    ProvisionedIopsNotAvailableInAZFault: Type[BotocoreClientError]
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

class NeptuneClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        NeptuneClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#generate_presigned_url)
        """

    def add_role_to_db_cluster(
        self, **kwargs: Unpack[AddRoleToDBClusterMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates an Identity and Access Management (IAM) role with an Neptune DB
        cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/add_role_to_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#add_role_to_db_cluster)
        """

    def add_source_identifier_to_subscription(
        self, **kwargs: Unpack[AddSourceIdentifierToSubscriptionMessageTypeDef]
    ) -> AddSourceIdentifierToSubscriptionResultTypeDef:
        """
        Adds a source identifier to an existing event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/add_source_identifier_to_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#add_source_identifier_to_subscription)
        """

    def add_tags_to_resource(
        self, **kwargs: Unpack[AddTagsToResourceMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds metadata tags to an Amazon Neptune resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/add_tags_to_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#add_tags_to_resource)
        """

    def apply_pending_maintenance_action(
        self, **kwargs: Unpack[ApplyPendingMaintenanceActionMessageTypeDef]
    ) -> ApplyPendingMaintenanceActionResultTypeDef:
        """
        Applies a pending maintenance action to a resource (for example, to a DB
        instance).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/apply_pending_maintenance_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#apply_pending_maintenance_action)
        """

    def copy_db_cluster_parameter_group(
        self, **kwargs: Unpack[CopyDBClusterParameterGroupMessageTypeDef]
    ) -> CopyDBClusterParameterGroupResultTypeDef:
        """
        Copies the specified DB cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/copy_db_cluster_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#copy_db_cluster_parameter_group)
        """

    def copy_db_cluster_snapshot(
        self, **kwargs: Unpack[CopyDBClusterSnapshotMessageTypeDef]
    ) -> CopyDBClusterSnapshotResultTypeDef:
        """
        Copies a snapshot of a DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/copy_db_cluster_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#copy_db_cluster_snapshot)
        """

    def copy_db_parameter_group(
        self, **kwargs: Unpack[CopyDBParameterGroupMessageTypeDef]
    ) -> CopyDBParameterGroupResultTypeDef:
        """
        Copies the specified DB parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/copy_db_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#copy_db_parameter_group)
        """

    def create_db_cluster(
        self, **kwargs: Unpack[CreateDBClusterMessageTypeDef]
    ) -> CreateDBClusterResultTypeDef:
        """
        Creates a new Amazon Neptune DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/create_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#create_db_cluster)
        """

    def create_db_cluster_endpoint(
        self, **kwargs: Unpack[CreateDBClusterEndpointMessageTypeDef]
    ) -> CreateDBClusterEndpointOutputTypeDef:
        """
        Creates a new custom endpoint and associates it with an Amazon Neptune DB
        cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/create_db_cluster_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#create_db_cluster_endpoint)
        """

    def create_db_cluster_parameter_group(
        self, **kwargs: Unpack[CreateDBClusterParameterGroupMessageTypeDef]
    ) -> CreateDBClusterParameterGroupResultTypeDef:
        """
        Creates a new DB cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/create_db_cluster_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#create_db_cluster_parameter_group)
        """

    def create_db_cluster_snapshot(
        self, **kwargs: Unpack[CreateDBClusterSnapshotMessageTypeDef]
    ) -> CreateDBClusterSnapshotResultTypeDef:
        """
        Creates a snapshot of a DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/create_db_cluster_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#create_db_cluster_snapshot)
        """

    def create_db_instance(
        self, **kwargs: Unpack[CreateDBInstanceMessageTypeDef]
    ) -> CreateDBInstanceResultTypeDef:
        """
        Creates a new DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/create_db_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#create_db_instance)
        """

    def create_db_parameter_group(
        self, **kwargs: Unpack[CreateDBParameterGroupMessageTypeDef]
    ) -> CreateDBParameterGroupResultTypeDef:
        """
        Creates a new DB parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/create_db_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#create_db_parameter_group)
        """

    def create_db_subnet_group(
        self, **kwargs: Unpack[CreateDBSubnetGroupMessageTypeDef]
    ) -> CreateDBSubnetGroupResultTypeDef:
        """
        Creates a new DB subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/create_db_subnet_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#create_db_subnet_group)
        """

    def create_event_subscription(
        self, **kwargs: Unpack[CreateEventSubscriptionMessageTypeDef]
    ) -> CreateEventSubscriptionResultTypeDef:
        """
        Creates an event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/create_event_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#create_event_subscription)
        """

    def create_global_cluster(
        self, **kwargs: Unpack[CreateGlobalClusterMessageTypeDef]
    ) -> CreateGlobalClusterResultTypeDef:
        """
        Creates a Neptune global database spread across multiple Amazon Regions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/create_global_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#create_global_cluster)
        """

    def delete_db_cluster(
        self, **kwargs: Unpack[DeleteDBClusterMessageTypeDef]
    ) -> DeleteDBClusterResultTypeDef:
        """
        The DeleteDBCluster action deletes a previously provisioned DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/delete_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#delete_db_cluster)
        """

    def delete_db_cluster_endpoint(
        self, **kwargs: Unpack[DeleteDBClusterEndpointMessageTypeDef]
    ) -> DeleteDBClusterEndpointOutputTypeDef:
        """
        Deletes a custom endpoint and removes it from an Amazon Neptune DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/delete_db_cluster_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#delete_db_cluster_endpoint)
        """

    def delete_db_cluster_parameter_group(
        self, **kwargs: Unpack[DeleteDBClusterParameterGroupMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a specified DB cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/delete_db_cluster_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#delete_db_cluster_parameter_group)
        """

    def delete_db_cluster_snapshot(
        self, **kwargs: Unpack[DeleteDBClusterSnapshotMessageTypeDef]
    ) -> DeleteDBClusterSnapshotResultTypeDef:
        """
        Deletes a DB cluster snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/delete_db_cluster_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#delete_db_cluster_snapshot)
        """

    def delete_db_instance(
        self, **kwargs: Unpack[DeleteDBInstanceMessageTypeDef]
    ) -> DeleteDBInstanceResultTypeDef:
        """
        The DeleteDBInstance action deletes a previously provisioned DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/delete_db_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#delete_db_instance)
        """

    def delete_db_parameter_group(
        self, **kwargs: Unpack[DeleteDBParameterGroupMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a specified DBParameterGroup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/delete_db_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#delete_db_parameter_group)
        """

    def delete_db_subnet_group(
        self, **kwargs: Unpack[DeleteDBSubnetGroupMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a DB subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/delete_db_subnet_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#delete_db_subnet_group)
        """

    def delete_event_subscription(
        self, **kwargs: Unpack[DeleteEventSubscriptionMessageTypeDef]
    ) -> DeleteEventSubscriptionResultTypeDef:
        """
        Deletes an event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/delete_event_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#delete_event_subscription)
        """

    def delete_global_cluster(
        self, **kwargs: Unpack[DeleteGlobalClusterMessageTypeDef]
    ) -> DeleteGlobalClusterResultTypeDef:
        """
        Deletes a global database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/delete_global_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#delete_global_cluster)
        """

    def describe_db_cluster_endpoints(
        self, **kwargs: Unpack[DescribeDBClusterEndpointsMessageTypeDef]
    ) -> DBClusterEndpointMessageTypeDef:
        """
        Returns information about endpoints for an Amazon Neptune DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/describe_db_cluster_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#describe_db_cluster_endpoints)
        """

    def describe_db_cluster_parameter_groups(
        self, **kwargs: Unpack[DescribeDBClusterParameterGroupsMessageTypeDef]
    ) -> DBClusterParameterGroupsMessageTypeDef:
        """
        Returns a list of <code>DBClusterParameterGroup</code> descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/describe_db_cluster_parameter_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#describe_db_cluster_parameter_groups)
        """

    def describe_db_cluster_parameters(
        self, **kwargs: Unpack[DescribeDBClusterParametersMessageTypeDef]
    ) -> DBClusterParameterGroupDetailsTypeDef:
        """
        Returns the detailed parameter list for a particular DB cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/describe_db_cluster_parameters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#describe_db_cluster_parameters)
        """

    def describe_db_cluster_snapshot_attributes(
        self, **kwargs: Unpack[DescribeDBClusterSnapshotAttributesMessageTypeDef]
    ) -> DescribeDBClusterSnapshotAttributesResultTypeDef:
        """
        Returns a list of DB cluster snapshot attribute names and values for a manual
        DB cluster snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/describe_db_cluster_snapshot_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#describe_db_cluster_snapshot_attributes)
        """

    def describe_db_cluster_snapshots(
        self, **kwargs: Unpack[DescribeDBClusterSnapshotsMessageTypeDef]
    ) -> DBClusterSnapshotMessageTypeDef:
        """
        Returns information about DB cluster snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/describe_db_cluster_snapshots.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#describe_db_cluster_snapshots)
        """

    def describe_db_clusters(
        self, **kwargs: Unpack[DescribeDBClustersMessageTypeDef]
    ) -> DBClusterMessageTypeDef:
        """
        Returns information about provisioned DB clusters, and supports pagination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/describe_db_clusters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#describe_db_clusters)
        """

    def describe_db_engine_versions(
        self, **kwargs: Unpack[DescribeDBEngineVersionsMessageTypeDef]
    ) -> DBEngineVersionMessageTypeDef:
        """
        Returns a list of the available DB engines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/describe_db_engine_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#describe_db_engine_versions)
        """

    def describe_db_instances(
        self, **kwargs: Unpack[DescribeDBInstancesMessageTypeDef]
    ) -> DBInstanceMessageTypeDef:
        """
        Returns information about provisioned instances, and supports pagination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/describe_db_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#describe_db_instances)
        """

    def describe_db_parameter_groups(
        self, **kwargs: Unpack[DescribeDBParameterGroupsMessageTypeDef]
    ) -> DBParameterGroupsMessageTypeDef:
        """
        Returns a list of <code>DBParameterGroup</code> descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/describe_db_parameter_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#describe_db_parameter_groups)
        """

    def describe_db_parameters(
        self, **kwargs: Unpack[DescribeDBParametersMessageTypeDef]
    ) -> DBParameterGroupDetailsTypeDef:
        """
        Returns the detailed parameter list for a particular DB parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/describe_db_parameters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#describe_db_parameters)
        """

    def describe_db_subnet_groups(
        self, **kwargs: Unpack[DescribeDBSubnetGroupsMessageTypeDef]
    ) -> DBSubnetGroupMessageTypeDef:
        """
        Returns a list of DBSubnetGroup descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/describe_db_subnet_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#describe_db_subnet_groups)
        """

    def describe_engine_default_cluster_parameters(
        self, **kwargs: Unpack[DescribeEngineDefaultClusterParametersMessageTypeDef]
    ) -> DescribeEngineDefaultClusterParametersResultTypeDef:
        """
        Returns the default engine and system parameter information for the cluster
        database engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/describe_engine_default_cluster_parameters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#describe_engine_default_cluster_parameters)
        """

    def describe_engine_default_parameters(
        self, **kwargs: Unpack[DescribeEngineDefaultParametersMessageTypeDef]
    ) -> DescribeEngineDefaultParametersResultTypeDef:
        """
        Returns the default engine and system parameter information for the specified
        database engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/describe_engine_default_parameters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#describe_engine_default_parameters)
        """

    def describe_event_categories(
        self, **kwargs: Unpack[DescribeEventCategoriesMessageTypeDef]
    ) -> EventCategoriesMessageTypeDef:
        """
        Displays a list of categories for all event source types, or, if specified, for
        a specified source type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/describe_event_categories.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#describe_event_categories)
        """

    def describe_event_subscriptions(
        self, **kwargs: Unpack[DescribeEventSubscriptionsMessageTypeDef]
    ) -> EventSubscriptionsMessageTypeDef:
        """
        Lists all the subscription descriptions for a customer account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/describe_event_subscriptions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#describe_event_subscriptions)
        """

    def describe_events(
        self, **kwargs: Unpack[DescribeEventsMessageTypeDef]
    ) -> EventsMessageTypeDef:
        """
        Returns events related to DB instances, DB security groups, DB snapshots, and
        DB parameter groups for the past 14 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/describe_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#describe_events)
        """

    def describe_global_clusters(
        self, **kwargs: Unpack[DescribeGlobalClustersMessageTypeDef]
    ) -> GlobalClustersMessageTypeDef:
        """
        Returns information about Neptune global database clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/describe_global_clusters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#describe_global_clusters)
        """

    def describe_orderable_db_instance_options(
        self, **kwargs: Unpack[DescribeOrderableDBInstanceOptionsMessageTypeDef]
    ) -> OrderableDBInstanceOptionsMessageTypeDef:
        """
        Returns a list of orderable DB instance options for the specified engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/describe_orderable_db_instance_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#describe_orderable_db_instance_options)
        """

    def describe_pending_maintenance_actions(
        self, **kwargs: Unpack[DescribePendingMaintenanceActionsMessageTypeDef]
    ) -> PendingMaintenanceActionsMessageTypeDef:
        """
        Returns a list of resources (for example, DB instances) that have at least one
        pending maintenance action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/describe_pending_maintenance_actions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#describe_pending_maintenance_actions)
        """

    def describe_valid_db_instance_modifications(
        self, **kwargs: Unpack[DescribeValidDBInstanceModificationsMessageTypeDef]
    ) -> DescribeValidDBInstanceModificationsResultTypeDef:
        """
        You can call <a>DescribeValidDBInstanceModifications</a> to learn what
        modifications you can make to your DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/describe_valid_db_instance_modifications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#describe_valid_db_instance_modifications)
        """

    def failover_db_cluster(
        self, **kwargs: Unpack[FailoverDBClusterMessageTypeDef]
    ) -> FailoverDBClusterResultTypeDef:
        """
        Forces a failover for a DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/failover_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#failover_db_cluster)
        """

    def failover_global_cluster(
        self, **kwargs: Unpack[FailoverGlobalClusterMessageTypeDef]
    ) -> FailoverGlobalClusterResultTypeDef:
        """
        Initiates the failover process for a Neptune global database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/failover_global_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#failover_global_cluster)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceMessageTypeDef]
    ) -> TagListMessageTypeDef:
        """
        Lists all tags on an Amazon Neptune resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#list_tags_for_resource)
        """

    def modify_db_cluster(
        self, **kwargs: Unpack[ModifyDBClusterMessageTypeDef]
    ) -> ModifyDBClusterResultTypeDef:
        """
        Modify a setting for a DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/modify_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#modify_db_cluster)
        """

    def modify_db_cluster_endpoint(
        self, **kwargs: Unpack[ModifyDBClusterEndpointMessageTypeDef]
    ) -> ModifyDBClusterEndpointOutputTypeDef:
        """
        Modifies the properties of an endpoint in an Amazon Neptune DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/modify_db_cluster_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#modify_db_cluster_endpoint)
        """

    def modify_db_cluster_parameter_group(
        self, **kwargs: Unpack[ModifyDBClusterParameterGroupMessageTypeDef]
    ) -> DBClusterParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a DB cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/modify_db_cluster_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#modify_db_cluster_parameter_group)
        """

    def modify_db_cluster_snapshot_attribute(
        self, **kwargs: Unpack[ModifyDBClusterSnapshotAttributeMessageTypeDef]
    ) -> ModifyDBClusterSnapshotAttributeResultTypeDef:
        """
        Adds an attribute and values to, or removes an attribute and values from, a
        manual DB cluster snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/modify_db_cluster_snapshot_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#modify_db_cluster_snapshot_attribute)
        """

    def modify_db_instance(
        self, **kwargs: Unpack[ModifyDBInstanceMessageTypeDef]
    ) -> ModifyDBInstanceResultTypeDef:
        """
        Modifies settings for a DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/modify_db_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#modify_db_instance)
        """

    def modify_db_parameter_group(
        self, **kwargs: Unpack[ModifyDBParameterGroupMessageTypeDef]
    ) -> DBParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a DB parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/modify_db_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#modify_db_parameter_group)
        """

    def modify_db_subnet_group(
        self, **kwargs: Unpack[ModifyDBSubnetGroupMessageTypeDef]
    ) -> ModifyDBSubnetGroupResultTypeDef:
        """
        Modifies an existing DB subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/modify_db_subnet_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#modify_db_subnet_group)
        """

    def modify_event_subscription(
        self, **kwargs: Unpack[ModifyEventSubscriptionMessageTypeDef]
    ) -> ModifyEventSubscriptionResultTypeDef:
        """
        Modifies an existing event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/modify_event_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#modify_event_subscription)
        """

    def modify_global_cluster(
        self, **kwargs: Unpack[ModifyGlobalClusterMessageTypeDef]
    ) -> ModifyGlobalClusterResultTypeDef:
        """
        Modify a setting for an Amazon Neptune global cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/modify_global_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#modify_global_cluster)
        """

    def promote_read_replica_db_cluster(
        self, **kwargs: Unpack[PromoteReadReplicaDBClusterMessageTypeDef]
    ) -> PromoteReadReplicaDBClusterResultTypeDef:
        """
        Not supported.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/promote_read_replica_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#promote_read_replica_db_cluster)
        """

    def reboot_db_instance(
        self, **kwargs: Unpack[RebootDBInstanceMessageTypeDef]
    ) -> RebootDBInstanceResultTypeDef:
        """
        You might need to reboot your DB instance, usually for maintenance reasons.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/reboot_db_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#reboot_db_instance)
        """

    def remove_from_global_cluster(
        self, **kwargs: Unpack[RemoveFromGlobalClusterMessageTypeDef]
    ) -> RemoveFromGlobalClusterResultTypeDef:
        """
        Detaches a Neptune DB cluster from a Neptune global database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/remove_from_global_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#remove_from_global_cluster)
        """

    def remove_role_from_db_cluster(
        self, **kwargs: Unpack[RemoveRoleFromDBClusterMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disassociates an Identity and Access Management (IAM) role from a DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/remove_role_from_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#remove_role_from_db_cluster)
        """

    def remove_source_identifier_from_subscription(
        self, **kwargs: Unpack[RemoveSourceIdentifierFromSubscriptionMessageTypeDef]
    ) -> RemoveSourceIdentifierFromSubscriptionResultTypeDef:
        """
        Removes a source identifier from an existing event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/remove_source_identifier_from_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#remove_source_identifier_from_subscription)
        """

    def remove_tags_from_resource(
        self, **kwargs: Unpack[RemoveTagsFromResourceMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes metadata tags from an Amazon Neptune resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/remove_tags_from_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#remove_tags_from_resource)
        """

    def reset_db_cluster_parameter_group(
        self, **kwargs: Unpack[ResetDBClusterParameterGroupMessageTypeDef]
    ) -> DBClusterParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a DB cluster parameter group to the default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/reset_db_cluster_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#reset_db_cluster_parameter_group)
        """

    def reset_db_parameter_group(
        self, **kwargs: Unpack[ResetDBParameterGroupMessageTypeDef]
    ) -> DBParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a DB parameter group to the engine/system default
        value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/reset_db_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#reset_db_parameter_group)
        """

    def restore_db_cluster_from_snapshot(
        self, **kwargs: Unpack[RestoreDBClusterFromSnapshotMessageTypeDef]
    ) -> RestoreDBClusterFromSnapshotResultTypeDef:
        """
        Creates a new DB cluster from a DB snapshot or DB cluster snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/restore_db_cluster_from_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#restore_db_cluster_from_snapshot)
        """

    def restore_db_cluster_to_point_in_time(
        self, **kwargs: Unpack[RestoreDBClusterToPointInTimeMessageTypeDef]
    ) -> RestoreDBClusterToPointInTimeResultTypeDef:
        """
        Restores a DB cluster to an arbitrary point in time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/restore_db_cluster_to_point_in_time.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#restore_db_cluster_to_point_in_time)
        """

    def start_db_cluster(
        self, **kwargs: Unpack[StartDBClusterMessageTypeDef]
    ) -> StartDBClusterResultTypeDef:
        """
        Starts an Amazon Neptune DB cluster that was stopped using the Amazon console,
        the Amazon CLI stop-db-cluster command, or the StopDBCluster API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/start_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#start_db_cluster)
        """

    def stop_db_cluster(
        self, **kwargs: Unpack[StopDBClusterMessageTypeDef]
    ) -> StopDBClusterResultTypeDef:
        """
        Stops an Amazon Neptune DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/stop_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#stop_db_cluster)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_cluster_endpoints"]
    ) -> DescribeDBClusterEndpointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_cluster_parameter_groups"]
    ) -> DescribeDBClusterParameterGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_cluster_parameters"]
    ) -> DescribeDBClusterParametersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_cluster_snapshots"]
    ) -> DescribeDBClusterSnapshotsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_clusters"]
    ) -> DescribeDBClustersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_engine_versions"]
    ) -> DescribeDBEngineVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_instances"]
    ) -> DescribeDBInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_parameter_groups"]
    ) -> DescribeDBParameterGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_parameters"]
    ) -> DescribeDBParametersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_subnet_groups"]
    ) -> DescribeDBSubnetGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_engine_default_parameters"]
    ) -> DescribeEngineDefaultParametersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_event_subscriptions"]
    ) -> DescribeEventSubscriptionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_events"]
    ) -> DescribeEventsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_global_clusters"]
    ) -> DescribeGlobalClustersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_orderable_db_instance_options"]
    ) -> DescribeOrderableDBInstanceOptionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_pending_maintenance_actions"]
    ) -> DescribePendingMaintenanceActionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["db_instance_available"]
    ) -> DBInstanceAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["db_instance_deleted"]
    ) -> DBInstanceDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/client/#get_waiter)
        """
