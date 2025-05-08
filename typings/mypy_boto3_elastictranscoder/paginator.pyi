"""
Type annotations for elastictranscoder service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_elastictranscoder.client import ElasticTranscoderClient
    from mypy_boto3_elastictranscoder.paginator import (
        ListJobsByPipelinePaginator,
        ListJobsByStatusPaginator,
        ListPipelinesPaginator,
        ListPresetsPaginator,
    )

    session = Session()
    client: ElasticTranscoderClient = session.client("elastictranscoder")

    list_jobs_by_pipeline_paginator: ListJobsByPipelinePaginator = client.get_paginator("list_jobs_by_pipeline")
    list_jobs_by_status_paginator: ListJobsByStatusPaginator = client.get_paginator("list_jobs_by_status")
    list_pipelines_paginator: ListPipelinesPaginator = client.get_paginator("list_pipelines")
    list_presets_paginator: ListPresetsPaginator = client.get_paginator("list_presets")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListJobsByPipelineRequestPaginateTypeDef,
    ListJobsByPipelineResponseTypeDef,
    ListJobsByStatusRequestPaginateTypeDef,
    ListJobsByStatusResponseTypeDef,
    ListPipelinesRequestPaginateTypeDef,
    ListPipelinesResponseTypeDef,
    ListPresetsRequestPaginateTypeDef,
    ListPresetsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListJobsByPipelinePaginator",
    "ListJobsByStatusPaginator",
    "ListPipelinesPaginator",
    "ListPresetsPaginator",
)

if TYPE_CHECKING:
    _ListJobsByPipelinePaginatorBase = Paginator[ListJobsByPipelineResponseTypeDef]
else:
    _ListJobsByPipelinePaginatorBase = Paginator  # type: ignore[assignment]

class ListJobsByPipelinePaginator(_ListJobsByPipelinePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder/paginator/ListJobsByPipeline.html#ElasticTranscoder.Paginator.ListJobsByPipeline)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/paginators/#listjobsbypipelinepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListJobsByPipelineRequestPaginateTypeDef]
    ) -> PageIterator[ListJobsByPipelineResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder/paginator/ListJobsByPipeline.html#ElasticTranscoder.Paginator.ListJobsByPipeline.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/paginators/#listjobsbypipelinepaginator)
        """

if TYPE_CHECKING:
    _ListJobsByStatusPaginatorBase = Paginator[ListJobsByStatusResponseTypeDef]
else:
    _ListJobsByStatusPaginatorBase = Paginator  # type: ignore[assignment]

class ListJobsByStatusPaginator(_ListJobsByStatusPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder/paginator/ListJobsByStatus.html#ElasticTranscoder.Paginator.ListJobsByStatus)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/paginators/#listjobsbystatuspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListJobsByStatusRequestPaginateTypeDef]
    ) -> PageIterator[ListJobsByStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder/paginator/ListJobsByStatus.html#ElasticTranscoder.Paginator.ListJobsByStatus.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/paginators/#listjobsbystatuspaginator)
        """

if TYPE_CHECKING:
    _ListPipelinesPaginatorBase = Paginator[ListPipelinesResponseTypeDef]
else:
    _ListPipelinesPaginatorBase = Paginator  # type: ignore[assignment]

class ListPipelinesPaginator(_ListPipelinesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder/paginator/ListPipelines.html#ElasticTranscoder.Paginator.ListPipelines)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/paginators/#listpipelinespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPipelinesRequestPaginateTypeDef]
    ) -> PageIterator[ListPipelinesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder/paginator/ListPipelines.html#ElasticTranscoder.Paginator.ListPipelines.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/paginators/#listpipelinespaginator)
        """

if TYPE_CHECKING:
    _ListPresetsPaginatorBase = Paginator[ListPresetsResponseTypeDef]
else:
    _ListPresetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPresetsPaginator(_ListPresetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder/paginator/ListPresets.html#ElasticTranscoder.Paginator.ListPresets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/paginators/#listpresetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPresetsRequestPaginateTypeDef]
    ) -> PageIterator[ListPresetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder/paginator/ListPresets.html#ElasticTranscoder.Paginator.ListPresets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/paginators/#listpresetspaginator)
        """
