"""
Type annotations for guardduty service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/literals.html)

Usage::

    ```python
    from mypy_boto3_guardduty.literals import AdminStatusType

    data: AdminStatusType = "DISABLE_IN_PROGRESS"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AdminStatusType",
    "DataSourceStatusType",
    "DataSourceType",
    "DestinationTypeType",
    "DetectorStatusType",
    "FeedbackType",
    "FilterActionType",
    "FindingPublishingFrequencyType",
    "FindingStatisticTypeType",
    "IpSetFormatType",
    "IpSetStatusType",
    "ListDetectorsPaginatorName",
    "ListFiltersPaginatorName",
    "ListFindingsPaginatorName",
    "ListIPSetsPaginatorName",
    "ListInvitationsPaginatorName",
    "ListMembersPaginatorName",
    "ListOrganizationAdminAccountsPaginatorName",
    "ListThreatIntelSetsPaginatorName",
    "OrderByType",
    "PublishingStatusType",
    "ThreatIntelSetFormatType",
    "ThreatIntelSetStatusType",
    "UsageStatisticTypeType",
)

AdminStatusType = Literal["DISABLE_IN_PROGRESS", "ENABLED"]
DataSourceStatusType = Literal["DISABLED", "ENABLED"]
DataSourceType = Literal["CLOUD_TRAIL", "DNS_LOGS", "FLOW_LOGS", "S3_LOGS"]
DestinationTypeType = Literal["S3"]
DetectorStatusType = Literal["DISABLED", "ENABLED"]
FeedbackType = Literal["NOT_USEFUL", "USEFUL"]
FilterActionType = Literal["ARCHIVE", "NOOP"]
FindingPublishingFrequencyType = Literal["FIFTEEN_MINUTES", "ONE_HOUR", "SIX_HOURS"]
FindingStatisticTypeType = Literal["COUNT_BY_SEVERITY"]
IpSetFormatType = Literal["ALIEN_VAULT", "FIRE_EYE", "OTX_CSV", "PROOF_POINT", "STIX", "TXT"]
IpSetStatusType = Literal[
    "ACTIVATING", "ACTIVE", "DEACTIVATING", "DELETED", "DELETE_PENDING", "ERROR", "INACTIVE"
]
ListDetectorsPaginatorName = Literal["list_detectors"]
ListFiltersPaginatorName = Literal["list_filters"]
ListFindingsPaginatorName = Literal["list_findings"]
ListIPSetsPaginatorName = Literal["list_ip_sets"]
ListInvitationsPaginatorName = Literal["list_invitations"]
ListMembersPaginatorName = Literal["list_members"]
ListOrganizationAdminAccountsPaginatorName = Literal["list_organization_admin_accounts"]
ListThreatIntelSetsPaginatorName = Literal["list_threat_intel_sets"]
OrderByType = Literal["ASC", "DESC"]
PublishingStatusType = Literal[
    "PENDING_VERIFICATION", "PUBLISHING", "STOPPED", "UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY"
]
ThreatIntelSetFormatType = Literal[
    "ALIEN_VAULT", "FIRE_EYE", "OTX_CSV", "PROOF_POINT", "STIX", "TXT"
]
ThreatIntelSetStatusType = Literal[
    "ACTIVATING", "ACTIVE", "DEACTIVATING", "DELETED", "DELETE_PENDING", "ERROR", "INACTIVE"
]
UsageStatisticTypeType = Literal[
    "SUM_BY_ACCOUNT", "SUM_BY_DATA_SOURCE", "SUM_BY_RESOURCE", "TOP_RESOURCES"
]
