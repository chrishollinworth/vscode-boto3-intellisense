"""
Type annotations for marketplace-deployment service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_deployment/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_marketplace_deployment import MarketplaceDeploymentServiceClient

    client: MarketplaceDeploymentServiceClient = boto3.client("marketplace-deployment")
    ```
"""

from datetime import datetime
from typing import Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    DeploymentParameterInputTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutDeploymentParameterResponseTypeDef,
)

__all__ = ("MarketplaceDeploymentServiceClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class MarketplaceDeploymentServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-deployment.html#MarketplaceDeploymentService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_deployment/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MarketplaceDeploymentServiceClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-deployment.html#MarketplaceDeploymentService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_deployment/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-deployment.html#MarketplaceDeploymentService.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_deployment/client.html#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-deployment.html#MarketplaceDeploymentService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_deployment/client.html#generate_presigned_url)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags that have been added to a deployment parameter resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-deployment.html#MarketplaceDeploymentService.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_deployment/client.html#list_tags_for_resource)
        """

    def put_deployment_parameter(
        self,
        *,
        agreementId: str,
        catalog: str,
        deploymentParameter: "DeploymentParameterInputTypeDef",
        productId: str,
        clientToken: str = None,
        expirationDate: Union[datetime, str] = None,
        tags: Dict[str, str] = None
    ) -> PutDeploymentParameterResponseTypeDef:
        """
        Creates or updates a deployment parameter and is targeted by `catalog` and
        `agreementId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-deployment.html#MarketplaceDeploymentService.Client.put_deployment_parameter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_deployment/client.html#put_deployment_parameter)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str] = None) -> Dict[str, Any]:
        """
        Tags a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-deployment.html#MarketplaceDeploymentService.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_deployment/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a tag or list of tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-deployment.html#MarketplaceDeploymentService.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_deployment/client.html#untag_resource)
        """
