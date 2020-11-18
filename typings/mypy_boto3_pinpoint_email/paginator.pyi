# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for pinpoint-email service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_pinpoint_email import PinpointEmailClient
    from mypy_boto3_pinpoint_email.paginator import (
        GetDedicatedIpsPaginator,
        ListConfigurationSetsPaginator,
        ListDedicatedIpPoolsPaginator,
        ListDeliverabilityTestReportsPaginator,
        ListEmailIdentitiesPaginator,
    )

    client: PinpointEmailClient = boto3.client("pinpoint-email")

    get_dedicated_ips_paginator: GetDedicatedIpsPaginator = client.get_paginator("get_dedicated_ips")
    list_configuration_sets_paginator: ListConfigurationSetsPaginator = client.get_paginator("list_configuration_sets")
    list_dedicated_ip_pools_paginator: ListDedicatedIpPoolsPaginator = client.get_paginator("list_dedicated_ip_pools")
    list_deliverability_test_reports_paginator: ListDeliverabilityTestReportsPaginator = client.get_paginator("list_deliverability_test_reports")
    list_email_identities_paginator: ListEmailIdentitiesPaginator = client.get_paginator("list_email_identities")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_pinpoint_email.type_defs import (
    GetDedicatedIpsResponseTypeDef,
    ListConfigurationSetsResponseTypeDef,
    ListDedicatedIpPoolsResponseTypeDef,
    ListDeliverabilityTestReportsResponseTypeDef,
    ListEmailIdentitiesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "GetDedicatedIpsPaginator",
    "ListConfigurationSetsPaginator",
    "ListDedicatedIpPoolsPaginator",
    "ListDeliverabilityTestReportsPaginator",
    "ListEmailIdentitiesPaginator",
)


class GetDedicatedIpsPaginator(Boto3Paginator):
    """
    [Paginator.GetDedicatedIps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Paginator.GetDedicatedIps)
    """

    def paginate(
        self, PoolName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetDedicatedIpsResponseTypeDef]:
        """
        [GetDedicatedIps.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Paginator.GetDedicatedIps.paginate)
        """


class ListConfigurationSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListConfigurationSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListConfigurationSets)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConfigurationSetsResponseTypeDef]:
        """
        [ListConfigurationSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListConfigurationSets.paginate)
        """


class ListDedicatedIpPoolsPaginator(Boto3Paginator):
    """
    [Paginator.ListDedicatedIpPools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDedicatedIpPools)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDedicatedIpPoolsResponseTypeDef]:
        """
        [ListDedicatedIpPools.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDedicatedIpPools.paginate)
        """


class ListDeliverabilityTestReportsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeliverabilityTestReports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDeliverabilityTestReports)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeliverabilityTestReportsResponseTypeDef]:
        """
        [ListDeliverabilityTestReports.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDeliverabilityTestReports.paginate)
        """


class ListEmailIdentitiesPaginator(Boto3Paginator):
    """
    [Paginator.ListEmailIdentities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListEmailIdentities)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEmailIdentitiesResponseTypeDef]:
        """
        [ListEmailIdentities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListEmailIdentities.paginate)
        """
