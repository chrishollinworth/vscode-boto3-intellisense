"""
Type annotations for greengrassv2 service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_greengrassv2 import GreengrassV2Client
    from mypy_boto3_greengrassv2.paginator import (
        ListClientDevicesAssociatedWithCoreDevicePaginator,
        ListComponentVersionsPaginator,
        ListComponentsPaginator,
        ListCoreDevicesPaginator,
        ListDeploymentsPaginator,
        ListEffectiveDeploymentsPaginator,
        ListInstalledComponentsPaginator,
    )

    client: GreengrassV2Client = boto3.client("greengrassv2")

    list_client_devices_associated_with_core_device_paginator: ListClientDevicesAssociatedWithCoreDevicePaginator = client.get_paginator("list_client_devices_associated_with_core_device")
    list_component_versions_paginator: ListComponentVersionsPaginator = client.get_paginator("list_component_versions")
    list_components_paginator: ListComponentsPaginator = client.get_paginator("list_components")
    list_core_devices_paginator: ListCoreDevicesPaginator = client.get_paginator("list_core_devices")
    list_deployments_paginator: ListDeploymentsPaginator = client.get_paginator("list_deployments")
    list_effective_deployments_paginator: ListEffectiveDeploymentsPaginator = client.get_paginator("list_effective_deployments")
    list_installed_components_paginator: ListInstalledComponentsPaginator = client.get_paginator("list_installed_components")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    ComponentVisibilityScopeType,
    CoreDeviceStatusType,
    DeploymentHistoryFilterType,
    InstalledComponentTopologyFilterType,
)
from .type_defs import (
    ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef,
    ListComponentsResponseTypeDef,
    ListComponentVersionsResponseTypeDef,
    ListCoreDevicesResponseTypeDef,
    ListDeploymentsResponseTypeDef,
    ListEffectiveDeploymentsResponseTypeDef,
    ListInstalledComponentsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListClientDevicesAssociatedWithCoreDevicePaginator",
    "ListComponentVersionsPaginator",
    "ListComponentsPaginator",
    "ListCoreDevicesPaginator",
    "ListDeploymentsPaginator",
    "ListEffectiveDeploymentsPaginator",
    "ListInstalledComponentsPaginator",
)

class ListClientDevicesAssociatedWithCoreDevicePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListClientDevicesAssociatedWithCoreDevice)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators.html#listclientdevicesassociatedwithcoredevicepaginator)
    """

    def paginate(
        self, *, coreDeviceThingName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListClientDevicesAssociatedWithCoreDevice.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators.html#listclientdevicesassociatedwithcoredevicepaginator)
        """

class ListComponentVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListComponentVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators.html#listcomponentversionspaginator)
    """

    def paginate(
        self, *, arn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListComponentVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListComponentVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators.html#listcomponentversionspaginator)
        """

class ListComponentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListComponents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators.html#listcomponentspaginator)
    """

    def paginate(
        self,
        *,
        scope: ComponentVisibilityScopeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListComponentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListComponents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators.html#listcomponentspaginator)
        """

class ListCoreDevicesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListCoreDevices)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators.html#listcoredevicespaginator)
    """

    def paginate(
        self,
        *,
        thingGroupArn: str = None,
        status: CoreDeviceStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCoreDevicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListCoreDevices.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators.html#listcoredevicespaginator)
        """

class ListDeploymentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListDeployments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators.html#listdeploymentspaginator)
    """

    def paginate(
        self,
        *,
        targetArn: str = None,
        historyFilter: DeploymentHistoryFilterType = None,
        parentTargetArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeploymentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListDeployments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators.html#listdeploymentspaginator)
        """

class ListEffectiveDeploymentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListEffectiveDeployments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators.html#listeffectivedeploymentspaginator)
    """

    def paginate(
        self, *, coreDeviceThingName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEffectiveDeploymentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListEffectiveDeployments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators.html#listeffectivedeploymentspaginator)
        """

class ListInstalledComponentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListInstalledComponents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators.html#listinstalledcomponentspaginator)
    """

    def paginate(
        self,
        *,
        coreDeviceThingName: str,
        topologyFilter: InstalledComponentTopologyFilterType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstalledComponentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListInstalledComponents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators.html#listinstalledcomponentspaginator)
        """
