"""
Type annotations for ebs service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ebs/literals.html)

Usage::

    ```python
    from mypy_boto3_ebs.literals import ChecksumAggregationMethodType

    data: ChecksumAggregationMethodType = "LINEAR"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ChecksumAggregationMethodType", "ChecksumAlgorithmType", "StatusType")

ChecksumAggregationMethodType = Literal["LINEAR"]
ChecksumAlgorithmType = Literal["SHA256"]
StatusType = Literal["completed", "error", "pending"]
