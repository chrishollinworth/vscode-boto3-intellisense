"""
Main interface for workspaces-web service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_workspaces_web import (
        Client,
        ListDataProtectionSettingsPaginator,
        ListSessionLoggersPaginator,
        ListSessionsPaginator,
        WorkSpacesWebClient,
    )

    session = Session()
    client: WorkSpacesWebClient = session.client("workspaces-web")

    list_data_protection_settings_paginator: ListDataProtectionSettingsPaginator = client.get_paginator("list_data_protection_settings")
    list_session_loggers_paginator: ListSessionLoggersPaginator = client.get_paginator("list_session_loggers")
    list_sessions_paginator: ListSessionsPaginator = client.get_paginator("list_sessions")
    ```
"""

from .client import WorkSpacesWebClient
from .paginator import (
    ListDataProtectionSettingsPaginator,
    ListSessionLoggersPaginator,
    ListSessionsPaginator,
)

Client = WorkSpacesWebClient

__all__ = (
    "Client",
    "ListDataProtectionSettingsPaginator",
    "ListSessionLoggersPaginator",
    "ListSessionsPaginator",
    "WorkSpacesWebClient",
)
