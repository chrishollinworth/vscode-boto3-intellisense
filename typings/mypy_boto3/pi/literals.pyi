"""
Type annotations for pi service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pi/literals.html)

Usage::

    ```python
    from mypy_boto3_pi.literals import DetailStatusType

    data: DetailStatusType = "AVAILABLE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("DetailStatusType", "FeatureStatusType", "ServiceTypeType")

DetailStatusType = Literal["AVAILABLE", "PROCESSING", "UNAVAILABLE"]
FeatureStatusType = Literal[
    "DISABLED",
    "DISABLED_PENDING_REBOOT",
    "ENABLED",
    "ENABLED_PENDING_REBOOT",
    "UNKNOWN",
    "UNSUPPORTED",
]
ServiceTypeType = Literal["DOCDB", "RDS"]
