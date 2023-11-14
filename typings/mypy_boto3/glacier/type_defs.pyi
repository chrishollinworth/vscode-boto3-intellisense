"""
Type annotations for glacier service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/type_defs.html)

Usage::

    ```python
    from mypy_boto3_glacier.type_defs import AbortMultipartUploadInputRequestTypeDef

    data: AbortMultipartUploadInputRequestTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ActionCodeType,
    CannedACLType,
    EncryptionTypeType,
    FileHeaderInfoType,
    PermissionType,
    QuoteFieldsType,
    StatusCodeType,
    StorageClassType,
    TypeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AbortMultipartUploadInputRequestTypeDef",
    "AbortVaultLockInputRequestTypeDef",
    "AccountVaultRequestTypeDef",
    "AddTagsToVaultInputRequestTypeDef",
    "ArchiveCreationOutputTypeDef",
    "CSVInputTypeDef",
    "CSVOutputTypeDef",
    "CompleteMultipartUploadInputMultipartUploadTypeDef",
    "CompleteMultipartUploadInputRequestTypeDef",
    "CompleteVaultLockInputRequestTypeDef",
    "CreateVaultInputAccountTypeDef",
    "CreateVaultInputRequestTypeDef",
    "CreateVaultInputServiceResourceTypeDef",
    "CreateVaultOutputTypeDef",
    "DataRetrievalPolicyTypeDef",
    "DataRetrievalRuleTypeDef",
    "DeleteArchiveInputRequestTypeDef",
    "DeleteVaultAccessPolicyInputRequestTypeDef",
    "DeleteVaultInputRequestTypeDef",
    "DeleteVaultNotificationsInputRequestTypeDef",
    "DescribeJobInputRequestTypeDef",
    "DescribeVaultInputRequestTypeDef",
    "DescribeVaultOutputResponseMetadataTypeDef",
    "DescribeVaultOutputTypeDef",
    "EncryptionTypeDef",
    "GetDataRetrievalPolicyInputRequestTypeDef",
    "GetDataRetrievalPolicyOutputTypeDef",
    "GetJobOutputInputJobTypeDef",
    "GetJobOutputInputRequestTypeDef",
    "GetJobOutputOutputTypeDef",
    "GetVaultAccessPolicyInputRequestTypeDef",
    "GetVaultAccessPolicyOutputTypeDef",
    "GetVaultLockInputRequestTypeDef",
    "GetVaultLockOutputTypeDef",
    "GetVaultNotificationsInputRequestTypeDef",
    "GetVaultNotificationsOutputTypeDef",
    "GlacierJobDescriptionResponseMetadataTypeDef",
    "GlacierJobDescriptionTypeDef",
    "GrantTypeDef",
    "GranteeTypeDef",
    "InitiateJobInputArchiveTypeDef",
    "InitiateJobInputRequestTypeDef",
    "InitiateJobInputVaultTypeDef",
    "InitiateJobOutputTypeDef",
    "InitiateMultipartUploadInputRequestTypeDef",
    "InitiateMultipartUploadInputVaultTypeDef",
    "InitiateMultipartUploadOutputTypeDef",
    "InitiateVaultLockInputRequestTypeDef",
    "InitiateVaultLockOutputTypeDef",
    "InputSerializationTypeDef",
    "InventoryRetrievalJobDescriptionTypeDef",
    "InventoryRetrievalJobInputTypeDef",
    "JobParametersTypeDef",
    "ListJobsInputRequestTypeDef",
    "ListJobsOutputTypeDef",
    "ListMultipartUploadsInputRequestTypeDef",
    "ListMultipartUploadsOutputTypeDef",
    "ListPartsInputMultipartUploadTypeDef",
    "ListPartsInputRequestTypeDef",
    "ListPartsOutputTypeDef",
    "ListProvisionedCapacityInputRequestTypeDef",
    "ListProvisionedCapacityOutputTypeDef",
    "ListTagsForVaultInputRequestTypeDef",
    "ListTagsForVaultOutputTypeDef",
    "ListVaultsInputRequestTypeDef",
    "ListVaultsOutputTypeDef",
    "OutputLocationTypeDef",
    "OutputSerializationTypeDef",
    "PaginatorConfigTypeDef",
    "PartListElementTypeDef",
    "ProvisionedCapacityDescriptionTypeDef",
    "PurchaseProvisionedCapacityInputRequestTypeDef",
    "PurchaseProvisionedCapacityOutputTypeDef",
    "RemoveTagsFromVaultInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "SelectParametersTypeDef",
    "ServiceResourceAccountRequestTypeDef",
    "ServiceResourceArchiveRequestTypeDef",
    "ServiceResourceJobRequestTypeDef",
    "ServiceResourceMultipartUploadRequestTypeDef",
    "ServiceResourceNotificationRequestTypeDef",
    "ServiceResourceVaultRequestTypeDef",
    "SetDataRetrievalPolicyInputRequestTypeDef",
    "SetVaultAccessPolicyInputRequestTypeDef",
    "SetVaultNotificationsInputNotificationTypeDef",
    "SetVaultNotificationsInputRequestTypeDef",
    "UploadArchiveInputRequestTypeDef",
    "UploadArchiveInputVaultTypeDef",
    "UploadListElementTypeDef",
    "UploadMultipartPartInputMultipartUploadTypeDef",
    "UploadMultipartPartInputRequestTypeDef",
    "UploadMultipartPartOutputTypeDef",
    "VaultAccessPolicyTypeDef",
    "VaultArchiveRequestTypeDef",
    "VaultJobRequestTypeDef",
    "VaultLockPolicyTypeDef",
    "VaultMultipartUploadRequestTypeDef",
    "VaultNotificationConfigTypeDef",
    "WaiterConfigTypeDef",
)

AbortMultipartUploadInputRequestTypeDef = TypedDict(
    "AbortMultipartUploadInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
        "uploadId": str,
    },
)

AbortVaultLockInputRequestTypeDef = TypedDict(
    "AbortVaultLockInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)

AccountVaultRequestTypeDef = TypedDict(
    "AccountVaultRequestTypeDef",
    {
        "name": str,
    },
)

_RequiredAddTagsToVaultInputRequestTypeDef = TypedDict(
    "_RequiredAddTagsToVaultInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)
_OptionalAddTagsToVaultInputRequestTypeDef = TypedDict(
    "_OptionalAddTagsToVaultInputRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

class AddTagsToVaultInputRequestTypeDef(
    _RequiredAddTagsToVaultInputRequestTypeDef, _OptionalAddTagsToVaultInputRequestTypeDef
):
    pass

ArchiveCreationOutputTypeDef = TypedDict(
    "ArchiveCreationOutputTypeDef",
    {
        "location": str,
        "checksum": str,
        "archiveId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CSVInputTypeDef = TypedDict(
    "CSVInputTypeDef",
    {
        "FileHeaderInfo": FileHeaderInfoType,
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)

CSVOutputTypeDef = TypedDict(
    "CSVOutputTypeDef",
    {
        "QuoteFields": QuoteFieldsType,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)

CompleteMultipartUploadInputMultipartUploadTypeDef = TypedDict(
    "CompleteMultipartUploadInputMultipartUploadTypeDef",
    {
        "archiveSize": str,
        "checksum": str,
    },
    total=False,
)

_RequiredCompleteMultipartUploadInputRequestTypeDef = TypedDict(
    "_RequiredCompleteMultipartUploadInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
        "uploadId": str,
    },
)
_OptionalCompleteMultipartUploadInputRequestTypeDef = TypedDict(
    "_OptionalCompleteMultipartUploadInputRequestTypeDef",
    {
        "archiveSize": str,
        "checksum": str,
    },
    total=False,
)

class CompleteMultipartUploadInputRequestTypeDef(
    _RequiredCompleteMultipartUploadInputRequestTypeDef,
    _OptionalCompleteMultipartUploadInputRequestTypeDef,
):
    pass

CompleteVaultLockInputRequestTypeDef = TypedDict(
    "CompleteVaultLockInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
        "lockId": str,
    },
)

CreateVaultInputAccountTypeDef = TypedDict(
    "CreateVaultInputAccountTypeDef",
    {
        "vaultName": str,
    },
)

CreateVaultInputRequestTypeDef = TypedDict(
    "CreateVaultInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)

CreateVaultInputServiceResourceTypeDef = TypedDict(
    "CreateVaultInputServiceResourceTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)

CreateVaultOutputTypeDef = TypedDict(
    "CreateVaultOutputTypeDef",
    {
        "location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataRetrievalPolicyTypeDef = TypedDict(
    "DataRetrievalPolicyTypeDef",
    {
        "Rules": List["DataRetrievalRuleTypeDef"],
    },
    total=False,
)

DataRetrievalRuleTypeDef = TypedDict(
    "DataRetrievalRuleTypeDef",
    {
        "Strategy": str,
        "BytesPerHour": int,
    },
    total=False,
)

DeleteArchiveInputRequestTypeDef = TypedDict(
    "DeleteArchiveInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
        "archiveId": str,
    },
)

DeleteVaultAccessPolicyInputRequestTypeDef = TypedDict(
    "DeleteVaultAccessPolicyInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)

DeleteVaultInputRequestTypeDef = TypedDict(
    "DeleteVaultInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)

DeleteVaultNotificationsInputRequestTypeDef = TypedDict(
    "DeleteVaultNotificationsInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)

DescribeJobInputRequestTypeDef = TypedDict(
    "DescribeJobInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
        "jobId": str,
    },
)

DescribeVaultInputRequestTypeDef = TypedDict(
    "DescribeVaultInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)

DescribeVaultOutputResponseMetadataTypeDef = TypedDict(
    "DescribeVaultOutputResponseMetadataTypeDef",
    {
        "VaultARN": str,
        "VaultName": str,
        "CreationDate": str,
        "LastInventoryDate": str,
        "NumberOfArchives": int,
        "SizeInBytes": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVaultOutputTypeDef = TypedDict(
    "DescribeVaultOutputTypeDef",
    {
        "VaultARN": str,
        "VaultName": str,
        "CreationDate": str,
        "LastInventoryDate": str,
        "NumberOfArchives": int,
        "SizeInBytes": int,
    },
    total=False,
)

EncryptionTypeDef = TypedDict(
    "EncryptionTypeDef",
    {
        "EncryptionType": EncryptionTypeType,
        "KMSKeyId": str,
        "KMSContext": str,
    },
    total=False,
)

GetDataRetrievalPolicyInputRequestTypeDef = TypedDict(
    "GetDataRetrievalPolicyInputRequestTypeDef",
    {
        "accountId": str,
    },
)

GetDataRetrievalPolicyOutputTypeDef = TypedDict(
    "GetDataRetrievalPolicyOutputTypeDef",
    {
        "Policy": "DataRetrievalPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobOutputInputJobTypeDef = TypedDict(
    "GetJobOutputInputJobTypeDef",
    {
        "range": str,
    },
    total=False,
)

_RequiredGetJobOutputInputRequestTypeDef = TypedDict(
    "_RequiredGetJobOutputInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
        "jobId": str,
    },
)
_OptionalGetJobOutputInputRequestTypeDef = TypedDict(
    "_OptionalGetJobOutputInputRequestTypeDef",
    {
        "range": str,
    },
    total=False,
)

class GetJobOutputInputRequestTypeDef(
    _RequiredGetJobOutputInputRequestTypeDef, _OptionalGetJobOutputInputRequestTypeDef
):
    pass

GetJobOutputOutputTypeDef = TypedDict(
    "GetJobOutputOutputTypeDef",
    {
        "body": StreamingBody,
        "checksum": str,
        "status": int,
        "contentRange": str,
        "acceptRanges": str,
        "contentType": str,
        "archiveDescription": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVaultAccessPolicyInputRequestTypeDef = TypedDict(
    "GetVaultAccessPolicyInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)

GetVaultAccessPolicyOutputTypeDef = TypedDict(
    "GetVaultAccessPolicyOutputTypeDef",
    {
        "policy": "VaultAccessPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVaultLockInputRequestTypeDef = TypedDict(
    "GetVaultLockInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)

GetVaultLockOutputTypeDef = TypedDict(
    "GetVaultLockOutputTypeDef",
    {
        "Policy": str,
        "State": str,
        "ExpirationDate": str,
        "CreationDate": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVaultNotificationsInputRequestTypeDef = TypedDict(
    "GetVaultNotificationsInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)

GetVaultNotificationsOutputTypeDef = TypedDict(
    "GetVaultNotificationsOutputTypeDef",
    {
        "vaultNotificationConfig": "VaultNotificationConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GlacierJobDescriptionResponseMetadataTypeDef = TypedDict(
    "GlacierJobDescriptionResponseMetadataTypeDef",
    {
        "JobId": str,
        "JobDescription": str,
        "Action": ActionCodeType,
        "ArchiveId": str,
        "VaultARN": str,
        "CreationDate": str,
        "Completed": bool,
        "StatusCode": StatusCodeType,
        "StatusMessage": str,
        "ArchiveSizeInBytes": int,
        "InventorySizeInBytes": int,
        "SNSTopic": str,
        "CompletionDate": str,
        "SHA256TreeHash": str,
        "ArchiveSHA256TreeHash": str,
        "RetrievalByteRange": str,
        "Tier": str,
        "InventoryRetrievalParameters": "InventoryRetrievalJobDescriptionTypeDef",
        "JobOutputPath": str,
        "SelectParameters": "SelectParametersTypeDef",
        "OutputLocation": "OutputLocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GlacierJobDescriptionTypeDef = TypedDict(
    "GlacierJobDescriptionTypeDef",
    {
        "JobId": str,
        "JobDescription": str,
        "Action": ActionCodeType,
        "ArchiveId": str,
        "VaultARN": str,
        "CreationDate": str,
        "Completed": bool,
        "StatusCode": StatusCodeType,
        "StatusMessage": str,
        "ArchiveSizeInBytes": int,
        "InventorySizeInBytes": int,
        "SNSTopic": str,
        "CompletionDate": str,
        "SHA256TreeHash": str,
        "ArchiveSHA256TreeHash": str,
        "RetrievalByteRange": str,
        "Tier": str,
        "InventoryRetrievalParameters": "InventoryRetrievalJobDescriptionTypeDef",
        "JobOutputPath": str,
        "SelectParameters": "SelectParametersTypeDef",
        "OutputLocation": "OutputLocationTypeDef",
    },
    total=False,
)

GrantTypeDef = TypedDict(
    "GrantTypeDef",
    {
        "Grantee": "GranteeTypeDef",
        "Permission": PermissionType,
    },
    total=False,
)

_RequiredGranteeTypeDef = TypedDict(
    "_RequiredGranteeTypeDef",
    {
        "Type": TypeType,
    },
)
_OptionalGranteeTypeDef = TypedDict(
    "_OptionalGranteeTypeDef",
    {
        "DisplayName": str,
        "URI": str,
        "ID": str,
        "EmailAddress": str,
    },
    total=False,
)

class GranteeTypeDef(_RequiredGranteeTypeDef, _OptionalGranteeTypeDef):
    pass

InitiateJobInputArchiveTypeDef = TypedDict(
    "InitiateJobInputArchiveTypeDef",
    {
        "jobParameters": "JobParametersTypeDef",
    },
    total=False,
)

_RequiredInitiateJobInputRequestTypeDef = TypedDict(
    "_RequiredInitiateJobInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)
_OptionalInitiateJobInputRequestTypeDef = TypedDict(
    "_OptionalInitiateJobInputRequestTypeDef",
    {
        "jobParameters": "JobParametersTypeDef",
    },
    total=False,
)

class InitiateJobInputRequestTypeDef(
    _RequiredInitiateJobInputRequestTypeDef, _OptionalInitiateJobInputRequestTypeDef
):
    pass

InitiateJobInputVaultTypeDef = TypedDict(
    "InitiateJobInputVaultTypeDef",
    {
        "jobParameters": "JobParametersTypeDef",
    },
    total=False,
)

InitiateJobOutputTypeDef = TypedDict(
    "InitiateJobOutputTypeDef",
    {
        "location": str,
        "jobId": str,
        "jobOutputPath": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredInitiateMultipartUploadInputRequestTypeDef = TypedDict(
    "_RequiredInitiateMultipartUploadInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)
_OptionalInitiateMultipartUploadInputRequestTypeDef = TypedDict(
    "_OptionalInitiateMultipartUploadInputRequestTypeDef",
    {
        "archiveDescription": str,
        "partSize": str,
    },
    total=False,
)

class InitiateMultipartUploadInputRequestTypeDef(
    _RequiredInitiateMultipartUploadInputRequestTypeDef,
    _OptionalInitiateMultipartUploadInputRequestTypeDef,
):
    pass

InitiateMultipartUploadInputVaultTypeDef = TypedDict(
    "InitiateMultipartUploadInputVaultTypeDef",
    {
        "archiveDescription": str,
        "partSize": str,
    },
    total=False,
)

InitiateMultipartUploadOutputTypeDef = TypedDict(
    "InitiateMultipartUploadOutputTypeDef",
    {
        "location": str,
        "uploadId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredInitiateVaultLockInputRequestTypeDef = TypedDict(
    "_RequiredInitiateVaultLockInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)
_OptionalInitiateVaultLockInputRequestTypeDef = TypedDict(
    "_OptionalInitiateVaultLockInputRequestTypeDef",
    {
        "policy": "VaultLockPolicyTypeDef",
    },
    total=False,
)

class InitiateVaultLockInputRequestTypeDef(
    _RequiredInitiateVaultLockInputRequestTypeDef, _OptionalInitiateVaultLockInputRequestTypeDef
):
    pass

InitiateVaultLockOutputTypeDef = TypedDict(
    "InitiateVaultLockOutputTypeDef",
    {
        "lockId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputSerializationTypeDef = TypedDict(
    "InputSerializationTypeDef",
    {
        "csv": "CSVInputTypeDef",
    },
    total=False,
)

InventoryRetrievalJobDescriptionTypeDef = TypedDict(
    "InventoryRetrievalJobDescriptionTypeDef",
    {
        "Format": str,
        "StartDate": str,
        "EndDate": str,
        "Limit": str,
        "Marker": str,
    },
    total=False,
)

InventoryRetrievalJobInputTypeDef = TypedDict(
    "InventoryRetrievalJobInputTypeDef",
    {
        "StartDate": str,
        "EndDate": str,
        "Limit": str,
        "Marker": str,
    },
    total=False,
)

JobParametersTypeDef = TypedDict(
    "JobParametersTypeDef",
    {
        "Format": str,
        "Type": str,
        "ArchiveId": str,
        "Description": str,
        "SNSTopic": str,
        "RetrievalByteRange": str,
        "Tier": str,
        "InventoryRetrievalParameters": "InventoryRetrievalJobInputTypeDef",
        "SelectParameters": "SelectParametersTypeDef",
        "OutputLocation": "OutputLocationTypeDef",
    },
    total=False,
)

_RequiredListJobsInputRequestTypeDef = TypedDict(
    "_RequiredListJobsInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)
_OptionalListJobsInputRequestTypeDef = TypedDict(
    "_OptionalListJobsInputRequestTypeDef",
    {
        "limit": str,
        "marker": str,
        "statuscode": str,
        "completed": str,
    },
    total=False,
)

class ListJobsInputRequestTypeDef(
    _RequiredListJobsInputRequestTypeDef, _OptionalListJobsInputRequestTypeDef
):
    pass

ListJobsOutputTypeDef = TypedDict(
    "ListJobsOutputTypeDef",
    {
        "JobList": List["GlacierJobDescriptionTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMultipartUploadsInputRequestTypeDef = TypedDict(
    "_RequiredListMultipartUploadsInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)
_OptionalListMultipartUploadsInputRequestTypeDef = TypedDict(
    "_OptionalListMultipartUploadsInputRequestTypeDef",
    {
        "marker": str,
        "limit": str,
    },
    total=False,
)

class ListMultipartUploadsInputRequestTypeDef(
    _RequiredListMultipartUploadsInputRequestTypeDef,
    _OptionalListMultipartUploadsInputRequestTypeDef,
):
    pass

ListMultipartUploadsOutputTypeDef = TypedDict(
    "ListMultipartUploadsOutputTypeDef",
    {
        "UploadsList": List["UploadListElementTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPartsInputMultipartUploadTypeDef = TypedDict(
    "ListPartsInputMultipartUploadTypeDef",
    {
        "marker": str,
        "limit": str,
    },
    total=False,
)

_RequiredListPartsInputRequestTypeDef = TypedDict(
    "_RequiredListPartsInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
        "uploadId": str,
    },
)
_OptionalListPartsInputRequestTypeDef = TypedDict(
    "_OptionalListPartsInputRequestTypeDef",
    {
        "marker": str,
        "limit": str,
    },
    total=False,
)

class ListPartsInputRequestTypeDef(
    _RequiredListPartsInputRequestTypeDef, _OptionalListPartsInputRequestTypeDef
):
    pass

ListPartsOutputTypeDef = TypedDict(
    "ListPartsOutputTypeDef",
    {
        "MultipartUploadId": str,
        "VaultARN": str,
        "ArchiveDescription": str,
        "PartSizeInBytes": int,
        "CreationDate": str,
        "Parts": List["PartListElementTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProvisionedCapacityInputRequestTypeDef = TypedDict(
    "ListProvisionedCapacityInputRequestTypeDef",
    {
        "accountId": str,
    },
)

ListProvisionedCapacityOutputTypeDef = TypedDict(
    "ListProvisionedCapacityOutputTypeDef",
    {
        "ProvisionedCapacityList": List["ProvisionedCapacityDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForVaultInputRequestTypeDef = TypedDict(
    "ListTagsForVaultInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)

ListTagsForVaultOutputTypeDef = TypedDict(
    "ListTagsForVaultOutputTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListVaultsInputRequestTypeDef = TypedDict(
    "_RequiredListVaultsInputRequestTypeDef",
    {
        "accountId": str,
    },
)
_OptionalListVaultsInputRequestTypeDef = TypedDict(
    "_OptionalListVaultsInputRequestTypeDef",
    {
        "marker": str,
        "limit": str,
    },
    total=False,
)

class ListVaultsInputRequestTypeDef(
    _RequiredListVaultsInputRequestTypeDef, _OptionalListVaultsInputRequestTypeDef
):
    pass

ListVaultsOutputTypeDef = TypedDict(
    "ListVaultsOutputTypeDef",
    {
        "VaultList": List["DescribeVaultOutputTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OutputLocationTypeDef = TypedDict(
    "OutputLocationTypeDef",
    {
        "S3": "S3LocationTypeDef",
    },
    total=False,
)

OutputSerializationTypeDef = TypedDict(
    "OutputSerializationTypeDef",
    {
        "csv": "CSVOutputTypeDef",
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PartListElementTypeDef = TypedDict(
    "PartListElementTypeDef",
    {
        "RangeInBytes": str,
        "SHA256TreeHash": str,
    },
    total=False,
)

ProvisionedCapacityDescriptionTypeDef = TypedDict(
    "ProvisionedCapacityDescriptionTypeDef",
    {
        "CapacityId": str,
        "StartDate": str,
        "ExpirationDate": str,
    },
    total=False,
)

PurchaseProvisionedCapacityInputRequestTypeDef = TypedDict(
    "PurchaseProvisionedCapacityInputRequestTypeDef",
    {
        "accountId": str,
    },
)

PurchaseProvisionedCapacityOutputTypeDef = TypedDict(
    "PurchaseProvisionedCapacityOutputTypeDef",
    {
        "capacityId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRemoveTagsFromVaultInputRequestTypeDef = TypedDict(
    "_RequiredRemoveTagsFromVaultInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)
_OptionalRemoveTagsFromVaultInputRequestTypeDef = TypedDict(
    "_OptionalRemoveTagsFromVaultInputRequestTypeDef",
    {
        "TagKeys": List[str],
    },
    total=False,
)

class RemoveTagsFromVaultInputRequestTypeDef(
    _RequiredRemoveTagsFromVaultInputRequestTypeDef, _OptionalRemoveTagsFromVaultInputRequestTypeDef
):
    pass

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "BucketName": str,
        "Prefix": str,
        "Encryption": "EncryptionTypeDef",
        "CannedACL": CannedACLType,
        "AccessControlList": List["GrantTypeDef"],
        "Tagging": Dict[str, str],
        "UserMetadata": Dict[str, str],
        "StorageClass": StorageClassType,
    },
    total=False,
)

SelectParametersTypeDef = TypedDict(
    "SelectParametersTypeDef",
    {
        "InputSerialization": "InputSerializationTypeDef",
        "ExpressionType": Literal["SQL"],
        "Expression": str,
        "OutputSerialization": "OutputSerializationTypeDef",
    },
    total=False,
)

ServiceResourceAccountRequestTypeDef = TypedDict(
    "ServiceResourceAccountRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceArchiveRequestTypeDef = TypedDict(
    "ServiceResourceArchiveRequestTypeDef",
    {
        "account_id": str,
        "vault_name": str,
        "id": str,
    },
)

ServiceResourceJobRequestTypeDef = TypedDict(
    "ServiceResourceJobRequestTypeDef",
    {
        "account_id": str,
        "vault_name": str,
        "id": str,
    },
)

ServiceResourceMultipartUploadRequestTypeDef = TypedDict(
    "ServiceResourceMultipartUploadRequestTypeDef",
    {
        "account_id": str,
        "vault_name": str,
        "id": str,
    },
)

ServiceResourceNotificationRequestTypeDef = TypedDict(
    "ServiceResourceNotificationRequestTypeDef",
    {
        "account_id": str,
        "vault_name": str,
    },
)

ServiceResourceVaultRequestTypeDef = TypedDict(
    "ServiceResourceVaultRequestTypeDef",
    {
        "account_id": str,
        "name": str,
    },
)

_RequiredSetDataRetrievalPolicyInputRequestTypeDef = TypedDict(
    "_RequiredSetDataRetrievalPolicyInputRequestTypeDef",
    {
        "accountId": str,
    },
)
_OptionalSetDataRetrievalPolicyInputRequestTypeDef = TypedDict(
    "_OptionalSetDataRetrievalPolicyInputRequestTypeDef",
    {
        "Policy": "DataRetrievalPolicyTypeDef",
    },
    total=False,
)

class SetDataRetrievalPolicyInputRequestTypeDef(
    _RequiredSetDataRetrievalPolicyInputRequestTypeDef,
    _OptionalSetDataRetrievalPolicyInputRequestTypeDef,
):
    pass

_RequiredSetVaultAccessPolicyInputRequestTypeDef = TypedDict(
    "_RequiredSetVaultAccessPolicyInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)
_OptionalSetVaultAccessPolicyInputRequestTypeDef = TypedDict(
    "_OptionalSetVaultAccessPolicyInputRequestTypeDef",
    {
        "policy": "VaultAccessPolicyTypeDef",
    },
    total=False,
)

class SetVaultAccessPolicyInputRequestTypeDef(
    _RequiredSetVaultAccessPolicyInputRequestTypeDef,
    _OptionalSetVaultAccessPolicyInputRequestTypeDef,
):
    pass

SetVaultNotificationsInputNotificationTypeDef = TypedDict(
    "SetVaultNotificationsInputNotificationTypeDef",
    {
        "vaultNotificationConfig": "VaultNotificationConfigTypeDef",
    },
    total=False,
)

_RequiredSetVaultNotificationsInputRequestTypeDef = TypedDict(
    "_RequiredSetVaultNotificationsInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)
_OptionalSetVaultNotificationsInputRequestTypeDef = TypedDict(
    "_OptionalSetVaultNotificationsInputRequestTypeDef",
    {
        "vaultNotificationConfig": "VaultNotificationConfigTypeDef",
    },
    total=False,
)

class SetVaultNotificationsInputRequestTypeDef(
    _RequiredSetVaultNotificationsInputRequestTypeDef,
    _OptionalSetVaultNotificationsInputRequestTypeDef,
):
    pass

_RequiredUploadArchiveInputRequestTypeDef = TypedDict(
    "_RequiredUploadArchiveInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": str,
    },
)
_OptionalUploadArchiveInputRequestTypeDef = TypedDict(
    "_OptionalUploadArchiveInputRequestTypeDef",
    {
        "archiveDescription": str,
        "checksum": str,
        "body": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

class UploadArchiveInputRequestTypeDef(
    _RequiredUploadArchiveInputRequestTypeDef, _OptionalUploadArchiveInputRequestTypeDef
):
    pass

UploadArchiveInputVaultTypeDef = TypedDict(
    "UploadArchiveInputVaultTypeDef",
    {
        "archiveDescription": str,
        "checksum": str,
        "body": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

UploadListElementTypeDef = TypedDict(
    "UploadListElementTypeDef",
    {
        "MultipartUploadId": str,
        "VaultARN": str,
        "ArchiveDescription": str,
        "PartSizeInBytes": int,
        "CreationDate": str,
    },
    total=False,
)

UploadMultipartPartInputMultipartUploadTypeDef = TypedDict(
    "UploadMultipartPartInputMultipartUploadTypeDef",
    {
        "checksum": str,
        "range": str,
        "body": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

_RequiredUploadMultipartPartInputRequestTypeDef = TypedDict(
    "_RequiredUploadMultipartPartInputRequestTypeDef",
    {
        "accountId": str,
        "vaultName": str,
        "uploadId": str,
    },
)
_OptionalUploadMultipartPartInputRequestTypeDef = TypedDict(
    "_OptionalUploadMultipartPartInputRequestTypeDef",
    {
        "checksum": str,
        "range": str,
        "body": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

class UploadMultipartPartInputRequestTypeDef(
    _RequiredUploadMultipartPartInputRequestTypeDef, _OptionalUploadMultipartPartInputRequestTypeDef
):
    pass

UploadMultipartPartOutputTypeDef = TypedDict(
    "UploadMultipartPartOutputTypeDef",
    {
        "checksum": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VaultAccessPolicyTypeDef = TypedDict(
    "VaultAccessPolicyTypeDef",
    {
        "Policy": str,
    },
    total=False,
)

VaultArchiveRequestTypeDef = TypedDict(
    "VaultArchiveRequestTypeDef",
    {
        "id": str,
    },
)

VaultJobRequestTypeDef = TypedDict(
    "VaultJobRequestTypeDef",
    {
        "id": str,
    },
)

VaultLockPolicyTypeDef = TypedDict(
    "VaultLockPolicyTypeDef",
    {
        "Policy": str,
    },
    total=False,
)

VaultMultipartUploadRequestTypeDef = TypedDict(
    "VaultMultipartUploadRequestTypeDef",
    {
        "id": str,
    },
)

VaultNotificationConfigTypeDef = TypedDict(
    "VaultNotificationConfigTypeDef",
    {
        "SNSTopic": str,
        "Events": List[str],
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
