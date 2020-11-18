# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for codedeploy service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_codedeploy import CodeDeployClient
    from mypy_boto3_codedeploy.paginator import (
        ListApplicationRevisionsPaginator,
        ListApplicationsPaginator,
        ListDeploymentConfigsPaginator,
        ListDeploymentGroupsPaginator,
        ListDeploymentInstancesPaginator,
        ListDeploymentTargetsPaginator,
        ListDeploymentsPaginator,
        ListGitHubAccountTokenNamesPaginator,
        ListOnPremisesInstancesPaginator,
    )

    client: CodeDeployClient = boto3.client("codedeploy")

    list_application_revisions_paginator: ListApplicationRevisionsPaginator = client.get_paginator("list_application_revisions")
    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_deployment_configs_paginator: ListDeploymentConfigsPaginator = client.get_paginator("list_deployment_configs")
    list_deployment_groups_paginator: ListDeploymentGroupsPaginator = client.get_paginator("list_deployment_groups")
    list_deployment_instances_paginator: ListDeploymentInstancesPaginator = client.get_paginator("list_deployment_instances")
    list_deployment_targets_paginator: ListDeploymentTargetsPaginator = client.get_paginator("list_deployment_targets")
    list_deployments_paginator: ListDeploymentsPaginator = client.get_paginator("list_deployments")
    list_git_hub_account_token_names_paginator: ListGitHubAccountTokenNamesPaginator = client.get_paginator("list_git_hub_account_token_names")
    list_on_premises_instances_paginator: ListOnPremisesInstancesPaginator = client.get_paginator("list_on_premises_instances")
    ```
"""
import sys
from typing import Dict, Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_codedeploy.type_defs import (
    ListApplicationRevisionsOutputTypeDef,
    ListApplicationsOutputTypeDef,
    ListDeploymentConfigsOutputTypeDef,
    ListDeploymentGroupsOutputTypeDef,
    ListDeploymentInstancesOutputTypeDef,
    ListDeploymentsOutputTypeDef,
    ListDeploymentTargetsOutputTypeDef,
    ListGitHubAccountTokenNamesOutputTypeDef,
    ListOnPremisesInstancesOutputTypeDef,
    PaginatorConfigTypeDef,
    TagFilterTypeDef,
    TimeRangeTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListApplicationRevisionsPaginator",
    "ListApplicationsPaginator",
    "ListDeploymentConfigsPaginator",
    "ListDeploymentGroupsPaginator",
    "ListDeploymentInstancesPaginator",
    "ListDeploymentTargetsPaginator",
    "ListDeploymentsPaginator",
    "ListGitHubAccountTokenNamesPaginator",
    "ListOnPremisesInstancesPaginator",
)


class ListApplicationRevisionsPaginator(Boto3Paginator):
    """
    [Paginator.ListApplicationRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListApplicationRevisions)
    """

    def paginate(
        self,
        applicationName: str,
        sortBy: Literal["registerTime", "firstUsedTime", "lastUsedTime"] = None,
        sortOrder: Literal["ascending", "descending"] = None,
        s3Bucket: str = None,
        s3KeyPrefix: str = None,
        deployed: Literal["include", "exclude", "ignore"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListApplicationRevisionsOutputTypeDef]:
        """
        [ListApplicationRevisions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListApplicationRevisions.paginate)
        """


class ListApplicationsPaginator(Boto3Paginator):
    """
    [Paginator.ListApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListApplications)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationsOutputTypeDef]:
        """
        [ListApplications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListApplications.paginate)
        """


class ListDeploymentConfigsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeploymentConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentConfigs)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeploymentConfigsOutputTypeDef]:
        """
        [ListDeploymentConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentConfigs.paginate)
        """


class ListDeploymentGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeploymentGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentGroups)
    """

    def paginate(
        self, applicationName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeploymentGroupsOutputTypeDef]:
        """
        [ListDeploymentGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentGroups.paginate)
        """


class ListDeploymentInstancesPaginator(Boto3Paginator):
    """
    [Paginator.ListDeploymentInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentInstances)
    """

    def paginate(
        self,
        deploymentId: str,
        instanceStatusFilter: List[
            Literal["Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"]
        ] = None,
        instanceTypeFilter: List[Literal["Blue", "Green"]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListDeploymentInstancesOutputTypeDef]:
        """
        [ListDeploymentInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentInstances.paginate)
        """


class ListDeploymentTargetsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeploymentTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentTargets)
    """

    def paginate(
        self,
        deploymentId: str = None,
        targetFilters: Dict[Literal["TargetStatus", "ServerInstanceLabel"], List[str]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListDeploymentTargetsOutputTypeDef]:
        """
        [ListDeploymentTargets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentTargets.paginate)
        """


class ListDeploymentsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeployments)
    """

    def paginate(
        self,
        applicationName: str = None,
        deploymentGroupName: str = None,
        externalId: str = None,
        includeOnlyStatuses: List[
            Literal[
                "Created",
                "Queued",
                "InProgress",
                "Baking",
                "Succeeded",
                "Failed",
                "Stopped",
                "Ready",
            ]
        ] = None,
        createTimeRange: TimeRangeTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListDeploymentsOutputTypeDef]:
        """
        [ListDeployments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeployments.paginate)
        """


class ListGitHubAccountTokenNamesPaginator(Boto3Paginator):
    """
    [Paginator.ListGitHubAccountTokenNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListGitHubAccountTokenNames)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGitHubAccountTokenNamesOutputTypeDef]:
        """
        [ListGitHubAccountTokenNames.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListGitHubAccountTokenNames.paginate)
        """


class ListOnPremisesInstancesPaginator(Boto3Paginator):
    """
    [Paginator.ListOnPremisesInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListOnPremisesInstances)
    """

    def paginate(
        self,
        registrationStatus: Literal["Registered", "Deregistered"] = None,
        tagFilters: List["TagFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListOnPremisesInstancesOutputTypeDef]:
        """
        [ListOnPremisesInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codedeploy.html#CodeDeploy.Paginator.ListOnPremisesInstances.paginate)
        """
