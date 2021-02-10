"""
Main interface for greengrassv2 service.

Usage::

    ```python
    import boto3
    from mypy_boto3_greengrassv2 import (
        Client,
        GreengrassV2Client,
        ListComponentVersionsPaginator,
        ListComponentsPaginator,
        ListCoreDevicesPaginator,
        ListDeploymentsPaginator,
        ListEffectiveDeploymentsPaginator,
        ListInstalledComponentsPaginator,
    )

    session = boto3.Session()

    client: GreengrassV2Client = boto3.client("greengrassv2")
    session_client: GreengrassV2Client = session.client("greengrassv2")

    list_component_versions_paginator: ListComponentVersionsPaginator = client.get_paginator("list_component_versions")
    list_components_paginator: ListComponentsPaginator = client.get_paginator("list_components")
    list_core_devices_paginator: ListCoreDevicesPaginator = client.get_paginator("list_core_devices")
    list_deployments_paginator: ListDeploymentsPaginator = client.get_paginator("list_deployments")
    list_effective_deployments_paginator: ListEffectiveDeploymentsPaginator = client.get_paginator("list_effective_deployments")
    list_installed_components_paginator: ListInstalledComponentsPaginator = client.get_paginator("list_installed_components")
    ```
"""
from mypy_boto3_greengrassv2.client import GreengrassV2Client
from mypy_boto3_greengrassv2.paginator import (
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
    "ListComponentVersionsPaginator",
    "ListComponentsPaginator",
    "ListCoreDevicesPaginator",
    "ListDeploymentsPaginator",
    "ListEffectiveDeploymentsPaginator",
    "ListInstalledComponentsPaginator",
)
