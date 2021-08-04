"""
Type annotations for ssm-incidents service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/literals.html)

Usage::

    ```python
    from mypy_boto3_ssm_incidents.literals import GetResourcePoliciesPaginatorName

    data: GetResourcePoliciesPaginatorName = "get_resource_policies"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "GetResourcePoliciesPaginatorName",
    "IncidentRecordStatusType",
    "ItemTypeType",
    "ListIncidentRecordsPaginatorName",
    "ListRelatedItemsPaginatorName",
    "ListReplicationSetsPaginatorName",
    "ListResponsePlansPaginatorName",
    "ListTimelineEventsPaginatorName",
    "RegionStatusType",
    "ReplicationSetStatusType",
    "SortOrderType",
    "SsmTargetAccountType",
    "TimelineEventSortType",
    "WaitForReplicationSetActiveWaiterName",
    "WaitForReplicationSetDeletedWaiterName",
)

GetResourcePoliciesPaginatorName = Literal["get_resource_policies"]
IncidentRecordStatusType = Literal["OPEN", "RESOLVED"]
ItemTypeType = Literal["ANALYSIS", "ATTACHMENT", "INCIDENT", "METRIC", "OTHER", "PARENT"]
ListIncidentRecordsPaginatorName = Literal["list_incident_records"]
ListRelatedItemsPaginatorName = Literal["list_related_items"]
ListReplicationSetsPaginatorName = Literal["list_replication_sets"]
ListResponsePlansPaginatorName = Literal["list_response_plans"]
ListTimelineEventsPaginatorName = Literal["list_timeline_events"]
RegionStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]
ReplicationSetStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
SsmTargetAccountType = Literal["IMPACTED_ACCOUNT", "RESPONSE_PLAN_OWNER_ACCOUNT"]
TimelineEventSortType = Literal["EVENT_TIME"]
WaitForReplicationSetActiveWaiterName = Literal["wait_for_replication_set_active"]
WaitForReplicationSetDeletedWaiterName = Literal["wait_for_replication_set_deleted"]
