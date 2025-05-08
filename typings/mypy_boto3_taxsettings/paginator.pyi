"""
Type annotations for taxsettings service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_taxsettings.client import TaxSettingsClient
    from mypy_boto3_taxsettings.paginator import (
        ListSupplementalTaxRegistrationsPaginator,
        ListTaxExemptionsPaginator,
        ListTaxRegistrationsPaginator,
    )

    session = Session()
    client: TaxSettingsClient = session.client("taxsettings")

    list_supplemental_tax_registrations_paginator: ListSupplementalTaxRegistrationsPaginator = client.get_paginator("list_supplemental_tax_registrations")
    list_tax_exemptions_paginator: ListTaxExemptionsPaginator = client.get_paginator("list_tax_exemptions")
    list_tax_registrations_paginator: ListTaxRegistrationsPaginator = client.get_paginator("list_tax_registrations")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListSupplementalTaxRegistrationsRequestPaginateTypeDef,
    ListSupplementalTaxRegistrationsResponseTypeDef,
    ListTaxExemptionsRequestPaginateTypeDef,
    ListTaxExemptionsResponseTypeDef,
    ListTaxRegistrationsRequestPaginateTypeDef,
    ListTaxRegistrationsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListSupplementalTaxRegistrationsPaginator",
    "ListTaxExemptionsPaginator",
    "ListTaxRegistrationsPaginator",
)

if TYPE_CHECKING:
    _ListSupplementalTaxRegistrationsPaginatorBase = Paginator[
        ListSupplementalTaxRegistrationsResponseTypeDef
    ]
else:
    _ListSupplementalTaxRegistrationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSupplementalTaxRegistrationsPaginator(_ListSupplementalTaxRegistrationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/paginator/ListSupplementalTaxRegistrations.html#TaxSettings.Paginator.ListSupplementalTaxRegistrations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/paginators/#listsupplementaltaxregistrationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSupplementalTaxRegistrationsRequestPaginateTypeDef]
    ) -> PageIterator[ListSupplementalTaxRegistrationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/paginator/ListSupplementalTaxRegistrations.html#TaxSettings.Paginator.ListSupplementalTaxRegistrations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/paginators/#listsupplementaltaxregistrationspaginator)
        """

if TYPE_CHECKING:
    _ListTaxExemptionsPaginatorBase = Paginator[ListTaxExemptionsResponseTypeDef]
else:
    _ListTaxExemptionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTaxExemptionsPaginator(_ListTaxExemptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/paginator/ListTaxExemptions.html#TaxSettings.Paginator.ListTaxExemptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/paginators/#listtaxexemptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTaxExemptionsRequestPaginateTypeDef]
    ) -> PageIterator[ListTaxExemptionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/paginator/ListTaxExemptions.html#TaxSettings.Paginator.ListTaxExemptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/paginators/#listtaxexemptionspaginator)
        """

if TYPE_CHECKING:
    _ListTaxRegistrationsPaginatorBase = Paginator[ListTaxRegistrationsResponseTypeDef]
else:
    _ListTaxRegistrationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTaxRegistrationsPaginator(_ListTaxRegistrationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/paginator/ListTaxRegistrations.html#TaxSettings.Paginator.ListTaxRegistrations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/paginators/#listtaxregistrationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTaxRegistrationsRequestPaginateTypeDef]
    ) -> PageIterator[ListTaxRegistrationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings/paginator/ListTaxRegistrations.html#TaxSettings.Paginator.ListTaxRegistrations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/paginators/#listtaxregistrationspaginator)
        """
