"""
Type annotations for application-signals service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_application_signals import CloudWatchApplicationSignalsClient
    from mypy_boto3_application_signals.paginator import (
        ListServiceDependenciesPaginator,
        ListServiceDependentsPaginator,
        ListServiceLevelObjectivesPaginator,
        ListServiceOperationsPaginator,
        ListServicesPaginator,
    )

    client: CloudWatchApplicationSignalsClient = boto3.client("application-signals")

    list_service_dependencies_paginator: ListServiceDependenciesPaginator = client.get_paginator("list_service_dependencies")
    list_service_dependents_paginator: ListServiceDependentsPaginator = client.get_paginator("list_service_dependents")
    list_service_level_objectives_paginator: ListServiceLevelObjectivesPaginator = client.get_paginator("list_service_level_objectives")
    list_service_operations_paginator: ListServiceOperationsPaginator = client.get_paginator("list_service_operations")
    list_services_paginator: ListServicesPaginator = client.get_paginator("list_services")
    ```
"""

from datetime import datetime
from typing import Dict, Iterator, Union

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListServiceDependenciesOutputTypeDef,
    ListServiceDependentsOutputTypeDef,
    ListServiceLevelObjectivesOutputTypeDef,
    ListServiceOperationsOutputTypeDef,
    ListServicesOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListServiceDependenciesPaginator",
    "ListServiceDependentsPaginator",
    "ListServiceLevelObjectivesPaginator",
    "ListServiceOperationsPaginator",
    "ListServicesPaginator",
)

class ListServiceDependenciesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Paginator.ListServiceDependencies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/paginators.html#listservicedependenciespaginator)
    """

    def paginate(
        self,
        *,
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        KeyAttributes: Dict[str, str],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServiceDependenciesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Paginator.ListServiceDependencies.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/paginators.html#listservicedependenciespaginator)
        """

class ListServiceDependentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Paginator.ListServiceDependents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/paginators.html#listservicedependentspaginator)
    """

    def paginate(
        self,
        *,
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        KeyAttributes: Dict[str, str],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServiceDependentsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Paginator.ListServiceDependents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/paginators.html#listservicedependentspaginator)
        """

class ListServiceLevelObjectivesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Paginator.ListServiceLevelObjectives)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/paginators.html#listservicelevelobjectivespaginator)
    """

    def paginate(
        self,
        *,
        KeyAttributes: Dict[str, str] = None,
        OperationName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServiceLevelObjectivesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Paginator.ListServiceLevelObjectives.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/paginators.html#listservicelevelobjectivespaginator)
        """

class ListServiceOperationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Paginator.ListServiceOperations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/paginators.html#listserviceoperationspaginator)
    """

    def paginate(
        self,
        *,
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        KeyAttributes: Dict[str, str],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServiceOperationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Paginator.ListServiceOperations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/paginators.html#listserviceoperationspaginator)
        """

class ListServicesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Paginator.ListServices)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/paginators.html#listservicespaginator)
    """

    def paginate(
        self,
        *,
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServicesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/application-signals.html#CloudWatchApplicationSignals.Paginator.ListServices.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/paginators.html#listservicespaginator)
        """
