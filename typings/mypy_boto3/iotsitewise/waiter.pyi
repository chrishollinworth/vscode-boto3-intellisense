"""
Type annotations for iotsitewise service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_iotsitewise.client import IoTSiteWiseClient
    from mypy_boto3_iotsitewise.waiter import (
        AssetActiveWaiter,
        AssetModelActiveWaiter,
        AssetModelNotExistsWaiter,
        AssetNotExistsWaiter,
        PortalActiveWaiter,
        PortalNotExistsWaiter,
    )

    session = Session()
    client: IoTSiteWiseClient = session.client("iotsitewise")

    asset_active_waiter: AssetActiveWaiter = client.get_waiter("asset_active")
    asset_model_active_waiter: AssetModelActiveWaiter = client.get_waiter("asset_model_active")
    asset_model_not_exists_waiter: AssetModelNotExistsWaiter = client.get_waiter("asset_model_not_exists")
    asset_not_exists_waiter: AssetNotExistsWaiter = client.get_waiter("asset_not_exists")
    portal_active_waiter: PortalActiveWaiter = client.get_waiter("portal_active")
    portal_not_exists_waiter: PortalNotExistsWaiter = client.get_waiter("portal_not_exists")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    DescribeAssetModelRequestWaitExtraTypeDef,
    DescribeAssetModelRequestWaitTypeDef,
    DescribeAssetRequestWaitExtraTypeDef,
    DescribeAssetRequestWaitTypeDef,
    DescribePortalRequestWaitExtraTypeDef,
    DescribePortalRequestWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "AssetActiveWaiter",
    "AssetModelActiveWaiter",
    "AssetModelNotExistsWaiter",
    "AssetNotExistsWaiter",
    "PortalActiveWaiter",
    "PortalNotExistsWaiter",
)

class AssetActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/waiter/AssetActive.html#IoTSiteWise.Waiter.AssetActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters/#assetactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAssetRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/waiter/AssetActive.html#IoTSiteWise.Waiter.AssetActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters/#assetactivewaiter)
        """

class AssetModelActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/waiter/AssetModelActive.html#IoTSiteWise.Waiter.AssetModelActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters/#assetmodelactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAssetModelRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/waiter/AssetModelActive.html#IoTSiteWise.Waiter.AssetModelActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters/#assetmodelactivewaiter)
        """

class AssetModelNotExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/waiter/AssetModelNotExists.html#IoTSiteWise.Waiter.AssetModelNotExists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters/#assetmodelnotexistswaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAssetModelRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/waiter/AssetModelNotExists.html#IoTSiteWise.Waiter.AssetModelNotExists.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters/#assetmodelnotexistswaiter)
        """

class AssetNotExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/waiter/AssetNotExists.html#IoTSiteWise.Waiter.AssetNotExists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters/#assetnotexistswaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAssetRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/waiter/AssetNotExists.html#IoTSiteWise.Waiter.AssetNotExists.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters/#assetnotexistswaiter)
        """

class PortalActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/waiter/PortalActive.html#IoTSiteWise.Waiter.PortalActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters/#portalactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribePortalRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/waiter/PortalActive.html#IoTSiteWise.Waiter.PortalActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters/#portalactivewaiter)
        """

class PortalNotExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/waiter/PortalNotExists.html#IoTSiteWise.Waiter.PortalNotExists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters/#portalnotexistswaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribePortalRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/waiter/PortalNotExists.html#IoTSiteWise.Waiter.PortalNotExists.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters/#portalnotexistswaiter)
        """
