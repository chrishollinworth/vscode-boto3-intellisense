"""
Type annotations for sdb service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_sdb.client import SimpleDBClient

    session = Session()
    client: SimpleDBClient = session.client("sdb")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListDomainsPaginator, SelectPaginator
from .type_defs import (
    BatchDeleteAttributesRequestTypeDef,
    BatchPutAttributesRequestTypeDef,
    CreateDomainRequestTypeDef,
    DeleteAttributesRequestTypeDef,
    DeleteDomainRequestTypeDef,
    DomainMetadataRequestTypeDef,
    DomainMetadataResultTypeDef,
    EmptyResponseMetadataTypeDef,
    GetAttributesRequestTypeDef,
    GetAttributesResultTypeDef,
    ListDomainsRequestTypeDef,
    ListDomainsResultTypeDef,
    PutAttributesRequestTypeDef,
    SelectRequestTypeDef,
    SelectResultTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("SimpleDBClient",)

class Exceptions(BaseClientExceptions):
    AttributeDoesNotExist: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DuplicateItemName: Type[BotocoreClientError]
    InvalidNextToken: Type[BotocoreClientError]
    InvalidNumberPredicates: Type[BotocoreClientError]
    InvalidNumberValueTests: Type[BotocoreClientError]
    InvalidParameterValue: Type[BotocoreClientError]
    InvalidQueryExpression: Type[BotocoreClientError]
    MissingParameter: Type[BotocoreClientError]
    NoSuchDomain: Type[BotocoreClientError]
    NumberDomainAttributesExceeded: Type[BotocoreClientError]
    NumberDomainBytesExceeded: Type[BotocoreClientError]
    NumberDomainsExceeded: Type[BotocoreClientError]
    NumberItemAttributesExceeded: Type[BotocoreClientError]
    NumberSubmittedAttributesExceeded: Type[BotocoreClientError]
    NumberSubmittedItemsExceeded: Type[BotocoreClientError]
    RequestTimeout: Type[BotocoreClientError]
    TooManyRequestedAttributes: Type[BotocoreClientError]

class SimpleDBClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb.html#SimpleDB.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SimpleDBClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb.html#SimpleDB.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#generate_presigned_url)
        """

    def batch_delete_attributes(
        self, **kwargs: Unpack[BatchDeleteAttributesRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Performs multiple DeleteAttributes operations in a single call, which reduces
        round trips and latencies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/batch_delete_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#batch_delete_attributes)
        """

    def batch_put_attributes(
        self, **kwargs: Unpack[BatchPutAttributesRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        The <code>BatchPutAttributes</code> operation creates or replaces attributes
        within one or more items.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/batch_put_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#batch_put_attributes)
        """

    def create_domain(
        self, **kwargs: Unpack[CreateDomainRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        The <code>CreateDomain</code> operation creates a new domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/create_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#create_domain)
        """

    def delete_attributes(
        self, **kwargs: Unpack[DeleteAttributesRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes one or more attributes associated with an item.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/delete_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#delete_attributes)
        """

    def delete_domain(
        self, **kwargs: Unpack[DeleteDomainRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        The <code>DeleteDomain</code> operation deletes a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/delete_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#delete_domain)
        """

    def domain_metadata(
        self, **kwargs: Unpack[DomainMetadataRequestTypeDef]
    ) -> DomainMetadataResultTypeDef:
        """
        Returns information about the domain, including when the domain was created,
        the number of items and attributes in the domain, and the size of the attribute
        names and values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/domain_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#domain_metadata)
        """

    def get_attributes(
        self, **kwargs: Unpack[GetAttributesRequestTypeDef]
    ) -> GetAttributesResultTypeDef:
        """
        Returns all of the attributes associated with the specified item.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/get_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#get_attributes)
        """

    def list_domains(self, **kwargs: Unpack[ListDomainsRequestTypeDef]) -> ListDomainsResultTypeDef:
        """
        The <code>ListDomains</code> operation lists all domains associated with the
        Access Key ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/list_domains.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#list_domains)
        """

    def put_attributes(
        self, **kwargs: Unpack[PutAttributesRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        The PutAttributes operation creates or replaces attributes in an item.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/put_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#put_attributes)
        """

    def select(self, **kwargs: Unpack[SelectRequestTypeDef]) -> SelectResultTypeDef:
        """
        The <code>Select</code> operation returns a set of attributes for
        <code>ItemNames</code> that match the select expression.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/select.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#select)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_domains"]
    ) -> ListDomainsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["select"]
    ) -> SelectPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/client/#get_paginator)
        """
