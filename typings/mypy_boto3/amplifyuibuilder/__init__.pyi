"""
Main interface for amplifyuibuilder service.

Usage::

    ```python
    import boto3
    from mypy_boto3_amplifyuibuilder import (
        AmplifyUIBuilderClient,
        Client,
        ExportComponentsPaginator,
        ExportFormsPaginator,
        ExportThemesPaginator,
        ListComponentsPaginator,
        ListFormsPaginator,
        ListThemesPaginator,
    )

    session = boto3.Session()

    client: AmplifyUIBuilderClient = boto3.client("amplifyuibuilder")
    session_client: AmplifyUIBuilderClient = session.client("amplifyuibuilder")

    export_components_paginator: ExportComponentsPaginator = client.get_paginator("export_components")
    export_forms_paginator: ExportFormsPaginator = client.get_paginator("export_forms")
    export_themes_paginator: ExportThemesPaginator = client.get_paginator("export_themes")
    list_components_paginator: ListComponentsPaginator = client.get_paginator("list_components")
    list_forms_paginator: ListFormsPaginator = client.get_paginator("list_forms")
    list_themes_paginator: ListThemesPaginator = client.get_paginator("list_themes")
    ```
"""
from .client import AmplifyUIBuilderClient
from .paginator import (
    ExportComponentsPaginator,
    ExportFormsPaginator,
    ExportThemesPaginator,
    ListComponentsPaginator,
    ListFormsPaginator,
    ListThemesPaginator,
)

Client = AmplifyUIBuilderClient

__all__ = (
    "AmplifyUIBuilderClient",
    "Client",
    "ExportComponentsPaginator",
    "ExportFormsPaginator",
    "ExportThemesPaginator",
    "ListComponentsPaginator",
    "ListFormsPaginator",
    "ListThemesPaginator",
)
