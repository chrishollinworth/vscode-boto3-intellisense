"""
Type annotations for bedrock-agentcore service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_bedrock_agentcore.client import BedrockAgentCoreClient
    from mypy_boto3_bedrock_agentcore.paginator import (
        ListActorsPaginator,
        ListEventsPaginator,
        ListMemoryExtractionJobsPaginator,
        ListMemoryRecordsPaginator,
        ListSessionsPaginator,
        RetrieveMemoryRecordsPaginator,
    )

    session = Session()
    client: BedrockAgentCoreClient = session.client("bedrock-agentcore")

    list_actors_paginator: ListActorsPaginator = client.get_paginator("list_actors")
    list_events_paginator: ListEventsPaginator = client.get_paginator("list_events")
    list_memory_extraction_jobs_paginator: ListMemoryExtractionJobsPaginator = client.get_paginator("list_memory_extraction_jobs")
    list_memory_records_paginator: ListMemoryRecordsPaginator = client.get_paginator("list_memory_records")
    list_sessions_paginator: ListSessionsPaginator = client.get_paginator("list_sessions")
    retrieve_memory_records_paginator: RetrieveMemoryRecordsPaginator = client.get_paginator("retrieve_memory_records")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListActorsInputPaginateTypeDef,
    ListActorsOutputTypeDef,
    ListEventsInputPaginateTypeDef,
    ListEventsOutputTypeDef,
    ListMemoryExtractionJobsInputPaginateTypeDef,
    ListMemoryExtractionJobsOutputTypeDef,
    ListMemoryRecordsInputPaginateTypeDef,
    ListMemoryRecordsOutputTypeDef,
    ListSessionsInputPaginateTypeDef,
    ListSessionsOutputTypeDef,
    RetrieveMemoryRecordsInputPaginateTypeDef,
    RetrieveMemoryRecordsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListActorsPaginator",
    "ListEventsPaginator",
    "ListMemoryExtractionJobsPaginator",
    "ListMemoryRecordsPaginator",
    "ListSessionsPaginator",
    "RetrieveMemoryRecordsPaginator",
)

if TYPE_CHECKING:
    _ListActorsPaginatorBase = Paginator[ListActorsOutputTypeDef]
else:
    _ListActorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListActorsPaginator(_ListActorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore/paginator/ListActors.html#BedrockAgentCore.Paginator.ListActors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore/paginators/#listactorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListActorsInputPaginateTypeDef]
    ) -> PageIterator[ListActorsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore/paginator/ListActors.html#BedrockAgentCore.Paginator.ListActors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore/paginators/#listactorspaginator)
        """

if TYPE_CHECKING:
    _ListEventsPaginatorBase = Paginator[ListEventsOutputTypeDef]
else:
    _ListEventsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEventsPaginator(_ListEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore/paginator/ListEvents.html#BedrockAgentCore.Paginator.ListEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore/paginators/#listeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEventsInputPaginateTypeDef]
    ) -> PageIterator[ListEventsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore/paginator/ListEvents.html#BedrockAgentCore.Paginator.ListEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore/paginators/#listeventspaginator)
        """

if TYPE_CHECKING:
    _ListMemoryExtractionJobsPaginatorBase = Paginator[ListMemoryExtractionJobsOutputTypeDef]
else:
    _ListMemoryExtractionJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMemoryExtractionJobsPaginator(_ListMemoryExtractionJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore/paginator/ListMemoryExtractionJobs.html#BedrockAgentCore.Paginator.ListMemoryExtractionJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore/paginators/#listmemoryextractionjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMemoryExtractionJobsInputPaginateTypeDef]
    ) -> PageIterator[ListMemoryExtractionJobsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore/paginator/ListMemoryExtractionJobs.html#BedrockAgentCore.Paginator.ListMemoryExtractionJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore/paginators/#listmemoryextractionjobspaginator)
        """

if TYPE_CHECKING:
    _ListMemoryRecordsPaginatorBase = Paginator[ListMemoryRecordsOutputTypeDef]
else:
    _ListMemoryRecordsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMemoryRecordsPaginator(_ListMemoryRecordsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore/paginator/ListMemoryRecords.html#BedrockAgentCore.Paginator.ListMemoryRecords)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore/paginators/#listmemoryrecordspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMemoryRecordsInputPaginateTypeDef]
    ) -> PageIterator[ListMemoryRecordsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore/paginator/ListMemoryRecords.html#BedrockAgentCore.Paginator.ListMemoryRecords.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore/paginators/#listmemoryrecordspaginator)
        """

if TYPE_CHECKING:
    _ListSessionsPaginatorBase = Paginator[ListSessionsOutputTypeDef]
else:
    _ListSessionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSessionsPaginator(_ListSessionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore/paginator/ListSessions.html#BedrockAgentCore.Paginator.ListSessions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore/paginators/#listsessionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSessionsInputPaginateTypeDef]
    ) -> PageIterator[ListSessionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore/paginator/ListSessions.html#BedrockAgentCore.Paginator.ListSessions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore/paginators/#listsessionspaginator)
        """

if TYPE_CHECKING:
    _RetrieveMemoryRecordsPaginatorBase = Paginator[RetrieveMemoryRecordsOutputTypeDef]
else:
    _RetrieveMemoryRecordsPaginatorBase = Paginator  # type: ignore[assignment]

class RetrieveMemoryRecordsPaginator(_RetrieveMemoryRecordsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore/paginator/RetrieveMemoryRecords.html#BedrockAgentCore.Paginator.RetrieveMemoryRecords)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore/paginators/#retrievememoryrecordspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[RetrieveMemoryRecordsInputPaginateTypeDef]
    ) -> PageIterator[RetrieveMemoryRecordsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore/paginator/RetrieveMemoryRecords.html#BedrockAgentCore.Paginator.RetrieveMemoryRecords.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore/paginators/#retrievememoryrecordspaginator)
        """
