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

from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import ParticipantStateType, ParticipantTokenCapabilityType
from .type_defs import (
    CreateEncoderConfigurationResponseTypeDef,
    CreateParticipantTokenResponseTypeDef,
    CreateStageResponseTypeDef,
    CreateStorageConfigurationResponseTypeDef,
    DestinationConfigurationTypeDef,
    GetCompositionResponseTypeDef,
    GetEncoderConfigurationResponseTypeDef,
    GetParticipantResponseTypeDef,
    GetStageResponseTypeDef,
    GetStageSessionResponseTypeDef,
    GetStorageConfigurationResponseTypeDef,
    LayoutConfigurationTypeDef,
    ListCompositionsResponseTypeDef,
    ListEncoderConfigurationsResponseTypeDef,
    ListParticipantEventsResponseTypeDef,
    ListParticipantsResponseTypeDef,
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#close)
        """

    def create_encoder_configuration(
        self, *, name: str = None, tags: Dict[str, str] = None, video: "VideoTypeDef" = None
    ) -> CreateEncoderConfigurationResponseTypeDef:
        """
        Creates an EncoderConfiguration object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.create_encoder_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#create_encoder_configuration)
        """

    def create_participant_token(
        self,
        *,
        stageArn: str,
        attributes: Dict[str, str] = None,
        capabilities: List[ParticipantTokenCapabilityType] = None,
        duration: int = None,
        userId: str = None
    ) -> CreateParticipantTokenResponseTypeDef:
        """
        Creates an additional token for a specified stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.create_participant_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#create_participant_token)
        """

    def create_stage(
        self,
        *,
        name: str = None,
        participantTokenConfigurations: List["ParticipantTokenConfigurationTypeDef"] = None,
        tags: Dict[str, str] = None
    ) -> CreateStageResponseTypeDef:
        """
        Creates a new stage (and optionally participant tokens).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.create_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#create_stage)
        """

    def create_storage_configuration(
        self, *, s3: "S3StorageConfigurationTypeDef", name: str = None, tags: Dict[str, str] = None
    ) -> CreateStorageConfigurationResponseTypeDef:
        """
        Creates a new storage configuration, used to enable recording to Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.create_storage_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#create_storage_configuration)
        """

    def delete_encoder_configuration(self, *, arn: str) -> Dict[str, Any]:
        """
        Deletes an EncoderConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.delete_encoder_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#delete_encoder_configuration)
        """

    def delete_stage(self, *, arn: str) -> Dict[str, Any]:
        """
        Shuts down and deletes the specified stage (disconnecting all participants).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.delete_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#delete_stage)
        """

    def delete_storage_configuration(self, *, arn: str) -> Dict[str, Any]:
        """
        Deletes the storage configuration for the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.delete_storage_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#delete_storage_configuration)
        """

    def disconnect_participant(
        self, *, participantId: str, stageArn: str, reason: str = None
    ) -> Dict[str, Any]:
        """
        Disconnects a specified participant and revokes the participant permanently from
        a specified stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.disconnect_participant)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#generate_presigned_url)
        """

    def get_composition(self, *, arn: str) -> GetCompositionResponseTypeDef:
        """
        Get information about the specified Composition resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.get_composition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#get_composition)
        """

    def get_encoder_configuration(self, *, arn: str) -> GetEncoderConfigurationResponseTypeDef:
        """
        Gets information about the specified EncoderConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.get_encoder_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#get_encoder_configuration)
        """

    def get_participant(
        self, *, participantId: str, sessionId: str, stageArn: str
    ) -> GetParticipantResponseTypeDef:
        """
        Gets information about the specified participant token.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.get_participant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#get_participant)
        """

    def get_stage(self, *, arn: str) -> GetStageResponseTypeDef:
        """
        Gets information for the specified stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.get_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#get_stage)
        """

    def get_stage_session(self, *, sessionId: str, stageArn: str) -> GetStageSessionResponseTypeDef:
        """
        Gets information for the specified stage session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.get_stage_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#get_stage_session)
        """

    def get_storage_configuration(self, *, arn: str) -> GetStorageConfigurationResponseTypeDef:
        """
        Gets the storage configuration for the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.get_storage_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#get_storage_configuration)
        """

    def list_compositions(
        self,
        *,
        filterByEncoderConfigurationArn: str = None,
        filterByStageArn: str = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListCompositionsResponseTypeDef:
        """
        Gets summary information about all Compositions in your account, in the AWS
        region where the API request is processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.list_compositions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#list_compositions)
        """

    def list_encoder_configurations(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListEncoderConfigurationsResponseTypeDef:
        """
        Gets summary information about all EncoderConfigurations in your account, in the
        AWS region where the API request is processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.list_encoder_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#list_encoder_configurations)
        """

    def list_participant_events(
        self,
        *,
        participantId: str,
        sessionId: str,
        stageArn: str,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListParticipantEventsResponseTypeDef:
        """
        Lists events for a specified participant that occurred during a specified stage
        session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.list_participant_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#list_participant_events)
        """

    def list_participants(
        self,
        *,
        sessionId: str,
        stageArn: str,
        filterByPublished: bool = None,
        filterByState: ParticipantStateType = None,
        filterByUserId: str = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListParticipantsResponseTypeDef:
        """
        Lists all participants in a specified stage session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.list_participants)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#list_participants)
        """

    def list_stage_sessions(
        self, *, stageArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListStageSessionsResponseTypeDef:
        """
        Gets all sessions for a specified stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.list_stage_sessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#list_stage_sessions)
        """

    def list_stages(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListStagesResponseTypeDef:
        """
        Gets summary information about all stages in your account, in the AWS region
        where the API request is processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.list_stages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#list_stages)
        """

    def list_storage_configurations(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListStorageConfigurationsResponseTypeDef:
        """
        Gets summary information about all storage configurations in your account, in
        the AWS region where the API request is processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.list_storage_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#list_storage_configurations)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Gets information about AWS tags for the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#list_tags_for_resource)
        """

    def start_composition(
        self,
        *,
        destinations: List["DestinationConfigurationTypeDef"],
        stageArn: str,
        idempotencyToken: str = None,
        layout: "LayoutConfigurationTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> StartCompositionResponseTypeDef:
        """
        Starts a Composition from a stage based on the configuration provided in the
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.start_composition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#start_composition)
        """

    def stop_composition(self, *, arn: str) -> Dict[str, Any]:
        """
        Stops and deletes a Composition resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.stop_composition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#stop_composition)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds or updates tags for the AWS resource with the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from the resource with the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#untag_resource)
        """

    def update_stage(self, *, arn: str, name: str = None) -> UpdateStageResponseTypeDef:
        """
        Updates a stage’s configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ivs-realtime.html#ivsrealtime.Client.update_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/client.html#update_stage)
        """
