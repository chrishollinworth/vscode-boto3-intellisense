"""
Type annotations for elastictranscoder service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_elastictranscoder import ElasticTranscoderClient

    client: ElasticTranscoderClient = boto3.client("elastictranscoder")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListJobsByPipelinePaginator,
    ListJobsByStatusPaginator,
    ListPipelinesPaginator,
    ListPresetsPaginator,
)
from .type_defs import (
    AudioParametersTypeDef,
    CreateJobOutputTypeDef,
    CreateJobPlaylistTypeDef,
    CreateJobResponseTypeDef,
    CreatePipelineResponseTypeDef,
    CreatePresetResponseTypeDef,
    JobInputTypeDef,
    ListJobsByPipelineResponseTypeDef,
    ListJobsByStatusResponseTypeDef,
    ListPipelinesResponseTypeDef,
    ListPresetsResponseTypeDef,
    NotificationsTypeDef,
    PipelineOutputConfigTypeDef,
    ReadJobResponseTypeDef,
    ReadPipelineResponseTypeDef,
    ReadPresetResponseTypeDef,
    TestRoleResponseTypeDef,
    ThumbnailsTypeDef,
    UpdatePipelineNotificationsResponseTypeDef,
    UpdatePipelineResponseTypeDef,
    UpdatePipelineStatusResponseTypeDef,
    VideoParametersTypeDef,
)
from .waiter import JobCompleteWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ElasticTranscoderClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    IncompatibleVersionException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ElasticTranscoderClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ElasticTranscoderClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/client.html#can_paginate)
        """
    def cancel_job(self, *, Id: str) -> Dict[str, Any]:
        """
        The CancelJob operation cancels an unfinished job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Client.cancel_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/client.html#cancel_job)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/client.html#close)
        """
    def create_job(
        self,
        *,
        PipelineId: str,
        Input: "JobInputTypeDef" = None,
        Inputs: List["JobInputTypeDef"] = None,
        Output: "CreateJobOutputTypeDef" = None,
        Outputs: List["CreateJobOutputTypeDef"] = None,
        OutputKeyPrefix: str = None,
        Playlists: List["CreateJobPlaylistTypeDef"] = None,
        UserMetadata: Dict[str, str] = None
    ) -> CreateJobResponseTypeDef:
        """
        When you create a job, Elastic Transcoder returns JSON data that includes the
        values that you specified plus information about the job that is created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Client.create_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/client.html#create_job)
        """
    def create_pipeline(
        self,
        *,
        Name: str,
        InputBucket: str,
        Role: str,
        OutputBucket: str = None,
        AwsKmsKeyArn: str = None,
        Notifications: "NotificationsTypeDef" = None,
        ContentConfig: "PipelineOutputConfigTypeDef" = None,
        ThumbnailConfig: "PipelineOutputConfigTypeDef" = None
    ) -> CreatePipelineResponseTypeDef:
        """
        The CreatePipeline operation creates a pipeline with settings that you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Client.create_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/client.html#create_pipeline)
        """
    def create_preset(
        self,
        *,
        Name: str,
        Container: str,
        Description: str = None,
        Video: "VideoParametersTypeDef" = None,
        Audio: "AudioParametersTypeDef" = None,
        Thumbnails: "ThumbnailsTypeDef" = None
    ) -> CreatePresetResponseTypeDef:
        """
        The CreatePreset operation creates a preset with settings that you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Client.create_preset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/client.html#create_preset)
        """
    def delete_pipeline(self, *, Id: str) -> Dict[str, Any]:
        """
        The DeletePipeline operation removes a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Client.delete_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/client.html#delete_pipeline)
        """
    def delete_preset(self, *, Id: str) -> Dict[str, Any]:
        """
        The DeletePreset operation removes a preset that you've added in an AWS region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Client.delete_preset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/client.html#delete_preset)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/client.html#generate_presigned_url)
        """
    def list_jobs_by_pipeline(
        self, *, PipelineId: str, Ascending: str = None, PageToken: str = None
    ) -> ListJobsByPipelineResponseTypeDef:
        """
        The ListJobsByPipeline operation gets a list of the jobs currently in a
        pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Client.list_jobs_by_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/client.html#list_jobs_by_pipeline)
        """
    def list_jobs_by_status(
        self, *, Status: str, Ascending: str = None, PageToken: str = None
    ) -> ListJobsByStatusResponseTypeDef:
        """
        The ListJobsByStatus operation gets a list of jobs that have a specified status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Client.list_jobs_by_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/client.html#list_jobs_by_status)
        """
    def list_pipelines(
        self, *, Ascending: str = None, PageToken: str = None
    ) -> ListPipelinesResponseTypeDef:
        """
        The ListPipelines operation gets a list of the pipelines associated with the
        current AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Client.list_pipelines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/client.html#list_pipelines)
        """
    def list_presets(
        self, *, Ascending: str = None, PageToken: str = None
    ) -> ListPresetsResponseTypeDef:
        """
        The ListPresets operation gets a list of the default presets included with
        Elastic Transcoder and the presets that you've added in an AWS region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Client.list_presets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/client.html#list_presets)
        """
    def read_job(self, *, Id: str) -> ReadJobResponseTypeDef:
        """
        The ReadJob operation returns detailed information about a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Client.read_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/client.html#read_job)
        """
    def read_pipeline(self, *, Id: str) -> ReadPipelineResponseTypeDef:
        """
        The ReadPipeline operation gets detailed information about a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Client.read_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/client.html#read_pipeline)
        """
    def read_preset(self, *, Id: str) -> ReadPresetResponseTypeDef:
        """
        The ReadPreset operation gets detailed information about a preset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Client.read_preset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/client.html#read_preset)
        """
    def test_role(
        self, *, Role: str, InputBucket: str, OutputBucket: str, Topics: List[str]
    ) -> TestRoleResponseTypeDef:
        """
        The TestRole operation tests the IAM role used to create the pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Client.test_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/client.html#test_role)
        """
    def update_pipeline(
        self,
        *,
        Id: str,
        Name: str = None,
        InputBucket: str = None,
        Role: str = None,
        AwsKmsKeyArn: str = None,
        Notifications: "NotificationsTypeDef" = None,
        ContentConfig: "PipelineOutputConfigTypeDef" = None,
        ThumbnailConfig: "PipelineOutputConfigTypeDef" = None
    ) -> UpdatePipelineResponseTypeDef:
        """
        Use the `UpdatePipeline` operation to update settings for a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Client.update_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/client.html#update_pipeline)
        """
    def update_pipeline_notifications(
        self, *, Id: str, Notifications: "NotificationsTypeDef"
    ) -> UpdatePipelineNotificationsResponseTypeDef:
        """
        With the UpdatePipelineNotifications operation, you can update Amazon Simple
        Notification Service (Amazon SNS) notifications for a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Client.update_pipeline_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/client.html#update_pipeline_notifications)
        """
    def update_pipeline_status(
        self, *, Id: str, Status: str
    ) -> UpdatePipelineStatusResponseTypeDef:
        """
        The UpdatePipelineStatus operation pauses or reactivates a pipeline, so that the
        pipeline stops or restarts the processing of jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Client.update_pipeline_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/client.html#update_pipeline_status)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_jobs_by_pipeline"]
    ) -> ListJobsByPipelinePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByPipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/paginators.html#listjobsbypipelinepaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_jobs_by_status"]
    ) -> ListJobsByStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByStatus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/paginators.html#listjobsbystatuspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_pipelines"]) -> ListPipelinesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPipelines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/paginators.html#listpipelinespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_presets"]) -> ListPresetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPresets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/paginators.html#listpresetspaginator)
        """
    def get_waiter(self, waiter_name: Literal["job_complete"]) -> JobCompleteWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/elastictranscoder.html#ElasticTranscoder.Waiter.JobComplete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/waiters.html#jobcompletewaiter)
        """
