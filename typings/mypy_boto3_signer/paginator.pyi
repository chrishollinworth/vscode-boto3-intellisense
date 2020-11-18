# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for signer service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_signer import SignerClient
    from mypy_boto3_signer.paginator import (
        ListSigningJobsPaginator,
        ListSigningPlatformsPaginator,
        ListSigningProfilesPaginator,
    )

    client: SignerClient = boto3.client("signer")

    list_signing_jobs_paginator: ListSigningJobsPaginator = client.get_paginator("list_signing_jobs")
    list_signing_platforms_paginator: ListSigningPlatformsPaginator = client.get_paginator("list_signing_platforms")
    list_signing_profiles_paginator: ListSigningProfilesPaginator = client.get_paginator("list_signing_profiles")
    ```
"""
import sys
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_signer.type_defs import (
    ListSigningJobsResponseTypeDef,
    ListSigningPlatformsResponseTypeDef,
    ListSigningProfilesResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListSigningJobsPaginator",
    "ListSigningPlatformsPaginator",
    "ListSigningProfilesPaginator",
)


class ListSigningJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListSigningJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Paginator.ListSigningJobs)
    """

    def paginate(
        self,
        status: Literal["InProgress", "Failed", "Succeeded"] = None,
        platformId: str = None,
        requestedBy: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListSigningJobsResponseTypeDef]:
        """
        [ListSigningJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Paginator.ListSigningJobs.paginate)
        """


class ListSigningPlatformsPaginator(Boto3Paginator):
    """
    [Paginator.ListSigningPlatforms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Paginator.ListSigningPlatforms)
    """

    def paginate(
        self,
        category: str = None,
        partner: str = None,
        target: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListSigningPlatformsResponseTypeDef]:
        """
        [ListSigningPlatforms.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Paginator.ListSigningPlatforms.paginate)
        """


class ListSigningProfilesPaginator(Boto3Paginator):
    """
    [Paginator.ListSigningProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Paginator.ListSigningProfiles)
    """

    def paginate(
        self, includeCanceled: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSigningProfilesResponseTypeDef]:
        """
        [ListSigningProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Paginator.ListSigningProfiles.paginate)
        """
