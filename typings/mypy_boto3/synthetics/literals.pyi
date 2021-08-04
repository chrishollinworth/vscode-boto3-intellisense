"""
Type annotations for synthetics service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/literals.html)

Usage::

    ```python
    from mypy_boto3_synthetics.literals import CanaryRunStateReasonCodeType

    data: CanaryRunStateReasonCodeType = "CANARY_FAILURE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CanaryRunStateReasonCodeType",
    "CanaryRunStateType",
    "CanaryStateReasonCodeType",
    "CanaryStateType",
)

CanaryRunStateReasonCodeType = Literal["CANARY_FAILURE", "EXECUTION_FAILURE"]
CanaryRunStateType = Literal["FAILED", "PASSED", "RUNNING"]
CanaryStateReasonCodeType = Literal["INVALID_PERMISSIONS"]
CanaryStateType = Literal[
    "CREATING",
    "DELETING",
    "ERROR",
    "READY",
    "RUNNING",
    "STARTING",
    "STOPPED",
    "STOPPING",
    "UPDATING",
]
