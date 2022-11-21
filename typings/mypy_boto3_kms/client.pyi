"""
Type annotations for kms service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html)

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

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import (
    AlgorithmSpecType,
    CustomerMasterKeySpecType,
    DataKeyPairSpecType,
    DataKeySpecType,
    EncryptionAlgorithmSpecType,
    ExpirationModelTypeType,
    GrantOperationType,
    KeySpecType,
    KeyUsageTypeType,
    MacAlgorithmSpecType,
    MessageTypeType,
    OriginTypeType,
    SigningAlgorithmSpecType,
)
from .paginator import (
    DescribeCustomKeyStoresPaginator,
    ListAliasesPaginator,
    ListGrantsPaginator,
    ListKeyPoliciesPaginator,
    ListKeysPaginator,
    ListResourceTagsPaginator,
    ListRetirableGrantsPaginator,
)
from .type_defs import (
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
    GenerateMacResponseTypeDef,
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
    ReplicateKeyResponseTypeDef,
    ScheduleKeyDeletionResponseTypeDef,
    SignResponseTypeDef,
    TagTypeDef,
    VerifyMacResponseTypeDef,
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
    KMSInvalidMacException: Type[BotocoreClientError]
    KMSInvalidSignatureException: Type[BotocoreClientError]
    KMSInvalidStateException: Type[BotocoreClientError]
    KeyUnavailableException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MalformedPolicyDocumentException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    TagException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]

class KMSClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        KMSClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#can_paginate)
        """
    def cancel_key_deletion(self, *, KeyId: str) -> CancelKeyDeletionResponseTypeDef:
        """
        Cancels the deletion of a KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.cancel_key_deletion)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#cancel_key_deletion)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#close)
        """
    def connect_custom_key_store(self, *, CustomKeyStoreId: str) -> Dict[str, Any]:
        """
        Connects or reconnects a `custom key store
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-
        overview.html>`__ to its associated CloudHSM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.connect_custom_key_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#connect_custom_key_store)
        """
    def create_alias(self, *, AliasName: str, TargetKeyId: str) -> None:
        """
        Creates a friendly name for a KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.create_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#create_alias)
        """
    def create_custom_key_store(
        self,
        *,
        CustomKeyStoreName: str,
        CloudHsmClusterId: str = None,
        TrustAnchorCertificate: str = None,
        KeyStorePassword: str = None
    ) -> CreateCustomKeyStoreResponseTypeDef:
        """
        Creates a `custom key store
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-
        overview.html>`__ that is associated with an `CloudHSM cluster
        <https://docs.aws.amazon.com/cloudhsm/latest/userguide/clusters.html>`__ that
        you own and manage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.create_custom_key_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#create_custom_key_store)
        """
    def create_grant(
        self,
        *,
        KeyId: str,
        GranteePrincipal: str,
        Operations: List[GrantOperationType],
        RetiringPrincipal: str = None,
        Constraints: "GrantConstraintsTypeDef" = None,
        GrantTokens: List[str] = None,
        Name: str = None
    ) -> CreateGrantResponseTypeDef:
        """
        Adds a grant to a KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.create_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#create_grant)
        """
    def create_key(
        self,
        *,
        Policy: str = None,
        Description: str = None,
        KeyUsage: KeyUsageTypeType = None,
        CustomerMasterKeySpec: CustomerMasterKeySpecType = None,
        KeySpec: KeySpecType = None,
        Origin: OriginTypeType = None,
        CustomKeyStoreId: str = None,
        BypassPolicyLockoutSafetyCheck: bool = None,
        Tags: List["TagTypeDef"] = None,
        MultiRegion: bool = None
    ) -> CreateKeyResponseTypeDef:
        """
        Creates a unique customer managed `KMS key
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms-
        keys>`__ in your Amazon Web Services account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.create_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#create_key)
        """
    def decrypt(
        self,
        *,
        CiphertextBlob: Union[bytes, IO[bytes], StreamingBody],
        EncryptionContext: Dict[str, str] = None,
        GrantTokens: List[str] = None,
        KeyId: str = None,
        EncryptionAlgorithm: EncryptionAlgorithmSpecType = None
    ) -> DecryptResponseTypeDef:
        """
        Decrypts ciphertext that was encrypted by a KMS key using any of the following
        operations *  Encrypt *  GenerateDataKey *  GenerateDataKeyPair *
        GenerateDataKeyWithoutPlaintext *  GenerateDataKeyPairWithoutPlaintext You can
        use this operation to decrypt cipher...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.decrypt)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#decrypt)
        """
    def delete_alias(self, *, AliasName: str) -> None:
        """
        Deletes the specified alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.delete_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#delete_alias)
        """
    def delete_custom_key_store(self, *, CustomKeyStoreId: str) -> Dict[str, Any]:
        """
        Deletes a `custom key store
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-
        overview.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.delete_custom_key_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#delete_custom_key_store)
        """
    def delete_imported_key_material(self, *, KeyId: str) -> None:
        """
        Deletes key material that you previously imported.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.delete_imported_key_material)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#delete_imported_key_material)
        """
    def describe_custom_key_stores(
        self,
        *,
        CustomKeyStoreId: str = None,
        CustomKeyStoreName: str = None,
        Limit: int = None,
        Marker: str = None
    ) -> DescribeCustomKeyStoresResponseTypeDef:
        """
        Gets information about `custom key stores
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-
        overview.html>`__ in the account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.describe_custom_key_stores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#describe_custom_key_stores)
        """
    def describe_key(
        self, *, KeyId: str, GrantTokens: List[str] = None
    ) -> DescribeKeyResponseTypeDef:
        """
        Provides detailed information about a KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.describe_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#describe_key)
        """
    def disable_key(self, *, KeyId: str) -> None:
        """
        Sets the state of a KMS key to disabled.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.disable_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#disable_key)
        """
    def disable_key_rotation(self, *, KeyId: str) -> None:
        """
        Disables `automatic rotation of the key material
        <https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html>`__ of
        the specified symmetric encryption KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.disable_key_rotation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#disable_key_rotation)
        """
    def disconnect_custom_key_store(self, *, CustomKeyStoreId: str) -> Dict[str, Any]:
        """
        Disconnects the `custom key store
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-
        overview.html>`__ from its associated CloudHSM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.disconnect_custom_key_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#disconnect_custom_key_store)
        """
    def enable_key(self, *, KeyId: str) -> None:
        """
        Sets the key state of a KMS key to enabled.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.enable_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#enable_key)
        """
    def enable_key_rotation(self, *, KeyId: str) -> None:
        """
        Enables `automatic rotation of the key material
        <https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html>`__ of
        the specified symmetric encryption KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.enable_key_rotation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#enable_key_rotation)
        """
    def encrypt(
        self,
        *,
        KeyId: str,
        Plaintext: Union[bytes, IO[bytes], StreamingBody],
        EncryptionContext: Dict[str, str] = None,
        GrantTokens: List[str] = None,
        EncryptionAlgorithm: EncryptionAlgorithmSpecType = None
    ) -> EncryptResponseTypeDef:
        """
        Encrypts plaintext of up to 4,096 bytes using a KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.encrypt)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#encrypt)
        """
    def generate_data_key(
        self,
        *,
        KeyId: str,
        EncryptionContext: Dict[str, str] = None,
        NumberOfBytes: int = None,
        KeySpec: DataKeySpecType = None,
        GrantTokens: List[str] = None
    ) -> GenerateDataKeyResponseTypeDef:
        """
        Returns a unique symmetric data key for use outside of KMS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.generate_data_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#generate_data_key)
        """
    def generate_data_key_pair(
        self,
        *,
        KeyId: str,
        KeyPairSpec: DataKeyPairSpecType,
        EncryptionContext: Dict[str, str] = None,
        GrantTokens: List[str] = None
    ) -> GenerateDataKeyPairResponseTypeDef:
        """
        Returns a unique asymmetric data key pair for use outside of KMS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.generate_data_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#generate_data_key_pair)
        """
    def generate_data_key_pair_without_plaintext(
        self,
        *,
        KeyId: str,
        KeyPairSpec: DataKeyPairSpecType,
        EncryptionContext: Dict[str, str] = None,
        GrantTokens: List[str] = None
    ) -> GenerateDataKeyPairWithoutPlaintextResponseTypeDef:
        """
        Returns a unique asymmetric data key pair for use outside of KMS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.generate_data_key_pair_without_plaintext)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#generate_data_key_pair_without_plaintext)
        """
    def generate_data_key_without_plaintext(
        self,
        *,
        KeyId: str,
        EncryptionContext: Dict[str, str] = None,
        KeySpec: DataKeySpecType = None,
        NumberOfBytes: int = None,
        GrantTokens: List[str] = None
    ) -> GenerateDataKeyWithoutPlaintextResponseTypeDef:
        """
        Returns a unique symmetric data key for use outside of KMS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.generate_data_key_without_plaintext)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#generate_data_key_without_plaintext)
        """
    def generate_mac(
        self,
        *,
        Message: Union[bytes, IO[bytes], StreamingBody],
        KeyId: str,
        MacAlgorithm: MacAlgorithmSpecType,
        GrantTokens: List[str] = None
    ) -> GenerateMacResponseTypeDef:
        """
        Generates a hash-based message authentication code (HMAC) for a message using an
        HMAC KMS key and a MAC algorithm that the key supports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.generate_mac)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#generate_mac)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#generate_presigned_url)
        """
    def generate_random(
        self, *, NumberOfBytes: int = None, CustomKeyStoreId: str = None
    ) -> GenerateRandomResponseTypeDef:
        """
        Returns a random byte string that is cryptographically secure.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.generate_random)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#generate_random)
        """
    def get_key_policy(self, *, KeyId: str, PolicyName: str) -> GetKeyPolicyResponseTypeDef:
        """
        Gets a key policy attached to the specified KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.get_key_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#get_key_policy)
        """
    def get_key_rotation_status(self, *, KeyId: str) -> GetKeyRotationStatusResponseTypeDef:
        """
        Gets a Boolean value that indicates whether `automatic rotation of the key
        material <https://docs.aws.amazon.com/kms/latest/developerguide/rotate-
        keys.html>`__ is enabled for the specified KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.get_key_rotation_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#get_key_rotation_status)
        """
    def get_parameters_for_import(
        self,
        *,
        KeyId: str,
        WrappingAlgorithm: AlgorithmSpecType,
        WrappingKeySpec: Literal["RSA_2048"]
    ) -> GetParametersForImportResponseTypeDef:
        """
        Returns the items you need to import key material into a symmetric encryption
        KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.get_parameters_for_import)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#get_parameters_for_import)
        """
    def get_public_key(
        self, *, KeyId: str, GrantTokens: List[str] = None
    ) -> GetPublicKeyResponseTypeDef:
        """
        Returns the public key of an asymmetric KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.get_public_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#get_public_key)
        """
    def import_key_material(
        self,
        *,
        KeyId: str,
        ImportToken: Union[bytes, IO[bytes], StreamingBody],
        EncryptedKeyMaterial: Union[bytes, IO[bytes], StreamingBody],
        ValidTo: Union[datetime, str] = None,
        ExpirationModel: ExpirationModelTypeType = None
    ) -> Dict[str, Any]:
        """
        Imports key material into an existing symmetric encryption KMS key that was
        created without key material.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.import_key_material)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#import_key_material)
        """
    def list_aliases(
        self, *, KeyId: str = None, Limit: int = None, Marker: str = None
    ) -> ListAliasesResponseTypeDef:
        """
        Gets a list of aliases in the caller's Amazon Web Services account and region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.list_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#list_aliases)
        """
    def list_grants(
        self,
        *,
        KeyId: str,
        Limit: int = None,
        Marker: str = None,
        GrantId: str = None,
        GranteePrincipal: str = None
    ) -> ListGrantsResponseTypeDef:
        """
        Gets a list of all grants for the specified KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.list_grants)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#list_grants)
        """
    def list_key_policies(
        self, *, KeyId: str, Limit: int = None, Marker: str = None
    ) -> ListKeyPoliciesResponseTypeDef:
        """
        Gets the names of the key policies that are attached to a KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.list_key_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#list_key_policies)
        """
    def list_keys(self, *, Limit: int = None, Marker: str = None) -> ListKeysResponseTypeDef:
        """
        Gets a list of all KMS keys in the caller's Amazon Web Services account and
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.list_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#list_keys)
        """
    def list_resource_tags(
        self, *, KeyId: str, Limit: int = None, Marker: str = None
    ) -> ListResourceTagsResponseTypeDef:
        """
        Returns all tags on the specified KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.list_resource_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#list_resource_tags)
        """
    def list_retirable_grants(
        self, *, RetiringPrincipal: str, Limit: int = None, Marker: str = None
    ) -> ListGrantsResponseTypeDef:
        """
        Returns information about all grants in the Amazon Web Services account and
        Region that have the specified retiring principal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.list_retirable_grants)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#list_retirable_grants)
        """
    def put_key_policy(
        self,
        *,
        KeyId: str,
        PolicyName: str,
        Policy: str,
        BypassPolicyLockoutSafetyCheck: bool = None
    ) -> None:
        """
        Attaches a key policy to the specified KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.put_key_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#put_key_policy)
        """
    def re_encrypt(
        self,
        *,
        CiphertextBlob: Union[bytes, IO[bytes], StreamingBody],
        DestinationKeyId: str,
        SourceEncryptionContext: Dict[str, str] = None,
        SourceKeyId: str = None,
        DestinationEncryptionContext: Dict[str, str] = None,
        SourceEncryptionAlgorithm: EncryptionAlgorithmSpecType = None,
        DestinationEncryptionAlgorithm: EncryptionAlgorithmSpecType = None,
        GrantTokens: List[str] = None
    ) -> ReEncryptResponseTypeDef:
        """
        Decrypts ciphertext and then reencrypts it entirely within KMS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.re_encrypt)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#re_encrypt)
        """
    def replicate_key(
        self,
        *,
        KeyId: str,
        ReplicaRegion: str,
        Policy: str = None,
        BypassPolicyLockoutSafetyCheck: bool = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> ReplicateKeyResponseTypeDef:
        """
        Replicates a multi-Region key into the specified Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.replicate_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#replicate_key)
        """
    def retire_grant(
        self, *, GrantToken: str = None, KeyId: str = None, GrantId: str = None
    ) -> None:
        """
        Deletes a grant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.retire_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#retire_grant)
        """
    def revoke_grant(self, *, KeyId: str, GrantId: str) -> None:
        """
        Deletes the specified grant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.revoke_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#revoke_grant)
        """
    def schedule_key_deletion(
        self, *, KeyId: str, PendingWindowInDays: int = None
    ) -> ScheduleKeyDeletionResponseTypeDef:
        """
        Schedules the deletion of a KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.schedule_key_deletion)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#schedule_key_deletion)
        """
    def sign(
        self,
        *,
        KeyId: str,
        Message: Union[bytes, IO[bytes], StreamingBody],
        SigningAlgorithm: SigningAlgorithmSpecType,
        MessageType: MessageTypeType = None,
        GrantTokens: List[str] = None
    ) -> SignResponseTypeDef:
        """
        Creates a `digital signature
        <https://en.wikipedia.org/wiki/Digital_signature>`__ for a message or message
        digest by using the private key in an asymmetric signing KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.sign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#sign)
        """
    def tag_resource(self, *, KeyId: str, Tags: List["TagTypeDef"]) -> None:
        """
        Adds or edits tags on a `customer managed key
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-
        cmk>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#tag_resource)
        """
    def untag_resource(self, *, KeyId: str, TagKeys: List[str]) -> None:
        """
        Deletes tags from a `customer managed key
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-
        cmk>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#untag_resource)
        """
    def update_alias(self, *, AliasName: str, TargetKeyId: str) -> None:
        """
        Associates an existing KMS alias with a different KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.update_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#update_alias)
        """
    def update_custom_key_store(
        self,
        *,
        CustomKeyStoreId: str,
        NewCustomKeyStoreName: str = None,
        KeyStorePassword: str = None,
        CloudHsmClusterId: str = None
    ) -> Dict[str, Any]:
        """
        Changes the properties of a custom key store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.update_custom_key_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#update_custom_key_store)
        """
    def update_key_description(self, *, KeyId: str, Description: str) -> None:
        """
        Updates the description of a KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.update_key_description)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#update_key_description)
        """
    def update_primary_region(self, *, KeyId: str, PrimaryRegion: str) -> None:
        """
        Changes the primary key of a multi-Region key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.update_primary_region)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#update_primary_region)
        """
    def verify(
        self,
        *,
        KeyId: str,
        Message: Union[bytes, IO[bytes], StreamingBody],
        Signature: Union[bytes, IO[bytes], StreamingBody],
        SigningAlgorithm: SigningAlgorithmSpecType,
        MessageType: MessageTypeType = None,
        GrantTokens: List[str] = None
    ) -> VerifyResponseTypeDef:
        """
        Verifies a digital signature that was generated by the  Sign operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.verify)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#verify)
        """
    def verify_mac(
        self,
        *,
        Message: Union[bytes, IO[bytes], StreamingBody],
        KeyId: str,
        MacAlgorithm: MacAlgorithmSpecType,
        Mac: Union[bytes, IO[bytes], StreamingBody],
        GrantTokens: List[str] = None
    ) -> VerifyMacResponseTypeDef:
        """
        Verifies the hash-based message authentication code (HMAC) for a specified
        message, HMAC KMS key, and MAC algorithm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Client.verify_mac)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/client.html#verify_mac)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_custom_key_stores"]
    ) -> DescribeCustomKeyStoresPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Paginator.DescribeCustomKeyStores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#describecustomkeystorespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_aliases"]) -> ListAliasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Paginator.ListAliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listaliasespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_grants"]) -> ListGrantsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Paginator.ListGrants)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listgrantspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_key_policies"]
    ) -> ListKeyPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Paginator.ListKeyPolicies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listkeypoliciespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_keys"]) -> ListKeysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Paginator.ListKeys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listkeyspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_tags"]
    ) -> ListResourceTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Paginator.ListResourceTags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listresourcetagspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_retirable_grants"]
    ) -> ListRetirableGrantsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kms.html#KMS.Paginator.ListRetirableGrants)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listretirablegrantspaginator)
        """
