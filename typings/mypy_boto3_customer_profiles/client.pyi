"""
Type annotations for customer-profiles service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_customer_profiles import CustomerProfilesClient

    client: CustomerProfilesClient = boto3.client("customer-profiles")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta

from .literals import GenderType, PartyTypeType, StatusType
from .type_defs import (
    AddProfileKeyResponseTypeDef,
    AddressTypeDef,
    ConflictResolutionTypeDef,
    ConsolidationTypeDef,
    CreateDomainResponseTypeDef,
    CreateIntegrationWorkflowResponseTypeDef,
    CreateProfileResponseTypeDef,
    DeleteDomainResponseTypeDef,
    DeleteIntegrationResponseTypeDef,
    DeleteProfileKeyResponseTypeDef,
    DeleteProfileObjectResponseTypeDef,
    DeleteProfileObjectTypeResponseTypeDef,
    DeleteProfileResponseTypeDef,
    FieldSourceProfileIdsTypeDef,
    FlowDefinitionTypeDef,
    GetAutoMergingPreviewResponseTypeDef,
    GetDomainResponseTypeDef,
    GetIdentityResolutionJobResponseTypeDef,
    GetIntegrationResponseTypeDef,
    GetMatchesResponseTypeDef,
    GetProfileObjectTypeResponseTypeDef,
    GetProfileObjectTypeTemplateResponseTypeDef,
    GetWorkflowResponseTypeDef,
    GetWorkflowStepsResponseTypeDef,
    IntegrationConfigTypeDef,
    ListAccountIntegrationsResponseTypeDef,
    ListDomainsResponseTypeDef,
    ListIdentityResolutionJobsResponseTypeDef,
    ListIntegrationsResponseTypeDef,
    ListProfileObjectsResponseTypeDef,
    ListProfileObjectTypesResponseTypeDef,
    ListProfileObjectTypeTemplatesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWorkflowsResponseTypeDef,
    MatchingRequestTypeDef,
    MergeProfilesResponseTypeDef,
    ObjectFilterTypeDef,
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

class CustomerProfilesClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CustomerProfilesClient exceptions.
        """
    def add_profile_key(
        self, *, ProfileId: str, KeyName: str, Values: List[str], DomainName: str
    ) -> AddProfileKeyResponseTypeDef:
        """
        Associates a new key value with a specific profile, such as a Contact Trace
        Record (CTR) ContactId.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.add_profile_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#add_profile_key)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#close)
        """
    def create_domain(
        self,
        *,
        DomainName: str,
        DefaultExpirationDays: int,
        DefaultEncryptionKey: str = None,
        DeadLetterQueueUrl: str = None,
        Matching: "MatchingRequestTypeDef" = None,
        Tags: Dict[str, str] = None
    ) -> CreateDomainResponseTypeDef:
        """
        Creates a domain, which is a container for all customer data, such as customer
        profile attributes, object types, profile keys, and encryption keys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.create_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#create_domain)
        """
    def create_integration_workflow(
        self,
        *,
        DomainName: str,
        WorkflowType: Literal["APPFLOW_INTEGRATION"],
        IntegrationConfig: "IntegrationConfigTypeDef",
        ObjectTypeName: str,
        RoleArn: str,
        Tags: Dict[str, str] = None
    ) -> CreateIntegrationWorkflowResponseTypeDef:
        """
        Creates an integration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.create_integration_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#create_integration_workflow)
        """
    def create_profile(
        self,
        *,
        DomainName: str,
        AccountNumber: str = None,
        AdditionalInformation: str = None,
        PartyType: PartyTypeType = None,
        BusinessName: str = None,
        FirstName: str = None,
        MiddleName: str = None,
        LastName: str = None,
        BirthDate: str = None,
        Gender: GenderType = None,
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
        Attributes: Dict[str, str] = None
    ) -> CreateProfileResponseTypeDef:
        """
        Creates a standard profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.create_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#create_profile)
        """
    def delete_domain(self, *, DomainName: str) -> DeleteDomainResponseTypeDef:
        """
        Deletes a specific domain and all of its customer data, such as customer profile
        attributes and their related objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#delete_domain)
        """
    def delete_integration(self, *, DomainName: str, Uri: str) -> DeleteIntegrationResponseTypeDef:
        """
        Removes an integration from a specific domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#delete_integration)
        """
    def delete_profile(self, *, ProfileId: str, DomainName: str) -> DeleteProfileResponseTypeDef:
        """
        Deletes the standard customer profile and all data pertaining to the profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#delete_profile)
        """
    def delete_profile_key(
        self, *, ProfileId: str, KeyName: str, Values: List[str], DomainName: str
    ) -> DeleteProfileKeyResponseTypeDef:
        """
        Removes a searchable key from a customer profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_profile_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#delete_profile_key)
        """
    def delete_profile_object(
        self, *, ProfileId: str, ProfileObjectUniqueKey: str, ObjectTypeName: str, DomainName: str
    ) -> DeleteProfileObjectResponseTypeDef:
        """
        Removes an object associated with a profile of a given ProfileObjectType.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_profile_object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#delete_profile_object)
        """
    def delete_profile_object_type(
        self, *, DomainName: str, ObjectTypeName: str
    ) -> DeleteProfileObjectTypeResponseTypeDef:
        """
        Removes a ProfileObjectType from a specific domain as well as removes all the
        ProfileObjects of that type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_profile_object_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#delete_profile_object_type)
        """
    def delete_workflow(self, *, DomainName: str, WorkflowId: str) -> Dict[str, Any]:
        """
        Deletes the specified workflow and all its corresponding resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#delete_workflow)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#generate_presigned_url)
        """
    def get_auto_merging_preview(
        self,
        *,
        DomainName: str,
        Consolidation: "ConsolidationTypeDef",
        ConflictResolution: "ConflictResolutionTypeDef",
        MinAllowedConfidenceScoreForMerging: float = None
    ) -> GetAutoMergingPreviewResponseTypeDef:
        """
        Tests the auto-merging settings of your Identity Resolution Job without merging
        your data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.get_auto_merging_preview)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#get_auto_merging_preview)
        """
    def get_domain(self, *, DomainName: str) -> GetDomainResponseTypeDef:
        """
        Returns information about a specific domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.get_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#get_domain)
        """
    def get_identity_resolution_job(
        self, *, DomainName: str, JobId: str
    ) -> GetIdentityResolutionJobResponseTypeDef:
        """
        Returns information about an Identity Resolution Job in a specific domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.get_identity_resolution_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#get_identity_resolution_job)
        """
    def get_integration(self, *, DomainName: str, Uri: str) -> GetIntegrationResponseTypeDef:
        """
        Returns an integration for a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.get_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#get_integration)
        """
    def get_matches(
        self, *, DomainName: str, NextToken: str = None, MaxResults: int = None
    ) -> GetMatchesResponseTypeDef:
        """
        Before calling this API, use `CreateDomain <https://docs.aws.amazon.com/customer
        profiles/latest/APIReference/API_CreateDomain.html>`__ or `UpdateDomain <https:/
        /docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateDomain.html>
        `__ to enable identity resolution: set `Matching` to tr...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.get_matches)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#get_matches)
        """
    def get_profile_object_type(
        self, *, DomainName: str, ObjectTypeName: str
    ) -> GetProfileObjectTypeResponseTypeDef:
        """
        Returns the object types for a specific domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.get_profile_object_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#get_profile_object_type)
        """
    def get_profile_object_type_template(
        self, *, TemplateId: str
    ) -> GetProfileObjectTypeTemplateResponseTypeDef:
        """
        Returns the template information for a specific object type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.get_profile_object_type_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#get_profile_object_type_template)
        """
    def get_workflow(self, *, DomainName: str, WorkflowId: str) -> GetWorkflowResponseTypeDef:
        """
        Get details of specified workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.get_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#get_workflow)
        """
    def get_workflow_steps(
        self, *, DomainName: str, WorkflowId: str, NextToken: str = None, MaxResults: int = None
    ) -> GetWorkflowStepsResponseTypeDef:
        """
        Get granular list of steps in workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.get_workflow_steps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#get_workflow_steps)
        """
    def list_account_integrations(
        self, *, Uri: str, NextToken: str = None, MaxResults: int = None, IncludeHidden: bool = None
    ) -> ListAccountIntegrationsResponseTypeDef:
        """
        Lists all of the integrations associated to a specific URI in the AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.list_account_integrations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#list_account_integrations)
        """
    def list_domains(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListDomainsResponseTypeDef:
        """
        Returns a list of all the domains for an AWS account that have been created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.list_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#list_domains)
        """
    def list_identity_resolution_jobs(
        self, *, DomainName: str, NextToken: str = None, MaxResults: int = None
    ) -> ListIdentityResolutionJobsResponseTypeDef:
        """
        Lists all of the Identity Resolution Jobs in your domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.list_identity_resolution_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#list_identity_resolution_jobs)
        """
    def list_integrations(
        self,
        *,
        DomainName: str,
        NextToken: str = None,
        MaxResults: int = None,
        IncludeHidden: bool = None
    ) -> ListIntegrationsResponseTypeDef:
        """
        Lists all of the integrations in your domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.list_integrations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#list_integrations)
        """
    def list_profile_object_type_templates(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListProfileObjectTypeTemplatesResponseTypeDef:
        """
        Lists all of the template information for object types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.list_profile_object_type_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#list_profile_object_type_templates)
        """
    def list_profile_object_types(
        self, *, DomainName: str, NextToken: str = None, MaxResults: int = None
    ) -> ListProfileObjectTypesResponseTypeDef:
        """
        Lists all of the templates available within the service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.list_profile_object_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#list_profile_object_types)
        """
    def list_profile_objects(
        self,
        *,
        DomainName: str,
        ObjectTypeName: str,
        ProfileId: str,
        NextToken: str = None,
        MaxResults: int = None,
        ObjectFilter: "ObjectFilterTypeDef" = None
    ) -> ListProfileObjectsResponseTypeDef:
        """
        Returns a list of objects associated with a profile of a given
        ProfileObjectType.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.list_profile_objects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#list_profile_objects)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Displays the tags associated with an Amazon Connect Customer Profiles resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#list_tags_for_resource)
        """
    def list_workflows(
        self,
        *,
        DomainName: str,
        WorkflowType: Literal["APPFLOW_INTEGRATION"] = None,
        Status: StatusType = None,
        QueryStartDate: Union[datetime, str] = None,
        QueryEndDate: Union[datetime, str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListWorkflowsResponseTypeDef:
        """
        Query to list all workflows.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.list_workflows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#list_workflows)
        """
    def merge_profiles(
        self,
        *,
        DomainName: str,
        MainProfileId: str,
        ProfileIdsToBeMerged: List[str],
        FieldSourceProfileIds: "FieldSourceProfileIdsTypeDef" = None
    ) -> MergeProfilesResponseTypeDef:
        """
        Runs an AWS Lambda job that does the following * All the profileKeys in the
        `ProfileToBeMerged` will be moved to the main profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.merge_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#merge_profiles)
        """
    def put_integration(
        self,
        *,
        DomainName: str,
        Uri: str = None,
        ObjectTypeName: str = None,
        Tags: Dict[str, str] = None,
        FlowDefinition: "FlowDefinitionTypeDef" = None,
        ObjectTypeNames: Dict[str, str] = None
    ) -> PutIntegrationResponseTypeDef:
        """
        Adds an integration between the service and a third-party service, which
        includes Amazon AppFlow and Amazon Connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.put_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#put_integration)
        """
    def put_profile_object(
        self, *, ObjectTypeName: str, Object: str, DomainName: str
    ) -> PutProfileObjectResponseTypeDef:
        """
        Adds additional objects to customer profiles of a given ObjectType.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.put_profile_object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#put_profile_object)
        """
    def put_profile_object_type(
        self,
        *,
        DomainName: str,
        ObjectTypeName: str,
        Description: str,
        TemplateId: str = None,
        ExpirationDays: int = None,
        EncryptionKey: str = None,
        AllowProfileCreation: bool = None,
        SourceLastUpdatedTimestampFormat: str = None,
        Fields: Dict[str, "ObjectTypeFieldTypeDef"] = None,
        Keys: Dict[str, List["ObjectTypeKeyTypeDef"]] = None,
        Tags: Dict[str, str] = None
    ) -> PutProfileObjectTypeResponseTypeDef:
        """
        Defines a ProfileObjectType.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.put_profile_object_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#put_profile_object_type)
        """
    def search_profiles(
        self,
        *,
        DomainName: str,
        KeyName: str,
        Values: List[str],
        NextToken: str = None,
        MaxResults: int = None
    ) -> SearchProfilesResponseTypeDef:
        """
        Searches for profiles within a specific domain name using name, phone number,
        email address, account number, or a custom defined index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.search_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#search_profiles)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified Amazon Connect
        Customer Profiles resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified Amazon Connect Customer Profiles
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#untag_resource)
        """
    def update_domain(
        self,
        *,
        DomainName: str,
        DefaultExpirationDays: int = None,
        DefaultEncryptionKey: str = None,
        DeadLetterQueueUrl: str = None,
        Matching: "MatchingRequestTypeDef" = None,
        Tags: Dict[str, str] = None
    ) -> UpdateDomainResponseTypeDef:
        """
        Updates the properties of a domain, including creating or selecting a dead
        letter queue or an encryption key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.update_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#update_domain)
        """
    def update_profile(
        self,
        *,
        DomainName: str,
        ProfileId: str,
        AdditionalInformation: str = None,
        AccountNumber: str = None,
        PartyType: PartyTypeType = None,
        BusinessName: str = None,
        FirstName: str = None,
        MiddleName: str = None,
        LastName: str = None,
        BirthDate: str = None,
        Gender: GenderType = None,
        PhoneNumber: str = None,
        MobilePhoneNumber: str = None,
        HomePhoneNumber: str = None,
        BusinessPhoneNumber: str = None,
        EmailAddress: str = None,
        PersonalEmailAddress: str = None,
        BusinessEmailAddress: str = None,
        Address: "UpdateAddressTypeDef" = None,
        ShippingAddress: "UpdateAddressTypeDef" = None,
        MailingAddress: "UpdateAddressTypeDef" = None,
        BillingAddress: "UpdateAddressTypeDef" = None,
        Attributes: Dict[str, str] = None
    ) -> UpdateProfileResponseTypeDef:
        """
        Updates the properties of a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/customer-profiles.html#CustomerProfiles.Client.update_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client.html#update_profile)
        """
