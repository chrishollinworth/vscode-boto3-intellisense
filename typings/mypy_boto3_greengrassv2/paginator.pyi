"""
Type annotations for greengrassv2 service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_greengrassv2.client import GreengrassV2Client
    from mypy_boto3_greengrassv2.paginator import (
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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListClientDevicesAssociatedWithCoreDeviceRequestPaginateTypeDef,
    ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef,
    ListComponentsRequestPaginateTypeDef,
    ListComponentsResponseTypeDef,
    ListComponentVersionsRequestPaginateTypeDef,
    ListComponentVersionsResponseTypeDef,
    ListCoreDevicesRequestPaginateTypeDef,
    ListCoreDevicesResponseTypeDef,
    ListDeploymentsRequestPaginateTypeDef,
    ListDeploymentsResponseTypeDef,
    ListEffectiveDeploymentsRequestPaginateTypeDef,
    ListEffectiveDeploymentsResponseTypeDef,
    ListInstalledComponentsRequestPaginateTypeDef,
    ListInstalledComponentsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListClientDevicesAssociatedWithCoreDevicePaginator",
    "ListComponentVersionsPaginator",
    "ListComponentsPaginator",
    "ListCoreDevicesPaginator",
    "ListDeploymentsPaginator",
    "ListEffectiveDeploymentsPaginator",
    "ListInstalledComponentsPaginator",
)

if TYPE_CHECKING:
    _ListClientDevicesAssociatedWithCoreDevicePaginatorBase = Paginator[
        ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef
    ]
else:
    _ListClientDevicesAssociatedWithCoreDevicePaginatorBase = Paginator  # type: ignore[assignment]

class ListClientDevicesAssociatedWithCoreDevicePaginator(
    _ListClientDevicesAssociatedWithCoreDevicePaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2/paginator/ListClientDevicesAssociatedWithCoreDevice.html#GreengrassV2.Paginator.ListClientDevicesAssociatedWithCoreDevice)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators/#listclientdevicesassociatedwithcoredevicepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListClientDevicesAssociatedWithCoreDeviceRequestPaginateTypeDef]
    ) -> PageIterator[ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2/paginator/ListClientDevicesAssociatedWithCoreDevice.html#GreengrassV2.Paginator.ListClientDevicesAssociatedWithCoreDevice.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators/#listclientdevicesassociatedwithcoredevicepaginator)
        """

if TYPE_CHECKING:
    _ListComponentVersionsPaginatorBase = Paginator[ListComponentVersionsResponseTypeDef]
else:
    _ListComponentVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListComponentVersionsPaginator(_ListComponentVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2/paginator/ListComponentVersions.html#GreengrassV2.Paginator.ListComponentVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators/#listcomponentversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListComponentVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListComponentVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2/paginator/ListComponentVersions.html#GreengrassV2.Paginator.ListComponentVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators/#listcomponentversionspaginator)
        """

if TYPE_CHECKING:
    _ListComponentsPaginatorBase = Paginator[ListComponentsResponseTypeDef]
else:
    _ListComponentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListComponentsPaginator(_ListComponentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2/paginator/ListComponents.html#GreengrassV2.Paginator.ListComponents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators/#listcomponentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListComponentsRequestPaginateTypeDef]
    ) -> PageIterator[ListComponentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2/paginator/ListComponents.html#GreengrassV2.Paginator.ListComponents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators/#listcomponentspaginator)
        """

if TYPE_CHECKING:
    _ListCoreDevicesPaginatorBase = Paginator[ListCoreDevicesResponseTypeDef]
else:
    _ListCoreDevicesPaginatorBase = Paginator  # type: ignore[assignment]

class ListCoreDevicesPaginator(_ListCoreDevicesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2/paginator/ListCoreDevices.html#GreengrassV2.Paginator.ListCoreDevices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators/#listcoredevicespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCoreDevicesRequestPaginateTypeDef]
    ) -> PageIterator[ListCoreDevicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2/paginator/ListCoreDevices.html#GreengrassV2.Paginator.ListCoreDevices.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators/#listcoredevicespaginator)
        """

if TYPE_CHECKING:
    _ListDeploymentsPaginatorBase = Paginator[ListDeploymentsResponseTypeDef]
else:
    _ListDeploymentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDeploymentsPaginator(_ListDeploymentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2/paginator/ListDeployments.html#GreengrassV2.Paginator.ListDeployments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators/#listdeploymentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDeploymentsRequestPaginateTypeDef]
    ) -> PageIterator[ListDeploymentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2/paginator/ListDeployments.html#GreengrassV2.Paginator.ListDeployments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators/#listdeploymentspaginator)
        """

if TYPE_CHECKING:
    _ListEffectiveDeploymentsPaginatorBase = Paginator[ListEffectiveDeploymentsResponseTypeDef]
else:
    _ListEffectiveDeploymentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEffectiveDeploymentsPaginator(_ListEffectiveDeploymentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2/paginator/ListEffectiveDeployments.html#GreengrassV2.Paginator.ListEffectiveDeployments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators/#listeffectivedeploymentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEffectiveDeploymentsRequestPaginateTypeDef]
    ) -> PageIterator[ListEffectiveDeploymentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2/paginator/ListEffectiveDeployments.html#GreengrassV2.Paginator.ListEffectiveDeployments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators/#listeffectivedeploymentspaginator)
        """

if TYPE_CHECKING:
    _ListInstalledComponentsPaginatorBase = Paginator[ListInstalledComponentsResponseTypeDef]
else:
    _ListInstalledComponentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListInstalledComponentsPaginator(_ListInstalledComponentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2/paginator/ListInstalledComponents.html#GreengrassV2.Paginator.ListInstalledComponents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators/#listinstalledcomponentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInstalledComponentsRequestPaginateTypeDef]
    ) -> PageIterator[ListInstalledComponentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2/paginator/ListInstalledComponents.html#GreengrassV2.Paginator.ListInstalledComponents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators/#listinstalledcomponentspaginator)
        """
