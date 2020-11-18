# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for kms service client

Usage::

    ```python
    import boto3
    from mypy_boto3_kms import KMSClient

    client: KMSClient = boto3.client("kms")
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import ClientMeta

from mypy_boto3_kms.paginator import (
    ListAliasesPaginator,
    ListGrantsPaginator,
    ListKeyPoliciesPaginator,
    ListKeysPaginator,
)
from mypy_boto3_kms.type_defs import (
    CancelKeyDeletionResponseTypeDef,
    CreateCustomKeyStoreResponseTypeDef,
    CreateGrantResponseTypeDef,
    CreateKeyResponseTypeDef,
    DecryptResponseTypeDef,
    DescribeCustomKeyStoresResponseTypeDef,
    DescribeKeyResponseTypeDef,
    EncryptResponseTypeDef,
    GenerateDataKeyPairResponseTypeDef,
    GenerateDataKeyPairWithoutPlaintextResponseTypeDef,
    GenerateDataKeyResponseTypeDef,
    GenerateDataKeyWithoutPlaintextResponseTypeDef,
    GenerateRandomResponseTypeDef,
    GetKeyPolicyResponseTypeDef,
    GetKeyRotationStatusResponseTypeDef,
    GetParametersForImportResponseTypeDef,
    GetPublicKeyResponseTypeDef,
    GrantConstraintsTypeDef,
    ListAliasesResponseTypeDef,
    ListGrantsResponseTypeDef,
    ListKeyPoliciesResponseTypeDef,
    ListKeysResponseTypeDef,
    ListResourceTagsResponseTypeDef,
    ReEncryptResponseTypeDef,
    ScheduleKeyDeletionResponseTypeDef,
    SignResponseTypeDef,
    TagTypeDef,
    VerifyResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("KMSClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AlreadyExistsException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    CloudHsmClusterInUseException: Type[BotocoreClientError]
    CloudHsmClusterInvalidConfigurationException: Type[BotocoreClientError]
    CloudHsmClusterNotActiveException: Type[BotocoreClientError]
    CloudHsmClusterNotFoundException: Type[BotocoreClientError]
    CloudHsmClusterNotRelatedException: Type[BotocoreClientError]
    CustomKeyStoreHasCMKsException: Type[BotocoreClientError]
    CustomKeyStoreInvalidStateException: Type[BotocoreClientError]
    CustomKeyStoreNameInUseException: Type[BotocoreClientError]
    CustomKeyStoreNotFoundException: Type[BotocoreClientError]
    DependencyTimeoutException: Type[BotocoreClientError]
    DisabledException: Type[BotocoreClientError]
    ExpiredImportTokenException: Type[BotocoreClientError]
    IncorrectKeyException: Type[BotocoreClientError]
    IncorrectKeyMaterialException: Type[BotocoreClientError]
    IncorrectTrustAnchorException: Type[BotocoreClientError]
    InvalidAliasNameException: Type[BotocoreClientError]
    InvalidArnException: Type[BotocoreClientError]
    InvalidCiphertextException: Type[BotocoreClientError]
    InvalidGrantIdException: Type[BotocoreClientError]
    InvalidGrantTokenException: Type[BotocoreClientError]
    InvalidImportTokenException: Type[BotocoreClientError]
    InvalidKeyUsageException: Type[BotocoreClientError]
    InvalidMarkerException: Type[BotocoreClientError]
    KMSInternalException: Type[BotocoreClientError]
    KMSInvalidSignatureException: Type[BotocoreClientError]
    KMSInvalidStateException: Type[BotocoreClientError]
    KeyUnavailableException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MalformedPolicyDocumentException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    TagException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]


class KMSClient:
    """
    [KMS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.can_paginate)
        """

    def cancel_key_deletion(self, KeyId: str) -> CancelKeyDeletionResponseTypeDef:
        """
        [Client.cancel_key_deletion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.cancel_key_deletion)
        """

    def connect_custom_key_store(self, CustomKeyStoreId: str) -> Dict[str, Any]:
        """
        [Client.connect_custom_key_store documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.connect_custom_key_store)
        """

    def create_alias(self, AliasName: str, TargetKeyId: str) -> None:
        """
        [Client.create_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.create_alias)
        """

    def create_custom_key_store(
        self,
        CustomKeyStoreName: str,
        CloudHsmClusterId: str,
        TrustAnchorCertificate: str,
        KeyStorePassword: str,
    ) -> CreateCustomKeyStoreResponseTypeDef:
        """
        [Client.create_custom_key_store documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.create_custom_key_store)
        """

    def create_grant(
        self,
        KeyId: str,
        GranteePrincipal: str,
        Operations: List[
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
        RetiringPrincipal: str = None,
        Constraints: "GrantConstraintsTypeDef" = None,
        GrantTokens: List[str] = None,
        Name: str = None,
    ) -> CreateGrantResponseTypeDef:
        """
        [Client.create_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.create_grant)
        """

    def create_key(
        self,
        Policy: str = None,
        Description: str = None,
        KeyUsage: Literal["SIGN_VERIFY", "ENCRYPT_DECRYPT"] = None,
        CustomerMasterKeySpec: Literal[
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
            "SYMMETRIC_DEFAULT",
        ] = None,
        Origin: Literal["AWS_KMS", "EXTERNAL", "AWS_CLOUDHSM"] = None,
        CustomKeyStoreId: str = None,
        BypassPolicyLockoutSafetyCheck: bool = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateKeyResponseTypeDef:
        """
        [Client.create_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.create_key)
        """

    def decrypt(
        self,
        CiphertextBlob: Union[bytes, IO[bytes]],
        EncryptionContext: Dict[str, str] = None,
        GrantTokens: List[str] = None,
        KeyId: str = None,
        EncryptionAlgorithm: Literal[
            "SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"
        ] = None,
    ) -> DecryptResponseTypeDef:
        """
        [Client.decrypt documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.decrypt)
        """

    def delete_alias(self, AliasName: str) -> None:
        """
        [Client.delete_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.delete_alias)
        """

    def delete_custom_key_store(self, CustomKeyStoreId: str) -> Dict[str, Any]:
        """
        [Client.delete_custom_key_store documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.delete_custom_key_store)
        """

    def delete_imported_key_material(self, KeyId: str) -> None:
        """
        [Client.delete_imported_key_material documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.delete_imported_key_material)
        """

    def describe_custom_key_stores(
        self,
        CustomKeyStoreId: str = None,
        CustomKeyStoreName: str = None,
        Limit: int = None,
        Marker: str = None,
    ) -> DescribeCustomKeyStoresResponseTypeDef:
        """
        [Client.describe_custom_key_stores documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.describe_custom_key_stores)
        """

    def describe_key(self, KeyId: str, GrantTokens: List[str] = None) -> DescribeKeyResponseTypeDef:
        """
        [Client.describe_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.describe_key)
        """

    def disable_key(self, KeyId: str) -> None:
        """
        [Client.disable_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.disable_key)
        """

    def disable_key_rotation(self, KeyId: str) -> None:
        """
        [Client.disable_key_rotation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.disable_key_rotation)
        """

    def disconnect_custom_key_store(self, CustomKeyStoreId: str) -> Dict[str, Any]:
        """
        [Client.disconnect_custom_key_store documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.disconnect_custom_key_store)
        """

    def enable_key(self, KeyId: str) -> None:
        """
        [Client.enable_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.enable_key)
        """

    def enable_key_rotation(self, KeyId: str) -> None:
        """
        [Client.enable_key_rotation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.enable_key_rotation)
        """

    def encrypt(
        self,
        KeyId: str,
        Plaintext: Union[bytes, IO[bytes]],
        EncryptionContext: Dict[str, str] = None,
        GrantTokens: List[str] = None,
        EncryptionAlgorithm: Literal[
            "SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"
        ] = None,
    ) -> EncryptResponseTypeDef:
        """
        [Client.encrypt documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.encrypt)
        """

    def generate_data_key(
        self,
        KeyId: str,
        EncryptionContext: Dict[str, str] = None,
        NumberOfBytes: int = None,
        KeySpec: Literal["AES_256", "AES_128"] = None,
        GrantTokens: List[str] = None,
    ) -> GenerateDataKeyResponseTypeDef:
        """
        [Client.generate_data_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.generate_data_key)
        """

    def generate_data_key_pair(
        self,
        KeyId: str,
        KeyPairSpec: Literal[
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
        ],
        EncryptionContext: Dict[str, str] = None,
        GrantTokens: List[str] = None,
    ) -> GenerateDataKeyPairResponseTypeDef:
        """
        [Client.generate_data_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.generate_data_key_pair)
        """

    def generate_data_key_pair_without_plaintext(
        self,
        KeyId: str,
        KeyPairSpec: Literal[
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
        ],
        EncryptionContext: Dict[str, str] = None,
        GrantTokens: List[str] = None,
    ) -> GenerateDataKeyPairWithoutPlaintextResponseTypeDef:
        """
        [Client.generate_data_key_pair_without_plaintext documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.generate_data_key_pair_without_plaintext)
        """

    def generate_data_key_without_plaintext(
        self,
        KeyId: str,
        EncryptionContext: Dict[str, str] = None,
        KeySpec: Literal["AES_256", "AES_128"] = None,
        NumberOfBytes: int = None,
        GrantTokens: List[str] = None,
    ) -> GenerateDataKeyWithoutPlaintextResponseTypeDef:
        """
        [Client.generate_data_key_without_plaintext documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.generate_data_key_without_plaintext)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.generate_presigned_url)
        """

    def generate_random(
        self, NumberOfBytes: int = None, CustomKeyStoreId: str = None
    ) -> GenerateRandomResponseTypeDef:
        """
        [Client.generate_random documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.generate_random)
        """

    def get_key_policy(self, KeyId: str, PolicyName: str) -> GetKeyPolicyResponseTypeDef:
        """
        [Client.get_key_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.get_key_policy)
        """

    def get_key_rotation_status(self, KeyId: str) -> GetKeyRotationStatusResponseTypeDef:
        """
        [Client.get_key_rotation_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.get_key_rotation_status)
        """

    def get_parameters_for_import(
        self,
        KeyId: str,
        WrappingAlgorithm: Literal["RSAES_PKCS1_V1_5", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"],
        WrappingKeySpec: Literal["RSA_2048"],
    ) -> GetParametersForImportResponseTypeDef:
        """
        [Client.get_parameters_for_import documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.get_parameters_for_import)
        """

    def get_public_key(
        self, KeyId: str, GrantTokens: List[str] = None
    ) -> GetPublicKeyResponseTypeDef:
        """
        [Client.get_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.get_public_key)
        """

    def import_key_material(
        self,
        KeyId: str,
        ImportToken: Union[bytes, IO[bytes]],
        EncryptedKeyMaterial: Union[bytes, IO[bytes]],
        ValidTo: datetime = None,
        ExpirationModel: Literal["KEY_MATERIAL_EXPIRES", "KEY_MATERIAL_DOES_NOT_EXPIRE"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.import_key_material documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.import_key_material)
        """

    def list_aliases(
        self, KeyId: str = None, Limit: int = None, Marker: str = None
    ) -> ListAliasesResponseTypeDef:
        """
        [Client.list_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.list_aliases)
        """

    def list_grants(
        self, KeyId: str, Limit: int = None, Marker: str = None
    ) -> ListGrantsResponseTypeDef:
        """
        [Client.list_grants documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.list_grants)
        """

    def list_key_policies(
        self, KeyId: str, Limit: int = None, Marker: str = None
    ) -> ListKeyPoliciesResponseTypeDef:
        """
        [Client.list_key_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.list_key_policies)
        """

    def list_keys(self, Limit: int = None, Marker: str = None) -> ListKeysResponseTypeDef:
        """
        [Client.list_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.list_keys)
        """

    def list_resource_tags(
        self, KeyId: str, Limit: int = None, Marker: str = None
    ) -> ListResourceTagsResponseTypeDef:
        """
        [Client.list_resource_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.list_resource_tags)
        """

    def list_retirable_grants(
        self, RetiringPrincipal: str, Limit: int = None, Marker: str = None
    ) -> ListGrantsResponseTypeDef:
        """
        [Client.list_retirable_grants documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.list_retirable_grants)
        """

    def put_key_policy(
        self, KeyId: str, PolicyName: str, Policy: str, BypassPolicyLockoutSafetyCheck: bool = None
    ) -> None:
        """
        [Client.put_key_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.put_key_policy)
        """

    def re_encrypt(
        self,
        CiphertextBlob: Union[bytes, IO[bytes]],
        DestinationKeyId: str,
        SourceEncryptionContext: Dict[str, str] = None,
        SourceKeyId: str = None,
        DestinationEncryptionContext: Dict[str, str] = None,
        SourceEncryptionAlgorithm: Literal[
            "SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"
        ] = None,
        DestinationEncryptionAlgorithm: Literal[
            "SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"
        ] = None,
        GrantTokens: List[str] = None,
    ) -> ReEncryptResponseTypeDef:
        """
        [Client.re_encrypt documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.re_encrypt)
        """

    def retire_grant(self, GrantToken: str = None, KeyId: str = None, GrantId: str = None) -> None:
        """
        [Client.retire_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.retire_grant)
        """

    def revoke_grant(self, KeyId: str, GrantId: str) -> None:
        """
        [Client.revoke_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.revoke_grant)
        """

    def schedule_key_deletion(
        self, KeyId: str, PendingWindowInDays: int = None
    ) -> ScheduleKeyDeletionResponseTypeDef:
        """
        [Client.schedule_key_deletion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.schedule_key_deletion)
        """

    def sign(
        self,
        KeyId: str,
        Message: Union[bytes, IO[bytes]],
        SigningAlgorithm: Literal[
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
        MessageType: Literal["RAW", "DIGEST"] = None,
        GrantTokens: List[str] = None,
    ) -> SignResponseTypeDef:
        """
        [Client.sign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.sign)
        """

    def tag_resource(self, KeyId: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.tag_resource)
        """

    def untag_resource(self, KeyId: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.untag_resource)
        """

    def update_alias(self, AliasName: str, TargetKeyId: str) -> None:
        """
        [Client.update_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.update_alias)
        """

    def update_custom_key_store(
        self,
        CustomKeyStoreId: str,
        NewCustomKeyStoreName: str = None,
        KeyStorePassword: str = None,
        CloudHsmClusterId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_custom_key_store documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.update_custom_key_store)
        """

    def update_key_description(self, KeyId: str, Description: str) -> None:
        """
        [Client.update_key_description documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.update_key_description)
        """

    def verify(
        self,
        KeyId: str,
        Message: Union[bytes, IO[bytes]],
        Signature: Union[bytes, IO[bytes]],
        SigningAlgorithm: Literal[
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
        MessageType: Literal["RAW", "DIGEST"] = None,
        GrantTokens: List[str] = None,
    ) -> VerifyResponseTypeDef:
        """
        [Client.verify documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Client.verify)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_aliases"]) -> ListAliasesPaginator:
        """
        [Paginator.ListAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Paginator.ListAliases)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_grants"]) -> ListGrantsPaginator:
        """
        [Paginator.ListGrants documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Paginator.ListGrants)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_key_policies"]
    ) -> ListKeyPoliciesPaginator:
        """
        [Paginator.ListKeyPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Paginator.ListKeyPolicies)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_keys"]) -> ListKeysPaginator:
        """
        [Paginator.ListKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Paginator.ListKeys)
        """
