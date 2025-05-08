"""
Type annotations for ses service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_ses.client import SESClient
    from mypy_boto3_ses.paginator import (
        ListConfigurationSetsPaginator,
        ListCustomVerificationEmailTemplatesPaginator,
        ListIdentitiesPaginator,
        ListReceiptRuleSetsPaginator,
        ListTemplatesPaginator,
    )

    session = Session()
    client: SESClient = session.client("ses")

    list_configuration_sets_paginator: ListConfigurationSetsPaginator = client.get_paginator("list_configuration_sets")
    list_custom_verification_email_templates_paginator: ListCustomVerificationEmailTemplatesPaginator = client.get_paginator("list_custom_verification_email_templates")
    list_identities_paginator: ListIdentitiesPaginator = client.get_paginator("list_identities")
    list_receipt_rule_sets_paginator: ListReceiptRuleSetsPaginator = client.get_paginator("list_receipt_rule_sets")
    list_templates_paginator: ListTemplatesPaginator = client.get_paginator("list_templates")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListConfigurationSetsRequestPaginateTypeDef,
    ListConfigurationSetsResponseTypeDef,
    ListCustomVerificationEmailTemplatesRequestPaginateTypeDef,
    ListCustomVerificationEmailTemplatesResponseTypeDef,
    ListIdentitiesRequestPaginateTypeDef,
    ListIdentitiesResponseTypeDef,
    ListReceiptRuleSetsRequestPaginateTypeDef,
    ListReceiptRuleSetsResponseTypeDef,
    ListTemplatesRequestPaginateTypeDef,
    ListTemplatesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListConfigurationSetsPaginator",
    "ListCustomVerificationEmailTemplatesPaginator",
    "ListIdentitiesPaginator",
    "ListReceiptRuleSetsPaginator",
    "ListTemplatesPaginator",
)

if TYPE_CHECKING:
    _ListConfigurationSetsPaginatorBase = Paginator[ListConfigurationSetsResponseTypeDef]
else:
    _ListConfigurationSetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConfigurationSetsPaginator(_ListConfigurationSetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses/paginator/ListConfigurationSets.html#SES.Paginator.ListConfigurationSets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators/#listconfigurationsetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConfigurationSetsRequestPaginateTypeDef]
    ) -> PageIterator[ListConfigurationSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses/paginator/ListConfigurationSets.html#SES.Paginator.ListConfigurationSets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators/#listconfigurationsetspaginator)
        """

if TYPE_CHECKING:
    _ListCustomVerificationEmailTemplatesPaginatorBase = Paginator[
        ListCustomVerificationEmailTemplatesResponseTypeDef
    ]
else:
    _ListCustomVerificationEmailTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListCustomVerificationEmailTemplatesPaginator(
    _ListCustomVerificationEmailTemplatesPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses/paginator/ListCustomVerificationEmailTemplates.html#SES.Paginator.ListCustomVerificationEmailTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators/#listcustomverificationemailtemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCustomVerificationEmailTemplatesRequestPaginateTypeDef]
    ) -> PageIterator[ListCustomVerificationEmailTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses/paginator/ListCustomVerificationEmailTemplates.html#SES.Paginator.ListCustomVerificationEmailTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators/#listcustomverificationemailtemplatespaginator)
        """

if TYPE_CHECKING:
    _ListIdentitiesPaginatorBase = Paginator[ListIdentitiesResponseTypeDef]
else:
    _ListIdentitiesPaginatorBase = Paginator  # type: ignore[assignment]

class ListIdentitiesPaginator(_ListIdentitiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses/paginator/ListIdentities.html#SES.Paginator.ListIdentities)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators/#listidentitiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIdentitiesRequestPaginateTypeDef]
    ) -> PageIterator[ListIdentitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses/paginator/ListIdentities.html#SES.Paginator.ListIdentities.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators/#listidentitiespaginator)
        """

if TYPE_CHECKING:
    _ListReceiptRuleSetsPaginatorBase = Paginator[ListReceiptRuleSetsResponseTypeDef]
else:
    _ListReceiptRuleSetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListReceiptRuleSetsPaginator(_ListReceiptRuleSetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses/paginator/ListReceiptRuleSets.html#SES.Paginator.ListReceiptRuleSets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators/#listreceiptrulesetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListReceiptRuleSetsRequestPaginateTypeDef]
    ) -> PageIterator[ListReceiptRuleSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses/paginator/ListReceiptRuleSets.html#SES.Paginator.ListReceiptRuleSets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators/#listreceiptrulesetspaginator)
        """

if TYPE_CHECKING:
    _ListTemplatesPaginatorBase = Paginator[ListTemplatesResponseTypeDef]
else:
    _ListTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListTemplatesPaginator(_ListTemplatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses/paginator/ListTemplates.html#SES.Paginator.ListTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators/#listtemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTemplatesRequestPaginateTypeDef]
    ) -> PageIterator[ListTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses/paginator/ListTemplates.html#SES.Paginator.ListTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators/#listtemplatespaginator)
        """
