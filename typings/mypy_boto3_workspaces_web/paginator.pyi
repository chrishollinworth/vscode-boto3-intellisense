"""
Type annotations for workspaces-web service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_workspaces_web.client import WorkSpacesWebClient
    from mypy_boto3_workspaces_web.paginator import (
        ListDataProtectionSettingsPaginator,
        ListSessionLoggersPaginator,
        ListSessionsPaginator,
    )

    session = Session()
    client: WorkSpacesWebClient = session.client("workspaces-web")

    list_data_protection_settings_paginator: ListDataProtectionSettingsPaginator = client.get_paginator("list_data_protection_settings")
    list_session_loggers_paginator: ListSessionLoggersPaginator = client.get_paginator("list_session_loggers")
    list_sessions_paginator: ListSessionsPaginator = client.get_paginator("list_sessions")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListDataProtectionSettingsRequestPaginateTypeDef,
    ListDataProtectionSettingsResponseTypeDef,
    ListSessionLoggersRequestPaginateTypeDef,
    ListSessionLoggersResponseTypeDef,
    ListSessionsRequestPaginateTypeDef,
    ListSessionsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListDataProtectionSettingsPaginator",
    "ListSessionLoggersPaginator",
    "ListSessionsPaginator",
)

if TYPE_CHECKING:
    _ListDataProtectionSettingsPaginatorBase = Paginator[ListDataProtectionSettingsResponseTypeDef]
else:
    _ListDataProtectionSettingsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataProtectionSettingsPaginator(_ListDataProtectionSettingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/paginator/ListDataProtectionSettings.html#WorkSpacesWeb.Paginator.ListDataProtectionSettings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/paginators/#listdataprotectionsettingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataProtectionSettingsRequestPaginateTypeDef]
    ) -> PageIterator[ListDataProtectionSettingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/paginator/ListDataProtectionSettings.html#WorkSpacesWeb.Paginator.ListDataProtectionSettings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/paginators/#listdataprotectionsettingspaginator)
        """

if TYPE_CHECKING:
    _ListSessionLoggersPaginatorBase = Paginator[ListSessionLoggersResponseTypeDef]
else:
    _ListSessionLoggersPaginatorBase = Paginator  # type: ignore[assignment]

class ListSessionLoggersPaginator(_ListSessionLoggersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/paginator/ListSessionLoggers.html#WorkSpacesWeb.Paginator.ListSessionLoggers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/paginators/#listsessionloggerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSessionLoggersRequestPaginateTypeDef]
    ) -> PageIterator[ListSessionLoggersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/paginator/ListSessionLoggers.html#WorkSpacesWeb.Paginator.ListSessionLoggers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/paginators/#listsessionloggerspaginator)
        """

if TYPE_CHECKING:
    _ListSessionsPaginatorBase = Paginator[ListSessionsResponseTypeDef]
else:
    _ListSessionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSessionsPaginator(_ListSessionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/paginator/ListSessions.html#WorkSpacesWeb.Paginator.ListSessions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/paginators/#listsessionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSessionsRequestPaginateTypeDef]
    ) -> PageIterator[ListSessionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/paginator/ListSessions.html#WorkSpacesWeb.Paginator.ListSessions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/paginators/#listsessionspaginator)
        """
