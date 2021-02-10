"""
Main interface for greengrassv2 service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_greengrassv2 import GreengrassV2Client
    from mypy_boto3_greengrassv2.paginator import (
        ListComponentVersionsPaginator,
        ListComponentsPaginator,
        ListCoreDevicesPaginator,
        ListDeploymentsPaginator,
        ListEffectiveDeploymentsPaginator,
        ListInstalledComponentsPaginator,
    )

    client: GreengrassV2Client = boto3.client("greengrassv2")

    list_component_versions_paginator: ListComponentVersionsPaginator = client.get_paginator("list_component_versions")
    list_components_paginator: ListComponentsPaginator = client.get_paginator("list_components")
    list_core_devices_paginator: ListCoreDevicesPaginator = client.get_paginator("list_core_devices")
    list_deployments_paginator: ListDeploymentsPaginator = client.get_paginator("list_deployments")
    list_effective_deployments_paginator: ListEffectiveDeploymentsPaginator = client.get_paginator("list_effective_deployments")
    list_installed_components_paginator: ListInstalledComponentsPaginator = client.get_paginator("list_installed_components")
    ```
"""
import sys
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_greengrassv2.type_defs import (
    ListComponentsResponseTypeDef,
    ListComponentVersionsResponseTypeDef,
    ListCoreDevicesResponseTypeDef,
    ListDeploymentsResponseTypeDef,
    ListEffectiveDeploymentsResponseTypeDef,
    ListInstalledComponentsResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListComponentVersionsPaginator",
    "ListComponentsPaginator",
    "ListCoreDevicesPaginator",
    "ListDeploymentsPaginator",
    "ListEffectiveDeploymentsPaginator",
    "ListInstalledComponentsPaginator",
)


class ListComponentVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListComponentVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListComponentVersions)
    """

    def paginate(
        self, arn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListComponentVersionsResponseTypeDef]:
        """
        [ListComponentVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListComponentVersions.paginate)
        """


class ListComponentsPaginator(Boto3Paginator):
    """
    [Paginator.ListComponents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListComponents)
    """

    def paginate(
        self,
        scope: Literal["PRIVATE", "PUBLIC"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListComponentsResponseTypeDef]:
        """
        [ListComponents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListComponents.paginate)
        """


class ListCoreDevicesPaginator(Boto3Paginator):
    """
    [Paginator.ListCoreDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListCoreDevices)
    """

    def paginate(
        self,
        thingGroupArn: str = None,
        status: Literal["HEALTHY", "UNHEALTHY"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListCoreDevicesResponseTypeDef]:
        """
        [ListCoreDevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListCoreDevices.paginate)
        """


class ListDeploymentsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListDeployments)
    """

    def paginate(
        self,
        targetArn: str = None,
        historyFilter: Literal["ALL", "LATEST_ONLY"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListDeploymentsResponseTypeDef]:
        """
        [ListDeployments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListDeployments.paginate)
        """


class ListEffectiveDeploymentsPaginator(Boto3Paginator):
    """
    [Paginator.ListEffectiveDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListEffectiveDeployments)
    """

    def paginate(
        self, coreDeviceThingName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEffectiveDeploymentsResponseTypeDef]:
        """
        [ListEffectiveDeployments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListEffectiveDeployments.paginate)
        """


class ListInstalledComponentsPaginator(Boto3Paginator):
    """
    [Paginator.ListInstalledComponents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListInstalledComponents)
    """

    def paginate(
        self, coreDeviceThingName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstalledComponentsResponseTypeDef]:
        """
        [ListInstalledComponents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListInstalledComponents.paginate)
        """
