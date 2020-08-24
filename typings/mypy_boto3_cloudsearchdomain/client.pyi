# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for cloudsearchdomain service client

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudsearchdomain import CloudSearchDomainClient

    client: CloudSearchDomainClient = boto3.client("cloudsearchdomain")
    ```
"""
import sys
from typing import IO, Any, Dict, Type, Union

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_cloudsearchdomain.type_defs import (
    SearchResponseTypeDef,
    SuggestResponseTypeDef,
    UploadDocumentsResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CloudSearchDomainClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    DocumentServiceException: Type[Boto3ClientError]
    SearchException: Type[Boto3ClientError]


class CloudSearchDomainClient:
    """
    [CloudSearchDomain.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.generate_presigned_url)
        """

    def search(
        self,
        query: str,
        cursor: str = None,
        expr: str = None,
        facet: str = None,
        filterQuery: str = None,
        highlight: str = None,
        partial: bool = None,
        queryOptions: str = None,
        queryParser: Literal["simple", "structured", "lucene", "dismax"] = None,
        returnFields: str = None,
        size: int = None,
        sort: str = None,
        start: int = None,
        stats: str = None,
    ) -> SearchResponseTypeDef:
        """
        [Client.search documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.search)
        """

    def suggest(self, query: str, suggester: str, size: int = None) -> SuggestResponseTypeDef:
        """
        [Client.suggest documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.suggest)
        """

    def upload_documents(
        self,
        documents: Union[bytes, IO[bytes]],
        contentType: Literal["application/json", "application/xml"],
    ) -> UploadDocumentsResponseTypeDef:
        """
        [Client.upload_documents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.upload_documents)
        """
