"""
Main interface for ses service.

Usage::

    ```python
    import boto3
    from mypy_boto3_ses import (
        Client,
        IdentityExistsWaiter,
        ListConfigurationSetsPaginator,
        ListCustomVerificationEmailTemplatesPaginator,
        ListIdentitiesPaginator,
        ListReceiptRuleSetsPaginator,
        ListTemplatesPaginator,
        SESClient,
    )

    session = boto3.Session()

    client: SESClient = boto3.client("ses")
    session_client: SESClient = session.client("ses")

    identity_exists_waiter: IdentityExistsWaiter = client.get_waiter("identity_exists")

    list_configuration_sets_paginator: ListConfigurationSetsPaginator = client.get_paginator("list_configuration_sets")
    list_custom_verification_email_templates_paginator: ListCustomVerificationEmailTemplatesPaginator = client.get_paginator("list_custom_verification_email_templates")
    list_identities_paginator: ListIdentitiesPaginator = client.get_paginator("list_identities")
    list_receipt_rule_sets_paginator: ListReceiptRuleSetsPaginator = client.get_paginator("list_receipt_rule_sets")
    list_templates_paginator: ListTemplatesPaginator = client.get_paginator("list_templates")
    ```
"""
from mypy_boto3_ses.client import SESClient
from mypy_boto3_ses.paginator import (
    ListConfigurationSetsPaginator,
    ListCustomVerificationEmailTemplatesPaginator,
    ListIdentitiesPaginator,
    ListReceiptRuleSetsPaginator,
    ListTemplatesPaginator,
)
from mypy_boto3_ses.waiter import IdentityExistsWaiter

Client = SESClient


__all__ = (
    "Client",
    "IdentityExistsWaiter",
    "ListConfigurationSetsPaginator",
    "ListCustomVerificationEmailTemplatesPaginator",
    "ListIdentitiesPaginator",
    "ListReceiptRuleSetsPaginator",
    "ListTemplatesPaginator",
    "SESClient",
)
