"""
Type annotations for fis service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/literals.html)

Usage::

    ```python
    from mypy_boto3_fis.literals import ExperimentActionStatusType

    data: ExperimentActionStatusType = "cancelled"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ExperimentActionStatusType", "ExperimentStatusType")

ExperimentActionStatusType = Literal[
    "cancelled", "completed", "failed", "initiating", "pending", "running", "stopped", "stopping"
]
ExperimentStatusType = Literal[
    "completed", "failed", "initiating", "pending", "running", "stopped", "stopping"
]
