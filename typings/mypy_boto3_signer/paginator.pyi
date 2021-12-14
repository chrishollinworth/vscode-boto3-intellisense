"""
Type annotations for signer service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_signer/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_signer import signerClient
    from mypy_boto3_signer.paginator import (
        ListSigningJobsPaginator,
        ListSigningPlatformsPaginator,
        ListSigningProfilesPaginator,
    )

    client: signerClient = boto3.client("signer")

    list_signing_jobs_paginator: ListSigningJobsPaginator = client.get_paginator("list_signing_jobs")
    list_signing_platforms_paginator: ListSigningPlatformsPaginator = client.get_paginator("list_signing_platforms")
    list_signing_profiles_paginator: ListSigningProfilesPaginator = client.get_paginator("list_signing_profiles")
    ```
"""
from datetime import datetime
from typing import Iterator, List, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import SigningProfileStatusType, SigningStatusType
from .type_defs import (
    ListSigningJobsResponseTypeDef,
    ListSigningPlatformsResponseTypeDef,
    ListSigningProfilesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListSigningJobsPaginator",
    "ListSigningPlatformsPaginator",
    "ListSigningProfilesPaginator",
)

class ListSigningJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/signer.html#signer.Paginator.ListSigningJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_signer/paginators.html#listsigningjobspaginator)
    """

    def paginate(
        self,
        *,
        status: SigningStatusType = None,
        platformId: str = None,
        requestedBy: str = None,
        isRevoked: bool = None,
        signatureExpiresBefore: Union[datetime, str] = None,
        signatureExpiresAfter: Union[datetime, str] = None,
        jobInvoker: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSigningJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/signer.html#signer.Paginator.ListSigningJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_signer/paginators.html#listsigningjobspaginator)
        """

class ListSigningPlatformsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/signer.html#signer.Paginator.ListSigningPlatforms)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_signer/paginators.html#listsigningplatformspaginator)
    """

    def paginate(
        self,
        *,
        category: str = None,
        partner: str = None,
        target: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSigningPlatformsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/signer.html#signer.Paginator.ListSigningPlatforms.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_signer/paginators.html#listsigningplatformspaginator)
        """

class ListSigningProfilesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/signer.html#signer.Paginator.ListSigningProfiles)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_signer/paginators.html#listsigningprofilespaginator)
    """

    def paginate(
        self,
        *,
        includeCanceled: bool = None,
        platformId: str = None,
        statuses: List[SigningProfileStatusType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSigningProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/signer.html#signer.Paginator.ListSigningProfiles.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_signer/paginators.html#listsigningprofilespaginator)
        """
