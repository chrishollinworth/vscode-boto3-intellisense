"""
Type annotations for amplifyuibuilder service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_amplifyuibuilder import AmplifyUIBuilderClient
    from mypy_boto3_amplifyuibuilder.paginator import (
        ListComponentsPaginator,
        ListThemesPaginator,
    )

    client: AmplifyUIBuilderClient = boto3.client("amplifyuibuilder")

    list_components_paginator: ListComponentsPaginator = client.get_paginator("list_components")
    list_themes_paginator: ListThemesPaginator = client.get_paginator("list_themes")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListComponentsResponseTypeDef,
    ListThemesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListComponentsPaginator", "ListThemesPaginator")

class ListComponentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Paginator.ListComponents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/paginators.html#listcomponentspaginator)
    """

    def paginate(
        self, *, appId: str, environmentName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListComponentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Paginator.ListComponents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/paginators.html#listcomponentspaginator)
        """

class ListThemesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Paginator.ListThemes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/paginators.html#listthemespaginator)
    """

    def paginate(
        self, *, appId: str, environmentName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThemesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Paginator.ListThemes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/paginators.html#listthemespaginator)
        """
