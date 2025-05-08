"""
Main interface for connectcampaignsv2 service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_connectcampaignsv2 import (
        Client,
        ConnectCampaignServiceV2Client,
        ListCampaignsPaginator,
        ListConnectInstanceIntegrationsPaginator,
    )

    session = Session()
    client: ConnectCampaignServiceV2Client = session.client("connectcampaignsv2")

    list_campaigns_paginator: ListCampaignsPaginator = client.get_paginator("list_campaigns")
    list_connect_instance_integrations_paginator: ListConnectInstanceIntegrationsPaginator = client.get_paginator("list_connect_instance_integrations")
    ```
"""

from .client import ConnectCampaignServiceV2Client
from .paginator import ListCampaignsPaginator, ListConnectInstanceIntegrationsPaginator

Client = ConnectCampaignServiceV2Client

__all__ = (
    "Client",
    "ConnectCampaignServiceV2Client",
    "ListCampaignsPaginator",
    "ListConnectInstanceIntegrationsPaginator",
)
