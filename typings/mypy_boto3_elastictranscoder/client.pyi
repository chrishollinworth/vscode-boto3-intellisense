# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for elastictranscoder service client

Usage::

    ```python
    import boto3
    from mypy_boto3_elastictranscoder import ElasticTranscoderClient

    client: ElasticTranscoderClient = boto3.client("elastictranscoder")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_elastictranscoder.paginator import (
    ListJobsByPipelinePaginator,
    ListJobsByStatusPaginator,
    ListPipelinesPaginator,
    ListPresetsPaginator,
)
from mypy_boto3_elastictranscoder.type_defs import (
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
from mypy_boto3_elastictranscoder.waiter import JobCompleteWaiter

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


class ElasticTranscoderClient:
    """
    [ElasticTranscoder.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Client.can_paginate)
        """

    def cancel_job(self, Id: str) -> Dict[str, Any]:
        """
        [Client.cancel_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Client.cancel_job)
        """

    def create_job(
        self,
        PipelineId: str,
        Input: "JobInputTypeDef" = None,
        Inputs: List["JobInputTypeDef"] = None,
        Output: CreateJobOutputTypeDef = None,
        Outputs: List[CreateJobOutputTypeDef] = None,
        OutputKeyPrefix: str = None,
        Playlists: List[CreateJobPlaylistTypeDef] = None,
        UserMetadata: Dict[str, str] = None,
    ) -> CreateJobResponseTypeDef:
        """
        [Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Client.create_job)
        """

    def create_pipeline(
        self,
        Name: str,
        InputBucket: str,
        Role: str,
        OutputBucket: str = None,
        AwsKmsKeyArn: str = None,
        Notifications: "NotificationsTypeDef" = None,
        ContentConfig: "PipelineOutputConfigTypeDef" = None,
        ThumbnailConfig: "PipelineOutputConfigTypeDef" = None,
    ) -> CreatePipelineResponseTypeDef:
        """
        [Client.create_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Client.create_pipeline)
        """

    def create_preset(
        self,
        Name: str,
        Container: str,
        Description: str = None,
        Video: "VideoParametersTypeDef" = None,
        Audio: "AudioParametersTypeDef" = None,
        Thumbnails: "ThumbnailsTypeDef" = None,
    ) -> CreatePresetResponseTypeDef:
        """
        [Client.create_preset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Client.create_preset)
        """

    def delete_pipeline(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Client.delete_pipeline)
        """

    def delete_preset(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_preset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Client.delete_preset)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Client.generate_presigned_url)
        """

    def list_jobs_by_pipeline(
        self, PipelineId: str, Ascending: str = None, PageToken: str = None
    ) -> ListJobsByPipelineResponseTypeDef:
        """
        [Client.list_jobs_by_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Client.list_jobs_by_pipeline)
        """

    def list_jobs_by_status(
        self, Status: str, Ascending: str = None, PageToken: str = None
    ) -> ListJobsByStatusResponseTypeDef:
        """
        [Client.list_jobs_by_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Client.list_jobs_by_status)
        """

    def list_pipelines(
        self, Ascending: str = None, PageToken: str = None
    ) -> ListPipelinesResponseTypeDef:
        """
        [Client.list_pipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Client.list_pipelines)
        """

    def list_presets(
        self, Ascending: str = None, PageToken: str = None
    ) -> ListPresetsResponseTypeDef:
        """
        [Client.list_presets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Client.list_presets)
        """

    def read_job(self, Id: str) -> ReadJobResponseTypeDef:
        """
        [Client.read_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Client.read_job)
        """

    def read_pipeline(self, Id: str) -> ReadPipelineResponseTypeDef:
        """
        [Client.read_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Client.read_pipeline)
        """

    def read_preset(self, Id: str) -> ReadPresetResponseTypeDef:
        """
        [Client.read_preset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Client.read_preset)
        """

    def test_role(
        self, Role: str, InputBucket: str, OutputBucket: str, Topics: List[str]
    ) -> TestRoleResponseTypeDef:
        """
        [Client.test_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Client.test_role)
        """

    def update_pipeline(
        self,
        Id: str,
        Name: str = None,
        InputBucket: str = None,
        Role: str = None,
        AwsKmsKeyArn: str = None,
        Notifications: "NotificationsTypeDef" = None,
        ContentConfig: "PipelineOutputConfigTypeDef" = None,
        ThumbnailConfig: "PipelineOutputConfigTypeDef" = None,
    ) -> UpdatePipelineResponseTypeDef:
        """
        [Client.update_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Client.update_pipeline)
        """

    def update_pipeline_notifications(
        self, Id: str, Notifications: "NotificationsTypeDef"
    ) -> UpdatePipelineNotificationsResponseTypeDef:
        """
        [Client.update_pipeline_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Client.update_pipeline_notifications)
        """

    def update_pipeline_status(self, Id: str, Status: str) -> UpdatePipelineStatusResponseTypeDef:
        """
        [Client.update_pipeline_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Client.update_pipeline_status)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_jobs_by_pipeline"]
    ) -> ListJobsByPipelinePaginator:
        """
        [Paginator.ListJobsByPipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByPipeline)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_jobs_by_status"]
    ) -> ListJobsByStatusPaginator:
        """
        [Paginator.ListJobsByStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByStatus)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_pipelines"]) -> ListPipelinesPaginator:
        """
        [Paginator.ListPipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPipelines)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_presets"]) -> ListPresetsPaginator:
        """
        [Paginator.ListPresets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPresets)
        """

    def get_waiter(self, waiter_name: Literal["job_complete"]) -> JobCompleteWaiter:
        """
        [Waiter.JobComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Waiter.JobComplete)
        """
