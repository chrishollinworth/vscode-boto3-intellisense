"""
Main interface for guardduty service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_guardduty import (
        Client,
        DescribeMalwareScansPaginator,
        GuardDutyClient,
        ListCoveragePaginator,
        ListDetectorsPaginator,
        ListFiltersPaginator,
        ListFindingsPaginator,
        ListIPSetsPaginator,
        ListInvitationsPaginator,
        ListMalwareScansPaginator,
        ListMembersPaginator,
        ListOrganizationAdminAccountsPaginator,
        ListThreatEntitySetsPaginator,
        ListThreatIntelSetsPaginator,
        ListTrustedEntitySetsPaginator,
    )

    session = Session()
    client: GuardDutyClient = session.client("guardduty")

    describe_malware_scans_paginator: DescribeMalwareScansPaginator = client.get_paginator("describe_malware_scans")
    list_coverage_paginator: ListCoveragePaginator = client.get_paginator("list_coverage")
    list_detectors_paginator: ListDetectorsPaginator = client.get_paginator("list_detectors")
    list_filters_paginator: ListFiltersPaginator = client.get_paginator("list_filters")
    list_findings_paginator: ListFindingsPaginator = client.get_paginator("list_findings")
    list_ip_sets_paginator: ListIPSetsPaginator = client.get_paginator("list_ip_sets")
    list_invitations_paginator: ListInvitationsPaginator = client.get_paginator("list_invitations")
    list_malware_scans_paginator: ListMalwareScansPaginator = client.get_paginator("list_malware_scans")
    list_members_paginator: ListMembersPaginator = client.get_paginator("list_members")
    list_organization_admin_accounts_paginator: ListOrganizationAdminAccountsPaginator = client.get_paginator("list_organization_admin_accounts")
    list_threat_entity_sets_paginator: ListThreatEntitySetsPaginator = client.get_paginator("list_threat_entity_sets")
    list_threat_intel_sets_paginator: ListThreatIntelSetsPaginator = client.get_paginator("list_threat_intel_sets")
    list_trusted_entity_sets_paginator: ListTrustedEntitySetsPaginator = client.get_paginator("list_trusted_entity_sets")
    ```
"""

from .client import GuardDutyClient
from .paginator import (
    DescribeMalwareScansPaginator,
    ListCoveragePaginator,
    ListDetectorsPaginator,
    ListFiltersPaginator,
    ListFindingsPaginator,
    ListInvitationsPaginator,
    ListIPSetsPaginator,
    ListMalwareScansPaginator,
    ListMembersPaginator,
    ListOrganizationAdminAccountsPaginator,
    ListThreatEntitySetsPaginator,
    ListThreatIntelSetsPaginator,
    ListTrustedEntitySetsPaginator,
)

Client = GuardDutyClient

__all__ = (
    "Client",
    "DescribeMalwareScansPaginator",
    "GuardDutyClient",
    "ListCoveragePaginator",
    "ListDetectorsPaginator",
    "ListFiltersPaginator",
    "ListFindingsPaginator",
    "ListIPSetsPaginator",
    "ListInvitationsPaginator",
    "ListMalwareScansPaginator",
    "ListMembersPaginator",
    "ListOrganizationAdminAccountsPaginator",
    "ListThreatEntitySetsPaginator",
    "ListThreatIntelSetsPaginator",
    "ListTrustedEntitySetsPaginator",
)
