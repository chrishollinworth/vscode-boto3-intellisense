"""
Type annotations for workspaces-thin-client service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_workspaces_thin_client.client import WorkSpacesThinClientClient
    from mypy_boto3_workspaces_thin_client.paginator import (
        ListDevicesPaginator,
        ListEnvironmentsPaginator,
        ListSoftwareSetsPaginator,
    )

    session = Session()
    client: WorkSpacesThinClientClient = session.client("workspaces-thin-client")

    list_devices_paginator: ListDevicesPaginator = client.get_paginator("list_devices")
    list_environments_paginator: ListEnvironmentsPaginator = client.get_paginator("list_environments")
    list_software_sets_paginator: ListSoftwareSetsPaginator = client.get_paginator("list_software_sets")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListDevicesRequestPaginateTypeDef,
    ListDevicesResponseTypeDef,
    ListEnvironmentsRequestPaginateTypeDef,
    ListEnvironmentsResponseTypeDef,
    ListSoftwareSetsRequestPaginateTypeDef,
    ListSoftwareSetsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListDevicesPaginator", "ListEnvironmentsPaginator", "ListSoftwareSetsPaginator")

if TYPE_CHECKING:
    _ListDevicesPaginatorBase = Paginator[ListDevicesResponseTypeDef]
else:
    _ListDevicesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDevicesPaginator(_ListDevicesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-thin-client/paginator/ListDevices.html#WorkSpacesThinClient.Paginator.ListDevices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/paginators/#listdevicespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDevicesRequestPaginateTypeDef]
    ) -> PageIterator[ListDevicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-thin-client/paginator/ListDevices.html#WorkSpacesThinClient.Paginator.ListDevices.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/paginators/#listdevicespaginator)
        """

if TYPE_CHECKING:
    _ListEnvironmentsPaginatorBase = Paginator[ListEnvironmentsResponseTypeDef]
else:
    _ListEnvironmentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEnvironmentsPaginator(_ListEnvironmentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-thin-client/paginator/ListEnvironments.html#WorkSpacesThinClient.Paginator.ListEnvironments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/paginators/#listenvironmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnvironmentsRequestPaginateTypeDef]
    ) -> PageIterator[ListEnvironmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-thin-client/paginator/ListEnvironments.html#WorkSpacesThinClient.Paginator.ListEnvironments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/paginators/#listenvironmentspaginator)
        """

if TYPE_CHECKING:
    _ListSoftwareSetsPaginatorBase = Paginator[ListSoftwareSetsResponseTypeDef]
else:
    _ListSoftwareSetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSoftwareSetsPaginator(_ListSoftwareSetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-thin-client/paginator/ListSoftwareSets.html#WorkSpacesThinClient.Paginator.ListSoftwareSets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/paginators/#listsoftwaresetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSoftwareSetsRequestPaginateTypeDef]
    ) -> PageIterator[ListSoftwareSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-thin-client/paginator/ListSoftwareSets.html#WorkSpacesThinClient.Paginator.ListSoftwareSets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/paginators/#listsoftwaresetspaginator)
        """
