"""
Type annotations for ssm-sap service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_ssm_sap.client import SsmSapClient
    from mypy_boto3_ssm_sap.paginator import (
        ListApplicationsPaginator,
        ListComponentsPaginator,
        ListDatabasesPaginator,
        ListOperationEventsPaginator,
        ListOperationsPaginator,
    )

    session = Session()
    client: SsmSapClient = session.client("ssm-sap")

    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_components_paginator: ListComponentsPaginator = client.get_paginator("list_components")
    list_databases_paginator: ListDatabasesPaginator = client.get_paginator("list_databases")
    list_operation_events_paginator: ListOperationEventsPaginator = client.get_paginator("list_operation_events")
    list_operations_paginator: ListOperationsPaginator = client.get_paginator("list_operations")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListApplicationsInputPaginateTypeDef,
    ListApplicationsOutputTypeDef,
    ListComponentsInputPaginateTypeDef,
    ListComponentsOutputTypeDef,
    ListDatabasesInputPaginateTypeDef,
    ListDatabasesOutputTypeDef,
    ListOperationEventsInputPaginateTypeDef,
    ListOperationEventsOutputTypeDef,
    ListOperationsInputPaginateTypeDef,
    ListOperationsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListApplicationsPaginator",
    "ListComponentsPaginator",
    "ListDatabasesPaginator",
    "ListOperationEventsPaginator",
    "ListOperationsPaginator",
)

if TYPE_CHECKING:
    _ListApplicationsPaginatorBase = Paginator[ListApplicationsOutputTypeDef]
else:
    _ListApplicationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListApplicationsPaginator(_ListApplicationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap/paginator/ListApplications.html#SsmSap.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/paginators/#listapplicationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApplicationsInputPaginateTypeDef]
    ) -> PageIterator[ListApplicationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap/paginator/ListApplications.html#SsmSap.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/paginators/#listapplicationspaginator)
        """

if TYPE_CHECKING:
    _ListComponentsPaginatorBase = Paginator[ListComponentsOutputTypeDef]
else:
    _ListComponentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListComponentsPaginator(_ListComponentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap/paginator/ListComponents.html#SsmSap.Paginator.ListComponents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/paginators/#listcomponentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListComponentsInputPaginateTypeDef]
    ) -> PageIterator[ListComponentsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap/paginator/ListComponents.html#SsmSap.Paginator.ListComponents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/paginators/#listcomponentspaginator)
        """

if TYPE_CHECKING:
    _ListDatabasesPaginatorBase = Paginator[ListDatabasesOutputTypeDef]
else:
    _ListDatabasesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDatabasesPaginator(_ListDatabasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap/paginator/ListDatabases.html#SsmSap.Paginator.ListDatabases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/paginators/#listdatabasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDatabasesInputPaginateTypeDef]
    ) -> PageIterator[ListDatabasesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap/paginator/ListDatabases.html#SsmSap.Paginator.ListDatabases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/paginators/#listdatabasespaginator)
        """

if TYPE_CHECKING:
    _ListOperationEventsPaginatorBase = Paginator[ListOperationEventsOutputTypeDef]
else:
    _ListOperationEventsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOperationEventsPaginator(_ListOperationEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap/paginator/ListOperationEvents.html#SsmSap.Paginator.ListOperationEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/paginators/#listoperationeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOperationEventsInputPaginateTypeDef]
    ) -> PageIterator[ListOperationEventsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap/paginator/ListOperationEvents.html#SsmSap.Paginator.ListOperationEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/paginators/#listoperationeventspaginator)
        """

if TYPE_CHECKING:
    _ListOperationsPaginatorBase = Paginator[ListOperationsOutputTypeDef]
else:
    _ListOperationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOperationsPaginator(_ListOperationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap/paginator/ListOperations.html#SsmSap.Paginator.ListOperations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/paginators/#listoperationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOperationsInputPaginateTypeDef]
    ) -> PageIterator[ListOperationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap/paginator/ListOperations.html#SsmSap.Paginator.ListOperations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/paginators/#listoperationspaginator)
        """
