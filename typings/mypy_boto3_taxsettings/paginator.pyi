"""
Type annotations for taxsettings service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_taxsettings import TaxSettingsClient
    from mypy_boto3_taxsettings.paginator import (
        ListTaxRegistrationsPaginator,
    )

    client: TaxSettingsClient = boto3.client("taxsettings")

    list_tax_registrations_paginator: ListTaxRegistrationsPaginator = client.get_paginator("list_tax_registrations")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import ListTaxRegistrationsResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListTaxRegistrationsPaginator",)

class ListTaxRegistrationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/taxsettings.html#TaxSettings.Paginator.ListTaxRegistrations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/paginators.html#listtaxregistrationspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTaxRegistrationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/taxsettings.html#TaxSettings.Paginator.ListTaxRegistrations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/paginators.html#listtaxregistrationspaginator)
        """
