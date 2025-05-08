"""
Main interface for pca-connector-scep service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_pca_connector_scep import (
        Client,
        ListChallengeMetadataPaginator,
        ListConnectorsPaginator,
        PrivateCAConnectorforSCEPClient,
    )

    session = Session()
    client: PrivateCAConnectorforSCEPClient = session.client("pca-connector-scep")

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
