"""
Type annotations for cloudtrail service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/literals.html)

Usage::

    ```python
    from mypy_boto3_cloudtrail.literals import EventCategoryType

    data: EventCategoryType = "insight"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "EventCategoryType",
    "EventDataStoreStatusType",
    "InsightTypeType",
    "ListPublicKeysPaginatorName",
    "ListTagsPaginatorName",
    "ListTrailsPaginatorName",
    "LookupAttributeKeyType",
    "LookupEventsPaginatorName",
    "QueryStatusType",
    "ReadWriteTypeType",
)

EventCategoryType = Literal["insight"]
EventDataStoreStatusType = Literal["CREATED", "ENABLED", "PENDING_DELETION"]
InsightTypeType = Literal["ApiCallRateInsight", "ApiErrorRateInsight"]
ListPublicKeysPaginatorName = Literal["list_public_keys"]
ListTagsPaginatorName = Literal["list_tags"]
ListTrailsPaginatorName = Literal["list_trails"]
LookupAttributeKeyType = Literal[
    "AccessKeyId",
    "EventId",
    "EventName",
    "EventSource",
    "ReadOnly",
    "ResourceName",
    "ResourceType",
    "Username",
]
LookupEventsPaginatorName = Literal["lookup_events"]
QueryStatusType = Literal["CANCELLED", "FAILED", "FINISHED", "QUEUED", "RUNNING", "TIMED_OUT"]
ReadWriteTypeType = Literal["All", "ReadOnly", "WriteOnly"]
