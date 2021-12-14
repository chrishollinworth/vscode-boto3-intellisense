"""
Type annotations for cloudtrail service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators.html)

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
from typing import Iterator, List, Union

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudtrail.html#CloudTrail.Paginator.ListPublicKeys)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators.html#listpublickeyspaginator)
    """

    def paginate(
        self,
        *,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPublicKeysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudtrail.html#CloudTrail.Paginator.ListPublicKeys.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators.html#listpublickeyspaginator)
        """

class ListTagsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTags)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators.html#listtagspaginator)
    """

    def paginate(
        self, *, ResourceIdList: List[str], PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTags.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators.html#listtagspaginator)
        """

class ListTrailsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTrails)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators.html#listtrailspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTrailsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTrails.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators.html#listtrailspaginator)
        """

class LookupEventsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudtrail.html#CloudTrail.Paginator.LookupEvents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators.html#lookupeventspaginator)
    """

    def paginate(
        self,
        *,
        LookupAttributes: List["LookupAttributeTypeDef"] = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        EventCategory: Literal["insight"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[LookupEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudtrail.html#CloudTrail.Paginator.LookupEvents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators.html#lookupeventspaginator)
        """
