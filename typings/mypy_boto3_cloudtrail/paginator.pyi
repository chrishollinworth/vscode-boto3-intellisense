"""
Type annotations for cloudtrail service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_cloudtrail.client import CloudTrailClient
    from mypy_boto3_cloudtrail.paginator import (
        ListImportFailuresPaginator,
        ListImportsPaginator,
        ListPublicKeysPaginator,
        ListTagsPaginator,
        ListTrailsPaginator,
        LookupEventsPaginator,
    )

    session = Session()
    client: CloudTrailClient = session.client("cloudtrail")

    list_import_failures_paginator: ListImportFailuresPaginator = client.get_paginator("list_import_failures")
    list_imports_paginator: ListImportsPaginator = client.get_paginator("list_imports")
    list_public_keys_paginator: ListPublicKeysPaginator = client.get_paginator("list_public_keys")
    list_tags_paginator: ListTagsPaginator = client.get_paginator("list_tags")
    list_trails_paginator: ListTrailsPaginator = client.get_paginator("list_trails")
    lookup_events_paginator: LookupEventsPaginator = client.get_paginator("lookup_events")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListImportFailuresRequestPaginateTypeDef,
    ListImportFailuresResponseTypeDef,
    ListImportsRequestPaginateTypeDef,
    ListImportsResponseTypeDef,
    ListPublicKeysRequestPaginateTypeDef,
    ListPublicKeysResponseTypeDef,
    ListTagsRequestPaginateTypeDef,
    ListTagsResponseTypeDef,
    ListTrailsRequestPaginateTypeDef,
    ListTrailsResponseTypeDef,
    LookupEventsRequestPaginateTypeDef,
    LookupEventsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListImportFailuresPaginator",
    "ListImportsPaginator",
    "ListPublicKeysPaginator",
    "ListTagsPaginator",
    "ListTrailsPaginator",
    "LookupEventsPaginator",
)

if TYPE_CHECKING:
    _ListImportFailuresPaginatorBase = Paginator[ListImportFailuresResponseTypeDef]
else:
    _ListImportFailuresPaginatorBase = Paginator  # type: ignore[assignment]

class ListImportFailuresPaginator(_ListImportFailuresPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail/paginator/ListImportFailures.html#CloudTrail.Paginator.ListImportFailures)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators/#listimportfailurespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListImportFailuresRequestPaginateTypeDef]
    ) -> PageIterator[ListImportFailuresResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail/paginator/ListImportFailures.html#CloudTrail.Paginator.ListImportFailures.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators/#listimportfailurespaginator)
        """

if TYPE_CHECKING:
    _ListImportsPaginatorBase = Paginator[ListImportsResponseTypeDef]
else:
    _ListImportsPaginatorBase = Paginator  # type: ignore[assignment]

class ListImportsPaginator(_ListImportsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail/paginator/ListImports.html#CloudTrail.Paginator.ListImports)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators/#listimportspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListImportsRequestPaginateTypeDef]
    ) -> PageIterator[ListImportsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail/paginator/ListImports.html#CloudTrail.Paginator.ListImports.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators/#listimportspaginator)
        """

if TYPE_CHECKING:
    _ListPublicKeysPaginatorBase = Paginator[ListPublicKeysResponseTypeDef]
else:
    _ListPublicKeysPaginatorBase = Paginator  # type: ignore[assignment]

class ListPublicKeysPaginator(_ListPublicKeysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail/paginator/ListPublicKeys.html#CloudTrail.Paginator.ListPublicKeys)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators/#listpublickeyspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPublicKeysRequestPaginateTypeDef]
    ) -> PageIterator[ListPublicKeysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail/paginator/ListPublicKeys.html#CloudTrail.Paginator.ListPublicKeys.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators/#listpublickeyspaginator)
        """

if TYPE_CHECKING:
    _ListTagsPaginatorBase = Paginator[ListTagsResponseTypeDef]
else:
    _ListTagsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTagsPaginator(_ListTagsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail/paginator/ListTags.html#CloudTrail.Paginator.ListTags)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators/#listtagspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagsRequestPaginateTypeDef]
    ) -> PageIterator[ListTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail/paginator/ListTags.html#CloudTrail.Paginator.ListTags.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators/#listtagspaginator)
        """

if TYPE_CHECKING:
    _ListTrailsPaginatorBase = Paginator[ListTrailsResponseTypeDef]
else:
    _ListTrailsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTrailsPaginator(_ListTrailsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail/paginator/ListTrails.html#CloudTrail.Paginator.ListTrails)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators/#listtrailspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTrailsRequestPaginateTypeDef]
    ) -> PageIterator[ListTrailsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail/paginator/ListTrails.html#CloudTrail.Paginator.ListTrails.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators/#listtrailspaginator)
        """

if TYPE_CHECKING:
    _LookupEventsPaginatorBase = Paginator[LookupEventsResponseTypeDef]
else:
    _LookupEventsPaginatorBase = Paginator  # type: ignore[assignment]

class LookupEventsPaginator(_LookupEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail/paginator/LookupEvents.html#CloudTrail.Paginator.LookupEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators/#lookupeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[LookupEventsRequestPaginateTypeDef]
    ) -> PageIterator[LookupEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail/paginator/LookupEvents.html#CloudTrail.Paginator.LookupEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators/#lookupeventspaginator)
        """
