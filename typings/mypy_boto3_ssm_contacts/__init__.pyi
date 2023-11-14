"""
Main interface for ssm-contacts service.

Usage::

    ```python
    import boto3
    from mypy_boto3_ssm_contacts import (
        Client,
        ListContactChannelsPaginator,
        ListContactsPaginator,
        ListEngagementsPaginator,
        ListPageReceiptsPaginator,
        ListPageResolutionsPaginator,
        ListPagesByContactPaginator,
        ListPagesByEngagementPaginator,
        ListPreviewRotationShiftsPaginator,
        ListRotationOverridesPaginator,
        ListRotationShiftsPaginator,
        ListRotationsPaginator,
        SSMContactsClient,
    )

    session = boto3.Session()

    client: SSMContactsClient = boto3.client("ssm-contacts")
    session_client: SSMContactsClient = session.client("ssm-contacts")

    list_contact_channels_paginator: ListContactChannelsPaginator = client.get_paginator("list_contact_channels")
    list_contacts_paginator: ListContactsPaginator = client.get_paginator("list_contacts")
    list_engagements_paginator: ListEngagementsPaginator = client.get_paginator("list_engagements")
    list_page_receipts_paginator: ListPageReceiptsPaginator = client.get_paginator("list_page_receipts")
    list_page_resolutions_paginator: ListPageResolutionsPaginator = client.get_paginator("list_page_resolutions")
    list_pages_by_contact_paginator: ListPagesByContactPaginator = client.get_paginator("list_pages_by_contact")
    list_pages_by_engagement_paginator: ListPagesByEngagementPaginator = client.get_paginator("list_pages_by_engagement")
    list_preview_rotation_shifts_paginator: ListPreviewRotationShiftsPaginator = client.get_paginator("list_preview_rotation_shifts")
    list_rotation_overrides_paginator: ListRotationOverridesPaginator = client.get_paginator("list_rotation_overrides")
    list_rotation_shifts_paginator: ListRotationShiftsPaginator = client.get_paginator("list_rotation_shifts")
    list_rotations_paginator: ListRotationsPaginator = client.get_paginator("list_rotations")
    ```
"""
from .client import SSMContactsClient
from .paginator import (
    ListContactChannelsPaginator,
    ListContactsPaginator,
    ListEngagementsPaginator,
    ListPageReceiptsPaginator,
    ListPageResolutionsPaginator,
    ListPagesByContactPaginator,
    ListPagesByEngagementPaginator,
    ListPreviewRotationShiftsPaginator,
    ListRotationOverridesPaginator,
    ListRotationShiftsPaginator,
    ListRotationsPaginator,
)

Client = SSMContactsClient

__all__ = (
    "Client",
    "ListContactChannelsPaginator",
    "ListContactsPaginator",
    "ListEngagementsPaginator",
    "ListPageReceiptsPaginator",
    "ListPageResolutionsPaginator",
    "ListPagesByContactPaginator",
    "ListPagesByEngagementPaginator",
    "ListPreviewRotationShiftsPaginator",
    "ListRotationOverridesPaginator",
    "ListRotationShiftsPaginator",
    "ListRotationsPaginator",
    "SSMContactsClient",
)
