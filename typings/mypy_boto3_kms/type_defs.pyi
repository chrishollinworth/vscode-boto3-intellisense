"""
Main interface for kms service type definitions.

Usage::

    ```python
    from mypy_boto3_kms.type_defs import AliasListEntryTypeDef

    data: AliasListEntryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

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
    "CustomKeyStoresListEntryTypeDef",
    "GrantConstraintsTypeDef",
    "GrantListEntryTypeDef",
    "KeyListEntryTypeDef",
    "KeyMetadataTypeDef",
    "TagTypeDef",
    "CancelKeyDeletionResponseTypeDef",
    "CreateCustomKeyStoreResponseTypeDef",
    "CreateGrantResponseTypeDef",
    "CreateKeyResponseTypeDef",
    "DecryptResponseTypeDef",
    "DescribeCustomKeyStoresResponseTypeDef",
    "DescribeKeyResponseTypeDef",
    "EncryptResponseTypeDef",
    "GenerateDataKeyPairResponseTypeDef",
    "GenerateDataKeyPairWithoutPlaintextResponseTypeDef",
    "GenerateDataKeyResponseTypeDef",
    "GenerateDataKeyWithoutPlaintextResponseTypeDef",
    "GenerateRandomResponseTypeDef",
    "GetKeyPolicyResponseTypeDef",
    "GetKeyRotationStatusResponseTypeDef",
    "GetParametersForImportResponseTypeDef",
    "GetPublicKeyResponseTypeDef",
    "ListAliasesResponseTypeDef",
    "ListGrantsResponseTypeDef",
    "ListKeyPoliciesResponseTypeDef",
    "ListKeysResponseTypeDef",
    "ListResourceTagsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ReEncryptResponseTypeDef",
    "ScheduleKeyDeletionResponseTypeDef",
    "SignResponseTypeDef",
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

CustomKeyStoresListEntryTypeDef = TypedDict(
    "CustomKeyStoresListEntryTypeDef",
    {
        "CustomKeyStoreId": str,
        "CustomKeyStoreName": str,
        "CloudHsmClusterId": str,
        "TrustAnchorCertificate": str,
        "ConnectionState": Literal[
            "CONNECTED", "CONNECTING", "FAILED", "DISCONNECTED", "DISCONNECTING"
        ],
        "ConnectionErrorCode": Literal[
            "INVALID_CREDENTIALS",
            "CLUSTER_NOT_FOUND",
            "NETWORK_ERRORS",
            "INTERNAL_ERROR",
            "INSUFFICIENT_CLOUDHSM_HSMS",
            "USER_LOCKED_OUT",
            "USER_NOT_FOUND",
            "USER_LOGGED_IN",
            "SUBNET_NOT_FOUND",
        ],
        "CreationDate": datetime,
    },
    total=False,
)

GrantConstraintsTypeDef = TypedDict(
    "GrantConstraintsTypeDef",
    {"EncryptionContextSubset": Dict[str, str], "EncryptionContextEquals": Dict[str, str]},
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
        "Operations": List[
            Literal[
                "Decrypt",
                "Encrypt",
                "GenerateDataKey",
                "GenerateDataKeyWithoutPlaintext",
                "ReEncryptFrom",
                "ReEncryptTo",
                "Sign",
                "Verify",
                "GetPublicKey",
                "CreateGrant",
                "RetireGrant",
                "DescribeKey",
                "GenerateDataKeyPair",
                "GenerateDataKeyPairWithoutPlaintext",
            ]
        ],
        "Constraints": "GrantConstraintsTypeDef",
    },
    total=False,
)

KeyListEntryTypeDef = TypedDict("KeyListEntryTypeDef", {"KeyId": str, "KeyArn": str}, total=False)

_RequiredKeyMetadataTypeDef = TypedDict("_RequiredKeyMetadataTypeDef", {"KeyId": str})
_OptionalKeyMetadataTypeDef = TypedDict(
    "_OptionalKeyMetadataTypeDef",
    {
        "AWSAccountId": str,
        "Arn": str,
        "CreationDate": datetime,
        "Enabled": bool,
        "Description": str,
        "KeyUsage": Literal["SIGN_VERIFY", "ENCRYPT_DECRYPT"],
        "KeyState": Literal[
            "Enabled", "Disabled", "PendingDeletion", "PendingImport", "Unavailable"
        ],
        "DeletionDate": datetime,
        "ValidTo": datetime,
        "Origin": Literal["AWS_KMS", "EXTERNAL", "AWS_CLOUDHSM"],
        "CustomKeyStoreId": str,
        "CloudHsmClusterId": str,
        "ExpirationModel": Literal["KEY_MATERIAL_EXPIRES", "KEY_MATERIAL_DOES_NOT_EXPIRE"],
        "KeyManager": Literal["AWS", "CUSTOMER"],
        "CustomerMasterKeySpec": Literal[
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
            "SYMMETRIC_DEFAULT",
        ],
        "EncryptionAlgorithms": List[
            Literal["SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"]
        ],
        "SigningAlgorithms": List[
            Literal[
                "RSASSA_PSS_SHA_256",
                "RSASSA_PSS_SHA_384",
                "RSASSA_PSS_SHA_512",
                "RSASSA_PKCS1_V1_5_SHA_256",
                "RSASSA_PKCS1_V1_5_SHA_384",
                "RSASSA_PKCS1_V1_5_SHA_512",
                "ECDSA_SHA_256",
                "ECDSA_SHA_384",
                "ECDSA_SHA_512",
            ]
        ],
    },
    total=False,
)


class KeyMetadataTypeDef(_RequiredKeyMetadataTypeDef, _OptionalKeyMetadataTypeDef):
    pass


TagTypeDef = TypedDict("TagTypeDef", {"TagKey": str, "TagValue": str})

CancelKeyDeletionResponseTypeDef = TypedDict(
    "CancelKeyDeletionResponseTypeDef", {"KeyId": str}, total=False
)

CreateCustomKeyStoreResponseTypeDef = TypedDict(
    "CreateCustomKeyStoreResponseTypeDef", {"CustomKeyStoreId": str}, total=False
)

CreateGrantResponseTypeDef = TypedDict(
    "CreateGrantResponseTypeDef", {"GrantToken": str, "GrantId": str}, total=False
)

CreateKeyResponseTypeDef = TypedDict(
    "CreateKeyResponseTypeDef", {"KeyMetadata": "KeyMetadataTypeDef"}, total=False
)

DecryptResponseTypeDef = TypedDict(
    "DecryptResponseTypeDef",
    {
        "KeyId": str,
        "Plaintext": Union[bytes, IO[bytes]],
        "EncryptionAlgorithm": Literal[
            "SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"
        ],
    },
    total=False,
)

DescribeCustomKeyStoresResponseTypeDef = TypedDict(
    "DescribeCustomKeyStoresResponseTypeDef",
    {
        "CustomKeyStores": List["CustomKeyStoresListEntryTypeDef"],
        "NextMarker": str,
        "Truncated": bool,
    },
    total=False,
)

DescribeKeyResponseTypeDef = TypedDict(
    "DescribeKeyResponseTypeDef", {"KeyMetadata": "KeyMetadataTypeDef"}, total=False
)

EncryptResponseTypeDef = TypedDict(
    "EncryptResponseTypeDef",
    {
        "CiphertextBlob": Union[bytes, IO[bytes]],
        "KeyId": str,
        "EncryptionAlgorithm": Literal[
            "SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"
        ],
    },
    total=False,
)

GenerateDataKeyPairResponseTypeDef = TypedDict(
    "GenerateDataKeyPairResponseTypeDef",
    {
        "PrivateKeyCiphertextBlob": Union[bytes, IO[bytes]],
        "PrivateKeyPlaintext": Union[bytes, IO[bytes]],
        "PublicKey": Union[bytes, IO[bytes]],
        "KeyId": str,
        "KeyPairSpec": Literal[
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
        ],
    },
    total=False,
)

GenerateDataKeyPairWithoutPlaintextResponseTypeDef = TypedDict(
    "GenerateDataKeyPairWithoutPlaintextResponseTypeDef",
    {
        "PrivateKeyCiphertextBlob": Union[bytes, IO[bytes]],
        "PublicKey": Union[bytes, IO[bytes]],
        "KeyId": str,
        "KeyPairSpec": Literal[
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
        ],
    },
    total=False,
)

GenerateDataKeyResponseTypeDef = TypedDict(
    "GenerateDataKeyResponseTypeDef",
    {"CiphertextBlob": Union[bytes, IO[bytes]], "Plaintext": Union[bytes, IO[bytes]], "KeyId": str},
    total=False,
)

GenerateDataKeyWithoutPlaintextResponseTypeDef = TypedDict(
    "GenerateDataKeyWithoutPlaintextResponseTypeDef",
    {"CiphertextBlob": Union[bytes, IO[bytes]], "KeyId": str},
    total=False,
)

GenerateRandomResponseTypeDef = TypedDict(
    "GenerateRandomResponseTypeDef", {"Plaintext": Union[bytes, IO[bytes]]}, total=False
)

GetKeyPolicyResponseTypeDef = TypedDict("GetKeyPolicyResponseTypeDef", {"Policy": str}, total=False)

GetKeyRotationStatusResponseTypeDef = TypedDict(
    "GetKeyRotationStatusResponseTypeDef", {"KeyRotationEnabled": bool}, total=False
)

GetParametersForImportResponseTypeDef = TypedDict(
    "GetParametersForImportResponseTypeDef",
    {
        "KeyId": str,
        "ImportToken": Union[bytes, IO[bytes]],
        "PublicKey": Union[bytes, IO[bytes]],
        "ParametersValidTo": datetime,
    },
    total=False,
)

GetPublicKeyResponseTypeDef = TypedDict(
    "GetPublicKeyResponseTypeDef",
    {
        "KeyId": str,
        "PublicKey": Union[bytes, IO[bytes]],
        "CustomerMasterKeySpec": Literal[
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
            "SYMMETRIC_DEFAULT",
        ],
        "KeyUsage": Literal["SIGN_VERIFY", "ENCRYPT_DECRYPT"],
        "EncryptionAlgorithms": List[
            Literal["SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"]
        ],
        "SigningAlgorithms": List[
            Literal[
                "RSASSA_PSS_SHA_256",
                "RSASSA_PSS_SHA_384",
                "RSASSA_PSS_SHA_512",
                "RSASSA_PKCS1_V1_5_SHA_256",
                "RSASSA_PKCS1_V1_5_SHA_384",
                "RSASSA_PKCS1_V1_5_SHA_512",
                "ECDSA_SHA_256",
                "ECDSA_SHA_384",
                "ECDSA_SHA_512",
            ]
        ],
    },
    total=False,
)

ListAliasesResponseTypeDef = TypedDict(
    "ListAliasesResponseTypeDef",
    {"Aliases": List["AliasListEntryTypeDef"], "NextMarker": str, "Truncated": bool},
    total=False,
)

ListGrantsResponseTypeDef = TypedDict(
    "ListGrantsResponseTypeDef",
    {"Grants": List["GrantListEntryTypeDef"], "NextMarker": str, "Truncated": bool},
    total=False,
)

ListKeyPoliciesResponseTypeDef = TypedDict(
    "ListKeyPoliciesResponseTypeDef",
    {"PolicyNames": List[str], "NextMarker": str, "Truncated": bool},
    total=False,
)

ListKeysResponseTypeDef = TypedDict(
    "ListKeysResponseTypeDef",
    {"Keys": List["KeyListEntryTypeDef"], "NextMarker": str, "Truncated": bool},
    total=False,
)

ListResourceTagsResponseTypeDef = TypedDict(
    "ListResourceTagsResponseTypeDef",
    {"Tags": List["TagTypeDef"], "NextMarker": str, "Truncated": bool},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

ReEncryptResponseTypeDef = TypedDict(
    "ReEncryptResponseTypeDef",
    {
        "CiphertextBlob": Union[bytes, IO[bytes]],
        "SourceKeyId": str,
        "KeyId": str,
        "SourceEncryptionAlgorithm": Literal[
            "SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"
        ],
        "DestinationEncryptionAlgorithm": Literal[
            "SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"
        ],
    },
    total=False,
)

ScheduleKeyDeletionResponseTypeDef = TypedDict(
    "ScheduleKeyDeletionResponseTypeDef", {"KeyId": str, "DeletionDate": datetime}, total=False
)

SignResponseTypeDef = TypedDict(
    "SignResponseTypeDef",
    {
        "KeyId": str,
        "Signature": Union[bytes, IO[bytes]],
        "SigningAlgorithm": Literal[
            "RSASSA_PSS_SHA_256",
            "RSASSA_PSS_SHA_384",
            "RSASSA_PSS_SHA_512",
            "RSASSA_PKCS1_V1_5_SHA_256",
            "RSASSA_PKCS1_V1_5_SHA_384",
            "RSASSA_PKCS1_V1_5_SHA_512",
            "ECDSA_SHA_256",
            "ECDSA_SHA_384",
            "ECDSA_SHA_512",
        ],
    },
    total=False,
)

VerifyResponseTypeDef = TypedDict(
    "VerifyResponseTypeDef",
    {
        "KeyId": str,
        "SignatureValid": bool,
        "SigningAlgorithm": Literal[
            "RSASSA_PSS_SHA_256",
            "RSASSA_PSS_SHA_384",
            "RSASSA_PSS_SHA_512",
            "RSASSA_PKCS1_V1_5_SHA_256",
            "RSASSA_PKCS1_V1_5_SHA_384",
            "RSASSA_PKCS1_V1_5_SHA_512",
            "ECDSA_SHA_256",
            "ECDSA_SHA_384",
            "ECDSA_SHA_512",
        ],
    },
    total=False,
)
