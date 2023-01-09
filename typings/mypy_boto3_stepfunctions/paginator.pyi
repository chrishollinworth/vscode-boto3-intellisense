"""
Type annotations for stepfunctions service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_stepfunctions import SFNClient
    from mypy_boto3_stepfunctions.paginator import (
        GetExecutionHistoryPaginator,
        ListActivitiesPaginator,
        ListExecutionsPaginator,
        ListMapRunsPaginator,
        ListStateMachinesPaginator,
    )

    client: SFNClient = boto3.client("stepfunctions")

    get_execution_history_paginator: GetExecutionHistoryPaginator = client.get_paginator("get_execution_history")
    list_activities_paginator: ListActivitiesPaginator = client.get_paginator("list_activities")
    list_executions_paginator: ListExecutionsPaginator = client.get_paginator("list_executions")
    list_map_runs_paginator: ListMapRunsPaginator = client.get_paginator("list_map_runs")
    list_state_machines_paginator: ListStateMachinesPaginator = client.get_paginator("list_state_machines")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import ExecutionStatusType
from .type_defs import (
    GetExecutionHistoryOutputTypeDef,
    ListActivitiesOutputTypeDef,
    ListExecutionsOutputTypeDef,
    ListMapRunsOutputTypeDef,
    ListStateMachinesOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "GetExecutionHistoryPaginator",
    "ListActivitiesPaginator",
    "ListExecutionsPaginator",
    "ListMapRunsPaginator",
    "ListStateMachinesPaginator",
)

class GetExecutionHistoryPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/stepfunctions.html#SFN.Paginator.GetExecutionHistory)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators.html#getexecutionhistorypaginator)
    """

    def paginate(
        self,
        *,
        executionArn: str,
        reverseOrder: bool = None,
        includeExecutionData: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetExecutionHistoryOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/stepfunctions.html#SFN.Paginator.GetExecutionHistory.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators.html#getexecutionhistorypaginator)
        """

class ListActivitiesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/stepfunctions.html#SFN.Paginator.ListActivities)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators.html#listactivitiespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListActivitiesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/stepfunctions.html#SFN.Paginator.ListActivities.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators.html#listactivitiespaginator)
        """

class ListExecutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/stepfunctions.html#SFN.Paginator.ListExecutions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators.html#listexecutionspaginator)
    """

    def paginate(
        self,
        *,
        stateMachineArn: str = None,
        statusFilter: ExecutionStatusType = None,
        mapRunArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListExecutionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/stepfunctions.html#SFN.Paginator.ListExecutions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators.html#listexecutionspaginator)
        """

class ListMapRunsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/stepfunctions.html#SFN.Paginator.ListMapRuns)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators.html#listmaprunspaginator)
    """

    def paginate(
        self, *, executionArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMapRunsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/stepfunctions.html#SFN.Paginator.ListMapRuns.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators.html#listmaprunspaginator)
        """

class ListStateMachinesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/stepfunctions.html#SFN.Paginator.ListStateMachines)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators.html#liststatemachinespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStateMachinesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/stepfunctions.html#SFN.Paginator.ListStateMachines.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators.html#liststatemachinespaginator)
        """
