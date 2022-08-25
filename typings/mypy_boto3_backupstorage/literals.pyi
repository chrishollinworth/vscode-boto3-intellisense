"""
Type annotations for backupstorage service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backupstorage/literals.html)

Usage::

    ```python
    from mypy_boto3_backupstorage.literals import DataChecksumAlgorithmType

    data: DataChecksumAlgorithmType = "SHA256"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("DataChecksumAlgorithmType", "SummaryChecksumAlgorithmType")

DataChecksumAlgorithmType = Literal["SHA256"]
SummaryChecksumAlgorithmType = Literal["SUMMARY"]
