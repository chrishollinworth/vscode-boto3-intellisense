"""
Type annotations for ivs-realtime service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_ivs_realtime import ivsrealtimeClient

    client: ivsrealtimeClient = boto3.client("ivs-realtime")
    ```
"""

import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ParticipantRecordingFilterByRecordingStateType,
    ParticipantStateType,
    ParticipantTokenCapabilityType,
)
from .paginator import ListPublicKeysPaginator
from .type_defs import (
    AutoParticipantRecordingConfigurationTypeDef,
    CreateEncoderConfigurationResponseTypeDef,
    CreateParticipantTokenResponseTypeDef,
    CreateStageResponseTypeDef,
    CreateStorageConfigurationResponseTypeDef,
    DestinationConfigurationTypeDef,
    GetCompositionResponseTypeDef,
    GetEncoderConfigurationResponseTypeDef,
    GetParticipantResponseTypeDef,
    GetPublicKeyResponseTypeDef,
    GetStageResponseTypeDef,
    GetStageSessionResponseTypeDef,
    GetStorageConfigurationResponseTypeDef,
    ImportPublicKeyResponseTypeDef,
    LayoutConfigurationTypeDef,
    ListCompositionsResponseTypeDef,
    ListEncoderConfigurationsResponseTypeDef,
    ListParticipantEventsResponseTypeDef,
    ListParticipantsResponseTypeDef,
    ListPublicKeysResponseTypeDef,
    ListStageSessionsResponseTypeDef,
    ListStagesResponseTypeDef,
    ListStorageConfigurationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ParticipantTokenConfigurationTypeDef,
    S3StorageConfigurationTypeDef,
    StartCompositionResponseTypeDef,
    UpdateStageResponseTypeDef,
    VideoTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ivsrealtimeClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    PendingVerification: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ivsrealtimeClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ivsrealtimeClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#close)
        """

    def create_encoder_configuration(
        self, *, name: str = None, video: "VideoTypeDef" = None, tags: Dict[str, str] = None
    ) -> CreateEncoderConfigurationResponseTypeDef:
        """
        Creates an EncoderConfiguration object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.create_encoder_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#create_encoder_configuration)
        """

    def create_participant_token(
        self,
        *,
        stageArn: str,
        duration: int = None,
        userId: str = None,
        attributes: Dict[str, str] = None,
        capabilities: List[ParticipantTokenCapabilityType] = None
    ) -> CreateParticipantTokenResponseTypeDef:
        """
        Creates an additional token for a specified stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.create_participant_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#create_participant_token)
        """

    def create_stage(
        self,
        *,
        name: str = None,
        participantTokenConfigurations: List["ParticipantTokenConfigurationTypeDef"] = None,
        tags: Dict[str, str] = None,
        autoParticipantRecordingConfiguration: "AutoParticipantRecordingConfigurationTypeDef" = None
    ) -> CreateStageResponseTypeDef:
        """
        Creates a new stage (and optionally participant tokens).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.create_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#create_stage)
        """

    def create_storage_configuration(
        self, *, s3: "S3StorageConfigurationTypeDef", name: str = None, tags: Dict[str, str] = None
    ) -> CreateStorageConfigurationResponseTypeDef:
        """
        Creates a new storage configuration, used to enable recording to Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.create_storage_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#create_storage_configuration)
        """

    def delete_encoder_configuration(self, *, arn: str) -> Dict[str, Any]:
        """
        Deletes an EncoderConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.delete_encoder_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#delete_encoder_configuration)
        """

    def delete_public_key(self, *, arn: str) -> Dict[str, Any]:
        """
        Deletes the specified public key used to sign stage participant tokens.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.delete_public_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#delete_public_key)
        """

    def delete_stage(self, *, arn: str) -> Dict[str, Any]:
        """
        Shuts down and deletes the specified stage (disconnecting all participants).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.delete_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#delete_stage)
        """

    def delete_storage_configuration(self, *, arn: str) -> Dict[str, Any]:
        """
        Deletes the storage configuration for the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.delete_storage_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#delete_storage_configuration)
        """

    def disconnect_participant(
        self, *, stageArn: str, participantId: str, reason: str = None
    ) -> Dict[str, Any]:
        """
        Disconnects a specified participant and revokes the participant permanently from
        a specified stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.disconnect_participant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#disconnect_participant)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#generate_presigned_url)
        """

    def get_composition(self, *, arn: str) -> GetCompositionResponseTypeDef:
        """
        Get information about the specified Composition resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.get_composition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#get_composition)
        """

    def get_encoder_configuration(self, *, arn: str) -> GetEncoderConfigurationResponseTypeDef:
        """
        Gets information about the specified EncoderConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.get_encoder_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#get_encoder_configuration)
        """

    def get_participant(
        self, *, stageArn: str, sessionId: str, participantId: str
    ) -> GetParticipantResponseTypeDef:
        """
        Gets information about the specified participant token.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.get_participant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#get_participant)
        """

    def get_public_key(self, *, arn: str) -> GetPublicKeyResponseTypeDef:
        """
        Gets information for the specified public key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.get_public_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#get_public_key)
        """

    def get_stage(self, *, arn: str) -> GetStageResponseTypeDef:
        """
        Gets information for the specified stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.get_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#get_stage)
        """

    def get_stage_session(self, *, stageArn: str, sessionId: str) -> GetStageSessionResponseTypeDef:
        """
        Gets information for the specified stage session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.get_stage_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#get_stage_session)
        """

    def get_storage_configuration(self, *, arn: str) -> GetStorageConfigurationResponseTypeDef:
        """
        Gets the storage configuration for the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.get_storage_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#get_storage_configuration)
        """

    def import_public_key(
        self, *, publicKeyMaterial: str, name: str = None, tags: Dict[str, str] = None
    ) -> ImportPublicKeyResponseTypeDef:
        """
        Import a public key to be used for signing stage participant tokens.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.import_public_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#import_public_key)
        """

    def list_compositions(
        self,
        *,
        filterByStageArn: str = None,
        filterByEncoderConfigurationArn: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListCompositionsResponseTypeDef:
        """
        Gets summary information about all Compositions in your account, in the AWS
        region where the API request is processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.list_compositions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#list_compositions)
        """

    def list_encoder_configurations(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListEncoderConfigurationsResponseTypeDef:
        """
        Gets summary information about all EncoderConfigurations in your account, in the
        AWS region where the API request is processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.list_encoder_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#list_encoder_configurations)
        """

    def list_participant_events(
        self,
        *,
        stageArn: str,
        sessionId: str,
        participantId: str,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListParticipantEventsResponseTypeDef:
        """
        Lists events for a specified participant that occurred during a specified stage
        session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.list_participant_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#list_participant_events)
        """

    def list_participants(
        self,
        *,
        stageArn: str,
        sessionId: str,
        filterByUserId: str = None,
        filterByPublished: bool = None,
        filterByState: ParticipantStateType = None,
        nextToken: str = None,
        maxResults: int = None,
        filterByRecordingState: ParticipantRecordingFilterByRecordingStateType = None
    ) -> ListParticipantsResponseTypeDef:
        """
        Lists all participants in a specified stage session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.list_participants)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#list_participants)
        """

    def list_public_keys(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListPublicKeysResponseTypeDef:
        """
        Gets summary information about all public keys in your account, in the AWS
        region where the API request is processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.list_public_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#list_public_keys)
        """

    def list_stage_sessions(
        self, *, stageArn: str, nextToken: str = None, maxResults: int = None
    ) -> ListStageSessionsResponseTypeDef:
        """
        Gets all sessions for a specified stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.list_stage_sessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#list_stage_sessions)
        """

    def list_stages(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListStagesResponseTypeDef:
        """
        Gets summary information about all stages in your account, in the AWS region
        where the API request is processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.list_stages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#list_stages)
        """

    def list_storage_configurations(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListStorageConfigurationsResponseTypeDef:
        """
        Gets summary information about all storage configurations in your account, in
        the AWS region where the API request is processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.list_storage_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#list_storage_configurations)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Gets information about AWS tags for the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#list_tags_for_resource)
        """

    def start_composition(
        self,
        *,
        stageArn: str,
        destinations: List["DestinationConfigurationTypeDef"],
        idempotencyToken: str = None,
        layout: "LayoutConfigurationTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> StartCompositionResponseTypeDef:
        """
        Starts a Composition from a stage based on the configuration provided in the
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.start_composition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#start_composition)
        """

    def stop_composition(self, *, arn: str) -> Dict[str, Any]:
        """
        Stops and deletes a Composition resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.stop_composition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#stop_composition)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds or updates tags for the AWS resource with the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from the resource with the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#untag_resource)
        """

    def update_stage(
        self,
        *,
        arn: str,
        name: str = None,
        autoParticipantRecordingConfiguration: "AutoParticipantRecordingConfigurationTypeDef" = None
    ) -> UpdateStageResponseTypeDef:
        """
        Updates a stage’s configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Client.update_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#update_stage)
        """

    def get_paginator(self, operation_name: Literal["list_public_keys"]) -> ListPublicKeysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Paginator.ListPublicKeys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/paginators.html#listpublickeyspaginator)
        """
