"""
Type annotations for customer-profiles service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_customer_profiles import CustomerProfilesClient
    from mypy_boto3_customer_profiles.paginator import (
        ListEventStreamsPaginator,
    )

    client: CustomerProfilesClient = boto3.client("customer-profiles")

    list_event_streams_paginator: ListEventStreamsPaginator = client.get_paginator("list_event_streams")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import ListEventStreamsResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListEventStreamsPaginator",)

class ListEventStreamsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/customer-profiles.html#CustomerProfiles.Paginator.ListEventStreams)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/paginators.html#listeventstreamspaginator)
    """

    def paginate(
        self, *, DomainName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEventStreamsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/customer-profiles.html#CustomerProfiles.Paginator.ListEventStreams.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/paginators.html#listeventstreamspaginator)
        """
