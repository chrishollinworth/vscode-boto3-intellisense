"""
Type annotations for cleanroomsml service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_cleanroomsml.client import CleanRoomsMLClient
    from mypy_boto3_cleanroomsml.paginator import (
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
    list_trained_models_paginator: ListTrainedModelsPaginator = client.get_paginator("list_trained_models")
    list_training_datasets_paginator: ListTrainingDatasetsPaginator = client.get_paginator("list_training_datasets")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAudienceExportJobsRequestPaginateTypeDef,
    ListAudienceExportJobsResponseTypeDef,
    ListAudienceGenerationJobsRequestPaginateTypeDef,
    ListAudienceGenerationJobsResponseTypeDef,
    ListAudienceModelsRequestPaginateTypeDef,
    ListAudienceModelsResponseTypeDef,
    ListCollaborationConfiguredModelAlgorithmAssociationsRequestPaginateTypeDef,
    ListCollaborationConfiguredModelAlgorithmAssociationsResponseTypeDef,
    ListCollaborationMLInputChannelsRequestPaginateTypeDef,
    ListCollaborationMLInputChannelsResponseTypeDef,
    ListCollaborationTrainedModelExportJobsRequestPaginateTypeDef,
    ListCollaborationTrainedModelExportJobsResponseTypeDef,
    ListCollaborationTrainedModelInferenceJobsRequestPaginateTypeDef,
    ListCollaborationTrainedModelInferenceJobsResponseTypeDef,
    ListCollaborationTrainedModelsRequestPaginateTypeDef,
    ListCollaborationTrainedModelsResponseTypeDef,
    ListConfiguredAudienceModelsRequestPaginateTypeDef,
    ListConfiguredAudienceModelsResponseTypeDef,
    ListConfiguredModelAlgorithmAssociationsRequestPaginateTypeDef,
    ListConfiguredModelAlgorithmAssociationsResponseTypeDef,
    ListConfiguredModelAlgorithmsRequestPaginateTypeDef,
    ListConfiguredModelAlgorithmsResponseTypeDef,
    ListMLInputChannelsRequestPaginateTypeDef,
    ListMLInputChannelsResponseTypeDef,
    ListTrainedModelInferenceJobsRequestPaginateTypeDef,
    ListTrainedModelInferenceJobsResponseTypeDef,
    ListTrainedModelsRequestPaginateTypeDef,
    ListTrainedModelsResponseTypeDef,
    ListTrainingDatasetsRequestPaginateTypeDef,
    ListTrainingDatasetsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
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
    "ListTrainedModelsPaginator",
    "ListTrainingDatasetsPaginator",
)

if TYPE_CHECKING:
    _ListAudienceExportJobsPaginatorBase = Paginator[ListAudienceExportJobsResponseTypeDef]
else:
    _ListAudienceExportJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAudienceExportJobsPaginator(_ListAudienceExportJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListAudienceExportJobs.html#CleanRoomsML.Paginator.ListAudienceExportJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listaudienceexportjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAudienceExportJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListAudienceExportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListAudienceExportJobs.html#CleanRoomsML.Paginator.ListAudienceExportJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listaudienceexportjobspaginator)
        """

if TYPE_CHECKING:
    _ListAudienceGenerationJobsPaginatorBase = Paginator[ListAudienceGenerationJobsResponseTypeDef]
else:
    _ListAudienceGenerationJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAudienceGenerationJobsPaginator(_ListAudienceGenerationJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListAudienceGenerationJobs.html#CleanRoomsML.Paginator.ListAudienceGenerationJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listaudiencegenerationjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAudienceGenerationJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListAudienceGenerationJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListAudienceGenerationJobs.html#CleanRoomsML.Paginator.ListAudienceGenerationJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listaudiencegenerationjobspaginator)
        """

if TYPE_CHECKING:
    _ListAudienceModelsPaginatorBase = Paginator[ListAudienceModelsResponseTypeDef]
else:
    _ListAudienceModelsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAudienceModelsPaginator(_ListAudienceModelsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListAudienceModels.html#CleanRoomsML.Paginator.ListAudienceModels)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listaudiencemodelspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAudienceModelsRequestPaginateTypeDef]
    ) -> PageIterator[ListAudienceModelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListAudienceModels.html#CleanRoomsML.Paginator.ListAudienceModels.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listaudiencemodelspaginator)
        """

if TYPE_CHECKING:
    _ListCollaborationConfiguredModelAlgorithmAssociationsPaginatorBase = Paginator[
        ListCollaborationConfiguredModelAlgorithmAssociationsResponseTypeDef
    ]
else:
    _ListCollaborationConfiguredModelAlgorithmAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCollaborationConfiguredModelAlgorithmAssociationsPaginator(
    _ListCollaborationConfiguredModelAlgorithmAssociationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListCollaborationConfiguredModelAlgorithmAssociations.html#CleanRoomsML.Paginator.ListCollaborationConfiguredModelAlgorithmAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listcollaborationconfiguredmodelalgorithmassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self,
        **kwargs: Unpack[
            ListCollaborationConfiguredModelAlgorithmAssociationsRequestPaginateTypeDef
        ],
    ) -> PageIterator[ListCollaborationConfiguredModelAlgorithmAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListCollaborationConfiguredModelAlgorithmAssociations.html#CleanRoomsML.Paginator.ListCollaborationConfiguredModelAlgorithmAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listcollaborationconfiguredmodelalgorithmassociationspaginator)
        """

if TYPE_CHECKING:
    _ListCollaborationMLInputChannelsPaginatorBase = Paginator[
        ListCollaborationMLInputChannelsResponseTypeDef
    ]
else:
    _ListCollaborationMLInputChannelsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCollaborationMLInputChannelsPaginator(_ListCollaborationMLInputChannelsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListCollaborationMLInputChannels.html#CleanRoomsML.Paginator.ListCollaborationMLInputChannels)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listcollaborationmlinputchannelspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCollaborationMLInputChannelsRequestPaginateTypeDef]
    ) -> PageIterator[ListCollaborationMLInputChannelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListCollaborationMLInputChannels.html#CleanRoomsML.Paginator.ListCollaborationMLInputChannels.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listcollaborationmlinputchannelspaginator)
        """

if TYPE_CHECKING:
    _ListCollaborationTrainedModelExportJobsPaginatorBase = Paginator[
        ListCollaborationTrainedModelExportJobsResponseTypeDef
    ]
else:
    _ListCollaborationTrainedModelExportJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCollaborationTrainedModelExportJobsPaginator(
    _ListCollaborationTrainedModelExportJobsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListCollaborationTrainedModelExportJobs.html#CleanRoomsML.Paginator.ListCollaborationTrainedModelExportJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listcollaborationtrainedmodelexportjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCollaborationTrainedModelExportJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListCollaborationTrainedModelExportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListCollaborationTrainedModelExportJobs.html#CleanRoomsML.Paginator.ListCollaborationTrainedModelExportJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listcollaborationtrainedmodelexportjobspaginator)
        """

if TYPE_CHECKING:
    _ListCollaborationTrainedModelInferenceJobsPaginatorBase = Paginator[
        ListCollaborationTrainedModelInferenceJobsResponseTypeDef
    ]
else:
    _ListCollaborationTrainedModelInferenceJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCollaborationTrainedModelInferenceJobsPaginator(
    _ListCollaborationTrainedModelInferenceJobsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListCollaborationTrainedModelInferenceJobs.html#CleanRoomsML.Paginator.ListCollaborationTrainedModelInferenceJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listcollaborationtrainedmodelinferencejobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCollaborationTrainedModelInferenceJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListCollaborationTrainedModelInferenceJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListCollaborationTrainedModelInferenceJobs.html#CleanRoomsML.Paginator.ListCollaborationTrainedModelInferenceJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listcollaborationtrainedmodelinferencejobspaginator)
        """

if TYPE_CHECKING:
    _ListCollaborationTrainedModelsPaginatorBase = Paginator[
        ListCollaborationTrainedModelsResponseTypeDef
    ]
else:
    _ListCollaborationTrainedModelsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCollaborationTrainedModelsPaginator(_ListCollaborationTrainedModelsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListCollaborationTrainedModels.html#CleanRoomsML.Paginator.ListCollaborationTrainedModels)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listcollaborationtrainedmodelspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCollaborationTrainedModelsRequestPaginateTypeDef]
    ) -> PageIterator[ListCollaborationTrainedModelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListCollaborationTrainedModels.html#CleanRoomsML.Paginator.ListCollaborationTrainedModels.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listcollaborationtrainedmodelspaginator)
        """

if TYPE_CHECKING:
    _ListConfiguredAudienceModelsPaginatorBase = Paginator[
        ListConfiguredAudienceModelsResponseTypeDef
    ]
else:
    _ListConfiguredAudienceModelsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConfiguredAudienceModelsPaginator(_ListConfiguredAudienceModelsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListConfiguredAudienceModels.html#CleanRoomsML.Paginator.ListConfiguredAudienceModels)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listconfiguredaudiencemodelspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConfiguredAudienceModelsRequestPaginateTypeDef]
    ) -> PageIterator[ListConfiguredAudienceModelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListConfiguredAudienceModels.html#CleanRoomsML.Paginator.ListConfiguredAudienceModels.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listconfiguredaudiencemodelspaginator)
        """

if TYPE_CHECKING:
    _ListConfiguredModelAlgorithmAssociationsPaginatorBase = Paginator[
        ListConfiguredModelAlgorithmAssociationsResponseTypeDef
    ]
else:
    _ListConfiguredModelAlgorithmAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConfiguredModelAlgorithmAssociationsPaginator(
    _ListConfiguredModelAlgorithmAssociationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListConfiguredModelAlgorithmAssociations.html#CleanRoomsML.Paginator.ListConfiguredModelAlgorithmAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listconfiguredmodelalgorithmassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConfiguredModelAlgorithmAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListConfiguredModelAlgorithmAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListConfiguredModelAlgorithmAssociations.html#CleanRoomsML.Paginator.ListConfiguredModelAlgorithmAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listconfiguredmodelalgorithmassociationspaginator)
        """

if TYPE_CHECKING:
    _ListConfiguredModelAlgorithmsPaginatorBase = Paginator[
        ListConfiguredModelAlgorithmsResponseTypeDef
    ]
else:
    _ListConfiguredModelAlgorithmsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConfiguredModelAlgorithmsPaginator(_ListConfiguredModelAlgorithmsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListConfiguredModelAlgorithms.html#CleanRoomsML.Paginator.ListConfiguredModelAlgorithms)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listconfiguredmodelalgorithmspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConfiguredModelAlgorithmsRequestPaginateTypeDef]
    ) -> PageIterator[ListConfiguredModelAlgorithmsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListConfiguredModelAlgorithms.html#CleanRoomsML.Paginator.ListConfiguredModelAlgorithms.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listconfiguredmodelalgorithmspaginator)
        """

if TYPE_CHECKING:
    _ListMLInputChannelsPaginatorBase = Paginator[ListMLInputChannelsResponseTypeDef]
else:
    _ListMLInputChannelsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMLInputChannelsPaginator(_ListMLInputChannelsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListMLInputChannels.html#CleanRoomsML.Paginator.ListMLInputChannels)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listmlinputchannelspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMLInputChannelsRequestPaginateTypeDef]
    ) -> PageIterator[ListMLInputChannelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListMLInputChannels.html#CleanRoomsML.Paginator.ListMLInputChannels.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listmlinputchannelspaginator)
        """

if TYPE_CHECKING:
    _ListTrainedModelInferenceJobsPaginatorBase = Paginator[
        ListTrainedModelInferenceJobsResponseTypeDef
    ]
else:
    _ListTrainedModelInferenceJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTrainedModelInferenceJobsPaginator(_ListTrainedModelInferenceJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListTrainedModelInferenceJobs.html#CleanRoomsML.Paginator.ListTrainedModelInferenceJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listtrainedmodelinferencejobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTrainedModelInferenceJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListTrainedModelInferenceJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListTrainedModelInferenceJobs.html#CleanRoomsML.Paginator.ListTrainedModelInferenceJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listtrainedmodelinferencejobspaginator)
        """

if TYPE_CHECKING:
    _ListTrainedModelsPaginatorBase = Paginator[ListTrainedModelsResponseTypeDef]
else:
    _ListTrainedModelsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTrainedModelsPaginator(_ListTrainedModelsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListTrainedModels.html#CleanRoomsML.Paginator.ListTrainedModels)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listtrainedmodelspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTrainedModelsRequestPaginateTypeDef]
    ) -> PageIterator[ListTrainedModelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListTrainedModels.html#CleanRoomsML.Paginator.ListTrainedModels.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listtrainedmodelspaginator)
        """

if TYPE_CHECKING:
    _ListTrainingDatasetsPaginatorBase = Paginator[ListTrainingDatasetsResponseTypeDef]
else:
    _ListTrainingDatasetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTrainingDatasetsPaginator(_ListTrainingDatasetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListTrainingDatasets.html#CleanRoomsML.Paginator.ListTrainingDatasets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listtrainingdatasetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTrainingDatasetsRequestPaginateTypeDef]
    ) -> PageIterator[ListTrainingDatasetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml/paginator/ListTrainingDatasets.html#CleanRoomsML.Paginator.ListTrainingDatasets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listtrainingdatasetspaginator)
        """
