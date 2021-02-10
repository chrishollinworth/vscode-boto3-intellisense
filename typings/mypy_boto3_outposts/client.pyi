"""
Main interface for outposts service client

Usage::

    ```python
    import boto3
    from mypy_boto3_outposts import OutpostsClient

    client: OutpostsClient = boto3.client("outposts")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_outposts.type_defs import (
    CreateOutpostOutputTypeDef,
    GetOutpostInstanceTypesOutputTypeDef,
    GetOutpostOutputTypeDef,
    ListOutpostsOutputTypeDef,
    ListSitesOutputTypeDef,
    ListTagsForResourceResponseTypeDef,
)

__all__ = ("OutpostsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class OutpostsClient:
    """
    [Outposts.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/outposts.html#Outposts.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/outposts.html#Outposts.Client.can_paginate)
        """

    def create_outpost(
        self,
        Name: str,
        SiteId: str,
        Description: str = None,
        AvailabilityZone: str = None,
        AvailabilityZoneId: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateOutpostOutputTypeDef:
        """
        [Client.create_outpost documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/outposts.html#Outposts.Client.create_outpost)
        """

    def delete_outpost(self, OutpostId: str) -> Dict[str, Any]:
        """
        [Client.delete_outpost documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/outposts.html#Outposts.Client.delete_outpost)
        """

    def delete_site(self, SiteId: str) -> Dict[str, Any]:
        """
        [Client.delete_site documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/outposts.html#Outposts.Client.delete_site)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/outposts.html#Outposts.Client.generate_presigned_url)
        """

    def get_outpost(self, OutpostId: str) -> GetOutpostOutputTypeDef:
        """
        [Client.get_outpost documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/outposts.html#Outposts.Client.get_outpost)
        """

    def get_outpost_instance_types(
        self, OutpostId: str, NextToken: str = None, MaxResults: int = None
    ) -> GetOutpostInstanceTypesOutputTypeDef:
        """
        [Client.get_outpost_instance_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/outposts.html#Outposts.Client.get_outpost_instance_types)
        """

    def list_outposts(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListOutpostsOutputTypeDef:
        """
        [Client.list_outposts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/outposts.html#Outposts.Client.list_outposts)
        """

    def list_sites(self, NextToken: str = None, MaxResults: int = None) -> ListSitesOutputTypeDef:
        """
        [Client.list_sites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/outposts.html#Outposts.Client.list_sites)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/outposts.html#Outposts.Client.list_tags_for_resource)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/outposts.html#Outposts.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/outposts.html#Outposts.Client.untag_resource)
        """
