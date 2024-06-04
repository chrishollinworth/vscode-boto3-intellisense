"""
Type annotations for controltower service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_controltower import ControlTowerClient
    from mypy_boto3_controltower.paginator import (
        ListBaselinesPaginator,
        ListControlOperationsPaginator,
        ListEnabledBaselinesPaginator,
        ListEnabledControlsPaginator,
        ListLandingZonesPaginator,
    )

    client: ControlTowerClient = boto3.client("controltower")

    list_baselines_paginator: ListBaselinesPaginator = client.get_paginator("list_baselines")
    list_control_operations_paginator: ListControlOperationsPaginator = client.get_paginator("list_control_operations")
    list_enabled_baselines_paginator: ListEnabledBaselinesPaginator = client.get_paginator("list_enabled_baselines")
    list_enabled_controls_paginator: ListEnabledControlsPaginator = client.get_paginator("list_enabled_controls")
    list_landing_zones_paginator: ListLandingZonesPaginator = client.get_paginator("list_landing_zones")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ControlOperationFilterTypeDef,
    EnabledBaselineFilterTypeDef,
    EnabledControlFilterTypeDef,
    ListBaselinesOutputTypeDef,
    ListControlOperationsOutputTypeDef,
    ListEnabledBaselinesOutputTypeDef,
    ListEnabledControlsOutputTypeDef,
    ListLandingZonesOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListBaselinesPaginator",
    "ListControlOperationsPaginator",
    "ListEnabledBaselinesPaginator",
    "ListEnabledControlsPaginator",
    "ListLandingZonesPaginator",
)

class ListBaselinesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/controltower.html#ControlTower.Paginator.ListBaselines)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/paginators.html#listbaselinespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBaselinesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/controltower.html#ControlTower.Paginator.ListBaselines.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/paginators.html#listbaselinespaginator)
        """

class ListControlOperationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/controltower.html#ControlTower.Paginator.ListControlOperations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/paginators.html#listcontroloperationspaginator)
    """

    def paginate(
        self,
        *,
        filter: "ControlOperationFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListControlOperationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/controltower.html#ControlTower.Paginator.ListControlOperations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/paginators.html#listcontroloperationspaginator)
        """

class ListEnabledBaselinesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/controltower.html#ControlTower.Paginator.ListEnabledBaselines)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/paginators.html#listenabledbaselinespaginator)
    """

    def paginate(
        self,
        *,
        filter: "EnabledBaselineFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnabledBaselinesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/controltower.html#ControlTower.Paginator.ListEnabledBaselines.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/paginators.html#listenabledbaselinespaginator)
        """

class ListEnabledControlsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/controltower.html#ControlTower.Paginator.ListEnabledControls)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/paginators.html#listenabledcontrolspaginator)
    """

    def paginate(
        self,
        *,
        filter: "EnabledControlFilterTypeDef" = None,
        targetIdentifier: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnabledControlsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/controltower.html#ControlTower.Paginator.ListEnabledControls.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/paginators.html#listenabledcontrolspaginator)
        """

class ListLandingZonesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/controltower.html#ControlTower.Paginator.ListLandingZones)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/paginators.html#listlandingzonespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLandingZonesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/controltower.html#ControlTower.Paginator.ListLandingZones.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/paginators.html#listlandingzonespaginator)
        """
