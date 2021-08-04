"""
Type annotations for codestar-notifications service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/literals.html)

Usage::

    ```python
    from mypy_boto3_codestar_notifications.literals import DetailTypeType

    data: DetailTypeType = "BASIC"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DetailTypeType",
    "ListEventTypesFilterNameType",
    "ListEventTypesPaginatorName",
    "ListNotificationRulesFilterNameType",
    "ListNotificationRulesPaginatorName",
    "ListTargetsFilterNameType",
    "ListTargetsPaginatorName",
    "NotificationRuleStatusType",
    "TargetStatusType",
)

DetailTypeType = Literal["BASIC", "FULL"]
ListEventTypesFilterNameType = Literal["RESOURCE_TYPE", "SERVICE_NAME"]
ListEventTypesPaginatorName = Literal["list_event_types"]
ListNotificationRulesFilterNameType = Literal[
    "CREATED_BY", "EVENT_TYPE_ID", "RESOURCE", "TARGET_ADDRESS"
]
ListNotificationRulesPaginatorName = Literal["list_notification_rules"]
ListTargetsFilterNameType = Literal["TARGET_ADDRESS", "TARGET_STATUS", "TARGET_TYPE"]
ListTargetsPaginatorName = Literal["list_targets"]
NotificationRuleStatusType = Literal["DISABLED", "ENABLED"]
TargetStatusType = Literal["ACTIVE", "DEACTIVATED", "INACTIVE", "PENDING", "UNREACHABLE"]
