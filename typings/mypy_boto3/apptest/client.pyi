"""
Type annotations for apptest service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_apptest import MainframeModernizationApplicationTestingClient

    client: MainframeModernizationApplicationTestingClient = boto3.client("apptest")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListTestCasesPaginator,
    ListTestConfigurationsPaginator,
    ListTestRunsPaginator,
    ListTestRunStepsPaginator,
    ListTestRunTestCasesPaginator,
    ListTestSuitesPaginator,
)
from .type_defs import (
    CreateTestCaseResponseTypeDef,
    CreateTestConfigurationResponseTypeDef,
    CreateTestSuiteResponseTypeDef,
    GetTestCaseResponseTypeDef,
    GetTestConfigurationResponseTypeDef,
    GetTestRunStepResponseTypeDef,
    GetTestSuiteResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTestCasesResponseTypeDef,
    ListTestConfigurationsResponseTypeDef,
    ListTestRunsResponseTypeDef,
    ListTestRunStepsResponseTypeDef,
    ListTestRunTestCasesResponseTypeDef,
    ListTestSuitesResponseTypeDef,
    ResourceTypeDef,
    ServiceSettingsTypeDef,
    StartTestRunResponseTypeDef,
    StepTypeDef,
    TestCasesTypeDef,
    UpdateTestCaseResponseTypeDef,
    UpdateTestConfigurationResponseTypeDef,
    UpdateTestSuiteResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("MainframeModernizationApplicationTestingClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class MainframeModernizationApplicationTestingClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MainframeModernizationApplicationTestingClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#close)
        """

    def create_test_case(
        self,
        *,
        name: str,
        steps: List["StepTypeDef"],
        description: str = None,
        clientToken: str = None,
        tags: Dict[str, str] = None
    ) -> CreateTestCaseResponseTypeDef:
        """
        Creates a test case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.create_test_case)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#create_test_case)
        """

    def create_test_configuration(
        self,
        *,
        name: str,
        resources: List["ResourceTypeDef"],
        description: str = None,
        properties: Dict[str, str] = None,
        clientToken: str = None,
        tags: Dict[str, str] = None,
        serviceSettings: "ServiceSettingsTypeDef" = None
    ) -> CreateTestConfigurationResponseTypeDef:
        """
        Creates a test configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.create_test_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#create_test_configuration)
        """

    def create_test_suite(
        self,
        *,
        name: str,
        testCases: "TestCasesTypeDef",
        description: str = None,
        beforeSteps: List["StepTypeDef"] = None,
        afterSteps: List["StepTypeDef"] = None,
        clientToken: str = None,
        tags: Dict[str, str] = None
    ) -> CreateTestSuiteResponseTypeDef:
        """
        Creates a test suite.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.create_test_suite)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#create_test_suite)
        """

    def delete_test_case(self, *, testCaseId: str) -> Dict[str, Any]:
        """
        Deletes a test case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.delete_test_case)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#delete_test_case)
        """

    def delete_test_configuration(self, *, testConfigurationId: str) -> Dict[str, Any]:
        """
        Deletes a test configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.delete_test_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#delete_test_configuration)
        """

    def delete_test_run(self, *, testRunId: str) -> Dict[str, Any]:
        """
        Deletes a test run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.delete_test_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#delete_test_run)
        """

    def delete_test_suite(self, *, testSuiteId: str) -> Dict[str, Any]:
        """
        Deletes a test suite.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.delete_test_suite)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#delete_test_suite)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#generate_presigned_url)
        """

    def get_test_case(
        self, *, testCaseId: str, testCaseVersion: int = None
    ) -> GetTestCaseResponseTypeDef:
        """
        Gets a test case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.get_test_case)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#get_test_case)
        """

    def get_test_configuration(
        self, *, testConfigurationId: str, testConfigurationVersion: int = None
    ) -> GetTestConfigurationResponseTypeDef:
        """
        Gets a test configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.get_test_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#get_test_configuration)
        """

    def get_test_run_step(
        self, *, testRunId: str, stepName: str, testCaseId: str = None, testSuiteId: str = None
    ) -> GetTestRunStepResponseTypeDef:
        """
        Gets a test run step.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.get_test_run_step)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#get_test_run_step)
        """

    def get_test_suite(
        self, *, testSuiteId: str, testSuiteVersion: int = None
    ) -> GetTestSuiteResponseTypeDef:
        """
        Gets a test suite.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.get_test_suite)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#get_test_suite)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#list_tags_for_resource)
        """

    def list_test_cases(
        self, *, testCaseIds: List[str] = None, nextToken: str = None, maxResults: int = None
    ) -> ListTestCasesResponseTypeDef:
        """
        Lists test cases.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.list_test_cases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#list_test_cases)
        """

    def list_test_configurations(
        self,
        *,
        testConfigurationIds: List[str] = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListTestConfigurationsResponseTypeDef:
        """
        Lists test configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.list_test_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#list_test_configurations)
        """

    def list_test_run_steps(
        self,
        *,
        testRunId: str,
        testCaseId: str = None,
        testSuiteId: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListTestRunStepsResponseTypeDef:
        """
        Lists test run steps.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.list_test_run_steps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#list_test_run_steps)
        """

    def list_test_run_test_cases(
        self, *, testRunId: str, nextToken: str = None, maxResults: int = None
    ) -> ListTestRunTestCasesResponseTypeDef:
        """
        Lists test run test cases.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.list_test_run_test_cases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#list_test_run_test_cases)
        """

    def list_test_runs(
        self,
        *,
        testSuiteId: str = None,
        testRunIds: List[str] = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListTestRunsResponseTypeDef:
        """
        Lists test runs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.list_test_runs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#list_test_runs)
        """

    def list_test_suites(
        self, *, testSuiteIds: List[str] = None, nextToken: str = None, maxResults: int = None
    ) -> ListTestSuitesResponseTypeDef:
        """
        Lists test suites.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.list_test_suites)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#list_test_suites)
        """

    def start_test_run(
        self,
        *,
        testSuiteId: str,
        testConfigurationId: str = None,
        clientToken: str = None,
        tags: Dict[str, str] = None
    ) -> StartTestRunResponseTypeDef:
        """
        Starts a test run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.start_test_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#start_test_run)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Specifies tags of a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Untags a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#untag_resource)
        """

    def update_test_case(
        self, *, testCaseId: str, description: str = None, steps: List["StepTypeDef"] = None
    ) -> UpdateTestCaseResponseTypeDef:
        """
        Updates a test case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.update_test_case)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#update_test_case)
        """

    def update_test_configuration(
        self,
        *,
        testConfigurationId: str,
        description: str = None,
        resources: List["ResourceTypeDef"] = None,
        properties: Dict[str, str] = None,
        serviceSettings: "ServiceSettingsTypeDef" = None
    ) -> UpdateTestConfigurationResponseTypeDef:
        """
        Updates a test configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.update_test_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#update_test_configuration)
        """

    def update_test_suite(
        self,
        *,
        testSuiteId: str,
        description: str = None,
        beforeSteps: List["StepTypeDef"] = None,
        afterSteps: List["StepTypeDef"] = None,
        testCases: "TestCasesTypeDef" = None
    ) -> UpdateTestSuiteResponseTypeDef:
        """
        Updates a test suite.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client.update_test_suite)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/client.html#update_test_suite)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_test_cases"]) -> ListTestCasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Paginator.ListTestCases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators.html#listtestcasespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_test_configurations"]
    ) -> ListTestConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Paginator.ListTestConfigurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators.html#listtestconfigurationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_test_run_steps"]
    ) -> ListTestRunStepsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Paginator.ListTestRunSteps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators.html#listtestrunstepspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_test_run_test_cases"]
    ) -> ListTestRunTestCasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Paginator.ListTestRunTestCases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators.html#listtestruntestcasespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_test_runs"]) -> ListTestRunsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Paginator.ListTestRuns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators.html#listtestrunspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_test_suites"]) -> ListTestSuitesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/apptest.html#MainframeModernizationApplicationTesting.Paginator.ListTestSuites)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/paginators.html#listtestsuitespaginator)
        """
