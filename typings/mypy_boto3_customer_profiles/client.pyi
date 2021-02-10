"""
Main interface for customer-profiles service client

Usage::

    ```python
    import boto3
    from mypy_boto3_customer_profiles import CustomerProfilesClient

    client: CustomerProfilesClient = boto3.client("customer-profiles")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_customer_profiles.type_defs import (
    AddProfileKeyResponseTypeDef,
    AddressTypeDef,
    CreateDomainResponseTypeDef,
    CreateProfileResponseTypeDef,
    DeleteDomainResponseTypeDef,
    DeleteIntegrationResponseTypeDef,
    DeleteProfileKeyResponseTypeDef,
    DeleteProfileObjectResponseTypeDef,
    DeleteProfileObjectTypeResponseTypeDef,
    DeleteProfileResponseTypeDef,
    GetDomainResponseTypeDef,
    GetIntegrationResponseTypeDef,
    GetProfileObjectTypeResponseTypeDef,
    GetProfileObjectTypeTemplateResponseTypeDef,
    ListAccountIntegrationsResponseTypeDef,
    ListDomainsResponseTypeDef,
    ListIntegrationsResponseTypeDef,
    ListProfileObjectsResponseTypeDef,
    ListProfileObjectTypesResponseTypeDef,
    ListProfileObjectTypeTemplatesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ObjectTypeFieldTypeDef,
    ObjectTypeKeyTypeDef,
    PutIntegrationResponseTypeDef,
    PutProfileObjectResponseTypeDef,
    PutProfileObjectTypeResponseTypeDef,
    SearchProfilesResponseTypeDef,
    UpdateAddressTypeDef,
    UpdateDomainResponseTypeDef,
    UpdateProfileResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CustomerProfilesClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]


class CustomerProfilesClient:
    """
    [CustomerProfiles.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_profile_key(
        self, ProfileId: str, KeyName: str, Values: List[str], DomainName: str
    ) -> AddProfileKeyResponseTypeDef:
        """
        [Client.add_profile_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.add_profile_key)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.can_paginate)
        """

    def create_domain(
        self,
        DomainName: str,
        DefaultExpirationDays: int,
        DefaultEncryptionKey: str = None,
        DeadLetterQueueUrl: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateDomainResponseTypeDef:
        """
        [Client.create_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.create_domain)
        """

    def create_profile(
        self,
        DomainName: str,
        AccountNumber: str = None,
        AdditionalInformation: str = None,
        PartyType: Literal["INDIVIDUAL", "BUSINESS", "OTHER"] = None,
        BusinessName: str = None,
        FirstName: str = None,
        MiddleName: str = None,
        LastName: str = None,
        BirthDate: str = None,
        Gender: Literal["MALE", "FEMALE", "UNSPECIFIED"] = None,
        PhoneNumber: str = None,
        MobilePhoneNumber: str = None,
        HomePhoneNumber: str = None,
        BusinessPhoneNumber: str = None,
        EmailAddress: str = None,
        PersonalEmailAddress: str = None,
        BusinessEmailAddress: str = None,
        Address: "AddressTypeDef" = None,
        ShippingAddress: "AddressTypeDef" = None,
        MailingAddress: "AddressTypeDef" = None,
        BillingAddress: "AddressTypeDef" = None,
        Attributes: Dict[str, str] = None,
    ) -> CreateProfileResponseTypeDef:
        """
        [Client.create_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.create_profile)
        """

    def delete_domain(self, DomainName: str) -> DeleteDomainResponseTypeDef:
        """
        [Client.delete_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_domain)
        """

    def delete_integration(self, DomainName: str, Uri: str) -> DeleteIntegrationResponseTypeDef:
        """
        [Client.delete_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_integration)
        """

    def delete_profile(self, ProfileId: str, DomainName: str) -> DeleteProfileResponseTypeDef:
        """
        [Client.delete_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_profile)
        """

    def delete_profile_key(
        self, ProfileId: str, KeyName: str, Values: List[str], DomainName: str
    ) -> DeleteProfileKeyResponseTypeDef:
        """
        [Client.delete_profile_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_profile_key)
        """

    def delete_profile_object(
        self, ProfileId: str, ProfileObjectUniqueKey: str, ObjectTypeName: str, DomainName: str
    ) -> DeleteProfileObjectResponseTypeDef:
        """
        [Client.delete_profile_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_profile_object)
        """

    def delete_profile_object_type(
        self, DomainName: str, ObjectTypeName: str
    ) -> DeleteProfileObjectTypeResponseTypeDef:
        """
        [Client.delete_profile_object_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_profile_object_type)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.generate_presigned_url)
        """

    def get_domain(self, DomainName: str) -> GetDomainResponseTypeDef:
        """
        [Client.get_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.get_domain)
        """

    def get_integration(self, DomainName: str, Uri: str) -> GetIntegrationResponseTypeDef:
        """
        [Client.get_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.get_integration)
        """

    def get_profile_object_type(
        self, DomainName: str, ObjectTypeName: str
    ) -> GetProfileObjectTypeResponseTypeDef:
        """
        [Client.get_profile_object_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.get_profile_object_type)
        """

    def get_profile_object_type_template(
        self, TemplateId: str
    ) -> GetProfileObjectTypeTemplateResponseTypeDef:
        """
        [Client.get_profile_object_type_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.get_profile_object_type_template)
        """

    def list_account_integrations(
        self, Uri: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAccountIntegrationsResponseTypeDef:
        """
        [Client.list_account_integrations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.list_account_integrations)
        """

    def list_domains(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListDomainsResponseTypeDef:
        """
        [Client.list_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.list_domains)
        """

    def list_integrations(
        self, DomainName: str, NextToken: str = None, MaxResults: int = None
    ) -> ListIntegrationsResponseTypeDef:
        """
        [Client.list_integrations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.list_integrations)
        """

    def list_profile_object_type_templates(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListProfileObjectTypeTemplatesResponseTypeDef:
        """
        [Client.list_profile_object_type_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.list_profile_object_type_templates)
        """

    def list_profile_object_types(
        self, DomainName: str, NextToken: str = None, MaxResults: int = None
    ) -> ListProfileObjectTypesResponseTypeDef:
        """
        [Client.list_profile_object_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.list_profile_object_types)
        """

    def list_profile_objects(
        self,
        DomainName: str,
        ObjectTypeName: str,
        ProfileId: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListProfileObjectsResponseTypeDef:
        """
        [Client.list_profile_objects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.list_profile_objects)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.list_tags_for_resource)
        """

    def put_integration(
        self, DomainName: str, Uri: str, ObjectTypeName: str, Tags: Dict[str, str] = None
    ) -> PutIntegrationResponseTypeDef:
        """
        [Client.put_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.put_integration)
        """

    def put_profile_object(
        self, ObjectTypeName: str, Object: str, DomainName: str
    ) -> PutProfileObjectResponseTypeDef:
        """
        [Client.put_profile_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.put_profile_object)
        """

    def put_profile_object_type(
        self,
        DomainName: str,
        ObjectTypeName: str,
        Description: str,
        TemplateId: str = None,
        ExpirationDays: int = None,
        EncryptionKey: str = None,
        AllowProfileCreation: bool = None,
        Fields: Dict[str, "ObjectTypeFieldTypeDef"] = None,
        Keys: Dict[str, List["ObjectTypeKeyTypeDef"]] = None,
        Tags: Dict[str, str] = None,
    ) -> PutProfileObjectTypeResponseTypeDef:
        """
        [Client.put_profile_object_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.put_profile_object_type)
        """

    def search_profiles(
        self,
        DomainName: str,
        KeyName: str,
        Values: List[str],
        NextToken: str = None,
        MaxResults: int = None,
    ) -> SearchProfilesResponseTypeDef:
        """
        [Client.search_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.search_profiles)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.untag_resource)
        """

    def update_domain(
        self,
        DomainName: str,
        DefaultExpirationDays: int = None,
        DefaultEncryptionKey: str = None,
        DeadLetterQueueUrl: str = None,
        Tags: Dict[str, str] = None,
    ) -> UpdateDomainResponseTypeDef:
        """
        [Client.update_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.update_domain)
        """

    def update_profile(
        self,
        DomainName: str,
        ProfileId: str,
        AdditionalInformation: str = None,
        AccountNumber: str = None,
        PartyType: Literal["INDIVIDUAL", "BUSINESS", "OTHER"] = None,
        BusinessName: str = None,
        FirstName: str = None,
        MiddleName: str = None,
        LastName: str = None,
        BirthDate: str = None,
        Gender: Literal["MALE", "FEMALE", "UNSPECIFIED"] = None,
        PhoneNumber: str = None,
        MobilePhoneNumber: str = None,
        HomePhoneNumber: str = None,
        BusinessPhoneNumber: str = None,
        EmailAddress: str = None,
        PersonalEmailAddress: str = None,
        BusinessEmailAddress: str = None,
        Address: UpdateAddressTypeDef = None,
        ShippingAddress: UpdateAddressTypeDef = None,
        MailingAddress: UpdateAddressTypeDef = None,
        BillingAddress: UpdateAddressTypeDef = None,
        Attributes: Dict[str, str] = None,
    ) -> UpdateProfileResponseTypeDef:
        """
        [Client.update_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/customer-profiles.html#CustomerProfiles.Client.update_profile)
        """
