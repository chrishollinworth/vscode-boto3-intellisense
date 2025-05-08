"""
Type annotations for appconfig service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_appconfig.client import AppConfigClient
    from mypy_boto3_appconfig.paginator import (
        ListApplicationsPaginator,
        ListConfigurationProfilesPaginator,
        ListDeploymentStrategiesPaginator,
        ListDeploymentsPaginator,
        ListEnvironmentsPaginator,
        ListExtensionAssociationsPaginator,
        ListExtensionsPaginator,
        ListHostedConfigurationVersionsPaginator,
    )

    session = Session()
    client: AppConfigClient = session.client("appconfig")

    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_configuration_profiles_paginator: ListConfigurationProfilesPaginator = client.get_paginator("list_configuration_profiles")
    list_deployment_strategies_paginator: ListDeploymentStrategiesPaginator = client.get_paginator("list_deployment_strategies")
    list_deployments_paginator: ListDeploymentsPaginator = client.get_paginator("list_deployments")
    list_environments_paginator: ListEnvironmentsPaginator = client.get_paginator("list_environments")
    list_extension_associations_paginator: ListExtensionAssociationsPaginator = client.get_paginator("list_extension_associations")
    list_extensions_paginator: ListExtensionsPaginator = client.get_paginator("list_extensions")
    list_hosted_configuration_versions_paginator: ListHostedConfigurationVersionsPaginator = client.get_paginator("list_hosted_configuration_versions")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ApplicationsTypeDef,
    ConfigurationProfilesTypeDef,
    DeploymentStrategiesTypeDef,
    DeploymentsTypeDef,
    EnvironmentsTypeDef,
    ExtensionAssociationsTypeDef,
    ExtensionsTypeDef,
    HostedConfigurationVersionsTypeDef,
    ListApplicationsRequestPaginateTypeDef,
    ListConfigurationProfilesRequestPaginateTypeDef,
    ListDeploymentsRequestPaginateTypeDef,
    ListDeploymentStrategiesRequestPaginateTypeDef,
    ListEnvironmentsRequestPaginateTypeDef,
    ListExtensionAssociationsRequestPaginateTypeDef,
    ListExtensionsRequestPaginateTypeDef,
    ListHostedConfigurationVersionsRequestPaginateTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListApplicationsPaginator",
    "ListConfigurationProfilesPaginator",
    "ListDeploymentStrategiesPaginator",
    "ListDeploymentsPaginator",
    "ListEnvironmentsPaginator",
    "ListExtensionAssociationsPaginator",
    "ListExtensionsPaginator",
    "ListHostedConfigurationVersionsPaginator",
)

if TYPE_CHECKING:
    _ListApplicationsPaginatorBase = Paginator[ApplicationsTypeDef]
else:
    _ListApplicationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListApplicationsPaginator(_ListApplicationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/paginator/ListApplications.html#AppConfig.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators/#listapplicationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApplicationsRequestPaginateTypeDef]
    ) -> PageIterator[ApplicationsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/paginator/ListApplications.html#AppConfig.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators/#listapplicationspaginator)
        """

if TYPE_CHECKING:
    _ListConfigurationProfilesPaginatorBase = Paginator[ConfigurationProfilesTypeDef]
else:
    _ListConfigurationProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class ListConfigurationProfilesPaginator(_ListConfigurationProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/paginator/ListConfigurationProfiles.html#AppConfig.Paginator.ListConfigurationProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators/#listconfigurationprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConfigurationProfilesRequestPaginateTypeDef]
    ) -> PageIterator[ConfigurationProfilesTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/paginator/ListConfigurationProfiles.html#AppConfig.Paginator.ListConfigurationProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators/#listconfigurationprofilespaginator)
        """

if TYPE_CHECKING:
    _ListDeploymentStrategiesPaginatorBase = Paginator[DeploymentStrategiesTypeDef]
else:
    _ListDeploymentStrategiesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDeploymentStrategiesPaginator(_ListDeploymentStrategiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/paginator/ListDeploymentStrategies.html#AppConfig.Paginator.ListDeploymentStrategies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators/#listdeploymentstrategiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDeploymentStrategiesRequestPaginateTypeDef]
    ) -> PageIterator[DeploymentStrategiesTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/paginator/ListDeploymentStrategies.html#AppConfig.Paginator.ListDeploymentStrategies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators/#listdeploymentstrategiespaginator)
        """

if TYPE_CHECKING:
    _ListDeploymentsPaginatorBase = Paginator[DeploymentsTypeDef]
else:
    _ListDeploymentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDeploymentsPaginator(_ListDeploymentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/paginator/ListDeployments.html#AppConfig.Paginator.ListDeployments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators/#listdeploymentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDeploymentsRequestPaginateTypeDef]
    ) -> PageIterator[DeploymentsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/paginator/ListDeployments.html#AppConfig.Paginator.ListDeployments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators/#listdeploymentspaginator)
        """

if TYPE_CHECKING:
    _ListEnvironmentsPaginatorBase = Paginator[EnvironmentsTypeDef]
else:
    _ListEnvironmentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEnvironmentsPaginator(_ListEnvironmentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/paginator/ListEnvironments.html#AppConfig.Paginator.ListEnvironments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators/#listenvironmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnvironmentsRequestPaginateTypeDef]
    ) -> PageIterator[EnvironmentsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/paginator/ListEnvironments.html#AppConfig.Paginator.ListEnvironments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators/#listenvironmentspaginator)
        """

if TYPE_CHECKING:
    _ListExtensionAssociationsPaginatorBase = Paginator[ExtensionAssociationsTypeDef]
else:
    _ListExtensionAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListExtensionAssociationsPaginator(_ListExtensionAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/paginator/ListExtensionAssociations.html#AppConfig.Paginator.ListExtensionAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators/#listextensionassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListExtensionAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ExtensionAssociationsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/paginator/ListExtensionAssociations.html#AppConfig.Paginator.ListExtensionAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators/#listextensionassociationspaginator)
        """

if TYPE_CHECKING:
    _ListExtensionsPaginatorBase = Paginator[ExtensionsTypeDef]
else:
    _ListExtensionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListExtensionsPaginator(_ListExtensionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/paginator/ListExtensions.html#AppConfig.Paginator.ListExtensions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators/#listextensionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListExtensionsRequestPaginateTypeDef]
    ) -> PageIterator[ExtensionsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/paginator/ListExtensions.html#AppConfig.Paginator.ListExtensions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators/#listextensionspaginator)
        """

if TYPE_CHECKING:
    _ListHostedConfigurationVersionsPaginatorBase = Paginator[HostedConfigurationVersionsTypeDef]
else:
    _ListHostedConfigurationVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListHostedConfigurationVersionsPaginator(_ListHostedConfigurationVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/paginator/ListHostedConfigurationVersions.html#AppConfig.Paginator.ListHostedConfigurationVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators/#listhostedconfigurationversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListHostedConfigurationVersionsRequestPaginateTypeDef]
    ) -> PageIterator[HostedConfigurationVersionsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig/paginator/ListHostedConfigurationVersions.html#AppConfig.Paginator.ListHostedConfigurationVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators/#listhostedconfigurationversionspaginator)
        """
