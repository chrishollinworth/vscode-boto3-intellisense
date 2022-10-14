"""
Type annotations for sdb service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_sdb import SimpleDBClient

    client: SimpleDBClient = boto3.client("sdb")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import ListDomainsPaginator, SelectPaginator
from .type_defs import (
    AttributeTypeDef,
    DeletableItemTypeDef,
    DomainMetadataResultTypeDef,
    GetAttributesResultTypeDef,
    ListDomainsResultTypeDef,
    ReplaceableAttributeTypeDef,
    ReplaceableItemTypeDef,
    SelectResultTypeDef,
    UpdateConditionTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("SimpleDBClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sdb.html#SimpleDB.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SimpleDBClient exceptions.
        """
    def batch_delete_attributes(
        self, *, DomainName: str, Items: List["DeletableItemTypeDef"]
    ) -> None:
        """
        Performs multiple DeleteAttributes operations in a single call, which reduces
        round trips and latencies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sdb.html#SimpleDB.Client.batch_delete_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/client.html#batch_delete_attributes)
        """
    def batch_put_attributes(
        self, *, DomainName: str, Items: List["ReplaceableItemTypeDef"]
    ) -> None:
        """
        The `BatchPutAttributes` operation creates or replaces attributes within one or
        more items.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sdb.html#SimpleDB.Client.batch_put_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/client.html#batch_put_attributes)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sdb.html#SimpleDB.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sdb.html#SimpleDB.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/client.html#close)
        """
    def create_domain(self, *, DomainName: str) -> None:
        """
        The `CreateDomain` operation creates a new domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sdb.html#SimpleDB.Client.create_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/client.html#create_domain)
        """
    def delete_attributes(
        self,
        *,
        DomainName: str,
        ItemName: str,
        Attributes: List["AttributeTypeDef"] = None,
        Expected: "UpdateConditionTypeDef" = None
    ) -> None:
        """
        Deletes one or more attributes associated with an item.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sdb.html#SimpleDB.Client.delete_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/client.html#delete_attributes)
        """
    def delete_domain(self, *, DomainName: str) -> None:
        """
        The `DeleteDomain` operation deletes a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sdb.html#SimpleDB.Client.delete_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/client.html#delete_domain)
        """
    def domain_metadata(self, *, DomainName: str) -> DomainMetadataResultTypeDef:
        """
        Returns information about the domain, including when the domain was created, the
        number of items and attributes in the domain, and the size of the attribute
        names and values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sdb.html#SimpleDB.Client.domain_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/client.html#domain_metadata)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sdb.html#SimpleDB.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/client.html#generate_presigned_url)
        """
    def get_attributes(
        self,
        *,
        DomainName: str,
        ItemName: str,
        AttributeNames: List[str] = None,
        ConsistentRead: bool = None
    ) -> GetAttributesResultTypeDef:
        """
        Returns all of the attributes associated with the specified item.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sdb.html#SimpleDB.Client.get_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/client.html#get_attributes)
        """
    def list_domains(
        self, *, MaxNumberOfDomains: int = None, NextToken: str = None
    ) -> ListDomainsResultTypeDef:
        """
        The `ListDomains` operation lists all domains associated with the Access Key ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sdb.html#SimpleDB.Client.list_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/client.html#list_domains)
        """
    def put_attributes(
        self,
        *,
        DomainName: str,
        ItemName: str,
        Attributes: List["ReplaceableAttributeTypeDef"],
        Expected: "UpdateConditionTypeDef" = None
    ) -> None:
        """
        The PutAttributes operation creates or replaces attributes in an item.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sdb.html#SimpleDB.Client.put_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/client.html#put_attributes)
        """
    def select(
        self, *, SelectExpression: str, NextToken: str = None, ConsistentRead: bool = None
    ) -> SelectResultTypeDef:
        """
        The `Select` operation returns a set of attributes for `ItemNames` that match
        the select expression.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sdb.html#SimpleDB.Client.select)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/client.html#select)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_domains"]) -> ListDomainsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sdb.html#SimpleDB.Paginator.ListDomains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/paginators.html#listdomainspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["select"]) -> SelectPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sdb.html#SimpleDB.Paginator.Select)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/paginators.html#selectpaginator)
        """
