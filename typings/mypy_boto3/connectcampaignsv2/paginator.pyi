"""
Type annotations for connectcampaignsv2 service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_connectcampaignsv2.client import ConnectCampaignServiceV2Client
    from mypy_boto3_connectcampaignsv2.paginator import (
        ListCampaignsPaginator,
        ListConnectInstanceIntegrationsPaginator,
    )

    session = Session()
    client: ConnectCampaignServiceV2Client = session.client("connectcampaignsv2")

    list_campaigns_paginator: ListCampaignsPaginator = client.get_paginator("list_campaigns")
    list_connect_instance_integrations_paginator: ListConnectInstanceIntegrationsPaginator = client.get_paginator("list_connect_instance_integrations")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListCampaignsRequestPaginateTypeDef,
    ListCampaignsResponseTypeDef,
    ListConnectInstanceIntegrationsRequestPaginateTypeDef,
    ListConnectInstanceIntegrationsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListCampaignsPaginator", "ListConnectInstanceIntegrationsPaginator")

if TYPE_CHECKING:
    _ListCampaignsPaginatorBase = Paginator[ListCampaignsResponseTypeDef]
else:
    _ListCampaignsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCampaignsPaginator(_ListCampaignsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/paginator/ListCampaigns.html#ConnectCampaignServiceV2.Paginator.ListCampaigns)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/paginators/#listcampaignspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCampaignsRequestPaginateTypeDef]
    ) -> PageIterator[ListCampaignsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/paginator/ListCampaigns.html#ConnectCampaignServiceV2.Paginator.ListCampaigns.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/paginators/#listcampaignspaginator)
        """

if TYPE_CHECKING:
    _ListConnectInstanceIntegrationsPaginatorBase = Paginator[
        ListConnectInstanceIntegrationsResponseTypeDef
    ]
else:
    _ListConnectInstanceIntegrationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConnectInstanceIntegrationsPaginator(_ListConnectInstanceIntegrationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/paginator/ListConnectInstanceIntegrations.html#ConnectCampaignServiceV2.Paginator.ListConnectInstanceIntegrations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/paginators/#listconnectinstanceintegrationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConnectInstanceIntegrationsRequestPaginateTypeDef]
    ) -> PageIterator[ListConnectInstanceIntegrationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/paginator/ListConnectInstanceIntegrations.html#ConnectCampaignServiceV2.Paginator.ListConnectInstanceIntegrations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/paginators/#listconnectinstanceintegrationspaginator)
        """
