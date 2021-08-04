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
    "ListContactChannelsPaginatorName",
    "ListContactsPaginatorName",
    "ListEngagementsPaginatorName",
    "ListPageReceiptsPaginatorName",
    "ListPagesByContactPaginatorName",
    "ListPagesByEngagementPaginatorName",
    "ReceiptTypeType",
)

AcceptCodeValidationType = Literal["ENFORCE", "IGNORE"]
AcceptTypeType = Literal["DELIVERED", "READ"]
ActivationStatusType = Literal["ACTIVATED", "NOT_ACTIVATED"]
ChannelTypeType = Literal["EMAIL", "SMS", "VOICE"]
ContactTypeType = Literal["ESCALATION", "PERSONAL"]
ListContactChannelsPaginatorName = Literal["list_contact_channels"]
ListContactsPaginatorName = Literal["list_contacts"]
ListEngagementsPaginatorName = Literal["list_engagements"]
ListPageReceiptsPaginatorName = Literal["list_page_receipts"]
ListPagesByContactPaginatorName = Literal["list_pages_by_contact"]
ListPagesByEngagementPaginatorName = Literal["list_pages_by_engagement"]
ReceiptTypeType = Literal["DELIVERED", "ERROR", "READ", "SENT", "STOP"]
