"""
Type annotations for connectcampaignsv2 service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_connectcampaignsv2.client import ConnectCampaignServiceV2Client

    session = Session()
    client: ConnectCampaignServiceV2Client = session.client("connectcampaignsv2")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListCampaignsPaginator, ListConnectInstanceIntegrationsPaginator
from .type_defs import (
    CreateCampaignRequestTypeDef,
    CreateCampaignResponseTypeDef,
    DeleteCampaignChannelSubtypeConfigRequestTypeDef,
    DeleteCampaignCommunicationLimitsRequestTypeDef,
    DeleteCampaignCommunicationTimeRequestTypeDef,
    DeleteCampaignRequestTypeDef,
    DeleteConnectInstanceConfigRequestTypeDef,
    DeleteConnectInstanceIntegrationRequestTypeDef,
    DeleteInstanceOnboardingJobRequestTypeDef,
    DescribeCampaignRequestTypeDef,
    DescribeCampaignResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetCampaignStateBatchRequestTypeDef,
    GetCampaignStateBatchResponseTypeDef,
    GetCampaignStateRequestTypeDef,
    GetCampaignStateResponseTypeDef,
    GetConnectInstanceConfigRequestTypeDef,
    GetConnectInstanceConfigResponseTypeDef,
    GetInstanceOnboardingJobStatusRequestTypeDef,
    GetInstanceOnboardingJobStatusResponseTypeDef,
    ListCampaignsRequestTypeDef,
    ListCampaignsResponseTypeDef,
    ListConnectInstanceIntegrationsRequestTypeDef,
    ListConnectInstanceIntegrationsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PauseCampaignRequestTypeDef,
    PutConnectInstanceIntegrationRequestTypeDef,
    PutOutboundRequestBatchRequestTypeDef,
    PutOutboundRequestBatchResponseTypeDef,
    PutProfileOutboundRequestBatchRequestTypeDef,
    PutProfileOutboundRequestBatchResponseTypeDef,
    ResumeCampaignRequestTypeDef,
    StartCampaignRequestTypeDef,
    StartInstanceOnboardingJobRequestTypeDef,
    StartInstanceOnboardingJobResponseTypeDef,
    StopCampaignRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateCampaignChannelSubtypeConfigRequestTypeDef,
    UpdateCampaignCommunicationLimitsRequestTypeDef,
    UpdateCampaignCommunicationTimeRequestTypeDef,
    UpdateCampaignFlowAssociationRequestTypeDef,
    UpdateCampaignNameRequestTypeDef,
    UpdateCampaignScheduleRequestTypeDef,
    UpdateCampaignSourceRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("ConnectCampaignServiceV2Client",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidCampaignStateException: Type[BotocoreClientError]
    InvalidStateException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ConnectCampaignServiceV2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2.html#ConnectCampaignServiceV2.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ConnectCampaignServiceV2Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2.html#ConnectCampaignServiceV2.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#generate_presigned_url)
        """

    def create_campaign(
        self, **kwargs: Unpack[CreateCampaignRequestTypeDef]
    ) -> CreateCampaignResponseTypeDef:
        """
        Creates a campaign for the specified Amazon Connect account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/create_campaign.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#create_campaign)
        """

    def delete_campaign(
        self, **kwargs: Unpack[DeleteCampaignRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a campaign from the specified Amazon Connect account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/delete_campaign.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#delete_campaign)
        """

    def delete_campaign_channel_subtype_config(
        self, **kwargs: Unpack[DeleteCampaignChannelSubtypeConfigRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the channel subtype config of a campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/delete_campaign_channel_subtype_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#delete_campaign_channel_subtype_config)
        """

    def delete_campaign_communication_limits(
        self, **kwargs: Unpack[DeleteCampaignCommunicationLimitsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the communication limits config for a campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/delete_campaign_communication_limits.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#delete_campaign_communication_limits)
        """

    def delete_campaign_communication_time(
        self, **kwargs: Unpack[DeleteCampaignCommunicationTimeRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the communication time config for a campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/delete_campaign_communication_time.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#delete_campaign_communication_time)
        """

    def delete_connect_instance_config(
        self, **kwargs: Unpack[DeleteConnectInstanceConfigRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a connect instance config from the specified AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/delete_connect_instance_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#delete_connect_instance_config)
        """

    def delete_connect_instance_integration(
        self, **kwargs: Unpack[DeleteConnectInstanceIntegrationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete the integration for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/delete_connect_instance_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#delete_connect_instance_integration)
        """

    def delete_instance_onboarding_job(
        self, **kwargs: Unpack[DeleteInstanceOnboardingJobRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete the Connect Campaigns onboarding job for the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/delete_instance_onboarding_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#delete_instance_onboarding_job)
        """

    def describe_campaign(
        self, **kwargs: Unpack[DescribeCampaignRequestTypeDef]
    ) -> DescribeCampaignResponseTypeDef:
        """
        Describes the specific campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/describe_campaign.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#describe_campaign)
        """

    def get_campaign_state(
        self, **kwargs: Unpack[GetCampaignStateRequestTypeDef]
    ) -> GetCampaignStateResponseTypeDef:
        """
        Get state of a campaign for the specified Amazon Connect account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/get_campaign_state.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#get_campaign_state)
        """

    def get_campaign_state_batch(
        self, **kwargs: Unpack[GetCampaignStateBatchRequestTypeDef]
    ) -> GetCampaignStateBatchResponseTypeDef:
        """
        Get state of campaigns for the specified Amazon Connect account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/get_campaign_state_batch.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#get_campaign_state_batch)
        """

    def get_connect_instance_config(
        self, **kwargs: Unpack[GetConnectInstanceConfigRequestTypeDef]
    ) -> GetConnectInstanceConfigResponseTypeDef:
        """
        Get the specific Connect instance config.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/get_connect_instance_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#get_connect_instance_config)
        """

    def get_instance_onboarding_job_status(
        self, **kwargs: Unpack[GetInstanceOnboardingJobStatusRequestTypeDef]
    ) -> GetInstanceOnboardingJobStatusResponseTypeDef:
        """
        Get the specific instance onboarding job status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/get_instance_onboarding_job_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#get_instance_onboarding_job_status)
        """

    def list_campaigns(
        self, **kwargs: Unpack[ListCampaignsRequestTypeDef]
    ) -> ListCampaignsResponseTypeDef:
        """
        Provides summary information about the campaigns under the specified Amazon
        Connect account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/list_campaigns.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#list_campaigns)
        """

    def list_connect_instance_integrations(
        self, **kwargs: Unpack[ListConnectInstanceIntegrationsRequestTypeDef]
    ) -> ListConnectInstanceIntegrationsResponseTypeDef:
        """
        Provides summary information about the integration under the specified Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/list_connect_instance_integrations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#list_connect_instance_integrations)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        List tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#list_tags_for_resource)
        """

    def pause_campaign(
        self, **kwargs: Unpack[PauseCampaignRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Pauses a campaign for the specified Amazon Connect account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/pause_campaign.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#pause_campaign)
        """

    def put_connect_instance_integration(
        self, **kwargs: Unpack[PutConnectInstanceIntegrationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Put or update the integration for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/put_connect_instance_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#put_connect_instance_integration)
        """

    def put_outbound_request_batch(
        self, **kwargs: Unpack[PutOutboundRequestBatchRequestTypeDef]
    ) -> PutOutboundRequestBatchResponseTypeDef:
        """
        Creates outbound requests for the specified campaign Amazon Connect account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/put_outbound_request_batch.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#put_outbound_request_batch)
        """

    def put_profile_outbound_request_batch(
        self, **kwargs: Unpack[PutProfileOutboundRequestBatchRequestTypeDef]
    ) -> PutProfileOutboundRequestBatchResponseTypeDef:
        """
        Takes in a list of profile outbound requests to be placed as part of an
        outbound campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/put_profile_outbound_request_batch.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#put_profile_outbound_request_batch)
        """

    def resume_campaign(
        self, **kwargs: Unpack[ResumeCampaignRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops a campaign for the specified Amazon Connect account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/resume_campaign.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#resume_campaign)
        """

    def start_campaign(
        self, **kwargs: Unpack[StartCampaignRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Starts a campaign for the specified Amazon Connect account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/start_campaign.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#start_campaign)
        """

    def start_instance_onboarding_job(
        self, **kwargs: Unpack[StartInstanceOnboardingJobRequestTypeDef]
    ) -> StartInstanceOnboardingJobResponseTypeDef:
        """
        Onboard the specific Amazon Connect instance to Connect Campaigns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/start_instance_onboarding_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#start_instance_onboarding_job)
        """

    def stop_campaign(
        self, **kwargs: Unpack[StopCampaignRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops a campaign for the specified Amazon Connect account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/stop_campaign.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#stop_campaign)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Tag a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Untag a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#untag_resource)
        """

    def update_campaign_channel_subtype_config(
        self, **kwargs: Unpack[UpdateCampaignChannelSubtypeConfigRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the channel subtype config of a campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/update_campaign_channel_subtype_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#update_campaign_channel_subtype_config)
        """

    def update_campaign_communication_limits(
        self, **kwargs: Unpack[UpdateCampaignCommunicationLimitsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the communication limits config for a campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/update_campaign_communication_limits.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#update_campaign_communication_limits)
        """

    def update_campaign_communication_time(
        self, **kwargs: Unpack[UpdateCampaignCommunicationTimeRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the communication time config for a campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/update_campaign_communication_time.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#update_campaign_communication_time)
        """

    def update_campaign_flow_association(
        self, **kwargs: Unpack[UpdateCampaignFlowAssociationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the campaign flow associated with a campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/update_campaign_flow_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#update_campaign_flow_association)
        """

    def update_campaign_name(
        self, **kwargs: Unpack[UpdateCampaignNameRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the name of a campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/update_campaign_name.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#update_campaign_name)
        """

    def update_campaign_schedule(
        self, **kwargs: Unpack[UpdateCampaignScheduleRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the schedule for a campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/update_campaign_schedule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#update_campaign_schedule)
        """

    def update_campaign_source(
        self, **kwargs: Unpack[UpdateCampaignSourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the campaign source with a campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/update_campaign_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#update_campaign_source)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_campaigns"]
    ) -> ListCampaignsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_connect_instance_integrations"]
    ) -> ListConnectInstanceIntegrationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaignsv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/client/#get_paginator)
        """
