"""
Type annotations for qldb service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/literals.html)

Usage::

    ```python
    from mypy_boto3_qldb.literals import EncryptionStatusType

    data: EncryptionStatusType = "ENABLED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "EncryptionStatusType",
    "ErrorCauseType",
    "ExportStatusType",
    "LedgerStateType",
    "PermissionsModeType",
    "S3ObjectEncryptionTypeType",
    "StreamStatusType",
)

EncryptionStatusType = Literal["ENABLED", "KMS_KEY_INACCESSIBLE", "UPDATING"]
ErrorCauseType = Literal["IAM_PERMISSION_REVOKED", "KINESIS_STREAM_NOT_FOUND"]
ExportStatusType = Literal["CANCELLED", "COMPLETED", "IN_PROGRESS"]
LedgerStateType = Literal["ACTIVE", "CREATING", "DELETED", "DELETING"]
PermissionsModeType = Literal["ALLOW_ALL", "STANDARD"]
S3ObjectEncryptionTypeType = Literal["NO_ENCRYPTION", "SSE_KMS", "SSE_S3"]
StreamStatusType = Literal["ACTIVE", "CANCELED", "COMPLETED", "FAILED", "IMPAIRED"]
