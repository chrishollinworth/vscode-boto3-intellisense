"""
Type annotations for pinpoint-email service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators.html)

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

from .type_defs import (
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/pinpoint-email.html#PinpointEmail.Paginator.GetDedicatedIps)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators.html#getdedicatedipspaginator)
    """

    def paginate(
        self, *, PoolName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetDedicatedIpsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/pinpoint-email.html#PinpointEmail.Paginator.GetDedicatedIps.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators.html#getdedicatedipspaginator)
        """

class ListConfigurationSetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListConfigurationSets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators.html#listconfigurationsetspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConfigurationSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListConfigurationSets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators.html#listconfigurationsetspaginator)
        """

class ListDedicatedIpPoolsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDedicatedIpPools)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators.html#listdedicatedippoolspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDedicatedIpPoolsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDedicatedIpPools.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators.html#listdedicatedippoolspaginator)
        """

class ListDeliverabilityTestReportsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDeliverabilityTestReports)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators.html#listdeliverabilitytestreportspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeliverabilityTestReportsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDeliverabilityTestReports.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators.html#listdeliverabilitytestreportspaginator)
        """

class ListEmailIdentitiesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListEmailIdentities)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators.html#listemailidentitiespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEmailIdentitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListEmailIdentities.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators.html#listemailidentitiespaginator)
        """
