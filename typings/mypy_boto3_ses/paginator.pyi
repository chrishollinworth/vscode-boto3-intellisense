# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for ses service client paginators.

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
import sys
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_ses.type_defs import (
    ListConfigurationSetsResponseTypeDef,
    ListCustomVerificationEmailTemplatesResponseTypeDef,
    ListIdentitiesResponseTypeDef,
    ListReceiptRuleSetsResponseTypeDef,
    ListTemplatesResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListConfigurationSetsPaginator",
    "ListCustomVerificationEmailTemplatesPaginator",
    "ListIdentitiesPaginator",
    "ListReceiptRuleSetsPaginator",
    "ListTemplatesPaginator",
)


class ListConfigurationSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListConfigurationSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ses.html#SES.Paginator.ListConfigurationSets)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConfigurationSetsResponseTypeDef]:
        """
        [ListConfigurationSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ses.html#SES.Paginator.ListConfigurationSets.paginate)
        """


class ListCustomVerificationEmailTemplatesPaginator(Boto3Paginator):
    """
    [Paginator.ListCustomVerificationEmailTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ses.html#SES.Paginator.ListCustomVerificationEmailTemplates)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCustomVerificationEmailTemplatesResponseTypeDef]:
        """
        [ListCustomVerificationEmailTemplates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ses.html#SES.Paginator.ListCustomVerificationEmailTemplates.paginate)
        """


class ListIdentitiesPaginator(Boto3Paginator):
    """
    [Paginator.ListIdentities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ses.html#SES.Paginator.ListIdentities)
    """

    def paginate(
        self,
        IdentityType: Literal["EmailAddress", "Domain"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListIdentitiesResponseTypeDef]:
        """
        [ListIdentities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ses.html#SES.Paginator.ListIdentities.paginate)
        """


class ListReceiptRuleSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListReceiptRuleSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ses.html#SES.Paginator.ListReceiptRuleSets)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListReceiptRuleSetsResponseTypeDef]:
        """
        [ListReceiptRuleSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ses.html#SES.Paginator.ListReceiptRuleSets.paginate)
        """


class ListTemplatesPaginator(Boto3Paginator):
    """
    [Paginator.ListTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ses.html#SES.Paginator.ListTemplates)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTemplatesResponseTypeDef]:
        """
        [ListTemplates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ses.html#SES.Paginator.ListTemplates.paginate)
        """
