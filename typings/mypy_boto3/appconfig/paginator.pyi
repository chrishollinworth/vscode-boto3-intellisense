"""
Type annotations for appconfig service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_appconfig import AppConfigClient
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

    client: AppConfigClient = boto3.client("appconfig")

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

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ApplicationsTypeDef,
    ConfigurationProfilesTypeDef,
    DeploymentStrategiesTypeDef,
    DeploymentsTypeDef,
    EnvironmentsTypeDef,
    ExtensionAssociationsTypeDef,
    ExtensionsTypeDef,
    HostedConfigurationVersionsTypeDef,
    PaginatorConfigTypeDef,
)

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

class ListApplicationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appconfig.html#AppConfig.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators.html#listapplicationspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ApplicationsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appconfig.html#AppConfig.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators.html#listapplicationspaginator)
        """

class ListConfigurationProfilesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appconfig.html#AppConfig.Paginator.ListConfigurationProfiles)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators.html#listconfigurationprofilespaginator)
    """

    def paginate(
        self,
        *,
        ApplicationId: str,
        Type: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ConfigurationProfilesTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appconfig.html#AppConfig.Paginator.ListConfigurationProfiles.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators.html#listconfigurationprofilespaginator)
        """

class ListDeploymentStrategiesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appconfig.html#AppConfig.Paginator.ListDeploymentStrategies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators.html#listdeploymentstrategiespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DeploymentStrategiesTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appconfig.html#AppConfig.Paginator.ListDeploymentStrategies.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators.html#listdeploymentstrategiespaginator)
        """

class ListDeploymentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appconfig.html#AppConfig.Paginator.ListDeployments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators.html#listdeploymentspaginator)
    """

    def paginate(
        self,
        *,
        ApplicationId: str,
        EnvironmentId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DeploymentsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appconfig.html#AppConfig.Paginator.ListDeployments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators.html#listdeploymentspaginator)
        """

class ListEnvironmentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appconfig.html#AppConfig.Paginator.ListEnvironments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators.html#listenvironmentspaginator)
    """

    def paginate(
        self, *, ApplicationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[EnvironmentsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appconfig.html#AppConfig.Paginator.ListEnvironments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators.html#listenvironmentspaginator)
        """

class ListExtensionAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appconfig.html#AppConfig.Paginator.ListExtensionAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators.html#listextensionassociationspaginator)
    """

    def paginate(
        self,
        *,
        ResourceIdentifier: str = None,
        ExtensionIdentifier: str = None,
        ExtensionVersionNumber: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ExtensionAssociationsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appconfig.html#AppConfig.Paginator.ListExtensionAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators.html#listextensionassociationspaginator)
        """

class ListExtensionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appconfig.html#AppConfig.Paginator.ListExtensions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators.html#listextensionspaginator)
    """

    def paginate(
        self, *, Name: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ExtensionsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appconfig.html#AppConfig.Paginator.ListExtensions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators.html#listextensionspaginator)
        """

class ListHostedConfigurationVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appconfig.html#AppConfig.Paginator.ListHostedConfigurationVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators.html#listhostedconfigurationversionspaginator)
    """

    def paginate(
        self,
        *,
        ApplicationId: str,
        ConfigurationProfileId: str,
        VersionLabel: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[HostedConfigurationVersionsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appconfig.html#AppConfig.Paginator.ListHostedConfigurationVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/paginators.html#listhostedconfigurationversionspaginator)
        """
