"""
Main interface for taxsettings service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_taxsettings import (
        Client,
        ListSupplementalTaxRegistrationsPaginator,
        ListTaxExemptionsPaginator,
        ListTaxRegistrationsPaginator,
        TaxSettingsClient,
    )

    session = Session()
    client: TaxSettingsClient = session.client("taxsettings")

    list_supplemental_tax_registrations_paginator: ListSupplementalTaxRegistrationsPaginator = client.get_paginator("list_supplemental_tax_registrations")
    list_tax_exemptions_paginator: ListTaxExemptionsPaginator = client.get_paginator("list_tax_exemptions")
    list_tax_registrations_paginator: ListTaxRegistrationsPaginator = client.get_paginator("list_tax_registrations")
    ```
"""

from .client import TaxSettingsClient
from .paginator import (
    ListSupplementalTaxRegistrationsPaginator,
    ListTaxExemptionsPaginator,
    ListTaxRegistrationsPaginator,
)

Client = TaxSettingsClient

__all__ = (
    "Client",
    "ListSupplementalTaxRegistrationsPaginator",
    "ListTaxExemptionsPaginator",
    "ListTaxRegistrationsPaginator",
    "TaxSettingsClient",
)
