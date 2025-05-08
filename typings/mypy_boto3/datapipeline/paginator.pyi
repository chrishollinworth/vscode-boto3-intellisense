"""
Type annotations for datapipeline service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_datapipeline.client import DataPipelineClient
    from mypy_boto3_datapipeline.paginator import (
        DescribeObjectsPaginator,
        ListPipelinesPaginator,
        QueryObjectsPaginator,
    )

    session = Session()
    client: DataPipelineClient = session.client("datapipeline")

    describe_objects_paginator: DescribeObjectsPaginator = client.get_paginator("describe_objects")
    list_pipelines_paginator: ListPipelinesPaginator = client.get_paginator("list_pipelines")
    query_objects_paginator: QueryObjectsPaginator = client.get_paginator("query_objects")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeObjectsInputPaginateTypeDef,
    DescribeObjectsOutputTypeDef,
    ListPipelinesInputPaginateTypeDef,
    ListPipelinesOutputTypeDef,
    QueryObjectsInputPaginateTypeDef,
    QueryObjectsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("DescribeObjectsPaginator", "ListPipelinesPaginator", "QueryObjectsPaginator")

if TYPE_CHECKING:
    _DescribeObjectsPaginatorBase = Paginator[DescribeObjectsOutputTypeDef]
else:
    _DescribeObjectsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeObjectsPaginator(_DescribeObjectsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/paginator/DescribeObjects.html#DataPipeline.Paginator.DescribeObjects)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/paginators/#describeobjectspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeObjectsInputPaginateTypeDef]
    ) -> PageIterator[DescribeObjectsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/paginator/DescribeObjects.html#DataPipeline.Paginator.DescribeObjects.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/paginators/#describeobjectspaginator)
        """

if TYPE_CHECKING:
    _ListPipelinesPaginatorBase = Paginator[ListPipelinesOutputTypeDef]
else:
    _ListPipelinesPaginatorBase = Paginator  # type: ignore[assignment]

class ListPipelinesPaginator(_ListPipelinesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/paginator/ListPipelines.html#DataPipeline.Paginator.ListPipelines)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/paginators/#listpipelinespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPipelinesInputPaginateTypeDef]
    ) -> PageIterator[ListPipelinesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/paginator/ListPipelines.html#DataPipeline.Paginator.ListPipelines.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/paginators/#listpipelinespaginator)
        """

if TYPE_CHECKING:
    _QueryObjectsPaginatorBase = Paginator[QueryObjectsOutputTypeDef]
else:
    _QueryObjectsPaginatorBase = Paginator  # type: ignore[assignment]

class QueryObjectsPaginator(_QueryObjectsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/paginator/QueryObjects.html#DataPipeline.Paginator.QueryObjects)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/paginators/#queryobjectspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[QueryObjectsInputPaginateTypeDef]
    ) -> PageIterator[QueryObjectsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/paginator/QueryObjects.html#DataPipeline.Paginator.QueryObjects.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/paginators/#queryobjectspaginator)
        """
