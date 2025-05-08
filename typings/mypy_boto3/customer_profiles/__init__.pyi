"""
Main interface for customer-profiles service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_customer_profiles import (
        Client,
        CustomerProfilesClient,
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

from .client import CustomerProfilesClient
from .paginator import (
    GetSimilarProfilesPaginator,
    ListEventStreamsPaginator,
    ListEventTriggersPaginator,
    ListObjectTypeAttributesPaginator,
    ListRuleBasedMatchesPaginator,
    ListSegmentDefinitionsPaginator,
)

Client = CustomerProfilesClient

__all__ = (
    "Client",
    "CustomerProfilesClient",
    "GetSimilarProfilesPaginator",
    "ListEventStreamsPaginator",
    "ListEventTriggersPaginator",
    "ListObjectTypeAttributesPaginator",
    "ListRuleBasedMatchesPaginator",
    "ListSegmentDefinitionsPaginator",
)
