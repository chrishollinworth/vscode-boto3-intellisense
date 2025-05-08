"""
Type annotations for signer service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_signer.client import SignerClient
    from mypy_boto3_signer.paginator import (
        ListSigningJobsPaginator,
        ListSigningPlatformsPaginator,
        ListSigningProfilesPaginator,
    )

    session = Session()
    client: SignerClient = session.client("signer")

    list_signing_jobs_paginator: ListSigningJobsPaginator = client.get_paginator("list_signing_jobs")
    list_signing_platforms_paginator: ListSigningPlatformsPaginator = client.get_paginator("list_signing_platforms")
    list_signing_profiles_paginator: ListSigningProfilesPaginator = client.get_paginator("list_signing_profiles")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListSigningJobsRequestPaginateTypeDef,
    ListSigningJobsResponseTypeDef,
    ListSigningPlatformsRequestPaginateTypeDef,
    ListSigningPlatformsResponseTypeDef,
    ListSigningProfilesRequestPaginateTypeDef,
    ListSigningProfilesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListSigningJobsPaginator",
    "ListSigningPlatformsPaginator",
    "ListSigningProfilesPaginator",
)

if TYPE_CHECKING:
    _ListSigningJobsPaginatorBase = Paginator[ListSigningJobsResponseTypeDef]
else:
    _ListSigningJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSigningJobsPaginator(_ListSigningJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/paginator/ListSigningJobs.html#Signer.Paginator.ListSigningJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/paginators/#listsigningjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSigningJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListSigningJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/paginator/ListSigningJobs.html#Signer.Paginator.ListSigningJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/paginators/#listsigningjobspaginator)
        """

if TYPE_CHECKING:
    _ListSigningPlatformsPaginatorBase = Paginator[ListSigningPlatformsResponseTypeDef]
else:
    _ListSigningPlatformsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSigningPlatformsPaginator(_ListSigningPlatformsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/paginator/ListSigningPlatforms.html#Signer.Paginator.ListSigningPlatforms)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/paginators/#listsigningplatformspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSigningPlatformsRequestPaginateTypeDef]
    ) -> PageIterator[ListSigningPlatformsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/paginator/ListSigningPlatforms.html#Signer.Paginator.ListSigningPlatforms.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/paginators/#listsigningplatformspaginator)
        """

if TYPE_CHECKING:
    _ListSigningProfilesPaginatorBase = Paginator[ListSigningProfilesResponseTypeDef]
else:
    _ListSigningProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSigningProfilesPaginator(_ListSigningProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/paginator/ListSigningProfiles.html#Signer.Paginator.ListSigningProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/paginators/#listsigningprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSigningProfilesRequestPaginateTypeDef]
    ) -> PageIterator[ListSigningProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/paginator/ListSigningProfiles.html#Signer.Paginator.ListSigningProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/paginators/#listsigningprofilespaginator)
        """
