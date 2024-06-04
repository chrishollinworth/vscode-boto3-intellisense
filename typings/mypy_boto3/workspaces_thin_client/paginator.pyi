"""
Type annotations for workspaces-thin-client service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_workspaces_thin_client import WorkSpacesThinClientClient
    from mypy_boto3_workspaces_thin_client.paginator import (
        ListDevicesPaginator,
        ListEnvironmentsPaginator,
        ListSoftwareSetsPaginator,
    )

    client: WorkSpacesThinClientClient = boto3.client("workspaces-thin-client")

    list_devices_paginator: ListDevicesPaginator = client.get_paginator("list_devices")
    list_environments_paginator: ListEnvironmentsPaginator = client.get_paginator("list_environments")
    list_software_sets_paginator: ListSoftwareSetsPaginator = client.get_paginator("list_software_sets")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListDevicesResponseTypeDef,
    ListEnvironmentsResponseTypeDef,
    ListSoftwareSetsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListDevicesPaginator", "ListEnvironmentsPaginator", "ListSoftwareSetsPaginator")

class ListDevicesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Paginator.ListDevices)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/paginators.html#listdevicespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDevicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Paginator.ListDevices.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/paginators.html#listdevicespaginator)
        """

class ListEnvironmentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Paginator.ListEnvironments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/paginators.html#listenvironmentspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnvironmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Paginator.ListEnvironments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/paginators.html#listenvironmentspaginator)
        """

class ListSoftwareSetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Paginator.ListSoftwareSets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/paginators.html#listsoftwaresetspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSoftwareSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Paginator.ListSoftwareSets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/paginators.html#listsoftwaresetspaginator)
        """
