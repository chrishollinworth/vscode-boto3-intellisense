"""
Type annotations for cleanroomsml service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cleanroomsml.client import CleanRoomsMLClient

    session = Session()
    client: CleanRoomsMLClient = session.client("cleanroomsml")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAudienceExportJobsPaginator,
    ListAudienceGenerationJobsPaginator,
    ListAudienceModelsPaginator,
    ListCollaborationConfiguredModelAlgorithmAssociationsPaginator,
    ListCollaborationMLInputChannelsPaginator,
    ListCollaborationTrainedModelExportJobsPaginator,
    ListCollaborationTrainedModelInferenceJobsPaginator,
    ListCollaborationTrainedModelsPaginator,
    ListConfiguredAudienceModelsPaginator,
    ListConfiguredModelAlgorithmAssociationsPaginator,
    ListConfiguredModelAlgorithmsPaginator,
    ListMLInputChannelsPaginator,
    ListTrainedModelInferenceJobsPaginator,
    ListTrainedModelsPaginator,
    ListTrainingDatasetsPaginator,
)
from .type_defs import (
    CancelTrainedModelInferenceJobRequestTypeDef,
    CancelTrainedModelRequestTypeDef,
    CreateAudienceModelRequestTypeDef,
    CreateAudienceModelResponseTypeDef,
    CreateConfiguredAudienceModelRequestTypeDef,
    CreateConfiguredAudienceModelResponseTypeDef,
    CreateConfiguredModelAlgorithmAssociationRequestTypeDef,
    CreateConfiguredModelAlgorithmAssociationResponseTypeDef,
    CreateConfiguredModelAlgorithmRequestTypeDef,
    CreateConfiguredModelAlgorithmResponseTypeDef,
    CreateMLInputChannelRequestTypeDef,
    CreateMLInputChannelResponseTypeDef,
    CreateTrainedModelRequestTypeDef,
    CreateTrainedModelResponseTypeDef,
    CreateTrainingDatasetRequestTypeDef,
    CreateTrainingDatasetResponseTypeDef,
    DeleteAudienceGenerationJobRequestTypeDef,
    DeleteAudienceModelRequestTypeDef,
    DeleteConfiguredAudienceModelPolicyRequestTypeDef,
    DeleteConfiguredAudienceModelRequestTypeDef,
    DeleteConfiguredModelAlgorithmAssociationRequestTypeDef,
    DeleteConfiguredModelAlgorithmRequestTypeDef,
    DeleteMLConfigurationRequestTypeDef,
    DeleteMLInputChannelDataRequestTypeDef,
    DeleteTrainedModelOutputRequestTypeDef,
    DeleteTrainingDatasetRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetAudienceGenerationJobRequestTypeDef,
    GetAudienceGenerationJobResponseTypeDef,
    GetAudienceModelRequestTypeDef,
    GetAudienceModelResponseTypeDef,
    GetCollaborationConfiguredModelAlgorithmAssociationRequestTypeDef,
    GetCollaborationConfiguredModelAlgorithmAssociationResponseTypeDef,
    GetCollaborationMLInputChannelRequestTypeDef,
    GetCollaborationMLInputChannelResponseTypeDef,
    GetCollaborationTrainedModelRequestTypeDef,
    GetCollaborationTrainedModelResponseTypeDef,
    GetConfiguredAudienceModelPolicyRequestTypeDef,
    GetConfiguredAudienceModelPolicyResponseTypeDef,
    GetConfiguredAudienceModelRequestTypeDef,
    GetConfiguredAudienceModelResponseTypeDef,
    GetConfiguredModelAlgorithmAssociationRequestTypeDef,
    GetConfiguredModelAlgorithmAssociationResponseTypeDef,
    GetConfiguredModelAlgorithmRequestTypeDef,
    GetConfiguredModelAlgorithmResponseTypeDef,
    GetMLConfigurationRequestTypeDef,
    GetMLConfigurationResponseTypeDef,
    GetMLInputChannelRequestTypeDef,
    GetMLInputChannelResponseTypeDef,
    GetTrainedModelInferenceJobRequestTypeDef,
    GetTrainedModelInferenceJobResponseTypeDef,
    GetTrainedModelRequestTypeDef,
    GetTrainedModelResponseTypeDef,
    GetTrainingDatasetRequestTypeDef,
    GetTrainingDatasetResponseTypeDef,
    ListAudienceExportJobsRequestTypeDef,
    ListAudienceExportJobsResponseTypeDef,
    ListAudienceGenerationJobsRequestTypeDef,
    ListAudienceGenerationJobsResponseTypeDef,
    ListAudienceModelsRequestTypeDef,
    ListAudienceModelsResponseTypeDef,
    ListCollaborationConfiguredModelAlgorithmAssociationsRequestTypeDef,
    ListCollaborationConfiguredModelAlgorithmAssociationsResponseTypeDef,
    ListCollaborationMLInputChannelsRequestTypeDef,
    ListCollaborationMLInputChannelsResponseTypeDef,
    ListCollaborationTrainedModelExportJobsRequestTypeDef,
    ListCollaborationTrainedModelExportJobsResponseTypeDef,
    ListCollaborationTrainedModelInferenceJobsRequestTypeDef,
    ListCollaborationTrainedModelInferenceJobsResponseTypeDef,
    ListCollaborationTrainedModelsRequestTypeDef,
    ListCollaborationTrainedModelsResponseTypeDef,
    ListConfiguredAudienceModelsRequestTypeDef,
    ListConfiguredAudienceModelsResponseTypeDef,
    ListConfiguredModelAlgorithmAssociationsRequestTypeDef,
    ListConfiguredModelAlgorithmAssociationsResponseTypeDef,
    ListConfiguredModelAlgorithmsRequestTypeDef,
    ListConfiguredModelAlgorithmsResponseTypeDef,
    ListMLInputChannelsRequestTypeDef,
    ListMLInputChannelsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTrainedModelInferenceJobsRequestTypeDef,
    ListTrainedModelInferenceJobsResponseTypeDef,
    ListTrainedModelsRequestTypeDef,
    ListTrainedModelsResponseTypeDef,
    ListTrainingDatasetsRequestTypeDef,
    ListTrainingDatasetsResponseTypeDef,
    PutConfiguredAudienceModelPolicyRequestTypeDef,
    PutConfiguredAudienceModelPolicyResponseTypeDef,
    PutMLConfigurationRequestTypeDef,
    StartAudienceExportJobRequestTypeDef,
    StartAudienceGenerationJobRequestTypeDef,
    StartAudienceGenerationJobResponseTypeDef,
    StartTrainedModelExportJobRequestTypeDef,
    StartTrainedModelInferenceJobRequestTypeDef,
    StartTrainedModelInferenceJobResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateConfiguredAudienceModelRequestTypeDef,
    UpdateConfiguredAudienceModelResponseTypeDef,
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

__all__ = ("CleanRoomsMLClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class CleanRoomsMLClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CleanRoomsMLClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#generate_presigned_url)
        """

    def cancel_trained_model(
        self, **kwargs: Unpack[CancelTrainedModelRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Submits a request to cancel the trained model job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/cancel_trained_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#cancel_trained_model)
        """

    def cancel_trained_model_inference_job(
        self, **kwargs: Unpack[CancelTrainedModelInferenceJobRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Submits a request to cancel a trained model inference job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/cancel_trained_model_inference_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#cancel_trained_model_inference_job)
        """

    def create_audience_model(
        self, **kwargs: Unpack[CreateAudienceModelRequestTypeDef]
    ) -> CreateAudienceModelResponseTypeDef:
        """
        Defines the information necessary to create an audience model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/create_audience_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#create_audience_model)
        """

    def create_configured_audience_model(
        self, **kwargs: Unpack[CreateConfiguredAudienceModelRequestTypeDef]
    ) -> CreateConfiguredAudienceModelResponseTypeDef:
        """
        Defines the information necessary to create a configured audience model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/create_configured_audience_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#create_configured_audience_model)
        """

    def create_configured_model_algorithm(
        self, **kwargs: Unpack[CreateConfiguredModelAlgorithmRequestTypeDef]
    ) -> CreateConfiguredModelAlgorithmResponseTypeDef:
        """
        Creates a configured model algorithm using a container image stored in an ECR
        repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/create_configured_model_algorithm.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#create_configured_model_algorithm)
        """

    def create_configured_model_algorithm_association(
        self, **kwargs: Unpack[CreateConfiguredModelAlgorithmAssociationRequestTypeDef]
    ) -> CreateConfiguredModelAlgorithmAssociationResponseTypeDef:
        """
        Associates a configured model algorithm to a collaboration for use by any
        member of the collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/create_configured_model_algorithm_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#create_configured_model_algorithm_association)
        """

    def create_ml_input_channel(
        self, **kwargs: Unpack[CreateMLInputChannelRequestTypeDef]
    ) -> CreateMLInputChannelResponseTypeDef:
        """
        Provides the information to create an ML input channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/create_ml_input_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#create_ml_input_channel)
        """

    def create_trained_model(
        self, **kwargs: Unpack[CreateTrainedModelRequestTypeDef]
    ) -> CreateTrainedModelResponseTypeDef:
        """
        Creates a trained model from an associated configured model algorithm using
        data from any member of the collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/create_trained_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#create_trained_model)
        """

    def create_training_dataset(
        self, **kwargs: Unpack[CreateTrainingDatasetRequestTypeDef]
    ) -> CreateTrainingDatasetResponseTypeDef:
        """
        Defines the information necessary to create a training dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/create_training_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#create_training_dataset)
        """

    def delete_audience_generation_job(
        self, **kwargs: Unpack[DeleteAudienceGenerationJobRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified audience generation job, and removes all data associated
        with the job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/delete_audience_generation_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#delete_audience_generation_job)
        """

    def delete_audience_model(
        self, **kwargs: Unpack[DeleteAudienceModelRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Specifies an audience model that you want to delete.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/delete_audience_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#delete_audience_model)
        """

    def delete_configured_audience_model(
        self, **kwargs: Unpack[DeleteConfiguredAudienceModelRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified configured audience model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/delete_configured_audience_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#delete_configured_audience_model)
        """

    def delete_configured_audience_model_policy(
        self, **kwargs: Unpack[DeleteConfiguredAudienceModelPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified configured audience model policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/delete_configured_audience_model_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#delete_configured_audience_model_policy)
        """

    def delete_configured_model_algorithm(
        self, **kwargs: Unpack[DeleteConfiguredModelAlgorithmRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a configured model algorithm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/delete_configured_model_algorithm.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#delete_configured_model_algorithm)
        """

    def delete_configured_model_algorithm_association(
        self, **kwargs: Unpack[DeleteConfiguredModelAlgorithmAssociationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a configured model algorithm association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/delete_configured_model_algorithm_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#delete_configured_model_algorithm_association)
        """

    def delete_ml_configuration(
        self, **kwargs: Unpack[DeleteMLConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a ML modeling configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/delete_ml_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#delete_ml_configuration)
        """

    def delete_ml_input_channel_data(
        self, **kwargs: Unpack[DeleteMLInputChannelDataRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Provides the information necessary to delete an ML input channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/delete_ml_input_channel_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#delete_ml_input_channel_data)
        """

    def delete_trained_model_output(
        self, **kwargs: Unpack[DeleteTrainedModelOutputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the output of a trained model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/delete_trained_model_output.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#delete_trained_model_output)
        """

    def delete_training_dataset(
        self, **kwargs: Unpack[DeleteTrainingDatasetRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Specifies a training dataset that you want to delete.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/delete_training_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#delete_training_dataset)
        """

    def get_audience_generation_job(
        self, **kwargs: Unpack[GetAudienceGenerationJobRequestTypeDef]
    ) -> GetAudienceGenerationJobResponseTypeDef:
        """
        Returns information about an audience generation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_audience_generation_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_audience_generation_job)
        """

    def get_audience_model(
        self, **kwargs: Unpack[GetAudienceModelRequestTypeDef]
    ) -> GetAudienceModelResponseTypeDef:
        """
        Returns information about an audience model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_audience_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_audience_model)
        """

    def get_collaboration_configured_model_algorithm_association(
        self, **kwargs: Unpack[GetCollaborationConfiguredModelAlgorithmAssociationRequestTypeDef]
    ) -> GetCollaborationConfiguredModelAlgorithmAssociationResponseTypeDef:
        """
        Returns information about the configured model algorithm association in a
        collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_collaboration_configured_model_algorithm_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_collaboration_configured_model_algorithm_association)
        """

    def get_collaboration_ml_input_channel(
        self, **kwargs: Unpack[GetCollaborationMLInputChannelRequestTypeDef]
    ) -> GetCollaborationMLInputChannelResponseTypeDef:
        """
        Returns information about a specific ML input channel in a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_collaboration_ml_input_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_collaboration_ml_input_channel)
        """

    def get_collaboration_trained_model(
        self, **kwargs: Unpack[GetCollaborationTrainedModelRequestTypeDef]
    ) -> GetCollaborationTrainedModelResponseTypeDef:
        """
        Returns information about a trained model in a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_collaboration_trained_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_collaboration_trained_model)
        """

    def get_configured_audience_model(
        self, **kwargs: Unpack[GetConfiguredAudienceModelRequestTypeDef]
    ) -> GetConfiguredAudienceModelResponseTypeDef:
        """
        Returns information about a specified configured audience model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_configured_audience_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_configured_audience_model)
        """

    def get_configured_audience_model_policy(
        self, **kwargs: Unpack[GetConfiguredAudienceModelPolicyRequestTypeDef]
    ) -> GetConfiguredAudienceModelPolicyResponseTypeDef:
        """
        Returns information about a configured audience model policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_configured_audience_model_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_configured_audience_model_policy)
        """

    def get_configured_model_algorithm(
        self, **kwargs: Unpack[GetConfiguredModelAlgorithmRequestTypeDef]
    ) -> GetConfiguredModelAlgorithmResponseTypeDef:
        """
        Returns information about a configured model algorithm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_configured_model_algorithm.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_configured_model_algorithm)
        """

    def get_configured_model_algorithm_association(
        self, **kwargs: Unpack[GetConfiguredModelAlgorithmAssociationRequestTypeDef]
    ) -> GetConfiguredModelAlgorithmAssociationResponseTypeDef:
        """
        Returns information about a configured model algorithm association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_configured_model_algorithm_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_configured_model_algorithm_association)
        """

    def get_ml_configuration(
        self, **kwargs: Unpack[GetMLConfigurationRequestTypeDef]
    ) -> GetMLConfigurationResponseTypeDef:
        """
        Returns information about a specific ML configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_ml_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_ml_configuration)
        """

    def get_ml_input_channel(
        self, **kwargs: Unpack[GetMLInputChannelRequestTypeDef]
    ) -> GetMLInputChannelResponseTypeDef:
        """
        Returns information about an ML input channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_ml_input_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_ml_input_channel)
        """

    def get_trained_model(
        self, **kwargs: Unpack[GetTrainedModelRequestTypeDef]
    ) -> GetTrainedModelResponseTypeDef:
        """
        Returns information about a trained model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_trained_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_trained_model)
        """

    def get_trained_model_inference_job(
        self, **kwargs: Unpack[GetTrainedModelInferenceJobRequestTypeDef]
    ) -> GetTrainedModelInferenceJobResponseTypeDef:
        """
        Returns information about a trained model inference job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_trained_model_inference_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_trained_model_inference_job)
        """

    def get_training_dataset(
        self, **kwargs: Unpack[GetTrainingDatasetRequestTypeDef]
    ) -> GetTrainingDatasetResponseTypeDef:
        """
        Returns information about a training dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_training_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_training_dataset)
        """

    def list_audience_export_jobs(
        self, **kwargs: Unpack[ListAudienceExportJobsRequestTypeDef]
    ) -> ListAudienceExportJobsResponseTypeDef:
        """
        Returns a list of the audience export jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/list_audience_export_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#list_audience_export_jobs)
        """

    def list_audience_generation_jobs(
        self, **kwargs: Unpack[ListAudienceGenerationJobsRequestTypeDef]
    ) -> ListAudienceGenerationJobsResponseTypeDef:
        """
        Returns a list of audience generation jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/list_audience_generation_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#list_audience_generation_jobs)
        """

    def list_audience_models(
        self, **kwargs: Unpack[ListAudienceModelsRequestTypeDef]
    ) -> ListAudienceModelsResponseTypeDef:
        """
        Returns a list of audience models.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/list_audience_models.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#list_audience_models)
        """

    def list_collaboration_configured_model_algorithm_associations(
        self, **kwargs: Unpack[ListCollaborationConfiguredModelAlgorithmAssociationsRequestTypeDef]
    ) -> ListCollaborationConfiguredModelAlgorithmAssociationsResponseTypeDef:
        """
        Returns a list of the configured model algorithm associations in a
        collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/list_collaboration_configured_model_algorithm_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#list_collaboration_configured_model_algorithm_associations)
        """

    def list_collaboration_ml_input_channels(
        self, **kwargs: Unpack[ListCollaborationMLInputChannelsRequestTypeDef]
    ) -> ListCollaborationMLInputChannelsResponseTypeDef:
        """
        Returns a list of the ML input channels in a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/list_collaboration_ml_input_channels.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#list_collaboration_ml_input_channels)
        """

    def list_collaboration_trained_model_export_jobs(
        self, **kwargs: Unpack[ListCollaborationTrainedModelExportJobsRequestTypeDef]
    ) -> ListCollaborationTrainedModelExportJobsResponseTypeDef:
        """
        Returns a list of the export jobs for a trained model in a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/list_collaboration_trained_model_export_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#list_collaboration_trained_model_export_jobs)
        """

    def list_collaboration_trained_model_inference_jobs(
        self, **kwargs: Unpack[ListCollaborationTrainedModelInferenceJobsRequestTypeDef]
    ) -> ListCollaborationTrainedModelInferenceJobsResponseTypeDef:
        """
        Returns a list of trained model inference jobs in a specified collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/list_collaboration_trained_model_inference_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#list_collaboration_trained_model_inference_jobs)
        """

    def list_collaboration_trained_models(
        self, **kwargs: Unpack[ListCollaborationTrainedModelsRequestTypeDef]
    ) -> ListCollaborationTrainedModelsResponseTypeDef:
        """
        Returns a list of the trained models in a collaboration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/list_collaboration_trained_models.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#list_collaboration_trained_models)
        """

    def list_configured_audience_models(
        self, **kwargs: Unpack[ListConfiguredAudienceModelsRequestTypeDef]
    ) -> ListConfiguredAudienceModelsResponseTypeDef:
        """
        Returns a list of the configured audience models.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/list_configured_audience_models.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#list_configured_audience_models)
        """

    def list_configured_model_algorithm_associations(
        self, **kwargs: Unpack[ListConfiguredModelAlgorithmAssociationsRequestTypeDef]
    ) -> ListConfiguredModelAlgorithmAssociationsResponseTypeDef:
        """
        Returns a list of configured model algorithm associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/list_configured_model_algorithm_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#list_configured_model_algorithm_associations)
        """

    def list_configured_model_algorithms(
        self, **kwargs: Unpack[ListConfiguredModelAlgorithmsRequestTypeDef]
    ) -> ListConfiguredModelAlgorithmsResponseTypeDef:
        """
        Returns a list of configured model algorithms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/list_configured_model_algorithms.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#list_configured_model_algorithms)
        """

    def list_ml_input_channels(
        self, **kwargs: Unpack[ListMLInputChannelsRequestTypeDef]
    ) -> ListMLInputChannelsResponseTypeDef:
        """
        Returns a list of ML input channels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/list_ml_input_channels.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#list_ml_input_channels)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags for a provided resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#list_tags_for_resource)
        """

    def list_trained_model_inference_jobs(
        self, **kwargs: Unpack[ListTrainedModelInferenceJobsRequestTypeDef]
    ) -> ListTrainedModelInferenceJobsResponseTypeDef:
        """
        Returns a list of trained model inference jobs that match the request
        parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/list_trained_model_inference_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#list_trained_model_inference_jobs)
        """

    def list_trained_models(
        self, **kwargs: Unpack[ListTrainedModelsRequestTypeDef]
    ) -> ListTrainedModelsResponseTypeDef:
        """
        Returns a list of trained models.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/list_trained_models.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#list_trained_models)
        """

    def list_training_datasets(
        self, **kwargs: Unpack[ListTrainingDatasetsRequestTypeDef]
    ) -> ListTrainingDatasetsResponseTypeDef:
        """
        Returns a list of training datasets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/list_training_datasets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#list_training_datasets)
        """

    def put_configured_audience_model_policy(
        self, **kwargs: Unpack[PutConfiguredAudienceModelPolicyRequestTypeDef]
    ) -> PutConfiguredAudienceModelPolicyResponseTypeDef:
        """
        Create or update the resource policy for a configured audience model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/put_configured_audience_model_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#put_configured_audience_model_policy)
        """

    def put_ml_configuration(
        self, **kwargs: Unpack[PutMLConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Assigns information about an ML configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/put_ml_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#put_ml_configuration)
        """

    def start_audience_export_job(
        self, **kwargs: Unpack[StartAudienceExportJobRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Export an audience of a specified size after you have generated an audience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/start_audience_export_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#start_audience_export_job)
        """

    def start_audience_generation_job(
        self, **kwargs: Unpack[StartAudienceGenerationJobRequestTypeDef]
    ) -> StartAudienceGenerationJobResponseTypeDef:
        """
        Information necessary to start the audience generation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/start_audience_generation_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#start_audience_generation_job)
        """

    def start_trained_model_export_job(
        self, **kwargs: Unpack[StartTrainedModelExportJobRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Provides the information necessary to start a trained model export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/start_trained_model_export_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#start_trained_model_export_job)
        """

    def start_trained_model_inference_job(
        self, **kwargs: Unpack[StartTrainedModelInferenceJobRequestTypeDef]
    ) -> StartTrainedModelInferenceJobResponseTypeDef:
        """
        Defines the information necessary to begin a trained model inference job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/start_trained_model_inference_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#start_trained_model_inference_job)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds metadata tags to a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes metadata tags from a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#untag_resource)
        """

    def update_configured_audience_model(
        self, **kwargs: Unpack[UpdateConfiguredAudienceModelRequestTypeDef]
    ) -> UpdateConfiguredAudienceModelResponseTypeDef:
        """
        Provides the information necessary to update a configured audience model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/update_configured_audience_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#update_configured_audience_model)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_audience_export_jobs"]
    ) -> ListAudienceExportJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_audience_generation_jobs"]
    ) -> ListAudienceGenerationJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_audience_models"]
    ) -> ListAudienceModelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_collaboration_configured_model_algorithm_associations"]
    ) -> ListCollaborationConfiguredModelAlgorithmAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_collaboration_ml_input_channels"]
    ) -> ListCollaborationMLInputChannelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_collaboration_trained_model_export_jobs"]
    ) -> ListCollaborationTrainedModelExportJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_collaboration_trained_model_inference_jobs"]
    ) -> ListCollaborationTrainedModelInferenceJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_collaboration_trained_models"]
    ) -> ListCollaborationTrainedModelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_configured_audience_models"]
    ) -> ListConfiguredAudienceModelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_configured_model_algorithm_associations"]
    ) -> ListConfiguredModelAlgorithmAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_configured_model_algorithms"]
    ) -> ListConfiguredModelAlgorithmsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_ml_input_channels"]
    ) -> ListMLInputChannelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_trained_model_inference_jobs"]
    ) -> ListTrainedModelInferenceJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_trained_models"]
    ) -> ListTrainedModelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_training_datasets"]
    ) -> ListTrainingDatasetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_paginator)
        """
