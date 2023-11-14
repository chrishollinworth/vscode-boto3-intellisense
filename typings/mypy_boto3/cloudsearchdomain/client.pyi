"""
Type annotations for cloudsearchdomain service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudsearchdomain import CloudSearchDomainClient

    client: CloudSearchDomainClient = boto3.client("cloudsearchdomain")
    ```
"""
from typing import IO, Any, Dict, Type, Union

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import ContentTypeType, QueryParserType
from .type_defs import SearchResponseTypeDef, SuggestResponseTypeDef, UploadDocumentsResponseTypeDef

__all__ = ("CloudSearchDomainClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    DocumentServiceException: Type[BotocoreClientError]
    SearchException: Type[BotocoreClientError]

class CloudSearchDomainClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudSearchDomainClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client.html#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client.html#generate_presigned_url)
        """
    def search(
        self,
        *,
        query: str,
        cursor: str = None,
        expr: str = None,
        facet: str = None,
        filterQuery: str = None,
        highlight: str = None,
        partial: bool = None,
        queryOptions: str = None,
        queryParser: QueryParserType = None,
        returnFields: str = None,
        size: int = None,
        sort: str = None,
        start: int = None,
        stats: str = None
    ) -> SearchResponseTypeDef:
        """
        Retrieves a list of documents that match the specified search criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.search)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client.html#search)
        """
    def suggest(self, *, query: str, suggester: str, size: int = None) -> SuggestResponseTypeDef:
        """
        Retrieves autocomplete suggestions for a partial query string.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.suggest)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client.html#suggest)
        """
    def upload_documents(
        self, *, documents: Union[bytes, IO[bytes], StreamingBody], contentType: ContentTypeType
    ) -> UploadDocumentsResponseTypeDef:
        """
        Posts a batch of documents to a search domain for indexing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.upload_documents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client.html#upload_documents)
        """
