"""
Type annotations for ssm-contacts service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_ssm_contacts.client import SSMContactsClient
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

    session = Session()
    client: SSMContactsClient = session.client("ssm-contacts")

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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListContactChannelsRequestPaginateTypeDef,
    ListContactChannelsResultTypeDef,
    ListContactsRequestPaginateTypeDef,
    ListContactsResultTypeDef,
    ListEngagementsRequestPaginateTypeDef,
    ListEngagementsResultTypeDef,
    ListPageReceiptsRequestPaginateTypeDef,
    ListPageReceiptsResultTypeDef,
    ListPageResolutionsRequestPaginateTypeDef,
    ListPageResolutionsResultTypeDef,
    ListPagesByContactRequestPaginateTypeDef,
    ListPagesByContactResultTypeDef,
    ListPagesByEngagementRequestPaginateTypeDef,
    ListPagesByEngagementResultTypeDef,
    ListPreviewRotationShiftsRequestPaginateTypeDef,
    ListPreviewRotationShiftsResultTypeDef,
    ListRotationOverridesRequestPaginateTypeDef,
    ListRotationOverridesResultTypeDef,
    ListRotationShiftsRequestPaginateTypeDef,
    ListRotationShiftsResultTypeDef,
    ListRotationsRequestPaginateTypeDef,
    ListRotationsResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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

if TYPE_CHECKING:
    _ListContactChannelsPaginatorBase = Paginator[ListContactChannelsResultTypeDef]
else:
    _ListContactChannelsPaginatorBase = Paginator  # type: ignore[assignment]

class ListContactChannelsPaginator(_ListContactChannelsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/paginator/ListContactChannels.html#SSMContacts.Paginator.ListContactChannels)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators/#listcontactchannelspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListContactChannelsRequestPaginateTypeDef]
    ) -> PageIterator[ListContactChannelsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/paginator/ListContactChannels.html#SSMContacts.Paginator.ListContactChannels.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators/#listcontactchannelspaginator)
        """

if TYPE_CHECKING:
    _ListContactsPaginatorBase = Paginator[ListContactsResultTypeDef]
else:
    _ListContactsPaginatorBase = Paginator  # type: ignore[assignment]

class ListContactsPaginator(_ListContactsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/paginator/ListContacts.html#SSMContacts.Paginator.ListContacts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators/#listcontactspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListContactsRequestPaginateTypeDef]
    ) -> PageIterator[ListContactsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/paginator/ListContacts.html#SSMContacts.Paginator.ListContacts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators/#listcontactspaginator)
        """

if TYPE_CHECKING:
    _ListEngagementsPaginatorBase = Paginator[ListEngagementsResultTypeDef]
else:
    _ListEngagementsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEngagementsPaginator(_ListEngagementsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/paginator/ListEngagements.html#SSMContacts.Paginator.ListEngagements)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators/#listengagementspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEngagementsRequestPaginateTypeDef]
    ) -> PageIterator[ListEngagementsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/paginator/ListEngagements.html#SSMContacts.Paginator.ListEngagements.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators/#listengagementspaginator)
        """

if TYPE_CHECKING:
    _ListPageReceiptsPaginatorBase = Paginator[ListPageReceiptsResultTypeDef]
else:
    _ListPageReceiptsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPageReceiptsPaginator(_ListPageReceiptsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/paginator/ListPageReceipts.html#SSMContacts.Paginator.ListPageReceipts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators/#listpagereceiptspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPageReceiptsRequestPaginateTypeDef]
    ) -> PageIterator[ListPageReceiptsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/paginator/ListPageReceipts.html#SSMContacts.Paginator.ListPageReceipts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators/#listpagereceiptspaginator)
        """

if TYPE_CHECKING:
    _ListPageResolutionsPaginatorBase = Paginator[ListPageResolutionsResultTypeDef]
else:
    _ListPageResolutionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPageResolutionsPaginator(_ListPageResolutionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/paginator/ListPageResolutions.html#SSMContacts.Paginator.ListPageResolutions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators/#listpageresolutionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPageResolutionsRequestPaginateTypeDef]
    ) -> PageIterator[ListPageResolutionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/paginator/ListPageResolutions.html#SSMContacts.Paginator.ListPageResolutions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators/#listpageresolutionspaginator)
        """

if TYPE_CHECKING:
    _ListPagesByContactPaginatorBase = Paginator[ListPagesByContactResultTypeDef]
else:
    _ListPagesByContactPaginatorBase = Paginator  # type: ignore[assignment]

class ListPagesByContactPaginator(_ListPagesByContactPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/paginator/ListPagesByContact.html#SSMContacts.Paginator.ListPagesByContact)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators/#listpagesbycontactpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPagesByContactRequestPaginateTypeDef]
    ) -> PageIterator[ListPagesByContactResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/paginator/ListPagesByContact.html#SSMContacts.Paginator.ListPagesByContact.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators/#listpagesbycontactpaginator)
        """

if TYPE_CHECKING:
    _ListPagesByEngagementPaginatorBase = Paginator[ListPagesByEngagementResultTypeDef]
else:
    _ListPagesByEngagementPaginatorBase = Paginator  # type: ignore[assignment]

class ListPagesByEngagementPaginator(_ListPagesByEngagementPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/paginator/ListPagesByEngagement.html#SSMContacts.Paginator.ListPagesByEngagement)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators/#listpagesbyengagementpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPagesByEngagementRequestPaginateTypeDef]
    ) -> PageIterator[ListPagesByEngagementResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/paginator/ListPagesByEngagement.html#SSMContacts.Paginator.ListPagesByEngagement.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators/#listpagesbyengagementpaginator)
        """

if TYPE_CHECKING:
    _ListPreviewRotationShiftsPaginatorBase = Paginator[ListPreviewRotationShiftsResultTypeDef]
else:
    _ListPreviewRotationShiftsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPreviewRotationShiftsPaginator(_ListPreviewRotationShiftsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/paginator/ListPreviewRotationShifts.html#SSMContacts.Paginator.ListPreviewRotationShifts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators/#listpreviewrotationshiftspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPreviewRotationShiftsRequestPaginateTypeDef]
    ) -> PageIterator[ListPreviewRotationShiftsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/paginator/ListPreviewRotationShifts.html#SSMContacts.Paginator.ListPreviewRotationShifts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators/#listpreviewrotationshiftspaginator)
        """

if TYPE_CHECKING:
    _ListRotationOverridesPaginatorBase = Paginator[ListRotationOverridesResultTypeDef]
else:
    _ListRotationOverridesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRotationOverridesPaginator(_ListRotationOverridesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/paginator/ListRotationOverrides.html#SSMContacts.Paginator.ListRotationOverrides)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators/#listrotationoverridespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRotationOverridesRequestPaginateTypeDef]
    ) -> PageIterator[ListRotationOverridesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/paginator/ListRotationOverrides.html#SSMContacts.Paginator.ListRotationOverrides.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators/#listrotationoverridespaginator)
        """

if TYPE_CHECKING:
    _ListRotationShiftsPaginatorBase = Paginator[ListRotationShiftsResultTypeDef]
else:
    _ListRotationShiftsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRotationShiftsPaginator(_ListRotationShiftsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/paginator/ListRotationShifts.html#SSMContacts.Paginator.ListRotationShifts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators/#listrotationshiftspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRotationShiftsRequestPaginateTypeDef]
    ) -> PageIterator[ListRotationShiftsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/paginator/ListRotationShifts.html#SSMContacts.Paginator.ListRotationShifts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators/#listrotationshiftspaginator)
        """

if TYPE_CHECKING:
    _ListRotationsPaginatorBase = Paginator[ListRotationsResultTypeDef]
else:
    _ListRotationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRotationsPaginator(_ListRotationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/paginator/ListRotations.html#SSMContacts.Paginator.ListRotations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators/#listrotationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRotationsRequestPaginateTypeDef]
    ) -> PageIterator[ListRotationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/paginator/ListRotations.html#SSMContacts.Paginator.ListRotations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators/#listrotationspaginator)
        """
