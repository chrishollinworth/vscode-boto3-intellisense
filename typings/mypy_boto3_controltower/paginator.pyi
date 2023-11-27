"""
Type annotations for controltower service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_controltower import ControlTowerClient
    from mypy_boto3_controltower.paginator import (
        ListEnabledControlsPaginator,
        ListLandingZonesPaginator,
    )

    client: ControlTowerClient = boto3.client("controltower")

    list_enabled_controls_paginator: ListEnabledControlsPaginator = client.get_paginator("list_enabled_controls")
    list_landing_zones_paginator: ListLandingZonesPaginator = client.get_paginator("list_landing_zones")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListEnabledControlsOutputTypeDef,
    ListLandingZonesOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListEnabledControlsPaginator", "ListLandingZonesPaginator")

class ListEnabledControlsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Paginator.ListEnabledControls)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/paginators.html#listenabledcontrolspaginator)
    """

    def paginate(
        self, *, targetIdentifier: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnabledControlsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Paginator.ListEnabledControls.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/paginators.html#listenabledcontrolspaginator)
        """

class ListLandingZonesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Paginator.ListLandingZones)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/paginators.html#listlandingzonespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLandingZonesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Paginator.ListLandingZones.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/paginators.html#listlandingzonespaginator)
        """
