"""
Type annotations for ssm-sap service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_ssm_sap import SsmSapClient
    from mypy_boto3_ssm_sap.paginator import (
        ListApplicationsPaginator,
        ListComponentsPaginator,
        ListDatabasesPaginator,
    )

    client: SsmSapClient = boto3.client("ssm-sap")

    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_components_paginator: ListComponentsPaginator = client.get_paginator("list_components")
    list_databases_paginator: ListDatabasesPaginator = client.get_paginator("list_databases")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListApplicationsOutputTypeDef,
    ListComponentsOutputTypeDef,
    ListDatabasesOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListApplicationsPaginator", "ListComponentsPaginator", "ListDatabasesPaginator")

class ListApplicationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ssm-sap.html#SsmSap.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/paginators.html#listapplicationspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ssm-sap.html#SsmSap.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/paginators.html#listapplicationspaginator)
        """

class ListComponentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ssm-sap.html#SsmSap.Paginator.ListComponents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/paginators.html#listcomponentspaginator)
    """

    def paginate(
        self, *, ApplicationId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListComponentsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ssm-sap.html#SsmSap.Paginator.ListComponents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/paginators.html#listcomponentspaginator)
        """

class ListDatabasesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ssm-sap.html#SsmSap.Paginator.ListDatabases)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/paginators.html#listdatabasespaginator)
    """

    def paginate(
        self,
        *,
        ApplicationId: str = None,
        ComponentId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatabasesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/ssm-sap.html#SsmSap.Paginator.ListDatabases.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/paginators.html#listdatabasespaginator)
        """
