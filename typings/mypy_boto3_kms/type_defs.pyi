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
    CustomKeyStoreTypeType,
    DataKeyPairSpecType,
    DataKeySpecType,
    EncryptionAlgorithmSpecType,
    ExpirationModelTypeType,
    GrantOperationType,
    KeyManagerTypeType,
    KeySpecType,
    KeyStateType,
    KeyUsageTypeType,
    MacAlgorithmSpecType,
    MessageTypeType,
    MultiRegionKeyTypeType,
    OriginTypeType,
    RotationTypeType,
    SigningAlgorithmSpecType,
    WrappingKeySpecType,
    XksProxyConnectivityTypeType,
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
    "DeriveSharedSecretRequestRequestTypeDef",
    "DeriveSharedSecretResponseTypeDef",
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
    "GenerateMacRequestRequestTypeDef",
    "GenerateMacResponseTypeDef",
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
    "ListKeyRotationsRequestRequestTypeDef",
    "ListKeyRotationsResponseTypeDef",
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
    "RecipientInfoTypeDef",
    "ReplicateKeyRequestRequestTypeDef",
    "ReplicateKeyResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RetireGrantRequestRequestTypeDef",
    "RevokeGrantRequestRequestTypeDef",
    "RotateKeyOnDemandRequestRequestTypeDef",
    "RotateKeyOnDemandResponseTypeDef",
    "RotationsListEntryTypeDef",
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
    "VerifyMacRequestRequestTypeDef",
    "VerifyMacResponseTypeDef",
    "VerifyRequestRequestTypeDef",
    "VerifyResponseTypeDef",
    "XksKeyConfigurationTypeTypeDef",
    "XksProxyAuthenticationCredentialTypeTypeDef",
    "XksProxyConfigurationTypeTypeDef",
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

_RequiredCreateCustomKeyStoreRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCustomKeyStoreRequestRequestTypeDef",
    {
        "CustomKeyStoreName": str,
    },
)
_OptionalCreateCustomKeyStoreRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCustomKeyStoreRequestRequestTypeDef",
    {
        "CloudHsmClusterId": str,
        "TrustAnchorCertificate": str,
        "KeyStorePassword": str,
        "CustomKeyStoreType": CustomKeyStoreTypeType,
        "XksProxyUriEndpoint": str,
        "XksProxyUriPath": str,
        "XksProxyVpcEndpointServiceName": str,
        "XksProxyAuthenticationCredential": "XksProxyAuthenticationCredentialTypeTypeDef",
        "XksProxyConnectivity": XksProxyConnectivityTypeType,
    },
    total=False,
)

class CreateCustomKeyStoreRequestRequestTypeDef(
    _RequiredCreateCustomKeyStoreRequestRequestTypeDef,
    _OptionalCreateCustomKeyStoreRequestRequestTypeDef,
):
    pass

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
        "DryRun": bool,
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
        "KeySpec": KeySpecType,
        "Origin": OriginTypeType,
        "CustomKeyStoreId": str,
        "BypassPolicyLockoutSafetyCheck": bool,
        "Tags": List["TagTypeDef"],
        "MultiRegion": bool,
        "XksKeyId": str,
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
        "CustomKeyStoreType": CustomKeyStoreTypeType,
        "XksProxyConfiguration": "XksProxyConfigurationTypeTypeDef",
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
        "Recipient": "RecipientInfoTypeDef",
        "DryRun": bool,
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
        "CiphertextForRecipient": bytes,
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

_RequiredDeriveSharedSecretRequestRequestTypeDef = TypedDict(
    "_RequiredDeriveSharedSecretRequestRequestTypeDef",
    {
        "KeyId": str,
        "KeyAgreementAlgorithm": Literal["ECDH"],
        "PublicKey": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalDeriveSharedSecretRequestRequestTypeDef = TypedDict(
    "_OptionalDeriveSharedSecretRequestRequestTypeDef",
    {
        "GrantTokens": List[str],
        "DryRun": bool,
        "Recipient": "RecipientInfoTypeDef",
    },
    total=False,
)

class DeriveSharedSecretRequestRequestTypeDef(
    _RequiredDeriveSharedSecretRequestRequestTypeDef,
    _OptionalDeriveSharedSecretRequestRequestTypeDef,
):
    pass

DeriveSharedSecretResponseTypeDef = TypedDict(
    "DeriveSharedSecretResponseTypeDef",
    {
        "KeyId": str,
        "SharedSecret": bytes,
        "CiphertextForRecipient": bytes,
        "KeyAgreementAlgorithm": Literal["ECDH"],
        "KeyOrigin": OriginTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

_RequiredEnableKeyRotationRequestRequestTypeDef = TypedDict(
    "_RequiredEnableKeyRotationRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)
_OptionalEnableKeyRotationRequestRequestTypeDef = TypedDict(
    "_OptionalEnableKeyRotationRequestRequestTypeDef",
    {
        "RotationPeriodInDays": int,
    },
    total=False,
)

class EnableKeyRotationRequestRequestTypeDef(
    _RequiredEnableKeyRotationRequestRequestTypeDef, _OptionalEnableKeyRotationRequestRequestTypeDef
):
    pass

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
        "DryRun": bool,
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
        "Recipient": "RecipientInfoTypeDef",
        "DryRun": bool,
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
        "CiphertextForRecipient": bytes,
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
        "DryRun": bool,
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
        "Recipient": "RecipientInfoTypeDef",
        "DryRun": bool,
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
        "CiphertextForRecipient": bytes,
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
        "DryRun": bool,
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

_RequiredGenerateMacRequestRequestTypeDef = TypedDict(
    "_RequiredGenerateMacRequestRequestTypeDef",
    {
        "Message": Union[bytes, IO[bytes], StreamingBody],
        "KeyId": str,
        "MacAlgorithm": MacAlgorithmSpecType,
    },
)
_OptionalGenerateMacRequestRequestTypeDef = TypedDict(
    "_OptionalGenerateMacRequestRequestTypeDef",
    {
        "GrantTokens": List[str],
        "DryRun": bool,
    },
    total=False,
)

class GenerateMacRequestRequestTypeDef(
    _RequiredGenerateMacRequestRequestTypeDef, _OptionalGenerateMacRequestRequestTypeDef
):
    pass

GenerateMacResponseTypeDef = TypedDict(
    "GenerateMacResponseTypeDef",
    {
        "Mac": bytes,
        "MacAlgorithm": MacAlgorithmSpecType,
        "KeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GenerateRandomRequestRequestTypeDef = TypedDict(
    "GenerateRandomRequestRequestTypeDef",
    {
        "NumberOfBytes": int,
        "CustomKeyStoreId": str,
        "Recipient": "RecipientInfoTypeDef",
    },
    total=False,
)

GenerateRandomResponseTypeDef = TypedDict(
    "GenerateRandomResponseTypeDef",
    {
        "Plaintext": bytes,
        "CiphertextForRecipient": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetKeyPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredGetKeyPolicyRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)
_OptionalGetKeyPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalGetKeyPolicyRequestRequestTypeDef",
    {
        "PolicyName": str,
    },
    total=False,
)

class GetKeyPolicyRequestRequestTypeDef(
    _RequiredGetKeyPolicyRequestRequestTypeDef, _OptionalGetKeyPolicyRequestRequestTypeDef
):
    pass

GetKeyPolicyResponseTypeDef = TypedDict(
    "GetKeyPolicyResponseTypeDef",
    {
        "Policy": str,
        "PolicyName": str,
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
        "KeyId": str,
        "RotationPeriodInDays": int,
        "NextRotationDate": datetime,
        "OnDemandRotationStartDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetParametersForImportRequestRequestTypeDef = TypedDict(
    "GetParametersForImportRequestRequestTypeDef",
    {
        "KeyId": str,
        "WrappingAlgorithm": AlgorithmSpecType,
        "WrappingKeySpec": WrappingKeySpecType,
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
        "KeySpec": KeySpecType,
        "KeyUsage": KeyUsageTypeType,
        "EncryptionAlgorithms": List[EncryptionAlgorithmSpecType],
        "SigningAlgorithms": List[SigningAlgorithmSpecType],
        "KeyAgreementAlgorithms": List[Literal["ECDH"]],
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
        "KeySpec": KeySpecType,
        "EncryptionAlgorithms": List[EncryptionAlgorithmSpecType],
        "SigningAlgorithms": List[SigningAlgorithmSpecType],
        "KeyAgreementAlgorithms": List[Literal["ECDH"]],
        "MultiRegion": bool,
        "MultiRegionConfiguration": "MultiRegionConfigurationTypeDef",
        "PendingDeletionWindowInDays": int,
        "MacAlgorithms": List[MacAlgorithmSpecType],
        "XksKeyConfiguration": "XksKeyConfigurationTypeTypeDef",
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

_RequiredListKeyRotationsRequestRequestTypeDef = TypedDict(
    "_RequiredListKeyRotationsRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)
_OptionalListKeyRotationsRequestRequestTypeDef = TypedDict(
    "_OptionalListKeyRotationsRequestRequestTypeDef",
    {
        "Limit": int,
        "Marker": str,
    },
    total=False,
)

class ListKeyRotationsRequestRequestTypeDef(
    _RequiredListKeyRotationsRequestRequestTypeDef, _OptionalListKeyRotationsRequestRequestTypeDef
):
    pass

ListKeyRotationsResponseTypeDef = TypedDict(
    "ListKeyRotationsResponseTypeDef",
    {
        "Rotations": List["RotationsListEntryTypeDef"],
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
        "Policy": str,
    },
)
_OptionalPutKeyPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutKeyPolicyRequestRequestTypeDef",
    {
        "PolicyName": str,
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
        "DryRun": bool,
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

RecipientInfoTypeDef = TypedDict(
    "RecipientInfoTypeDef",
    {
        "KeyEncryptionAlgorithm": Literal["RSAES_OAEP_SHA_256"],
        "AttestationDocument": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
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
        "DryRun": bool,
    },
    total=False,
)

_RequiredRevokeGrantRequestRequestTypeDef = TypedDict(
    "_RequiredRevokeGrantRequestRequestTypeDef",
    {
        "KeyId": str,
        "GrantId": str,
    },
)
_OptionalRevokeGrantRequestRequestTypeDef = TypedDict(
    "_OptionalRevokeGrantRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class RevokeGrantRequestRequestTypeDef(
    _RequiredRevokeGrantRequestRequestTypeDef, _OptionalRevokeGrantRequestRequestTypeDef
):
    pass

RotateKeyOnDemandRequestRequestTypeDef = TypedDict(
    "RotateKeyOnDemandRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)

RotateKeyOnDemandResponseTypeDef = TypedDict(
    "RotateKeyOnDemandResponseTypeDef",
    {
        "KeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RotationsListEntryTypeDef = TypedDict(
    "RotationsListEntryTypeDef",
    {
        "KeyId": str,
        "RotationDate": datetime,
        "RotationType": RotationTypeType,
    },
    total=False,
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
        "DryRun": bool,
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
        "XksProxyUriEndpoint": str,
        "XksProxyUriPath": str,
        "XksProxyVpcEndpointServiceName": str,
        "XksProxyAuthenticationCredential": "XksProxyAuthenticationCredentialTypeTypeDef",
        "XksProxyConnectivity": XksProxyConnectivityTypeType,
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

_RequiredVerifyMacRequestRequestTypeDef = TypedDict(
    "_RequiredVerifyMacRequestRequestTypeDef",
    {
        "Message": Union[bytes, IO[bytes], StreamingBody],
        "KeyId": str,
        "MacAlgorithm": MacAlgorithmSpecType,
        "Mac": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalVerifyMacRequestRequestTypeDef = TypedDict(
    "_OptionalVerifyMacRequestRequestTypeDef",
    {
        "GrantTokens": List[str],
        "DryRun": bool,
    },
    total=False,
)

class VerifyMacRequestRequestTypeDef(
    _RequiredVerifyMacRequestRequestTypeDef, _OptionalVerifyMacRequestRequestTypeDef
):
    pass

VerifyMacResponseTypeDef = TypedDict(
    "VerifyMacResponseTypeDef",
    {
        "KeyId": str,
        "MacValid": bool,
        "MacAlgorithm": MacAlgorithmSpecType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
        "DryRun": bool,
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

XksKeyConfigurationTypeTypeDef = TypedDict(
    "XksKeyConfigurationTypeTypeDef",
    {
        "Id": str,
    },
    total=False,
)

XksProxyAuthenticationCredentialTypeTypeDef = TypedDict(
    "XksProxyAuthenticationCredentialTypeTypeDef",
    {
        "AccessKeyId": str,
        "RawSecretAccessKey": str,
    },
)

XksProxyConfigurationTypeTypeDef = TypedDict(
    "XksProxyConfigurationTypeTypeDef",
    {
        "Connectivity": XksProxyConnectivityTypeType,
        "AccessKeyId": str,
        "UriEndpoint": str,
        "UriPath": str,
        "VpcEndpointServiceName": str,
    },
    total=False,
)
