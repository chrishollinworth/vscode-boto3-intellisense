"""
Type annotations for mediaconvert service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_mediaconvert import MediaConvertClient
    from mypy_boto3_mediaconvert.paginator import (
        DescribeEndpointsPaginator,
        ListJobTemplatesPaginator,
        ListJobsPaginator,
        ListPresetsPaginator,
        ListQueuesPaginator,
        SearchJobsPaginator,
    )

    client: MediaConvertClient = boto3.client("mediaconvert")

    describe_endpoints_paginator: DescribeEndpointsPaginator = client.get_paginator("describe_endpoints")
    list_job_templates_paginator: ListJobTemplatesPaginator = client.get_paginator("list_job_templates")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    list_presets_paginator: ListPresetsPaginator = client.get_paginator("list_presets")
    list_queues_paginator: ListQueuesPaginator = client.get_paginator("list_queues")
    search_jobs_paginator: SearchJobsPaginator = client.get_paginator("search_jobs")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    DescribeEndpointsModeType,
    JobStatusType,
    JobTemplateListByType,
    OrderType,
    PresetListByType,
    QueueListByType,
)
from .type_defs import (
    DescribeEndpointsResponseTypeDef,
    ListJobsResponseTypeDef,
    ListJobTemplatesResponseTypeDef,
    ListPresetsResponseTypeDef,
    ListQueuesResponseTypeDef,
    PaginatorConfigTypeDef,
    SearchJobsResponseTypeDef,
)

__all__ = (
    "DescribeEndpointsPaginator",
    "ListJobTemplatesPaginator",
    "ListJobsPaginator",
    "ListPresetsPaginator",
    "ListQueuesPaginator",
    "SearchJobsPaginator",
)

class DescribeEndpointsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconvert.html#MediaConvert.Paginator.DescribeEndpoints)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators.html#describeendpointspaginator)
    """

    def paginate(
        self,
        *,
        Mode: DescribeEndpointsModeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEndpointsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconvert.html#MediaConvert.Paginator.DescribeEndpoints.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators.html#describeendpointspaginator)
        """

class ListJobTemplatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconvert.html#MediaConvert.Paginator.ListJobTemplates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators.html#listjobtemplatespaginator)
    """

    def paginate(
        self,
        *,
        Category: str = None,
        ListBy: JobTemplateListByType = None,
        Order: OrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconvert.html#MediaConvert.Paginator.ListJobTemplates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators.html#listjobtemplatespaginator)
        """

class ListJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconvert.html#MediaConvert.Paginator.ListJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators.html#listjobspaginator)
    """

    def paginate(
        self,
        *,
        Order: OrderType = None,
        Queue: str = None,
        Status: JobStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconvert.html#MediaConvert.Paginator.ListJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators.html#listjobspaginator)
        """

class ListPresetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconvert.html#MediaConvert.Paginator.ListPresets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators.html#listpresetspaginator)
    """

    def paginate(
        self,
        *,
        Category: str = None,
        ListBy: PresetListByType = None,
        Order: OrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPresetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconvert.html#MediaConvert.Paginator.ListPresets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators.html#listpresetspaginator)
        """

class ListQueuesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconvert.html#MediaConvert.Paginator.ListQueues)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators.html#listqueuespaginator)
    """

    def paginate(
        self,
        *,
        ListBy: QueueListByType = None,
        Order: OrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListQueuesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconvert.html#MediaConvert.Paginator.ListQueues.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators.html#listqueuespaginator)
        """

class SearchJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconvert.html#MediaConvert.Paginator.SearchJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators.html#searchjobspaginator)
    """

    def paginate(
        self,
        *,
        InputFile: str = None,
        Order: OrderType = None,
        Queue: str = None,
        Status: JobStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediaconvert.html#MediaConvert.Paginator.SearchJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/paginators.html#searchjobspaginator)
        """
