"""
Main interface for route53resolver service.

Usage::

    ```python
    import boto3
    from mypy_boto3_route53resolver import (
        Client,
        ListTagsForResourcePaginator,
        Route53ResolverClient,
    )

    session = boto3.Session()

    client: Route53ResolverClient = boto3.client("route53resolver")
    session_client: Route53ResolverClient = session.client("route53resolver")

    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""
from mypy_boto3_route53resolver.client import Route53ResolverClient
from mypy_boto3_route53resolver.paginator import ListTagsForResourcePaginator

Client = Route53ResolverClient


__all__ = ("Client", "ListTagsForResourcePaginator", "Route53ResolverClient")
