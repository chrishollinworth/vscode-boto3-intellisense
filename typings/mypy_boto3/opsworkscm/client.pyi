"""
Type annotations for opsworkscm service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_opsworkscm.client import OpsWorksCMClient

    session = Session()
    client: OpsWorksCMClient = session.client("opsworkscm")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeBackupsPaginator,
    DescribeEventsPaginator,
    DescribeServersPaginator,
    ListTagsForResourcePaginator,
)
from .type_defs import (
    AssociateNodeRequestTypeDef,
    AssociateNodeResponseTypeDef,
    CreateBackupRequestTypeDef,
    CreateBackupResponseTypeDef,
    CreateServerRequestTypeDef,
    CreateServerResponseTypeDef,
    DeleteBackupRequestTypeDef,
    DeleteServerRequestTypeDef,
    DescribeAccountAttributesResponseTypeDef,
    DescribeBackupsRequestTypeDef,
    DescribeBackupsResponseTypeDef,
    DescribeEventsRequestTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeNodeAssociationStatusRequestTypeDef,
    DescribeNodeAssociationStatusResponseTypeDef,
    DescribeServersRequestTypeDef,
    DescribeServersResponseTypeDef,
    DisassociateNodeRequestTypeDef,
    DisassociateNodeResponseTypeDef,
    ExportServerEngineAttributeRequestTypeDef,
    ExportServerEngineAttributeResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    RestoreServerRequestTypeDef,
    RestoreServerResponseTypeDef,
    StartMaintenanceRequestTypeDef,
    StartMaintenanceResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateServerEngineAttributesRequestTypeDef,
    UpdateServerEngineAttributesResponseTypeDef,
    UpdateServerRequestTypeDef,
    UpdateServerResponseTypeDef,
)
from .waiter import NodeAssociatedWaiter

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

__all__ = ("OpsWorksCMClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidStateException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class OpsWorksCMClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        OpsWorksCMClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#generate_presigned_url)
        """

    def associate_node(
        self, **kwargs: Unpack[AssociateNodeRequestTypeDef]
    ) -> AssociateNodeResponseTypeDef:
        """
        Associates a new node with the server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/associate_node.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#associate_node)
        """

    def create_backup(
        self, **kwargs: Unpack[CreateBackupRequestTypeDef]
    ) -> CreateBackupResponseTypeDef:
        """
        Creates an application-level backup of a server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/create_backup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#create_backup)
        """

    def create_server(
        self, **kwargs: Unpack[CreateServerRequestTypeDef]
    ) -> CreateServerResponseTypeDef:
        """
        Creates and immedately starts a new server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/create_server.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#create_server)
        """

    def delete_backup(self, **kwargs: Unpack[DeleteBackupRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/delete_backup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#delete_backup)
        """

    def delete_server(self, **kwargs: Unpack[DeleteServerRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the server and the underlying AWS CloudFormation stacks (including the
        server's EC2 instance).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/delete_server.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#delete_server)
        """

    def describe_account_attributes(self) -> DescribeAccountAttributesResponseTypeDef:
        """
        Describes your OpsWorks-CM account attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/describe_account_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#describe_account_attributes)
        """

    def describe_backups(
        self, **kwargs: Unpack[DescribeBackupsRequestTypeDef]
    ) -> DescribeBackupsResponseTypeDef:
        """
        Describes backups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/describe_backups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#describe_backups)
        """

    def describe_events(
        self, **kwargs: Unpack[DescribeEventsRequestTypeDef]
    ) -> DescribeEventsResponseTypeDef:
        """
        Describes events for a specified server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/describe_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#describe_events)
        """

    def describe_node_association_status(
        self, **kwargs: Unpack[DescribeNodeAssociationStatusRequestTypeDef]
    ) -> DescribeNodeAssociationStatusResponseTypeDef:
        """
        Returns the current status of an existing association or disassociation request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/describe_node_association_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#describe_node_association_status)
        """

    def describe_servers(
        self, **kwargs: Unpack[DescribeServersRequestTypeDef]
    ) -> DescribeServersResponseTypeDef:
        """
        Lists all configuration management servers that are identified with your
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/describe_servers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#describe_servers)
        """

    def disassociate_node(
        self, **kwargs: Unpack[DisassociateNodeRequestTypeDef]
    ) -> DisassociateNodeResponseTypeDef:
        """
        Disassociates a node from an AWS OpsWorks CM server, and removes the node from
        the server's managed nodes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/disassociate_node.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#disassociate_node)
        """

    def export_server_engine_attribute(
        self, **kwargs: Unpack[ExportServerEngineAttributeRequestTypeDef]
    ) -> ExportServerEngineAttributeResponseTypeDef:
        """
        Exports a specified server engine attribute as a base64-encoded string.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/export_server_engine_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#export_server_engine_attribute)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags that are applied to the specified AWS OpsWorks for Chef
        Automate or AWS OpsWorks for Puppet Enterprise servers or backups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#list_tags_for_resource)
        """

    def restore_server(
        self, **kwargs: Unpack[RestoreServerRequestTypeDef]
    ) -> RestoreServerResponseTypeDef:
        """
        Restores a backup to a server that is in a <code>CONNECTION_LOST</code>,
        <code>HEALTHY</code>, <code>RUNNING</code>, <code>UNHEALTHY</code>, or
        <code>TERMINATED</code> state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/restore_server.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#restore_server)
        """

    def start_maintenance(
        self, **kwargs: Unpack[StartMaintenanceRequestTypeDef]
    ) -> StartMaintenanceResponseTypeDef:
        """
        Manually starts server maintenance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/start_maintenance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#start_maintenance)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Applies tags to an AWS OpsWorks for Chef Automate or AWS OpsWorks for Puppet
        Enterprise server, or to server backups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes specified tags from an AWS OpsWorks-CM server or backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#untag_resource)
        """

    def update_server(
        self, **kwargs: Unpack[UpdateServerRequestTypeDef]
    ) -> UpdateServerResponseTypeDef:
        """
        Updates settings for a server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/update_server.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#update_server)
        """

    def update_server_engine_attributes(
        self, **kwargs: Unpack[UpdateServerEngineAttributesRequestTypeDef]
    ) -> UpdateServerEngineAttributesResponseTypeDef:
        """
        Updates engine-specific attributes on a specified server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/update_server_engine_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#update_server_engine_attributes)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_backups"]
    ) -> DescribeBackupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_events"]
    ) -> DescribeEventsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_servers"]
    ) -> DescribeServersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#get_paginator)
        """

    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["node_associated"]
    ) -> NodeAssociatedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client/#get_waiter)
        """
