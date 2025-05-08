"""
Type annotations for pca-connector-scep service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_pca_connector_scep.client import PrivateCAConnectorforSCEPClient

    session = Session()
    client: PrivateCAConnectorforSCEPClient = session.client("pca-connector-scep")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListChallengeMetadataPaginator, ListConnectorsPaginator
from .type_defs import (
    CreateChallengeRequestTypeDef,
    CreateChallengeResponseTypeDef,
    CreateConnectorRequestTypeDef,
    CreateConnectorResponseTypeDef,
    DeleteChallengeRequestTypeDef,
    DeleteConnectorRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetChallengeMetadataRequestTypeDef,
    GetChallengeMetadataResponseTypeDef,
    GetChallengePasswordRequestTypeDef,
    GetChallengePasswordResponseTypeDef,
    GetConnectorRequestTypeDef,
    GetConnectorResponseTypeDef,
    ListChallengeMetadataRequestTypeDef,
    ListChallengeMetadataResponseTypeDef,
    ListConnectorsRequestTypeDef,
    ListConnectorsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
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

__all__ = ("PrivateCAConnectorforSCEPClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class PrivateCAConnectorforSCEPClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PrivateCAConnectorforSCEPClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#generate_presigned_url)
        """

    def create_challenge(
        self, **kwargs: Unpack[CreateChallengeRequestTypeDef]
    ) -> CreateChallengeResponseTypeDef:
        """
        For general-purpose connectors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep/client/create_challenge.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#create_challenge)
        """

    def create_connector(
        self, **kwargs: Unpack[CreateConnectorRequestTypeDef]
    ) -> CreateConnectorResponseTypeDef:
        """
        Creates a SCEP connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep/client/create_connector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#create_connector)
        """

    def delete_challenge(
        self, **kwargs: Unpack[DeleteChallengeRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified <a
        href="https://docs.aws.amazon.com/C4SCEP_API/pca-connector-scep/latest/APIReference/API_Challenge.html">Challenge</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep/client/delete_challenge.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#delete_challenge)
        """

    def delete_connector(
        self, **kwargs: Unpack[DeleteConnectorRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified <a
        href="https://docs.aws.amazon.com/C4SCEP_API/pca-connector-scep/latest/APIReference/API_Connector.html">Connector</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep/client/delete_connector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#delete_connector)
        """

    def get_challenge_metadata(
        self, **kwargs: Unpack[GetChallengeMetadataRequestTypeDef]
    ) -> GetChallengeMetadataResponseTypeDef:
        """
        Retrieves the metadata for the specified <a
        href="https://docs.aws.amazon.com/C4SCEP_API/pca-connector-scep/latest/APIReference/API_Challenge.html">Challenge</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep/client/get_challenge_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#get_challenge_metadata)
        """

    def get_challenge_password(
        self, **kwargs: Unpack[GetChallengePasswordRequestTypeDef]
    ) -> GetChallengePasswordResponseTypeDef:
        """
        Retrieves the challenge password for the specified <a
        href="https://docs.aws.amazon.com/C4SCEP_API/pca-connector-scep/latest/APIReference/API_Challenge.html">Challenge</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep/client/get_challenge_password.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#get_challenge_password)
        """

    def get_connector(
        self, **kwargs: Unpack[GetConnectorRequestTypeDef]
    ) -> GetConnectorResponseTypeDef:
        """
        Retrieves details about the specified <a
        href="https://docs.aws.amazon.com/C4SCEP_API/pca-connector-scep/latest/APIReference/API_Connector.html">Connector</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep/client/get_connector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#get_connector)
        """

    def list_challenge_metadata(
        self, **kwargs: Unpack[ListChallengeMetadataRequestTypeDef]
    ) -> ListChallengeMetadataResponseTypeDef:
        """
        Retrieves the challenge metadata for the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep/client/list_challenge_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#list_challenge_metadata)
        """

    def list_connectors(
        self, **kwargs: Unpack[ListConnectorsRequestTypeDef]
    ) -> ListConnectorsResponseTypeDef:
        """
        Lists the connectors belonging to your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep/client/list_connectors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#list_connectors)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the tags associated with the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#list_tags_for_resource)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds one or more tags to your resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes one or more tags from your resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#untag_resource)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_challenge_metadata"]
    ) -> ListChallengeMetadataPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_connectors"]
    ) -> ListConnectorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client/#get_paginator)
        """
