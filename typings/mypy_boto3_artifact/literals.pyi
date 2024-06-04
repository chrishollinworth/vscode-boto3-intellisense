"""
Type annotations for artifact service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_artifact/literals.html)

Usage::

    ```python
    from mypy_boto3_artifact.literals import AcceptanceTypeType

    data: AcceptanceTypeType = "EXPLICIT"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AcceptanceTypeType",
    "ListReportsPaginatorName",
    "NotificationSubscriptionStatusType",
    "PublishedStateType",
    "UploadStateType",
)

AcceptanceTypeType = Literal["EXPLICIT", "PASSTHROUGH"]
ListReportsPaginatorName = Literal["list_reports"]
NotificationSubscriptionStatusType = Literal["NOT_SUBSCRIBED", "SUBSCRIBED"]
PublishedStateType = Literal["PUBLISHED", "UNPUBLISHED"]
UploadStateType = Literal["COMPLETE", "FAILED", "FAULT", "PROCESSING"]
