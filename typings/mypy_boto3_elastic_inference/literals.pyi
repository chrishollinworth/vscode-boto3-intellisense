"""
Type annotations for elastic-inference service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastic_inference/literals.html)

Usage::

    ```python
    from mypy_boto3_elastic_inference.literals import DescribeAcceleratorsPaginatorName

    data: DescribeAcceleratorsPaginatorName = "describe_accelerators"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("DescribeAcceleratorsPaginatorName", "LocationTypeType")

DescribeAcceleratorsPaginatorName = Literal["describe_accelerators"]
LocationTypeType = Literal["availability-zone", "availability-zone-id", "region"]
