"""
Main interface for connectcampaigns service.

Usage::

    ```python
    import boto3
    from mypy_boto3_connectcampaigns import (
        Client,
        ConnectCampaignServiceClient,
        ListCampaignsPaginator,
    )

    session = boto3.Session()

    client: ConnectCampaignServiceClient = boto3.client("connectcampaigns")
    session_client: ConnectCampaignServiceClient = session.client("connectcampaigns")

    list_campaigns_paginator: ListCampaignsPaginator = client.get_paginator("list_campaigns")
    ```
"""

from .client import ConnectCampaignServiceClient
from .paginator import ListCampaignsPaginator

Client = ConnectCampaignServiceClient

__all__ = ("Client", "ConnectCampaignServiceClient", "ListCampaignsPaginator")
