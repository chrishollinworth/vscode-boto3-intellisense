# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for opsworkscm service client

Usage::

    ```python
    import boto3
    from mypy_boto3_opsworkscm import OpsWorksCMClient

    client: OpsWorksCMClient = boto3.client("opsworkscm")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_opsworkscm.paginator import (
    DescribeBackupsPaginator,
    DescribeEventsPaginator,
    DescribeServersPaginator,
    ListTagsForResourcePaginator,
)
from mypy_boto3_opsworkscm.type_defs import (
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
    StartMaintenanceResponseTypeDef,
    TagTypeDef,
    UpdateServerEngineAttributesResponseTypeDef,
    UpdateServerResponseTypeDef,
)
from mypy_boto3_opsworkscm.waiter import NodeAssociatedWaiter

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


class OpsWorksCMClient:
    """
    [OpsWorksCM.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_node(
        self, ServerName: str, NodeName: str, EngineAttributes: List["EngineAttributeTypeDef"]
    ) -> AssociateNodeResponseTypeDef:
        """
        [Client.associate_node documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Client.associate_node)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Client.can_paginate)
        """

    def create_backup(
        self, ServerName: str, Description: str = None, Tags: List["TagTypeDef"] = None
    ) -> CreateBackupResponseTypeDef:
        """
        [Client.create_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Client.create_backup)
        """

    def create_server(
        self,
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
        BackupId: str = None,
    ) -> CreateServerResponseTypeDef:
        """
        [Client.create_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Client.create_server)
        """

    def delete_backup(self, BackupId: str) -> Dict[str, Any]:
        """
        [Client.delete_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Client.delete_backup)
        """

    def delete_server(self, ServerName: str) -> Dict[str, Any]:
        """
        [Client.delete_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Client.delete_server)
        """

    def describe_account_attributes(self) -> DescribeAccountAttributesResponseTypeDef:
        """
        [Client.describe_account_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_account_attributes)
        """

    def describe_backups(
        self,
        BackupId: str = None,
        ServerName: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeBackupsResponseTypeDef:
        """
        [Client.describe_backups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_backups)
        """

    def describe_events(
        self, ServerName: str, NextToken: str = None, MaxResults: int = None
    ) -> DescribeEventsResponseTypeDef:
        """
        [Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_events)
        """

    def describe_node_association_status(
        self, NodeAssociationStatusToken: str, ServerName: str
    ) -> DescribeNodeAssociationStatusResponseTypeDef:
        """
        [Client.describe_node_association_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_node_association_status)
        """

    def describe_servers(
        self, ServerName: str = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeServersResponseTypeDef:
        """
        [Client.describe_servers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_servers)
        """

    def disassociate_node(
        self,
        ServerName: str,
        NodeName: str,
        EngineAttributes: List["EngineAttributeTypeDef"] = None,
    ) -> DisassociateNodeResponseTypeDef:
        """
        [Client.disassociate_node documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Client.disassociate_node)
        """

    def export_server_engine_attribute(
        self,
        ExportAttributeName: str,
        ServerName: str,
        InputAttributes: List["EngineAttributeTypeDef"] = None,
    ) -> ExportServerEngineAttributeResponseTypeDef:
        """
        [Client.export_server_engine_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Client.export_server_engine_attribute)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Client.generate_presigned_url)
        """

    def list_tags_for_resource(
        self, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Client.list_tags_for_resource)
        """

    def restore_server(
        self, BackupId: str, ServerName: str, InstanceType: str = None, KeyPair: str = None
    ) -> Dict[str, Any]:
        """
        [Client.restore_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Client.restore_server)
        """

    def start_maintenance(
        self, ServerName: str, EngineAttributes: List["EngineAttributeTypeDef"] = None
    ) -> StartMaintenanceResponseTypeDef:
        """
        [Client.start_maintenance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Client.start_maintenance)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Client.untag_resource)
        """

    def update_server(
        self,
        ServerName: str,
        DisableAutomatedBackup: bool = None,
        BackupRetentionCount: int = None,
        PreferredMaintenanceWindow: str = None,
        PreferredBackupWindow: str = None,
    ) -> UpdateServerResponseTypeDef:
        """
        [Client.update_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Client.update_server)
        """

    def update_server_engine_attributes(
        self, ServerName: str, AttributeName: str, AttributeValue: str = None
    ) -> UpdateServerEngineAttributesResponseTypeDef:
        """
        [Client.update_server_engine_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Client.update_server_engine_attributes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_backups"]
    ) -> DescribeBackupsPaginator:
        """
        [Paginator.DescribeBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeBackups)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_events"]) -> DescribeEventsPaginator:
        """
        [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeEvents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_servers"]
    ) -> DescribeServersPaginator:
        """
        [Paginator.DescribeServers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeServers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Paginator.ListTagsForResource)
        """

    def get_waiter(self, waiter_name: Literal["node_associated"]) -> NodeAssociatedWaiter:
        """
        [Waiter.NodeAssociated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Waiter.NodeAssociated)
        """
