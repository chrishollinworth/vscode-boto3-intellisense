"""
Type annotations for voice-id service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_voice_id.client import VoiceIDClient
    from mypy_boto3_voice_id.paginator import (
        ListDomainsPaginator,
        ListFraudsterRegistrationJobsPaginator,
        ListFraudstersPaginator,
        ListSpeakerEnrollmentJobsPaginator,
        ListSpeakersPaginator,
        ListWatchlistsPaginator,
    )

    session = Session()
    client: VoiceIDClient = session.client("voice-id")

    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    list_fraudster_registration_jobs_paginator: ListFraudsterRegistrationJobsPaginator = client.get_paginator("list_fraudster_registration_jobs")
    list_fraudsters_paginator: ListFraudstersPaginator = client.get_paginator("list_fraudsters")
    list_speaker_enrollment_jobs_paginator: ListSpeakerEnrollmentJobsPaginator = client.get_paginator("list_speaker_enrollment_jobs")
    list_speakers_paginator: ListSpeakersPaginator = client.get_paginator("list_speakers")
    list_watchlists_paginator: ListWatchlistsPaginator = client.get_paginator("list_watchlists")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListDomainsRequestPaginateTypeDef,
    ListDomainsResponseTypeDef,
    ListFraudsterRegistrationJobsRequestPaginateTypeDef,
    ListFraudsterRegistrationJobsResponseTypeDef,
    ListFraudstersRequestPaginateTypeDef,
    ListFraudstersResponseTypeDef,
    ListSpeakerEnrollmentJobsRequestPaginateTypeDef,
    ListSpeakerEnrollmentJobsResponseTypeDef,
    ListSpeakersRequestPaginateTypeDef,
    ListSpeakersResponseTypeDef,
    ListWatchlistsRequestPaginateTypeDef,
    ListWatchlistsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListDomainsPaginator",
    "ListFraudsterRegistrationJobsPaginator",
    "ListFraudstersPaginator",
    "ListSpeakerEnrollmentJobsPaginator",
    "ListSpeakersPaginator",
    "ListWatchlistsPaginator",
)

if TYPE_CHECKING:
    _ListDomainsPaginatorBase = Paginator[ListDomainsResponseTypeDef]
else:
    _ListDomainsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDomainsPaginator(_ListDomainsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id/paginator/ListDomains.html#VoiceID.Paginator.ListDomains)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators/#listdomainspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDomainsRequestPaginateTypeDef]
    ) -> PageIterator[ListDomainsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id/paginator/ListDomains.html#VoiceID.Paginator.ListDomains.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators/#listdomainspaginator)
        """

if TYPE_CHECKING:
    _ListFraudsterRegistrationJobsPaginatorBase = Paginator[
        ListFraudsterRegistrationJobsResponseTypeDef
    ]
else:
    _ListFraudsterRegistrationJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFraudsterRegistrationJobsPaginator(_ListFraudsterRegistrationJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id/paginator/ListFraudsterRegistrationJobs.html#VoiceID.Paginator.ListFraudsterRegistrationJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators/#listfraudsterregistrationjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFraudsterRegistrationJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListFraudsterRegistrationJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id/paginator/ListFraudsterRegistrationJobs.html#VoiceID.Paginator.ListFraudsterRegistrationJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators/#listfraudsterregistrationjobspaginator)
        """

if TYPE_CHECKING:
    _ListFraudstersPaginatorBase = Paginator[ListFraudstersResponseTypeDef]
else:
    _ListFraudstersPaginatorBase = Paginator  # type: ignore[assignment]

class ListFraudstersPaginator(_ListFraudstersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id/paginator/ListFraudsters.html#VoiceID.Paginator.ListFraudsters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators/#listfraudsterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFraudstersRequestPaginateTypeDef]
    ) -> PageIterator[ListFraudstersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id/paginator/ListFraudsters.html#VoiceID.Paginator.ListFraudsters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators/#listfraudsterspaginator)
        """

if TYPE_CHECKING:
    _ListSpeakerEnrollmentJobsPaginatorBase = Paginator[ListSpeakerEnrollmentJobsResponseTypeDef]
else:
    _ListSpeakerEnrollmentJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSpeakerEnrollmentJobsPaginator(_ListSpeakerEnrollmentJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id/paginator/ListSpeakerEnrollmentJobs.html#VoiceID.Paginator.ListSpeakerEnrollmentJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators/#listspeakerenrollmentjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSpeakerEnrollmentJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListSpeakerEnrollmentJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id/paginator/ListSpeakerEnrollmentJobs.html#VoiceID.Paginator.ListSpeakerEnrollmentJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators/#listspeakerenrollmentjobspaginator)
        """

if TYPE_CHECKING:
    _ListSpeakersPaginatorBase = Paginator[ListSpeakersResponseTypeDef]
else:
    _ListSpeakersPaginatorBase = Paginator  # type: ignore[assignment]

class ListSpeakersPaginator(_ListSpeakersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id/paginator/ListSpeakers.html#VoiceID.Paginator.ListSpeakers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators/#listspeakerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSpeakersRequestPaginateTypeDef]
    ) -> PageIterator[ListSpeakersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id/paginator/ListSpeakers.html#VoiceID.Paginator.ListSpeakers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators/#listspeakerspaginator)
        """

if TYPE_CHECKING:
    _ListWatchlistsPaginatorBase = Paginator[ListWatchlistsResponseTypeDef]
else:
    _ListWatchlistsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWatchlistsPaginator(_ListWatchlistsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id/paginator/ListWatchlists.html#VoiceID.Paginator.ListWatchlists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators/#listwatchlistspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWatchlistsRequestPaginateTypeDef]
    ) -> PageIterator[ListWatchlistsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id/paginator/ListWatchlists.html#VoiceID.Paginator.ListWatchlists.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators/#listwatchlistspaginator)
        """
