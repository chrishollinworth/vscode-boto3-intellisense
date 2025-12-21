"""
Main interface for cleanroomsml service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cleanroomsml import (
        CleanRoomsMLClient,
        Client,
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
        ListTrainedModelVersionsPaginator,
        ListTrainedModelsPaginator,
        ListTrainingDatasetsPaginator,
    )

    session = Session()
    client: CleanRoomsMLClient = session.client("cleanroomsml")

    list_audience_export_jobs_paginator: ListAudienceExportJobsPaginator = client.get_paginator("list_audience_export_jobs")
    list_audience_generation_jobs_paginator: ListAudienceGenerationJobsPaginator = client.get_paginator("list_audience_generation_jobs")
    list_audience_models_paginator: ListAudienceModelsPaginator = client.get_paginator("list_audience_models")
    list_collaboration_configured_model_algorithm_associations_paginator: ListCollaborationConfiguredModelAlgorithmAssociationsPaginator = client.get_paginator("list_collaboration_configured_model_algorithm_associations")
    list_collaboration_ml_input_channels_paginator: ListCollaborationMLInputChannelsPaginator = client.get_paginator("list_collaboration_ml_input_channels")
    list_collaboration_trained_model_export_jobs_paginator: ListCollaborationTrainedModelExportJobsPaginator = client.get_paginator("list_collaboration_trained_model_export_jobs")
    list_collaboration_trained_model_inference_jobs_paginator: ListCollaborationTrainedModelInferenceJobsPaginator = client.get_paginator("list_collaboration_trained_model_inference_jobs")
    list_collaboration_trained_models_paginator: ListCollaborationTrainedModelsPaginator = client.get_paginator("list_collaboration_trained_models")
    list_configured_audience_models_paginator: ListConfiguredAudienceModelsPaginator = client.get_paginator("list_configured_audience_models")
    list_configured_model_algorithm_associations_paginator: ListConfiguredModelAlgorithmAssociationsPaginator = client.get_paginator("list_configured_model_algorithm_associations")
    list_configured_model_algorithms_paginator: ListConfiguredModelAlgorithmsPaginator = client.get_paginator("list_configured_model_algorithms")
    list_ml_input_channels_paginator: ListMLInputChannelsPaginator = client.get_paginator("list_ml_input_channels")
    list_trained_model_inference_jobs_paginator: ListTrainedModelInferenceJobsPaginator = client.get_paginator("list_trained_model_inference_jobs")
    list_trained_model_versions_paginator: ListTrainedModelVersionsPaginator = client.get_paginator("list_trained_model_versions")
    list_trained_models_paginator: ListTrainedModelsPaginator = client.get_paginator("list_trained_models")
    list_training_datasets_paginator: ListTrainingDatasetsPaginator = client.get_paginator("list_training_datasets")
    ```
"""

from .client import CleanRoomsMLClient
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
    ListTrainedModelVersionsPaginator,
    ListTrainingDatasetsPaginator,
)

Client = CleanRoomsMLClient

__all__ = (
    "CleanRoomsMLClient",
    "Client",
    "ListAudienceExportJobsPaginator",
    "ListAudienceGenerationJobsPaginator",
    "ListAudienceModelsPaginator",
    "ListCollaborationConfiguredModelAlgorithmAssociationsPaginator",
    "ListCollaborationMLInputChannelsPaginator",
    "ListCollaborationTrainedModelExportJobsPaginator",
    "ListCollaborationTrainedModelInferenceJobsPaginator",
    "ListCollaborationTrainedModelsPaginator",
    "ListConfiguredAudienceModelsPaginator",
    "ListConfiguredModelAlgorithmAssociationsPaginator",
    "ListConfiguredModelAlgorithmsPaginator",
    "ListMLInputChannelsPaginator",
    "ListTrainedModelInferenceJobsPaginator",
    "ListTrainedModelVersionsPaginator",
    "ListTrainedModelsPaginator",
    "ListTrainingDatasetsPaginator",
)
