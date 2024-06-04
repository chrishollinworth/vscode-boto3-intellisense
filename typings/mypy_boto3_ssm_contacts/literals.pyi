"""
Type annotations for ssm-contacts service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/literals.html)

Usage::

    ```python
    from mypy_boto3_ssm_contacts.literals import AcceptCodeValidationType

    data: AcceptCodeValidationType = "ENFORCE"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AcceptCodeValidationType",
    "AcceptTypeType",
    "ActivationStatusType",
    "ChannelTypeType",
    "ContactTypeType",
    "DayOfWeekType",
    "ListContactChannelsPaginatorName",
    "ListContactsPaginatorName",
    "ListEngagementsPaginatorName",
    "ListPageReceiptsPaginatorName",
    "ListPageResolutionsPaginatorName",
    "ListPagesByContactPaginatorName",
    "ListPagesByEngagementPaginatorName",
    "ListPreviewRotationShiftsPaginatorName",
    "ListRotationOverridesPaginatorName",
    "ListRotationShiftsPaginatorName",
    "ListRotationsPaginatorName",
    "ReceiptTypeType",
    "ShiftTypeType",
)

AcceptCodeValidationType = Literal["ENFORCE", "IGNORE"]
AcceptTypeType = Literal["DELIVERED", "READ"]
ActivationStatusType = Literal["ACTIVATED", "NOT_ACTIVATED"]
ChannelTypeType = Literal["EMAIL", "SMS", "VOICE"]
ContactTypeType = Literal["ESCALATION", "ONCALL_SCHEDULE", "PERSONAL"]
DayOfWeekType = Literal["FRI", "MON", "SAT", "SUN", "THU", "TUE", "WED"]
ListContactChannelsPaginatorName = Literal["list_contact_channels"]
ListContactsPaginatorName = Literal["list_contacts"]
ListEngagementsPaginatorName = Literal["list_engagements"]
ListPageReceiptsPaginatorName = Literal["list_page_receipts"]
ListPageResolutionsPaginatorName = Literal["list_page_resolutions"]
ListPagesByContactPaginatorName = Literal["list_pages_by_contact"]
ListPagesByEngagementPaginatorName = Literal["list_pages_by_engagement"]
ListPreviewRotationShiftsPaginatorName = Literal["list_preview_rotation_shifts"]
ListRotationOverridesPaginatorName = Literal["list_rotation_overrides"]
ListRotationShiftsPaginatorName = Literal["list_rotation_shifts"]
ListRotationsPaginatorName = Literal["list_rotations"]
ReceiptTypeType = Literal["DELIVERED", "ERROR", "READ", "SENT", "STOP"]
ShiftTypeType = Literal["OVERRIDDEN", "REGULAR"]
