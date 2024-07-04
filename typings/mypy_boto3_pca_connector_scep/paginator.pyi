"""
Type annotations for pca-connector-scep service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_pca_connector_scep import PrivateCAConnectorforSCEPClient
    from mypy_boto3_pca_connector_scep.paginator import (
        ListChallengeMetadataPaginator,
        ListConnectorsPaginator,
    )

    client: PrivateCAConnectorforSCEPClient = boto3.client("pca-connector-scep")

    list_challenge_metadata_paginator: ListChallengeMetadataPaginator = client.get_paginator("list_challenge_metadata")
    list_connectors_paginator: ListConnectorsPaginator = client.get_paginator("list_connectors")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListChallengeMetadataResponseTypeDef,
    ListConnectorsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListChallengeMetadataPaginator", "ListConnectorsPaginator")

class ListChallengeMetadataPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Paginator.ListChallengeMetadata)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/paginators.html#listchallengemetadatapaginator)
    """

    def paginate(
        self, *, ConnectorArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListChallengeMetadataResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Paginator.ListChallengeMetadata.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/paginators.html#listchallengemetadatapaginator)
        """

class ListConnectorsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Paginator.ListConnectors)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/paginators.html#listconnectorspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConnectorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Paginator.ListConnectors.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/paginators.html#listconnectorspaginator)
        """
