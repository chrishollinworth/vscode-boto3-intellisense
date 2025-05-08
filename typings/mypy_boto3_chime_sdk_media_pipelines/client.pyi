"""
Type annotations for chime-sdk-media-pipelines service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_chime_sdk_media_pipelines.client import ChimeSDKMediaPipelinesClient

    session = Session()
    client: ChimeSDKMediaPipelinesClient = session.client("chime-sdk-media-pipelines")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    CreateMediaCapturePipelineRequestTypeDef,
    CreateMediaCapturePipelineResponseTypeDef,
    CreateMediaConcatenationPipelineRequestTypeDef,
    CreateMediaConcatenationPipelineResponseTypeDef,
    CreateMediaInsightsPipelineConfigurationRequestTypeDef,
    CreateMediaInsightsPipelineConfigurationResponseTypeDef,
    CreateMediaInsightsPipelineRequestTypeDef,
    CreateMediaInsightsPipelineResponseTypeDef,
    CreateMediaLiveConnectorPipelineRequestTypeDef,
    CreateMediaLiveConnectorPipelineResponseTypeDef,
    CreateMediaPipelineKinesisVideoStreamPoolRequestTypeDef,
    CreateMediaPipelineKinesisVideoStreamPoolResponseTypeDef,
    CreateMediaStreamPipelineRequestTypeDef,
    CreateMediaStreamPipelineResponseTypeDef,
    DeleteMediaCapturePipelineRequestTypeDef,
    DeleteMediaInsightsPipelineConfigurationRequestTypeDef,
    DeleteMediaPipelineKinesisVideoStreamPoolRequestTypeDef,
    DeleteMediaPipelineRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetMediaCapturePipelineRequestTypeDef,
    GetMediaCapturePipelineResponseTypeDef,
    GetMediaInsightsPipelineConfigurationRequestTypeDef,
    GetMediaInsightsPipelineConfigurationResponseTypeDef,
    GetMediaPipelineKinesisVideoStreamPoolRequestTypeDef,
    GetMediaPipelineKinesisVideoStreamPoolResponseTypeDef,
    GetMediaPipelineRequestTypeDef,
    GetMediaPipelineResponseTypeDef,
    GetSpeakerSearchTaskRequestTypeDef,
    GetSpeakerSearchTaskResponseTypeDef,
    GetVoiceToneAnalysisTaskRequestTypeDef,
    GetVoiceToneAnalysisTaskResponseTypeDef,
    ListMediaCapturePipelinesRequestTypeDef,
    ListMediaCapturePipelinesResponseTypeDef,
    ListMediaInsightsPipelineConfigurationsRequestTypeDef,
    ListMediaInsightsPipelineConfigurationsResponseTypeDef,
    ListMediaPipelineKinesisVideoStreamPoolsRequestTypeDef,
    ListMediaPipelineKinesisVideoStreamPoolsResponseTypeDef,
    ListMediaPipelinesRequestTypeDef,
    ListMediaPipelinesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    StartSpeakerSearchTaskRequestTypeDef,
    StartSpeakerSearchTaskResponseTypeDef,
    StartVoiceToneAnalysisTaskRequestTypeDef,
    StartVoiceToneAnalysisTaskResponseTypeDef,
    StopSpeakerSearchTaskRequestTypeDef,
    StopVoiceToneAnalysisTaskRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateMediaInsightsPipelineConfigurationRequestTypeDef,
    UpdateMediaInsightsPipelineConfigurationResponseTypeDef,
    UpdateMediaInsightsPipelineStatusRequestTypeDef,
    UpdateMediaPipelineKinesisVideoStreamPoolRequestTypeDef,
    UpdateMediaPipelineKinesisVideoStreamPoolResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ChimeSDKMediaPipelinesClient",)

class Exceptions(BaseClientExceptions):
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ServiceFailureException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottledClientException: Type[BotocoreClientError]
    UnauthorizedClientException: Type[BotocoreClientError]

class ChimeSDKMediaPipelinesClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ChimeSDKMediaPipelinesClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html#ChimeSDKMediaPipelines.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#generate_presigned_url)
        """

    def create_media_capture_pipeline(
        self, **kwargs: Unpack[CreateMediaCapturePipelineRequestTypeDef]
    ) -> CreateMediaCapturePipelineResponseTypeDef:
        """
        Creates a media pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/create_media_capture_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#create_media_capture_pipeline)
        """

    def create_media_concatenation_pipeline(
        self, **kwargs: Unpack[CreateMediaConcatenationPipelineRequestTypeDef]
    ) -> CreateMediaConcatenationPipelineResponseTypeDef:
        """
        Creates a media concatenation pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/create_media_concatenation_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#create_media_concatenation_pipeline)
        """

    def create_media_insights_pipeline(
        self, **kwargs: Unpack[CreateMediaInsightsPipelineRequestTypeDef]
    ) -> CreateMediaInsightsPipelineResponseTypeDef:
        """
        Creates a media insights pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/create_media_insights_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#create_media_insights_pipeline)
        """

    def create_media_insights_pipeline_configuration(
        self, **kwargs: Unpack[CreateMediaInsightsPipelineConfigurationRequestTypeDef]
    ) -> CreateMediaInsightsPipelineConfigurationResponseTypeDef:
        """
        A structure that contains the static configurations for a media insights
        pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/create_media_insights_pipeline_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#create_media_insights_pipeline_configuration)
        """

    def create_media_live_connector_pipeline(
        self, **kwargs: Unpack[CreateMediaLiveConnectorPipelineRequestTypeDef]
    ) -> CreateMediaLiveConnectorPipelineResponseTypeDef:
        """
        Creates a media live connector pipeline in an Amazon Chime SDK meeting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/create_media_live_connector_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#create_media_live_connector_pipeline)
        """

    def create_media_pipeline_kinesis_video_stream_pool(
        self, **kwargs: Unpack[CreateMediaPipelineKinesisVideoStreamPoolRequestTypeDef]
    ) -> CreateMediaPipelineKinesisVideoStreamPoolResponseTypeDef:
        """
        Creates an Amazon Kinesis Video Stream pool for use with media stream pipelines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/create_media_pipeline_kinesis_video_stream_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#create_media_pipeline_kinesis_video_stream_pool)
        """

    def create_media_stream_pipeline(
        self, **kwargs: Unpack[CreateMediaStreamPipelineRequestTypeDef]
    ) -> CreateMediaStreamPipelineResponseTypeDef:
        """
        Creates a streaming media pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/create_media_stream_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#create_media_stream_pipeline)
        """

    def delete_media_capture_pipeline(
        self, **kwargs: Unpack[DeleteMediaCapturePipelineRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the media pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/delete_media_capture_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#delete_media_capture_pipeline)
        """

    def delete_media_insights_pipeline_configuration(
        self, **kwargs: Unpack[DeleteMediaInsightsPipelineConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified configuration settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/delete_media_insights_pipeline_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#delete_media_insights_pipeline_configuration)
        """

    def delete_media_pipeline(
        self, **kwargs: Unpack[DeleteMediaPipelineRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the media pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/delete_media_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#delete_media_pipeline)
        """

    def delete_media_pipeline_kinesis_video_stream_pool(
        self, **kwargs: Unpack[DeleteMediaPipelineKinesisVideoStreamPoolRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Amazon Kinesis Video Stream pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/delete_media_pipeline_kinesis_video_stream_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#delete_media_pipeline_kinesis_video_stream_pool)
        """

    def get_media_capture_pipeline(
        self, **kwargs: Unpack[GetMediaCapturePipelineRequestTypeDef]
    ) -> GetMediaCapturePipelineResponseTypeDef:
        """
        Gets an existing media pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/get_media_capture_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#get_media_capture_pipeline)
        """

    def get_media_insights_pipeline_configuration(
        self, **kwargs: Unpack[GetMediaInsightsPipelineConfigurationRequestTypeDef]
    ) -> GetMediaInsightsPipelineConfigurationResponseTypeDef:
        """
        Gets the configuration settings for a media insights pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/get_media_insights_pipeline_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#get_media_insights_pipeline_configuration)
        """

    def get_media_pipeline(
        self, **kwargs: Unpack[GetMediaPipelineRequestTypeDef]
    ) -> GetMediaPipelineResponseTypeDef:
        """
        Gets an existing media pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/get_media_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#get_media_pipeline)
        """

    def get_media_pipeline_kinesis_video_stream_pool(
        self, **kwargs: Unpack[GetMediaPipelineKinesisVideoStreamPoolRequestTypeDef]
    ) -> GetMediaPipelineKinesisVideoStreamPoolResponseTypeDef:
        """
        Gets an Kinesis video stream pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/get_media_pipeline_kinesis_video_stream_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#get_media_pipeline_kinesis_video_stream_pool)
        """

    def get_speaker_search_task(
        self, **kwargs: Unpack[GetSpeakerSearchTaskRequestTypeDef]
    ) -> GetSpeakerSearchTaskResponseTypeDef:
        """
        Retrieves the details of the specified speaker search task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/get_speaker_search_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#get_speaker_search_task)
        """

    def get_voice_tone_analysis_task(
        self, **kwargs: Unpack[GetVoiceToneAnalysisTaskRequestTypeDef]
    ) -> GetVoiceToneAnalysisTaskResponseTypeDef:
        """
        Retrieves the details of a voice tone analysis task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/get_voice_tone_analysis_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#get_voice_tone_analysis_task)
        """

    def list_media_capture_pipelines(
        self, **kwargs: Unpack[ListMediaCapturePipelinesRequestTypeDef]
    ) -> ListMediaCapturePipelinesResponseTypeDef:
        """
        Returns a list of media pipelines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/list_media_capture_pipelines.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#list_media_capture_pipelines)
        """

    def list_media_insights_pipeline_configurations(
        self, **kwargs: Unpack[ListMediaInsightsPipelineConfigurationsRequestTypeDef]
    ) -> ListMediaInsightsPipelineConfigurationsResponseTypeDef:
        """
        Lists the available media insights pipeline configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/list_media_insights_pipeline_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#list_media_insights_pipeline_configurations)
        """

    def list_media_pipeline_kinesis_video_stream_pools(
        self, **kwargs: Unpack[ListMediaPipelineKinesisVideoStreamPoolsRequestTypeDef]
    ) -> ListMediaPipelineKinesisVideoStreamPoolsResponseTypeDef:
        """
        Lists the video stream pools in the media pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/list_media_pipeline_kinesis_video_stream_pools.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#list_media_pipeline_kinesis_video_stream_pools)
        """

    def list_media_pipelines(
        self, **kwargs: Unpack[ListMediaPipelinesRequestTypeDef]
    ) -> ListMediaPipelinesResponseTypeDef:
        """
        Returns a list of media pipelines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/list_media_pipelines.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#list_media_pipelines)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags available for a media pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#list_tags_for_resource)
        """

    def start_speaker_search_task(
        self, **kwargs: Unpack[StartSpeakerSearchTaskRequestTypeDef]
    ) -> StartSpeakerSearchTaskResponseTypeDef:
        """
        Starts a speaker search task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/start_speaker_search_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#start_speaker_search_task)
        """

    def start_voice_tone_analysis_task(
        self, **kwargs: Unpack[StartVoiceToneAnalysisTaskRequestTypeDef]
    ) -> StartVoiceToneAnalysisTaskResponseTypeDef:
        """
        Starts a voice tone analysis task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/start_voice_tone_analysis_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#start_voice_tone_analysis_task)
        """

    def stop_speaker_search_task(
        self, **kwargs: Unpack[StopSpeakerSearchTaskRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops a speaker search task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/stop_speaker_search_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#stop_speaker_search_task)
        """

    def stop_voice_tone_analysis_task(
        self, **kwargs: Unpack[StopVoiceToneAnalysisTaskRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops a voice tone analysis task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/stop_voice_tone_analysis_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#stop_voice_tone_analysis_task)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        The ARN of the media pipeline that you want to tag.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes any tags from a media pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#untag_resource)
        """

    def update_media_insights_pipeline_configuration(
        self, **kwargs: Unpack[UpdateMediaInsightsPipelineConfigurationRequestTypeDef]
    ) -> UpdateMediaInsightsPipelineConfigurationResponseTypeDef:
        """
        Updates the media insights pipeline's configuration settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/update_media_insights_pipeline_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#update_media_insights_pipeline_configuration)
        """

    def update_media_insights_pipeline_status(
        self, **kwargs: Unpack[UpdateMediaInsightsPipelineStatusRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the status of a media insights pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/update_media_insights_pipeline_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#update_media_insights_pipeline_status)
        """

    def update_media_pipeline_kinesis_video_stream_pool(
        self, **kwargs: Unpack[UpdateMediaPipelineKinesisVideoStreamPoolRequestTypeDef]
    ) -> UpdateMediaPipelineKinesisVideoStreamPoolResponseTypeDef:
        """
        Updates an Amazon Kinesis Video Stream pool in a media pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines/client/update_media_pipeline_kinesis_video_stream_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/client/#update_media_pipeline_kinesis_video_stream_pool)
        """
