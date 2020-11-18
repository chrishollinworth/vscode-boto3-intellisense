# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for iotsitewise service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_iotsitewise import IoTSiteWiseClient
    from mypy_boto3_iotsitewise.waiter import (
        AssetActiveWaiter,
        AssetModelActiveWaiter,
        AssetModelNotExistsWaiter,
        AssetNotExistsWaiter,
        PortalActiveWaiter,
        PortalNotExistsWaiter,
    )

    client: IoTSiteWiseClient = boto3.client("iotsitewise")

    asset_active_waiter: AssetActiveWaiter = client.get_waiter("asset_active")
    asset_model_active_waiter: AssetModelActiveWaiter = client.get_waiter("asset_model_active")
    asset_model_not_exists_waiter: AssetModelNotExistsWaiter = client.get_waiter("asset_model_not_exists")
    asset_not_exists_waiter: AssetNotExistsWaiter = client.get_waiter("asset_not_exists")
    portal_active_waiter: PortalActiveWaiter = client.get_waiter("portal_active")
    portal_not_exists_waiter: PortalNotExistsWaiter = client.get_waiter("portal_not_exists")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_iotsitewise.type_defs import WaiterConfigTypeDef

__all__ = (
    "AssetActiveWaiter",
    "AssetModelActiveWaiter",
    "AssetModelNotExistsWaiter",
    "AssetNotExistsWaiter",
    "PortalActiveWaiter",
    "PortalNotExistsWaiter",
)


class AssetActiveWaiter(Boto3Waiter):
    """
    [Waiter.AssetActive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotsitewise.html#IoTSiteWise.Waiter.AssetActive)
    """

    def wait(self, assetId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [AssetActive.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotsitewise.html#IoTSiteWise.Waiter.AssetActive.wait)
        """


class AssetModelActiveWaiter(Boto3Waiter):
    """
    [Waiter.AssetModelActive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotsitewise.html#IoTSiteWise.Waiter.AssetModelActive)
    """

    def wait(self, assetModelId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [AssetModelActive.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotsitewise.html#IoTSiteWise.Waiter.AssetModelActive.wait)
        """


class AssetModelNotExistsWaiter(Boto3Waiter):
    """
    [Waiter.AssetModelNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotsitewise.html#IoTSiteWise.Waiter.AssetModelNotExists)
    """

    def wait(self, assetModelId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [AssetModelNotExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotsitewise.html#IoTSiteWise.Waiter.AssetModelNotExists.wait)
        """


class AssetNotExistsWaiter(Boto3Waiter):
    """
    [Waiter.AssetNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotsitewise.html#IoTSiteWise.Waiter.AssetNotExists)
    """

    def wait(self, assetId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [AssetNotExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotsitewise.html#IoTSiteWise.Waiter.AssetNotExists.wait)
        """


class PortalActiveWaiter(Boto3Waiter):
    """
    [Waiter.PortalActive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotsitewise.html#IoTSiteWise.Waiter.PortalActive)
    """

    def wait(self, portalId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [PortalActive.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotsitewise.html#IoTSiteWise.Waiter.PortalActive.wait)
        """


class PortalNotExistsWaiter(Boto3Waiter):
    """
    [Waiter.PortalNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotsitewise.html#IoTSiteWise.Waiter.PortalNotExists)
    """

    def wait(self, portalId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [PortalNotExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotsitewise.html#IoTSiteWise.Waiter.PortalNotExists.wait)
        """
