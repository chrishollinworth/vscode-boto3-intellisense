"""
Type annotations for apptest service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_apptest import MainframeModernizationApplicationTestingClient
    from mypy_boto3_apptest.paginator import (
        ListTestCasesPaginator,
        ListTestConfigurationsPaginator,
        ListTestRunStepsPaginator,
        ListTestRunTestCasesPaginator,
        ListTestRunsPaginator,
        ListTestSuitesPaginator,
    )

    client: MainframeModernizationApplicationTestingClient = boto3.client("apptest")

    list_test_cases_paginator: ListTestCasesPaginator = client.get_paginator("list_test_cases")
    list_test_configurations_paginator: ListTestConfigurationsPaginator = client.get_paginator("list_test_configurations")
    list_test_run_steps_paginator: ListTestRunStepsPaginator = client.get_paginator("list_test_run_steps")
    list_test_run_test_cases_paginator: ListTestRunTestCasesPaginator = client.get_paginator("list_test_run_test_cases")
    list_test_runs_paginator: ListTestRunsPaginator = client.get_paginator("list_test_runs")
    list_test_suites_paginator: ListTestSuitesPaginator = client.get_paginator("list_test_suites")
    ```
"""

from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListTestCasesResponseTypeDef,
    ListTestConfigurationsResponseTypeDef,
    ListTestRunsResponseTypeDef,
    ListTestRunStepsResponseTypeDef,
    ListTestRunTestCasesResponseTypeDef,
    ListTestSuitesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListTestCasesPaginator",
    "ListTestConfigurationsPaginator",
    "ListTestRunStepsPaginator",
    "ListTestRunTestCasesPaginator",
    "ListTestRunsPaginator",
    "ListTestSuitesPaginator",
)

class ListTestCasesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Paginator.ListTestCases)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators.html#listtestcasespaginator)
    """

    def paginate(
        self, *, testCaseIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTestCasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Paginator.ListTestCases.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators.html#listtestcasespaginator)
        """

class ListTestConfigurationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Paginator.ListTestConfigurations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators.html#listtestconfigurationspaginator)
    """

    def paginate(
        self,
        *,
        testConfigurationIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTestConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Paginator.ListTestConfigurations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators.html#listtestconfigurationspaginator)
        """

class ListTestRunStepsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Paginator.ListTestRunSteps)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators.html#listtestrunstepspaginator)
    """

    def paginate(
        self,
        *,
        testRunId: str,
        testCaseId: str = None,
        testSuiteId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTestRunStepsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Paginator.ListTestRunSteps.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators.html#listtestrunstepspaginator)
        """

class ListTestRunTestCasesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Paginator.ListTestRunTestCases)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators.html#listtestruntestcasespaginator)
    """

    def paginate(
        self, *, testRunId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTestRunTestCasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Paginator.ListTestRunTestCases.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators.html#listtestruntestcasespaginator)
        """

class ListTestRunsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Paginator.ListTestRuns)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators.html#listtestrunspaginator)
    """

    def paginate(
        self,
        *,
        testSuiteId: str = None,
        testRunIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTestRunsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Paginator.ListTestRuns.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators.html#listtestrunspaginator)
        """

class ListTestSuitesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Paginator.ListTestSuites)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators.html#listtestsuitespaginator)
    """

    def paginate(
        self, *, testSuiteIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTestSuitesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Paginator.ListTestSuites.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators.html#listtestsuitespaginator)
        """
