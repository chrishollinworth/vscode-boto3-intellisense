# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for ecr service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_ecr import ECRClient
    from mypy_boto3_ecr.waiter import (
        ImageScanCompleteWaiter,
        LifecyclePolicyPreviewCompleteWaiter,
    )

    client: ECRClient = boto3.client("ecr")

    image_scan_complete_waiter: ImageScanCompleteWaiter = client.get_waiter("image_scan_complete")
    lifecycle_policy_preview_complete_waiter: LifecyclePolicyPreviewCompleteWaiter = client.get_waiter("lifecycle_policy_preview_complete")
    ```
"""
from typing import List

from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_ecr.type_defs import (
    ImageIdentifierTypeDef,
    LifecyclePolicyPreviewFilterTypeDef,
    WaiterConfigTypeDef,
)

__all__ = ("ImageScanCompleteWaiter", "LifecyclePolicyPreviewCompleteWaiter")


class ImageScanCompleteWaiter(Boto3Waiter):
    """
    [Waiter.ImageScanComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Waiter.ImageScanComplete)
    """

    def wait(
        self,
        repositoryName: str,
        imageId: "ImageIdentifierTypeDef",
        registryId: str = None,
        nextToken: str = None,
        maxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ImageScanComplete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Waiter.ImageScanComplete.wait)
        """


class LifecyclePolicyPreviewCompleteWaiter(Boto3Waiter):
    """
    [Waiter.LifecyclePolicyPreviewComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Waiter.LifecyclePolicyPreviewComplete)
    """

    def wait(
        self,
        repositoryName: str,
        registryId: str = None,
        imageIds: List["ImageIdentifierTypeDef"] = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: LifecyclePolicyPreviewFilterTypeDef = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [LifecyclePolicyPreviewComplete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Waiter.LifecyclePolicyPreviewComplete.wait)
        """
