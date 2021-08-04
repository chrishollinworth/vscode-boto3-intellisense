"""
Type annotations for cognito-sync service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/literals.html)

Usage::

    ```python
    from mypy_boto3_cognito_sync.literals import BulkPublishStatusType

    data: BulkPublishStatusType = "FAILED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("BulkPublishStatusType", "OperationType", "PlatformType", "StreamingStatusType")

BulkPublishStatusType = Literal["FAILED", "IN_PROGRESS", "NOT_STARTED", "SUCCEEDED"]
OperationType = Literal["remove", "replace"]
PlatformType = Literal["ADM", "APNS", "APNS_SANDBOX", "GCM"]
StreamingStatusType = Literal["DISABLED", "ENABLED"]
