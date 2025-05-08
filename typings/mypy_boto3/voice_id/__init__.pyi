"""
Main interface for voice-id service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_voice_id/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_voice_id import (
        Client,
        ListDomainsPaginator,
        ListFraudsterRegistrationJobsPaginator,
        ListFraudstersPaginator,
        ListSpeakerEnrollmentJobsPaginator,
        ListSpeakersPaginator,
        ListWatchlistsPaginator,
        VoiceIDClient,
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

from .client import VoiceIDClient
from .paginator import (
    ListDomainsPaginator,
    ListFraudsterRegistrationJobsPaginator,
    ListFraudstersPaginator,
    ListSpeakerEnrollmentJobsPaginator,
    ListSpeakersPaginator,
    ListWatchlistsPaginator,
)

Client = VoiceIDClient

__all__ = (
    "Client",
    "ListDomainsPaginator",
    "ListFraudsterRegistrationJobsPaginator",
    "ListFraudstersPaginator",
    "ListSpeakerEnrollmentJobsPaginator",
    "ListSpeakersPaginator",
    "ListWatchlistsPaginator",
    "VoiceIDClient",
)
