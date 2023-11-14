"""
Type annotations for glacier service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/literals.html)

Usage::

    ```python
    from mypy_boto3_glacier.literals import ActionCodeType

    data: ActionCodeType = "ArchiveRetrieval"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActionCodeType",
    "CannedACLType",
    "EncryptionTypeType",
    "ExpressionTypeType",
    "FileHeaderInfoType",
    "ListJobsPaginatorName",
    "ListMultipartUploadsPaginatorName",
    "ListPartsPaginatorName",
    "ListVaultsPaginatorName",
    "PermissionType",
    "QuoteFieldsType",
    "StatusCodeType",
    "StorageClassType",
    "TypeType",
    "VaultExistsWaiterName",
    "VaultNotExistsWaiterName",
)

ActionCodeType = Literal["ArchiveRetrieval", "InventoryRetrieval", "Select"]
CannedACLType = Literal[
    "authenticated-read",
    "aws-exec-read",
    "bucket-owner-full-control",
    "bucket-owner-read",
    "private",
    "public-read",
    "public-read-write",
]
EncryptionTypeType = Literal["AES256", "aws:kms"]
ExpressionTypeType = Literal["SQL"]
FileHeaderInfoType = Literal["IGNORE", "NONE", "USE"]
ListJobsPaginatorName = Literal["list_jobs"]
ListMultipartUploadsPaginatorName = Literal["list_multipart_uploads"]
ListPartsPaginatorName = Literal["list_parts"]
ListVaultsPaginatorName = Literal["list_vaults"]
PermissionType = Literal["FULL_CONTROL", "READ", "READ_ACP", "WRITE", "WRITE_ACP"]
QuoteFieldsType = Literal["ALWAYS", "ASNEEDED"]
StatusCodeType = Literal["Failed", "InProgress", "Succeeded"]
StorageClassType = Literal["REDUCED_REDUNDANCY", "STANDARD", "STANDARD_IA"]
TypeType = Literal["AmazonCustomerByEmail", "CanonicalUser", "Group"]
VaultExistsWaiterName = Literal["vault_exists"]
VaultNotExistsWaiterName = Literal["vault_not_exists"]
