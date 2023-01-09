"""
Type annotations for sagemaker-featurestore-runtime service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_featurestore_runtime/literals.html)

Usage::

    ```python
    from mypy_boto3_sagemaker_featurestore_runtime.literals import TargetStoreType

    data: TargetStoreType = "OfflineStore"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("TargetStoreType",)

TargetStoreType = Literal["OfflineStore", "OnlineStore"]