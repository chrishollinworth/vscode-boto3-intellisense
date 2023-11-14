"""
Type annotations for ssm-contacts service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_ssm_contacts import SSMContactsClient
    from mypy_boto3_ssm_contacts.paginator import (
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

    client: SSMContactsClient = boto3.client("ssm-contacts")

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
from datetime import datetime
from typing import Iterator, List, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import ContactTypeType
from .type_defs import (
    ListContactChannelsResultTypeDef,
    ListContactsResultTypeDef,
    ListEngagementsResultTypeDef,
    ListPageReceiptsResultTypeDef,
    ListPageResolutionsResultTypeDef,
    ListPagesByContactResultTypeDef,
    ListPagesByEngagementResultTypeDef,
    ListPreviewRotationShiftsResultTypeDef,
    ListRotationOverridesResultTypeDef,
    ListRotationShiftsResultTypeDef,
    ListRotationsResultTypeDef,
    PaginatorConfigTypeDef,
    PreviewOverrideTypeDef,
    RecurrenceSettingsTypeDef,
    TimeRangeTypeDef,
)

__all__ = (
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
)

class ListContactChannelsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListContactChannels)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listcontactchannelspaginator)
    """

    def paginate(
        self, *, ContactId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListContactChannelsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListContactChannels.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listcontactchannelspaginator)
        """

class ListContactsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListContacts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listcontactspaginator)
    """

    def paginate(
        self,
        *,
        AliasPrefix: str = None,
        Type: ContactTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListContactsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListContacts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listcontactspaginator)
        """

class ListEngagementsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListEngagements)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listengagementspaginator)
    """

    def paginate(
        self,
        *,
        IncidentId: str = None,
        TimeRangeValue: "TimeRangeTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEngagementsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListEngagements.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listengagementspaginator)
        """

class ListPageReceiptsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPageReceipts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listpagereceiptspaginator)
    """

    def paginate(
        self, *, PageId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPageReceiptsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPageReceipts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listpagereceiptspaginator)
        """

class ListPageResolutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPageResolutions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listpageresolutionspaginator)
    """

    def paginate(
        self, *, PageId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPageResolutionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPageResolutions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listpageresolutionspaginator)
        """

class ListPagesByContactPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPagesByContact)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listpagesbycontactpaginator)
    """

    def paginate(
        self, *, ContactId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPagesByContactResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPagesByContact.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listpagesbycontactpaginator)
        """

class ListPagesByEngagementPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPagesByEngagement)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listpagesbyengagementpaginator)
    """

    def paginate(
        self, *, EngagementId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPagesByEngagementResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPagesByEngagement.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listpagesbyengagementpaginator)
        """

class ListPreviewRotationShiftsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPreviewRotationShifts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listpreviewrotationshiftspaginator)
    """

    def paginate(
        self,
        *,
        EndTime: Union[datetime, str],
        Members: List[str],
        TimeZoneId: str,
        Recurrence: "RecurrenceSettingsTypeDef",
        RotationStartTime: Union[datetime, str] = None,
        StartTime: Union[datetime, str] = None,
        Overrides: List["PreviewOverrideTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPreviewRotationShiftsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPreviewRotationShifts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listpreviewrotationshiftspaginator)
        """

class ListRotationOverridesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListRotationOverrides)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listrotationoverridespaginator)
    """

    def paginate(
        self,
        *,
        RotationId: str,
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRotationOverridesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListRotationOverrides.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listrotationoverridespaginator)
        """

class ListRotationShiftsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListRotationShifts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listrotationshiftspaginator)
    """

    def paginate(
        self,
        *,
        RotationId: str,
        EndTime: Union[datetime, str],
        StartTime: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRotationShiftsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListRotationShifts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listrotationshiftspaginator)
        """

class ListRotationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListRotations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listrotationspaginator)
    """

    def paginate(
        self, *, RotationNamePrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRotationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListRotations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listrotationspaginator)
        """
