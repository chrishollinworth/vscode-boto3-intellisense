"""
Type annotations for customer-profiles service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_customer_profiles.client import CustomerProfilesClient

    session = Session()
    client: CustomerProfilesClient = session.client("customer-profiles")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    GetSimilarProfilesPaginator,
    ListDomainLayoutsPaginator,
    ListDomainObjectTypesPaginator,
    ListEventStreamsPaginator,
    ListEventTriggersPaginator,
    ListObjectTypeAttributesPaginator,
    ListRecommenderRecipesPaginator,
    ListRecommendersPaginator,
    ListRuleBasedMatchesPaginator,
    ListSegmentDefinitionsPaginator,
    ListUploadJobsPaginator,
)
from .type_defs import (
    AddProfileKeyRequestTypeDef,
    AddProfileKeyResponseTypeDef,
    BatchGetCalculatedAttributeForProfileRequestTypeDef,
    BatchGetCalculatedAttributeForProfileResponseTypeDef,
    BatchGetProfileRequestTypeDef,
    BatchGetProfileResponseTypeDef,
    CreateCalculatedAttributeDefinitionRequestTypeDef,
    CreateCalculatedAttributeDefinitionResponseTypeDef,
    CreateDomainLayoutRequestTypeDef,
    CreateDomainLayoutResponseTypeDef,
    CreateDomainRequestTypeDef,
    CreateDomainResponseTypeDef,
    CreateEventStreamRequestTypeDef,
    CreateEventStreamResponseTypeDef,
    CreateEventTriggerRequestTypeDef,
    CreateEventTriggerResponseTypeDef,
    CreateIntegrationWorkflowRequestTypeDef,
    CreateIntegrationWorkflowResponseTypeDef,
    CreateProfileRequestTypeDef,
    CreateProfileResponseTypeDef,
    CreateRecommenderRequestTypeDef,
    CreateRecommenderResponseTypeDef,
    CreateSegmentDefinitionRequestTypeDef,
    CreateSegmentDefinitionResponseTypeDef,
    CreateSegmentEstimateRequestTypeDef,
    CreateSegmentEstimateResponseTypeDef,
    CreateSegmentSnapshotRequestTypeDef,
    CreateSegmentSnapshotResponseTypeDef,
    CreateUploadJobRequestTypeDef,
    CreateUploadJobResponseTypeDef,
    DeleteCalculatedAttributeDefinitionRequestTypeDef,
    DeleteDomainLayoutRequestTypeDef,
    DeleteDomainLayoutResponseTypeDef,
    DeleteDomainObjectTypeRequestTypeDef,
    DeleteDomainRequestTypeDef,
    DeleteDomainResponseTypeDef,
    DeleteEventStreamRequestTypeDef,
    DeleteEventTriggerRequestTypeDef,
    DeleteEventTriggerResponseTypeDef,
    DeleteIntegrationRequestTypeDef,
    DeleteIntegrationResponseTypeDef,
    DeleteProfileKeyRequestTypeDef,
    DeleteProfileKeyResponseTypeDef,
    DeleteProfileObjectRequestTypeDef,
    DeleteProfileObjectResponseTypeDef,
    DeleteProfileObjectTypeRequestTypeDef,
    DeleteProfileObjectTypeResponseTypeDef,
    DeleteProfileRequestTypeDef,
    DeleteProfileResponseTypeDef,
    DeleteRecommenderRequestTypeDef,
    DeleteSegmentDefinitionRequestTypeDef,
    DeleteSegmentDefinitionResponseTypeDef,
    DeleteWorkflowRequestTypeDef,
    DetectProfileObjectTypeRequestTypeDef,
    DetectProfileObjectTypeResponseTypeDef,
    GetAutoMergingPreviewRequestTypeDef,
    GetAutoMergingPreviewResponseTypeDef,
    GetCalculatedAttributeDefinitionRequestTypeDef,
    GetCalculatedAttributeDefinitionResponseTypeDef,
    GetCalculatedAttributeForProfileRequestTypeDef,
    GetCalculatedAttributeForProfileResponseTypeDef,
    GetDomainLayoutRequestTypeDef,
    GetDomainLayoutResponseTypeDef,
    GetDomainObjectTypeRequestTypeDef,
    GetDomainObjectTypeResponseTypeDef,
    GetDomainRequestTypeDef,
    GetDomainResponseTypeDef,
    GetEventStreamRequestTypeDef,
    GetEventStreamResponseTypeDef,
    GetEventTriggerRequestTypeDef,
    GetEventTriggerResponseTypeDef,
    GetIdentityResolutionJobRequestTypeDef,
    GetIdentityResolutionJobResponseTypeDef,
    GetIntegrationRequestTypeDef,
    GetIntegrationResponseTypeDef,
    GetMatchesRequestTypeDef,
    GetMatchesResponseTypeDef,
    GetObjectTypeAttributeStatisticsRequestTypeDef,
    GetObjectTypeAttributeStatisticsResponseTypeDef,
    GetProfileHistoryRecordRequestTypeDef,
    GetProfileHistoryRecordResponseTypeDef,
    GetProfileObjectTypeRequestTypeDef,
    GetProfileObjectTypeResponseTypeDef,
    GetProfileObjectTypeTemplateRequestTypeDef,
    GetProfileObjectTypeTemplateResponseTypeDef,
    GetProfileRecommendationsRequestTypeDef,
    GetProfileRecommendationsResponseTypeDef,
    GetRecommenderRequestTypeDef,
    GetRecommenderResponseTypeDef,
    GetSegmentDefinitionRequestTypeDef,
    GetSegmentDefinitionResponseTypeDef,
    GetSegmentEstimateRequestTypeDef,
    GetSegmentEstimateResponseTypeDef,
    GetSegmentMembershipRequestTypeDef,
    GetSegmentMembershipResponseTypeDef,
    GetSegmentSnapshotRequestTypeDef,
    GetSegmentSnapshotResponseTypeDef,
    GetSimilarProfilesRequestTypeDef,
    GetSimilarProfilesResponseTypeDef,
    GetUploadJobPathRequestTypeDef,
    GetUploadJobPathResponseTypeDef,
    GetUploadJobRequestTypeDef,
    GetUploadJobResponseTypeDef,
    GetWorkflowRequestTypeDef,
    GetWorkflowResponseTypeDef,
    GetWorkflowStepsRequestTypeDef,
    GetWorkflowStepsResponseTypeDef,
    ListAccountIntegrationsRequestTypeDef,
    ListAccountIntegrationsResponseTypeDef,
    ListCalculatedAttributeDefinitionsRequestTypeDef,
    ListCalculatedAttributeDefinitionsResponseTypeDef,
    ListCalculatedAttributesForProfileRequestTypeDef,
    ListCalculatedAttributesForProfileResponseTypeDef,
    ListDomainLayoutsRequestTypeDef,
    ListDomainLayoutsResponseTypeDef,
    ListDomainObjectTypesRequestTypeDef,
    ListDomainObjectTypesResponseTypeDef,
    ListDomainsRequestTypeDef,
    ListDomainsResponseTypeDef,
    ListEventStreamsRequestTypeDef,
    ListEventStreamsResponseTypeDef,
    ListEventTriggersRequestTypeDef,
    ListEventTriggersResponseTypeDef,
    ListIdentityResolutionJobsRequestTypeDef,
    ListIdentityResolutionJobsResponseTypeDef,
    ListIntegrationsRequestTypeDef,
    ListIntegrationsResponseTypeDef,
    ListObjectTypeAttributesRequestTypeDef,
    ListObjectTypeAttributesResponseTypeDef,
    ListObjectTypeAttributeValuesRequestTypeDef,
    ListObjectTypeAttributeValuesResponseTypeDef,
    ListProfileHistoryRecordsRequestTypeDef,
    ListProfileHistoryRecordsResponseTypeDef,
    ListProfileObjectsRequestTypeDef,
    ListProfileObjectsResponseTypeDef,
    ListProfileObjectTypesRequestTypeDef,
    ListProfileObjectTypesResponseTypeDef,
    ListProfileObjectTypeTemplatesRequestTypeDef,
    ListProfileObjectTypeTemplatesResponseTypeDef,
    ListRecommenderRecipesRequestTypeDef,
    ListRecommenderRecipesResponseTypeDef,
    ListRecommendersRequestTypeDef,
    ListRecommendersResponseTypeDef,
    ListRuleBasedMatchesRequestTypeDef,
    ListRuleBasedMatchesResponseTypeDef,
    ListSegmentDefinitionsRequestTypeDef,
    ListSegmentDefinitionsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUploadJobsRequestTypeDef,
    ListUploadJobsResponseTypeDef,
    ListWorkflowsRequestTypeDef,
    ListWorkflowsResponseTypeDef,
    MergeProfilesRequestTypeDef,
    MergeProfilesResponseTypeDef,
    ProfileAttributeValuesRequestTypeDef,
    ProfileAttributeValuesResponseTypeDef,
    PutDomainObjectTypeRequestTypeDef,
    PutDomainObjectTypeResponseTypeDef,
    PutIntegrationRequestTypeDef,
    PutIntegrationResponseTypeDef,
    PutProfileObjectRequestTypeDef,
    PutProfileObjectResponseTypeDef,
    PutProfileObjectTypeRequestTypeDef,
    PutProfileObjectTypeResponseTypeDef,
    SearchProfilesRequestTypeDef,
    SearchProfilesResponseTypeDef,
    StartRecommenderRequestTypeDef,
    StartUploadJobRequestTypeDef,
    StopRecommenderRequestTypeDef,
    StopUploadJobRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateCalculatedAttributeDefinitionRequestTypeDef,
    UpdateCalculatedAttributeDefinitionResponseTypeDef,
    UpdateDomainLayoutRequestTypeDef,
    UpdateDomainLayoutResponseTypeDef,
    UpdateDomainRequestTypeDef,
    UpdateDomainResponseTypeDef,
    UpdateEventTriggerRequestTypeDef,
    UpdateEventTriggerResponseTypeDef,
    UpdateProfileRequestTypeDef,
    UpdateProfileResponseTypeDef,
    UpdateRecommenderRequestTypeDef,
    UpdateRecommenderResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("CustomerProfilesClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]

class CustomerProfilesClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CustomerProfilesClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#generate_presigned_url)
        """

    def add_profile_key(
        self, **kwargs: Unpack[AddProfileKeyRequestTypeDef]
    ) -> AddProfileKeyResponseTypeDef:
        """
        Associates a new key value with a specific profile, such as a Contact Record
        ContactId.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/add_profile_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#add_profile_key)
        """

    def batch_get_calculated_attribute_for_profile(
        self, **kwargs: Unpack[BatchGetCalculatedAttributeForProfileRequestTypeDef]
    ) -> BatchGetCalculatedAttributeForProfileResponseTypeDef:
        """
        Fetch the possible attribute values given the attribute name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/batch_get_calculated_attribute_for_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#batch_get_calculated_attribute_for_profile)
        """

    def batch_get_profile(
        self, **kwargs: Unpack[BatchGetProfileRequestTypeDef]
    ) -> BatchGetProfileResponseTypeDef:
        """
        Get a batch of profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/batch_get_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#batch_get_profile)
        """

    def create_calculated_attribute_definition(
        self, **kwargs: Unpack[CreateCalculatedAttributeDefinitionRequestTypeDef]
    ) -> CreateCalculatedAttributeDefinitionResponseTypeDef:
        """
        Creates a new calculated attribute definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/create_calculated_attribute_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#create_calculated_attribute_definition)
        """

    def create_domain(
        self, **kwargs: Unpack[CreateDomainRequestTypeDef]
    ) -> CreateDomainResponseTypeDef:
        """
        Creates a domain, which is a container for all customer data, such as customer
        profile attributes, object types, profile keys, and encryption keys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/create_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#create_domain)
        """

    def create_domain_layout(
        self, **kwargs: Unpack[CreateDomainLayoutRequestTypeDef]
    ) -> CreateDomainLayoutResponseTypeDef:
        """
        Creates the layout to view data for a specific domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/create_domain_layout.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#create_domain_layout)
        """

    def create_event_stream(
        self, **kwargs: Unpack[CreateEventStreamRequestTypeDef]
    ) -> CreateEventStreamResponseTypeDef:
        """
        Creates an event stream, which is a subscription to real-time events, such as
        when profiles are created and updated through Amazon Connect Customer Profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/create_event_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#create_event_stream)
        """

    def create_event_trigger(
        self, **kwargs: Unpack[CreateEventTriggerRequestTypeDef]
    ) -> CreateEventTriggerResponseTypeDef:
        """
        Creates an event trigger, which specifies the rules when to perform action
        based on customer's ingested data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/create_event_trigger.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#create_event_trigger)
        """

    def create_integration_workflow(
        self, **kwargs: Unpack[CreateIntegrationWorkflowRequestTypeDef]
    ) -> CreateIntegrationWorkflowResponseTypeDef:
        """
        Creates an integration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/create_integration_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#create_integration_workflow)
        """

    def create_profile(
        self, **kwargs: Unpack[CreateProfileRequestTypeDef]
    ) -> CreateProfileResponseTypeDef:
        """
        Creates a standard profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/create_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#create_profile)
        """

    def create_recommender(
        self, **kwargs: Unpack[CreateRecommenderRequestTypeDef]
    ) -> CreateRecommenderResponseTypeDef:
        """
        Creates a recommender.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/create_recommender.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#create_recommender)
        """

    def create_segment_definition(
        self, **kwargs: Unpack[CreateSegmentDefinitionRequestTypeDef]
    ) -> CreateSegmentDefinitionResponseTypeDef:
        """
        Creates a segment definition associated to the given domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/create_segment_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#create_segment_definition)
        """

    def create_segment_estimate(
        self, **kwargs: Unpack[CreateSegmentEstimateRequestTypeDef]
    ) -> CreateSegmentEstimateResponseTypeDef:
        """
        Creates a segment estimate query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/create_segment_estimate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#create_segment_estimate)
        """

    def create_segment_snapshot(
        self, **kwargs: Unpack[CreateSegmentSnapshotRequestTypeDef]
    ) -> CreateSegmentSnapshotResponseTypeDef:
        """
        Triggers a job to export a segment to a specified destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/create_segment_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#create_segment_snapshot)
        """

    def create_upload_job(
        self, **kwargs: Unpack[CreateUploadJobRequestTypeDef]
    ) -> CreateUploadJobResponseTypeDef:
        """
        Creates an Upload job to ingest data for segment imports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/create_upload_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#create_upload_job)
        """

    def delete_calculated_attribute_definition(
        self, **kwargs: Unpack[DeleteCalculatedAttributeDefinitionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an existing calculated attribute definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/delete_calculated_attribute_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#delete_calculated_attribute_definition)
        """

    def delete_domain(
        self, **kwargs: Unpack[DeleteDomainRequestTypeDef]
    ) -> DeleteDomainResponseTypeDef:
        """
        Deletes a specific domain and all of its customer data, such as customer
        profile attributes and their related objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/delete_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#delete_domain)
        """

    def delete_domain_layout(
        self, **kwargs: Unpack[DeleteDomainLayoutRequestTypeDef]
    ) -> DeleteDomainLayoutResponseTypeDef:
        """
        Deletes the layout used to view data for a specific domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/delete_domain_layout.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#delete_domain_layout)
        """

    def delete_domain_object_type(
        self, **kwargs: Unpack[DeleteDomainObjectTypeRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete a DomainObjectType for the given Domain and ObjectType name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/delete_domain_object_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#delete_domain_object_type)
        """

    def delete_event_stream(
        self, **kwargs: Unpack[DeleteEventStreamRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disables and deletes the specified event stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/delete_event_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#delete_event_stream)
        """

    def delete_event_trigger(
        self, **kwargs: Unpack[DeleteEventTriggerRequestTypeDef]
    ) -> DeleteEventTriggerResponseTypeDef:
        """
        Disable and deletes the Event Trigger.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/delete_event_trigger.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#delete_event_trigger)
        """

    def delete_integration(
        self, **kwargs: Unpack[DeleteIntegrationRequestTypeDef]
    ) -> DeleteIntegrationResponseTypeDef:
        """
        Removes an integration from a specific domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/delete_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#delete_integration)
        """

    def delete_profile(
        self, **kwargs: Unpack[DeleteProfileRequestTypeDef]
    ) -> DeleteProfileResponseTypeDef:
        """
        Deletes the standard customer profile and all data pertaining to the profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/delete_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#delete_profile)
        """

    def delete_profile_key(
        self, **kwargs: Unpack[DeleteProfileKeyRequestTypeDef]
    ) -> DeleteProfileKeyResponseTypeDef:
        """
        Removes a searchable key from a customer profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/delete_profile_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#delete_profile_key)
        """

    def delete_profile_object(
        self, **kwargs: Unpack[DeleteProfileObjectRequestTypeDef]
    ) -> DeleteProfileObjectResponseTypeDef:
        """
        Removes an object associated with a profile of a given ProfileObjectType.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/delete_profile_object.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#delete_profile_object)
        """

    def delete_profile_object_type(
        self, **kwargs: Unpack[DeleteProfileObjectTypeRequestTypeDef]
    ) -> DeleteProfileObjectTypeResponseTypeDef:
        """
        Removes a ProfileObjectType from a specific domain as well as removes all the
        ProfileObjects of that type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/delete_profile_object_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#delete_profile_object_type)
        """

    def delete_recommender(
        self, **kwargs: Unpack[DeleteRecommenderRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a recommender.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/delete_recommender.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#delete_recommender)
        """

    def delete_segment_definition(
        self, **kwargs: Unpack[DeleteSegmentDefinitionRequestTypeDef]
    ) -> DeleteSegmentDefinitionResponseTypeDef:
        """
        Deletes a segment definition from the domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/delete_segment_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#delete_segment_definition)
        """

    def delete_workflow(self, **kwargs: Unpack[DeleteWorkflowRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified workflow and all its corresponding resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/delete_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#delete_workflow)
        """

    def detect_profile_object_type(
        self, **kwargs: Unpack[DetectProfileObjectTypeRequestTypeDef]
    ) -> DetectProfileObjectTypeResponseTypeDef:
        """
        The process of detecting profile object type mapping by using given objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/detect_profile_object_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#detect_profile_object_type)
        """

    def get_auto_merging_preview(
        self, **kwargs: Unpack[GetAutoMergingPreviewRequestTypeDef]
    ) -> GetAutoMergingPreviewResponseTypeDef:
        """
        Tests the auto-merging settings of your Identity Resolution Job without merging
        your data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_auto_merging_preview.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_auto_merging_preview)
        """

    def get_calculated_attribute_definition(
        self, **kwargs: Unpack[GetCalculatedAttributeDefinitionRequestTypeDef]
    ) -> GetCalculatedAttributeDefinitionResponseTypeDef:
        """
        Provides more information on a calculated attribute definition for Customer
        Profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_calculated_attribute_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_calculated_attribute_definition)
        """

    def get_calculated_attribute_for_profile(
        self, **kwargs: Unpack[GetCalculatedAttributeForProfileRequestTypeDef]
    ) -> GetCalculatedAttributeForProfileResponseTypeDef:
        """
        Retrieve a calculated attribute for a customer profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_calculated_attribute_for_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_calculated_attribute_for_profile)
        """

    def get_domain(self, **kwargs: Unpack[GetDomainRequestTypeDef]) -> GetDomainResponseTypeDef:
        """
        Returns information about a specific domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_domain)
        """

    def get_domain_layout(
        self, **kwargs: Unpack[GetDomainLayoutRequestTypeDef]
    ) -> GetDomainLayoutResponseTypeDef:
        """
        Gets the layout to view data for a specific domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_domain_layout.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_domain_layout)
        """

    def get_domain_object_type(
        self, **kwargs: Unpack[GetDomainObjectTypeRequestTypeDef]
    ) -> GetDomainObjectTypeResponseTypeDef:
        """
        Return a DomainObjectType for the input Domain and ObjectType names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_domain_object_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_domain_object_type)
        """

    def get_event_stream(
        self, **kwargs: Unpack[GetEventStreamRequestTypeDef]
    ) -> GetEventStreamResponseTypeDef:
        """
        Returns information about the specified event stream in a specific domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_event_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_event_stream)
        """

    def get_event_trigger(
        self, **kwargs: Unpack[GetEventTriggerRequestTypeDef]
    ) -> GetEventTriggerResponseTypeDef:
        """
        Get a specific Event Trigger from the domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_event_trigger.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_event_trigger)
        """

    def get_identity_resolution_job(
        self, **kwargs: Unpack[GetIdentityResolutionJobRequestTypeDef]
    ) -> GetIdentityResolutionJobResponseTypeDef:
        """
        Returns information about an Identity Resolution Job in a specific domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_identity_resolution_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_identity_resolution_job)
        """

    def get_integration(
        self, **kwargs: Unpack[GetIntegrationRequestTypeDef]
    ) -> GetIntegrationResponseTypeDef:
        """
        Returns an integration for a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_integration)
        """

    def get_matches(self, **kwargs: Unpack[GetMatchesRequestTypeDef]) -> GetMatchesResponseTypeDef:
        """
        Before calling this API, use <a
        href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateDomain.html">CreateDomain</a>
        or <a
        href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateDomain.html">UpdateDomain</a>
        to enable identity resolution: set <c...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_matches.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_matches)
        """

    def get_object_type_attribute_statistics(
        self, **kwargs: Unpack[GetObjectTypeAttributeStatisticsRequestTypeDef]
    ) -> GetObjectTypeAttributeStatisticsResponseTypeDef:
        """
        The GetObjectTypeAttributeValues API delivers statistical insights about
        attributes within a specific object type, but is exclusively available for
        domains with data store enabled.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_object_type_attribute_statistics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_object_type_attribute_statistics)
        """

    def get_profile_history_record(
        self, **kwargs: Unpack[GetProfileHistoryRecordRequestTypeDef]
    ) -> GetProfileHistoryRecordResponseTypeDef:
        """
        Returns a history record for a specific profile, for a specific domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_profile_history_record.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_profile_history_record)
        """

    def get_profile_object_type(
        self, **kwargs: Unpack[GetProfileObjectTypeRequestTypeDef]
    ) -> GetProfileObjectTypeResponseTypeDef:
        """
        Returns the object types for a specific domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_profile_object_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_profile_object_type)
        """

    def get_profile_object_type_template(
        self, **kwargs: Unpack[GetProfileObjectTypeTemplateRequestTypeDef]
    ) -> GetProfileObjectTypeTemplateResponseTypeDef:
        """
        Returns the template information for a specific object type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_profile_object_type_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_profile_object_type_template)
        """

    def get_profile_recommendations(
        self, **kwargs: Unpack[GetProfileRecommendationsRequestTypeDef]
    ) -> GetProfileRecommendationsResponseTypeDef:
        """
        Fetches the recommendations for a profile in the input Customer Profiles domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_profile_recommendations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_profile_recommendations)
        """

    def get_recommender(
        self, **kwargs: Unpack[GetRecommenderRequestTypeDef]
    ) -> GetRecommenderResponseTypeDef:
        """
        Retrieves a recommender.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_recommender.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_recommender)
        """

    def get_segment_definition(
        self, **kwargs: Unpack[GetSegmentDefinitionRequestTypeDef]
    ) -> GetSegmentDefinitionResponseTypeDef:
        """
        Gets a segment definition from the domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_segment_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_segment_definition)
        """

    def get_segment_estimate(
        self, **kwargs: Unpack[GetSegmentEstimateRequestTypeDef]
    ) -> GetSegmentEstimateResponseTypeDef:
        """
        Gets the result of a segment estimate query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_segment_estimate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_segment_estimate)
        """

    def get_segment_membership(
        self, **kwargs: Unpack[GetSegmentMembershipRequestTypeDef]
    ) -> GetSegmentMembershipResponseTypeDef:
        """
        Determines if the given profiles are within a segment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_segment_membership.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_segment_membership)
        """

    def get_segment_snapshot(
        self, **kwargs: Unpack[GetSegmentSnapshotRequestTypeDef]
    ) -> GetSegmentSnapshotResponseTypeDef:
        """
        Retrieve the latest status of a segment snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_segment_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_segment_snapshot)
        """

    def get_similar_profiles(
        self, **kwargs: Unpack[GetSimilarProfilesRequestTypeDef]
    ) -> GetSimilarProfilesResponseTypeDef:
        """
        Returns a set of profiles that belong to the same matching group using the
        <code>matchId</code> or <code>profileId</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_similar_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_similar_profiles)
        """

    def get_upload_job(
        self, **kwargs: Unpack[GetUploadJobRequestTypeDef]
    ) -> GetUploadJobResponseTypeDef:
        """
        This API retrieves the details of a specific upload job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_upload_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_upload_job)
        """

    def get_upload_job_path(
        self, **kwargs: Unpack[GetUploadJobPathRequestTypeDef]
    ) -> GetUploadJobPathResponseTypeDef:
        """
        This API retrieves the pre-signed URL and client token for uploading the file
        associated with the upload job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_upload_job_path.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_upload_job_path)
        """

    def get_workflow(
        self, **kwargs: Unpack[GetWorkflowRequestTypeDef]
    ) -> GetWorkflowResponseTypeDef:
        """
        Get details of specified workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_workflow)
        """

    def get_workflow_steps(
        self, **kwargs: Unpack[GetWorkflowStepsRequestTypeDef]
    ) -> GetWorkflowStepsResponseTypeDef:
        """
        Get granular list of steps in workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_workflow_steps.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_workflow_steps)
        """

    def list_account_integrations(
        self, **kwargs: Unpack[ListAccountIntegrationsRequestTypeDef]
    ) -> ListAccountIntegrationsResponseTypeDef:
        """
        Lists all of the integrations associated to a specific URI in the AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/list_account_integrations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#list_account_integrations)
        """

    def list_calculated_attribute_definitions(
        self, **kwargs: Unpack[ListCalculatedAttributeDefinitionsRequestTypeDef]
    ) -> ListCalculatedAttributeDefinitionsResponseTypeDef:
        """
        Lists calculated attribute definitions for Customer Profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/list_calculated_attribute_definitions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#list_calculated_attribute_definitions)
        """

    def list_calculated_attributes_for_profile(
        self, **kwargs: Unpack[ListCalculatedAttributesForProfileRequestTypeDef]
    ) -> ListCalculatedAttributesForProfileResponseTypeDef:
        """
        Retrieve a list of calculated attributes for a customer profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/list_calculated_attributes_for_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#list_calculated_attributes_for_profile)
        """

    def list_domain_layouts(
        self, **kwargs: Unpack[ListDomainLayoutsRequestTypeDef]
    ) -> ListDomainLayoutsResponseTypeDef:
        """
        Lists the existing layouts that can be used to view data for a specific domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/list_domain_layouts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#list_domain_layouts)
        """

    def list_domain_object_types(
        self, **kwargs: Unpack[ListDomainObjectTypesRequestTypeDef]
    ) -> ListDomainObjectTypesResponseTypeDef:
        """
        List all DomainObjectType(s) in a Customer Profiles domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/list_domain_object_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#list_domain_object_types)
        """

    def list_domains(
        self, **kwargs: Unpack[ListDomainsRequestTypeDef]
    ) -> ListDomainsResponseTypeDef:
        """
        Returns a list of all the domains for an AWS account that have been created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/list_domains.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#list_domains)
        """

    def list_event_streams(
        self, **kwargs: Unpack[ListEventStreamsRequestTypeDef]
    ) -> ListEventStreamsResponseTypeDef:
        """
        Returns a list of all the event streams in a specific domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/list_event_streams.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#list_event_streams)
        """

    def list_event_triggers(
        self, **kwargs: Unpack[ListEventTriggersRequestTypeDef]
    ) -> ListEventTriggersResponseTypeDef:
        """
        List all Event Triggers under a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/list_event_triggers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#list_event_triggers)
        """

    def list_identity_resolution_jobs(
        self, **kwargs: Unpack[ListIdentityResolutionJobsRequestTypeDef]
    ) -> ListIdentityResolutionJobsResponseTypeDef:
        """
        Lists all of the Identity Resolution Jobs in your domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/list_identity_resolution_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#list_identity_resolution_jobs)
        """

    def list_integrations(
        self, **kwargs: Unpack[ListIntegrationsRequestTypeDef]
    ) -> ListIntegrationsResponseTypeDef:
        """
        Lists all of the integrations in your domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/list_integrations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#list_integrations)
        """

    def list_object_type_attribute_values(
        self, **kwargs: Unpack[ListObjectTypeAttributeValuesRequestTypeDef]
    ) -> ListObjectTypeAttributeValuesResponseTypeDef:
        """
        The ListObjectTypeAttributeValues API provides access to the most recent
        distinct values for any specified attribute, making it valuable for real-time
        data validation and consistency checks within your object types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/list_object_type_attribute_values.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#list_object_type_attribute_values)
        """

    def list_object_type_attributes(
        self, **kwargs: Unpack[ListObjectTypeAttributesRequestTypeDef]
    ) -> ListObjectTypeAttributesResponseTypeDef:
        """
        Fetch the possible attribute values given the attribute name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/list_object_type_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#list_object_type_attributes)
        """

    def list_profile_attribute_values(
        self, **kwargs: Unpack[ProfileAttributeValuesRequestTypeDef]
    ) -> ProfileAttributeValuesResponseTypeDef:
        """
        Fetch the possible attribute values given the attribute name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/list_profile_attribute_values.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#list_profile_attribute_values)
        """

    def list_profile_history_records(
        self, **kwargs: Unpack[ListProfileHistoryRecordsRequestTypeDef]
    ) -> ListProfileHistoryRecordsResponseTypeDef:
        """
        Returns a list of history records for a specific profile, for a specific domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/list_profile_history_records.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#list_profile_history_records)
        """

    def list_profile_object_type_templates(
        self, **kwargs: Unpack[ListProfileObjectTypeTemplatesRequestTypeDef]
    ) -> ListProfileObjectTypeTemplatesResponseTypeDef:
        """
        Lists all of the template information for object types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/list_profile_object_type_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#list_profile_object_type_templates)
        """

    def list_profile_object_types(
        self, **kwargs: Unpack[ListProfileObjectTypesRequestTypeDef]
    ) -> ListProfileObjectTypesResponseTypeDef:
        """
        Lists all of the templates available within the service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/list_profile_object_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#list_profile_object_types)
        """

    def list_profile_objects(
        self, **kwargs: Unpack[ListProfileObjectsRequestTypeDef]
    ) -> ListProfileObjectsResponseTypeDef:
        """
        Returns a list of objects associated with a profile of a given
        ProfileObjectType.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/list_profile_objects.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#list_profile_objects)
        """

    def list_recommender_recipes(
        self, **kwargs: Unpack[ListRecommenderRecipesRequestTypeDef]
    ) -> ListRecommenderRecipesResponseTypeDef:
        """
        Returns a list of available recommender recipes that can be used to create
        recommenders.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/list_recommender_recipes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#list_recommender_recipes)
        """

    def list_recommenders(
        self, **kwargs: Unpack[ListRecommendersRequestTypeDef]
    ) -> ListRecommendersResponseTypeDef:
        """
        Returns a list of recommenders in the specified domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/list_recommenders.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#list_recommenders)
        """

    def list_rule_based_matches(
        self, **kwargs: Unpack[ListRuleBasedMatchesRequestTypeDef]
    ) -> ListRuleBasedMatchesResponseTypeDef:
        """
        Returns a set of <code>MatchIds</code> that belong to the given domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/list_rule_based_matches.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#list_rule_based_matches)
        """

    def list_segment_definitions(
        self, **kwargs: Unpack[ListSegmentDefinitionsRequestTypeDef]
    ) -> ListSegmentDefinitionsResponseTypeDef:
        """
        Lists all segment definitions under a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/list_segment_definitions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#list_segment_definitions)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Displays the tags associated with an Amazon Connect Customer Profiles resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#list_tags_for_resource)
        """

    def list_upload_jobs(
        self, **kwargs: Unpack[ListUploadJobsRequestTypeDef]
    ) -> ListUploadJobsResponseTypeDef:
        """
        This API retrieves a list of upload jobs for the specified domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/list_upload_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#list_upload_jobs)
        """

    def list_workflows(
        self, **kwargs: Unpack[ListWorkflowsRequestTypeDef]
    ) -> ListWorkflowsResponseTypeDef:
        """
        Query to list all workflows.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/list_workflows.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#list_workflows)
        """

    def merge_profiles(
        self, **kwargs: Unpack[MergeProfilesRequestTypeDef]
    ) -> MergeProfilesResponseTypeDef:
        """
        Runs an AWS Lambda job that does the following:.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/merge_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#merge_profiles)
        """

    def put_domain_object_type(
        self, **kwargs: Unpack[PutDomainObjectTypeRequestTypeDef]
    ) -> PutDomainObjectTypeResponseTypeDef:
        """
        Create/Update a DomainObjectType in a Customer Profiles domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/put_domain_object_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#put_domain_object_type)
        """

    def put_integration(
        self, **kwargs: Unpack[PutIntegrationRequestTypeDef]
    ) -> PutIntegrationResponseTypeDef:
        """
        Adds an integration between the service and a third-party service, which
        includes Amazon AppFlow and Amazon Connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/put_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#put_integration)
        """

    def put_profile_object(
        self, **kwargs: Unpack[PutProfileObjectRequestTypeDef]
    ) -> PutProfileObjectResponseTypeDef:
        """
        Adds additional objects to customer profiles of a given ObjectType.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/put_profile_object.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#put_profile_object)
        """

    def put_profile_object_type(
        self, **kwargs: Unpack[PutProfileObjectTypeRequestTypeDef]
    ) -> PutProfileObjectTypeResponseTypeDef:
        """
        Defines a ProfileObjectType.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/put_profile_object_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#put_profile_object_type)
        """

    def search_profiles(
        self, **kwargs: Unpack[SearchProfilesRequestTypeDef]
    ) -> SearchProfilesResponseTypeDef:
        """
        Searches for profiles within a specific domain using one or more predefined
        search keys (e.g., _fullName, _phone, _email, _account, etc.) and/or
        custom-defined search keys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/search_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#search_profiles)
        """

    def start_recommender(self, **kwargs: Unpack[StartRecommenderRequestTypeDef]) -> Dict[str, Any]:
        """
        Starts a recommender that was previously stopped.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/start_recommender.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#start_recommender)
        """

    def start_upload_job(self, **kwargs: Unpack[StartUploadJobRequestTypeDef]) -> Dict[str, Any]:
        """
        This API starts the processing of an upload job to ingest profile data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/start_upload_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#start_upload_job)
        """

    def stop_recommender(self, **kwargs: Unpack[StopRecommenderRequestTypeDef]) -> Dict[str, Any]:
        """
        Stops a recommender, suspending its ability to generate recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/stop_recommender.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#stop_recommender)
        """

    def stop_upload_job(self, **kwargs: Unpack[StopUploadJobRequestTypeDef]) -> Dict[str, Any]:
        """
        This API stops the processing of an upload job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/stop_upload_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#stop_upload_job)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified Amazon Connect
        Customer Profiles resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified Amazon Connect Customer Profiles
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#untag_resource)
        """

    def update_calculated_attribute_definition(
        self, **kwargs: Unpack[UpdateCalculatedAttributeDefinitionRequestTypeDef]
    ) -> UpdateCalculatedAttributeDefinitionResponseTypeDef:
        """
        Updates an existing calculated attribute definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/update_calculated_attribute_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#update_calculated_attribute_definition)
        """

    def update_domain(
        self, **kwargs: Unpack[UpdateDomainRequestTypeDef]
    ) -> UpdateDomainResponseTypeDef:
        """
        Updates the properties of a domain, including creating or selecting a dead
        letter queue or an encryption key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/update_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#update_domain)
        """

    def update_domain_layout(
        self, **kwargs: Unpack[UpdateDomainLayoutRequestTypeDef]
    ) -> UpdateDomainLayoutResponseTypeDef:
        """
        Updates the layout used to view data for a specific domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/update_domain_layout.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#update_domain_layout)
        """

    def update_event_trigger(
        self, **kwargs: Unpack[UpdateEventTriggerRequestTypeDef]
    ) -> UpdateEventTriggerResponseTypeDef:
        """
        Update the properties of an Event Trigger.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/update_event_trigger.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#update_event_trigger)
        """

    def update_profile(
        self, **kwargs: Unpack[UpdateProfileRequestTypeDef]
    ) -> UpdateProfileResponseTypeDef:
        """
        Updates the properties of a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/update_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#update_profile)
        """

    def update_recommender(
        self, **kwargs: Unpack[UpdateRecommenderRequestTypeDef]
    ) -> UpdateRecommenderResponseTypeDef:
        """
        Updates the properties of an existing recommender, allowing you to modify its
        configuration and description.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/update_recommender.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#update_recommender)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_similar_profiles"]
    ) -> GetSimilarProfilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_domain_layouts"]
    ) -> ListDomainLayoutsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_domain_object_types"]
    ) -> ListDomainObjectTypesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_event_streams"]
    ) -> ListEventStreamsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_event_triggers"]
    ) -> ListEventTriggersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_object_type_attributes"]
    ) -> ListObjectTypeAttributesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_recommender_recipes"]
    ) -> ListRecommenderRecipesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_recommenders"]
    ) -> ListRecommendersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_rule_based_matches"]
    ) -> ListRuleBasedMatchesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_segment_definitions"]
    ) -> ListSegmentDefinitionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_upload_jobs"]
    ) -> ListUploadJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/client/#get_paginator)
        """
