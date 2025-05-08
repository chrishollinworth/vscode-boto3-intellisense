"""
Type annotations for s3outposts service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_s3outposts.client import S3OutpostsClient

    session = Session()
    client: S3OutpostsClient = session.client("s3outposts")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListEndpointsPaginator,
    ListOutpostsWithS3Paginator,
    ListSharedEndpointsPaginator,
)
from .type_defs import (
    CreateEndpointRequestTypeDef,
    CreateEndpointResultTypeDef,
    DeleteEndpointRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    ListEndpointsRequestTypeDef,
    ListEndpointsResultTypeDef,
    ListOutpostsWithS3RequestTypeDef,
    ListOutpostsWithS3ResultTypeDef,
    ListSharedEndpointsRequestTypeDef,
    ListSharedEndpointsResultTypeDef,
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

__all__ = ("S3OutpostsClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    OutpostOfflineException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class S3OutpostsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts.html#S3Outposts.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        S3OutpostsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts.html#S3Outposts.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client/#generate_presigned_url)
        """

    def create_endpoint(
        self, **kwargs: Unpack[CreateEndpointRequestTypeDef]
    ) -> CreateEndpointResultTypeDef:
        """
        Creates an endpoint and associates it with the specified Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts/client/create_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client/#create_endpoint)
        """

    def delete_endpoint(
        self, **kwargs: Unpack[DeleteEndpointRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts/client/delete_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client/#delete_endpoint)
        """

    def list_endpoints(
        self, **kwargs: Unpack[ListEndpointsRequestTypeDef]
    ) -> ListEndpointsResultTypeDef:
        """
        Lists endpoints associated with the specified Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts/client/list_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client/#list_endpoints)
        """

    def list_outposts_with_s3(
        self, **kwargs: Unpack[ListOutpostsWithS3RequestTypeDef]
    ) -> ListOutpostsWithS3ResultTypeDef:
        """
        Lists the Outposts with S3 on Outposts capacity for your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts/client/list_outposts_with_s3.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client/#list_outposts_with_s3)
        """

    def list_shared_endpoints(
        self, **kwargs: Unpack[ListSharedEndpointsRequestTypeDef]
    ) -> ListSharedEndpointsResultTypeDef:
        """
        Lists all endpoints associated with an Outpost that has been shared by Amazon
        Web Services Resource Access Manager (RAM).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts/client/list_shared_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client/#list_shared_endpoints)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_endpoints"]
    ) -> ListEndpointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_outposts_with_s3"]
    ) -> ListOutpostsWithS3Paginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_shared_endpoints"]
    ) -> ListSharedEndpointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client/#get_paginator)
        """
