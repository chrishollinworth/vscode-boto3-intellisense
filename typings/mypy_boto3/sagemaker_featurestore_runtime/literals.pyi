"""
Type annotations for sagemaker-featurestore-runtime service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_featurestore_runtime/literals.html)

Usage::

    ```python
    from mypy_boto3_sagemaker_featurestore_runtime.literals import DeletionModeType

    data: DeletionModeType = "HardDelete"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DeletionModeType",
    "ExpirationTimeResponseType",
    "TargetStoreType",
    "TtlDurationUnitType",
)

DeletionModeType = Literal["HardDelete", "SoftDelete"]
ExpirationTimeResponseType = Literal["Disabled", "Enabled"]
TargetStoreType = Literal["OfflineStore", "OnlineStore"]
TtlDurationUnitType = Literal["Days", "Hours", "Minutes", "Seconds", "Weeks"]
