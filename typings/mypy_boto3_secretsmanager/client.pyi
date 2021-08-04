"""
Type annotations for secretsmanager service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_secretsmanager import SecretsManagerClient

    client: SecretsManagerClient = boto3.client("secretsmanager")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import SortOrderTypeType
from .paginator import ListSecretsPaginator
from .type_defs import (
    CancelRotateSecretResponseTypeDef,
    CreateSecretResponseTypeDef,
    DeleteResourcePolicyResponseTypeDef,
    DeleteSecretResponseTypeDef,
    DescribeSecretResponseTypeDef,
    FilterTypeDef,
    GetRandomPasswordResponseTypeDef,
    GetResourcePolicyResponseTypeDef,
    GetSecretValueResponseTypeDef,
    ListSecretsResponseTypeDef,
    ListSecretVersionIdsResponseTypeDef,
    PutResourcePolicyResponseTypeDef,
    PutSecretValueResponseTypeDef,
    RemoveRegionsFromReplicationResponseTypeDef,
    ReplicaRegionTypeTypeDef,
    ReplicateSecretToRegionsResponseTypeDef,
    RestoreSecretResponseTypeDef,
    RotateSecretResponseTypeDef,
    RotationRulesTypeTypeDef,
    StopReplicationToReplicaResponseTypeDef,
    TagTypeDef,
    UpdateSecretResponseTypeDef,
    UpdateSecretVersionStageResponseTypeDef,
    ValidateResourcePolicyResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("SecretsManagerClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    DecryptionFailure: Type[BotocoreClientError]
    EncryptionFailure: Type[BotocoreClientError]
    InternalServiceError: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MalformedPolicyDocumentException: Type[BotocoreClientError]
    PreconditionNotMetException: Type[BotocoreClientError]
    PublicPolicyException: Type[BotocoreClientError]
    ResourceExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class SecretsManagerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        SecretsManagerClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#can_paginate)
        """
    def cancel_rotate_secret(self, *, SecretId: str) -> CancelRotateSecretResponseTypeDef:
        """
        Disables automatic scheduled rotation and cancels the rotation of a secret if
        currently in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client.cancel_rotate_secret)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#cancel_rotate_secret)
        """
    def create_secret(
        self,
        *,
        Name: str,
        ClientRequestToken: str = None,
        Description: str = None,
        KmsKeyId: str = None,
        SecretBinary: Union[bytes, IO[bytes], StreamingBody] = None,
        SecretString: str = None,
        Tags: List["TagTypeDef"] = None,
        AddReplicaRegions: List["ReplicaRegionTypeTypeDef"] = None,
        ForceOverwriteReplicaSecret: bool = None
    ) -> CreateSecretResponseTypeDef:
        """
        Creates a new secret.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client.create_secret)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#create_secret)
        """
    def delete_resource_policy(self, *, SecretId: str) -> DeleteResourcePolicyResponseTypeDef:
        """
        Deletes the resource-based permission policy attached to the secret.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#delete_resource_policy)
        """
    def delete_secret(
        self,
        *,
        SecretId: str,
        RecoveryWindowInDays: int = None,
        ForceDeleteWithoutRecovery: bool = None
    ) -> DeleteSecretResponseTypeDef:
        """
        Deletes an entire secret and all of the versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client.delete_secret)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#delete_secret)
        """
    def describe_secret(self, *, SecretId: str) -> DescribeSecretResponseTypeDef:
        """
        Retrieves the details of a secret.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client.describe_secret)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#describe_secret)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#generate_presigned_url)
        """
    def get_random_password(
        self,
        *,
        PasswordLength: int = None,
        ExcludeCharacters: str = None,
        ExcludeNumbers: bool = None,
        ExcludePunctuation: bool = None,
        ExcludeUppercase: bool = None,
        ExcludeLowercase: bool = None,
        IncludeSpace: bool = None,
        RequireEachIncludedType: bool = None
    ) -> GetRandomPasswordResponseTypeDef:
        """
        Generates a random password of the specified complexity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client.get_random_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#get_random_password)
        """
    def get_resource_policy(self, *, SecretId: str) -> GetResourcePolicyResponseTypeDef:
        """
        Retrieves the JSON text of the resource-based policy document attached to the
        specified secret.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client.get_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#get_resource_policy)
        """
    def get_secret_value(
        self, *, SecretId: str, VersionId: str = None, VersionStage: str = None
    ) -> GetSecretValueResponseTypeDef:
        """
        Retrieves the contents of the encrypted fields `SecretString` or `SecretBinary`
        from the specified version of a secret, whichever contains content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client.get_secret_value)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#get_secret_value)
        """
    def list_secret_version_ids(
        self,
        *,
        SecretId: str,
        MaxResults: int = None,
        NextToken: str = None,
        IncludeDeprecated: bool = None
    ) -> ListSecretVersionIdsResponseTypeDef:
        """
        Lists all of the versions attached to the specified secret.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client.list_secret_version_ids)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#list_secret_version_ids)
        """
    def list_secrets(
        self,
        *,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List["FilterTypeDef"] = None,
        SortOrder: SortOrderTypeType = None
    ) -> ListSecretsResponseTypeDef:
        """
        Lists all of the secrets that are stored by Secrets Manager in the Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client.list_secrets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#list_secrets)
        """
    def put_resource_policy(
        self, *, SecretId: str, ResourcePolicy: str, BlockPublicPolicy: bool = None
    ) -> PutResourcePolicyResponseTypeDef:
        """
        Attaches the contents of the specified resource-based permission policy to a
        secret.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client.put_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#put_resource_policy)
        """
    def put_secret_value(
        self,
        *,
        SecretId: str,
        ClientRequestToken: str = None,
        SecretBinary: Union[bytes, IO[bytes], StreamingBody] = None,
        SecretString: str = None,
        VersionStages: List[str] = None
    ) -> PutSecretValueResponseTypeDef:
        """
        Stores a new encrypted secret value in the specified secret.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client.put_secret_value)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#put_secret_value)
        """
    def remove_regions_from_replication(
        self, *, SecretId: str, RemoveReplicaRegions: List[str]
    ) -> RemoveRegionsFromReplicationResponseTypeDef:
        """
        Remove regions from replication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client.remove_regions_from_replication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#remove_regions_from_replication)
        """
    def replicate_secret_to_regions(
        self,
        *,
        SecretId: str,
        AddReplicaRegions: List["ReplicaRegionTypeTypeDef"],
        ForceOverwriteReplicaSecret: bool = None
    ) -> ReplicateSecretToRegionsResponseTypeDef:
        """
        Converts an existing secret to a multi-Region secret and begins replication the
        secret to a list of new regions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client.replicate_secret_to_regions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#replicate_secret_to_regions)
        """
    def restore_secret(self, *, SecretId: str) -> RestoreSecretResponseTypeDef:
        """
        Cancels the scheduled deletion of a secret by removing the `DeletedDate` time
        stamp.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client.restore_secret)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#restore_secret)
        """
    def rotate_secret(
        self,
        *,
        SecretId: str,
        ClientRequestToken: str = None,
        RotationLambdaARN: str = None,
        RotationRules: "RotationRulesTypeTypeDef" = None
    ) -> RotateSecretResponseTypeDef:
        """
        Configures and starts the asynchronous process of rotating this secret.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client.rotate_secret)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#rotate_secret)
        """
    def stop_replication_to_replica(
        self, *, SecretId: str
    ) -> StopReplicationToReplicaResponseTypeDef:
        """
        Removes the secret from replication and promotes the secret to a regional secret
        in the replica Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client.stop_replication_to_replica)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#stop_replication_to_replica)
        """
    def tag_resource(self, *, SecretId: str, Tags: List["TagTypeDef"]) -> None:
        """
        Attaches one or more tags, each consisting of a key name and a value, to the
        specified secret.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#tag_resource)
        """
    def untag_resource(self, *, SecretId: str, TagKeys: List[str]) -> None:
        """
        Removes one or more tags from the specified secret.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#untag_resource)
        """
    def update_secret(
        self,
        *,
        SecretId: str,
        ClientRequestToken: str = None,
        Description: str = None,
        KmsKeyId: str = None,
        SecretBinary: Union[bytes, IO[bytes], StreamingBody] = None,
        SecretString: str = None
    ) -> UpdateSecretResponseTypeDef:
        """
        Modifies many of the details of the specified secret.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client.update_secret)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#update_secret)
        """
    def update_secret_version_stage(
        self,
        *,
        SecretId: str,
        VersionStage: str,
        RemoveFromVersionId: str = None,
        MoveToVersionId: str = None
    ) -> UpdateSecretVersionStageResponseTypeDef:
        """
        Modifies the staging labels attached to a version of a secret.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client.update_secret_version_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#update_secret_version_stage)
        """
    def validate_resource_policy(
        self, *, ResourcePolicy: str, SecretId: str = None
    ) -> ValidateResourcePolicyResponseTypeDef:
        """
        Validates that the resource policy does not grant a wide range of IAM principals
        access to your secret.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Client.validate_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#validate_resource_policy)
        """
    def get_paginator(self, operation_name: Literal["list_secrets"]) -> ListSecretsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/secretsmanager.html#SecretsManager.Paginator.ListSecrets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/paginators.html#listsecretspaginator)
        """
