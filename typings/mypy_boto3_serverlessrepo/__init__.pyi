"""
Main interface for serverlessrepo service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_serverlessrepo import (
        Client,
        ListApplicationDependenciesPaginator,
        ListApplicationVersionsPaginator,
        ListApplicationsPaginator,
        ServerlessApplicationRepositoryClient,
    )

    session = Session()
    client: ServerlessApplicationRepositoryClient = session.client("serverlessrepo")

    list_application_dependencies_paginator: ListApplicationDependenciesPaginator = client.get_paginator("list_application_dependencies")
    list_application_versions_paginator: ListApplicationVersionsPaginator = client.get_paginator("list_application_versions")
    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    ```
"""

from .client import ServerlessApplicationRepositoryClient
from .paginator import (
    ListApplicationDependenciesPaginator,
    ListApplicationsPaginator,
    ListApplicationVersionsPaginator,
)

Client = ServerlessApplicationRepositoryClient

__all__ = (
    "Client",
    "ListApplicationDependenciesPaginator",
    "ListApplicationVersionsPaginator",
    "ListApplicationsPaginator",
    "ServerlessApplicationRepositoryClient",
)
