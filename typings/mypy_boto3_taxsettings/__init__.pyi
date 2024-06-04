"""
Main interface for taxsettings service.

Usage::

    ```python
    import boto3
    from mypy_boto3_taxsettings import (
        Client,
        ListTaxRegistrationsPaginator,
        TaxSettingsClient,
    )

    session = boto3.Session()

    client: TaxSettingsClient = boto3.client("taxsettings")
    session_client: TaxSettingsClient = session.client("taxsettings")

    list_tax_registrations_paginator: ListTaxRegistrationsPaginator = client.get_paginator("list_tax_registrations")
    ```
"""

from .client import TaxSettingsClient
from .paginator import ListTaxRegistrationsPaginator

Client = TaxSettingsClient

__all__ = ("Client", "ListTaxRegistrationsPaginator", "TaxSettingsClient")
