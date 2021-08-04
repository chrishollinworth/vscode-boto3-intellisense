"""
Type annotations for support service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support/literals.html)

Usage::

    ```python
    from mypy_boto3_support.literals import DescribeCasesPaginatorName

    data: DescribeCasesPaginatorName = "describe_cases"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("DescribeCasesPaginatorName", "DescribeCommunicationsPaginatorName")

DescribeCasesPaginatorName = Literal["describe_cases"]
DescribeCommunicationsPaginatorName = Literal["describe_communications"]
