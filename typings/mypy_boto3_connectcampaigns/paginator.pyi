"""
Type annotations for connectcampaigns service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_connectcampaigns import ConnectCampaignServiceClient
    from mypy_boto3_connectcampaigns.paginator import (
        ListCampaignsPaginator,
    )

    client: ConnectCampaignServiceClient = boto3.client("connectcampaigns")

    list_campaigns_paginator: ListCampaignsPaginator = client.get_paginator("list_campaigns")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import CampaignFiltersTypeDef, ListCampaignsResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListCampaignsPaginator",)

class ListCampaignsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/connectcampaigns.html#ConnectCampaignService.Paginator.ListCampaigns)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/paginators.html#listcampaignspaginator)
    """

    def paginate(
        self,
        *,
        filters: "CampaignFiltersTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCampaignsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/connectcampaigns.html#ConnectCampaignService.Paginator.ListCampaigns.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/paginators.html#listcampaignspaginator)
        """
