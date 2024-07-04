"""
Type annotations for launch-wizard service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_launch_wizard import LaunchWizardClient
    from mypy_boto3_launch_wizard.paginator import (
        ListDeploymentEventsPaginator,
        ListDeploymentsPaginator,
        ListWorkloadDeploymentPatternsPaginator,
        ListWorkloadsPaginator,
    )

    client: LaunchWizardClient = boto3.client("launch-wizard")

    list_deployment_events_paginator: ListDeploymentEventsPaginator = client.get_paginator("list_deployment_events")
    list_deployments_paginator: ListDeploymentsPaginator = client.get_paginator("list_deployments")
    list_workload_deployment_patterns_paginator: ListWorkloadDeploymentPatternsPaginator = client.get_paginator("list_workload_deployment_patterns")
    list_workloads_paginator: ListWorkloadsPaginator = client.get_paginator("list_workloads")
    ```
"""

from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    DeploymentFilterTypeDef,
    ListDeploymentEventsOutputTypeDef,
    ListDeploymentsOutputTypeDef,
    ListWorkloadDeploymentPatternsOutputTypeDef,
    ListWorkloadsOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListDeploymentEventsPaginator",
    "ListDeploymentsPaginator",
    "ListWorkloadDeploymentPatternsPaginator",
    "ListWorkloadsPaginator",
)

class ListDeploymentEventsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/launch-wizard.html#LaunchWizard.Paginator.ListDeploymentEvents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/paginators.html#listdeploymenteventspaginator)
    """

    def paginate(
        self, *, deploymentId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeploymentEventsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/launch-wizard.html#LaunchWizard.Paginator.ListDeploymentEvents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/paginators.html#listdeploymenteventspaginator)
        """

class ListDeploymentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/launch-wizard.html#LaunchWizard.Paginator.ListDeployments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/paginators.html#listdeploymentspaginator)
    """

    def paginate(
        self,
        *,
        filters: List["DeploymentFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeploymentsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/launch-wizard.html#LaunchWizard.Paginator.ListDeployments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/paginators.html#listdeploymentspaginator)
        """

class ListWorkloadDeploymentPatternsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/launch-wizard.html#LaunchWizard.Paginator.ListWorkloadDeploymentPatterns)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/paginators.html#listworkloaddeploymentpatternspaginator)
    """

    def paginate(
        self, *, workloadName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorkloadDeploymentPatternsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/launch-wizard.html#LaunchWizard.Paginator.ListWorkloadDeploymentPatterns.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/paginators.html#listworkloaddeploymentpatternspaginator)
        """

class ListWorkloadsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/launch-wizard.html#LaunchWizard.Paginator.ListWorkloads)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/paginators.html#listworkloadspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorkloadsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/launch-wizard.html#LaunchWizard.Paginator.ListWorkloads.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/paginators.html#listworkloadspaginator)
        """
