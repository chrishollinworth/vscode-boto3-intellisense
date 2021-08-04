"""
Type annotations for connectparticipant service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/literals.html)

Usage::

    ```python
    from mypy_boto3_connectparticipant.literals import ArtifactStatusType

    data: ArtifactStatusType = "APPROVED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ArtifactStatusType",
    "ChatItemTypeType",
    "ConnectionTypeType",
    "ParticipantRoleType",
    "ScanDirectionType",
    "SortKeyType",
)

ArtifactStatusType = Literal["APPROVED", "IN_PROGRESS", "REJECTED"]
ChatItemTypeType = Literal[
    "ATTACHMENT",
    "CHAT_ENDED",
    "CONNECTION_ACK",
    "EVENT",
    "MESSAGE",
    "PARTICIPANT_JOINED",
    "PARTICIPANT_LEFT",
    "TRANSFER_FAILED",
    "TRANSFER_SUCCEEDED",
    "TYPING",
]
ConnectionTypeType = Literal["CONNECTION_CREDENTIALS", "WEBSOCKET"]
ParticipantRoleType = Literal["AGENT", "CUSTOMER", "SYSTEM"]
ScanDirectionType = Literal["BACKWARD", "FORWARD"]
SortKeyType = Literal["ASCENDING", "DESCENDING"]
