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
        ListPagesByContactPaginator,
        ListPagesByEngagementPaginator,
    )

    client: SSMContactsClient = boto3.client("ssm-contacts")

    list_contact_channels_paginator: ListContactChannelsPaginator = client.get_paginator("list_contact_channels")
    list_contacts_paginator: ListContactsPaginator = client.get_paginator("list_contacts")
    list_engagements_paginator: ListEngagementsPaginator = client.get_paginator("list_engagements")
    list_page_receipts_paginator: ListPageReceiptsPaginator = client.get_paginator("list_page_receipts")
    list_pages_by_contact_paginator: ListPagesByContactPaginator = client.get_paginator("list_pages_by_contact")
    list_pages_by_engagement_paginator: ListPagesByEngagementPaginator = client.get_paginator("list_pages_by_engagement")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import ContactTypeType
from .type_defs import (
    ListContactChannelsResultTypeDef,
    ListContactsResultTypeDef,
    ListEngagementsResultTypeDef,
    ListPageReceiptsResultTypeDef,
    ListPagesByContactResultTypeDef,
    ListPagesByEngagementResultTypeDef,
    PaginatorConfigTypeDef,
    TimeRangeTypeDef,
)

__all__ = (
    "ListContactChannelsPaginator",
    "ListContactsPaginator",
    "ListEngagementsPaginator",
    "ListPageReceiptsPaginator",
    "ListPagesByContactPaginator",
    "ListPagesByEngagementPaginator",
)

class ListContactChannelsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListContactChannels)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listcontactchannelspaginator)
    """

    def paginate(
        self, *, ContactId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListContactChannelsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListContactChannels.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listcontactchannelspaginator)
        """

class ListContactsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListContacts)
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListContacts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listcontactspaginator)
        """

class ListEngagementsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListEngagements)
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListEngagements.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listengagementspaginator)
        """

class ListPageReceiptsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPageReceipts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listpagereceiptspaginator)
    """

    def paginate(
        self, *, PageId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPageReceiptsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPageReceipts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listpagereceiptspaginator)
        """

class ListPagesByContactPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPagesByContact)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listpagesbycontactpaginator)
    """

    def paginate(
        self, *, ContactId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPagesByContactResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPagesByContact.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listpagesbycontactpaginator)
        """

class ListPagesByEngagementPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPagesByEngagement)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listpagesbyengagementpaginator)
    """

    def paginate(
        self, *, EngagementId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPagesByEngagementResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPagesByEngagement.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/paginators.html#listpagesbyengagementpaginator)
        """
