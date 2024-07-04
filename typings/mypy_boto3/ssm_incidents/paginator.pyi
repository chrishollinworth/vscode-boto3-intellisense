"""
Type annotations for ssm-incidents service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_ssm_incidents import SSMIncidentsClient
    from mypy_boto3_ssm_incidents.paginator import (
        GetResourcePoliciesPaginator,
        ListIncidentFindingsPaginator,
        ListIncidentRecordsPaginator,
        ListRelatedItemsPaginator,
        ListReplicationSetsPaginator,
        ListResponsePlansPaginator,
        ListTimelineEventsPaginator,
    )

    client: SSMIncidentsClient = boto3.client("ssm-incidents")

    get_resource_policies_paginator: GetResourcePoliciesPaginator = client.get_paginator("get_resource_policies")
    list_incident_findings_paginator: ListIncidentFindingsPaginator = client.get_paginator("list_incident_findings")
    list_incident_records_paginator: ListIncidentRecordsPaginator = client.get_paginator("list_incident_records")
    list_related_items_paginator: ListRelatedItemsPaginator = client.get_paginator("list_related_items")
    list_replication_sets_paginator: ListReplicationSetsPaginator = client.get_paginator("list_replication_sets")
    list_response_plans_paginator: ListResponsePlansPaginator = client.get_paginator("list_response_plans")
    list_timeline_events_paginator: ListTimelineEventsPaginator = client.get_paginator("list_timeline_events")
    ```
"""

import sys
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import SortOrderType
from .type_defs import (
    FilterTypeDef,
    GetResourcePoliciesOutputTypeDef,
    ListIncidentFindingsOutputTypeDef,
    ListIncidentRecordsOutputTypeDef,
    ListRelatedItemsOutputTypeDef,
    ListReplicationSetsOutputTypeDef,
    ListResponsePlansOutputTypeDef,
    ListTimelineEventsOutputTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "GetResourcePoliciesPaginator",
    "ListIncidentFindingsPaginator",
    "ListIncidentRecordsPaginator",
    "ListRelatedItemsPaginator",
    "ListReplicationSetsPaginator",
    "ListResponsePlansPaginator",
    "ListTimelineEventsPaginator",
)

class GetResourcePoliciesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ssm-incidents.html#SSMIncidents.Paginator.GetResourcePolicies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#getresourcepoliciespaginator)
    """

    def paginate(
        self, *, resourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetResourcePoliciesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ssm-incidents.html#SSMIncidents.Paginator.GetResourcePolicies.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#getresourcepoliciespaginator)
        """

class ListIncidentFindingsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ssm-incidents.html#SSMIncidents.Paginator.ListIncidentFindings)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#listincidentfindingspaginator)
    """

    def paginate(
        self, *, incidentRecordArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIncidentFindingsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ssm-incidents.html#SSMIncidents.Paginator.ListIncidentFindings.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#listincidentfindingspaginator)
        """

class ListIncidentRecordsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ssm-incidents.html#SSMIncidents.Paginator.ListIncidentRecords)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#listincidentrecordspaginator)
    """

    def paginate(
        self,
        *,
        filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIncidentRecordsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ssm-incidents.html#SSMIncidents.Paginator.ListIncidentRecords.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#listincidentrecordspaginator)
        """

class ListRelatedItemsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ssm-incidents.html#SSMIncidents.Paginator.ListRelatedItems)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#listrelateditemspaginator)
    """

    def paginate(
        self, *, incidentRecordArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRelatedItemsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ssm-incidents.html#SSMIncidents.Paginator.ListRelatedItems.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#listrelateditemspaginator)
        """

class ListReplicationSetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ssm-incidents.html#SSMIncidents.Paginator.ListReplicationSets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#listreplicationsetspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListReplicationSetsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ssm-incidents.html#SSMIncidents.Paginator.ListReplicationSets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#listreplicationsetspaginator)
        """

class ListResponsePlansPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ssm-incidents.html#SSMIncidents.Paginator.ListResponsePlans)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#listresponseplanspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResponsePlansOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ssm-incidents.html#SSMIncidents.Paginator.ListResponsePlans.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#listresponseplanspaginator)
        """

class ListTimelineEventsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ssm-incidents.html#SSMIncidents.Paginator.ListTimelineEvents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#listtimelineeventspaginator)
    """

    def paginate(
        self,
        *,
        incidentRecordArn: str,
        filters: List["FilterTypeDef"] = None,
        sortBy: Literal["EVENT_TIME"] = None,
        sortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTimelineEventsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ssm-incidents.html#SSMIncidents.Paginator.ListTimelineEvents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#listtimelineeventspaginator)
        """
