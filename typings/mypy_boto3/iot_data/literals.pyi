"""
Type annotations for iot-data service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_data/literals.html)

Usage::

    ```python
    from mypy_boto3_iot_data.literals import ListRetainedMessagesPaginatorName

    data: ListRetainedMessagesPaginatorName = "list_retained_messages"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ListRetainedMessagesPaginatorName",)

ListRetainedMessagesPaginatorName = Literal["list_retained_messages"]
