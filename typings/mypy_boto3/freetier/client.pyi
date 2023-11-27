"""
Type annotations for freetier service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_freetier/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_freetier import FreeTierClient

    client: FreeTierClient = boto3.client("freetier")
    ```
"""
import sys
from typing import Any, Dict, Type

from botocore.client import BaseClient, ClientMeta

from .paginator import GetFreeTierUsagePaginator
from .type_defs import ExpressionTypeDef, GetFreeTierUsageResponseTypeDef

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("FreeTierClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class FreeTierClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/freetier.html#FreeTier.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_freetier/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        FreeTierClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/freetier.html#FreeTier.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_freetier/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/freetier.html#FreeTier.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_freetier/client.html#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/freetier.html#FreeTier.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_freetier/client.html#generate_presigned_url)
        """
    def get_free_tier_usage(
        self, *, filter: "ExpressionTypeDef" = None, maxResults: int = None, nextToken: str = None
    ) -> GetFreeTierUsageResponseTypeDef:
        """
        Returns a list of all Free Tier usage objects that match your filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/freetier.html#FreeTier.Client.get_free_tier_usage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_freetier/client.html#get_free_tier_usage)
        """
    def get_paginator(
        self, operation_name: Literal["get_free_tier_usage"]
    ) -> GetFreeTierUsagePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/freetier.html#FreeTier.Paginator.GetFreeTierUsage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_freetier/paginators.html#getfreetierusagepaginator)
        """
