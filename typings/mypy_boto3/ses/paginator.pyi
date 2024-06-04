"""
Type annotations for ses service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_ses import SESClient
    from mypy_boto3_ses.paginator import (
        ListConfigurationSetsPaginator,
        ListCustomVerificationEmailTemplatesPaginator,
        ListIdentitiesPaginator,
        ListReceiptRuleSetsPaginator,
        ListTemplatesPaginator,
    )

    client: SESClient = boto3.client("ses")

    list_configuration_sets_paginator: ListConfigurationSetsPaginator = client.get_paginator("list_configuration_sets")
    list_custom_verification_email_templates_paginator: ListCustomVerificationEmailTemplatesPaginator = client.get_paginator("list_custom_verification_email_templates")
    list_identities_paginator: ListIdentitiesPaginator = client.get_paginator("list_identities")
    list_receipt_rule_sets_paginator: ListReceiptRuleSetsPaginator = client.get_paginator("list_receipt_rule_sets")
    list_templates_paginator: ListTemplatesPaginator = client.get_paginator("list_templates")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import IdentityTypeType
from .type_defs import (
    ListConfigurationSetsResponseTypeDef,
    ListCustomVerificationEmailTemplatesResponseTypeDef,
    ListIdentitiesResponseTypeDef,
    ListReceiptRuleSetsResponseTypeDef,
    ListTemplatesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListConfigurationSetsPaginator",
    "ListCustomVerificationEmailTemplatesPaginator",
    "ListIdentitiesPaginator",
    "ListReceiptRuleSetsPaginator",
    "ListTemplatesPaginator",
)

class ListConfigurationSetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ses.html#SES.Paginator.ListConfigurationSets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators.html#listconfigurationsetspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConfigurationSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ses.html#SES.Paginator.ListConfigurationSets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators.html#listconfigurationsetspaginator)
        """

class ListCustomVerificationEmailTemplatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ses.html#SES.Paginator.ListCustomVerificationEmailTemplates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators.html#listcustomverificationemailtemplatespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCustomVerificationEmailTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ses.html#SES.Paginator.ListCustomVerificationEmailTemplates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators.html#listcustomverificationemailtemplatespaginator)
        """

class ListIdentitiesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ses.html#SES.Paginator.ListIdentities)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators.html#listidentitiespaginator)
    """

    def paginate(
        self,
        *,
        IdentityType: IdentityTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIdentitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ses.html#SES.Paginator.ListIdentities.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators.html#listidentitiespaginator)
        """

class ListReceiptRuleSetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ses.html#SES.Paginator.ListReceiptRuleSets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators.html#listreceiptrulesetspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListReceiptRuleSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ses.html#SES.Paginator.ListReceiptRuleSets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators.html#listreceiptrulesetspaginator)
        """

class ListTemplatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ses.html#SES.Paginator.ListTemplates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators.html#listtemplatespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ses.html#SES.Paginator.ListTemplates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators.html#listtemplatespaginator)
        """
