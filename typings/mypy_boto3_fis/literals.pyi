"""
Type annotations for fis service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/literals.html)

Usage::

    ```python
    from mypy_boto3_fis.literals import AccountTargetingType

    data: AccountTargetingType = "multi-account"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccountTargetingType",
    "ActionsModeType",
    "EmptyTargetResolutionModeType",
    "ExperimentActionStatusType",
    "ExperimentStatusType",
)

AccountTargetingType = Literal["multi-account", "single-account"]
ActionsModeType = Literal["run-all", "skip-all"]
EmptyTargetResolutionModeType = Literal["fail", "skip"]
ExperimentActionStatusType = Literal[
    "cancelled",
    "completed",
    "failed",
    "initiating",
    "pending",
    "running",
    "skipped",
    "stopped",
    "stopping",
]
ExperimentStatusType = Literal[
    "completed", "failed", "initiating", "pending", "running", "stopped", "stopping"
]
