# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for codestar-connections service client

Usage::

    ```python
    import boto3
    from mypy_boto3_codestar_connections import CodeStarconnectionsClient

    client: CodeStarconnectionsClient = boto3.client("codestar-connections")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_codestar_connections.type_defs import (
    CreateConnectionOutputTypeDef,
    CreateHostOutputTypeDef,
    GetConnectionOutputTypeDef,
    GetHostOutputTypeDef,
    ListConnectionsOutputTypeDef,
    ListHostsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    TagTypeDef,
    VpcConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CodeStarconnectionsClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]
    ResourceUnavailableException: Type[Boto3ClientError]


class CodeStarconnectionsClient:
    """
    [CodeStarconnections.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar-connections.html#CodeStarconnections.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar-connections.html#CodeStarconnections.Client.can_paginate)
        """

    def create_connection(
        self,
        ConnectionName: str,
        ProviderType: Literal["Bitbucket", "GitHubEnterpriseServer"] = None,
        Tags: List["TagTypeDef"] = None,
        HostArn: str = None,
    ) -> CreateConnectionOutputTypeDef:
        """
        [Client.create_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar-connections.html#CodeStarconnections.Client.create_connection)
        """

    def create_host(
        self,
        Name: str,
        ProviderType: Literal["Bitbucket", "GitHubEnterpriseServer"],
        ProviderEndpoint: str,
        VpcConfiguration: "VpcConfigurationTypeDef" = None,
    ) -> CreateHostOutputTypeDef:
        """
        [Client.create_host documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar-connections.html#CodeStarconnections.Client.create_host)
        """

    def delete_connection(self, ConnectionArn: str) -> Dict[str, Any]:
        """
        [Client.delete_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar-connections.html#CodeStarconnections.Client.delete_connection)
        """

    def delete_host(self, HostArn: str) -> Dict[str, Any]:
        """
        [Client.delete_host documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar-connections.html#CodeStarconnections.Client.delete_host)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar-connections.html#CodeStarconnections.Client.generate_presigned_url)
        """

    def get_connection(self, ConnectionArn: str) -> GetConnectionOutputTypeDef:
        """
        [Client.get_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar-connections.html#CodeStarconnections.Client.get_connection)
        """

    def get_host(self, HostArn: str) -> GetHostOutputTypeDef:
        """
        [Client.get_host documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar-connections.html#CodeStarconnections.Client.get_host)
        """

    def list_connections(
        self,
        ProviderTypeFilter: Literal["Bitbucket", "GitHubEnterpriseServer"] = None,
        HostArnFilter: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListConnectionsOutputTypeDef:
        """
        [Client.list_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar-connections.html#CodeStarconnections.Client.list_connections)
        """

    def list_hosts(self, MaxResults: int = None, NextToken: str = None) -> ListHostsOutputTypeDef:
        """
        [Client.list_hosts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar-connections.html#CodeStarconnections.Client.list_hosts)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar-connections.html#CodeStarconnections.Client.list_tags_for_resource)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar-connections.html#CodeStarconnections.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar-connections.html#CodeStarconnections.Client.untag_resource)
        """
