"""
Type annotations for cloudsearchdomain service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cloudsearchdomain.client import CloudSearchDomainClient

    session = Session()
    client: CloudSearchDomainClient = session.client("cloudsearchdomain")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    SearchRequestTypeDef,
    SearchResponseTypeDef,
    SuggestRequestTypeDef,
    SuggestResponseTypeDef,
    UploadDocumentsRequestTypeDef,
    UploadDocumentsResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("CloudSearchDomainClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    DocumentServiceException: Type[BotocoreClientError]
    SearchException: Type[BotocoreClientError]

class CloudSearchDomainClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudSearchDomainClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client/#generate_presigned_url)
        """

    def search(self, **kwargs: Unpack[SearchRequestTypeDef]) -> SearchResponseTypeDef:
        """
        Retrieves a list of documents that match the specified search criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain/client/search.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client/#search)
        """

    def suggest(self, **kwargs: Unpack[SuggestRequestTypeDef]) -> SuggestResponseTypeDef:
        """
        Retrieves autocomplete suggestions for a partial query string.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain/client/suggest.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client/#suggest)
        """

    def upload_documents(
        self, **kwargs: Unpack[UploadDocumentsRequestTypeDef]
    ) -> UploadDocumentsResponseTypeDef:
        """
        Posts a batch of documents to a search domain for indexing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain/client/upload_documents.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client/#upload_documents)
        """
