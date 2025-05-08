"""
Type annotations for application-signals service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_application_signals.client import CloudWatchApplicationSignalsClient

    session = Session()
    client: CloudWatchApplicationSignalsClient = session.client("application-signals")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListServiceDependenciesPaginator,
    ListServiceDependentsPaginator,
    ListServiceLevelObjectiveExclusionWindowsPaginator,
    ListServiceLevelObjectivesPaginator,
    ListServiceOperationsPaginator,
    ListServicesPaginator,
)
from .type_defs import (
    BatchGetServiceLevelObjectiveBudgetReportInputTypeDef,
    BatchGetServiceLevelObjectiveBudgetReportOutputTypeDef,
    BatchUpdateExclusionWindowsInputTypeDef,
    BatchUpdateExclusionWindowsOutputTypeDef,
    CreateServiceLevelObjectiveInputTypeDef,
    CreateServiceLevelObjectiveOutputTypeDef,
    DeleteServiceLevelObjectiveInputTypeDef,
    GetServiceInputTypeDef,
    GetServiceLevelObjectiveInputTypeDef,
    GetServiceLevelObjectiveOutputTypeDef,
    GetServiceOutputTypeDef,
    ListServiceDependenciesInputTypeDef,
    ListServiceDependenciesOutputTypeDef,
    ListServiceDependentsInputTypeDef,
    ListServiceDependentsOutputTypeDef,
    ListServiceLevelObjectiveExclusionWindowsInputTypeDef,
    ListServiceLevelObjectiveExclusionWindowsOutputTypeDef,
    ListServiceLevelObjectivesInputTypeDef,
    ListServiceLevelObjectivesOutputTypeDef,
    ListServiceOperationsInputTypeDef,
    ListServiceOperationsOutputTypeDef,
    ListServicesInputTypeDef,
    ListServicesOutputTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateServiceLevelObjectiveInputTypeDef,
    UpdateServiceLevelObjectiveOutputTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("CloudWatchApplicationSignalsClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class CloudWatchApplicationSignalsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals.html#CloudWatchApplicationSignals.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudWatchApplicationSignalsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals.html#CloudWatchApplicationSignals.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#generate_presigned_url)
        """

    def batch_get_service_level_objective_budget_report(
        self, **kwargs: Unpack[BatchGetServiceLevelObjectiveBudgetReportInputTypeDef]
    ) -> BatchGetServiceLevelObjectiveBudgetReportOutputTypeDef:
        """
        Use this operation to retrieve one or more <i>service level objective (SLO)
        budget reports</i>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/batch_get_service_level_objective_budget_report.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#batch_get_service_level_objective_budget_report)
        """

    def batch_update_exclusion_windows(
        self, **kwargs: Unpack[BatchUpdateExclusionWindowsInputTypeDef]
    ) -> BatchUpdateExclusionWindowsOutputTypeDef:
        """
        Add or remove time window exclusions for one or more Service Level Objectives
        (SLOs).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/batch_update_exclusion_windows.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#batch_update_exclusion_windows)
        """

    def create_service_level_objective(
        self, **kwargs: Unpack[CreateServiceLevelObjectiveInputTypeDef]
    ) -> CreateServiceLevelObjectiveOutputTypeDef:
        """
        Creates a service level objective (SLO), which can help you ensure that your
        critical business operations are meeting customer expectations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/create_service_level_objective.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#create_service_level_objective)
        """

    def delete_service_level_objective(
        self, **kwargs: Unpack[DeleteServiceLevelObjectiveInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified service level objective.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/delete_service_level_objective.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#delete_service_level_objective)
        """

    def get_service(self, **kwargs: Unpack[GetServiceInputTypeDef]) -> GetServiceOutputTypeDef:
        """
        Returns information about a service discovered by Application Signals.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/get_service.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#get_service)
        """

    def get_service_level_objective(
        self, **kwargs: Unpack[GetServiceLevelObjectiveInputTypeDef]
    ) -> GetServiceLevelObjectiveOutputTypeDef:
        """
        Returns information about one SLO created in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/get_service_level_objective.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#get_service_level_objective)
        """

    def list_service_dependencies(
        self, **kwargs: Unpack[ListServiceDependenciesInputTypeDef]
    ) -> ListServiceDependenciesOutputTypeDef:
        """
        Returns a list of service dependencies of the service that you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/list_service_dependencies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#list_service_dependencies)
        """

    def list_service_dependents(
        self, **kwargs: Unpack[ListServiceDependentsInputTypeDef]
    ) -> ListServiceDependentsOutputTypeDef:
        """
        Returns the list of dependents that invoked the specified service during the
        provided time range.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/list_service_dependents.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#list_service_dependents)
        """

    def list_service_level_objective_exclusion_windows(
        self, **kwargs: Unpack[ListServiceLevelObjectiveExclusionWindowsInputTypeDef]
    ) -> ListServiceLevelObjectiveExclusionWindowsOutputTypeDef:
        """
        Retrieves all exclusion windows configured for a specific SLO.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/list_service_level_objective_exclusion_windows.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#list_service_level_objective_exclusion_windows)
        """

    def list_service_level_objectives(
        self, **kwargs: Unpack[ListServiceLevelObjectivesInputTypeDef]
    ) -> ListServiceLevelObjectivesOutputTypeDef:
        """
        Returns a list of SLOs created in this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/list_service_level_objectives.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#list_service_level_objectives)
        """

    def list_service_operations(
        self, **kwargs: Unpack[ListServiceOperationsInputTypeDef]
    ) -> ListServiceOperationsOutputTypeDef:
        """
        Returns a list of the <i>operations</i> of this service that have been
        discovered by Application Signals.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/list_service_operations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#list_service_operations)
        """

    def list_services(
        self, **kwargs: Unpack[ListServicesInputTypeDef]
    ) -> ListServicesOutputTypeDef:
        """
        Returns a list of services that have been discovered by Application Signals.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/list_services.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#list_services)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Displays the tags associated with a CloudWatch resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#list_tags_for_resource)
        """

    def start_discovery(self) -> Dict[str, Any]:
        """
        Enables this Amazon Web Services account to be able to use CloudWatch
        Application Signals by creating the
        <i>AWSServiceRoleForCloudWatchApplicationSignals</i> service-linked role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/start_discovery.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#start_discovery)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified CloudWatch
        resource, such as a service level objective.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#untag_resource)
        """

    def update_service_level_objective(
        self, **kwargs: Unpack[UpdateServiceLevelObjectiveInputTypeDef]
    ) -> UpdateServiceLevelObjectiveOutputTypeDef:
        """
        Updates an existing service level objective (SLO).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/update_service_level_objective.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#update_service_level_objective)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_service_dependencies"]
    ) -> ListServiceDependenciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_service_dependents"]
    ) -> ListServiceDependentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_service_level_objective_exclusion_windows"]
    ) -> ListServiceLevelObjectiveExclusionWindowsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_service_level_objectives"]
    ) -> ListServiceLevelObjectivesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_service_operations"]
    ) -> ListServiceOperationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_services"]
    ) -> ListServicesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-signals/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/client/#get_paginator)
        """
