"""
Main interface for workspaces-thin-client service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_workspaces_thin_client import (
        Client,
        ListDevicesPaginator,
        ListEnvironmentsPaginator,
        ListSoftwareSetsPaginator,
        WorkSpacesThinClientClient,
    )

    session = Session()
    client: WorkSpacesThinClientClient = session.client("workspaces-thin-client")

    list_devices_paginator: ListDevicesPaginator = client.get_paginator("list_devices")
    list_environments_paginator: ListEnvironmentsPaginator = client.get_paginator("list_environments")
    list_software_sets_paginator: ListSoftwareSetsPaginator = client.get_paginator("list_software_sets")
    ```
"""

from .client import WorkSpacesThinClientClient
from .paginator import ListDevicesPaginator, ListEnvironmentsPaginator, ListSoftwareSetsPaginator

Client = WorkSpacesThinClientClient

__all__ = (
    "Client",
    "ListDevicesPaginator",
    "ListEnvironmentsPaginator",
    "ListSoftwareSetsPaginator",
    "WorkSpacesThinClientClient",
)
