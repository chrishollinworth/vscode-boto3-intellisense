# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for cloudtrail service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_cloudtrail import CloudTrailClient
    from mypy_boto3_cloudtrail.paginator import (
        ListPublicKeysPaginator,
        ListTagsPaginator,
        ListTrailsPaginator,
        LookupEventsPaginator,
    )

    client: CloudTrailClient = boto3.client("cloudtrail")

    list_public_keys_paginator: ListPublicKeysPaginator = client.get_paginator("list_public_keys")
    list_tags_paginator: ListTagsPaginator = client.get_paginator("list_tags")
    list_trails_paginator: ListTrailsPaginator = client.get_paginator("list_trails")
    lookup_events_paginator: LookupEventsPaginator = client.get_paginator("lookup_events")
    ```
"""
import sys
from datetime import datetime
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_cloudtrail.type_defs import (
    ListPublicKeysResponseTypeDef,
    ListTagsResponseTypeDef,
    ListTrailsResponseTypeDef,
    LookupAttributeTypeDef,
    LookupEventsResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListPublicKeysPaginator",
    "ListTagsPaginator",
    "ListTrailsPaginator",
    "LookupEventsPaginator",
)


class ListPublicKeysPaginator(Boto3Paginator):
    """
    [Paginator.ListPublicKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Paginator.ListPublicKeys)
    """

    def paginate(
        self,
        StartTime: datetime = None,
        EndTime: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListPublicKeysResponseTypeDef]:
        """
        [ListPublicKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Paginator.ListPublicKeys.paginate)
        """


class ListTagsPaginator(Boto3Paginator):
    """
    [Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTags)
    """

    def paginate(
        self, ResourceIdList: List[str], PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsResponseTypeDef]:
        """
        [ListTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTags.paginate)
        """


class ListTrailsPaginator(Boto3Paginator):
    """
    [Paginator.ListTrails documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTrails)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTrailsResponseTypeDef]:
        """
        [ListTrails.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTrails.paginate)
        """


class LookupEventsPaginator(Boto3Paginator):
    """
    [Paginator.LookupEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Paginator.LookupEvents)
    """

    def paginate(
        self,
        LookupAttributes: List[LookupAttributeTypeDef] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        EventCategory: Literal["insight"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[LookupEventsResponseTypeDef]:
        """
        [LookupEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Paginator.LookupEvents.paginate)
        """
