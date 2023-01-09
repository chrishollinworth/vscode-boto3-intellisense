"""
Type annotations for lookoutvision service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_lookoutvision import LookoutforVisionClient

    client: LookoutforVisionClient = boto3.client("lookoutvision")
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .paginator import (
    ListDatasetEntriesPaginator,
    ListModelPackagingJobsPaginator,
    ListModelsPaginator,
    ListProjectsPaginator,
)
from .type_defs import (
    CreateDatasetResponseTypeDef,
    CreateModelResponseTypeDef,
    CreateProjectResponseTypeDef,
    DatasetSourceTypeDef,
    DeleteModelResponseTypeDef,
    DeleteProjectResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeModelPackagingJobResponseTypeDef,
    DescribeModelResponseTypeDef,
    DescribeProjectResponseTypeDef,
    DetectAnomaliesResponseTypeDef,
    ListDatasetEntriesResponseTypeDef,
    ListModelPackagingJobsResponseTypeDef,
    ListModelsResponseTypeDef,
    ListProjectsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ModelPackagingConfigurationTypeDef,
    OutputConfigTypeDef,
    StartModelPackagingJobResponseTypeDef,
    StartModelResponseTypeDef,
    StopModelResponseTypeDef,
    TagTypeDef,
    UpdateDatasetEntriesResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("LookoutforVisionClient",)

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
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class LookoutforVisionClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LookoutforVisionClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#close)
        """
    def create_dataset(
        self,
        *,
        ProjectName: str,
        DatasetType: str,
        DatasetSource: "DatasetSourceTypeDef" = None,
        ClientToken: str = None
    ) -> CreateDatasetResponseTypeDef:
        """
        Creates a new dataset in an Amazon Lookout for Vision project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.create_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#create_dataset)
        """
    def create_model(
        self,
        *,
        ProjectName: str,
        OutputConfig: "OutputConfigTypeDef",
        Description: str = None,
        ClientToken: str = None,
        KmsKeyId: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateModelResponseTypeDef:
        """
        Creates a new version of a model within an an Amazon Lookout for Vision project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.create_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#create_model)
        """
    def create_project(
        self, *, ProjectName: str, ClientToken: str = None
    ) -> CreateProjectResponseTypeDef:
        """
        Creates an empty Amazon Lookout for Vision project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.create_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#create_project)
        """
    def delete_dataset(
        self, *, ProjectName: str, DatasetType: str, ClientToken: str = None
    ) -> Dict[str, Any]:
        """
        Deletes an existing Amazon Lookout for Vision `dataset` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.delete_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#delete_dataset)
        """
    def delete_model(
        self, *, ProjectName: str, ModelVersion: str, ClientToken: str = None
    ) -> DeleteModelResponseTypeDef:
        """
        Deletes an Amazon Lookout for Vision model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.delete_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#delete_model)
        """
    def delete_project(
        self, *, ProjectName: str, ClientToken: str = None
    ) -> DeleteProjectResponseTypeDef:
        """
        Deletes an Amazon Lookout for Vision project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.delete_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#delete_project)
        """
    def describe_dataset(
        self, *, ProjectName: str, DatasetType: str
    ) -> DescribeDatasetResponseTypeDef:
        """
        Describe an Amazon Lookout for Vision dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.describe_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#describe_dataset)
        """
    def describe_model(
        self, *, ProjectName: str, ModelVersion: str
    ) -> DescribeModelResponseTypeDef:
        """
        Describes a version of an Amazon Lookout for Vision model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.describe_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#describe_model)
        """
    def describe_model_packaging_job(
        self, *, ProjectName: str, JobName: str
    ) -> DescribeModelPackagingJobResponseTypeDef:
        """
        Describes an Amazon Lookout for Vision model packaging job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.describe_model_packaging_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#describe_model_packaging_job)
        """
    def describe_project(self, *, ProjectName: str) -> DescribeProjectResponseTypeDef:
        """
        Describes an Amazon Lookout for Vision project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.describe_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#describe_project)
        """
    def detect_anomalies(
        self,
        *,
        ProjectName: str,
        ModelVersion: str,
        Body: Union[bytes, IO[bytes], StreamingBody],
        ContentType: str
    ) -> DetectAnomaliesResponseTypeDef:
        """
        Detects anomalies in an image that you supply.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.detect_anomalies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#detect_anomalies)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#generate_presigned_url)
        """
    def list_dataset_entries(
        self,
        *,
        ProjectName: str,
        DatasetType: str,
        Labeled: bool = None,
        AnomalyClass: str = None,
        BeforeCreationDate: Union[datetime, str] = None,
        AfterCreationDate: Union[datetime, str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        SourceRefContains: str = None
    ) -> ListDatasetEntriesResponseTypeDef:
        """
        Lists the JSON Lines within a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.list_dataset_entries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#list_dataset_entries)
        """
    def list_model_packaging_jobs(
        self, *, ProjectName: str, NextToken: str = None, MaxResults: int = None
    ) -> ListModelPackagingJobsResponseTypeDef:
        """
        Lists the model packaging jobs created for an Amazon Lookout for Vision project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.list_model_packaging_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#list_model_packaging_jobs)
        """
    def list_models(
        self, *, ProjectName: str, NextToken: str = None, MaxResults: int = None
    ) -> ListModelsResponseTypeDef:
        """
        Lists the versions of a model in an Amazon Lookout for Vision project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.list_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#list_models)
        """
    def list_projects(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListProjectsResponseTypeDef:
        """
        Lists the Amazon Lookout for Vision projects in your AWS account that are in the
        AWS Region in which you call `ListProjects` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.list_projects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#list_projects)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags attached to the specified Amazon Lookout for Vision
        model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#list_tags_for_resource)
        """
    def start_model(
        self,
        *,
        ProjectName: str,
        ModelVersion: str,
        MinInferenceUnits: int,
        ClientToken: str = None,
        MaxInferenceUnits: int = None
    ) -> StartModelResponseTypeDef:
        """
        Starts the running of the version of an Amazon Lookout for Vision model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.start_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#start_model)
        """
    def start_model_packaging_job(
        self,
        *,
        ProjectName: str,
        ModelVersion: str,
        Configuration: "ModelPackagingConfigurationTypeDef",
        JobName: str = None,
        Description: str = None,
        ClientToken: str = None
    ) -> StartModelPackagingJobResponseTypeDef:
        """
        Starts an Amazon Lookout for Vision model packaging job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.start_model_packaging_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#start_model_packaging_job)
        """
    def stop_model(
        self, *, ProjectName: str, ModelVersion: str, ClientToken: str = None
    ) -> StopModelResponseTypeDef:
        """
        Stops the hosting of a running model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.stop_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#stop_model)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds one or more key-value tags to an Amazon Lookout for Vision model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from an Amazon Lookout for Vision model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#untag_resource)
        """
    def update_dataset_entries(
        self,
        *,
        ProjectName: str,
        DatasetType: str,
        Changes: Union[bytes, IO[bytes], StreamingBody],
        ClientToken: str = None
    ) -> UpdateDatasetEntriesResponseTypeDef:
        """
        Adds or updates one or more JSON Line entries in a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Client.update_dataset_entries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client.html#update_dataset_entries)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_entries"]
    ) -> ListDatasetEntriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Paginator.ListDatasetEntries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/paginators.html#listdatasetentriespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_packaging_jobs"]
    ) -> ListModelPackagingJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Paginator.ListModelPackagingJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/paginators.html#listmodelpackagingjobspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_models"]) -> ListModelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Paginator.ListModels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/paginators.html#listmodelspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_projects"]) -> ListProjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/lookoutvision.html#LookoutforVision.Paginator.ListProjects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/paginators.html#listprojectspaginator)
        """
