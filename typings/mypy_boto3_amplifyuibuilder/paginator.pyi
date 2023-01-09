"""
Type annotations for amplifyuibuilder service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_amplifyuibuilder import AmplifyUIBuilderClient
    from mypy_boto3_amplifyuibuilder.paginator import (
        ExportComponentsPaginator,
        ExportFormsPaginator,
        ExportThemesPaginator,
        ListComponentsPaginator,
        ListFormsPaginator,
        ListThemesPaginator,
    )

    client: AmplifyUIBuilderClient = boto3.client("amplifyuibuilder")

    export_components_paginator: ExportComponentsPaginator = client.get_paginator("export_components")
    export_forms_paginator: ExportFormsPaginator = client.get_paginator("export_forms")
    export_themes_paginator: ExportThemesPaginator = client.get_paginator("export_themes")
    list_components_paginator: ListComponentsPaginator = client.get_paginator("list_components")
    list_forms_paginator: ListFormsPaginator = client.get_paginator("list_forms")
    list_themes_paginator: ListThemesPaginator = client.get_paginator("list_themes")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ExportComponentsResponseTypeDef,
    ExportFormsResponseTypeDef,
    ExportThemesResponseTypeDef,
    ListComponentsResponseTypeDef,
    ListFormsResponseTypeDef,
    ListThemesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ExportComponentsPaginator",
    "ExportFormsPaginator",
    "ExportThemesPaginator",
    "ListComponentsPaginator",
    "ListFormsPaginator",
    "ListThemesPaginator",
)

class ExportComponentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Paginator.ExportComponents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/paginators.html#exportcomponentspaginator)
    """

    def paginate(
        self, *, appId: str, environmentName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ExportComponentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Paginator.ExportComponents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/paginators.html#exportcomponentspaginator)
        """

class ExportFormsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Paginator.ExportForms)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/paginators.html#exportformspaginator)
    """

    def paginate(
        self, *, appId: str, environmentName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ExportFormsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Paginator.ExportForms.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/paginators.html#exportformspaginator)
        """

class ExportThemesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Paginator.ExportThemes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/paginators.html#exportthemespaginator)
    """

    def paginate(
        self, *, appId: str, environmentName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ExportThemesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Paginator.ExportThemes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/paginators.html#exportthemespaginator)
        """

class ListComponentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Paginator.ListComponents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/paginators.html#listcomponentspaginator)
    """

    def paginate(
        self, *, appId: str, environmentName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListComponentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Paginator.ListComponents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/paginators.html#listcomponentspaginator)
        """

class ListFormsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Paginator.ListForms)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/paginators.html#listformspaginator)
    """

    def paginate(
        self, *, appId: str, environmentName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFormsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Paginator.ListForms.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/paginators.html#listformspaginator)
        """

class ListThemesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Paginator.ListThemes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/paginators.html#listthemespaginator)
    """

    def paginate(
        self, *, appId: str, environmentName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThemesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Paginator.ListThemes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/paginators.html#listthemespaginator)
        """
