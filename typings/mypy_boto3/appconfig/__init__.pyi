"""
Main interface for appconfig service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_appconfig import (
        AppConfigClient,
        Client,
        DeploymentCompleteWaiter,
        EnvironmentReadyForDeploymentWaiter,
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

    deployment_complete_waiter: DeploymentCompleteWaiter = client.get_waiter("deployment_complete")
    environment_ready_for_deployment_waiter: EnvironmentReadyForDeploymentWaiter = client.get_waiter("environment_ready_for_deployment")

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

from .client import AppConfigClient
from .paginator import (
    ListApplicationsPaginator,
    ListConfigurationProfilesPaginator,
    ListDeploymentsPaginator,
    ListDeploymentStrategiesPaginator,
    ListEnvironmentsPaginator,
    ListExtensionAssociationsPaginator,
    ListExtensionsPaginator,
    ListHostedConfigurationVersionsPaginator,
)
from .waiter import DeploymentCompleteWaiter, EnvironmentReadyForDeploymentWaiter

Client = AppConfigClient

__all__ = (
    "AppConfigClient",
    "Client",
    "DeploymentCompleteWaiter",
    "EnvironmentReadyForDeploymentWaiter",
    "ListApplicationsPaginator",
    "ListConfigurationProfilesPaginator",
    "ListDeploymentStrategiesPaginator",
    "ListDeploymentsPaginator",
    "ListEnvironmentsPaginator",
    "ListExtensionAssociationsPaginator",
    "ListExtensionsPaginator",
    "ListHostedConfigurationVersionsPaginator",
)
