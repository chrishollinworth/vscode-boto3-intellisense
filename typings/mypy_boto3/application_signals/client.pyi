"""
Type annotations for application-signals service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_application_signals import CloudWatchApplicationSignalsClient

    client: CloudWatchApplicationSignalsClient = boto3.client("application-signals")
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListServiceDependenciesPaginator,
    ListServiceDependentsPaginator,
    ListServiceLevelObjectivesPaginator,
    ListServiceOperationsPaginator,
    ListServicesPaginator,
)
from .type_defs import (
    BatchGetServiceLevelObjectiveBudgetReportOutputTypeDef,
    CreateServiceLevelObjectiveOutputTypeDef,
    GetServiceLevelObjectiveOutputTypeDef,
    GetServiceOutputTypeDef,
    GoalTypeDef,
    ListServiceDependenciesOutputTypeDef,
    ListServiceDependentsOutputTypeDef,
    ListServiceLevelObjectivesOutputTypeDef,
    ListServiceOperationsOutputTypeDef,
    ListServicesOutputTypeDef,
    ListTagsForResourceResponseTypeDef,
    ServiceLevelIndicatorConfigTypeDef,
    TagTypeDef,
    UpdateServiceLevelObjectiveOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CloudWatchApplicationSignalsClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class CloudWatchApplicationSignalsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudWatchApplicationSignalsClient exceptions.
        """

    def batch_get_service_level_objective_budget_report(
        self, *, Timestamp: Union[datetime, str], SloIds: List[str]
    ) -> BatchGetServiceLevelObjectiveBudgetReportOutputTypeDef:
        """
        Use this operation to retrieve one or more *service level objective (SLO) budget
        reports*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Client.batch_get_service_level_objective_budget_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client.html#batch_get_service_level_objective_budget_report)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client.html#close)
        """

    def create_service_level_objective(
        self,
        *,
        Name: str,
        SliConfig: "ServiceLevelIndicatorConfigTypeDef",
        Description: str = None,
        Goal: "GoalTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateServiceLevelObjectiveOutputTypeDef:
        """
        Creates a service level objective (SLO), which can help you ensure that your
        critical business operations are meeting customer expectations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Client.create_service_level_objective)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client.html#create_service_level_objective)
        """

    def delete_service_level_objective(self, *, Id: str) -> Dict[str, Any]:
        """
        Deletes the specified service level objective.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Client.delete_service_level_objective)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client.html#delete_service_level_objective)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client.html#generate_presigned_url)
        """

    def get_service(
        self,
        *,
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        KeyAttributes: Dict[str, str]
    ) -> GetServiceOutputTypeDef:
        """
        Returns information about a service discovered by Application Signals.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Client.get_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client.html#get_service)
        """

    def get_service_level_objective(self, *, Id: str) -> GetServiceLevelObjectiveOutputTypeDef:
        """
        Returns information about one SLO created in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Client.get_service_level_objective)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client.html#get_service_level_objective)
        """

    def list_service_dependencies(
        self,
        *,
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        KeyAttributes: Dict[str, str],
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListServiceDependenciesOutputTypeDef:
        """
        Returns a list of service dependencies of the service that you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Client.list_service_dependencies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client.html#list_service_dependencies)
        """

    def list_service_dependents(
        self,
        *,
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        KeyAttributes: Dict[str, str],
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListServiceDependentsOutputTypeDef:
        """
        Returns the list of dependents that invoked the specified service during the
        provided time range.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Client.list_service_dependents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client.html#list_service_dependents)
        """

    def list_service_level_objectives(
        self,
        *,
        KeyAttributes: Dict[str, str] = None,
        OperationName: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListServiceLevelObjectivesOutputTypeDef:
        """
        Returns a list of SLOs created in this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Client.list_service_level_objectives)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client.html#list_service_level_objectives)
        """

    def list_service_operations(
        self,
        *,
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        KeyAttributes: Dict[str, str],
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListServiceOperationsOutputTypeDef:
        """
        Returns a list of the *operations* of this service that have been discovered by
        Application Signals.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Client.list_service_operations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client.html#list_service_operations)
        """

    def list_services(
        self,
        *,
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListServicesOutputTypeDef:
        """
        Returns a list of services that have been discovered by Application Signals.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Client.list_services)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client.html#list_services)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Displays the tags associated with a CloudWatch resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client.html#list_tags_for_resource)
        """

    def start_discovery(self) -> Dict[str, Any]:
        """
        Enables this Amazon Web Services account to be able to use CloudWatch
        Application Signals by creating the
        *AWSServiceRoleForCloudWatchApplicationSignals* service-linked role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Client.start_discovery)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client.html#start_discovery)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified CloudWatch resource,
        such as a service level objective.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client.html#untag_resource)
        """

    def update_service_level_objective(
        self,
        *,
        Id: str,
        Description: str = None,
        SliConfig: "ServiceLevelIndicatorConfigTypeDef" = None,
        Goal: "GoalTypeDef" = None
    ) -> UpdateServiceLevelObjectiveOutputTypeDef:
        """
        Updates an existing service level objective (SLO).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Client.update_service_level_objective)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client.html#update_service_level_objective)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_dependencies"]
    ) -> ListServiceDependenciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Paginator.ListServiceDependencies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/paginators.html#listservicedependenciespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_dependents"]
    ) -> ListServiceDependentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Paginator.ListServiceDependents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/paginators.html#listservicedependentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_level_objectives"]
    ) -> ListServiceLevelObjectivesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Paginator.ListServiceLevelObjectives)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/paginators.html#listservicelevelobjectivespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_operations"]
    ) -> ListServiceOperationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Paginator.ListServiceOperations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/paginators.html#listserviceoperationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_services"]) -> ListServicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Paginator.ListServices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/paginators.html#listservicespaginator)
        """
