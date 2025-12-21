"""
Main interface for resourcegroupstaggingapi service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_resourcegroupstaggingapi import (
        Client,
        GetComplianceSummaryPaginator,
        GetResourcesPaginator,
        GetTagKeysPaginator,
        GetTagValuesPaginator,
        ListRequiredTagsPaginator,
        ResourceGroupsTaggingAPIClient,
    )

    session = Session()
    client: ResourceGroupsTaggingAPIClient = session.client("resourcegroupstaggingapi")

    get_compliance_summary_paginator: GetComplianceSummaryPaginator = client.get_paginator("get_compliance_summary")
    get_resources_paginator: GetResourcesPaginator = client.get_paginator("get_resources")
    get_tag_keys_paginator: GetTagKeysPaginator = client.get_paginator("get_tag_keys")
    get_tag_values_paginator: GetTagValuesPaginator = client.get_paginator("get_tag_values")
    list_required_tags_paginator: ListRequiredTagsPaginator = client.get_paginator("list_required_tags")
    ```
"""

from .client import ResourceGroupsTaggingAPIClient
from .paginator import (
    GetComplianceSummaryPaginator,
    GetResourcesPaginator,
    GetTagKeysPaginator,
    GetTagValuesPaginator,
    ListRequiredTagsPaginator,
)

Client = ResourceGroupsTaggingAPIClient

__all__ = (
    "Client",
    "GetComplianceSummaryPaginator",
    "GetResourcesPaginator",
    "GetTagKeysPaginator",
    "GetTagValuesPaginator",
    "ListRequiredTagsPaginator",
    "ResourceGroupsTaggingAPIClient",
)
