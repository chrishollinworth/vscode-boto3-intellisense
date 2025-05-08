"""
Type annotations for lookoutvision service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_lookoutvision.client import LookoutforVisionClient

    session = Session()
    client: LookoutforVisionClient = session.client("lookoutvision")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListDatasetEntriesPaginator,
    ListModelPackagingJobsPaginator,
    ListModelsPaginator,
    ListProjectsPaginator,
)
from .type_defs import (
    CreateDatasetRequestTypeDef,
    CreateDatasetResponseTypeDef,
    CreateModelRequestTypeDef,
    CreateModelResponseTypeDef,
    CreateProjectRequestTypeDef,
    CreateProjectResponseTypeDef,
    DeleteDatasetRequestTypeDef,
    DeleteModelRequestTypeDef,
    DeleteModelResponseTypeDef,
    DeleteProjectRequestTypeDef,
    DeleteProjectResponseTypeDef,
    DescribeDatasetRequestTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeModelPackagingJobRequestTypeDef,
    DescribeModelPackagingJobResponseTypeDef,
    DescribeModelRequestTypeDef,
    DescribeModelResponseTypeDef,
    DescribeProjectRequestTypeDef,
    DescribeProjectResponseTypeDef,
    DetectAnomaliesRequestTypeDef,
    DetectAnomaliesResponseTypeDef,
    ListDatasetEntriesRequestTypeDef,
    ListDatasetEntriesResponseTypeDef,
    ListModelPackagingJobsRequestTypeDef,
    ListModelPackagingJobsResponseTypeDef,
    ListModelsRequestTypeDef,
    ListModelsResponseTypeDef,
    ListProjectsRequestTypeDef,
    ListProjectsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    StartModelPackagingJobRequestTypeDef,
    StartModelPackagingJobResponseTypeDef,
    StartModelRequestTypeDef,
    StartModelResponseTypeDef,
    StopModelRequestTypeDef,
    StopModelResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateDatasetEntriesRequestTypeDef,
    UpdateDatasetEntriesResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("LookoutforVisionClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LookoutforVisionClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#generate_presigned_url)
        """

    def create_dataset(
        self, **kwargs: Unpack[CreateDatasetRequestTypeDef]
    ) -> CreateDatasetResponseTypeDef:
        """
        Creates a new dataset in an Amazon Lookout for Vision project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/create_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#create_dataset)
        """

    def create_model(
        self, **kwargs: Unpack[CreateModelRequestTypeDef]
    ) -> CreateModelResponseTypeDef:
        """
        Creates a new version of a model within an an Amazon Lookout for Vision project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/create_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#create_model)
        """

    def create_project(
        self, **kwargs: Unpack[CreateProjectRequestTypeDef]
    ) -> CreateProjectResponseTypeDef:
        """
        Creates an empty Amazon Lookout for Vision project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/create_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#create_project)
        """

    def delete_dataset(self, **kwargs: Unpack[DeleteDatasetRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an existing Amazon Lookout for Vision <code>dataset</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/delete_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#delete_dataset)
        """

    def delete_model(
        self, **kwargs: Unpack[DeleteModelRequestTypeDef]
    ) -> DeleteModelResponseTypeDef:
        """
        Deletes an Amazon Lookout for Vision model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/delete_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#delete_model)
        """

    def delete_project(
        self, **kwargs: Unpack[DeleteProjectRequestTypeDef]
    ) -> DeleteProjectResponseTypeDef:
        """
        Deletes an Amazon Lookout for Vision project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/delete_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#delete_project)
        """

    def describe_dataset(
        self, **kwargs: Unpack[DescribeDatasetRequestTypeDef]
    ) -> DescribeDatasetResponseTypeDef:
        """
        Describe an Amazon Lookout for Vision dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/describe_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#describe_dataset)
        """

    def describe_model(
        self, **kwargs: Unpack[DescribeModelRequestTypeDef]
    ) -> DescribeModelResponseTypeDef:
        """
        Describes a version of an Amazon Lookout for Vision model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/describe_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#describe_model)
        """

    def describe_model_packaging_job(
        self, **kwargs: Unpack[DescribeModelPackagingJobRequestTypeDef]
    ) -> DescribeModelPackagingJobResponseTypeDef:
        """
        Describes an Amazon Lookout for Vision model packaging job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/describe_model_packaging_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#describe_model_packaging_job)
        """

    def describe_project(
        self, **kwargs: Unpack[DescribeProjectRequestTypeDef]
    ) -> DescribeProjectResponseTypeDef:
        """
        Describes an Amazon Lookout for Vision project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/describe_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#describe_project)
        """

    def detect_anomalies(
        self, **kwargs: Unpack[DetectAnomaliesRequestTypeDef]
    ) -> DetectAnomaliesResponseTypeDef:
        """
        Detects anomalies in an image that you supply.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/detect_anomalies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#detect_anomalies)
        """

    def list_dataset_entries(
        self, **kwargs: Unpack[ListDatasetEntriesRequestTypeDef]
    ) -> ListDatasetEntriesResponseTypeDef:
        """
        Lists the JSON Lines within a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/list_dataset_entries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#list_dataset_entries)
        """

    def list_model_packaging_jobs(
        self, **kwargs: Unpack[ListModelPackagingJobsRequestTypeDef]
    ) -> ListModelPackagingJobsResponseTypeDef:
        """
        Lists the model packaging jobs created for an Amazon Lookout for Vision project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/list_model_packaging_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#list_model_packaging_jobs)
        """

    def list_models(self, **kwargs: Unpack[ListModelsRequestTypeDef]) -> ListModelsResponseTypeDef:
        """
        Lists the versions of a model in an Amazon Lookout for Vision project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/list_models.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#list_models)
        """

    def list_projects(
        self, **kwargs: Unpack[ListProjectsRequestTypeDef]
    ) -> ListProjectsResponseTypeDef:
        """
        Lists the Amazon Lookout for Vision projects in your AWS account that are in
        the AWS Region in which you call <code>ListProjects</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/list_projects.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#list_projects)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags attached to the specified Amazon Lookout for Vision
        model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#list_tags_for_resource)
        """

    def start_model(self, **kwargs: Unpack[StartModelRequestTypeDef]) -> StartModelResponseTypeDef:
        """
        Starts the running of the version of an Amazon Lookout for Vision model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/start_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#start_model)
        """

    def start_model_packaging_job(
        self, **kwargs: Unpack[StartModelPackagingJobRequestTypeDef]
    ) -> StartModelPackagingJobResponseTypeDef:
        """
        Starts an Amazon Lookout for Vision model packaging job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/start_model_packaging_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#start_model_packaging_job)
        """

    def stop_model(self, **kwargs: Unpack[StopModelRequestTypeDef]) -> StopModelResponseTypeDef:
        """
        Stops the hosting of a running model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/stop_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#stop_model)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds one or more key-value tags to an Amazon Lookout for Vision model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from an Amazon Lookout for Vision model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#untag_resource)
        """

    def update_dataset_entries(
        self, **kwargs: Unpack[UpdateDatasetEntriesRequestTypeDef]
    ) -> UpdateDatasetEntriesResponseTypeDef:
        """
        Adds or updates one or more JSON Line entries in a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/update_dataset_entries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#update_dataset_entries)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_dataset_entries"]
    ) -> ListDatasetEntriesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_model_packaging_jobs"]
    ) -> ListModelPackagingJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_models"]
    ) -> ListModelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_projects"]
    ) -> ListProjectsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/client/#get_paginator)
        """
