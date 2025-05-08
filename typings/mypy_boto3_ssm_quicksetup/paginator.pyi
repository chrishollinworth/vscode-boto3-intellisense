"""
Type annotations for ssm-quicksetup service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_ssm_quicksetup.client import SystemsManagerQuickSetupClient
    from mypy_boto3_ssm_quicksetup.paginator import (
        ListConfigurationManagersPaginator,
        ListConfigurationsPaginator,
    )

    session = Session()
    client: SystemsManagerQuickSetupClient = session.client("ssm-quicksetup")

    list_configuration_managers_paginator: ListConfigurationManagersPaginator = client.get_paginator("list_configuration_managers")
    list_configurations_paginator: ListConfigurationsPaginator = client.get_paginator("list_configurations")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListConfigurationManagersInputPaginateTypeDef,
    ListConfigurationManagersOutputTypeDef,
    ListConfigurationsInputPaginateTypeDef,
    ListConfigurationsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListConfigurationManagersPaginator", "ListConfigurationsPaginator")

if TYPE_CHECKING:
    _ListConfigurationManagersPaginatorBase = Paginator[ListConfigurationManagersOutputTypeDef]
else:
    _ListConfigurationManagersPaginatorBase = Paginator  # type: ignore[assignment]

class ListConfigurationManagersPaginator(_ListConfigurationManagersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup/paginator/ListConfigurationManagers.html#SystemsManagerQuickSetup.Paginator.ListConfigurationManagers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/paginators/#listconfigurationmanagerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConfigurationManagersInputPaginateTypeDef]
    ) -> PageIterator[ListConfigurationManagersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup/paginator/ListConfigurationManagers.html#SystemsManagerQuickSetup.Paginator.ListConfigurationManagers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/paginators/#listconfigurationmanagerspaginator)
        """

if TYPE_CHECKING:
    _ListConfigurationsPaginatorBase = Paginator[ListConfigurationsOutputTypeDef]
else:
    _ListConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConfigurationsPaginator(_ListConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup/paginator/ListConfigurations.html#SystemsManagerQuickSetup.Paginator.ListConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/paginators/#listconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConfigurationsInputPaginateTypeDef]
    ) -> PageIterator[ListConfigurationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup/paginator/ListConfigurations.html#SystemsManagerQuickSetup.Paginator.ListConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/paginators/#listconfigurationspaginator)
        """
