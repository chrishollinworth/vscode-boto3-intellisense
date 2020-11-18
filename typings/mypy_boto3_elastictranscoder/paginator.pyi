# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for elastictranscoder service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_elastictranscoder import ElasticTranscoderClient
    from mypy_boto3_elastictranscoder.paginator import (
        ListJobsByPipelinePaginator,
        ListJobsByStatusPaginator,
        ListPipelinesPaginator,
        ListPresetsPaginator,
    )

    client: ElasticTranscoderClient = boto3.client("elastictranscoder")

    list_jobs_by_pipeline_paginator: ListJobsByPipelinePaginator = client.get_paginator("list_jobs_by_pipeline")
    list_jobs_by_status_paginator: ListJobsByStatusPaginator = client.get_paginator("list_jobs_by_status")
    list_pipelines_paginator: ListPipelinesPaginator = client.get_paginator("list_pipelines")
    list_presets_paginator: ListPresetsPaginator = client.get_paginator("list_presets")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_elastictranscoder.type_defs import (
    ListJobsByPipelineResponseTypeDef,
    ListJobsByStatusResponseTypeDef,
    ListPipelinesResponseTypeDef,
    ListPresetsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListJobsByPipelinePaginator",
    "ListJobsByStatusPaginator",
    "ListPipelinesPaginator",
    "ListPresetsPaginator",
)


class ListJobsByPipelinePaginator(Boto3Paginator):
    """
    [Paginator.ListJobsByPipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByPipeline)
    """

    def paginate(
        self,
        PipelineId: str,
        Ascending: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListJobsByPipelineResponseTypeDef]:
        """
        [ListJobsByPipeline.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByPipeline.paginate)
        """


class ListJobsByStatusPaginator(Boto3Paginator):
    """
    [Paginator.ListJobsByStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByStatus)
    """

    def paginate(
        self, Status: str, Ascending: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobsByStatusResponseTypeDef]:
        """
        [ListJobsByStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByStatus.paginate)
        """


class ListPipelinesPaginator(Boto3Paginator):
    """
    [Paginator.ListPipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPipelines)
    """

    def paginate(
        self, Ascending: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPipelinesResponseTypeDef]:
        """
        [ListPipelines.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPipelines.paginate)
        """


class ListPresetsPaginator(Boto3Paginator):
    """
    [Paginator.ListPresets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPresets)
    """

    def paginate(
        self, Ascending: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPresetsResponseTypeDef]:
        """
        [ListPresets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPresets.paginate)
        """
