"""
Type annotations for inspector-scan service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector_scan/literals.html)

Usage::

    ```python
    from mypy_boto3_inspector_scan.literals import OutputFormatType

    data: OutputFormatType = "CYCLONE_DX_1_5"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("OutputFormatType",)

OutputFormatType = Literal["CYCLONE_DX_1_5", "INSPECTOR"]
