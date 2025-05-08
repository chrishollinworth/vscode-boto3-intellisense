"""
Type annotations for pca-connector-scep service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_pca_connector_scep.client import PrivateCAConnectorforSCEPClient
    from mypy_boto3_pca_connector_scep.paginator import (
        ListChallengeMetadataPaginator,
        ListConnectorsPaginator,
    )

    session = Session()
    client: PrivateCAConnectorforSCEPClient = session.client("pca-connector-scep")

    list_challenge_metadata_paginator: ListChallengeMetadataPaginator = client.get_paginator("list_challenge_metadata")
    list_connectors_paginator: ListConnectorsPaginator = client.get_paginator("list_connectors")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListChallengeMetadataRequestPaginateTypeDef,
    ListChallengeMetadataResponseTypeDef,
    ListConnectorsRequestPaginateTypeDef,
    ListConnectorsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListChallengeMetadataPaginator", "ListConnectorsPaginator")

if TYPE_CHECKING:
    _ListChallengeMetadataPaginatorBase = Paginator[ListChallengeMetadataResponseTypeDef]
else:
    _ListChallengeMetadataPaginatorBase = Paginator  # type: ignore[assignment]

class ListChallengeMetadataPaginator(_ListChallengeMetadataPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep/paginator/ListChallengeMetadata.html#PrivateCAConnectorforSCEP.Paginator.ListChallengeMetadata)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/paginators/#listchallengemetadatapaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListChallengeMetadataRequestPaginateTypeDef]
    ) -> PageIterator[ListChallengeMetadataResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep/paginator/ListChallengeMetadata.html#PrivateCAConnectorforSCEP.Paginator.ListChallengeMetadata.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/paginators/#listchallengemetadatapaginator)
        """

if TYPE_CHECKING:
    _ListConnectorsPaginatorBase = Paginator[ListConnectorsResponseTypeDef]
else:
    _ListConnectorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConnectorsPaginator(_ListConnectorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep/paginator/ListConnectors.html#PrivateCAConnectorforSCEP.Paginator.ListConnectors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/paginators/#listconnectorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConnectorsRequestPaginateTypeDef]
    ) -> PageIterator[ListConnectorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-scep/paginator/ListConnectors.html#PrivateCAConnectorforSCEP.Paginator.ListConnectors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/paginators/#listconnectorspaginator)
        """
