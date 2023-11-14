"""
Type annotations for migrationhub-config service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhub_config/literals.html)

Usage::

    ```python
    from mypy_boto3_migrationhub_config.literals import TargetTypeType

    data: TargetTypeType = "ACCOUNT"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("TargetTypeType",)

TargetTypeType = Literal["ACCOUNT"]
