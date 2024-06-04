"""
Type annotations for opsworkscm service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_opsworkscm import OpsWorksCMClient

    client: OpsWorksCMClient = boto3.client("opsworkscm")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    DescribeBackupsPaginator,
    DescribeEventsPaginator,
    DescribeServersPaginator,
    ListTagsForResourcePaginator,
)
from .type_defs import (
    AssociateNodeResponseTypeDef,
    CreateBackupResponseTypeDef,
    CreateServerResponseTypeDef,
    DescribeAccountAttributesResponseTypeDef,
    DescribeBackupsResponseTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeNodeAssociationStatusResponseTypeDef,
    DescribeServersResponseTypeDef,
    DisassociateNodeResponseTypeDef,
    EngineAttributeTypeDef,
    ExportServerEngineAttributeResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    RestoreServerResponseTypeDef,
    StartMaintenanceResponseTypeDef,
    TagTypeDef,
    UpdateServerEngineAttributesResponseTypeDef,
    UpdateServerResponseTypeDef,
)
from .waiter import NodeAssociatedWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("OpsWorksCMClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidStateException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class OpsWorksCMClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        OpsWorksCMClient exceptions.
        """

    def associate_node(
        self, *, ServerName: str, NodeName: str, EngineAttributes: List["EngineAttributeTypeDef"]
    ) -> AssociateNodeResponseTypeDef:
        """
        Associates a new node with the server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Client.associate_node)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client.html#associate_node)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client.html#close)
        """

    def create_backup(
        self, *, ServerName: str, Description: str = None, Tags: List["TagTypeDef"] = None
    ) -> CreateBackupResponseTypeDef:
        """
        Creates an application-level backup of a server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Client.create_backup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client.html#create_backup)
        """

    def create_server(
        self,
        *,
        Engine: str,
        ServerName: str,
        InstanceProfileArn: str,
        InstanceType: str,
        ServiceRoleArn: str,
        AssociatePublicIpAddress: bool = None,
        CustomDomain: str = None,
        CustomCertificate: str = None,
        CustomPrivateKey: str = None,
        DisableAutomatedBackup: bool = None,
        EngineModel: str = None,
        EngineVersion: str = None,
        EngineAttributes: List["EngineAttributeTypeDef"] = None,
        BackupRetentionCount: int = None,
        KeyPair: str = None,
        PreferredMaintenanceWindow: str = None,
        PreferredBackupWindow: str = None,
        SecurityGroupIds: List[str] = None,
        SubnetIds: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        BackupId: str = None
    ) -> CreateServerResponseTypeDef:
        """
        Creates and immedately starts a new server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Client.create_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client.html#create_server)
        """

    def delete_backup(self, *, BackupId: str) -> Dict[str, Any]:
        """
        Deletes a backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Client.delete_backup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client.html#delete_backup)
        """

    def delete_server(self, *, ServerName: str) -> Dict[str, Any]:
        """
        Deletes the server and the underlying AWS CloudFormation stacks (including the
        server's EC2 instance).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Client.delete_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client.html#delete_server)
        """

    def describe_account_attributes(self) -> DescribeAccountAttributesResponseTypeDef:
        """
        Describes your OpsWorks-CM account attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_account_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client.html#describe_account_attributes)
        """

    def describe_backups(
        self,
        *,
        BackupId: str = None,
        ServerName: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeBackupsResponseTypeDef:
        """
        Describes backups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_backups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client.html#describe_backups)
        """

    def describe_events(
        self, *, ServerName: str, NextToken: str = None, MaxResults: int = None
    ) -> DescribeEventsResponseTypeDef:
        """
        Describes events for a specified server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client.html#describe_events)
        """

    def describe_node_association_status(
        self, *, NodeAssociationStatusToken: str, ServerName: str
    ) -> DescribeNodeAssociationStatusResponseTypeDef:
        """
        Returns the current status of an existing association or disassociation request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_node_association_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client.html#describe_node_association_status)
        """

    def describe_servers(
        self, *, ServerName: str = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeServersResponseTypeDef:
        """
        Lists all configuration management servers that are identified with your
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_servers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client.html#describe_servers)
        """

    def disassociate_node(
        self,
        *,
        ServerName: str,
        NodeName: str,
        EngineAttributes: List["EngineAttributeTypeDef"] = None
    ) -> DisassociateNodeResponseTypeDef:
        """
        Disassociates a node from an AWS OpsWorks CM server, and removes the node from
        the server's managed nodes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Client.disassociate_node)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client.html#disassociate_node)
        """

    def export_server_engine_attribute(
        self,
        *,
        ExportAttributeName: str,
        ServerName: str,
        InputAttributes: List["EngineAttributeTypeDef"] = None
    ) -> ExportServerEngineAttributeResponseTypeDef:
        """
        Exports a specified server engine attribute as a base64-encoded string.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Client.export_server_engine_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client.html#export_server_engine_attribute)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client.html#generate_presigned_url)
        """

    def list_tags_for_resource(
        self, *, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags that are applied to the specified AWS OpsWorks for Chef
        Automate or AWS OpsWorks for Puppet Enterprise servers or backups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client.html#list_tags_for_resource)
        """

    def restore_server(
        self, *, BackupId: str, ServerName: str, InstanceType: str = None, KeyPair: str = None
    ) -> RestoreServerResponseTypeDef:
        """
        Restores a backup to a server that is in a `CONNECTION_LOST`, `HEALTHY`,
        `RUNNING`, `UNHEALTHY`, or `TERMINATED` state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Client.restore_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client.html#restore_server)
        """

    def start_maintenance(
        self, *, ServerName: str, EngineAttributes: List["EngineAttributeTypeDef"] = None
    ) -> StartMaintenanceResponseTypeDef:
        """
        Manually starts server maintenance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Client.start_maintenance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client.html#start_maintenance)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Applies tags to an AWS OpsWorks for Chef Automate or AWS OpsWorks for Puppet
        Enterprise server, or to server backups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes specified tags from an AWS OpsWorks-CM server or backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client.html#untag_resource)
        """

    def update_server(
        self,
        *,
        ServerName: str,
        DisableAutomatedBackup: bool = None,
        BackupRetentionCount: int = None,
        PreferredMaintenanceWindow: str = None,
        PreferredBackupWindow: str = None
    ) -> UpdateServerResponseTypeDef:
        """
        Updates settings for a server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Client.update_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client.html#update_server)
        """

    def update_server_engine_attributes(
        self, *, ServerName: str, AttributeName: str, AttributeValue: str = None
    ) -> UpdateServerEngineAttributesResponseTypeDef:
        """
        Updates engine-specific attributes on a specified server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Client.update_server_engine_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/client.html#update_server_engine_attributes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_backups"]
    ) -> DescribeBackupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeBackups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/paginators.html#describebackupspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_events"]) -> DescribeEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeEvents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/paginators.html#describeeventspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_servers"]
    ) -> DescribeServersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeServers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/paginators.html#describeserverspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Paginator.ListTagsForResource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/paginators.html#listtagsforresourcepaginator)
        """

    def get_waiter(self, waiter_name: Literal["node_associated"]) -> NodeAssociatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/opsworkscm.html#OpsWorksCM.Waiter.NodeAssociated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/waiters.html#nodeassociatedwaiter)
        """
