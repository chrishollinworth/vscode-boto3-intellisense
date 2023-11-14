"""
Type annotations for connectcampaigns service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_connectcampaigns import ConnectCampaignServiceClient

    client: ConnectCampaignServiceClient = boto3.client("connectcampaigns")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .paginator import ListCampaignsPaginator
from .type_defs import (
    AnswerMachineDetectionConfigTypeDef,
    CampaignFiltersTypeDef,
    CreateCampaignResponseTypeDef,
    DescribeCampaignResponseTypeDef,
    DialerConfigTypeDef,
    DialRequestTypeDef,
    EncryptionConfigTypeDef,
    GetCampaignStateBatchResponseTypeDef,
    GetCampaignStateResponseTypeDef,
    GetConnectInstanceConfigResponseTypeDef,
    GetInstanceOnboardingJobStatusResponseTypeDef,
    ListCampaignsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    OutboundCallConfigTypeDef,
    PutDialRequestBatchResponseTypeDef,
    StartInstanceOnboardingJobResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ConnectCampaignServiceClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
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

class ConnectCampaignServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ConnectCampaignServiceClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#close)
        """
    def create_campaign(
        self,
        *,
        name: str,
        connectInstanceId: str,
        dialerConfig: "DialerConfigTypeDef",
        outboundCallConfig: "OutboundCallConfigTypeDef",
        tags: Dict[str, str] = None
    ) -> CreateCampaignResponseTypeDef:
        """
        Creates a campaign for the specified Amazon Connect account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.create_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#create_campaign)
        """
    def delete_campaign(self, *, id: str) -> None:
        """
        Deletes a campaign from the specified Amazon Connect account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.delete_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#delete_campaign)
        """
    def delete_connect_instance_config(self, *, connectInstanceId: str) -> None:
        """
        Deletes a connect instance config from the specified AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.delete_connect_instance_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#delete_connect_instance_config)
        """
    def delete_instance_onboarding_job(self, *, connectInstanceId: str) -> None:
        """
        Delete the Connect Campaigns onboarding job for the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.delete_instance_onboarding_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#delete_instance_onboarding_job)
        """
    def describe_campaign(self, *, id: str) -> DescribeCampaignResponseTypeDef:
        """
        Describes the specific campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.describe_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#describe_campaign)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#generate_presigned_url)
        """
    def get_campaign_state(self, *, id: str) -> GetCampaignStateResponseTypeDef:
        """
        Get state of a campaign for the specified Amazon Connect account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.get_campaign_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#get_campaign_state)
        """
    def get_campaign_state_batch(
        self, *, campaignIds: List[str]
    ) -> GetCampaignStateBatchResponseTypeDef:
        """
        Get state of campaigns for the specified Amazon Connect account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.get_campaign_state_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#get_campaign_state_batch)
        """
    def get_connect_instance_config(
        self, *, connectInstanceId: str
    ) -> GetConnectInstanceConfigResponseTypeDef:
        """
        Get the specific Connect instance config.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.get_connect_instance_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#get_connect_instance_config)
        """
    def get_instance_onboarding_job_status(
        self, *, connectInstanceId: str
    ) -> GetInstanceOnboardingJobStatusResponseTypeDef:
        """
        Get the specific instance onboarding job status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.get_instance_onboarding_job_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#get_instance_onboarding_job_status)
        """
    def list_campaigns(
        self,
        *,
        maxResults: int = None,
        nextToken: str = None,
        filters: "CampaignFiltersTypeDef" = None
    ) -> ListCampaignsResponseTypeDef:
        """
        Provides summary information about the campaigns under the specified Amazon
        Connect account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.list_campaigns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#list_campaigns)
        """
    def list_tags_for_resource(self, *, arn: str) -> ListTagsForResourceResponseTypeDef:
        """
        List tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#list_tags_for_resource)
        """
    def pause_campaign(self, *, id: str) -> None:
        """
        Pauses a campaign for the specified Amazon Connect account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.pause_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#pause_campaign)
        """
    def put_dial_request_batch(
        self, *, id: str, dialRequests: List["DialRequestTypeDef"]
    ) -> PutDialRequestBatchResponseTypeDef:
        """
        Creates dials requests for the specified campaign Amazon Connect account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.put_dial_request_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#put_dial_request_batch)
        """
    def resume_campaign(self, *, id: str) -> None:
        """
        Stops a campaign for the specified Amazon Connect account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.resume_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#resume_campaign)
        """
    def start_campaign(self, *, id: str) -> None:
        """
        Starts a campaign for the specified Amazon Connect account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.start_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#start_campaign)
        """
    def start_instance_onboarding_job(
        self, *, connectInstanceId: str, encryptionConfig: "EncryptionConfigTypeDef"
    ) -> StartInstanceOnboardingJobResponseTypeDef:
        """
        Onboard the specific Amazon Connect instance to Connect Campaigns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.start_instance_onboarding_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#start_instance_onboarding_job)
        """
    def stop_campaign(self, *, id: str) -> None:
        """
        Stops a campaign for the specified Amazon Connect account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.stop_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#stop_campaign)
        """
    def tag_resource(self, *, arn: str, tags: Dict[str, str]) -> None:
        """
        Tag a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#tag_resource)
        """
    def untag_resource(self, *, arn: str, tagKeys: List[str]) -> None:
        """
        Untag a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#untag_resource)
        """
    def update_campaign_dialer_config(
        self, *, id: str, dialerConfig: "DialerConfigTypeDef"
    ) -> None:
        """
        Updates the dialer config of a campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.update_campaign_dialer_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#update_campaign_dialer_config)
        """
    def update_campaign_name(self, *, id: str, name: str) -> None:
        """
        Updates the name of a campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.update_campaign_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#update_campaign_name)
        """
    def update_campaign_outbound_call_config(
        self,
        *,
        id: str,
        connectContactFlowId: str = None,
        connectSourcePhoneNumber: str = None,
        answerMachineDetectionConfig: "AnswerMachineDetectionConfigTypeDef" = None
    ) -> None:
        """
        Updates the outbound call config of a campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Client.update_campaign_outbound_call_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/client.html#update_campaign_outbound_call_config)
        """
    def get_paginator(self, operation_name: Literal["list_campaigns"]) -> ListCampaignsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/connectcampaigns.html#ConnectCampaignService.Paginator.ListCampaigns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/paginators.html#listcampaignspaginator)
        """
