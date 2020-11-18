# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for lakeformation service client

Usage::

    ```python
    import boto3
    from mypy_boto3_lakeformation import LakeFormationClient

    client: LakeFormationClient = boto3.client("lakeformation")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_lakeformation.type_defs import (
    BatchGrantPermissionsResponseTypeDef,
    BatchPermissionsRequestEntryTypeDef,
    BatchRevokePermissionsResponseTypeDef,
    DataLakePrincipalTypeDef,
    DataLakeSettingsTypeDef,
    DescribeResourceResponseTypeDef,
    FilterConditionTypeDef,
    GetDataLakeSettingsResponseTypeDef,
    GetEffectivePermissionsForPathResponseTypeDef,
    ListPermissionsResponseTypeDef,
    ListResourcesResponseTypeDef,
    ResourceTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("LakeFormationClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AlreadyExistsException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    EntityNotFoundException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    OperationTimeoutException: Type[BotocoreClientError]


class LakeFormationClient:
    """
    [LakeFormation.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lakeformation.html#LakeFormation.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_grant_permissions(
        self, Entries: List["BatchPermissionsRequestEntryTypeDef"], CatalogId: str = None
    ) -> BatchGrantPermissionsResponseTypeDef:
        """
        [Client.batch_grant_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lakeformation.html#LakeFormation.Client.batch_grant_permissions)
        """

    def batch_revoke_permissions(
        self, Entries: List["BatchPermissionsRequestEntryTypeDef"], CatalogId: str = None
    ) -> BatchRevokePermissionsResponseTypeDef:
        """
        [Client.batch_revoke_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lakeformation.html#LakeFormation.Client.batch_revoke_permissions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lakeformation.html#LakeFormation.Client.can_paginate)
        """

    def deregister_resource(self, ResourceArn: str) -> Dict[str, Any]:
        """
        [Client.deregister_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lakeformation.html#LakeFormation.Client.deregister_resource)
        """

    def describe_resource(self, ResourceArn: str) -> DescribeResourceResponseTypeDef:
        """
        [Client.describe_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lakeformation.html#LakeFormation.Client.describe_resource)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lakeformation.html#LakeFormation.Client.generate_presigned_url)
        """

    def get_data_lake_settings(self, CatalogId: str = None) -> GetDataLakeSettingsResponseTypeDef:
        """
        [Client.get_data_lake_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lakeformation.html#LakeFormation.Client.get_data_lake_settings)
        """

    def get_effective_permissions_for_path(
        self, ResourceArn: str, CatalogId: str = None, NextToken: str = None, MaxResults: int = None
    ) -> GetEffectivePermissionsForPathResponseTypeDef:
        """
        [Client.get_effective_permissions_for_path documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lakeformation.html#LakeFormation.Client.get_effective_permissions_for_path)
        """

    def grant_permissions(
        self,
        Principal: "DataLakePrincipalTypeDef",
        Resource: "ResourceTypeDef",
        Permissions: List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "DESCRIBE",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
        CatalogId: str = None,
        PermissionsWithGrantOption: List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "DESCRIBE",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ] = None,
    ) -> Dict[str, Any]:
        """
        [Client.grant_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lakeformation.html#LakeFormation.Client.grant_permissions)
        """

    def list_permissions(
        self,
        CatalogId: str = None,
        Principal: "DataLakePrincipalTypeDef" = None,
        ResourceType: Literal["CATALOG", "DATABASE", "TABLE", "DATA_LOCATION"] = None,
        Resource: "ResourceTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListPermissionsResponseTypeDef:
        """
        [Client.list_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lakeformation.html#LakeFormation.Client.list_permissions)
        """

    def list_resources(
        self,
        FilterConditionList: List[FilterConditionTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListResourcesResponseTypeDef:
        """
        [Client.list_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lakeformation.html#LakeFormation.Client.list_resources)
        """

    def put_data_lake_settings(
        self, DataLakeSettings: "DataLakeSettingsTypeDef", CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.put_data_lake_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lakeformation.html#LakeFormation.Client.put_data_lake_settings)
        """

    def register_resource(
        self, ResourceArn: str, UseServiceLinkedRole: bool = None, RoleArn: str = None
    ) -> Dict[str, Any]:
        """
        [Client.register_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lakeformation.html#LakeFormation.Client.register_resource)
        """

    def revoke_permissions(
        self,
        Principal: "DataLakePrincipalTypeDef",
        Resource: "ResourceTypeDef",
        Permissions: List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "DESCRIBE",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
        CatalogId: str = None,
        PermissionsWithGrantOption: List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "DESCRIBE",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ] = None,
    ) -> Dict[str, Any]:
        """
        [Client.revoke_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lakeformation.html#LakeFormation.Client.revoke_permissions)
        """

    def update_resource(self, RoleArn: str, ResourceArn: str) -> Dict[str, Any]:
        """
        [Client.update_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lakeformation.html#LakeFormation.Client.update_resource)
        """
