"""
Type annotations for voice-id service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_voice_id import VoiceIDClient
    from mypy_boto3_voice_id.paginator import (
        ListDomainsPaginator,
        ListFraudsterRegistrationJobsPaginator,
        ListFraudstersPaginator,
        ListSpeakerEnrollmentJobsPaginator,
        ListSpeakersPaginator,
        ListWatchlistsPaginator,
    )

    client: VoiceIDClient = boto3.client("voice-id")

    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    list_fraudster_registration_jobs_paginator: ListFraudsterRegistrationJobsPaginator = client.get_paginator("list_fraudster_registration_jobs")
    list_fraudsters_paginator: ListFraudstersPaginator = client.get_paginator("list_fraudsters")
    list_speaker_enrollment_jobs_paginator: ListSpeakerEnrollmentJobsPaginator = client.get_paginator("list_speaker_enrollment_jobs")
    list_speakers_paginator: ListSpeakersPaginator = client.get_paginator("list_speakers")
    list_watchlists_paginator: ListWatchlistsPaginator = client.get_paginator("list_watchlists")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import FraudsterRegistrationJobStatusType, SpeakerEnrollmentJobStatusType
from .type_defs import (
    ListDomainsResponseTypeDef,
    ListFraudsterRegistrationJobsResponseTypeDef,
    ListFraudstersResponseTypeDef,
    ListSpeakerEnrollmentJobsResponseTypeDef,
    ListSpeakersResponseTypeDef,
    ListWatchlistsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListDomainsPaginator",
    "ListFraudsterRegistrationJobsPaginator",
    "ListFraudstersPaginator",
    "ListSpeakerEnrollmentJobsPaginator",
    "ListSpeakersPaginator",
    "ListWatchlistsPaginator",
)

class ListDomainsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/voice-id.html#VoiceID.Paginator.ListDomains)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators.html#listdomainspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDomainsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/voice-id.html#VoiceID.Paginator.ListDomains.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators.html#listdomainspaginator)
        """

class ListFraudsterRegistrationJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/voice-id.html#VoiceID.Paginator.ListFraudsterRegistrationJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators.html#listfraudsterregistrationjobspaginator)
    """

    def paginate(
        self,
        *,
        DomainId: str,
        JobStatus: FraudsterRegistrationJobStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFraudsterRegistrationJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/voice-id.html#VoiceID.Paginator.ListFraudsterRegistrationJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators.html#listfraudsterregistrationjobspaginator)
        """

class ListFraudstersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/voice-id.html#VoiceID.Paginator.ListFraudsters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators.html#listfraudsterspaginator)
    """

    def paginate(
        self,
        *,
        DomainId: str,
        WatchlistId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFraudstersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/voice-id.html#VoiceID.Paginator.ListFraudsters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators.html#listfraudsterspaginator)
        """

class ListSpeakerEnrollmentJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/voice-id.html#VoiceID.Paginator.ListSpeakerEnrollmentJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators.html#listspeakerenrollmentjobspaginator)
    """

    def paginate(
        self,
        *,
        DomainId: str,
        JobStatus: SpeakerEnrollmentJobStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSpeakerEnrollmentJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/voice-id.html#VoiceID.Paginator.ListSpeakerEnrollmentJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators.html#listspeakerenrollmentjobspaginator)
        """

class ListSpeakersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/voice-id.html#VoiceID.Paginator.ListSpeakers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators.html#listspeakerspaginator)
    """

    def paginate(
        self, *, DomainId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSpeakersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/voice-id.html#VoiceID.Paginator.ListSpeakers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators.html#listspeakerspaginator)
        """

class ListWatchlistsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/voice-id.html#VoiceID.Paginator.ListWatchlists)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators.html#listwatchlistspaginator)
    """

    def paginate(
        self, *, DomainId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWatchlistsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/voice-id.html#VoiceID.Paginator.ListWatchlists.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/paginators.html#listwatchlistspaginator)
        """
