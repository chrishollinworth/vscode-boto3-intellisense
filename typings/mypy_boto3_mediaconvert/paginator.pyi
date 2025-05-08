"""
Type annotations for mediaconvert service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_mediaconvert.client import MediaConvertClient
    from mypy_boto3_mediaconvert.paginator import (
        DescribeEndpointsPaginator,
        ListJobTemplatesPaginator,
        ListJobsPaginator,
        ListPresetsPaginator,
        ListQueuesPaginator,
        ListVersionsPaginator,
        SearchJobsPaginator,
    )

    session = Session()
    client: MediaConvertClient = session.client("mediaconvert")

    describe_endpoints_paginator: DescribeEndpointsPaginator = client.get_paginator("describe_endpoints")
    list_job_templates_paginator: ListJobTemplatesPaginator = client.get_paginator("list_job_templates")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    list_presets_paginator: ListPresetsPaginator = client.get_paginator("list_presets")
    list_queues_paginator: ListQueuesPaginator = client.get_paginator("list_queues")
    list_versions_paginator: ListVersionsPaginator = client.get_paginator("list_versions")
    search_jobs_paginator: SearchJobsPaginator = client.get_paginator("search_jobs")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeEndpointsRequestPaginateTypeDef,
    DescribeEndpointsResponseTypeDef,
    ListJobsRequestPaginateTypeDef,
    ListJobsResponseTypeDef,
    ListJobTemplatesRequestPaginateTypeDef,
    ListJobTemplatesResponseTypeDef,
    ListPresetsRequestPaginateTypeDef,
    ListPresetsResponseTypeDef,
    ListQueuesRequestPaginateTypeDef,
    ListQueuesResponseTypeDef,
    ListVersionsRequestPaginateTypeDef,
    ListVersionsResponseTypeDef,
    SearchJobsRequestPaginateTypeDef,
    SearchJobsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeEndpointsPaginator",
    "ListJobTemplatesPaginator",
    "ListJobsPaginator",
    "ListPresetsPaginator",
    "ListQueuesPaginator",
    "ListVersionsPaginator",
    "SearchJobsPaginator",
)

if TYPE_CHECKING:
    _DescribeEndpointsPaginatorBase = Paginator[DescribeEndpointsResponseTypeDef]
else:
    _DescribeEndpointsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEndpointsPaginator(_DescribeEndpointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/paginator/DescribeEndpoints.html#MediaConvert.Paginator.DescribeEndpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators/#describeendpointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEndpointsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeEndpointsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/paginator/DescribeEndpoints.html#MediaConvert.Paginator.DescribeEndpoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators/#describeendpointspaginator)
        """

if TYPE_CHECKING:
    _ListJobTemplatesPaginatorBase = Paginator[ListJobTemplatesResponseTypeDef]
else:
    _ListJobTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListJobTemplatesPaginator(_ListJobTemplatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/paginator/ListJobTemplates.html#MediaConvert.Paginator.ListJobTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators/#listjobtemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListJobTemplatesRequestPaginateTypeDef]
    ) -> PageIterator[ListJobTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/paginator/ListJobTemplates.html#MediaConvert.Paginator.ListJobTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators/#listjobtemplatespaginator)
        """

if TYPE_CHECKING:
    _ListJobsPaginatorBase = Paginator[ListJobsResponseTypeDef]
else:
    _ListJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListJobsPaginator(_ListJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/paginator/ListJobs.html#MediaConvert.Paginator.ListJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators/#listjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/paginator/ListJobs.html#MediaConvert.Paginator.ListJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators/#listjobspaginator)
        """

if TYPE_CHECKING:
    _ListPresetsPaginatorBase = Paginator[ListPresetsResponseTypeDef]
else:
    _ListPresetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPresetsPaginator(_ListPresetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/paginator/ListPresets.html#MediaConvert.Paginator.ListPresets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators/#listpresetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPresetsRequestPaginateTypeDef]
    ) -> PageIterator[ListPresetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/paginator/ListPresets.html#MediaConvert.Paginator.ListPresets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators/#listpresetspaginator)
        """

if TYPE_CHECKING:
    _ListQueuesPaginatorBase = Paginator[ListQueuesResponseTypeDef]
else:
    _ListQueuesPaginatorBase = Paginator  # type: ignore[assignment]

class ListQueuesPaginator(_ListQueuesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/paginator/ListQueues.html#MediaConvert.Paginator.ListQueues)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators/#listqueuespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListQueuesRequestPaginateTypeDef]
    ) -> PageIterator[ListQueuesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/paginator/ListQueues.html#MediaConvert.Paginator.ListQueues.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators/#listqueuespaginator)
        """

if TYPE_CHECKING:
    _ListVersionsPaginatorBase = Paginator[ListVersionsResponseTypeDef]
else:
    _ListVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListVersionsPaginator(_ListVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/paginator/ListVersions.html#MediaConvert.Paginator.ListVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators/#listversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/paginator/ListVersions.html#MediaConvert.Paginator.ListVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators/#listversionspaginator)
        """

if TYPE_CHECKING:
    _SearchJobsPaginatorBase = Paginator[SearchJobsResponseTypeDef]
else:
    _SearchJobsPaginatorBase = Paginator  # type: ignore[assignment]

class SearchJobsPaginator(_SearchJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/paginator/SearchJobs.html#MediaConvert.Paginator.SearchJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators/#searchjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchJobsRequestPaginateTypeDef]
    ) -> PageIterator[SearchJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert/paginator/SearchJobs.html#MediaConvert.Paginator.SearchJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators/#searchjobspaginator)
        """
