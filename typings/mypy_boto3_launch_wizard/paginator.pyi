"""
Type annotations for launch-wizard service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_launch_wizard.client import LaunchWizardClient
    from mypy_boto3_launch_wizard.paginator import (
        ListDeploymentEventsPaginator,
        ListDeploymentsPaginator,
        ListWorkloadDeploymentPatternsPaginator,
        ListWorkloadsPaginator,
    )

    session = Session()
    client: LaunchWizardClient = session.client("launch-wizard")

    list_deployment_events_paginator: ListDeploymentEventsPaginator = client.get_paginator("list_deployment_events")
    list_deployments_paginator: ListDeploymentsPaginator = client.get_paginator("list_deployments")
    list_workload_deployment_patterns_paginator: ListWorkloadDeploymentPatternsPaginator = client.get_paginator("list_workload_deployment_patterns")
    list_workloads_paginator: ListWorkloadsPaginator = client.get_paginator("list_workloads")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListDeploymentEventsInputPaginateTypeDef,
    ListDeploymentEventsOutputTypeDef,
    ListDeploymentsInputPaginateTypeDef,
    ListDeploymentsOutputTypeDef,
    ListWorkloadDeploymentPatternsInputPaginateTypeDef,
    ListWorkloadDeploymentPatternsOutputTypeDef,
    ListWorkloadsInputPaginateTypeDef,
    ListWorkloadsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListDeploymentEventsPaginator",
    "ListDeploymentsPaginator",
    "ListWorkloadDeploymentPatternsPaginator",
    "ListWorkloadsPaginator",
)

if TYPE_CHECKING:
    _ListDeploymentEventsPaginatorBase = Paginator[ListDeploymentEventsOutputTypeDef]
else:
    _ListDeploymentEventsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDeploymentEventsPaginator(_ListDeploymentEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/paginator/ListDeploymentEvents.html#LaunchWizard.Paginator.ListDeploymentEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/paginators/#listdeploymenteventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDeploymentEventsInputPaginateTypeDef]
    ) -> PageIterator[ListDeploymentEventsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/paginator/ListDeploymentEvents.html#LaunchWizard.Paginator.ListDeploymentEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/paginators/#listdeploymenteventspaginator)
        """

if TYPE_CHECKING:
    _ListDeploymentsPaginatorBase = Paginator[ListDeploymentsOutputTypeDef]
else:
    _ListDeploymentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDeploymentsPaginator(_ListDeploymentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/paginator/ListDeployments.html#LaunchWizard.Paginator.ListDeployments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/paginators/#listdeploymentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDeploymentsInputPaginateTypeDef]
    ) -> PageIterator[ListDeploymentsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/paginator/ListDeployments.html#LaunchWizard.Paginator.ListDeployments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/paginators/#listdeploymentspaginator)
        """

if TYPE_CHECKING:
    _ListWorkloadDeploymentPatternsPaginatorBase = Paginator[
        ListWorkloadDeploymentPatternsOutputTypeDef
    ]
else:
    _ListWorkloadDeploymentPatternsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkloadDeploymentPatternsPaginator(_ListWorkloadDeploymentPatternsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/paginator/ListWorkloadDeploymentPatterns.html#LaunchWizard.Paginator.ListWorkloadDeploymentPatterns)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/paginators/#listworkloaddeploymentpatternspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkloadDeploymentPatternsInputPaginateTypeDef]
    ) -> PageIterator[ListWorkloadDeploymentPatternsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/paginator/ListWorkloadDeploymentPatterns.html#LaunchWizard.Paginator.ListWorkloadDeploymentPatterns.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/paginators/#listworkloaddeploymentpatternspaginator)
        """

if TYPE_CHECKING:
    _ListWorkloadsPaginatorBase = Paginator[ListWorkloadsOutputTypeDef]
else:
    _ListWorkloadsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkloadsPaginator(_ListWorkloadsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/paginator/ListWorkloads.html#LaunchWizard.Paginator.ListWorkloads)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/paginators/#listworkloadspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkloadsInputPaginateTypeDef]
    ) -> PageIterator[ListWorkloadsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/paginator/ListWorkloads.html#LaunchWizard.Paginator.ListWorkloads.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/paginators/#listworkloadspaginator)
        """
