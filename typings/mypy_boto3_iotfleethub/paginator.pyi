"""
Main interface for iotfleethub service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_iotfleethub import IoTFleetHubClient
    from mypy_boto3_iotfleethub.paginator import (
        ListApplicationsPaginator,
    )

    client: IoTFleetHubClient = boto3.client("iotfleethub")

    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_iotfleethub.type_defs import ListApplicationsResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListApplicationsPaginator",)


class ListApplicationsPaginator(Boto3Paginator):
    """
    [Paginator.ListApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotfleethub.html#IoTFleetHub.Paginator.ListApplications)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationsResponseTypeDef]:
        """
        [ListApplications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/iotfleethub.html#IoTFleetHub.Paginator.ListApplications.paginate)
        """
