"""
Type annotations for customer-profiles service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_customer_profiles.client import CustomerProfilesClient
    from mypy_boto3_customer_profiles.paginator import (
        GetSimilarProfilesPaginator,
        ListEventStreamsPaginator,
        ListEventTriggersPaginator,
        ListObjectTypeAttributesPaginator,
        ListRuleBasedMatchesPaginator,
        ListSegmentDefinitionsPaginator,
    )

    session = Session()
    client: CustomerProfilesClient = session.client("customer-profiles")

    get_similar_profiles_paginator: GetSimilarProfilesPaginator = client.get_paginator("get_similar_profiles")
    list_event_streams_paginator: ListEventStreamsPaginator = client.get_paginator("list_event_streams")
    list_event_triggers_paginator: ListEventTriggersPaginator = client.get_paginator("list_event_triggers")
    list_object_type_attributes_paginator: ListObjectTypeAttributesPaginator = client.get_paginator("list_object_type_attributes")
    list_rule_based_matches_paginator: ListRuleBasedMatchesPaginator = client.get_paginator("list_rule_based_matches")
    list_segment_definitions_paginator: ListSegmentDefinitionsPaginator = client.get_paginator("list_segment_definitions")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetSimilarProfilesRequestPaginateTypeDef,
    GetSimilarProfilesResponseTypeDef,
    ListEventStreamsRequestPaginateTypeDef,
    ListEventStreamsResponseTypeDef,
    ListEventTriggersRequestPaginateTypeDef,
    ListEventTriggersResponseTypeDef,
    ListObjectTypeAttributesRequestPaginateTypeDef,
    ListObjectTypeAttributesResponseTypeDef,
    ListRuleBasedMatchesRequestPaginateTypeDef,
    ListRuleBasedMatchesResponseTypeDef,
    ListSegmentDefinitionsRequestPaginateTypeDef,
    ListSegmentDefinitionsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetSimilarProfilesPaginator",
    "ListEventStreamsPaginator",
    "ListEventTriggersPaginator",
    "ListObjectTypeAttributesPaginator",
    "ListRuleBasedMatchesPaginator",
    "ListSegmentDefinitionsPaginator",
)

if TYPE_CHECKING:
    _GetSimilarProfilesPaginatorBase = Paginator[GetSimilarProfilesResponseTypeDef]
else:
    _GetSimilarProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class GetSimilarProfilesPaginator(_GetSimilarProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/paginator/GetSimilarProfiles.html#CustomerProfiles.Paginator.GetSimilarProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/paginators/#getsimilarprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetSimilarProfilesRequestPaginateTypeDef]
    ) -> PageIterator[GetSimilarProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/paginator/GetSimilarProfiles.html#CustomerProfiles.Paginator.GetSimilarProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/paginators/#getsimilarprofilespaginator)
        """

if TYPE_CHECKING:
    _ListEventStreamsPaginatorBase = Paginator[ListEventStreamsResponseTypeDef]
else:
    _ListEventStreamsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEventStreamsPaginator(_ListEventStreamsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/paginator/ListEventStreams.html#CustomerProfiles.Paginator.ListEventStreams)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/paginators/#listeventstreamspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEventStreamsRequestPaginateTypeDef]
    ) -> PageIterator[ListEventStreamsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/paginator/ListEventStreams.html#CustomerProfiles.Paginator.ListEventStreams.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/paginators/#listeventstreamspaginator)
        """

if TYPE_CHECKING:
    _ListEventTriggersPaginatorBase = Paginator[ListEventTriggersResponseTypeDef]
else:
    _ListEventTriggersPaginatorBase = Paginator  # type: ignore[assignment]

class ListEventTriggersPaginator(_ListEventTriggersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/paginator/ListEventTriggers.html#CustomerProfiles.Paginator.ListEventTriggers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/paginators/#listeventtriggerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEventTriggersRequestPaginateTypeDef]
    ) -> PageIterator[ListEventTriggersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/paginator/ListEventTriggers.html#CustomerProfiles.Paginator.ListEventTriggers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/paginators/#listeventtriggerspaginator)
        """

if TYPE_CHECKING:
    _ListObjectTypeAttributesPaginatorBase = Paginator[ListObjectTypeAttributesResponseTypeDef]
else:
    _ListObjectTypeAttributesPaginatorBase = Paginator  # type: ignore[assignment]

class ListObjectTypeAttributesPaginator(_ListObjectTypeAttributesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/paginator/ListObjectTypeAttributes.html#CustomerProfiles.Paginator.ListObjectTypeAttributes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/paginators/#listobjecttypeattributespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListObjectTypeAttributesRequestPaginateTypeDef]
    ) -> PageIterator[ListObjectTypeAttributesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/paginator/ListObjectTypeAttributes.html#CustomerProfiles.Paginator.ListObjectTypeAttributes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/paginators/#listobjecttypeattributespaginator)
        """

if TYPE_CHECKING:
    _ListRuleBasedMatchesPaginatorBase = Paginator[ListRuleBasedMatchesResponseTypeDef]
else:
    _ListRuleBasedMatchesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRuleBasedMatchesPaginator(_ListRuleBasedMatchesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/paginator/ListRuleBasedMatches.html#CustomerProfiles.Paginator.ListRuleBasedMatches)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/paginators/#listrulebasedmatchespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRuleBasedMatchesRequestPaginateTypeDef]
    ) -> PageIterator[ListRuleBasedMatchesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/paginator/ListRuleBasedMatches.html#CustomerProfiles.Paginator.ListRuleBasedMatches.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/paginators/#listrulebasedmatchespaginator)
        """

if TYPE_CHECKING:
    _ListSegmentDefinitionsPaginatorBase = Paginator[ListSegmentDefinitionsResponseTypeDef]
else:
    _ListSegmentDefinitionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSegmentDefinitionsPaginator(_ListSegmentDefinitionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/paginator/ListSegmentDefinitions.html#CustomerProfiles.Paginator.ListSegmentDefinitions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/paginators/#listsegmentdefinitionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSegmentDefinitionsRequestPaginateTypeDef]
    ) -> PageIterator[ListSegmentDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/paginator/ListSegmentDefinitions.html#CustomerProfiles.Paginator.ListSegmentDefinitions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/paginators/#listsegmentdefinitionspaginator)
        """
