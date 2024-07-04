"""
Type annotations for cleanroomsml service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_cleanroomsml import CleanRoomsMLClient
    from mypy_boto3_cleanroomsml.paginator import (
        ListAudienceExportJobsPaginator,
        ListAudienceGenerationJobsPaginator,
        ListAudienceModelsPaginator,
        ListConfiguredAudienceModelsPaginator,
        ListTrainingDatasetsPaginator,
    )

    client: CleanRoomsMLClient = boto3.client("cleanroomsml")

    list_audience_export_jobs_paginator: ListAudienceExportJobsPaginator = client.get_paginator("list_audience_export_jobs")
    list_audience_generation_jobs_paginator: ListAudienceGenerationJobsPaginator = client.get_paginator("list_audience_generation_jobs")
    list_audience_models_paginator: ListAudienceModelsPaginator = client.get_paginator("list_audience_models")
    list_configured_audience_models_paginator: ListConfiguredAudienceModelsPaginator = client.get_paginator("list_configured_audience_models")
    list_training_datasets_paginator: ListTrainingDatasetsPaginator = client.get_paginator("list_training_datasets")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListAudienceExportJobsResponseTypeDef,
    ListAudienceGenerationJobsResponseTypeDef,
    ListAudienceModelsResponseTypeDef,
    ListConfiguredAudienceModelsResponseTypeDef,
    ListTrainingDatasetsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListAudienceExportJobsPaginator",
    "ListAudienceGenerationJobsPaginator",
    "ListAudienceModelsPaginator",
    "ListConfiguredAudienceModelsPaginator",
    "ListTrainingDatasetsPaginator",
)

class ListAudienceExportJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListAudienceExportJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators.html#listaudienceexportjobspaginator)
    """

    def paginate(
        self,
        *,
        audienceGenerationJobArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAudienceExportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListAudienceExportJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators.html#listaudienceexportjobspaginator)
        """

class ListAudienceGenerationJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListAudienceGenerationJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators.html#listaudiencegenerationjobspaginator)
    """

    def paginate(
        self,
        *,
        collaborationId: str = None,
        configuredAudienceModelArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAudienceGenerationJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListAudienceGenerationJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators.html#listaudiencegenerationjobspaginator)
        """

class ListAudienceModelsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListAudienceModels)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators.html#listaudiencemodelspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAudienceModelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListAudienceModels.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators.html#listaudiencemodelspaginator)
        """

class ListConfiguredAudienceModelsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListConfiguredAudienceModels)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators.html#listconfiguredaudiencemodelspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConfiguredAudienceModelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListConfiguredAudienceModels.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators.html#listconfiguredaudiencemodelspaginator)
        """

class ListTrainingDatasetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListTrainingDatasets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators.html#listtrainingdatasetspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTrainingDatasetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListTrainingDatasets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators.html#listtrainingdatasetspaginator)
        """
