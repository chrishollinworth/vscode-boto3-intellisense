"""
Main interface for marketplace-deployment service.

Usage::

    ```python
    import boto3
    from mypy_boto3_marketplace_deployment import (
        Client,
        MarketplaceDeploymentServiceClient,
    )

    session = boto3.Session()

    client: MarketplaceDeploymentServiceClient = boto3.client("marketplace-deployment")
    session_client: MarketplaceDeploymentServiceClient = session.client("marketplace-deployment")
    ```
"""

from .client import MarketplaceDeploymentServiceClient

Client = MarketplaceDeploymentServiceClient

__all__ = ("Client", "MarketplaceDeploymentServiceClient")
