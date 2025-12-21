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
        ListDomainLayoutsPaginator,
        ListDomainObjectTypesPaginator,
        ListEventStreamsPaginator,
        ListEventTriggersPaginator,
        ListObjectTypeAttributesPaginator,
        ListRecommenderRecipesPaginator,
        ListRecommendersPaginator,
        ListRuleBasedMatchesPaginator,
        ListSegmentDefinitionsPaginator,
        ListUploadJobsPaginator,
    )

    session = Session()
    client: CustomerProfilesClient = session.client("customer-profiles")

    get_similar_profiles_paginator: GetSimilarProfilesPaginator = client.get_paginator("get_similar_profiles")
    list_domain_layouts_paginator: ListDomainLayoutsPaginator = client.get_paginator("list_domain_layouts")
    list_domain_object_types_paginator: ListDomainObjectTypesPaginator = client.get_paginator("list_domain_object_types")
    list_event_streams_paginator: ListEventStreamsPaginator = client.get_paginator("list_event_streams")
    list_event_triggers_paginator: ListEventTriggersPaginator = client.get_paginator("list_event_triggers")
    list_object_type_attributes_paginator: ListObjectTypeAttributesPaginator = client.get_paginator("list_object_type_attributes")
    list_recommender_recipes_paginator: ListRecommenderRecipesPaginator = client.get_paginator("list_recommender_recipes")
    list_recommenders_paginator: ListRecommendersPaginator = client.get_paginator("list_recommenders")
    list_rule_based_matches_paginator: ListRuleBasedMatchesPaginator = client.get_paginator("list_rule_based_matches")
    list_segment_definitions_paginator: ListSegmentDefinitionsPaginator = client.get_paginator("list_segment_definitions")
    list_upload_jobs_paginator: ListUploadJobsPaginator = client.get_paginator("list_upload_jobs")
    ```
"""

from .client import CustomerProfilesClient
from .paginator import (
    GetSimilarProfilesPaginator,
    ListDomainLayoutsPaginator,
    ListDomainObjectTypesPaginator,
    ListEventStreamsPaginator,
    ListEventTriggersPaginator,
    ListObjectTypeAttributesPaginator,
    ListRecommenderRecipesPaginator,
    ListRecommendersPaginator,
    ListRuleBasedMatchesPaginator,
    ListSegmentDefinitionsPaginator,
    ListUploadJobsPaginator,
)

Client = CustomerProfilesClient

__all__ = (
    "Client",
    "CustomerProfilesClient",
    "GetSimilarProfilesPaginator",
    "ListDomainLayoutsPaginator",
    "ListDomainObjectTypesPaginator",
    "ListEventStreamsPaginator",
    "ListEventTriggersPaginator",
    "ListObjectTypeAttributesPaginator",
    "ListRecommenderRecipesPaginator",
    "ListRecommendersPaginator",
    "ListRuleBasedMatchesPaginator",
    "ListSegmentDefinitionsPaginator",
    "ListUploadJobsPaginator",
)
