"""
Type annotations for connect-contact-lens service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect_contact_lens/literals.html)

Usage::

    ```python
    from mypy_boto3_connect_contact_lens.literals import SentimentValueType

    data: SentimentValueType = "NEGATIVE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("SentimentValueType",)

SentimentValueType = Literal["NEGATIVE", "NEUTRAL", "POSITIVE"]
