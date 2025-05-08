"""
Type annotations for redshift-serverless service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_redshift_serverless.client import RedshiftServerlessClient
    from mypy_boto3_redshift_serverless.paginator import (
        ListCustomDomainAssociationsPaginator,
        ListEndpointAccessPaginator,
        ListManagedWorkgroupsPaginator,
        ListNamespacesPaginator,
        ListRecoveryPointsPaginator,
        ListReservationOfferingsPaginator,
        ListReservationsPaginator,
        ListScheduledActionsPaginator,
        ListSnapshotCopyConfigurationsPaginator,
        ListSnapshotsPaginator,
        ListTableRestoreStatusPaginator,
        ListTracksPaginator,
        ListUsageLimitsPaginator,
        ListWorkgroupsPaginator,
    )

    session = Session()
    client: RedshiftServerlessClient = session.client("redshift-serverless")

    list_custom_domain_associations_paginator: ListCustomDomainAssociationsPaginator = client.get_paginator("list_custom_domain_associations")
    list_endpoint_access_paginator: ListEndpointAccessPaginator = client.get_paginator("list_endpoint_access")
    list_managed_workgroups_paginator: ListManagedWorkgroupsPaginator = client.get_paginator("list_managed_workgroups")
    list_namespaces_paginator: ListNamespacesPaginator = client.get_paginator("list_namespaces")
    list_recovery_points_paginator: ListRecoveryPointsPaginator = client.get_paginator("list_recovery_points")
    list_reservation_offerings_paginator: ListReservationOfferingsPaginator = client.get_paginator("list_reservation_offerings")
    list_reservations_paginator: ListReservationsPaginator = client.get_paginator("list_reservations")
    list_scheduled_actions_paginator: ListScheduledActionsPaginator = client.get_paginator("list_scheduled_actions")
    list_snapshot_copy_configurations_paginator: ListSnapshotCopyConfigurationsPaginator = client.get_paginator("list_snapshot_copy_configurations")
    list_snapshots_paginator: ListSnapshotsPaginator = client.get_paginator("list_snapshots")
    list_table_restore_status_paginator: ListTableRestoreStatusPaginator = client.get_paginator("list_table_restore_status")
    list_tracks_paginator: ListTracksPaginator = client.get_paginator("list_tracks")
    list_usage_limits_paginator: ListUsageLimitsPaginator = client.get_paginator("list_usage_limits")
    list_workgroups_paginator: ListWorkgroupsPaginator = client.get_paginator("list_workgroups")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListCustomDomainAssociationsRequestPaginateTypeDef,
    ListCustomDomainAssociationsResponseTypeDef,
    ListEndpointAccessRequestPaginateTypeDef,
    ListEndpointAccessResponseTypeDef,
    ListManagedWorkgroupsRequestPaginateTypeDef,
    ListManagedWorkgroupsResponseTypeDef,
    ListNamespacesRequestPaginateTypeDef,
    ListNamespacesResponseTypeDef,
    ListRecoveryPointsRequestPaginateTypeDef,
    ListRecoveryPointsResponseTypeDef,
    ListReservationOfferingsRequestPaginateTypeDef,
    ListReservationOfferingsResponseTypeDef,
    ListReservationsRequestPaginateTypeDef,
    ListReservationsResponseTypeDef,
    ListScheduledActionsRequestPaginateTypeDef,
    ListScheduledActionsResponseTypeDef,
    ListSnapshotCopyConfigurationsRequestPaginateTypeDef,
    ListSnapshotCopyConfigurationsResponseTypeDef,
    ListSnapshotsRequestPaginateTypeDef,
    ListSnapshotsResponseTypeDef,
    ListTableRestoreStatusRequestPaginateTypeDef,
    ListTableRestoreStatusResponseTypeDef,
    ListTracksRequestPaginateTypeDef,
    ListTracksResponseTypeDef,
    ListUsageLimitsRequestPaginateTypeDef,
    ListUsageLimitsResponseTypeDef,
    ListWorkgroupsRequestPaginateTypeDef,
    ListWorkgroupsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListCustomDomainAssociationsPaginator",
    "ListEndpointAccessPaginator",
    "ListManagedWorkgroupsPaginator",
    "ListNamespacesPaginator",
    "ListRecoveryPointsPaginator",
    "ListReservationOfferingsPaginator",
    "ListReservationsPaginator",
    "ListScheduledActionsPaginator",
    "ListSnapshotCopyConfigurationsPaginator",
    "ListSnapshotsPaginator",
    "ListTableRestoreStatusPaginator",
    "ListTracksPaginator",
    "ListUsageLimitsPaginator",
    "ListWorkgroupsPaginator",
)

if TYPE_CHECKING:
    _ListCustomDomainAssociationsPaginatorBase = Paginator[
        ListCustomDomainAssociationsResponseTypeDef
    ]
else:
    _ListCustomDomainAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCustomDomainAssociationsPaginator(_ListCustomDomainAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListCustomDomainAssociations.html#RedshiftServerless.Paginator.ListCustomDomainAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listcustomdomainassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCustomDomainAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListCustomDomainAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListCustomDomainAssociations.html#RedshiftServerless.Paginator.ListCustomDomainAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listcustomdomainassociationspaginator)
        """

if TYPE_CHECKING:
    _ListEndpointAccessPaginatorBase = Paginator[ListEndpointAccessResponseTypeDef]
else:
    _ListEndpointAccessPaginatorBase = Paginator  # type: ignore[assignment]

class ListEndpointAccessPaginator(_ListEndpointAccessPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListEndpointAccess.html#RedshiftServerless.Paginator.ListEndpointAccess)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listendpointaccesspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEndpointAccessRequestPaginateTypeDef]
    ) -> PageIterator[ListEndpointAccessResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListEndpointAccess.html#RedshiftServerless.Paginator.ListEndpointAccess.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listendpointaccesspaginator)
        """

if TYPE_CHECKING:
    _ListManagedWorkgroupsPaginatorBase = Paginator[ListManagedWorkgroupsResponseTypeDef]
else:
    _ListManagedWorkgroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListManagedWorkgroupsPaginator(_ListManagedWorkgroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListManagedWorkgroups.html#RedshiftServerless.Paginator.ListManagedWorkgroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listmanagedworkgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListManagedWorkgroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListManagedWorkgroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListManagedWorkgroups.html#RedshiftServerless.Paginator.ListManagedWorkgroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listmanagedworkgroupspaginator)
        """

if TYPE_CHECKING:
    _ListNamespacesPaginatorBase = Paginator[ListNamespacesResponseTypeDef]
else:
    _ListNamespacesPaginatorBase = Paginator  # type: ignore[assignment]

class ListNamespacesPaginator(_ListNamespacesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListNamespaces.html#RedshiftServerless.Paginator.ListNamespaces)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listnamespacespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListNamespacesRequestPaginateTypeDef]
    ) -> PageIterator[ListNamespacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListNamespaces.html#RedshiftServerless.Paginator.ListNamespaces.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listnamespacespaginator)
        """

if TYPE_CHECKING:
    _ListRecoveryPointsPaginatorBase = Paginator[ListRecoveryPointsResponseTypeDef]
else:
    _ListRecoveryPointsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRecoveryPointsPaginator(_ListRecoveryPointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListRecoveryPoints.html#RedshiftServerless.Paginator.ListRecoveryPoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listrecoverypointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRecoveryPointsRequestPaginateTypeDef]
    ) -> PageIterator[ListRecoveryPointsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListRecoveryPoints.html#RedshiftServerless.Paginator.ListRecoveryPoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listrecoverypointspaginator)
        """

if TYPE_CHECKING:
    _ListReservationOfferingsPaginatorBase = Paginator[ListReservationOfferingsResponseTypeDef]
else:
    _ListReservationOfferingsPaginatorBase = Paginator  # type: ignore[assignment]

class ListReservationOfferingsPaginator(_ListReservationOfferingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListReservationOfferings.html#RedshiftServerless.Paginator.ListReservationOfferings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listreservationofferingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListReservationOfferingsRequestPaginateTypeDef]
    ) -> PageIterator[ListReservationOfferingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListReservationOfferings.html#RedshiftServerless.Paginator.ListReservationOfferings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listreservationofferingspaginator)
        """

if TYPE_CHECKING:
    _ListReservationsPaginatorBase = Paginator[ListReservationsResponseTypeDef]
else:
    _ListReservationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListReservationsPaginator(_ListReservationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListReservations.html#RedshiftServerless.Paginator.ListReservations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listreservationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListReservationsRequestPaginateTypeDef]
    ) -> PageIterator[ListReservationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListReservations.html#RedshiftServerless.Paginator.ListReservations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listreservationspaginator)
        """

if TYPE_CHECKING:
    _ListScheduledActionsPaginatorBase = Paginator[ListScheduledActionsResponseTypeDef]
else:
    _ListScheduledActionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListScheduledActionsPaginator(_ListScheduledActionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListScheduledActions.html#RedshiftServerless.Paginator.ListScheduledActions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listscheduledactionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListScheduledActionsRequestPaginateTypeDef]
    ) -> PageIterator[ListScheduledActionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListScheduledActions.html#RedshiftServerless.Paginator.ListScheduledActions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listscheduledactionspaginator)
        """

if TYPE_CHECKING:
    _ListSnapshotCopyConfigurationsPaginatorBase = Paginator[
        ListSnapshotCopyConfigurationsResponseTypeDef
    ]
else:
    _ListSnapshotCopyConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSnapshotCopyConfigurationsPaginator(_ListSnapshotCopyConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListSnapshotCopyConfigurations.html#RedshiftServerless.Paginator.ListSnapshotCopyConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listsnapshotcopyconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSnapshotCopyConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[ListSnapshotCopyConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListSnapshotCopyConfigurations.html#RedshiftServerless.Paginator.ListSnapshotCopyConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listsnapshotcopyconfigurationspaginator)
        """

if TYPE_CHECKING:
    _ListSnapshotsPaginatorBase = Paginator[ListSnapshotsResponseTypeDef]
else:
    _ListSnapshotsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSnapshotsPaginator(_ListSnapshotsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListSnapshots.html#RedshiftServerless.Paginator.ListSnapshots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listsnapshotspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSnapshotsRequestPaginateTypeDef]
    ) -> PageIterator[ListSnapshotsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListSnapshots.html#RedshiftServerless.Paginator.ListSnapshots.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listsnapshotspaginator)
        """

if TYPE_CHECKING:
    _ListTableRestoreStatusPaginatorBase = Paginator[ListTableRestoreStatusResponseTypeDef]
else:
    _ListTableRestoreStatusPaginatorBase = Paginator  # type: ignore[assignment]

class ListTableRestoreStatusPaginator(_ListTableRestoreStatusPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListTableRestoreStatus.html#RedshiftServerless.Paginator.ListTableRestoreStatus)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listtablerestorestatuspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTableRestoreStatusRequestPaginateTypeDef]
    ) -> PageIterator[ListTableRestoreStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListTableRestoreStatus.html#RedshiftServerless.Paginator.ListTableRestoreStatus.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listtablerestorestatuspaginator)
        """

if TYPE_CHECKING:
    _ListTracksPaginatorBase = Paginator[ListTracksResponseTypeDef]
else:
    _ListTracksPaginatorBase = Paginator  # type: ignore[assignment]

class ListTracksPaginator(_ListTracksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListTracks.html#RedshiftServerless.Paginator.ListTracks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listtrackspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTracksRequestPaginateTypeDef]
    ) -> PageIterator[ListTracksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListTracks.html#RedshiftServerless.Paginator.ListTracks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listtrackspaginator)
        """

if TYPE_CHECKING:
    _ListUsageLimitsPaginatorBase = Paginator[ListUsageLimitsResponseTypeDef]
else:
    _ListUsageLimitsPaginatorBase = Paginator  # type: ignore[assignment]

class ListUsageLimitsPaginator(_ListUsageLimitsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListUsageLimits.html#RedshiftServerless.Paginator.ListUsageLimits)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listusagelimitspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUsageLimitsRequestPaginateTypeDef]
    ) -> PageIterator[ListUsageLimitsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListUsageLimits.html#RedshiftServerless.Paginator.ListUsageLimits.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listusagelimitspaginator)
        """

if TYPE_CHECKING:
    _ListWorkgroupsPaginatorBase = Paginator[ListWorkgroupsResponseTypeDef]
else:
    _ListWorkgroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkgroupsPaginator(_ListWorkgroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListWorkgroups.html#RedshiftServerless.Paginator.ListWorkgroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listworkgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkgroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkgroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless/paginator/ListWorkgroups.html#RedshiftServerless.Paginator.ListWorkgroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators/#listworkgroupspaginator)
        """
