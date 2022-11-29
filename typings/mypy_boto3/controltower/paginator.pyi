"""
Type annotations for controltower service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_controltower import ControlTowerClient
    from mypy_boto3_controltower.paginator import (
        ListEnabledControlsPaginator,
    )

    client: ControlTowerClient = boto3.client("controltower")

    list_enabled_controls_paginator: ListEnabledControlsPaginator = client.get_paginator("list_enabled_controls")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import ListEnabledControlsOutputTypeDef, PaginatorConfigTypeDef

__all__ = ("ListEnabledControlsPaginator",)

class ListEnabledControlsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/controltower.html#ControlTower.Paginator.ListEnabledControls)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/paginators.html#listenabledcontrolspaginator)
    """

    def paginate(
        self, *, targetIdentifier: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnabledControlsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/controltower.html#ControlTower.Paginator.ListEnabledControls.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/paginators.html#listenabledcontrolspaginator)
        """
