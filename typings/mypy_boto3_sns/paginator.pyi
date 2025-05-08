"""
Type annotations for sns service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_sns.client import SNSClient
    from mypy_boto3_sns.paginator import (
        ListEndpointsByPlatformApplicationPaginator,
        ListOriginationNumbersPaginator,
        ListPhoneNumbersOptedOutPaginator,
        ListPlatformApplicationsPaginator,
        ListSMSSandboxPhoneNumbersPaginator,
        ListSubscriptionsByTopicPaginator,
        ListSubscriptionsPaginator,
        ListTopicsPaginator,
    )

    session = Session()
    client: SNSClient = session.client("sns")

    list_endpoints_by_platform_application_paginator: ListEndpointsByPlatformApplicationPaginator = client.get_paginator("list_endpoints_by_platform_application")
    list_origination_numbers_paginator: ListOriginationNumbersPaginator = client.get_paginator("list_origination_numbers")
    list_phone_numbers_opted_out_paginator: ListPhoneNumbersOptedOutPaginator = client.get_paginator("list_phone_numbers_opted_out")
    list_platform_applications_paginator: ListPlatformApplicationsPaginator = client.get_paginator("list_platform_applications")
    list_sms_sandbox_phone_numbers_paginator: ListSMSSandboxPhoneNumbersPaginator = client.get_paginator("list_sms_sandbox_phone_numbers")
    list_subscriptions_by_topic_paginator: ListSubscriptionsByTopicPaginator = client.get_paginator("list_subscriptions_by_topic")
    list_subscriptions_paginator: ListSubscriptionsPaginator = client.get_paginator("list_subscriptions")
    list_topics_paginator: ListTopicsPaginator = client.get_paginator("list_topics")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListEndpointsByPlatformApplicationInputPaginateTypeDef,
    ListEndpointsByPlatformApplicationResponseTypeDef,
    ListOriginationNumbersRequestPaginateTypeDef,
    ListOriginationNumbersResultTypeDef,
    ListPhoneNumbersOptedOutInputPaginateTypeDef,
    ListPhoneNumbersOptedOutResponseTypeDef,
    ListPlatformApplicationsInputPaginateTypeDef,
    ListPlatformApplicationsResponseTypeDef,
    ListSMSSandboxPhoneNumbersInputPaginateTypeDef,
    ListSMSSandboxPhoneNumbersResultTypeDef,
    ListSubscriptionsByTopicInputPaginateTypeDef,
    ListSubscriptionsByTopicResponseTypeDef,
    ListSubscriptionsInputPaginateTypeDef,
    ListSubscriptionsResponseTypeDef,
    ListTopicsInputPaginateTypeDef,
    ListTopicsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListEndpointsByPlatformApplicationPaginator",
    "ListOriginationNumbersPaginator",
    "ListPhoneNumbersOptedOutPaginator",
    "ListPlatformApplicationsPaginator",
    "ListSMSSandboxPhoneNumbersPaginator",
    "ListSubscriptionsByTopicPaginator",
    "ListSubscriptionsPaginator",
    "ListTopicsPaginator",
)

if TYPE_CHECKING:
    _ListEndpointsByPlatformApplicationPaginatorBase = Paginator[
        ListEndpointsByPlatformApplicationResponseTypeDef
    ]
else:
    _ListEndpointsByPlatformApplicationPaginatorBase = Paginator  # type: ignore[assignment]

class ListEndpointsByPlatformApplicationPaginator(_ListEndpointsByPlatformApplicationPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/paginator/ListEndpointsByPlatformApplication.html#SNS.Paginator.ListEndpointsByPlatformApplication)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators/#listendpointsbyplatformapplicationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEndpointsByPlatformApplicationInputPaginateTypeDef]
    ) -> PageIterator[ListEndpointsByPlatformApplicationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/paginator/ListEndpointsByPlatformApplication.html#SNS.Paginator.ListEndpointsByPlatformApplication.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators/#listendpointsbyplatformapplicationpaginator)
        """

if TYPE_CHECKING:
    _ListOriginationNumbersPaginatorBase = Paginator[ListOriginationNumbersResultTypeDef]
else:
    _ListOriginationNumbersPaginatorBase = Paginator  # type: ignore[assignment]

class ListOriginationNumbersPaginator(_ListOriginationNumbersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/paginator/ListOriginationNumbers.html#SNS.Paginator.ListOriginationNumbers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators/#listoriginationnumberspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOriginationNumbersRequestPaginateTypeDef]
    ) -> PageIterator[ListOriginationNumbersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/paginator/ListOriginationNumbers.html#SNS.Paginator.ListOriginationNumbers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators/#listoriginationnumberspaginator)
        """

if TYPE_CHECKING:
    _ListPhoneNumbersOptedOutPaginatorBase = Paginator[ListPhoneNumbersOptedOutResponseTypeDef]
else:
    _ListPhoneNumbersOptedOutPaginatorBase = Paginator  # type: ignore[assignment]

class ListPhoneNumbersOptedOutPaginator(_ListPhoneNumbersOptedOutPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/paginator/ListPhoneNumbersOptedOut.html#SNS.Paginator.ListPhoneNumbersOptedOut)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators/#listphonenumbersoptedoutpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPhoneNumbersOptedOutInputPaginateTypeDef]
    ) -> PageIterator[ListPhoneNumbersOptedOutResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/paginator/ListPhoneNumbersOptedOut.html#SNS.Paginator.ListPhoneNumbersOptedOut.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators/#listphonenumbersoptedoutpaginator)
        """

if TYPE_CHECKING:
    _ListPlatformApplicationsPaginatorBase = Paginator[ListPlatformApplicationsResponseTypeDef]
else:
    _ListPlatformApplicationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPlatformApplicationsPaginator(_ListPlatformApplicationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/paginator/ListPlatformApplications.html#SNS.Paginator.ListPlatformApplications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators/#listplatformapplicationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPlatformApplicationsInputPaginateTypeDef]
    ) -> PageIterator[ListPlatformApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/paginator/ListPlatformApplications.html#SNS.Paginator.ListPlatformApplications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators/#listplatformapplicationspaginator)
        """

if TYPE_CHECKING:
    _ListSMSSandboxPhoneNumbersPaginatorBase = Paginator[ListSMSSandboxPhoneNumbersResultTypeDef]
else:
    _ListSMSSandboxPhoneNumbersPaginatorBase = Paginator  # type: ignore[assignment]

class ListSMSSandboxPhoneNumbersPaginator(_ListSMSSandboxPhoneNumbersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/paginator/ListSMSSandboxPhoneNumbers.html#SNS.Paginator.ListSMSSandboxPhoneNumbers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators/#listsmssandboxphonenumberspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSMSSandboxPhoneNumbersInputPaginateTypeDef]
    ) -> PageIterator[ListSMSSandboxPhoneNumbersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/paginator/ListSMSSandboxPhoneNumbers.html#SNS.Paginator.ListSMSSandboxPhoneNumbers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators/#listsmssandboxphonenumberspaginator)
        """

if TYPE_CHECKING:
    _ListSubscriptionsByTopicPaginatorBase = Paginator[ListSubscriptionsByTopicResponseTypeDef]
else:
    _ListSubscriptionsByTopicPaginatorBase = Paginator  # type: ignore[assignment]

class ListSubscriptionsByTopicPaginator(_ListSubscriptionsByTopicPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/paginator/ListSubscriptionsByTopic.html#SNS.Paginator.ListSubscriptionsByTopic)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators/#listsubscriptionsbytopicpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSubscriptionsByTopicInputPaginateTypeDef]
    ) -> PageIterator[ListSubscriptionsByTopicResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/paginator/ListSubscriptionsByTopic.html#SNS.Paginator.ListSubscriptionsByTopic.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators/#listsubscriptionsbytopicpaginator)
        """

if TYPE_CHECKING:
    _ListSubscriptionsPaginatorBase = Paginator[ListSubscriptionsResponseTypeDef]
else:
    _ListSubscriptionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSubscriptionsPaginator(_ListSubscriptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/paginator/ListSubscriptions.html#SNS.Paginator.ListSubscriptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators/#listsubscriptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSubscriptionsInputPaginateTypeDef]
    ) -> PageIterator[ListSubscriptionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/paginator/ListSubscriptions.html#SNS.Paginator.ListSubscriptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators/#listsubscriptionspaginator)
        """

if TYPE_CHECKING:
    _ListTopicsPaginatorBase = Paginator[ListTopicsResponseTypeDef]
else:
    _ListTopicsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTopicsPaginator(_ListTopicsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/paginator/ListTopics.html#SNS.Paginator.ListTopics)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators/#listtopicspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTopicsInputPaginateTypeDef]
    ) -> PageIterator[ListTopicsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/paginator/ListTopics.html#SNS.Paginator.ListTopics.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/paginators/#listtopicspaginator)
        """
