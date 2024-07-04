"""
Type annotations for controlcatalog service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_controlcatalog import ControlCatalogClient

    client: ControlCatalogClient = boto3.client("controlcatalog")
    ```
"""

import sys
from typing import Any, Dict, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import ListCommonControlsPaginator, ListDomainsPaginator, ListObjectivesPaginator
from .type_defs import (
    CommonControlFilterTypeDef,
    ListCommonControlsResponseTypeDef,
    ListDomainsResponseTypeDef,
    ListObjectivesResponseTypeDef,
    ObjectiveFilterTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ControlCatalogClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ControlCatalogClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/controlcatalog.html#ControlCatalog.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ControlCatalogClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/controlcatalog.html#ControlCatalog.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/controlcatalog.html#ControlCatalog.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/client.html#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/controlcatalog.html#ControlCatalog.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/client.html#generate_presigned_url)
        """

    def list_common_controls(
        self,
        *,
        CommonControlFilter: "CommonControlFilterTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListCommonControlsResponseTypeDef:
        """
        Returns a paginated list of common controls from the Amazon Web Services Control
        Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/controlcatalog.html#ControlCatalog.Client.list_common_controls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/client.html#list_common_controls)
        """

    def list_domains(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListDomainsResponseTypeDef:
        """
        Returns a paginated list of domains from the Amazon Web Services Control
        Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/controlcatalog.html#ControlCatalog.Client.list_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/client.html#list_domains)
        """

    def list_objectives(
        self,
        *,
        MaxResults: int = None,
        NextToken: str = None,
        ObjectiveFilter: "ObjectiveFilterTypeDef" = None
    ) -> ListObjectivesResponseTypeDef:
        """
        Returns a paginated list of objectives from the Amazon Web Services Control
        Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/controlcatalog.html#ControlCatalog.Client.list_objectives)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/client.html#list_objectives)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_common_controls"]
    ) -> ListCommonControlsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/controlcatalog.html#ControlCatalog.Paginator.ListCommonControls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/paginators.html#listcommoncontrolspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_domains"]) -> ListDomainsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/controlcatalog.html#ControlCatalog.Paginator.ListDomains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/paginators.html#listdomainspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_objectives"]) -> ListObjectivesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/controlcatalog.html#ControlCatalog.Paginator.ListObjectives)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/paginators.html#listobjectivespaginator)
        """
