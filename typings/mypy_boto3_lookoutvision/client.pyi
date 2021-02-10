"""
Main interface for lookoutvision service client

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

from botocore.client import ClientMeta

from mypy_boto3_lookoutvision.paginator import (
    ListDatasetEntriesPaginator,
    ListModelsPaginator,
    ListProjectsPaginator,
)
from mypy_boto3_lookoutvision.type_defs import (
    CreateDatasetResponseTypeDef,
    CreateModelResponseTypeDef,
    CreateProjectResponseTypeDef,
    DatasetSourceTypeDef,
    DeleteModelResponseTypeDef,
    DeleteProjectResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeModelResponseTypeDef,
    DescribeProjectResponseTypeDef,
    DetectAnomaliesResponseTypeDef,
    ListDatasetEntriesResponseTypeDef,
    ListModelsResponseTypeDef,
    ListProjectsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    OutputConfigTypeDef,
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


class LookoutforVisionClient:
    """
    [LookoutforVision.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Client.can_paginate)
        """

    def create_dataset(
        self,
        ProjectName: str,
        DatasetType: str,
        DatasetSource: DatasetSourceTypeDef = None,
        ClientToken: str = None,
    ) -> CreateDatasetResponseTypeDef:
        """
        [Client.create_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Client.create_dataset)
        """

    def create_model(
        self,
        ProjectName: str,
        OutputConfig: "OutputConfigTypeDef",
        Description: str = None,
        ClientToken: str = None,
        KmsKeyId: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateModelResponseTypeDef:
        """
        [Client.create_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Client.create_model)
        """

    def create_project(
        self, ProjectName: str, ClientToken: str = None
    ) -> CreateProjectResponseTypeDef:
        """
        [Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Client.create_project)
        """

    def delete_dataset(
        self, ProjectName: str, DatasetType: str, ClientToken: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Client.delete_dataset)
        """

    def delete_model(
        self, ProjectName: str, ModelVersion: str, ClientToken: str = None
    ) -> DeleteModelResponseTypeDef:
        """
        [Client.delete_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Client.delete_model)
        """

    def delete_project(
        self, ProjectName: str, ClientToken: str = None
    ) -> DeleteProjectResponseTypeDef:
        """
        [Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Client.delete_project)
        """

    def describe_dataset(
        self, ProjectName: str, DatasetType: str
    ) -> DescribeDatasetResponseTypeDef:
        """
        [Client.describe_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Client.describe_dataset)
        """

    def describe_model(self, ProjectName: str, ModelVersion: str) -> DescribeModelResponseTypeDef:
        """
        [Client.describe_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Client.describe_model)
        """

    def describe_project(self, ProjectName: str) -> DescribeProjectResponseTypeDef:
        """
        [Client.describe_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Client.describe_project)
        """

    def detect_anomalies(
        self, ProjectName: str, ModelVersion: str, Body: Union[bytes, IO[bytes]], ContentType: str
    ) -> DetectAnomaliesResponseTypeDef:
        """
        [Client.detect_anomalies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Client.detect_anomalies)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Client.generate_presigned_url)
        """

    def list_dataset_entries(
        self,
        ProjectName: str,
        DatasetType: str,
        Labeled: bool = None,
        AnomalyClass: str = None,
        BeforeCreationDate: datetime = None,
        AfterCreationDate: datetime = None,
        NextToken: str = None,
        MaxResults: int = None,
        SourceRefContains: str = None,
    ) -> ListDatasetEntriesResponseTypeDef:
        """
        [Client.list_dataset_entries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Client.list_dataset_entries)
        """

    def list_models(
        self, ProjectName: str, NextToken: str = None, MaxResults: int = None
    ) -> ListModelsResponseTypeDef:
        """
        [Client.list_models documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Client.list_models)
        """

    def list_projects(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListProjectsResponseTypeDef:
        """
        [Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Client.list_projects)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Client.list_tags_for_resource)
        """

    def start_model(
        self, ProjectName: str, ModelVersion: str, MinInferenceUnits: int, ClientToken: str = None
    ) -> StartModelResponseTypeDef:
        """
        [Client.start_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Client.start_model)
        """

    def stop_model(
        self, ProjectName: str, ModelVersion: str, ClientToken: str = None
    ) -> StopModelResponseTypeDef:
        """
        [Client.stop_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Client.stop_model)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Client.untag_resource)
        """

    def update_dataset_entries(
        self,
        ProjectName: str,
        DatasetType: str,
        Changes: Union[bytes, IO[bytes]],
        ClientToken: str = None,
    ) -> UpdateDatasetEntriesResponseTypeDef:
        """
        [Client.update_dataset_entries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Client.update_dataset_entries)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_entries"]
    ) -> ListDatasetEntriesPaginator:
        """
        [Paginator.ListDatasetEntries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Paginator.ListDatasetEntries)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_models"]) -> ListModelsPaginator:
        """
        [Paginator.ListModels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Paginator.ListModels)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_projects"]) -> ListProjectsPaginator:
        """
        [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Paginator.ListProjects)
        """
