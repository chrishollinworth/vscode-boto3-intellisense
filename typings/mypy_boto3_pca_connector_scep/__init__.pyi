"""
Main interface for pca-connector-scep service.

Usage::

    ```python
    import boto3
    from mypy_boto3_pca_connector_scep import (
        Client,
        ListChallengeMetadataPaginator,
        ListConnectorsPaginator,
        PrivateCAConnectorforSCEPClient,
    )

    session = boto3.Session()

    client: PrivateCAConnectorforSCEPClient = boto3.client("pca-connector-scep")
    session_client: PrivateCAConnectorforSCEPClient = session.client("pca-connector-scep")

    list_challenge_metadata_paginator: ListChallengeMetadataPaginator = client.get_paginator("list_challenge_metadata")
    list_connectors_paginator: ListConnectorsPaginator = client.get_paginator("list_connectors")
    ```
"""

from .client import PrivateCAConnectorforSCEPClient
from .paginator import ListChallengeMetadataPaginator, ListConnectorsPaginator

Client = PrivateCAConnectorforSCEPClient

__all__ = (
    "Client",
    "ListChallengeMetadataPaginator",
    "ListConnectorsPaginator",
    "PrivateCAConnectorforSCEPClient",
)
