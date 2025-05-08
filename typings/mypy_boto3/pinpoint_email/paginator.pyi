"""
Type annotations for pinpoint-email service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_pinpoint_email.client import PinpointEmailClient
    from mypy_boto3_pinpoint_email.paginator import (
        GetDedicatedIpsPaginator,
        ListConfigurationSetsPaginator,
        ListDedicatedIpPoolsPaginator,
        ListDeliverabilityTestReportsPaginator,
        ListEmailIdentitiesPaginator,
    )

    session = Session()
    client: PinpointEmailClient = session.client("pinpoint-email")

    get_dedicated_ips_paginator: GetDedicatedIpsPaginator = client.get_paginator("get_dedicated_ips")
    list_configuration_sets_paginator: ListConfigurationSetsPaginator = client.get_paginator("list_configuration_sets")
    list_dedicated_ip_pools_paginator: ListDedicatedIpPoolsPaginator = client.get_paginator("list_dedicated_ip_pools")
    list_deliverability_test_reports_paginator: ListDeliverabilityTestReportsPaginator = client.get_paginator("list_deliverability_test_reports")
    list_email_identities_paginator: ListEmailIdentitiesPaginator = client.get_paginator("list_email_identities")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetDedicatedIpsRequestPaginateTypeDef,
    GetDedicatedIpsResponseTypeDef,
    ListConfigurationSetsRequestPaginateTypeDef,
    ListConfigurationSetsResponseTypeDef,
    ListDedicatedIpPoolsRequestPaginateTypeDef,
    ListDedicatedIpPoolsResponseTypeDef,
    ListDeliverabilityTestReportsRequestPaginateTypeDef,
    ListDeliverabilityTestReportsResponseTypeDef,
    ListEmailIdentitiesRequestPaginateTypeDef,
    ListEmailIdentitiesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetDedicatedIpsPaginator",
    "ListConfigurationSetsPaginator",
    "ListDedicatedIpPoolsPaginator",
    "ListDeliverabilityTestReportsPaginator",
    "ListEmailIdentitiesPaginator",
)

if TYPE_CHECKING:
    _GetDedicatedIpsPaginatorBase = Paginator[GetDedicatedIpsResponseTypeDef]
else:
    _GetDedicatedIpsPaginatorBase = Paginator  # type: ignore[assignment]

class GetDedicatedIpsPaginator(_GetDedicatedIpsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-email/paginator/GetDedicatedIps.html#PinpointEmail.Paginator.GetDedicatedIps)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators/#getdedicatedipspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetDedicatedIpsRequestPaginateTypeDef]
    ) -> PageIterator[GetDedicatedIpsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-email/paginator/GetDedicatedIps.html#PinpointEmail.Paginator.GetDedicatedIps.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators/#getdedicatedipspaginator)
        """

if TYPE_CHECKING:
    _ListConfigurationSetsPaginatorBase = Paginator[ListConfigurationSetsResponseTypeDef]
else:
    _ListConfigurationSetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConfigurationSetsPaginator(_ListConfigurationSetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-email/paginator/ListConfigurationSets.html#PinpointEmail.Paginator.ListConfigurationSets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators/#listconfigurationsetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConfigurationSetsRequestPaginateTypeDef]
    ) -> PageIterator[ListConfigurationSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-email/paginator/ListConfigurationSets.html#PinpointEmail.Paginator.ListConfigurationSets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators/#listconfigurationsetspaginator)
        """

if TYPE_CHECKING:
    _ListDedicatedIpPoolsPaginatorBase = Paginator[ListDedicatedIpPoolsResponseTypeDef]
else:
    _ListDedicatedIpPoolsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDedicatedIpPoolsPaginator(_ListDedicatedIpPoolsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-email/paginator/ListDedicatedIpPools.html#PinpointEmail.Paginator.ListDedicatedIpPools)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators/#listdedicatedippoolspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDedicatedIpPoolsRequestPaginateTypeDef]
    ) -> PageIterator[ListDedicatedIpPoolsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-email/paginator/ListDedicatedIpPools.html#PinpointEmail.Paginator.ListDedicatedIpPools.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators/#listdedicatedippoolspaginator)
        """

if TYPE_CHECKING:
    _ListDeliverabilityTestReportsPaginatorBase = Paginator[
        ListDeliverabilityTestReportsResponseTypeDef
    ]
else:
    _ListDeliverabilityTestReportsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDeliverabilityTestReportsPaginator(_ListDeliverabilityTestReportsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-email/paginator/ListDeliverabilityTestReports.html#PinpointEmail.Paginator.ListDeliverabilityTestReports)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators/#listdeliverabilitytestreportspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDeliverabilityTestReportsRequestPaginateTypeDef]
    ) -> PageIterator[ListDeliverabilityTestReportsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-email/paginator/ListDeliverabilityTestReports.html#PinpointEmail.Paginator.ListDeliverabilityTestReports.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators/#listdeliverabilitytestreportspaginator)
        """

if TYPE_CHECKING:
    _ListEmailIdentitiesPaginatorBase = Paginator[ListEmailIdentitiesResponseTypeDef]
else:
    _ListEmailIdentitiesPaginatorBase = Paginator  # type: ignore[assignment]

class ListEmailIdentitiesPaginator(_ListEmailIdentitiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-email/paginator/ListEmailIdentities.html#PinpointEmail.Paginator.ListEmailIdentities)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators/#listemailidentitiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEmailIdentitiesRequestPaginateTypeDef]
    ) -> PageIterator[ListEmailIdentitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-email/paginator/ListEmailIdentities.html#PinpointEmail.Paginator.ListEmailIdentities.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators/#listemailidentitiespaginator)
        """
