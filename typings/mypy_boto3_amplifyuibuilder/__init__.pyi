"""
Main interface for amplifyuibuilder service.

Usage::

    ```python
    import boto3
    from mypy_boto3_amplifyuibuilder import (
        AmplifyUIBuilderClient,
        Client,
        ListComponentsPaginator,
        ListThemesPaginator,
    )

    session = boto3.Session()

    client: AmplifyUIBuilderClient = boto3.client("amplifyuibuilder")
    session_client: AmplifyUIBuilderClient = session.client("amplifyuibuilder")

    list_components_paginator: ListComponentsPaginator = client.get_paginator("list_components")
    list_themes_paginator: ListThemesPaginator = client.get_paginator("list_themes")
    ```
"""
from .client import AmplifyUIBuilderClient
from .paginator import ListComponentsPaginator, ListThemesPaginator

Client = AmplifyUIBuilderClient

__all__ = ("AmplifyUIBuilderClient", "Client", "ListComponentsPaginator", "ListThemesPaginator")
