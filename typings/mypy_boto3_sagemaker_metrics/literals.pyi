"""
Type annotations for sagemaker-metrics service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_metrics/literals.html)

Usage::

    ```python
    from mypy_boto3_sagemaker_metrics.literals import PutMetricsErrorCodeType

    data: PutMetricsErrorCodeType = "CONFLICT_ERROR"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("PutMetricsErrorCodeType",)

PutMetricsErrorCodeType = Literal[
    "CONFLICT_ERROR", "INTERNAL_ERROR", "METRIC_LIMIT_EXCEEDED", "VALIDATION_ERROR"
]
