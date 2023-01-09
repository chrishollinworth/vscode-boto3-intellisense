"""
Type annotations for emr service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_emr import EMRClient
    from mypy_boto3_emr.paginator import (
        ListBootstrapActionsPaginator,
        ListClustersPaginator,
        ListInstanceFleetsPaginator,
        ListInstanceGroupsPaginator,
        ListInstancesPaginator,
        ListNotebookExecutionsPaginator,
        ListSecurityConfigurationsPaginator,
        ListStepsPaginator,
        ListStudioSessionMappingsPaginator,
        ListStudiosPaginator,
    )

    client: EMRClient = boto3.client("emr")

    list_bootstrap_actions_paginator: ListBootstrapActionsPaginator = client.get_paginator("list_bootstrap_actions")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_instance_fleets_paginator: ListInstanceFleetsPaginator = client.get_paginator("list_instance_fleets")
    list_instance_groups_paginator: ListInstanceGroupsPaginator = client.get_paginator("list_instance_groups")
    list_instances_paginator: ListInstancesPaginator = client.get_paginator("list_instances")
    list_notebook_executions_paginator: ListNotebookExecutionsPaginator = client.get_paginator("list_notebook_executions")
    list_security_configurations_paginator: ListSecurityConfigurationsPaginator = client.get_paginator("list_security_configurations")
    list_steps_paginator: ListStepsPaginator = client.get_paginator("list_steps")
    list_studio_session_mappings_paginator: ListStudioSessionMappingsPaginator = client.get_paginator("list_studio_session_mappings")
    list_studios_paginator: ListStudiosPaginator = client.get_paginator("list_studios")
    ```
"""
from datetime import datetime
from typing import Iterator, List, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    ClusterStateType,
    IdentityTypeType,
    InstanceFleetTypeType,
    InstanceGroupTypeType,
    InstanceStateType,
    NotebookExecutionStatusType,
    StepStateType,
)
from .type_defs import (
    ListBootstrapActionsOutputTypeDef,
    ListClustersOutputTypeDef,
    ListInstanceFleetsOutputTypeDef,
    ListInstanceGroupsOutputTypeDef,
    ListInstancesOutputTypeDef,
    ListNotebookExecutionsOutputTypeDef,
    ListSecurityConfigurationsOutputTypeDef,
    ListStepsOutputTypeDef,
    ListStudioSessionMappingsOutputTypeDef,
    ListStudiosOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListBootstrapActionsPaginator",
    "ListClustersPaginator",
    "ListInstanceFleetsPaginator",
    "ListInstanceGroupsPaginator",
    "ListInstancesPaginator",
    "ListNotebookExecutionsPaginator",
    "ListSecurityConfigurationsPaginator",
    "ListStepsPaginator",
    "ListStudioSessionMappingsPaginator",
    "ListStudiosPaginator",
)

class ListBootstrapActionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/emr.html#EMR.Paginator.ListBootstrapActions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listbootstrapactionspaginator)
    """

    def paginate(
        self, *, ClusterId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBootstrapActionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/emr.html#EMR.Paginator.ListBootstrapActions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listbootstrapactionspaginator)
        """

class ListClustersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/emr.html#EMR.Paginator.ListClusters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listclusterspaginator)
    """

    def paginate(
        self,
        *,
        CreatedAfter: Union[datetime, str] = None,
        CreatedBefore: Union[datetime, str] = None,
        ClusterStates: List[ClusterStateType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListClustersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/emr.html#EMR.Paginator.ListClusters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listclusterspaginator)
        """

class ListInstanceFleetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/emr.html#EMR.Paginator.ListInstanceFleets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listinstancefleetspaginator)
    """

    def paginate(
        self, *, ClusterId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstanceFleetsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/emr.html#EMR.Paginator.ListInstanceFleets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listinstancefleetspaginator)
        """

class ListInstanceGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/emr.html#EMR.Paginator.ListInstanceGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listinstancegroupspaginator)
    """

    def paginate(
        self, *, ClusterId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstanceGroupsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/emr.html#EMR.Paginator.ListInstanceGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listinstancegroupspaginator)
        """

class ListInstancesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/emr.html#EMR.Paginator.ListInstances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listinstancespaginator)
    """

    def paginate(
        self,
        *,
        ClusterId: str,
        InstanceGroupId: str = None,
        InstanceGroupTypes: List[InstanceGroupTypeType] = None,
        InstanceFleetId: str = None,
        InstanceFleetType: InstanceFleetTypeType = None,
        InstanceStates: List[InstanceStateType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstancesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/emr.html#EMR.Paginator.ListInstances.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listinstancespaginator)
        """

class ListNotebookExecutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/emr.html#EMR.Paginator.ListNotebookExecutions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listnotebookexecutionspaginator)
    """

    def paginate(
        self,
        *,
        EditorId: str = None,
        Status: NotebookExecutionStatusType = None,
        From: Union[datetime, str] = None,
        To: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNotebookExecutionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/emr.html#EMR.Paginator.ListNotebookExecutions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listnotebookexecutionspaginator)
        """

class ListSecurityConfigurationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/emr.html#EMR.Paginator.ListSecurityConfigurations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listsecurityconfigurationspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSecurityConfigurationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/emr.html#EMR.Paginator.ListSecurityConfigurations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listsecurityconfigurationspaginator)
        """

class ListStepsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/emr.html#EMR.Paginator.ListSteps)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#liststepspaginator)
    """

    def paginate(
        self,
        *,
        ClusterId: str,
        StepStates: List[StepStateType] = None,
        StepIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStepsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/emr.html#EMR.Paginator.ListSteps.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#liststepspaginator)
        """

class ListStudioSessionMappingsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/emr.html#EMR.Paginator.ListStudioSessionMappings)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#liststudiosessionmappingspaginator)
    """

    def paginate(
        self,
        *,
        StudioId: str = None,
        IdentityType: IdentityTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStudioSessionMappingsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/emr.html#EMR.Paginator.ListStudioSessionMappings.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#liststudiosessionmappingspaginator)
        """

class ListStudiosPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/emr.html#EMR.Paginator.ListStudios)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#liststudiospaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStudiosOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/emr.html#EMR.Paginator.ListStudios.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#liststudiospaginator)
        """
