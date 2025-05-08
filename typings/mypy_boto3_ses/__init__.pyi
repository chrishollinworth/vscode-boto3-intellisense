"""
Main interface for ses service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ses/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
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

    session = Session()
    client: SESClient = session.client("ses")

    identity_exists_waiter: IdentityExistsWaiter = client.get_waiter("identity_exists")

    list_configuration_sets_paginator: ListConfigurationSetsPaginator = client.get_paginator("list_configuration_sets")
    list_custom_verification_email_templates_paginator: ListCustomVerificationEmailTemplatesPaginator = client.get_paginator("list_custom_verification_email_templates")
    list_identities_paginator: ListIdentitiesPaginator = client.get_paginator("list_identities")
    list_receipt_rule_sets_paginator: ListReceiptRuleSetsPaginator = client.get_paginator("list_receipt_rule_sets")
    list_templates_paginator: ListTemplatesPaginator = client.get_paginator("list_templates")
    ```
"""

from .client import SESClient
from .paginator import (
    ListConfigurationSetsPaginator,
    ListCustomVerificationEmailTemplatesPaginator,
    ListIdentitiesPaginator,
    ListReceiptRuleSetsPaginator,
    ListTemplatesPaginator,
)
from .waiter import IdentityExistsWaiter

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
