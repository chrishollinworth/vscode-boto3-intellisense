"""
Type annotations for taxsettings service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/literals.html)

Usage::

    ```python
    from mypy_boto3_taxsettings.literals import AddressRoleTypeType

    data: AddressRoleTypeType = "BillingAddress"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AddressRoleTypeType",
    "IndustriesType",
    "IsraelCustomerTypeType",
    "IsraelDealerTypeType",
    "ListTaxRegistrationsPaginatorName",
    "MalaysiaServiceTaxCodeType",
    "PersonTypeType",
    "RegistrationTypeType",
    "SaudiArabiaTaxRegistrationNumberTypeType",
    "SectorType",
    "TaxRegistrationNumberTypeType",
    "TaxRegistrationStatusType",
    "TaxRegistrationTypeType",
    "UkraineTrnTypeType",
)

AddressRoleTypeType = Literal["BillingAddress", "ContactAddress", "TaxAddress"]
IndustriesType = Literal[
    "Banks",
    "CirculatingOrg",
    "DevelopmentAgencies",
    "Insurance",
    "PensionAndBenefitFunds",
    "ProfessionalOrg",
]
IsraelCustomerTypeType = Literal["Business", "Individual"]
IsraelDealerTypeType = Literal["Authorized", "Non-authorized"]
ListTaxRegistrationsPaginatorName = Literal["list_tax_registrations"]
MalaysiaServiceTaxCodeType = Literal[
    "Consultancy", "Digital Service And Electronic Medium", "IT Services", "Training Or Coaching"
]
PersonTypeType = Literal["Business", "Legal Person", "Physical Person"]
RegistrationTypeType = Literal["Intra-EU", "Local"]
SaudiArabiaTaxRegistrationNumberTypeType = Literal[
    "CommercialRegistrationNumber", "TaxIdentificationNumber", "TaxRegistrationNumber"
]
SectorType = Literal["Business", "Government", "Individual"]
TaxRegistrationNumberTypeType = Literal["LocalRegistrationNumber", "TaxRegistrationNumber"]
TaxRegistrationStatusType = Literal["Deleted", "Pending", "Rejected", "Verified"]
TaxRegistrationTypeType = Literal["CNPJ", "CPF", "GST", "SST", "VAT"]
UkraineTrnTypeType = Literal["Business", "Individual"]
