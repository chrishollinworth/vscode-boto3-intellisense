"""
Type annotations for bedrock-data-automation service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_data_automation/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_bedrock_data_automation.client import DataAutomationforBedrockClient
    from mypy_boto3_bedrock_data_automation.paginator import (
        ListBlueprintsPaginator,
        ListDataAutomationProjectsPaginator,
    )

    session = Session()
    client: DataAutomationforBedrockClient = session.client("bedrock-data-automation")

    list_blueprints_paginator: ListBlueprintsPaginator = client.get_paginator("list_blueprints")
    list_data_automation_projects_paginator: ListDataAutomationProjectsPaginator = client.get_paginator("list_data_automation_projects")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListBlueprintsRequestPaginateTypeDef,
    ListBlueprintsResponseTypeDef,
    ListDataAutomationProjectsRequestPaginateTypeDef,
    ListDataAutomationProjectsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListBlueprintsPaginator", "ListDataAutomationProjectsPaginator")

if TYPE_CHECKING:
    _ListBlueprintsPaginatorBase = Paginator[ListBlueprintsResponseTypeDef]
else:
    _ListBlueprintsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBlueprintsPaginator(_ListBlueprintsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-data-automation/paginator/ListBlueprints.html#DataAutomationforBedrock.Paginator.ListBlueprints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_data_automation/paginators/#listblueprintspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBlueprintsRequestPaginateTypeDef]
    ) -> PageIterator[ListBlueprintsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-data-automation/paginator/ListBlueprints.html#DataAutomationforBedrock.Paginator.ListBlueprints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_data_automation/paginators/#listblueprintspaginator)
        """

if TYPE_CHECKING:
    _ListDataAutomationProjectsPaginatorBase = Paginator[ListDataAutomationProjectsResponseTypeDef]
else:
    _ListDataAutomationProjectsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataAutomationProjectsPaginator(_ListDataAutomationProjectsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-data-automation/paginator/ListDataAutomationProjects.html#DataAutomationforBedrock.Paginator.ListDataAutomationProjects)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_data_automation/paginators/#listdataautomationprojectspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataAutomationProjectsRequestPaginateTypeDef]
    ) -> PageIterator[ListDataAutomationProjectsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-data-automation/paginator/ListDataAutomationProjects.html#DataAutomationforBedrock.Paginator.ListDataAutomationProjects.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_data_automation/paginators/#listdataautomationprojectspaginator)
        """
