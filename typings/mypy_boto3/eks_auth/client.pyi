"""
Type annotations for eks-auth service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks_auth/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_eks_auth import EKSAuthClient

    client: EKSAuthClient = boto3.client("eks-auth")
    ```
"""

from typing import Any, Dict, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import AssumeRoleForPodIdentityResponseTypeDef

__all__ = ("EKSAuthClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ExpiredTokenException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    InvalidTokenException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]

class EKSAuthClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks-auth.html#EKSAuth.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks_auth/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        EKSAuthClient exceptions.
        """

    def assume_role_for_pod_identity(
        self, *, clusterName: str, token: str
    ) -> AssumeRoleForPodIdentityResponseTypeDef:
        """
        The Amazon EKS Auth API and the `AssumeRoleForPodIdentity` action are only used
        by the EKS Pod Identity Agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks-auth.html#EKSAuth.Client.assume_role_for_pod_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks_auth/client.html#assume_role_for_pod_identity)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks-auth.html#EKSAuth.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks_auth/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks-auth.html#EKSAuth.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks_auth/client.html#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks-auth.html#EKSAuth.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks_auth/client.html#generate_presigned_url)
        """
