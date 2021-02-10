"""
Main interface for iotfleethub service client

Usage::

    ```python
    import boto3
    from mypy_boto3_iotfleethub import IoTFleetHubClient

    client: IoTFleetHubClient = boto3.client("iotfleethub")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_iotfleethub.paginator import ListApplicationsPaginator
from mypy_boto3_iotfleethub.type_defs import (
    CreateApplicationResponseTypeDef,
    DescribeApplicationResponseTypeDef,
    ListApplicationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IoTFleetHubClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]


class IoTFleetHubClient:
    """
    [IoTFleetHub.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotfleethub.html#IoTFleetHub.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotfleethub.html#IoTFleetHub.Client.can_paginate)
        """

    def create_application(
        self,
        applicationName: str,
        roleArn: str,
        applicationDescription: str = None,
        clientToken: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateApplicationResponseTypeDef:
        """
        [Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotfleethub.html#IoTFleetHub.Client.create_application)
        """

    def delete_application(self, applicationId: str, clientToken: str = None) -> Dict[str, Any]:
        """
        [Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotfleethub.html#IoTFleetHub.Client.delete_application)
        """

    def describe_application(self, applicationId: str) -> DescribeApplicationResponseTypeDef:
        """
        [Client.describe_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotfleethub.html#IoTFleetHub.Client.describe_application)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotfleethub.html#IoTFleetHub.Client.generate_presigned_url)
        """

    def list_applications(self, nextToken: str = None) -> ListApplicationsResponseTypeDef:
        """
        [Client.list_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotfleethub.html#IoTFleetHub.Client.list_applications)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotfleethub.html#IoTFleetHub.Client.list_tags_for_resource)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotfleethub.html#IoTFleetHub.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotfleethub.html#IoTFleetHub.Client.untag_resource)
        """

    def update_application(
        self,
        applicationId: str,
        applicationName: str = None,
        applicationDescription: str = None,
        clientToken: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotfleethub.html#IoTFleetHub.Client.update_application)
        """

    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        [Paginator.ListApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotfleethub.html#IoTFleetHub.Paginator.ListApplications)
        """
