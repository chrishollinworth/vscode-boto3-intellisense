"""
Type annotations for fis service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_fis.client import FISClient
    from mypy_boto3_fis.paginator import (
        ListActionsPaginator,
        ListExperimentResolvedTargetsPaginator,
        ListExperimentTemplatesPaginator,
        ListExperimentsPaginator,
        ListTargetAccountConfigurationsPaginator,
        ListTargetResourceTypesPaginator,
    )

    session = Session()
    client: FISClient = session.client("fis")

    list_actions_paginator: ListActionsPaginator = client.get_paginator("list_actions")
    list_experiment_resolved_targets_paginator: ListExperimentResolvedTargetsPaginator = client.get_paginator("list_experiment_resolved_targets")
    list_experiment_templates_paginator: ListExperimentTemplatesPaginator = client.get_paginator("list_experiment_templates")
    list_experiments_paginator: ListExperimentsPaginator = client.get_paginator("list_experiments")
    list_target_account_configurations_paginator: ListTargetAccountConfigurationsPaginator = client.get_paginator("list_target_account_configurations")
    list_target_resource_types_paginator: ListTargetResourceTypesPaginator = client.get_paginator("list_target_resource_types")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListActionsRequestPaginateTypeDef,
    ListActionsResponseTypeDef,
    ListExperimentResolvedTargetsRequestPaginateTypeDef,
    ListExperimentResolvedTargetsResponseTypeDef,
    ListExperimentsRequestPaginateTypeDef,
    ListExperimentsResponseTypeDef,
    ListExperimentTemplatesRequestPaginateTypeDef,
    ListExperimentTemplatesResponseTypeDef,
    ListTargetAccountConfigurationsRequestPaginateTypeDef,
    ListTargetAccountConfigurationsResponseTypeDef,
    ListTargetResourceTypesRequestPaginateTypeDef,
    ListTargetResourceTypesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListActionsPaginator",
    "ListExperimentResolvedTargetsPaginator",
    "ListExperimentTemplatesPaginator",
    "ListExperimentsPaginator",
    "ListTargetAccountConfigurationsPaginator",
    "ListTargetResourceTypesPaginator",
)

if TYPE_CHECKING:
    _ListActionsPaginatorBase = Paginator[ListActionsResponseTypeDef]
else:
    _ListActionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListActionsPaginator(_ListActionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/paginator/ListActions.html#FIS.Paginator.ListActions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/paginators/#listactionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListActionsRequestPaginateTypeDef]
    ) -> PageIterator[ListActionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/paginator/ListActions.html#FIS.Paginator.ListActions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/paginators/#listactionspaginator)
        """

if TYPE_CHECKING:
    _ListExperimentResolvedTargetsPaginatorBase = Paginator[
        ListExperimentResolvedTargetsResponseTypeDef
    ]
else:
    _ListExperimentResolvedTargetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListExperimentResolvedTargetsPaginator(_ListExperimentResolvedTargetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/paginator/ListExperimentResolvedTargets.html#FIS.Paginator.ListExperimentResolvedTargets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/paginators/#listexperimentresolvedtargetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListExperimentResolvedTargetsRequestPaginateTypeDef]
    ) -> PageIterator[ListExperimentResolvedTargetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/paginator/ListExperimentResolvedTargets.html#FIS.Paginator.ListExperimentResolvedTargets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/paginators/#listexperimentresolvedtargetspaginator)
        """

if TYPE_CHECKING:
    _ListExperimentTemplatesPaginatorBase = Paginator[ListExperimentTemplatesResponseTypeDef]
else:
    _ListExperimentTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListExperimentTemplatesPaginator(_ListExperimentTemplatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/paginator/ListExperimentTemplates.html#FIS.Paginator.ListExperimentTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/paginators/#listexperimenttemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListExperimentTemplatesRequestPaginateTypeDef]
    ) -> PageIterator[ListExperimentTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/paginator/ListExperimentTemplates.html#FIS.Paginator.ListExperimentTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/paginators/#listexperimenttemplatespaginator)
        """

if TYPE_CHECKING:
    _ListExperimentsPaginatorBase = Paginator[ListExperimentsResponseTypeDef]
else:
    _ListExperimentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListExperimentsPaginator(_ListExperimentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/paginator/ListExperiments.html#FIS.Paginator.ListExperiments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/paginators/#listexperimentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListExperimentsRequestPaginateTypeDef]
    ) -> PageIterator[ListExperimentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/paginator/ListExperiments.html#FIS.Paginator.ListExperiments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/paginators/#listexperimentspaginator)
        """

if TYPE_CHECKING:
    _ListTargetAccountConfigurationsPaginatorBase = Paginator[
        ListTargetAccountConfigurationsResponseTypeDef
    ]
else:
    _ListTargetAccountConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTargetAccountConfigurationsPaginator(_ListTargetAccountConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/paginator/ListTargetAccountConfigurations.html#FIS.Paginator.ListTargetAccountConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/paginators/#listtargetaccountconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTargetAccountConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[ListTargetAccountConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/paginator/ListTargetAccountConfigurations.html#FIS.Paginator.ListTargetAccountConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/paginators/#listtargetaccountconfigurationspaginator)
        """

if TYPE_CHECKING:
    _ListTargetResourceTypesPaginatorBase = Paginator[ListTargetResourceTypesResponseTypeDef]
else:
    _ListTargetResourceTypesPaginatorBase = Paginator  # type: ignore[assignment]

class ListTargetResourceTypesPaginator(_ListTargetResourceTypesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/paginator/ListTargetResourceTypes.html#FIS.Paginator.ListTargetResourceTypes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/paginators/#listtargetresourcetypespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTargetResourceTypesRequestPaginateTypeDef]
    ) -> PageIterator[ListTargetResourceTypesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis/paginator/ListTargetResourceTypes.html#FIS.Paginator.ListTargetResourceTypes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/paginators/#listtargetresourcetypespaginator)
        """
