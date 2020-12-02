"""
Main interface for customer-profiles service type definitions.

Usage::

    ```python
    from mypy_boto3_customer_profiles.type_defs import AddressTypeDef

    data: AddressTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddressTypeDef",
    "DomainStatsTypeDef",
    "ListDomainItemTypeDef",
    "ListIntegrationItemTypeDef",
    "ListProfileObjectTypeItemTypeDef",
    "ListProfileObjectTypeTemplateItemTypeDef",
    "ListProfileObjectsItemTypeDef",
    "ObjectTypeFieldTypeDef",
    "ObjectTypeKeyTypeDef",
    "ProfileTypeDef",
    "AddProfileKeyResponseTypeDef",
    "CreateDomainResponseTypeDef",
    "CreateProfileResponseTypeDef",
    "DeleteDomainResponseTypeDef",
    "DeleteIntegrationResponseTypeDef",
    "DeleteProfileKeyResponseTypeDef",
    "DeleteProfileObjectResponseTypeDef",
    "DeleteProfileObjectTypeResponseTypeDef",
    "DeleteProfileResponseTypeDef",
    "GetDomainResponseTypeDef",
    "GetIntegrationResponseTypeDef",
    "GetProfileObjectTypeResponseTypeDef",
    "GetProfileObjectTypeTemplateResponseTypeDef",
    "ListAccountIntegrationsResponseTypeDef",
    "ListDomainsResponseTypeDef",
    "ListIntegrationsResponseTypeDef",
    "ListProfileObjectTypeTemplatesResponseTypeDef",
    "ListProfileObjectTypesResponseTypeDef",
    "ListProfileObjectsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutIntegrationResponseTypeDef",
    "PutProfileObjectResponseTypeDef",
    "PutProfileObjectTypeResponseTypeDef",
    "SearchProfilesResponseTypeDef",
    "UpdateAddressTypeDef",
    "UpdateDomainResponseTypeDef",
    "UpdateProfileResponseTypeDef",
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "Address1": str,
        "Address2": str,
        "Address3": str,
        "Address4": str,
        "City": str,
        "County": str,
        "State": str,
        "Province": str,
        "Country": str,
        "PostalCode": str,
    },
    total=False,
)

DomainStatsTypeDef = TypedDict(
    "DomainStatsTypeDef",
    {"ProfileCount": int, "MeteringProfileCount": int, "ObjectCount": int, "TotalSize": int},
    total=False,
)

_RequiredListDomainItemTypeDef = TypedDict(
    "_RequiredListDomainItemTypeDef",
    {"DomainName": str, "CreatedAt": datetime, "LastUpdatedAt": datetime},
)
_OptionalListDomainItemTypeDef = TypedDict(
    "_OptionalListDomainItemTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ListDomainItemTypeDef(_RequiredListDomainItemTypeDef, _OptionalListDomainItemTypeDef):
    pass


_RequiredListIntegrationItemTypeDef = TypedDict(
    "_RequiredListIntegrationItemTypeDef",
    {
        "DomainName": str,
        "Uri": str,
        "ObjectTypeName": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
)
_OptionalListIntegrationItemTypeDef = TypedDict(
    "_OptionalListIntegrationItemTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ListIntegrationItemTypeDef(
    _RequiredListIntegrationItemTypeDef, _OptionalListIntegrationItemTypeDef
):
    pass


_RequiredListProfileObjectTypeItemTypeDef = TypedDict(
    "_RequiredListProfileObjectTypeItemTypeDef", {"ObjectTypeName": str, "Description": str}
)
_OptionalListProfileObjectTypeItemTypeDef = TypedDict(
    "_OptionalListProfileObjectTypeItemTypeDef",
    {"CreatedAt": datetime, "LastUpdatedAt": datetime, "Tags": Dict[str, str]},
    total=False,
)


class ListProfileObjectTypeItemTypeDef(
    _RequiredListProfileObjectTypeItemTypeDef, _OptionalListProfileObjectTypeItemTypeDef
):
    pass


ListProfileObjectTypeTemplateItemTypeDef = TypedDict(
    "ListProfileObjectTypeTemplateItemTypeDef",
    {"TemplateId": str, "SourceName": str, "SourceObject": str},
    total=False,
)

ListProfileObjectsItemTypeDef = TypedDict(
    "ListProfileObjectsItemTypeDef",
    {"ObjectTypeName": str, "ProfileObjectUniqueKey": str, "Object": str},
    total=False,
)

ObjectTypeFieldTypeDef = TypedDict(
    "ObjectTypeFieldTypeDef",
    {
        "Source": str,
        "Target": str,
        "ContentType": Literal["STRING", "NUMBER", "PHONE_NUMBER", "EMAIL_ADDRESS", "NAME"],
    },
    total=False,
)

ObjectTypeKeyTypeDef = TypedDict(
    "ObjectTypeKeyTypeDef",
    {
        "StandardIdentifiers": List[
            Literal["PROFILE", "UNIQUE", "SECONDARY", "LOOKUP_ONLY", "NEW_ONLY"]
        ],
        "FieldNames": List[str],
    },
    total=False,
)

ProfileTypeDef = TypedDict(
    "ProfileTypeDef",
    {
        "ProfileId": str,
        "AccountNumber": str,
        "AdditionalInformation": str,
        "PartyType": Literal["INDIVIDUAL", "BUSINESS", "OTHER"],
        "BusinessName": str,
        "FirstName": str,
        "MiddleName": str,
        "LastName": str,
        "BirthDate": str,
        "Gender": Literal["MALE", "FEMALE", "UNSPECIFIED"],
        "PhoneNumber": str,
        "MobilePhoneNumber": str,
        "HomePhoneNumber": str,
        "BusinessPhoneNumber": str,
        "EmailAddress": str,
        "PersonalEmailAddress": str,
        "BusinessEmailAddress": str,
        "Address": "AddressTypeDef",
        "ShippingAddress": "AddressTypeDef",
        "MailingAddress": "AddressTypeDef",
        "BillingAddress": "AddressTypeDef",
        "Attributes": Dict[str, str],
    },
    total=False,
)

AddProfileKeyResponseTypeDef = TypedDict(
    "AddProfileKeyResponseTypeDef", {"KeyName": str, "Values": List[str]}, total=False
)

_RequiredCreateDomainResponseTypeDef = TypedDict(
    "_RequiredCreateDomainResponseTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": int,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
)
_OptionalCreateDomainResponseTypeDef = TypedDict(
    "_OptionalCreateDomainResponseTypeDef",
    {"DefaultEncryptionKey": str, "DeadLetterQueueUrl": str, "Tags": Dict[str, str]},
    total=False,
)


class CreateDomainResponseTypeDef(
    _RequiredCreateDomainResponseTypeDef, _OptionalCreateDomainResponseTypeDef
):
    pass


CreateProfileResponseTypeDef = TypedDict("CreateProfileResponseTypeDef", {"ProfileId": str})

DeleteDomainResponseTypeDef = TypedDict("DeleteDomainResponseTypeDef", {"Message": str})

DeleteIntegrationResponseTypeDef = TypedDict("DeleteIntegrationResponseTypeDef", {"Message": str})

DeleteProfileKeyResponseTypeDef = TypedDict(
    "DeleteProfileKeyResponseTypeDef", {"Message": str}, total=False
)

DeleteProfileObjectResponseTypeDef = TypedDict(
    "DeleteProfileObjectResponseTypeDef", {"Message": str}, total=False
)

DeleteProfileObjectTypeResponseTypeDef = TypedDict(
    "DeleteProfileObjectTypeResponseTypeDef", {"Message": str}
)

DeleteProfileResponseTypeDef = TypedDict(
    "DeleteProfileResponseTypeDef", {"Message": str}, total=False
)

_RequiredGetDomainResponseTypeDef = TypedDict(
    "_RequiredGetDomainResponseTypeDef",
    {"DomainName": str, "CreatedAt": datetime, "LastUpdatedAt": datetime},
)
_OptionalGetDomainResponseTypeDef = TypedDict(
    "_OptionalGetDomainResponseTypeDef",
    {
        "DefaultExpirationDays": int,
        "DefaultEncryptionKey": str,
        "DeadLetterQueueUrl": str,
        "Stats": "DomainStatsTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)


class GetDomainResponseTypeDef(
    _RequiredGetDomainResponseTypeDef, _OptionalGetDomainResponseTypeDef
):
    pass


_RequiredGetIntegrationResponseTypeDef = TypedDict(
    "_RequiredGetIntegrationResponseTypeDef",
    {
        "DomainName": str,
        "Uri": str,
        "ObjectTypeName": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
)
_OptionalGetIntegrationResponseTypeDef = TypedDict(
    "_OptionalGetIntegrationResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class GetIntegrationResponseTypeDef(
    _RequiredGetIntegrationResponseTypeDef, _OptionalGetIntegrationResponseTypeDef
):
    pass


_RequiredGetProfileObjectTypeResponseTypeDef = TypedDict(
    "_RequiredGetProfileObjectTypeResponseTypeDef", {"ObjectTypeName": str, "Description": str}
)
_OptionalGetProfileObjectTypeResponseTypeDef = TypedDict(
    "_OptionalGetProfileObjectTypeResponseTypeDef",
    {
        "TemplateId": str,
        "ExpirationDays": int,
        "EncryptionKey": str,
        "AllowProfileCreation": bool,
        "Fields": Dict[str, "ObjectTypeFieldTypeDef"],
        "Keys": Dict[str, List["ObjectTypeKeyTypeDef"]],
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
    },
    total=False,
)


class GetProfileObjectTypeResponseTypeDef(
    _RequiredGetProfileObjectTypeResponseTypeDef, _OptionalGetProfileObjectTypeResponseTypeDef
):
    pass


GetProfileObjectTypeTemplateResponseTypeDef = TypedDict(
    "GetProfileObjectTypeTemplateResponseTypeDef",
    {
        "TemplateId": str,
        "SourceName": str,
        "SourceObject": str,
        "AllowProfileCreation": bool,
        "Fields": Dict[str, "ObjectTypeFieldTypeDef"],
        "Keys": Dict[str, List["ObjectTypeKeyTypeDef"]],
    },
    total=False,
)

ListAccountIntegrationsResponseTypeDef = TypedDict(
    "ListAccountIntegrationsResponseTypeDef",
    {"Items": List["ListIntegrationItemTypeDef"], "NextToken": str},
    total=False,
)

ListDomainsResponseTypeDef = TypedDict(
    "ListDomainsResponseTypeDef",
    {"Items": List["ListDomainItemTypeDef"], "NextToken": str},
    total=False,
)

ListIntegrationsResponseTypeDef = TypedDict(
    "ListIntegrationsResponseTypeDef",
    {"Items": List["ListIntegrationItemTypeDef"], "NextToken": str},
    total=False,
)

ListProfileObjectTypeTemplatesResponseTypeDef = TypedDict(
    "ListProfileObjectTypeTemplatesResponseTypeDef",
    {"Items": List["ListProfileObjectTypeTemplateItemTypeDef"], "NextToken": str},
    total=False,
)

ListProfileObjectTypesResponseTypeDef = TypedDict(
    "ListProfileObjectTypesResponseTypeDef",
    {"Items": List["ListProfileObjectTypeItemTypeDef"], "NextToken": str},
    total=False,
)

ListProfileObjectsResponseTypeDef = TypedDict(
    "ListProfileObjectsResponseTypeDef",
    {"Items": List["ListProfileObjectsItemTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

_RequiredPutIntegrationResponseTypeDef = TypedDict(
    "_RequiredPutIntegrationResponseTypeDef",
    {
        "DomainName": str,
        "Uri": str,
        "ObjectTypeName": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
)
_OptionalPutIntegrationResponseTypeDef = TypedDict(
    "_OptionalPutIntegrationResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class PutIntegrationResponseTypeDef(
    _RequiredPutIntegrationResponseTypeDef, _OptionalPutIntegrationResponseTypeDef
):
    pass


PutProfileObjectResponseTypeDef = TypedDict(
    "PutProfileObjectResponseTypeDef", {"ProfileObjectUniqueKey": str}, total=False
)

_RequiredPutProfileObjectTypeResponseTypeDef = TypedDict(
    "_RequiredPutProfileObjectTypeResponseTypeDef", {"ObjectTypeName": str, "Description": str}
)
_OptionalPutProfileObjectTypeResponseTypeDef = TypedDict(
    "_OptionalPutProfileObjectTypeResponseTypeDef",
    {
        "TemplateId": str,
        "ExpirationDays": int,
        "EncryptionKey": str,
        "AllowProfileCreation": bool,
        "Fields": Dict[str, "ObjectTypeFieldTypeDef"],
        "Keys": Dict[str, List["ObjectTypeKeyTypeDef"]],
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
    },
    total=False,
)


class PutProfileObjectTypeResponseTypeDef(
    _RequiredPutProfileObjectTypeResponseTypeDef, _OptionalPutProfileObjectTypeResponseTypeDef
):
    pass


SearchProfilesResponseTypeDef = TypedDict(
    "SearchProfilesResponseTypeDef",
    {"Items": List["ProfileTypeDef"], "NextToken": str},
    total=False,
)

UpdateAddressTypeDef = TypedDict(
    "UpdateAddressTypeDef",
    {
        "Address1": str,
        "Address2": str,
        "Address3": str,
        "Address4": str,
        "City": str,
        "County": str,
        "State": str,
        "Province": str,
        "Country": str,
        "PostalCode": str,
    },
    total=False,
)

_RequiredUpdateDomainResponseTypeDef = TypedDict(
    "_RequiredUpdateDomainResponseTypeDef",
    {"DomainName": str, "CreatedAt": datetime, "LastUpdatedAt": datetime},
)
_OptionalUpdateDomainResponseTypeDef = TypedDict(
    "_OptionalUpdateDomainResponseTypeDef",
    {
        "DefaultExpirationDays": int,
        "DefaultEncryptionKey": str,
        "DeadLetterQueueUrl": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class UpdateDomainResponseTypeDef(
    _RequiredUpdateDomainResponseTypeDef, _OptionalUpdateDomainResponseTypeDef
):
    pass


UpdateProfileResponseTypeDef = TypedDict("UpdateProfileResponseTypeDef", {"ProfileId": str})
