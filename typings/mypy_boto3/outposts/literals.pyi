"""
Type annotations for outposts service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/literals.html)

Usage::

    ```python
    from mypy_boto3_outposts.literals import OrderStatusType

    data: OrderStatusType = "CANCELLED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("OrderStatusType", "PaymentOptionType", "PaymentTermType")

OrderStatusType = Literal[
    "CANCELLED", "FULFILLED", "INSTALLING", "PENDING", "PROCESSING", "RECEIVED"
]
PaymentOptionType = Literal["ALL_UPFRONT", "NO_UPFRONT", "PARTIAL_UPFRONT"]
PaymentTermType = Literal["THREE_YEARS"]
