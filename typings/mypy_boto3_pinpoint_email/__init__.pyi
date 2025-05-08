"""
Main interface for pinpoint-email service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_pinpoint_email import (
        Client,
        GetDedicatedIpsPaginator,
        ListConfigurationSetsPaginator,
        ListDedicatedIpPoolsPaginator,
        ListDeliverabilityTestReportsPaginator,
        ListEmailIdentitiesPaginator,
        PinpointEmailClient,
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

from .client import PinpointEmailClient
from .paginator import (
    GetDedicatedIpsPaginator,
    ListConfigurationSetsPaginator,
    ListDedicatedIpPoolsPaginator,
    ListDeliverabilityTestReportsPaginator,
    ListEmailIdentitiesPaginator,
)

Client = PinpointEmailClient

__all__ = (
    "Client",
    "GetDedicatedIpsPaginator",
    "ListConfigurationSetsPaginator",
    "ListDedicatedIpPoolsPaginator",
    "ListDeliverabilityTestReportsPaginator",
    "ListEmailIdentitiesPaginator",
    "PinpointEmailClient",
)
