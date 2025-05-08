"""
Main interface for macie2 service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_macie2 import (
        Client,
        DescribeBucketsPaginator,
        FindingRevealedWaiter,
        GetUsageStatisticsPaginator,
        ListAllowListsPaginator,
        ListAutomatedDiscoveryAccountsPaginator,
        ListClassificationJobsPaginator,
        ListClassificationScopesPaginator,
        ListCustomDataIdentifiersPaginator,
        ListFindingsFiltersPaginator,
        ListFindingsPaginator,
        ListInvitationsPaginator,
        ListManagedDataIdentifiersPaginator,
        ListMembersPaginator,
        ListOrganizationAdminAccountsPaginator,
        ListResourceProfileArtifactsPaginator,
        ListResourceProfileDetectionsPaginator,
        ListSensitivityInspectionTemplatesPaginator,
        Macie2Client,
        SearchResourcesPaginator,
    )

    session = Session()
    client: Macie2Client = session.client("macie2")

    finding_revealed_waiter: FindingRevealedWaiter = client.get_waiter("finding_revealed")

    describe_buckets_paginator: DescribeBucketsPaginator = client.get_paginator("describe_buckets")
    get_usage_statistics_paginator: GetUsageStatisticsPaginator = client.get_paginator("get_usage_statistics")
    list_allow_lists_paginator: ListAllowListsPaginator = client.get_paginator("list_allow_lists")
    list_automated_discovery_accounts_paginator: ListAutomatedDiscoveryAccountsPaginator = client.get_paginator("list_automated_discovery_accounts")
    list_classification_jobs_paginator: ListClassificationJobsPaginator = client.get_paginator("list_classification_jobs")
    list_classification_scopes_paginator: ListClassificationScopesPaginator = client.get_paginator("list_classification_scopes")
    list_custom_data_identifiers_paginator: ListCustomDataIdentifiersPaginator = client.get_paginator("list_custom_data_identifiers")
    list_findings_filters_paginator: ListFindingsFiltersPaginator = client.get_paginator("list_findings_filters")
    list_findings_paginator: ListFindingsPaginator = client.get_paginator("list_findings")
    list_invitations_paginator: ListInvitationsPaginator = client.get_paginator("list_invitations")
    list_managed_data_identifiers_paginator: ListManagedDataIdentifiersPaginator = client.get_paginator("list_managed_data_identifiers")
    list_members_paginator: ListMembersPaginator = client.get_paginator("list_members")
    list_organization_admin_accounts_paginator: ListOrganizationAdminAccountsPaginator = client.get_paginator("list_organization_admin_accounts")
    list_resource_profile_artifacts_paginator: ListResourceProfileArtifactsPaginator = client.get_paginator("list_resource_profile_artifacts")
    list_resource_profile_detections_paginator: ListResourceProfileDetectionsPaginator = client.get_paginator("list_resource_profile_detections")
    list_sensitivity_inspection_templates_paginator: ListSensitivityInspectionTemplatesPaginator = client.get_paginator("list_sensitivity_inspection_templates")
    search_resources_paginator: SearchResourcesPaginator = client.get_paginator("search_resources")
    ```
"""

from .client import Macie2Client
from .paginator import (
    DescribeBucketsPaginator,
    GetUsageStatisticsPaginator,
    ListAllowListsPaginator,
    ListAutomatedDiscoveryAccountsPaginator,
    ListClassificationJobsPaginator,
    ListClassificationScopesPaginator,
    ListCustomDataIdentifiersPaginator,
    ListFindingsFiltersPaginator,
    ListFindingsPaginator,
    ListInvitationsPaginator,
    ListManagedDataIdentifiersPaginator,
    ListMembersPaginator,
    ListOrganizationAdminAccountsPaginator,
    ListResourceProfileArtifactsPaginator,
    ListResourceProfileDetectionsPaginator,
    ListSensitivityInspectionTemplatesPaginator,
    SearchResourcesPaginator,
)
from .waiter import FindingRevealedWaiter

Client = Macie2Client

__all__ = (
    "Client",
    "DescribeBucketsPaginator",
    "FindingRevealedWaiter",
    "GetUsageStatisticsPaginator",
    "ListAllowListsPaginator",
    "ListAutomatedDiscoveryAccountsPaginator",
    "ListClassificationJobsPaginator",
    "ListClassificationScopesPaginator",
    "ListCustomDataIdentifiersPaginator",
    "ListFindingsFiltersPaginator",
    "ListFindingsPaginator",
    "ListInvitationsPaginator",
    "ListManagedDataIdentifiersPaginator",
    "ListMembersPaginator",
    "ListOrganizationAdminAccountsPaginator",
    "ListResourceProfileArtifactsPaginator",
    "ListResourceProfileDetectionsPaginator",
    "ListSensitivityInspectionTemplatesPaginator",
    "Macie2Client",
    "SearchResourcesPaginator",
)
