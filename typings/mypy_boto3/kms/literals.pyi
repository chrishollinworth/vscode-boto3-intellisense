"""
Type annotations for kms service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/literals.html)

Usage::

    ```python
    from mypy_boto3_kms.literals import AlgorithmSpecType

    data: AlgorithmSpecType = "RSA_AES_KEY_WRAP_SHA_1"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AlgorithmSpecType",
    "ConnectionErrorCodeTypeType",
    "ConnectionStateTypeType",
    "CustomKeyStoreTypeType",
    "CustomerMasterKeySpecType",
    "DataKeyPairSpecType",
    "DataKeySpecType",
    "DescribeCustomKeyStoresPaginatorName",
    "EncryptionAlgorithmSpecType",
    "ExpirationModelTypeType",
    "GrantOperationType",
    "KeyAgreementAlgorithmSpecType",
    "KeyEncryptionMechanismType",
    "KeyManagerTypeType",
    "KeySpecType",
    "KeyStateType",
    "KeyUsageTypeType",
    "ListAliasesPaginatorName",
    "ListGrantsPaginatorName",
    "ListKeyPoliciesPaginatorName",
    "ListKeyRotationsPaginatorName",
    "ListKeysPaginatorName",
    "ListResourceTagsPaginatorName",
    "ListRetirableGrantsPaginatorName",
    "MacAlgorithmSpecType",
    "MessageTypeType",
    "MultiRegionKeyTypeType",
    "OriginTypeType",
    "RotationTypeType",
    "SigningAlgorithmSpecType",
    "WrappingKeySpecType",
    "XksProxyConnectivityTypeType",
)

AlgorithmSpecType = Literal[
    "RSAES_OAEP_SHA_1",
    "RSAES_OAEP_SHA_256",
    "RSAES_PKCS1_V1_5",
    "RSA_AES_KEY_WRAP_SHA_1",
    "RSA_AES_KEY_WRAP_SHA_256",
    "SM2PKE",
]
ConnectionErrorCodeTypeType = Literal[
    "CLUSTER_NOT_FOUND",
    "INSUFFICIENT_CLOUDHSM_HSMS",
    "INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET",
    "INTERNAL_ERROR",
    "INVALID_CREDENTIALS",
    "NETWORK_ERRORS",
    "SUBNET_NOT_FOUND",
    "USER_LOCKED_OUT",
    "USER_LOGGED_IN",
    "USER_NOT_FOUND",
    "XKS_PROXY_ACCESS_DENIED",
    "XKS_PROXY_INVALID_CONFIGURATION",
    "XKS_PROXY_INVALID_RESPONSE",
    "XKS_PROXY_INVALID_TLS_CONFIGURATION",
    "XKS_PROXY_NOT_REACHABLE",
    "XKS_PROXY_TIMED_OUT",
    "XKS_VPC_ENDPOINT_SERVICE_INVALID_CONFIGURATION",
    "XKS_VPC_ENDPOINT_SERVICE_NOT_FOUND",
]
ConnectionStateTypeType = Literal[
    "CONNECTED", "CONNECTING", "DISCONNECTED", "DISCONNECTING", "FAILED"
]
CustomKeyStoreTypeType = Literal["AWS_CLOUDHSM", "EXTERNAL_KEY_STORE"]
CustomerMasterKeySpecType = Literal[
    "ECC_NIST_P256",
    "ECC_NIST_P384",
    "ECC_NIST_P521",
    "ECC_SECG_P256K1",
    "HMAC_224",
    "HMAC_256",
    "HMAC_384",
    "HMAC_512",
    "RSA_2048",
    "RSA_3072",
    "RSA_4096",
    "SM2",
    "SYMMETRIC_DEFAULT",
]
DataKeyPairSpecType = Literal[
    "ECC_NIST_P256",
    "ECC_NIST_P384",
    "ECC_NIST_P521",
    "ECC_SECG_P256K1",
    "RSA_2048",
    "RSA_3072",
    "RSA_4096",
    "SM2",
]
DataKeySpecType = Literal["AES_128", "AES_256"]
DescribeCustomKeyStoresPaginatorName = Literal["describe_custom_key_stores"]
EncryptionAlgorithmSpecType = Literal[
    "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256", "SM2PKE", "SYMMETRIC_DEFAULT"
]
ExpirationModelTypeType = Literal["KEY_MATERIAL_DOES_NOT_EXPIRE", "KEY_MATERIAL_EXPIRES"]
GrantOperationType = Literal[
    "CreateGrant",
    "Decrypt",
    "DeriveSharedSecret",
    "DescribeKey",
    "Encrypt",
    "GenerateDataKey",
    "GenerateDataKeyPair",
    "GenerateDataKeyPairWithoutPlaintext",
    "GenerateDataKeyWithoutPlaintext",
    "GenerateMac",
    "GetPublicKey",
    "ReEncryptFrom",
    "ReEncryptTo",
    "RetireGrant",
    "Sign",
    "Verify",
    "VerifyMac",
]
KeyAgreementAlgorithmSpecType = Literal["ECDH"]
KeyEncryptionMechanismType = Literal["RSAES_OAEP_SHA_256"]
KeyManagerTypeType = Literal["AWS", "CUSTOMER"]
KeySpecType = Literal[
    "ECC_NIST_P256",
    "ECC_NIST_P384",
    "ECC_NIST_P521",
    "ECC_SECG_P256K1",
    "HMAC_224",
    "HMAC_256",
    "HMAC_384",
    "HMAC_512",
    "RSA_2048",
    "RSA_3072",
    "RSA_4096",
    "SM2",
    "SYMMETRIC_DEFAULT",
]
KeyStateType = Literal[
    "Creating",
    "Disabled",
    "Enabled",
    "PendingDeletion",
    "PendingImport",
    "PendingReplicaDeletion",
    "Unavailable",
    "Updating",
]
KeyUsageTypeType = Literal["ENCRYPT_DECRYPT", "GENERATE_VERIFY_MAC", "KEY_AGREEMENT", "SIGN_VERIFY"]
ListAliasesPaginatorName = Literal["list_aliases"]
ListGrantsPaginatorName = Literal["list_grants"]
ListKeyPoliciesPaginatorName = Literal["list_key_policies"]
ListKeyRotationsPaginatorName = Literal["list_key_rotations"]
ListKeysPaginatorName = Literal["list_keys"]
ListResourceTagsPaginatorName = Literal["list_resource_tags"]
ListRetirableGrantsPaginatorName = Literal["list_retirable_grants"]
MacAlgorithmSpecType = Literal["HMAC_SHA_224", "HMAC_SHA_256", "HMAC_SHA_384", "HMAC_SHA_512"]
MessageTypeType = Literal["DIGEST", "RAW"]
MultiRegionKeyTypeType = Literal["PRIMARY", "REPLICA"]
OriginTypeType = Literal["AWS_CLOUDHSM", "AWS_KMS", "EXTERNAL", "EXTERNAL_KEY_STORE"]
RotationTypeType = Literal["AUTOMATIC", "ON_DEMAND"]
SigningAlgorithmSpecType = Literal[
    "ECDSA_SHA_256",
    "ECDSA_SHA_384",
    "ECDSA_SHA_512",
    "RSASSA_PKCS1_V1_5_SHA_256",
    "RSASSA_PKCS1_V1_5_SHA_384",
    "RSASSA_PKCS1_V1_5_SHA_512",
    "RSASSA_PSS_SHA_256",
    "RSASSA_PSS_SHA_384",
    "RSASSA_PSS_SHA_512",
    "SM2DSA",
]
WrappingKeySpecType = Literal["RSA_2048", "RSA_3072", "RSA_4096", "SM2"]
XksProxyConnectivityTypeType = Literal["PUBLIC_ENDPOINT", "VPC_ENDPOINT_SERVICE"]
