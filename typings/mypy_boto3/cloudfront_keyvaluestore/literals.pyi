"""
Type annotations for cloudfront-keyvaluestore service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront_keyvaluestore/literals.html)

Usage::

    ```python
    from mypy_boto3_cloudfront_keyvaluestore.literals import ListKeysPaginatorName

    data: ListKeysPaginatorName = "list_keys"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ListKeysPaginatorName",)

ListKeysPaginatorName = Literal["list_keys"]
