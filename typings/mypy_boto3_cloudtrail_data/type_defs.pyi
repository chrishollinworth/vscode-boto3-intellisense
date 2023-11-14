"""
Type annotations for cloudtrail-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudtrail_data.type_defs import AuditEventResultEntryTypeDef

    data: AuditEventResultEntryTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AuditEventResultEntryTypeDef",
    "AuditEventTypeDef",
    "PutAuditEventsRequestRequestTypeDef",
    "PutAuditEventsResponseTypeDef",
    "ResponseMetadataTypeDef",
    "ResultErrorEntryTypeDef",
)

AuditEventResultEntryTypeDef = TypedDict(
    "AuditEventResultEntryTypeDef",
    {
        "eventID": str,
        "id": str,
    },
)

_RequiredAuditEventTypeDef = TypedDict(
    "_RequiredAuditEventTypeDef",
    {
        "eventData": str,
        "id": str,
    },
)
_OptionalAuditEventTypeDef = TypedDict(
    "_OptionalAuditEventTypeDef",
    {
        "eventDataChecksum": str,
    },
    total=False,
)

class AuditEventTypeDef(_RequiredAuditEventTypeDef, _OptionalAuditEventTypeDef):
    pass

_RequiredPutAuditEventsRequestRequestTypeDef = TypedDict(
    "_RequiredPutAuditEventsRequestRequestTypeDef",
    {
        "auditEvents": List["AuditEventTypeDef"],
        "channelArn": str,
    },
)
_OptionalPutAuditEventsRequestRequestTypeDef = TypedDict(
    "_OptionalPutAuditEventsRequestRequestTypeDef",
    {
        "externalId": str,
    },
    total=False,
)

class PutAuditEventsRequestRequestTypeDef(
    _RequiredPutAuditEventsRequestRequestTypeDef, _OptionalPutAuditEventsRequestRequestTypeDef
):
    pass

PutAuditEventsResponseTypeDef = TypedDict(
    "PutAuditEventsResponseTypeDef",
    {
        "failed": List["ResultErrorEntryTypeDef"],
        "successful": List["AuditEventResultEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

ResultErrorEntryTypeDef = TypedDict(
    "ResultErrorEntryTypeDef",
    {
        "errorCode": str,
        "errorMessage": str,
        "id": str,
    },
)
