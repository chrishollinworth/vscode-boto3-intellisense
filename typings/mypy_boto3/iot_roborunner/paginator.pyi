"""
Type annotations for iot-roborunner service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_iot_roborunner import IoTRoboRunnerClient
    from mypy_boto3_iot_roborunner.paginator import (
        ListDestinationsPaginator,
        ListSitesPaginator,
        ListWorkerFleetsPaginator,
        ListWorkersPaginator,
    )

    client: IoTRoboRunnerClient = boto3.client("iot-roborunner")

    list_destinations_paginator: ListDestinationsPaginator = client.get_paginator("list_destinations")
    list_sites_paginator: ListSitesPaginator = client.get_paginator("list_sites")
    list_worker_fleets_paginator: ListWorkerFleetsPaginator = client.get_paginator("list_worker_fleets")
    list_workers_paginator: ListWorkersPaginator = client.get_paginator("list_workers")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import DestinationStateType
from .type_defs import (
    ListDestinationsResponseTypeDef,
    ListSitesResponseTypeDef,
    ListWorkerFleetsResponseTypeDef,
    ListWorkersResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListDestinationsPaginator",
    "ListSitesPaginator",
    "ListWorkerFleetsPaginator",
    "ListWorkersPaginator",
)

class ListDestinationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/iot-roborunner.html#IoTRoboRunner.Paginator.ListDestinations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/paginators.html#listdestinationspaginator)
    """

    def paginate(
        self,
        *,
        site: str,
        state: DestinationStateType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDestinationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/iot-roborunner.html#IoTRoboRunner.Paginator.ListDestinations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/paginators.html#listdestinationspaginator)
        """

class ListSitesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/iot-roborunner.html#IoTRoboRunner.Paginator.ListSites)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/paginators.html#listsitespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSitesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/iot-roborunner.html#IoTRoboRunner.Paginator.ListSites.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/paginators.html#listsitespaginator)
        """

class ListWorkerFleetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/iot-roborunner.html#IoTRoboRunner.Paginator.ListWorkerFleets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/paginators.html#listworkerfleetspaginator)
    """

    def paginate(
        self, *, site: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorkerFleetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/iot-roborunner.html#IoTRoboRunner.Paginator.ListWorkerFleets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/paginators.html#listworkerfleetspaginator)
        """

class ListWorkersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/iot-roborunner.html#IoTRoboRunner.Paginator.ListWorkers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/paginators.html#listworkerspaginator)
    """

    def paginate(
        self, *, site: str, fleet: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorkersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/iot-roborunner.html#IoTRoboRunner.Paginator.ListWorkers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/paginators.html#listworkerspaginator)
        """
