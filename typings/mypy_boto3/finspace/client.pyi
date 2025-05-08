"""
Type annotations for finspace service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_finspace.client import FinspaceClient

    session = Session()
    client: FinspaceClient = session.client("finspace")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListKxEnvironmentsPaginator
from .type_defs import (
    CreateEnvironmentRequestTypeDef,
    CreateEnvironmentResponseTypeDef,
    CreateKxChangesetRequestTypeDef,
    CreateKxChangesetResponseTypeDef,
    CreateKxClusterRequestTypeDef,
    CreateKxClusterResponseTypeDef,
    CreateKxDatabaseRequestTypeDef,
    CreateKxDatabaseResponseTypeDef,
    CreateKxDataviewRequestTypeDef,
    CreateKxDataviewResponseTypeDef,
    CreateKxEnvironmentRequestTypeDef,
    CreateKxEnvironmentResponseTypeDef,
    CreateKxScalingGroupRequestTypeDef,
    CreateKxScalingGroupResponseTypeDef,
    CreateKxUserRequestTypeDef,
    CreateKxUserResponseTypeDef,
    CreateKxVolumeRequestTypeDef,
    CreateKxVolumeResponseTypeDef,
    DeleteEnvironmentRequestTypeDef,
    DeleteKxClusterNodeRequestTypeDef,
    DeleteKxClusterRequestTypeDef,
    DeleteKxDatabaseRequestTypeDef,
    DeleteKxDataviewRequestTypeDef,
    DeleteKxEnvironmentRequestTypeDef,
    DeleteKxScalingGroupRequestTypeDef,
    DeleteKxUserRequestTypeDef,
    DeleteKxVolumeRequestTypeDef,
    GetEnvironmentRequestTypeDef,
    GetEnvironmentResponseTypeDef,
    GetKxChangesetRequestTypeDef,
    GetKxChangesetResponseTypeDef,
    GetKxClusterRequestTypeDef,
    GetKxClusterResponseTypeDef,
    GetKxConnectionStringRequestTypeDef,
    GetKxConnectionStringResponseTypeDef,
    GetKxDatabaseRequestTypeDef,
    GetKxDatabaseResponseTypeDef,
    GetKxDataviewRequestTypeDef,
    GetKxDataviewResponseTypeDef,
    GetKxEnvironmentRequestTypeDef,
    GetKxEnvironmentResponseTypeDef,
    GetKxScalingGroupRequestTypeDef,
    GetKxScalingGroupResponseTypeDef,
    GetKxUserRequestTypeDef,
    GetKxUserResponseTypeDef,
    GetKxVolumeRequestTypeDef,
    GetKxVolumeResponseTypeDef,
    ListEnvironmentsRequestTypeDef,
    ListEnvironmentsResponseTypeDef,
    ListKxChangesetsRequestTypeDef,
    ListKxChangesetsResponseTypeDef,
    ListKxClusterNodesRequestTypeDef,
    ListKxClusterNodesResponseTypeDef,
    ListKxClustersRequestTypeDef,
    ListKxClustersResponseTypeDef,
    ListKxDatabasesRequestTypeDef,
    ListKxDatabasesResponseTypeDef,
    ListKxDataviewsRequestTypeDef,
    ListKxDataviewsResponseTypeDef,
    ListKxEnvironmentsRequestTypeDef,
    ListKxEnvironmentsResponseTypeDef,
    ListKxScalingGroupsRequestTypeDef,
    ListKxScalingGroupsResponseTypeDef,
    ListKxUsersRequestTypeDef,
    ListKxUsersResponseTypeDef,
    ListKxVolumesRequestTypeDef,
    ListKxVolumesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateEnvironmentRequestTypeDef,
    UpdateEnvironmentResponseTypeDef,
    UpdateKxClusterCodeConfigurationRequestTypeDef,
    UpdateKxClusterDatabasesRequestTypeDef,
    UpdateKxDatabaseRequestTypeDef,
    UpdateKxDatabaseResponseTypeDef,
    UpdateKxDataviewRequestTypeDef,
    UpdateKxDataviewResponseTypeDef,
    UpdateKxEnvironmentNetworkRequestTypeDef,
    UpdateKxEnvironmentNetworkResponseTypeDef,
    UpdateKxEnvironmentRequestTypeDef,
    UpdateKxEnvironmentResponseTypeDef,
    UpdateKxUserRequestTypeDef,
    UpdateKxUserResponseTypeDef,
    UpdateKxVolumeRequestTypeDef,
    UpdateKxVolumeResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("FinspaceClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class FinspaceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#Finspace.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        FinspaceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html#Finspace.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#generate_presigned_url)
        """

    def create_environment(
        self, **kwargs: Unpack[CreateEnvironmentRequestTypeDef]
    ) -> CreateEnvironmentResponseTypeDef:
        """
        Create a new FinSpace environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/create_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#create_environment)
        """

    def create_kx_changeset(
        self, **kwargs: Unpack[CreateKxChangesetRequestTypeDef]
    ) -> CreateKxChangesetResponseTypeDef:
        """
        Creates a changeset for a kdb database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/create_kx_changeset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#create_kx_changeset)
        """

    def create_kx_cluster(
        self, **kwargs: Unpack[CreateKxClusterRequestTypeDef]
    ) -> CreateKxClusterResponseTypeDef:
        """
        Creates a new kdb cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/create_kx_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#create_kx_cluster)
        """

    def create_kx_database(
        self, **kwargs: Unpack[CreateKxDatabaseRequestTypeDef]
    ) -> CreateKxDatabaseResponseTypeDef:
        """
        Creates a new kdb database in the environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/create_kx_database.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#create_kx_database)
        """

    def create_kx_dataview(
        self, **kwargs: Unpack[CreateKxDataviewRequestTypeDef]
    ) -> CreateKxDataviewResponseTypeDef:
        """
        Creates a snapshot of kdb database with tiered storage capabilities and a
        pre-warmed cache, ready for mounting on kdb clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/create_kx_dataview.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#create_kx_dataview)
        """

    def create_kx_environment(
        self, **kwargs: Unpack[CreateKxEnvironmentRequestTypeDef]
    ) -> CreateKxEnvironmentResponseTypeDef:
        """
        Creates a managed kdb environment for the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/create_kx_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#create_kx_environment)
        """

    def create_kx_scaling_group(
        self, **kwargs: Unpack[CreateKxScalingGroupRequestTypeDef]
    ) -> CreateKxScalingGroupResponseTypeDef:
        """
        Creates a new scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/create_kx_scaling_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#create_kx_scaling_group)
        """

    def create_kx_user(
        self, **kwargs: Unpack[CreateKxUserRequestTypeDef]
    ) -> CreateKxUserResponseTypeDef:
        """
        Creates a user in FinSpace kdb environment with an associated IAM role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/create_kx_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#create_kx_user)
        """

    def create_kx_volume(
        self, **kwargs: Unpack[CreateKxVolumeRequestTypeDef]
    ) -> CreateKxVolumeResponseTypeDef:
        """
        Creates a new volume with a specific amount of throughput and storage capacity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/create_kx_volume.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#create_kx_volume)
        """

    def delete_environment(
        self, **kwargs: Unpack[DeleteEnvironmentRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete an FinSpace environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/delete_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#delete_environment)
        """

    def delete_kx_cluster(self, **kwargs: Unpack[DeleteKxClusterRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a kdb cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/delete_kx_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#delete_kx_cluster)
        """

    def delete_kx_cluster_node(
        self, **kwargs: Unpack[DeleteKxClusterNodeRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified nodes from a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/delete_kx_cluster_node.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#delete_kx_cluster_node)
        """

    def delete_kx_database(
        self, **kwargs: Unpack[DeleteKxDatabaseRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified database and all of its associated data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/delete_kx_database.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#delete_kx_database)
        """

    def delete_kx_dataview(
        self, **kwargs: Unpack[DeleteKxDataviewRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified dataview.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/delete_kx_dataview.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#delete_kx_dataview)
        """

    def delete_kx_environment(
        self, **kwargs: Unpack[DeleteKxEnvironmentRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the kdb environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/delete_kx_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#delete_kx_environment)
        """

    def delete_kx_scaling_group(
        self, **kwargs: Unpack[DeleteKxScalingGroupRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/delete_kx_scaling_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#delete_kx_scaling_group)
        """

    def delete_kx_user(self, **kwargs: Unpack[DeleteKxUserRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a user in the specified kdb environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/delete_kx_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#delete_kx_user)
        """

    def delete_kx_volume(self, **kwargs: Unpack[DeleteKxVolumeRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/delete_kx_volume.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#delete_kx_volume)
        """

    def get_environment(
        self, **kwargs: Unpack[GetEnvironmentRequestTypeDef]
    ) -> GetEnvironmentResponseTypeDef:
        """
        Returns the FinSpace environment object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/get_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#get_environment)
        """

    def get_kx_changeset(
        self, **kwargs: Unpack[GetKxChangesetRequestTypeDef]
    ) -> GetKxChangesetResponseTypeDef:
        """
        Returns information about a kdb changeset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/get_kx_changeset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#get_kx_changeset)
        """

    def get_kx_cluster(
        self, **kwargs: Unpack[GetKxClusterRequestTypeDef]
    ) -> GetKxClusterResponseTypeDef:
        """
        Retrieves information about a kdb cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/get_kx_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#get_kx_cluster)
        """

    def get_kx_connection_string(
        self, **kwargs: Unpack[GetKxConnectionStringRequestTypeDef]
    ) -> GetKxConnectionStringResponseTypeDef:
        """
        Retrieves a connection string for a user to connect to a kdb cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/get_kx_connection_string.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#get_kx_connection_string)
        """

    def get_kx_database(
        self, **kwargs: Unpack[GetKxDatabaseRequestTypeDef]
    ) -> GetKxDatabaseResponseTypeDef:
        """
        Returns database information for the specified environment ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/get_kx_database.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#get_kx_database)
        """

    def get_kx_dataview(
        self, **kwargs: Unpack[GetKxDataviewRequestTypeDef]
    ) -> GetKxDataviewResponseTypeDef:
        """
        Retrieves details of the dataview.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/get_kx_dataview.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#get_kx_dataview)
        """

    def get_kx_environment(
        self, **kwargs: Unpack[GetKxEnvironmentRequestTypeDef]
    ) -> GetKxEnvironmentResponseTypeDef:
        """
        Retrieves all the information for the specified kdb environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/get_kx_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#get_kx_environment)
        """

    def get_kx_scaling_group(
        self, **kwargs: Unpack[GetKxScalingGroupRequestTypeDef]
    ) -> GetKxScalingGroupResponseTypeDef:
        """
        Retrieves details of a scaling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/get_kx_scaling_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#get_kx_scaling_group)
        """

    def get_kx_user(self, **kwargs: Unpack[GetKxUserRequestTypeDef]) -> GetKxUserResponseTypeDef:
        """
        Retrieves information about the specified kdb user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/get_kx_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#get_kx_user)
        """

    def get_kx_volume(
        self, **kwargs: Unpack[GetKxVolumeRequestTypeDef]
    ) -> GetKxVolumeResponseTypeDef:
        """
        Retrieves the information about the volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/get_kx_volume.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#get_kx_volume)
        """

    def list_environments(
        self, **kwargs: Unpack[ListEnvironmentsRequestTypeDef]
    ) -> ListEnvironmentsResponseTypeDef:
        """
        A list of all of your FinSpace environments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/list_environments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#list_environments)
        """

    def list_kx_changesets(
        self, **kwargs: Unpack[ListKxChangesetsRequestTypeDef]
    ) -> ListKxChangesetsResponseTypeDef:
        """
        Returns a list of all the changesets for a database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/list_kx_changesets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#list_kx_changesets)
        """

    def list_kx_cluster_nodes(
        self, **kwargs: Unpack[ListKxClusterNodesRequestTypeDef]
    ) -> ListKxClusterNodesResponseTypeDef:
        """
        Lists all the nodes in a kdb cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/list_kx_cluster_nodes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#list_kx_cluster_nodes)
        """

    def list_kx_clusters(
        self, **kwargs: Unpack[ListKxClustersRequestTypeDef]
    ) -> ListKxClustersResponseTypeDef:
        """
        Returns a list of clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/list_kx_clusters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#list_kx_clusters)
        """

    def list_kx_databases(
        self, **kwargs: Unpack[ListKxDatabasesRequestTypeDef]
    ) -> ListKxDatabasesResponseTypeDef:
        """
        Returns a list of all the databases in the kdb environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/list_kx_databases.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#list_kx_databases)
        """

    def list_kx_dataviews(
        self, **kwargs: Unpack[ListKxDataviewsRequestTypeDef]
    ) -> ListKxDataviewsResponseTypeDef:
        """
        Returns a list of all the dataviews in the database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/list_kx_dataviews.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#list_kx_dataviews)
        """

    def list_kx_environments(
        self, **kwargs: Unpack[ListKxEnvironmentsRequestTypeDef]
    ) -> ListKxEnvironmentsResponseTypeDef:
        """
        Returns a list of kdb environments created in an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/list_kx_environments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#list_kx_environments)
        """

    def list_kx_scaling_groups(
        self, **kwargs: Unpack[ListKxScalingGroupsRequestTypeDef]
    ) -> ListKxScalingGroupsResponseTypeDef:
        """
        Returns a list of scaling groups in a kdb environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/list_kx_scaling_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#list_kx_scaling_groups)
        """

    def list_kx_users(
        self, **kwargs: Unpack[ListKxUsersRequestTypeDef]
    ) -> ListKxUsersResponseTypeDef:
        """
        Lists all the users in a kdb environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/list_kx_users.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#list_kx_users)
        """

    def list_kx_volumes(
        self, **kwargs: Unpack[ListKxVolumesRequestTypeDef]
    ) -> ListKxVolumesResponseTypeDef:
        """
        Lists all the volumes in a kdb environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/list_kx_volumes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#list_kx_volumes)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        A list of all tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#list_tags_for_resource)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds metadata tags to a FinSpace resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes metadata tags from a FinSpace resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#untag_resource)
        """

    def update_environment(
        self, **kwargs: Unpack[UpdateEnvironmentRequestTypeDef]
    ) -> UpdateEnvironmentResponseTypeDef:
        """
        Update your FinSpace environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/update_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#update_environment)
        """

    def update_kx_cluster_code_configuration(
        self, **kwargs: Unpack[UpdateKxClusterCodeConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Allows you to update code configuration on a running cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/update_kx_cluster_code_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#update_kx_cluster_code_configuration)
        """

    def update_kx_cluster_databases(
        self, **kwargs: Unpack[UpdateKxClusterDatabasesRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the databases mounted on a kdb cluster, which includes the
        <code>changesetId</code> and all the dbPaths to be cached.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/update_kx_cluster_databases.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#update_kx_cluster_databases)
        """

    def update_kx_database(
        self, **kwargs: Unpack[UpdateKxDatabaseRequestTypeDef]
    ) -> UpdateKxDatabaseResponseTypeDef:
        """
        Updates information for the given kdb database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/update_kx_database.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#update_kx_database)
        """

    def update_kx_dataview(
        self, **kwargs: Unpack[UpdateKxDataviewRequestTypeDef]
    ) -> UpdateKxDataviewResponseTypeDef:
        """
        Updates the specified dataview.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/update_kx_dataview.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#update_kx_dataview)
        """

    def update_kx_environment(
        self, **kwargs: Unpack[UpdateKxEnvironmentRequestTypeDef]
    ) -> UpdateKxEnvironmentResponseTypeDef:
        """
        Updates information for the given kdb environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/update_kx_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#update_kx_environment)
        """

    def update_kx_environment_network(
        self, **kwargs: Unpack[UpdateKxEnvironmentNetworkRequestTypeDef]
    ) -> UpdateKxEnvironmentNetworkResponseTypeDef:
        """
        Updates environment network to connect to your internal network by using a
        transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/update_kx_environment_network.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#update_kx_environment_network)
        """

    def update_kx_user(
        self, **kwargs: Unpack[UpdateKxUserRequestTypeDef]
    ) -> UpdateKxUserResponseTypeDef:
        """
        Updates the user details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/update_kx_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#update_kx_user)
        """

    def update_kx_volume(
        self, **kwargs: Unpack[UpdateKxVolumeRequestTypeDef]
    ) -> UpdateKxVolumeResponseTypeDef:
        """
        Updates the throughput or capacity of a volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/update_kx_volume.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#update_kx_volume)
        """

    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_kx_environments"]
    ) -> ListKxEnvironmentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/client/#get_paginator)
        """
