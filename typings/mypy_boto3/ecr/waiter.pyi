"""
Type annotations for ecr service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/waiters.html)

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

from .type_defs import (
    ImageIdentifierTypeDef,
    LifecyclePolicyPreviewFilterTypeDef,
    WaiterConfigTypeDef,
)

__all__ = ("ImageScanCompleteWaiter", "LifecyclePolicyPreviewCompleteWaiter")

class ImageScanCompleteWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ecr.html#ECR.Waiter.ImageScanComplete)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/waiters.html#imagescancompletewaiter)
    """

    def wait(
        self,
        *,
        repositoryName: str,
        imageId: "ImageIdentifierTypeDef",
        registryId: str = None,
        nextToken: str = None,
        maxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ecr.html#ECR.Waiter.ImageScanComplete.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/waiters.html#imagescancompletewaiter)
        """

class LifecyclePolicyPreviewCompleteWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ecr.html#ECR.Waiter.LifecyclePolicyPreviewComplete)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/waiters.html#lifecyclepolicypreviewcompletewaiter)
    """

    def wait(
        self,
        *,
        repositoryName: str,
        registryId: str = None,
        imageIds: List["ImageIdentifierTypeDef"] = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: "LifecyclePolicyPreviewFilterTypeDef" = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ecr.html#ECR.Waiter.LifecyclePolicyPreviewComplete.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/waiters.html#lifecyclepolicypreviewcompletewaiter)
        """
