"""
Type annotations for cleanroomsml service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_cleanroomsml import CleanRoomsMLClient

    client: CleanRoomsMLClient = boto3.client("cleanroomsml")
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import PolicyExistenceConditionType, SharedAudienceMetricsType, TagOnCreatePolicyType
from .paginator import (
    ListAudienceExportJobsPaginator,
    ListAudienceGenerationJobsPaginator,
    ListAudienceModelsPaginator,
    ListConfiguredAudienceModelsPaginator,
    ListTrainingDatasetsPaginator,
)
from .type_defs import (
    AudienceGenerationJobDataSourceTypeDef,
    AudienceSizeConfigTypeDef,
    AudienceSizeTypeDef,
    ConfiguredAudienceModelOutputConfigTypeDef,
    CreateAudienceModelResponseTypeDef,
    CreateConfiguredAudienceModelResponseTypeDef,
    CreateTrainingDatasetResponseTypeDef,
    DatasetTypeDef,
    GetAudienceGenerationJobResponseTypeDef,
    GetAudienceModelResponseTypeDef,
    GetConfiguredAudienceModelPolicyResponseTypeDef,
    GetConfiguredAudienceModelResponseTypeDef,
    GetTrainingDatasetResponseTypeDef,
    ListAudienceExportJobsResponseTypeDef,
    ListAudienceGenerationJobsResponseTypeDef,
    ListAudienceModelsResponseTypeDef,
    ListConfiguredAudienceModelsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTrainingDatasetsResponseTypeDef,
    PutConfiguredAudienceModelPolicyResponseTypeDef,
    StartAudienceGenerationJobResponseTypeDef,
    UpdateConfiguredAudienceModelResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CleanRoomsMLClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class CleanRoomsMLClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CleanRoomsMLClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#close)
        """

    def create_audience_model(
        self,
        *,
        name: str,
        trainingDatasetArn: str,
        description: str = None,
        kmsKeyArn: str = None,
        tags: Dict[str, str] = None,
        trainingDataEndTime: Union[datetime, str] = None,
        trainingDataStartTime: Union[datetime, str] = None
    ) -> CreateAudienceModelResponseTypeDef:
        """
        Defines the information necessary to create an audience model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.create_audience_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#create_audience_model)
        """

    def create_configured_audience_model(
        self,
        *,
        audienceModelArn: str,
        name: str,
        outputConfig: "ConfiguredAudienceModelOutputConfigTypeDef",
        sharedAudienceMetrics: List[SharedAudienceMetricsType],
        audienceSizeConfig: "AudienceSizeConfigTypeDef" = None,
        childResourceTagOnCreatePolicy: TagOnCreatePolicyType = None,
        description: str = None,
        minMatchingSeedSize: int = None,
        tags: Dict[str, str] = None
    ) -> CreateConfiguredAudienceModelResponseTypeDef:
        """
        Defines the information necessary to create a configured audience model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.create_configured_audience_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#create_configured_audience_model)
        """

    def create_training_dataset(
        self,
        *,
        name: str,
        roleArn: str,
        trainingData: List["DatasetTypeDef"],
        description: str = None,
        tags: Dict[str, str] = None
    ) -> CreateTrainingDatasetResponseTypeDef:
        """
        Defines the information necessary to create a training dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.create_training_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#create_training_dataset)
        """

    def delete_audience_generation_job(self, *, audienceGenerationJobArn: str) -> None:
        """
        Deletes the specified audience generation job, and removes all data associated
        with the job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.delete_audience_generation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#delete_audience_generation_job)
        """

    def delete_audience_model(self, *, audienceModelArn: str) -> None:
        """
        Specifies an audience model that you want to delete.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.delete_audience_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#delete_audience_model)
        """

    def delete_configured_audience_model(self, *, configuredAudienceModelArn: str) -> None:
        """
        Deletes the specified configured audience model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.delete_configured_audience_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#delete_configured_audience_model)
        """

    def delete_configured_audience_model_policy(self, *, configuredAudienceModelArn: str) -> None:
        """
        Deletes the specified configured audience model policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.delete_configured_audience_model_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#delete_configured_audience_model_policy)
        """

    def delete_training_dataset(self, *, trainingDatasetArn: str) -> None:
        """
        Specifies a training dataset that you want to delete.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.delete_training_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#delete_training_dataset)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#generate_presigned_url)
        """

    def get_audience_generation_job(
        self, *, audienceGenerationJobArn: str
    ) -> GetAudienceGenerationJobResponseTypeDef:
        """
        Returns information about an audience generation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.get_audience_generation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#get_audience_generation_job)
        """

    def get_audience_model(self, *, audienceModelArn: str) -> GetAudienceModelResponseTypeDef:
        """
        Returns information about an audience model See also: `AWS API Documentation <ht
        tps://docs.aws.amazon.com/goto/WebAPI/cleanroomsml-2023-09-
        06/GetAudienceModel>`_ **Request Syntax** response = client.get_audience_model(
        audienceModelArn='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.get_audience_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#get_audience_model)
        """

    def get_configured_audience_model(
        self, *, configuredAudienceModelArn: str
    ) -> GetConfiguredAudienceModelResponseTypeDef:
        """
        Returns information about a specified configured audience model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.get_configured_audience_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#get_configured_audience_model)
        """

    def get_configured_audience_model_policy(
        self, *, configuredAudienceModelArn: str
    ) -> GetConfiguredAudienceModelPolicyResponseTypeDef:
        """
        Returns information about a configured audience model policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.get_configured_audience_model_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#get_configured_audience_model_policy)
        """

    def get_training_dataset(self, *, trainingDatasetArn: str) -> GetTrainingDatasetResponseTypeDef:
        """
        Returns information about a training dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.get_training_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#get_training_dataset)
        """

    def list_audience_export_jobs(
        self, *, audienceGenerationJobArn: str = None, maxResults: int = None, nextToken: str = None
    ) -> ListAudienceExportJobsResponseTypeDef:
        """
        Returns a list of the audience export jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.list_audience_export_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#list_audience_export_jobs)
        """

    def list_audience_generation_jobs(
        self,
        *,
        collaborationId: str = None,
        configuredAudienceModelArn: str = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListAudienceGenerationJobsResponseTypeDef:
        """
        Returns a list of audience generation jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.list_audience_generation_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#list_audience_generation_jobs)
        """

    def list_audience_models(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListAudienceModelsResponseTypeDef:
        """
        Returns a list of audience models.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.list_audience_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#list_audience_models)
        """

    def list_configured_audience_models(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListConfiguredAudienceModelsResponseTypeDef:
        """
        Returns a list of the configured audience models.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.list_configured_audience_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#list_configured_audience_models)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags for a provided resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#list_tags_for_resource)
        """

    def list_training_datasets(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListTrainingDatasetsResponseTypeDef:
        """
        Returns a list of training datasets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.list_training_datasets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#list_training_datasets)
        """

    def put_configured_audience_model_policy(
        self,
        *,
        configuredAudienceModelArn: str,
        configuredAudienceModelPolicy: str,
        policyExistenceCondition: PolicyExistenceConditionType = None,
        previousPolicyHash: str = None
    ) -> PutConfiguredAudienceModelPolicyResponseTypeDef:
        """
        Create or update the resource policy for a configured audience model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.put_configured_audience_model_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#put_configured_audience_model_policy)
        """

    def start_audience_export_job(
        self,
        *,
        audienceGenerationJobArn: str,
        audienceSize: "AudienceSizeTypeDef",
        name: str,
        description: str = None
    ) -> None:
        """
        Export an audience of a specified size after you have generated an audience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.start_audience_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#start_audience_export_job)
        """

    def start_audience_generation_job(
        self,
        *,
        configuredAudienceModelArn: str,
        name: str,
        seedAudience: "AudienceGenerationJobDataSourceTypeDef",
        collaborationId: str = None,
        description: str = None,
        includeSeedInOutput: bool = None,
        tags: Dict[str, str] = None
    ) -> StartAudienceGenerationJobResponseTypeDef:
        """
        Information necessary to start the audience generation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.start_audience_generation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#start_audience_generation_job)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds metadata tags to a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes metadata tags from a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#untag_resource)
        """

    def update_configured_audience_model(
        self,
        *,
        configuredAudienceModelArn: str,
        audienceModelArn: str = None,
        audienceSizeConfig: "AudienceSizeConfigTypeDef" = None,
        description: str = None,
        minMatchingSeedSize: int = None,
        outputConfig: "ConfiguredAudienceModelOutputConfigTypeDef" = None,
        sharedAudienceMetrics: List[SharedAudienceMetricsType] = None
    ) -> UpdateConfiguredAudienceModelResponseTypeDef:
        """
        Provides the information necessary to update a configured audience model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Client.update_configured_audience_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client.html#update_configured_audience_model)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_audience_export_jobs"]
    ) -> ListAudienceExportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListAudienceExportJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators.html#listaudienceexportjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_audience_generation_jobs"]
    ) -> ListAudienceGenerationJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListAudienceGenerationJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators.html#listaudiencegenerationjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_audience_models"]
    ) -> ListAudienceModelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListAudienceModels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators.html#listaudiencemodelspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_configured_audience_models"]
    ) -> ListConfiguredAudienceModelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListConfiguredAudienceModels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators.html#listconfiguredaudiencemodelspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_training_datasets"]
    ) -> ListTrainingDatasetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListTrainingDatasets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators.html#listtrainingdatasetspaginator)
        """
