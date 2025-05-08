"""
Type annotations for connectcampaigns service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_connectcampaigns.client import ConnectCampaignServiceClient
    from mypy_boto3_connectcampaigns.paginator import (
        ListCampaignsPaginator,
    )

    session = Session()
    client: ConnectCampaignServiceClient = session.client("connectcampaigns")

    list_campaigns_paginator: ListCampaignsPaginator = client.get_paginator("list_campaigns")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListCampaignsRequestPaginateTypeDef, ListCampaignsResponseTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListCampaignsPaginator",)

if TYPE_CHECKING:
    _ListCampaignsPaginatorBase = Paginator[ListCampaignsResponseTypeDef]
else:
    _ListCampaignsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCampaignsPaginator(_ListCampaignsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaigns/paginator/ListCampaigns.html#ConnectCampaignService.Paginator.ListCampaigns)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/paginators/#listcampaignspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCampaignsRequestPaginateTypeDef]
    ) -> PageIterator[ListCampaignsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaigns/paginator/ListCampaigns.html#ConnectCampaignService.Paginator.ListCampaigns.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/paginators/#listcampaignspaginator)
        """
