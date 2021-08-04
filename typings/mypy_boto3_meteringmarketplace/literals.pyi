"""
Type annotations for meteringmarketplace service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/literals.html)

Usage::

    ```python
    from mypy_boto3_meteringmarketplace.literals import UsageRecordResultStatusType

    data: UsageRecordResultStatusType = "CustomerNotSubscribed"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("UsageRecordResultStatusType",)

UsageRecordResultStatusType = Literal["CustomerNotSubscribed", "DuplicateRecord", "Success"]
