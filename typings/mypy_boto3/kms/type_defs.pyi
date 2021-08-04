"""
Type annotations for kms service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kms.type_defs import AliasListEntryTypeDef

    data: AliasListEntryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AlgorithmSpecType,
    ConnectionErrorCodeTypeType,
    ConnectionStateTypeType,
    CustomerMasterKeySpecType,
    DataKeyPairSpecType,
    DataKeySpecType,
    EncryptionAlgorithmSpecType,
    ExpirationModelTypeType,
    GrantOperationType,
    KeyManagerTypeType,
    KeyStateType,
    KeyUsageTypeType,
    MessageTypeType,
    MultiRegionKeyTypeType,
    OriginTypeType,
    SigningAlgorithmSpecType,
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
    "AliasListEntryTypeDef",
    "CancelKeyDeletionRequestRequestTypeDef",
    "CancelKeyDeletionResponseTypeDef",
    "ConnectCustomKeyStoreRequestRequestTypeDef",
    "CreateAliasRequestRequestTypeDef",
    "CreateCustomKeyStoreRequestRequestTypeDef",
    "CreateCustomKeyStoreResponseTypeDef",
    "CreateGrantRequestRequestTypeDef",
    "CreateGrantResponseTypeDef",
    "CreateKeyRequestRequestTypeDef",
    "CreateKeyResponseTypeDef",
    "CustomKeyStoresListEntryTypeDef",
    "DecryptRequestRequestTypeDef",
    "DecryptResponseTypeDef",
    "DeleteAliasRequestRequestTypeDef",
    "DeleteCustomKeyStoreRequestRequestTypeDef",
    "DeleteImportedKeyMaterialRequestRequestTypeDef",
    "DescribeCustomKeyStoresRequestRequestTypeDef",
    "DescribeCustomKeyStoresResponseTypeDef",
    "DescribeKeyRequestRequestTypeDef",
    "DescribeKeyResponseTypeDef",
    "DisableKeyRequestRequestTypeDef",
    "DisableKeyRotationRequestRequestTypeDef",
    "DisconnectCustomKeyStoreRequestRequestTypeDef",
    "EnableKeyRequestRequestTypeDef",
    "EnableKeyRotationRequestRequestTypeDef",
    "EncryptRequestRequestTypeDef",
    "EncryptResponseTypeDef",
    "GenerateDataKeyPairRequestRequestTypeDef",
    "GenerateDataKeyPairResponseTypeDef",
    "GenerateDataKeyPairWithoutPlaintextRequestRequestTypeDef",
    "GenerateDataKeyPairWithoutPlaintextResponseTypeDef",
    "GenerateDataKeyRequestRequestTypeDef",
    "GenerateDataKeyResponseTypeDef",
    "GenerateDataKeyWithoutPlaintextRequestRequestTypeDef",
    "GenerateDataKeyWithoutPlaintextResponseTypeDef",
    "GenerateRandomRequestRequestTypeDef",
    "GenerateRandomResponseTypeDef",
    "GetKeyPolicyRequestRequestTypeDef",
    "GetKeyPolicyResponseTypeDef",
    "GetKeyRotationStatusRequestRequestTypeDef",
    "GetKeyRotationStatusResponseTypeDef",
    "GetParametersForImportRequestRequestTypeDef",
    "GetParametersForImportResponseTypeDef",
    "GetPublicKeyRequestRequestTypeDef",
    "GetPublicKeyResponseTypeDef",
    "GrantConstraintsTypeDef",
    "GrantListEntryTypeDef",
    "ImportKeyMaterialRequestRequestTypeDef",
    "KeyListEntryTypeDef",
    "KeyMetadataTypeDef",
    "ListAliasesRequestRequestTypeDef",
    "ListAliasesResponseTypeDef",
    "ListGrantsRequestRequestTypeDef",
    "ListGrantsResponseTypeDef",
    "ListKeyPoliciesRequestRequestTypeDef",
    "ListKeyPoliciesResponseTypeDef",
    "ListKeysRequestRequestTypeDef",
    "ListKeysResponseTypeDef",
    "ListResourceTagsRequestRequestTypeDef",
    "ListResourceTagsResponseTypeDef",
    "ListRetirableGrantsRequestRequestTypeDef",
    "MultiRegionConfigurationTypeDef",
    "MultiRegionKeyTypeDef",
    "PaginatorConfigTypeDef",
    "PutKeyPolicyRequestRequestTypeDef",
    "ReEncryptRequestRequestTypeDef",
    "ReEncryptResponseTypeDef",
    "ReplicateKeyRequestRequestTypeDef",
    "ReplicateKeyResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RetireGrantRequestRequestTypeDef",
    "RevokeGrantRequestRequestTypeDef",
    "ScheduleKeyDeletionRequestRequestTypeDef",
    "ScheduleKeyDeletionResponseTypeDef",
    "SignRequestRequestTypeDef",
    "SignResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAliasRequestRequestTypeDef",
    "UpdateCustomKeyStoreRequestRequestTypeDef",
    "UpdateKeyDescriptionRequestRequestTypeDef",
    "UpdatePrimaryRegionRequestRequestTypeDef",
    "VerifyRequestRequestTypeDef",
    "VerifyResponseTypeDef",
)

AliasListEntryTypeDef = TypedDict(
    "AliasListEntryTypeDef",
    {
        "AliasName": str,
        "AliasArn": str,
        "TargetKeyId": str,
        "CreationDate": datetime,
        "LastUpdatedDate": datetime,
    },
    total=False,
)

CancelKeyDeletionRequestRequestTypeDef = TypedDict(
    "CancelKeyDeletionRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)

CancelKeyDeletionResponseTypeDef = TypedDict(
    "CancelKeyDeletionResponseTypeDef",
    {
        "KeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConnectCustomKeyStoreRequestRequestTypeDef = TypedDict(
    "ConnectCustomKeyStoreRequestRequestTypeDef",
    {
        "CustomKeyStoreId": str,
    },
)

CreateAliasRequestRequestTypeDef = TypedDict(
    "CreateAliasRequestRequestTypeDef",
    {
        "AliasName": str,
        "TargetKeyId": str,
    },
)

CreateCustomKeyStoreRequestRequestTypeDef = TypedDict(
    "CreateCustomKeyStoreRequestRequestTypeDef",
    {
        "CustomKeyStoreName": str,
        "CloudHsmClusterId": str,
        "TrustAnchorCertificate": str,
        "KeyStorePassword": str,
    },
)

CreateCustomKeyStoreResponseTypeDef = TypedDict(
    "CreateCustomKeyStoreResponseTypeDef",
    {
        "CustomKeyStoreId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGrantRequestRequestTypeDef = TypedDict(
    "_RequiredCreateGrantRequestRequestTypeDef",
    {
        "KeyId": str,
        "GranteePrincipal": str,
        "Operations": List[GrantOperationType],
    },
)
_OptionalCreateGrantRequestRequestTypeDef = TypedDict(
    "_OptionalCreateGrantRequestRequestTypeDef",
    {
        "RetiringPrincipal": str,
        "Constraints": "GrantConstraintsTypeDef",
        "GrantTokens": List[str],
        "Name": str,
    },
    total=False,
)

class CreateGrantRequestRequestTypeDef(
    _RequiredCreateGrantRequestRequestTypeDef, _OptionalCreateGrantRequestRequestTypeDef
):
    pass

CreateGrantResponseTypeDef = TypedDict(
    "CreateGrantResponseTypeDef",
    {
        "GrantToken": str,
        "GrantId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateKeyRequestRequestTypeDef = TypedDict(
    "CreateKeyRequestRequestTypeDef",
    {
        "Policy": str,
        "Description": str,
        "KeyUsage": KeyUsageTypeType,
        "CustomerMasterKeySpec": CustomerMasterKeySpecType,
        "Origin": OriginTypeType,
        "CustomKeyStoreId": str,
        "BypassPolicyLockoutSafetyCheck": bool,
        "Tags": List["TagTypeDef"],
        "MultiRegion": bool,
    },
    total=False,
)

CreateKeyResponseTypeDef = TypedDict(
    "CreateKeyResponseTypeDef",
    {
        "KeyMetadata": "KeyMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomKeyStoresListEntryTypeDef = TypedDict(
    "CustomKeyStoresListEntryTypeDef",
    {
        "CustomKeyStoreId": str,
        "CustomKeyStoreName": str,
        "CloudHsmClusterId": str,
        "TrustAnchorCertificate": str,
        "ConnectionState": ConnectionStateTypeType,
        "ConnectionErrorCode": ConnectionErrorCodeTypeType,
        "CreationDate": datetime,
    },
    total=False,
)

_RequiredDecryptRequestRequestTypeDef = TypedDict(
    "_RequiredDecryptRequestRequestTypeDef",
    {
        "CiphertextBlob": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalDecryptRequestRequestTypeDef = TypedDict(
    "_OptionalDecryptRequestRequestTypeDef",
    {
        "EncryptionContext": Dict[str, str],
        "GrantTokens": List[str],
        "KeyId": str,
        "EncryptionAlgorithm": EncryptionAlgorithmSpecType,
    },
    total=False,
)

class DecryptRequestRequestTypeDef(
    _RequiredDecryptRequestRequestTypeDef, _OptionalDecryptRequestRequestTypeDef
):
    pass

DecryptResponseTypeDef = TypedDict(
    "DecryptResponseTypeDef",
    {
        "KeyId": str,
        "Plaintext": bytes,
        "EncryptionAlgorithm": EncryptionAlgorithmSpecType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAliasRequestRequestTypeDef = TypedDict(
    "DeleteAliasRequestRequestTypeDef",
    {
        "AliasName": str,
    },
)

DeleteCustomKeyStoreRequestRequestTypeDef = TypedDict(
    "DeleteCustomKeyStoreRequestRequestTypeDef",
    {
        "CustomKeyStoreId": str,
    },
)

DeleteImportedKeyMaterialRequestRequestTypeDef = TypedDict(
    "DeleteImportedKeyMaterialRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)

DescribeCustomKeyStoresRequestRequestTypeDef = TypedDict(
    "DescribeCustomKeyStoresRequestRequestTypeDef",
    {
        "CustomKeyStoreId": str,
        "CustomKeyStoreName": str,
        "Limit": int,
        "Marker": str,
    },
    total=False,
)

DescribeCustomKeyStoresResponseTypeDef = TypedDict(
    "DescribeCustomKeyStoresResponseTypeDef",
    {
        "CustomKeyStores": List["CustomKeyStoresListEntryTypeDef"],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeKeyRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeKeyRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)
_OptionalDescribeKeyRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeKeyRequestRequestTypeDef",
    {
        "GrantTokens": List[str],
    },
    total=False,
)

class DescribeKeyRequestRequestTypeDef(
    _RequiredDescribeKeyRequestRequestTypeDef, _OptionalDescribeKeyRequestRequestTypeDef
):
    pass

DescribeKeyResponseTypeDef = TypedDict(
    "DescribeKeyResponseTypeDef",
    {
        "KeyMetadata": "KeyMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableKeyRequestRequestTypeDef = TypedDict(
    "DisableKeyRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)

DisableKeyRotationRequestRequestTypeDef = TypedDict(
    "DisableKeyRotationRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)

DisconnectCustomKeyStoreRequestRequestTypeDef = TypedDict(
    "DisconnectCustomKeyStoreRequestRequestTypeDef",
    {
        "CustomKeyStoreId": str,
    },
)

EnableKeyRequestRequestTypeDef = TypedDict(
    "EnableKeyRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)

EnableKeyRotationRequestRequestTypeDef = TypedDict(
    "EnableKeyRotationRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)

_RequiredEncryptRequestRequestTypeDef = TypedDict(
    "_RequiredEncryptRequestRequestTypeDef",
    {
        "KeyId": str,
        "Plaintext": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalEncryptRequestRequestTypeDef = TypedDict(
    "_OptionalEncryptRequestRequestTypeDef",
    {
        "EncryptionContext": Dict[str, str],
        "GrantTokens": List[str],
        "EncryptionAlgorithm": EncryptionAlgorithmSpecType,
    },
    total=False,
)

class EncryptRequestRequestTypeDef(
    _RequiredEncryptRequestRequestTypeDef, _OptionalEncryptRequestRequestTypeDef
):
    pass

EncryptResponseTypeDef = TypedDict(
    "EncryptResponseTypeDef",
    {
        "CiphertextBlob": bytes,
        "KeyId": str,
        "EncryptionAlgorithm": EncryptionAlgorithmSpecType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGenerateDataKeyPairRequestRequestTypeDef = TypedDict(
    "_RequiredGenerateDataKeyPairRequestRequestTypeDef",
    {
        "KeyId": str,
        "KeyPairSpec": DataKeyPairSpecType,
    },
)
_OptionalGenerateDataKeyPairRequestRequestTypeDef = TypedDict(
    "_OptionalGenerateDataKeyPairRequestRequestTypeDef",
    {
        "EncryptionContext": Dict[str, str],
        "GrantTokens": List[str],
    },
    total=False,
)

class GenerateDataKeyPairRequestRequestTypeDef(
    _RequiredGenerateDataKeyPairRequestRequestTypeDef,
    _OptionalGenerateDataKeyPairRequestRequestTypeDef,
):
    pass

GenerateDataKeyPairResponseTypeDef = TypedDict(
    "GenerateDataKeyPairResponseTypeDef",
    {
        "PrivateKeyCiphertextBlob": bytes,
        "PrivateKeyPlaintext": bytes,
        "PublicKey": bytes,
        "KeyId": str,
        "KeyPairSpec": DataKeyPairSpecType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGenerateDataKeyPairWithoutPlaintextRequestRequestTypeDef = TypedDict(
    "_RequiredGenerateDataKeyPairWithoutPlaintextRequestRequestTypeDef",
    {
        "KeyId": str,
        "KeyPairSpec": DataKeyPairSpecType,
    },
)
_OptionalGenerateDataKeyPairWithoutPlaintextRequestRequestTypeDef = TypedDict(
    "_OptionalGenerateDataKeyPairWithoutPlaintextRequestRequestTypeDef",
    {
        "EncryptionContext": Dict[str, str],
        "GrantTokens": List[str],
    },
    total=False,
)

class GenerateDataKeyPairWithoutPlaintextRequestRequestTypeDef(
    _RequiredGenerateDataKeyPairWithoutPlaintextRequestRequestTypeDef,
    _OptionalGenerateDataKeyPairWithoutPlaintextRequestRequestTypeDef,
):
    pass

GenerateDataKeyPairWithoutPlaintextResponseTypeDef = TypedDict(
    "GenerateDataKeyPairWithoutPlaintextResponseTypeDef",
    {
        "PrivateKeyCiphertextBlob": bytes,
        "PublicKey": bytes,
        "KeyId": str,
        "KeyPairSpec": DataKeyPairSpecType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGenerateDataKeyRequestRequestTypeDef = TypedDict(
    "_RequiredGenerateDataKeyRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)
_OptionalGenerateDataKeyRequestRequestTypeDef = TypedDict(
    "_OptionalGenerateDataKeyRequestRequestTypeDef",
    {
        "EncryptionContext": Dict[str, str],
        "NumberOfBytes": int,
        "KeySpec": DataKeySpecType,
        "GrantTokens": List[str],
    },
    total=False,
)

class GenerateDataKeyRequestRequestTypeDef(
    _RequiredGenerateDataKeyRequestRequestTypeDef, _OptionalGenerateDataKeyRequestRequestTypeDef
):
    pass

GenerateDataKeyResponseTypeDef = TypedDict(
    "GenerateDataKeyResponseTypeDef",
    {
        "CiphertextBlob": bytes,
        "Plaintext": bytes,
        "KeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGenerateDataKeyWithoutPlaintextRequestRequestTypeDef = TypedDict(
    "_RequiredGenerateDataKeyWithoutPlaintextRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)
_OptionalGenerateDataKeyWithoutPlaintextRequestRequestTypeDef = TypedDict(
    "_OptionalGenerateDataKeyWithoutPlaintextRequestRequestTypeDef",
    {
        "EncryptionContext": Dict[str, str],
        "KeySpec": DataKeySpecType,
        "NumberOfBytes": int,
        "GrantTokens": List[str],
    },
    total=False,
)

class GenerateDataKeyWithoutPlaintextRequestRequestTypeDef(
    _RequiredGenerateDataKeyWithoutPlaintextRequestRequestTypeDef,
    _OptionalGenerateDataKeyWithoutPlaintextRequestRequestTypeDef,
):
    pass

GenerateDataKeyWithoutPlaintextResponseTypeDef = TypedDict(
    "GenerateDataKeyWithoutPlaintextResponseTypeDef",
    {
        "CiphertextBlob": bytes,
        "KeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GenerateRandomRequestRequestTypeDef = TypedDict(
    "GenerateRandomRequestRequestTypeDef",
    {
        "NumberOfBytes": int,
        "CustomKeyStoreId": str,
    },
    total=False,
)

GenerateRandomResponseTypeDef = TypedDict(
    "GenerateRandomResponseTypeDef",
    {
        "Plaintext": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKeyPolicyRequestRequestTypeDef = TypedDict(
    "GetKeyPolicyRequestRequestTypeDef",
    {
        "KeyId": str,
        "PolicyName": str,
    },
)

GetKeyPolicyResponseTypeDef = TypedDict(
    "GetKeyPolicyResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKeyRotationStatusRequestRequestTypeDef = TypedDict(
    "GetKeyRotationStatusRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)

GetKeyRotationStatusResponseTypeDef = TypedDict(
    "GetKeyRotationStatusResponseTypeDef",
    {
        "KeyRotationEnabled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetParametersForImportRequestRequestTypeDef = TypedDict(
    "GetParametersForImportRequestRequestTypeDef",
    {
        "KeyId": str,
        "WrappingAlgorithm": AlgorithmSpecType,
        "WrappingKeySpec": Literal["RSA_2048"],
    },
)

GetParametersForImportResponseTypeDef = TypedDict(
    "GetParametersForImportResponseTypeDef",
    {
        "KeyId": str,
        "ImportToken": bytes,
        "PublicKey": bytes,
        "ParametersValidTo": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPublicKeyRequestRequestTypeDef = TypedDict(
    "_RequiredGetPublicKeyRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)
_OptionalGetPublicKeyRequestRequestTypeDef = TypedDict(
    "_OptionalGetPublicKeyRequestRequestTypeDef",
    {
        "GrantTokens": List[str],
    },
    total=False,
)

class GetPublicKeyRequestRequestTypeDef(
    _RequiredGetPublicKeyRequestRequestTypeDef, _OptionalGetPublicKeyRequestRequestTypeDef
):
    pass

GetPublicKeyResponseTypeDef = TypedDict(
    "GetPublicKeyResponseTypeDef",
    {
        "KeyId": str,
        "PublicKey": bytes,
        "CustomerMasterKeySpec": CustomerMasterKeySpecType,
        "KeyUsage": KeyUsageTypeType,
        "EncryptionAlgorithms": List[EncryptionAlgorithmSpecType],
        "SigningAlgorithms": List[SigningAlgorithmSpecType],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GrantConstraintsTypeDef = TypedDict(
    "GrantConstraintsTypeDef",
    {
        "EncryptionContextSubset": Dict[str, str],
        "EncryptionContextEquals": Dict[str, str],
    },
    total=False,
)

GrantListEntryTypeDef = TypedDict(
    "GrantListEntryTypeDef",
    {
        "KeyId": str,
        "GrantId": str,
        "Name": str,
        "CreationDate": datetime,
        "GranteePrincipal": str,
        "RetiringPrincipal": str,
        "IssuingAccount": str,
        "Operations": List[GrantOperationType],
        "Constraints": "GrantConstraintsTypeDef",
    },
    total=False,
)

_RequiredImportKeyMaterialRequestRequestTypeDef = TypedDict(
    "_RequiredImportKeyMaterialRequestRequestTypeDef",
    {
        "KeyId": str,
        "ImportToken": Union[bytes, IO[bytes], StreamingBody],
        "EncryptedKeyMaterial": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalImportKeyMaterialRequestRequestTypeDef = TypedDict(
    "_OptionalImportKeyMaterialRequestRequestTypeDef",
    {
        "ValidTo": Union[datetime, str],
        "ExpirationModel": ExpirationModelTypeType,
    },
    total=False,
)

class ImportKeyMaterialRequestRequestTypeDef(
    _RequiredImportKeyMaterialRequestRequestTypeDef, _OptionalImportKeyMaterialRequestRequestTypeDef
):
    pass

KeyListEntryTypeDef = TypedDict(
    "KeyListEntryTypeDef",
    {
        "KeyId": str,
        "KeyArn": str,
    },
    total=False,
)

_RequiredKeyMetadataTypeDef = TypedDict(
    "_RequiredKeyMetadataTypeDef",
    {
        "KeyId": str,
    },
)
_OptionalKeyMetadataTypeDef = TypedDict(
    "_OptionalKeyMetadataTypeDef",
    {
        "AWSAccountId": str,
        "Arn": str,
        "CreationDate": datetime,
        "Enabled": bool,
        "Description": str,
        "KeyUsage": KeyUsageTypeType,
        "KeyState": KeyStateType,
        "DeletionDate": datetime,
        "ValidTo": datetime,
        "Origin": OriginTypeType,
        "CustomKeyStoreId": str,
        "CloudHsmClusterId": str,
        "ExpirationModel": ExpirationModelTypeType,
        "KeyManager": KeyManagerTypeType,
        "CustomerMasterKeySpec": CustomerMasterKeySpecType,
        "EncryptionAlgorithms": List[EncryptionAlgorithmSpecType],
        "SigningAlgorithms": List[SigningAlgorithmSpecType],
        "MultiRegion": bool,
        "MultiRegionConfiguration": "MultiRegionConfigurationTypeDef",
        "PendingDeletionWindowInDays": int,
    },
    total=False,
)

class KeyMetadataTypeDef(_RequiredKeyMetadataTypeDef, _OptionalKeyMetadataTypeDef):
    pass

ListAliasesRequestRequestTypeDef = TypedDict(
    "ListAliasesRequestRequestTypeDef",
    {
        "KeyId": str,
        "Limit": int,
        "Marker": str,
    },
    total=False,
)

ListAliasesResponseTypeDef = TypedDict(
    "ListAliasesResponseTypeDef",
    {
        "Aliases": List["AliasListEntryTypeDef"],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGrantsRequestRequestTypeDef = TypedDict(
    "_RequiredListGrantsRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)
_OptionalListGrantsRequestRequestTypeDef = TypedDict(
    "_OptionalListGrantsRequestRequestTypeDef",
    {
        "Limit": int,
        "Marker": str,
        "GrantId": str,
        "GranteePrincipal": str,
    },
    total=False,
)

class ListGrantsRequestRequestTypeDef(
    _RequiredListGrantsRequestRequestTypeDef, _OptionalListGrantsRequestRequestTypeDef
):
    pass

ListGrantsResponseTypeDef = TypedDict(
    "ListGrantsResponseTypeDef",
    {
        "Grants": List["GrantListEntryTypeDef"],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListKeyPoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredListKeyPoliciesRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)
_OptionalListKeyPoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalListKeyPoliciesRequestRequestTypeDef",
    {
        "Limit": int,
        "Marker": str,
    },
    total=False,
)

class ListKeyPoliciesRequestRequestTypeDef(
    _RequiredListKeyPoliciesRequestRequestTypeDef, _OptionalListKeyPoliciesRequestRequestTypeDef
):
    pass

ListKeyPoliciesResponseTypeDef = TypedDict(
    "ListKeyPoliciesResponseTypeDef",
    {
        "PolicyNames": List[str],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListKeysRequestRequestTypeDef = TypedDict(
    "ListKeysRequestRequestTypeDef",
    {
        "Limit": int,
        "Marker": str,
    },
    total=False,
)

ListKeysResponseTypeDef = TypedDict(
    "ListKeysResponseTypeDef",
    {
        "Keys": List["KeyListEntryTypeDef"],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourceTagsRequestRequestTypeDef = TypedDict(
    "_RequiredListResourceTagsRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)
_OptionalListResourceTagsRequestRequestTypeDef = TypedDict(
    "_OptionalListResourceTagsRequestRequestTypeDef",
    {
        "Limit": int,
        "Marker": str,
    },
    total=False,
)

class ListResourceTagsRequestRequestTypeDef(
    _RequiredListResourceTagsRequestRequestTypeDef, _OptionalListResourceTagsRequestRequestTypeDef
):
    pass

ListResourceTagsResponseTypeDef = TypedDict(
    "ListResourceTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRetirableGrantsRequestRequestTypeDef = TypedDict(
    "_RequiredListRetirableGrantsRequestRequestTypeDef",
    {
        "RetiringPrincipal": str,
    },
)
_OptionalListRetirableGrantsRequestRequestTypeDef = TypedDict(
    "_OptionalListRetirableGrantsRequestRequestTypeDef",
    {
        "Limit": int,
        "Marker": str,
    },
    total=False,
)

class ListRetirableGrantsRequestRequestTypeDef(
    _RequiredListRetirableGrantsRequestRequestTypeDef,
    _OptionalListRetirableGrantsRequestRequestTypeDef,
):
    pass

MultiRegionConfigurationTypeDef = TypedDict(
    "MultiRegionConfigurationTypeDef",
    {
        "MultiRegionKeyType": MultiRegionKeyTypeType,
        "PrimaryKey": "MultiRegionKeyTypeDef",
        "ReplicaKeys": List["MultiRegionKeyTypeDef"],
    },
    total=False,
)

MultiRegionKeyTypeDef = TypedDict(
    "MultiRegionKeyTypeDef",
    {
        "Arn": str,
        "Region": str,
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

_RequiredPutKeyPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutKeyPolicyRequestRequestTypeDef",
    {
        "KeyId": str,
        "PolicyName": str,
        "Policy": str,
    },
)
_OptionalPutKeyPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutKeyPolicyRequestRequestTypeDef",
    {
        "BypassPolicyLockoutSafetyCheck": bool,
    },
    total=False,
)

class PutKeyPolicyRequestRequestTypeDef(
    _RequiredPutKeyPolicyRequestRequestTypeDef, _OptionalPutKeyPolicyRequestRequestTypeDef
):
    pass

_RequiredReEncryptRequestRequestTypeDef = TypedDict(
    "_RequiredReEncryptRequestRequestTypeDef",
    {
        "CiphertextBlob": Union[bytes, IO[bytes], StreamingBody],
        "DestinationKeyId": str,
    },
)
_OptionalReEncryptRequestRequestTypeDef = TypedDict(
    "_OptionalReEncryptRequestRequestTypeDef",
    {
        "SourceEncryptionContext": Dict[str, str],
        "SourceKeyId": str,
        "DestinationEncryptionContext": Dict[str, str],
        "SourceEncryptionAlgorithm": EncryptionAlgorithmSpecType,
        "DestinationEncryptionAlgorithm": EncryptionAlgorithmSpecType,
        "GrantTokens": List[str],
    },
    total=False,
)

class ReEncryptRequestRequestTypeDef(
    _RequiredReEncryptRequestRequestTypeDef, _OptionalReEncryptRequestRequestTypeDef
):
    pass

ReEncryptResponseTypeDef = TypedDict(
    "ReEncryptResponseTypeDef",
    {
        "CiphertextBlob": bytes,
        "SourceKeyId": str,
        "KeyId": str,
        "SourceEncryptionAlgorithm": EncryptionAlgorithmSpecType,
        "DestinationEncryptionAlgorithm": EncryptionAlgorithmSpecType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredReplicateKeyRequestRequestTypeDef = TypedDict(
    "_RequiredReplicateKeyRequestRequestTypeDef",
    {
        "KeyId": str,
        "ReplicaRegion": str,
    },
)
_OptionalReplicateKeyRequestRequestTypeDef = TypedDict(
    "_OptionalReplicateKeyRequestRequestTypeDef",
    {
        "Policy": str,
        "BypassPolicyLockoutSafetyCheck": bool,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class ReplicateKeyRequestRequestTypeDef(
    _RequiredReplicateKeyRequestRequestTypeDef, _OptionalReplicateKeyRequestRequestTypeDef
):
    pass

ReplicateKeyResponseTypeDef = TypedDict(
    "ReplicateKeyResponseTypeDef",
    {
        "ReplicaKeyMetadata": "KeyMetadataTypeDef",
        "ReplicaPolicy": str,
        "ReplicaTags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

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

RetireGrantRequestRequestTypeDef = TypedDict(
    "RetireGrantRequestRequestTypeDef",
    {
        "GrantToken": str,
        "KeyId": str,
        "GrantId": str,
    },
    total=False,
)

RevokeGrantRequestRequestTypeDef = TypedDict(
    "RevokeGrantRequestRequestTypeDef",
    {
        "KeyId": str,
        "GrantId": str,
    },
)

_RequiredScheduleKeyDeletionRequestRequestTypeDef = TypedDict(
    "_RequiredScheduleKeyDeletionRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)
_OptionalScheduleKeyDeletionRequestRequestTypeDef = TypedDict(
    "_OptionalScheduleKeyDeletionRequestRequestTypeDef",
    {
        "PendingWindowInDays": int,
    },
    total=False,
)

class ScheduleKeyDeletionRequestRequestTypeDef(
    _RequiredScheduleKeyDeletionRequestRequestTypeDef,
    _OptionalScheduleKeyDeletionRequestRequestTypeDef,
):
    pass

ScheduleKeyDeletionResponseTypeDef = TypedDict(
    "ScheduleKeyDeletionResponseTypeDef",
    {
        "KeyId": str,
        "DeletionDate": datetime,
        "KeyState": KeyStateType,
        "PendingWindowInDays": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSignRequestRequestTypeDef = TypedDict(
    "_RequiredSignRequestRequestTypeDef",
    {
        "KeyId": str,
        "Message": Union[bytes, IO[bytes], StreamingBody],
        "SigningAlgorithm": SigningAlgorithmSpecType,
    },
)
_OptionalSignRequestRequestTypeDef = TypedDict(
    "_OptionalSignRequestRequestTypeDef",
    {
        "MessageType": MessageTypeType,
        "GrantTokens": List[str],
    },
    total=False,
)

class SignRequestRequestTypeDef(
    _RequiredSignRequestRequestTypeDef, _OptionalSignRequestRequestTypeDef
):
    pass

SignResponseTypeDef = TypedDict(
    "SignResponseTypeDef",
    {
        "KeyId": str,
        "Signature": bytes,
        "SigningAlgorithm": SigningAlgorithmSpecType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "KeyId": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "TagKey": str,
        "TagValue": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "KeyId": str,
        "TagKeys": List[str],
    },
)

UpdateAliasRequestRequestTypeDef = TypedDict(
    "UpdateAliasRequestRequestTypeDef",
    {
        "AliasName": str,
        "TargetKeyId": str,
    },
)

_RequiredUpdateCustomKeyStoreRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCustomKeyStoreRequestRequestTypeDef",
    {
        "CustomKeyStoreId": str,
    },
)
_OptionalUpdateCustomKeyStoreRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCustomKeyStoreRequestRequestTypeDef",
    {
        "NewCustomKeyStoreName": str,
        "KeyStorePassword": str,
        "CloudHsmClusterId": str,
    },
    total=False,
)

class UpdateCustomKeyStoreRequestRequestTypeDef(
    _RequiredUpdateCustomKeyStoreRequestRequestTypeDef,
    _OptionalUpdateCustomKeyStoreRequestRequestTypeDef,
):
    pass

UpdateKeyDescriptionRequestRequestTypeDef = TypedDict(
    "UpdateKeyDescriptionRequestRequestTypeDef",
    {
        "KeyId": str,
        "Description": str,
    },
)

UpdatePrimaryRegionRequestRequestTypeDef = TypedDict(
    "UpdatePrimaryRegionRequestRequestTypeDef",
    {
        "KeyId": str,
        "PrimaryRegion": str,
    },
)

_RequiredVerifyRequestRequestTypeDef = TypedDict(
    "_RequiredVerifyRequestRequestTypeDef",
    {
        "KeyId": str,
        "Message": Union[bytes, IO[bytes], StreamingBody],
        "Signature": Union[bytes, IO[bytes], StreamingBody],
        "SigningAlgorithm": SigningAlgorithmSpecType,
    },
)
_OptionalVerifyRequestRequestTypeDef = TypedDict(
    "_OptionalVerifyRequestRequestTypeDef",
    {
        "MessageType": MessageTypeType,
        "GrantTokens": List[str],
    },
    total=False,
)

class VerifyRequestRequestTypeDef(
    _RequiredVerifyRequestRequestTypeDef, _OptionalVerifyRequestRequestTypeDef
):
    pass

VerifyResponseTypeDef = TypedDict(
    "VerifyResponseTypeDef",
    {
        "KeyId": str,
        "SignatureValid": bool,
        "SigningAlgorithm": SigningAlgorithmSpecType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
