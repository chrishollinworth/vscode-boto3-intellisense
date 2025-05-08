"""
Type annotations for ssm-incidents service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_ssm_incidents.client import SSMIncidentsClient
    from mypy_boto3_ssm_incidents.paginator import (
        GetResourcePoliciesPaginator,
        ListIncidentFindingsPaginator,
        ListIncidentRecordsPaginator,
        ListRelatedItemsPaginator,
        ListReplicationSetsPaginator,
        ListResponsePlansPaginator,
        ListTimelineEventsPaginator,
    )

    session = Session()
    client: SSMIncidentsClient = session.client("ssm-incidents")

    get_resource_policies_paginator: GetResourcePoliciesPaginator = client.get_paginator("get_resource_policies")
    list_incident_findings_paginator: ListIncidentFindingsPaginator = client.get_paginator("list_incident_findings")
    list_incident_records_paginator: ListIncidentRecordsPaginator = client.get_paginator("list_incident_records")
    list_related_items_paginator: ListRelatedItemsPaginator = client.get_paginator("list_related_items")
    list_replication_sets_paginator: ListReplicationSetsPaginator = client.get_paginator("list_replication_sets")
    list_response_plans_paginator: ListResponsePlansPaginator = client.get_paginator("list_response_plans")
    list_timeline_events_paginator: ListTimelineEventsPaginator = client.get_paginator("list_timeline_events")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetResourcePoliciesInputPaginateTypeDef,
    GetResourcePoliciesOutputTypeDef,
    ListIncidentFindingsInputPaginateTypeDef,
    ListIncidentFindingsOutputTypeDef,
    ListIncidentRecordsInputPaginateTypeDef,
    ListIncidentRecordsOutputTypeDef,
    ListRelatedItemsInputPaginateTypeDef,
    ListRelatedItemsOutputTypeDef,
    ListReplicationSetsInputPaginateTypeDef,
    ListReplicationSetsOutputTypeDef,
    ListResponsePlansInputPaginateTypeDef,
    ListResponsePlansOutputTypeDef,
    ListTimelineEventsInputPaginateTypeDef,
    ListTimelineEventsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetResourcePoliciesPaginator",
    "ListIncidentFindingsPaginator",
    "ListIncidentRecordsPaginator",
    "ListRelatedItemsPaginator",
    "ListReplicationSetsPaginator",
    "ListResponsePlansPaginator",
    "ListTimelineEventsPaginator",
)

if TYPE_CHECKING:
    _GetResourcePoliciesPaginatorBase = Paginator[GetResourcePoliciesOutputTypeDef]
else:
    _GetResourcePoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class GetResourcePoliciesPaginator(_GetResourcePoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-incidents/paginator/GetResourcePolicies.html#SSMIncidents.Paginator.GetResourcePolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators/#getresourcepoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetResourcePoliciesInputPaginateTypeDef]
    ) -> PageIterator[GetResourcePoliciesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-incidents/paginator/GetResourcePolicies.html#SSMIncidents.Paginator.GetResourcePolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators/#getresourcepoliciespaginator)
        """

if TYPE_CHECKING:
    _ListIncidentFindingsPaginatorBase = Paginator[ListIncidentFindingsOutputTypeDef]
else:
    _ListIncidentFindingsPaginatorBase = Paginator  # type: ignore[assignment]

class ListIncidentFindingsPaginator(_ListIncidentFindingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-incidents/paginator/ListIncidentFindings.html#SSMIncidents.Paginator.ListIncidentFindings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators/#listincidentfindingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIncidentFindingsInputPaginateTypeDef]
    ) -> PageIterator[ListIncidentFindingsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-incidents/paginator/ListIncidentFindings.html#SSMIncidents.Paginator.ListIncidentFindings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators/#listincidentfindingspaginator)
        """

if TYPE_CHECKING:
    _ListIncidentRecordsPaginatorBase = Paginator[ListIncidentRecordsOutputTypeDef]
else:
    _ListIncidentRecordsPaginatorBase = Paginator  # type: ignore[assignment]

class ListIncidentRecordsPaginator(_ListIncidentRecordsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-incidents/paginator/ListIncidentRecords.html#SSMIncidents.Paginator.ListIncidentRecords)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators/#listincidentrecordspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIncidentRecordsInputPaginateTypeDef]
    ) -> PageIterator[ListIncidentRecordsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-incidents/paginator/ListIncidentRecords.html#SSMIncidents.Paginator.ListIncidentRecords.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators/#listincidentrecordspaginator)
        """

if TYPE_CHECKING:
    _ListRelatedItemsPaginatorBase = Paginator[ListRelatedItemsOutputTypeDef]
else:
    _ListRelatedItemsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRelatedItemsPaginator(_ListRelatedItemsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-incidents/paginator/ListRelatedItems.html#SSMIncidents.Paginator.ListRelatedItems)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators/#listrelateditemspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRelatedItemsInputPaginateTypeDef]
    ) -> PageIterator[ListRelatedItemsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-incidents/paginator/ListRelatedItems.html#SSMIncidents.Paginator.ListRelatedItems.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators/#listrelateditemspaginator)
        """

if TYPE_CHECKING:
    _ListReplicationSetsPaginatorBase = Paginator[ListReplicationSetsOutputTypeDef]
else:
    _ListReplicationSetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListReplicationSetsPaginator(_ListReplicationSetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-incidents/paginator/ListReplicationSets.html#SSMIncidents.Paginator.ListReplicationSets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators/#listreplicationsetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListReplicationSetsInputPaginateTypeDef]
    ) -> PageIterator[ListReplicationSetsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-incidents/paginator/ListReplicationSets.html#SSMIncidents.Paginator.ListReplicationSets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators/#listreplicationsetspaginator)
        """

if TYPE_CHECKING:
    _ListResponsePlansPaginatorBase = Paginator[ListResponsePlansOutputTypeDef]
else:
    _ListResponsePlansPaginatorBase = Paginator  # type: ignore[assignment]

class ListResponsePlansPaginator(_ListResponsePlansPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-incidents/paginator/ListResponsePlans.html#SSMIncidents.Paginator.ListResponsePlans)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators/#listresponseplanspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResponsePlansInputPaginateTypeDef]
    ) -> PageIterator[ListResponsePlansOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-incidents/paginator/ListResponsePlans.html#SSMIncidents.Paginator.ListResponsePlans.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators/#listresponseplanspaginator)
        """

if TYPE_CHECKING:
    _ListTimelineEventsPaginatorBase = Paginator[ListTimelineEventsOutputTypeDef]
else:
    _ListTimelineEventsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTimelineEventsPaginator(_ListTimelineEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-incidents/paginator/ListTimelineEvents.html#SSMIncidents.Paginator.ListTimelineEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators/#listtimelineeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTimelineEventsInputPaginateTypeDef]
    ) -> PageIterator[ListTimelineEventsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-incidents/paginator/ListTimelineEvents.html#SSMIncidents.Paginator.ListTimelineEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators/#listtimelineeventspaginator)
        """
