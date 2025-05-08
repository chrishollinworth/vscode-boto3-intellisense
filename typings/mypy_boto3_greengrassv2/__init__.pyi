"""
Main interface for greengrassv2 service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_greengrassv2 import (
        Client,
        GreengrassV2Client,
        ListClientDevicesAssociatedWithCoreDevicePaginator,
        ListComponentVersionsPaginator,
        ListComponentsPaginator,
        ListCoreDevicesPaginator,
        ListDeploymentsPaginator,
        ListEffectiveDeploymentsPaginator,
        ListInstalledComponentsPaginator,
    )

    session = Session()
    client: GreengrassV2Client = session.client("greengrassv2")

    list_client_devices_associated_with_core_device_paginator: ListClientDevicesAssociatedWithCoreDevicePaginator = client.get_paginator("list_client_devices_associated_with_core_device")
    list_component_versions_paginator: ListComponentVersionsPaginator = client.get_paginator("list_component_versions")
    list_components_paginator: ListComponentsPaginator = client.get_paginator("list_components")
    list_core_devices_paginator: ListCoreDevicesPaginator = client.get_paginator("list_core_devices")
    list_deployments_paginator: ListDeploymentsPaginator = client.get_paginator("list_deployments")
    list_effective_deployments_paginator: ListEffectiveDeploymentsPaginator = client.get_paginator("list_effective_deployments")
    list_installed_components_paginator: ListInstalledComponentsPaginator = client.get_paginator("list_installed_components")
    ```
"""

from .client import GreengrassV2Client
from .paginator import (
    ListClientDevicesAssociatedWithCoreDevicePaginator,
    ListComponentsPaginator,
    ListComponentVersionsPaginator,
    ListCoreDevicesPaginator,
    ListDeploymentsPaginator,
    ListEffectiveDeploymentsPaginator,
    ListInstalledComponentsPaginator,
)

Client = GreengrassV2Client

__all__ = (
    "Client",
    "GreengrassV2Client",
    "ListClientDevicesAssociatedWithCoreDevicePaginator",
    "ListComponentVersionsPaginator",
    "ListComponentsPaginator",
    "ListCoreDevicesPaginator",
    "ListDeploymentsPaginator",
    "ListEffectiveDeploymentsPaginator",
    "ListInstalledComponentsPaginator",
)
