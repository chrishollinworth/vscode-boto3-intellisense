# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for sdb service client

Usage::

    ```python
    import boto3
    from mypy_boto3_sdb import SimpleDBClient

    client: SimpleDBClient = boto3.client("sdb")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_sdb.paginator import ListDomainsPaginator, SelectPaginator
from mypy_boto3_sdb.type_defs import (
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


class Exceptions:
    AttributeDoesNotExist: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    DuplicateItemName: Type[Boto3ClientError]
    InvalidNextToken: Type[Boto3ClientError]
    InvalidNumberPredicates: Type[Boto3ClientError]
    InvalidNumberValueTests: Type[Boto3ClientError]
    InvalidParameterValue: Type[Boto3ClientError]
    InvalidQueryExpression: Type[Boto3ClientError]
    MissingParameter: Type[Boto3ClientError]
    NoSuchDomain: Type[Boto3ClientError]
    NumberDomainAttributesExceeded: Type[Boto3ClientError]
    NumberDomainBytesExceeded: Type[Boto3ClientError]
    NumberDomainsExceeded: Type[Boto3ClientError]
    NumberItemAttributesExceeded: Type[Boto3ClientError]
    NumberSubmittedAttributesExceeded: Type[Boto3ClientError]
    NumberSubmittedItemsExceeded: Type[Boto3ClientError]
    RequestTimeout: Type[Boto3ClientError]
    TooManyRequestedAttributes: Type[Boto3ClientError]


class SimpleDBClient:
    """
    [SimpleDB.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sdb.html#SimpleDB.Client)
    """

    exceptions: Exceptions

    def batch_delete_attributes(self, DomainName: str, Items: List[DeletableItemTypeDef]) -> None:
        """
        [Client.batch_delete_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sdb.html#SimpleDB.Client.batch_delete_attributes)
        """

    def batch_put_attributes(self, DomainName: str, Items: List[ReplaceableItemTypeDef]) -> None:
        """
        [Client.batch_put_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sdb.html#SimpleDB.Client.batch_put_attributes)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sdb.html#SimpleDB.Client.can_paginate)
        """

    def create_domain(self, DomainName: str) -> None:
        """
        [Client.create_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sdb.html#SimpleDB.Client.create_domain)
        """

    def delete_attributes(
        self,
        DomainName: str,
        ItemName: str,
        Attributes: List["AttributeTypeDef"] = None,
        Expected: UpdateConditionTypeDef = None,
    ) -> None:
        """
        [Client.delete_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sdb.html#SimpleDB.Client.delete_attributes)
        """

    def delete_domain(self, DomainName: str) -> None:
        """
        [Client.delete_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sdb.html#SimpleDB.Client.delete_domain)
        """

    def domain_metadata(self, DomainName: str) -> DomainMetadataResultTypeDef:
        """
        [Client.domain_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sdb.html#SimpleDB.Client.domain_metadata)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sdb.html#SimpleDB.Client.generate_presigned_url)
        """

    def get_attributes(
        self,
        DomainName: str,
        ItemName: str,
        AttributeNames: List[str] = None,
        ConsistentRead: bool = None,
    ) -> GetAttributesResultTypeDef:
        """
        [Client.get_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sdb.html#SimpleDB.Client.get_attributes)
        """

    def list_domains(
        self, MaxNumberOfDomains: int = None, NextToken: str = None
    ) -> ListDomainsResultTypeDef:
        """
        [Client.list_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sdb.html#SimpleDB.Client.list_domains)
        """

    def put_attributes(
        self,
        DomainName: str,
        ItemName: str,
        Attributes: List["ReplaceableAttributeTypeDef"],
        Expected: UpdateConditionTypeDef = None,
    ) -> None:
        """
        [Client.put_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sdb.html#SimpleDB.Client.put_attributes)
        """

    def select(
        self, SelectExpression: str, NextToken: str = None, ConsistentRead: bool = None
    ) -> SelectResultTypeDef:
        """
        [Client.select documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sdb.html#SimpleDB.Client.select)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_domains"]) -> ListDomainsPaginator:
        """
        [Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sdb.html#SimpleDB.Paginator.ListDomains)
        """

    @overload
    def get_paginator(self, operation_name: Literal["select"]) -> SelectPaginator:
        """
        [Paginator.Select documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sdb.html#SimpleDB.Paginator.Select)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
