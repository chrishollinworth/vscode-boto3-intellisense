"""
Type annotations for codedeploy service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_codedeploy.client import CodeDeployClient
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

    session = Session()
    client: CodeDeployClient = session.client("codedeploy")

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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListApplicationRevisionsInputPaginateTypeDef,
    ListApplicationRevisionsOutputTypeDef,
    ListApplicationsInputPaginateTypeDef,
    ListApplicationsOutputTypeDef,
    ListDeploymentConfigsInputPaginateTypeDef,
    ListDeploymentConfigsOutputTypeDef,
    ListDeploymentGroupsInputPaginateTypeDef,
    ListDeploymentGroupsOutputTypeDef,
    ListDeploymentInstancesInputPaginateTypeDef,
    ListDeploymentInstancesOutputTypeDef,
    ListDeploymentsInputPaginateTypeDef,
    ListDeploymentsOutputTypeDef,
    ListDeploymentTargetsInputPaginateTypeDef,
    ListDeploymentTargetsOutputTypeDef,
    ListGitHubAccountTokenNamesInputPaginateTypeDef,
    ListGitHubAccountTokenNamesOutputTypeDef,
    ListOnPremisesInstancesInputPaginateTypeDef,
    ListOnPremisesInstancesOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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

if TYPE_CHECKING:
    _ListApplicationRevisionsPaginatorBase = Paginator[ListApplicationRevisionsOutputTypeDef]
else:
    _ListApplicationRevisionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListApplicationRevisionsPaginator(_ListApplicationRevisionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/paginator/ListApplicationRevisions.html#CodeDeploy.Paginator.ListApplicationRevisions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators/#listapplicationrevisionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApplicationRevisionsInputPaginateTypeDef]
    ) -> PageIterator[ListApplicationRevisionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/paginator/ListApplicationRevisions.html#CodeDeploy.Paginator.ListApplicationRevisions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators/#listapplicationrevisionspaginator)
        """

if TYPE_CHECKING:
    _ListApplicationsPaginatorBase = Paginator[ListApplicationsOutputTypeDef]
else:
    _ListApplicationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListApplicationsPaginator(_ListApplicationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/paginator/ListApplications.html#CodeDeploy.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators/#listapplicationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApplicationsInputPaginateTypeDef]
    ) -> PageIterator[ListApplicationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/paginator/ListApplications.html#CodeDeploy.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators/#listapplicationspaginator)
        """

if TYPE_CHECKING:
    _ListDeploymentConfigsPaginatorBase = Paginator[ListDeploymentConfigsOutputTypeDef]
else:
    _ListDeploymentConfigsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDeploymentConfigsPaginator(_ListDeploymentConfigsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/paginator/ListDeploymentConfigs.html#CodeDeploy.Paginator.ListDeploymentConfigs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators/#listdeploymentconfigspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDeploymentConfigsInputPaginateTypeDef]
    ) -> PageIterator[ListDeploymentConfigsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/paginator/ListDeploymentConfigs.html#CodeDeploy.Paginator.ListDeploymentConfigs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators/#listdeploymentconfigspaginator)
        """

if TYPE_CHECKING:
    _ListDeploymentGroupsPaginatorBase = Paginator[ListDeploymentGroupsOutputTypeDef]
else:
    _ListDeploymentGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDeploymentGroupsPaginator(_ListDeploymentGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/paginator/ListDeploymentGroups.html#CodeDeploy.Paginator.ListDeploymentGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators/#listdeploymentgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDeploymentGroupsInputPaginateTypeDef]
    ) -> PageIterator[ListDeploymentGroupsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/paginator/ListDeploymentGroups.html#CodeDeploy.Paginator.ListDeploymentGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators/#listdeploymentgroupspaginator)
        """

if TYPE_CHECKING:
    _ListDeploymentInstancesPaginatorBase = Paginator[ListDeploymentInstancesOutputTypeDef]
else:
    _ListDeploymentInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDeploymentInstancesPaginator(_ListDeploymentInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/paginator/ListDeploymentInstances.html#CodeDeploy.Paginator.ListDeploymentInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators/#listdeploymentinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDeploymentInstancesInputPaginateTypeDef]
    ) -> PageIterator[ListDeploymentInstancesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/paginator/ListDeploymentInstances.html#CodeDeploy.Paginator.ListDeploymentInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators/#listdeploymentinstancespaginator)
        """

if TYPE_CHECKING:
    _ListDeploymentTargetsPaginatorBase = Paginator[ListDeploymentTargetsOutputTypeDef]
else:
    _ListDeploymentTargetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDeploymentTargetsPaginator(_ListDeploymentTargetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/paginator/ListDeploymentTargets.html#CodeDeploy.Paginator.ListDeploymentTargets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators/#listdeploymenttargetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDeploymentTargetsInputPaginateTypeDef]
    ) -> PageIterator[ListDeploymentTargetsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/paginator/ListDeploymentTargets.html#CodeDeploy.Paginator.ListDeploymentTargets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators/#listdeploymenttargetspaginator)
        """

if TYPE_CHECKING:
    _ListDeploymentsPaginatorBase = Paginator[ListDeploymentsOutputTypeDef]
else:
    _ListDeploymentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDeploymentsPaginator(_ListDeploymentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/paginator/ListDeployments.html#CodeDeploy.Paginator.ListDeployments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators/#listdeploymentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDeploymentsInputPaginateTypeDef]
    ) -> PageIterator[ListDeploymentsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/paginator/ListDeployments.html#CodeDeploy.Paginator.ListDeployments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators/#listdeploymentspaginator)
        """

if TYPE_CHECKING:
    _ListGitHubAccountTokenNamesPaginatorBase = Paginator[ListGitHubAccountTokenNamesOutputTypeDef]
else:
    _ListGitHubAccountTokenNamesPaginatorBase = Paginator  # type: ignore[assignment]

class ListGitHubAccountTokenNamesPaginator(_ListGitHubAccountTokenNamesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/paginator/ListGitHubAccountTokenNames.html#CodeDeploy.Paginator.ListGitHubAccountTokenNames)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators/#listgithubaccounttokennamespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGitHubAccountTokenNamesInputPaginateTypeDef]
    ) -> PageIterator[ListGitHubAccountTokenNamesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/paginator/ListGitHubAccountTokenNames.html#CodeDeploy.Paginator.ListGitHubAccountTokenNames.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators/#listgithubaccounttokennamespaginator)
        """

if TYPE_CHECKING:
    _ListOnPremisesInstancesPaginatorBase = Paginator[ListOnPremisesInstancesOutputTypeDef]
else:
    _ListOnPremisesInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class ListOnPremisesInstancesPaginator(_ListOnPremisesInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/paginator/ListOnPremisesInstances.html#CodeDeploy.Paginator.ListOnPremisesInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators/#listonpremisesinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOnPremisesInstancesInputPaginateTypeDef]
    ) -> PageIterator[ListOnPremisesInstancesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/paginator/ListOnPremisesInstances.html#CodeDeploy.Paginator.ListOnPremisesInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/paginators/#listonpremisesinstancespaginator)
        """
