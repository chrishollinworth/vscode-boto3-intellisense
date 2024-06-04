"""
Type annotations for voice-id service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_voice_id/literals.html)

Usage::

    ```python
    from mypy_boto3_voice_id.literals import AuthenticationDecisionType

    data: AuthenticationDecisionType = "ACCEPT"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AuthenticationDecisionType",
    "DomainStatusType",
    "DuplicateRegistrationActionType",
    "ExistingEnrollmentActionType",
    "FraudDetectionActionType",
    "FraudDetectionDecisionType",
    "FraudDetectionReasonType",
    "FraudsterRegistrationJobStatusType",
    "ListDomainsPaginatorName",
    "ListFraudsterRegistrationJobsPaginatorName",
    "ListFraudstersPaginatorName",
    "ListSpeakerEnrollmentJobsPaginatorName",
    "ListSpeakersPaginatorName",
    "ListWatchlistsPaginatorName",
    "ServerSideEncryptionUpdateStatusType",
    "SpeakerEnrollmentJobStatusType",
    "SpeakerStatusType",
    "StreamingStatusType",
)

AuthenticationDecisionType = Literal[
    "ACCEPT",
    "NOT_ENOUGH_SPEECH",
    "REJECT",
    "SPEAKER_EXPIRED",
    "SPEAKER_ID_NOT_PROVIDED",
    "SPEAKER_NOT_ENROLLED",
    "SPEAKER_OPTED_OUT",
]
DomainStatusType = Literal["ACTIVE", "PENDING", "SUSPENDED"]
DuplicateRegistrationActionType = Literal["REGISTER_AS_NEW", "SKIP"]
ExistingEnrollmentActionType = Literal["OVERWRITE", "SKIP"]
FraudDetectionActionType = Literal["FAIL", "IGNORE"]
FraudDetectionDecisionType = Literal["HIGH_RISK", "LOW_RISK", "NOT_ENOUGH_SPEECH"]
FraudDetectionReasonType = Literal["KNOWN_FRAUDSTER", "VOICE_SPOOFING"]
FraudsterRegistrationJobStatusType = Literal[
    "COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "IN_PROGRESS", "SUBMITTED"
]
ListDomainsPaginatorName = Literal["list_domains"]
ListFraudsterRegistrationJobsPaginatorName = Literal["list_fraudster_registration_jobs"]
ListFraudstersPaginatorName = Literal["list_fraudsters"]
ListSpeakerEnrollmentJobsPaginatorName = Literal["list_speaker_enrollment_jobs"]
ListSpeakersPaginatorName = Literal["list_speakers"]
ListWatchlistsPaginatorName = Literal["list_watchlists"]
ServerSideEncryptionUpdateStatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS"]
SpeakerEnrollmentJobStatusType = Literal[
    "COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "IN_PROGRESS", "SUBMITTED"
]
SpeakerStatusType = Literal["ENROLLED", "EXPIRED", "OPTED_OUT", "PENDING"]
StreamingStatusType = Literal["ENDED", "ONGOING", "PENDING_CONFIGURATION"]
