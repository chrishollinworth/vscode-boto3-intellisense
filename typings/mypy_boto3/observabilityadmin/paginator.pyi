"""
Type annotations for observabilityadmin service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_observabilityadmin/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_observabilityadmin.client import CloudWatchObservabilityAdminServiceClient
    from mypy_boto3_observabilityadmin.paginator import (
        ListResourceTelemetryForOrganizationPaginator,
        ListResourceTelemetryPaginator,
    )

    session = Session()
    client: CloudWatchObservabilityAdminServiceClient = session.client("observabilityadmin")

    list_resource_telemetry_for_organization_paginator: ListResourceTelemetryForOrganizationPaginator = client.get_paginator("list_resource_telemetry_for_organization")
    list_resource_telemetry_paginator: ListResourceTelemetryPaginator = client.get_paginator("list_resource_telemetry")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListResourceTelemetryForOrganizationInputPaginateTypeDef,
    ListResourceTelemetryForOrganizationOutputTypeDef,
    ListResourceTelemetryInputPaginateTypeDef,
    ListResourceTelemetryOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListResourceTelemetryForOrganizationPaginator", "ListResourceTelemetryPaginator")

if TYPE_CHECKING:
    _ListResourceTelemetryForOrganizationPaginatorBase = Paginator[
        ListResourceTelemetryForOrganizationOutputTypeDef
    ]
else:
    _ListResourceTelemetryForOrganizationPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourceTelemetryForOrganizationPaginator(
    _ListResourceTelemetryForOrganizationPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/observabilityadmin/paginator/ListResourceTelemetryForOrganization.html#CloudWatchObservabilityAdminService.Paginator.ListResourceTelemetryForOrganization)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_observabilityadmin/paginators/#listresourcetelemetryfororganizationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourceTelemetryForOrganizationInputPaginateTypeDef]
    ) -> PageIterator[ListResourceTelemetryForOrganizationOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/observabilityadmin/paginator/ListResourceTelemetryForOrganization.html#CloudWatchObservabilityAdminService.Paginator.ListResourceTelemetryForOrganization.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_observabilityadmin/paginators/#listresourcetelemetryfororganizationpaginator)
        """

if TYPE_CHECKING:
    _ListResourceTelemetryPaginatorBase = Paginator[ListResourceTelemetryOutputTypeDef]
else:
    _ListResourceTelemetryPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourceTelemetryPaginator(_ListResourceTelemetryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/observabilityadmin/paginator/ListResourceTelemetry.html#CloudWatchObservabilityAdminService.Paginator.ListResourceTelemetry)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_observabilityadmin/paginators/#listresourcetelemetrypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourceTelemetryInputPaginateTypeDef]
    ) -> PageIterator[ListResourceTelemetryOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/observabilityadmin/paginator/ListResourceTelemetry.html#CloudWatchObservabilityAdminService.Paginator.ListResourceTelemetry.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_observabilityadmin/paginators/#listresourcetelemetrypaginator)
        """
