"""
Type annotations for pinpoint service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_pinpoint import PinpointClient

    client: PinpointClient = boto3.client("pinpoint")
    ```
"""
from datetime import datetime
from typing import Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    ADMChannelRequestTypeDef,
    APNSChannelRequestTypeDef,
    APNSSandboxChannelRequestTypeDef,
    APNSVoipChannelRequestTypeDef,
    APNSVoipSandboxChannelRequestTypeDef,
    BaiduChannelRequestTypeDef,
    CreateApplicationRequestTypeDef,
    CreateAppResponseTypeDef,
    CreateCampaignResponseTypeDef,
    CreateEmailTemplateResponseTypeDef,
    CreateExportJobResponseTypeDef,
    CreateImportJobResponseTypeDef,
    CreateInAppTemplateResponseTypeDef,
    CreateJourneyResponseTypeDef,
    CreatePushTemplateResponseTypeDef,
    CreateRecommenderConfigurationResponseTypeDef,
    CreateRecommenderConfigurationTypeDef,
    CreateSegmentResponseTypeDef,
    CreateSmsTemplateResponseTypeDef,
    CreateVoiceTemplateResponseTypeDef,
    DeleteAdmChannelResponseTypeDef,
    DeleteApnsChannelResponseTypeDef,
    DeleteApnsSandboxChannelResponseTypeDef,
    DeleteApnsVoipChannelResponseTypeDef,
    DeleteApnsVoipSandboxChannelResponseTypeDef,
    DeleteAppResponseTypeDef,
    DeleteBaiduChannelResponseTypeDef,
    DeleteCampaignResponseTypeDef,
    DeleteEmailChannelResponseTypeDef,
    DeleteEmailTemplateResponseTypeDef,
    DeleteEndpointResponseTypeDef,
    DeleteEventStreamResponseTypeDef,
    DeleteGcmChannelResponseTypeDef,
    DeleteInAppTemplateResponseTypeDef,
    DeleteJourneyResponseTypeDef,
    DeletePushTemplateResponseTypeDef,
    DeleteRecommenderConfigurationResponseTypeDef,
    DeleteSegmentResponseTypeDef,
    DeleteSmsChannelResponseTypeDef,
    DeleteSmsTemplateResponseTypeDef,
    DeleteUserEndpointsResponseTypeDef,
    DeleteVoiceChannelResponseTypeDef,
    DeleteVoiceTemplateResponseTypeDef,
    EmailChannelRequestTypeDef,
    EmailTemplateRequestTypeDef,
    EndpointBatchRequestTypeDef,
    EndpointRequestTypeDef,
    EventsRequestTypeDef,
    ExportJobRequestTypeDef,
    GCMChannelRequestTypeDef,
    GetAdmChannelResponseTypeDef,
    GetApnsChannelResponseTypeDef,
    GetApnsSandboxChannelResponseTypeDef,
    GetApnsVoipChannelResponseTypeDef,
    GetApnsVoipSandboxChannelResponseTypeDef,
    GetApplicationDateRangeKpiResponseTypeDef,
    GetApplicationSettingsResponseTypeDef,
    GetAppResponseTypeDef,
    GetAppsResponseTypeDef,
    GetBaiduChannelResponseTypeDef,
    GetCampaignActivitiesResponseTypeDef,
    GetCampaignDateRangeKpiResponseTypeDef,
    GetCampaignResponseTypeDef,
    GetCampaignsResponseTypeDef,
    GetCampaignVersionResponseTypeDef,
    GetCampaignVersionsResponseTypeDef,
    GetChannelsResponseTypeDef,
    GetEmailChannelResponseTypeDef,
    GetEmailTemplateResponseTypeDef,
    GetEndpointResponseTypeDef,
    GetEventStreamResponseTypeDef,
    GetExportJobResponseTypeDef,
    GetExportJobsResponseTypeDef,
    GetGcmChannelResponseTypeDef,
    GetImportJobResponseTypeDef,
    GetImportJobsResponseTypeDef,
    GetInAppMessagesResponseTypeDef,
    GetInAppTemplateResponseTypeDef,
    GetJourneyDateRangeKpiResponseTypeDef,
    GetJourneyExecutionActivityMetricsResponseTypeDef,
    GetJourneyExecutionMetricsResponseTypeDef,
    GetJourneyResponseTypeDef,
    GetPushTemplateResponseTypeDef,
    GetRecommenderConfigurationResponseTypeDef,
    GetRecommenderConfigurationsResponseTypeDef,
    GetSegmentExportJobsResponseTypeDef,
    GetSegmentImportJobsResponseTypeDef,
    GetSegmentResponseTypeDef,
    GetSegmentsResponseTypeDef,
    GetSegmentVersionResponseTypeDef,
    GetSegmentVersionsResponseTypeDef,
    GetSmsChannelResponseTypeDef,
    GetSmsTemplateResponseTypeDef,
    GetUserEndpointsResponseTypeDef,
    GetVoiceChannelResponseTypeDef,
    GetVoiceTemplateResponseTypeDef,
    ImportJobRequestTypeDef,
    InAppTemplateRequestTypeDef,
    JourneyStateRequestTypeDef,
    ListJourneysResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTemplatesResponseTypeDef,
    ListTemplateVersionsResponseTypeDef,
    MessageRequestTypeDef,
    NumberValidateRequestTypeDef,
    PhoneNumberValidateResponseTypeDef,
    PushNotificationTemplateRequestTypeDef,
    PutEventsResponseTypeDef,
    PutEventStreamResponseTypeDef,
    RemoveAttributesResponseTypeDef,
    SendMessagesResponseTypeDef,
    SendOTPMessageRequestParametersTypeDef,
    SendOTPMessageResponseTypeDef,
    SendUsersMessageRequestTypeDef,
    SendUsersMessagesResponseTypeDef,
    SMSChannelRequestTypeDef,
    SMSTemplateRequestTypeDef,
    TagsModelTypeDef,
    TemplateActiveVersionRequestTypeDef,
    UpdateAdmChannelResponseTypeDef,
    UpdateApnsChannelResponseTypeDef,
    UpdateApnsSandboxChannelResponseTypeDef,
    UpdateApnsVoipChannelResponseTypeDef,
    UpdateApnsVoipSandboxChannelResponseTypeDef,
    UpdateApplicationSettingsResponseTypeDef,
    UpdateAttributesRequestTypeDef,
    UpdateBaiduChannelResponseTypeDef,
    UpdateCampaignResponseTypeDef,
    UpdateEmailChannelResponseTypeDef,
    UpdateEmailTemplateResponseTypeDef,
    UpdateEndpointResponseTypeDef,
    UpdateEndpointsBatchResponseTypeDef,
    UpdateGcmChannelResponseTypeDef,
    UpdateInAppTemplateResponseTypeDef,
    UpdateJourneyResponseTypeDef,
    UpdateJourneyStateResponseTypeDef,
    UpdatePushTemplateResponseTypeDef,
    UpdateRecommenderConfigurationResponseTypeDef,
    UpdateRecommenderConfigurationTypeDef,
    UpdateSegmentResponseTypeDef,
    UpdateSmsChannelResponseTypeDef,
    UpdateSmsTemplateResponseTypeDef,
    UpdateTemplateActiveVersionResponseTypeDef,
    UpdateVoiceChannelResponseTypeDef,
    UpdateVoiceTemplateResponseTypeDef,
    VerifyOTPMessageRequestParametersTypeDef,
    VerifyOTPMessageResponseTypeDef,
    VoiceChannelRequestTypeDef,
    VoiceTemplateRequestTypeDef,
    WriteApplicationSettingsRequestTypeDef,
    WriteCampaignRequestTypeDef,
    WriteEventStreamTypeDef,
    WriteJourneyRequestTypeDef,
    WriteSegmentRequestTypeDef,
)

__all__ = ("PinpointClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    MethodNotAllowedException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    PayloadTooLargeException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]

class PinpointClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PinpointClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#close)
        """
    def create_app(
        self, *, CreateApplicationRequest: "CreateApplicationRequestTypeDef"
    ) -> CreateAppResponseTypeDef:
        """
        Creates an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.create_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#create_app)
        """
    def create_campaign(
        self, *, ApplicationId: str, WriteCampaignRequest: "WriteCampaignRequestTypeDef"
    ) -> CreateCampaignResponseTypeDef:
        """
        Creates a new campaign for an application or updates the settings of an existing
        campaign for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.create_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#create_campaign)
        """
    def create_email_template(
        self, *, EmailTemplateRequest: "EmailTemplateRequestTypeDef", TemplateName: str
    ) -> CreateEmailTemplateResponseTypeDef:
        """
        Creates a message template for messages that are sent through the email channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.create_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#create_email_template)
        """
    def create_export_job(
        self, *, ApplicationId: str, ExportJobRequest: "ExportJobRequestTypeDef"
    ) -> CreateExportJobResponseTypeDef:
        """
        Creates an export job for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.create_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#create_export_job)
        """
    def create_import_job(
        self, *, ApplicationId: str, ImportJobRequest: "ImportJobRequestTypeDef"
    ) -> CreateImportJobResponseTypeDef:
        """
        Creates an import job for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.create_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#create_import_job)
        """
    def create_in_app_template(
        self, *, InAppTemplateRequest: "InAppTemplateRequestTypeDef", TemplateName: str
    ) -> CreateInAppTemplateResponseTypeDef:
        """
        Creates a new message template for messages using the in-app message channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.create_in_app_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#create_in_app_template)
        """
    def create_journey(
        self, *, ApplicationId: str, WriteJourneyRequest: "WriteJourneyRequestTypeDef"
    ) -> CreateJourneyResponseTypeDef:
        """
        Creates a journey for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.create_journey)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#create_journey)
        """
    def create_push_template(
        self,
        *,
        PushNotificationTemplateRequest: "PushNotificationTemplateRequestTypeDef",
        TemplateName: str
    ) -> CreatePushTemplateResponseTypeDef:
        """
        Creates a message template for messages that are sent through a push
        notification channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.create_push_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#create_push_template)
        """
    def create_recommender_configuration(
        self, *, CreateRecommenderConfiguration: "CreateRecommenderConfigurationTypeDef"
    ) -> CreateRecommenderConfigurationResponseTypeDef:
        """
        Creates an Amazon Pinpoint configuration for a recommender model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.create_recommender_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#create_recommender_configuration)
        """
    def create_segment(
        self, *, ApplicationId: str, WriteSegmentRequest: "WriteSegmentRequestTypeDef"
    ) -> CreateSegmentResponseTypeDef:
        """
        Creates a new segment for an application or updates the configuration,
        dimension, and other settings for an existing segment that's associated with an
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.create_segment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#create_segment)
        """
    def create_sms_template(
        self, *, SMSTemplateRequest: "SMSTemplateRequestTypeDef", TemplateName: str
    ) -> CreateSmsTemplateResponseTypeDef:
        """
        Creates a message template for messages that are sent through the SMS channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.create_sms_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#create_sms_template)
        """
    def create_voice_template(
        self, *, TemplateName: str, VoiceTemplateRequest: "VoiceTemplateRequestTypeDef"
    ) -> CreateVoiceTemplateResponseTypeDef:
        """
        Creates a message template for messages that are sent through the voice channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.create_voice_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#create_voice_template)
        """
    def delete_adm_channel(self, *, ApplicationId: str) -> DeleteAdmChannelResponseTypeDef:
        """
        Disables the ADM channel for an application and deletes any existing settings
        for the channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.delete_adm_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_adm_channel)
        """
    def delete_apns_channel(self, *, ApplicationId: str) -> DeleteApnsChannelResponseTypeDef:
        """
        Disables the APNs channel for an application and deletes any existing settings
        for the channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.delete_apns_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_apns_channel)
        """
    def delete_apns_sandbox_channel(
        self, *, ApplicationId: str
    ) -> DeleteApnsSandboxChannelResponseTypeDef:
        """
        Disables the APNs sandbox channel for an application and deletes any existing
        settings for the channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.delete_apns_sandbox_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_apns_sandbox_channel)
        """
    def delete_apns_voip_channel(
        self, *, ApplicationId: str
    ) -> DeleteApnsVoipChannelResponseTypeDef:
        """
        Disables the APNs VoIP channel for an application and deletes any existing
        settings for the channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.delete_apns_voip_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_apns_voip_channel)
        """
    def delete_apns_voip_sandbox_channel(
        self, *, ApplicationId: str
    ) -> DeleteApnsVoipSandboxChannelResponseTypeDef:
        """
        Disables the APNs VoIP sandbox channel for an application and deletes any
        existing settings for the channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.delete_apns_voip_sandbox_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_apns_voip_sandbox_channel)
        """
    def delete_app(self, *, ApplicationId: str) -> DeleteAppResponseTypeDef:
        """
        Deletes an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.delete_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_app)
        """
    def delete_baidu_channel(self, *, ApplicationId: str) -> DeleteBaiduChannelResponseTypeDef:
        """
        Disables the Baidu channel for an application and deletes any existing settings
        for the channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.delete_baidu_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_baidu_channel)
        """
    def delete_campaign(
        self, *, ApplicationId: str, CampaignId: str
    ) -> DeleteCampaignResponseTypeDef:
        """
        Deletes a campaign from an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.delete_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_campaign)
        """
    def delete_email_channel(self, *, ApplicationId: str) -> DeleteEmailChannelResponseTypeDef:
        """
        Disables the email channel for an application and deletes any existing settings
        for the channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.delete_email_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_email_channel)
        """
    def delete_email_template(
        self, *, TemplateName: str, Version: str = None
    ) -> DeleteEmailTemplateResponseTypeDef:
        """
        Deletes a message template for messages that were sent through the email
        channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.delete_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_email_template)
        """
    def delete_endpoint(
        self, *, ApplicationId: str, EndpointId: str
    ) -> DeleteEndpointResponseTypeDef:
        """
        Deletes an endpoint from an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.delete_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_endpoint)
        """
    def delete_event_stream(self, *, ApplicationId: str) -> DeleteEventStreamResponseTypeDef:
        """
        Deletes the event stream for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.delete_event_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_event_stream)
        """
    def delete_gcm_channel(self, *, ApplicationId: str) -> DeleteGcmChannelResponseTypeDef:
        """
        Disables the GCM channel for an application and deletes any existing settings
        for the channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.delete_gcm_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_gcm_channel)
        """
    def delete_in_app_template(
        self, *, TemplateName: str, Version: str = None
    ) -> DeleteInAppTemplateResponseTypeDef:
        """
        Deletes a message template for messages sent using the in-app message channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.delete_in_app_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_in_app_template)
        """
    def delete_journey(self, *, ApplicationId: str, JourneyId: str) -> DeleteJourneyResponseTypeDef:
        """
        Deletes a journey from an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.delete_journey)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_journey)
        """
    def delete_push_template(
        self, *, TemplateName: str, Version: str = None
    ) -> DeletePushTemplateResponseTypeDef:
        """
        Deletes a message template for messages that were sent through a push
        notification channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.delete_push_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_push_template)
        """
    def delete_recommender_configuration(
        self, *, RecommenderId: str
    ) -> DeleteRecommenderConfigurationResponseTypeDef:
        """
        Deletes an Amazon Pinpoint configuration for a recommender model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.delete_recommender_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_recommender_configuration)
        """
    def delete_segment(self, *, ApplicationId: str, SegmentId: str) -> DeleteSegmentResponseTypeDef:
        """
        Deletes a segment from an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.delete_segment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_segment)
        """
    def delete_sms_channel(self, *, ApplicationId: str) -> DeleteSmsChannelResponseTypeDef:
        """
        Disables the SMS channel for an application and deletes any existing settings
        for the channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.delete_sms_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_sms_channel)
        """
    def delete_sms_template(
        self, *, TemplateName: str, Version: str = None
    ) -> DeleteSmsTemplateResponseTypeDef:
        """
        Deletes a message template for messages that were sent through the SMS channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.delete_sms_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_sms_template)
        """
    def delete_user_endpoints(
        self, *, ApplicationId: str, UserId: str
    ) -> DeleteUserEndpointsResponseTypeDef:
        """
        Deletes all the endpoints that are associated with a specific user ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.delete_user_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_user_endpoints)
        """
    def delete_voice_channel(self, *, ApplicationId: str) -> DeleteVoiceChannelResponseTypeDef:
        """
        Disables the voice channel for an application and deletes any existing settings
        for the channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.delete_voice_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_voice_channel)
        """
    def delete_voice_template(
        self, *, TemplateName: str, Version: str = None
    ) -> DeleteVoiceTemplateResponseTypeDef:
        """
        Deletes a message template for messages that were sent through the voice
        channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.delete_voice_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_voice_template)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#generate_presigned_url)
        """
    def get_adm_channel(self, *, ApplicationId: str) -> GetAdmChannelResponseTypeDef:
        """
        Retrieves information about the status and settings of the ADM channel for an
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_adm_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_adm_channel)
        """
    def get_apns_channel(self, *, ApplicationId: str) -> GetApnsChannelResponseTypeDef:
        """
        Retrieves information about the status and settings of the APNs channel for an
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_apns_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_apns_channel)
        """
    def get_apns_sandbox_channel(
        self, *, ApplicationId: str
    ) -> GetApnsSandboxChannelResponseTypeDef:
        """
        Retrieves information about the status and settings of the APNs sandbox channel
        for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_apns_sandbox_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_apns_sandbox_channel)
        """
    def get_apns_voip_channel(self, *, ApplicationId: str) -> GetApnsVoipChannelResponseTypeDef:
        """
        Retrieves information about the status and settings of the APNs VoIP channel for
        an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_apns_voip_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_apns_voip_channel)
        """
    def get_apns_voip_sandbox_channel(
        self, *, ApplicationId: str
    ) -> GetApnsVoipSandboxChannelResponseTypeDef:
        """
        Retrieves information about the status and settings of the APNs VoIP sandbox
        channel for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_apns_voip_sandbox_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_apns_voip_sandbox_channel)
        """
    def get_app(self, *, ApplicationId: str) -> GetAppResponseTypeDef:
        """
        Retrieves information about an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_app)
        """
    def get_application_date_range_kpi(
        self,
        *,
        ApplicationId: str,
        KpiName: str,
        EndTime: Union[datetime, str] = None,
        NextToken: str = None,
        PageSize: str = None,
        StartTime: Union[datetime, str] = None
    ) -> GetApplicationDateRangeKpiResponseTypeDef:
        """
        Retrieves (queries) pre-aggregated data for a standard metric that applies to an
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_application_date_range_kpi)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_application_date_range_kpi)
        """
    def get_application_settings(
        self, *, ApplicationId: str
    ) -> GetApplicationSettingsResponseTypeDef:
        """
        Retrieves information about the settings for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_application_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_application_settings)
        """
    def get_apps(self, *, PageSize: str = None, Token: str = None) -> GetAppsResponseTypeDef:
        """
        Retrieves information about all the applications that are associated with your
        Amazon Pinpoint account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_apps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_apps)
        """
    def get_baidu_channel(self, *, ApplicationId: str) -> GetBaiduChannelResponseTypeDef:
        """
        Retrieves information about the status and settings of the Baidu channel for an
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_baidu_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_baidu_channel)
        """
    def get_campaign(self, *, ApplicationId: str, CampaignId: str) -> GetCampaignResponseTypeDef:
        """
        Retrieves information about the status, configuration, and other settings for a
        campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_campaign)
        """
    def get_campaign_activities(
        self, *, ApplicationId: str, CampaignId: str, PageSize: str = None, Token: str = None
    ) -> GetCampaignActivitiesResponseTypeDef:
        """
        Retrieves information about all the activities for a campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_campaign_activities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_campaign_activities)
        """
    def get_campaign_date_range_kpi(
        self,
        *,
        ApplicationId: str,
        CampaignId: str,
        KpiName: str,
        EndTime: Union[datetime, str] = None,
        NextToken: str = None,
        PageSize: str = None,
        StartTime: Union[datetime, str] = None
    ) -> GetCampaignDateRangeKpiResponseTypeDef:
        """
        Retrieves (queries) pre-aggregated data for a standard metric that applies to a
        campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_campaign_date_range_kpi)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_campaign_date_range_kpi)
        """
    def get_campaign_version(
        self, *, ApplicationId: str, CampaignId: str, Version: str
    ) -> GetCampaignVersionResponseTypeDef:
        """
        Retrieves information about the status, configuration, and other settings for a
        specific version of a campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_campaign_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_campaign_version)
        """
    def get_campaign_versions(
        self, *, ApplicationId: str, CampaignId: str, PageSize: str = None, Token: str = None
    ) -> GetCampaignVersionsResponseTypeDef:
        """
        Retrieves information about the status, configuration, and other settings for
        all versions of a campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_campaign_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_campaign_versions)
        """
    def get_campaigns(
        self, *, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> GetCampaignsResponseTypeDef:
        """
        Retrieves information about the status, configuration, and other settings for
        all the campaigns that are associated with an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_campaigns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_campaigns)
        """
    def get_channels(self, *, ApplicationId: str) -> GetChannelsResponseTypeDef:
        """
        Retrieves information about the history and status of each channel for an
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_channels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_channels)
        """
    def get_email_channel(self, *, ApplicationId: str) -> GetEmailChannelResponseTypeDef:
        """
        Retrieves information about the status and settings of the email channel for an
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_email_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_email_channel)
        """
    def get_email_template(
        self, *, TemplateName: str, Version: str = None
    ) -> GetEmailTemplateResponseTypeDef:
        """
        Retrieves the content and settings of a message template for messages that are
        sent through the email channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_email_template)
        """
    def get_endpoint(self, *, ApplicationId: str, EndpointId: str) -> GetEndpointResponseTypeDef:
        """
        Retrieves information about the settings and attributes of a specific endpoint
        for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_endpoint)
        """
    def get_event_stream(self, *, ApplicationId: str) -> GetEventStreamResponseTypeDef:
        """
        Retrieves information about the event stream settings for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_event_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_event_stream)
        """
    def get_export_job(self, *, ApplicationId: str, JobId: str) -> GetExportJobResponseTypeDef:
        """
        Retrieves information about the status and settings of a specific export job for
        an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_export_job)
        """
    def get_export_jobs(
        self, *, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> GetExportJobsResponseTypeDef:
        """
        Retrieves information about the status and settings of all the export jobs for
        an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_export_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_export_jobs)
        """
    def get_gcm_channel(self, *, ApplicationId: str) -> GetGcmChannelResponseTypeDef:
        """
        Retrieves information about the status and settings of the GCM channel for an
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_gcm_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_gcm_channel)
        """
    def get_import_job(self, *, ApplicationId: str, JobId: str) -> GetImportJobResponseTypeDef:
        """
        Retrieves information about the status and settings of a specific import job for
        an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_import_job)
        """
    def get_import_jobs(
        self, *, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> GetImportJobsResponseTypeDef:
        """
        Retrieves information about the status and settings of all the import jobs for
        an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_import_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_import_jobs)
        """
    def get_in_app_messages(
        self, *, ApplicationId: str, EndpointId: str
    ) -> GetInAppMessagesResponseTypeDef:
        """
        Retrieves the in-app messages targeted for the provided endpoint ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_in_app_messages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_in_app_messages)
        """
    def get_in_app_template(
        self, *, TemplateName: str, Version: str = None
    ) -> GetInAppTemplateResponseTypeDef:
        """
        Retrieves the content and settings of a message template for messages sent
        through the in-app channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_in_app_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_in_app_template)
        """
    def get_journey(self, *, ApplicationId: str, JourneyId: str) -> GetJourneyResponseTypeDef:
        """
        Retrieves information about the status, configuration, and other settings for a
        journey.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_journey)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_journey)
        """
    def get_journey_date_range_kpi(
        self,
        *,
        ApplicationId: str,
        JourneyId: str,
        KpiName: str,
        EndTime: Union[datetime, str] = None,
        NextToken: str = None,
        PageSize: str = None,
        StartTime: Union[datetime, str] = None
    ) -> GetJourneyDateRangeKpiResponseTypeDef:
        """
        Retrieves (queries) pre-aggregated data for a standard engagement metric that
        applies to a journey.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_journey_date_range_kpi)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_journey_date_range_kpi)
        """
    def get_journey_execution_activity_metrics(
        self,
        *,
        ApplicationId: str,
        JourneyActivityId: str,
        JourneyId: str,
        NextToken: str = None,
        PageSize: str = None
    ) -> GetJourneyExecutionActivityMetricsResponseTypeDef:
        """
        Retrieves (queries) pre-aggregated data for a standard execution metric that
        applies to a journey activity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_journey_execution_activity_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_journey_execution_activity_metrics)
        """
    def get_journey_execution_metrics(
        self, *, ApplicationId: str, JourneyId: str, NextToken: str = None, PageSize: str = None
    ) -> GetJourneyExecutionMetricsResponseTypeDef:
        """
        Retrieves (queries) pre-aggregated data for a standard execution metric that
        applies to a journey.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_journey_execution_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_journey_execution_metrics)
        """
    def get_push_template(
        self, *, TemplateName: str, Version: str = None
    ) -> GetPushTemplateResponseTypeDef:
        """
        Retrieves the content and settings of a message template for messages that are
        sent through a push notification channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_push_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_push_template)
        """
    def get_recommender_configuration(
        self, *, RecommenderId: str
    ) -> GetRecommenderConfigurationResponseTypeDef:
        """
        Retrieves information about an Amazon Pinpoint configuration for a recommender
        model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_recommender_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_recommender_configuration)
        """
    def get_recommender_configurations(
        self, *, PageSize: str = None, Token: str = None
    ) -> GetRecommenderConfigurationsResponseTypeDef:
        """
        Retrieves information about all the recommender model configurations that are
        associated with your Amazon Pinpoint account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_recommender_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_recommender_configurations)
        """
    def get_segment(self, *, ApplicationId: str, SegmentId: str) -> GetSegmentResponseTypeDef:
        """
        Retrieves information about the configuration, dimension, and other settings for
        a specific segment that's associated with an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_segment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_segment)
        """
    def get_segment_export_jobs(
        self, *, ApplicationId: str, SegmentId: str, PageSize: str = None, Token: str = None
    ) -> GetSegmentExportJobsResponseTypeDef:
        """
        Retrieves information about the status and settings of the export jobs for a
        segment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_segment_export_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_segment_export_jobs)
        """
    def get_segment_import_jobs(
        self, *, ApplicationId: str, SegmentId: str, PageSize: str = None, Token: str = None
    ) -> GetSegmentImportJobsResponseTypeDef:
        """
        Retrieves information about the status and settings of the import jobs for a
        segment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_segment_import_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_segment_import_jobs)
        """
    def get_segment_version(
        self, *, ApplicationId: str, SegmentId: str, Version: str
    ) -> GetSegmentVersionResponseTypeDef:
        """
        Retrieves information about the configuration, dimension, and other settings for
        a specific version of a segment that's associated with an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_segment_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_segment_version)
        """
    def get_segment_versions(
        self, *, ApplicationId: str, SegmentId: str, PageSize: str = None, Token: str = None
    ) -> GetSegmentVersionsResponseTypeDef:
        """
        Retrieves information about the configuration, dimension, and other settings for
        all the versions of a specific segment that's associated with an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_segment_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_segment_versions)
        """
    def get_segments(
        self, *, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> GetSegmentsResponseTypeDef:
        """
        Retrieves information about the configuration, dimension, and other settings for
        all the segments that are associated with an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_segments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_segments)
        """
    def get_sms_channel(self, *, ApplicationId: str) -> GetSmsChannelResponseTypeDef:
        """
        Retrieves information about the status and settings of the SMS channel for an
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_sms_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_sms_channel)
        """
    def get_sms_template(
        self, *, TemplateName: str, Version: str = None
    ) -> GetSmsTemplateResponseTypeDef:
        """
        Retrieves the content and settings of a message template for messages that are
        sent through the SMS channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_sms_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_sms_template)
        """
    def get_user_endpoints(
        self, *, ApplicationId: str, UserId: str
    ) -> GetUserEndpointsResponseTypeDef:
        """
        Retrieves information about all the endpoints that are associated with a
        specific user ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_user_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_user_endpoints)
        """
    def get_voice_channel(self, *, ApplicationId: str) -> GetVoiceChannelResponseTypeDef:
        """
        Retrieves information about the status and settings of the voice channel for an
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_voice_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_voice_channel)
        """
    def get_voice_template(
        self, *, TemplateName: str, Version: str = None
    ) -> GetVoiceTemplateResponseTypeDef:
        """
        Retrieves the content and settings of a message template for messages that are
        sent through the voice channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.get_voice_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_voice_template)
        """
    def list_journeys(
        self, *, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> ListJourneysResponseTypeDef:
        """
        Retrieves information about the status, configuration, and other settings for
        all the journeys that are associated with an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.list_journeys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#list_journeys)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves all the tags (keys and values) that are associated with an
        application, campaign, message template, or segment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#list_tags_for_resource)
        """
    def list_template_versions(
        self, *, TemplateName: str, TemplateType: str, NextToken: str = None, PageSize: str = None
    ) -> ListTemplateVersionsResponseTypeDef:
        """
        Retrieves information about all the versions of a specific message template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.list_template_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#list_template_versions)
        """
    def list_templates(
        self,
        *,
        NextToken: str = None,
        PageSize: str = None,
        Prefix: str = None,
        TemplateType: str = None
    ) -> ListTemplatesResponseTypeDef:
        """
        Retrieves information about all the message templates that are associated with
        your Amazon Pinpoint account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.list_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#list_templates)
        """
    def phone_number_validate(
        self, *, NumberValidateRequest: "NumberValidateRequestTypeDef"
    ) -> PhoneNumberValidateResponseTypeDef:
        """
        Retrieves information about a phone number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.phone_number_validate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#phone_number_validate)
        """
    def put_event_stream(
        self, *, ApplicationId: str, WriteEventStream: "WriteEventStreamTypeDef"
    ) -> PutEventStreamResponseTypeDef:
        """
        Creates a new event stream for an application or updates the settings of an
        existing event stream for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.put_event_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#put_event_stream)
        """
    def put_events(
        self, *, ApplicationId: str, EventsRequest: "EventsRequestTypeDef"
    ) -> PutEventsResponseTypeDef:
        """
        Creates a new event to record for endpoints, or creates or updates endpoint data
        that existing events are associated with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.put_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#put_events)
        """
    def remove_attributes(
        self,
        *,
        ApplicationId: str,
        AttributeType: str,
        UpdateAttributesRequest: "UpdateAttributesRequestTypeDef"
    ) -> RemoveAttributesResponseTypeDef:
        """
        Removes one or more attributes, of the same attribute type, from all the
        endpoints that are associated with an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.remove_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#remove_attributes)
        """
    def send_messages(
        self, *, ApplicationId: str, MessageRequest: "MessageRequestTypeDef"
    ) -> SendMessagesResponseTypeDef:
        """
        Creates and sends a direct message.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.send_messages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#send_messages)
        """
    def send_otp_message(
        self,
        *,
        ApplicationId: str,
        SendOTPMessageRequestParameters: "SendOTPMessageRequestParametersTypeDef"
    ) -> SendOTPMessageResponseTypeDef:
        """
        Send an OTP message See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-2016-12-01/SendOTPMessage>`_
        **Request Syntax** response = client.send_otp_message( ApplicationId='string',
        SendOTPMessageRequestParameters={ 'AllowedAttempts':...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.send_otp_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#send_otp_message)
        """
    def send_users_messages(
        self, *, ApplicationId: str, SendUsersMessageRequest: "SendUsersMessageRequestTypeDef"
    ) -> SendUsersMessagesResponseTypeDef:
        """
        Creates and sends a message to a list of users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.send_users_messages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#send_users_messages)
        """
    def tag_resource(self, *, ResourceArn: str, TagsModel: "TagsModelTypeDef") -> None:
        """
        Adds one or more tags (keys and values) to an application, campaign, message
        template, or segment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        Removes one or more tags (keys and values) from an application, campaign,
        message template, or segment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#untag_resource)
        """
    def update_adm_channel(
        self, *, ADMChannelRequest: "ADMChannelRequestTypeDef", ApplicationId: str
    ) -> UpdateAdmChannelResponseTypeDef:
        """
        Enables the ADM channel for an application or updates the status and settings of
        the ADM channel for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.update_adm_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_adm_channel)
        """
    def update_apns_channel(
        self, *, APNSChannelRequest: "APNSChannelRequestTypeDef", ApplicationId: str
    ) -> UpdateApnsChannelResponseTypeDef:
        """
        Enables the APNs channel for an application or updates the status and settings
        of the APNs channel for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.update_apns_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_apns_channel)
        """
    def update_apns_sandbox_channel(
        self, *, APNSSandboxChannelRequest: "APNSSandboxChannelRequestTypeDef", ApplicationId: str
    ) -> UpdateApnsSandboxChannelResponseTypeDef:
        """
        Enables the APNs sandbox channel for an application or updates the status and
        settings of the APNs sandbox channel for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.update_apns_sandbox_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_apns_sandbox_channel)
        """
    def update_apns_voip_channel(
        self, *, APNSVoipChannelRequest: "APNSVoipChannelRequestTypeDef", ApplicationId: str
    ) -> UpdateApnsVoipChannelResponseTypeDef:
        """
        Enables the APNs VoIP channel for an application or updates the status and
        settings of the APNs VoIP channel for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.update_apns_voip_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_apns_voip_channel)
        """
    def update_apns_voip_sandbox_channel(
        self,
        *,
        APNSVoipSandboxChannelRequest: "APNSVoipSandboxChannelRequestTypeDef",
        ApplicationId: str
    ) -> UpdateApnsVoipSandboxChannelResponseTypeDef:
        """
        Enables the APNs VoIP sandbox channel for an application or updates the status
        and settings of the APNs VoIP sandbox channel for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.update_apns_voip_sandbox_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_apns_voip_sandbox_channel)
        """
    def update_application_settings(
        self,
        *,
        ApplicationId: str,
        WriteApplicationSettingsRequest: "WriteApplicationSettingsRequestTypeDef"
    ) -> UpdateApplicationSettingsResponseTypeDef:
        """
        Updates the settings for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.update_application_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_application_settings)
        """
    def update_baidu_channel(
        self, *, ApplicationId: str, BaiduChannelRequest: "BaiduChannelRequestTypeDef"
    ) -> UpdateBaiduChannelResponseTypeDef:
        """
        Enables the Baidu channel for an application or updates the status and settings
        of the Baidu channel for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.update_baidu_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_baidu_channel)
        """
    def update_campaign(
        self,
        *,
        ApplicationId: str,
        CampaignId: str,
        WriteCampaignRequest: "WriteCampaignRequestTypeDef"
    ) -> UpdateCampaignResponseTypeDef:
        """
        Updates the configuration and other settings for a campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.update_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_campaign)
        """
    def update_email_channel(
        self, *, ApplicationId: str, EmailChannelRequest: "EmailChannelRequestTypeDef"
    ) -> UpdateEmailChannelResponseTypeDef:
        """
        Enables the email channel for an application or updates the status and settings
        of the email channel for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.update_email_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_email_channel)
        """
    def update_email_template(
        self,
        *,
        EmailTemplateRequest: "EmailTemplateRequestTypeDef",
        TemplateName: str,
        CreateNewVersion: bool = None,
        Version: str = None
    ) -> UpdateEmailTemplateResponseTypeDef:
        """
        Updates an existing message template for messages that are sent through the
        email channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.update_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_email_template)
        """
    def update_endpoint(
        self, *, ApplicationId: str, EndpointId: str, EndpointRequest: "EndpointRequestTypeDef"
    ) -> UpdateEndpointResponseTypeDef:
        """
        Creates a new endpoint for an application or updates the settings and attributes
        of an existing endpoint for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.update_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_endpoint)
        """
    def update_endpoints_batch(
        self, *, ApplicationId: str, EndpointBatchRequest: "EndpointBatchRequestTypeDef"
    ) -> UpdateEndpointsBatchResponseTypeDef:
        """
        Creates a new batch of endpoints for an application or updates the settings and
        attributes of a batch of existing endpoints for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.update_endpoints_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_endpoints_batch)
        """
    def update_gcm_channel(
        self, *, ApplicationId: str, GCMChannelRequest: "GCMChannelRequestTypeDef"
    ) -> UpdateGcmChannelResponseTypeDef:
        """
        Enables the GCM channel for an application or updates the status and settings of
        the GCM channel for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.update_gcm_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_gcm_channel)
        """
    def update_in_app_template(
        self,
        *,
        InAppTemplateRequest: "InAppTemplateRequestTypeDef",
        TemplateName: str,
        CreateNewVersion: bool = None,
        Version: str = None
    ) -> UpdateInAppTemplateResponseTypeDef:
        """
        Updates an existing message template for messages sent through the in-app
        message channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.update_in_app_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_in_app_template)
        """
    def update_journey(
        self,
        *,
        ApplicationId: str,
        JourneyId: str,
        WriteJourneyRequest: "WriteJourneyRequestTypeDef"
    ) -> UpdateJourneyResponseTypeDef:
        """
        Updates the configuration and other settings for a journey.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.update_journey)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_journey)
        """
    def update_journey_state(
        self,
        *,
        ApplicationId: str,
        JourneyId: str,
        JourneyStateRequest: "JourneyStateRequestTypeDef"
    ) -> UpdateJourneyStateResponseTypeDef:
        """
        Cancels (stops) an active journey.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.update_journey_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_journey_state)
        """
    def update_push_template(
        self,
        *,
        PushNotificationTemplateRequest: "PushNotificationTemplateRequestTypeDef",
        TemplateName: str,
        CreateNewVersion: bool = None,
        Version: str = None
    ) -> UpdatePushTemplateResponseTypeDef:
        """
        Updates an existing message template for messages that are sent through a push
        notification channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.update_push_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_push_template)
        """
    def update_recommender_configuration(
        self,
        *,
        RecommenderId: str,
        UpdateRecommenderConfiguration: "UpdateRecommenderConfigurationTypeDef"
    ) -> UpdateRecommenderConfigurationResponseTypeDef:
        """
        Updates an Amazon Pinpoint configuration for a recommender model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.update_recommender_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_recommender_configuration)
        """
    def update_segment(
        self,
        *,
        ApplicationId: str,
        SegmentId: str,
        WriteSegmentRequest: "WriteSegmentRequestTypeDef"
    ) -> UpdateSegmentResponseTypeDef:
        """
        Creates a new segment for an application or updates the configuration,
        dimension, and other settings for an existing segment that's associated with an
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.update_segment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_segment)
        """
    def update_sms_channel(
        self, *, ApplicationId: str, SMSChannelRequest: "SMSChannelRequestTypeDef"
    ) -> UpdateSmsChannelResponseTypeDef:
        """
        Enables the SMS channel for an application or updates the status and settings of
        the SMS channel for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.update_sms_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_sms_channel)
        """
    def update_sms_template(
        self,
        *,
        SMSTemplateRequest: "SMSTemplateRequestTypeDef",
        TemplateName: str,
        CreateNewVersion: bool = None,
        Version: str = None
    ) -> UpdateSmsTemplateResponseTypeDef:
        """
        Updates an existing message template for messages that are sent through the SMS
        channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.update_sms_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_sms_template)
        """
    def update_template_active_version(
        self,
        *,
        TemplateActiveVersionRequest: "TemplateActiveVersionRequestTypeDef",
        TemplateName: str,
        TemplateType: str
    ) -> UpdateTemplateActiveVersionResponseTypeDef:
        """
        Changes the status of a specific version of a message template to *active* .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.update_template_active_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_template_active_version)
        """
    def update_voice_channel(
        self, *, ApplicationId: str, VoiceChannelRequest: "VoiceChannelRequestTypeDef"
    ) -> UpdateVoiceChannelResponseTypeDef:
        """
        Enables the voice channel for an application or updates the status and settings
        of the voice channel for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.update_voice_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_voice_channel)
        """
    def update_voice_template(
        self,
        *,
        TemplateName: str,
        VoiceTemplateRequest: "VoiceTemplateRequestTypeDef",
        CreateNewVersion: bool = None,
        Version: str = None
    ) -> UpdateVoiceTemplateResponseTypeDef:
        """
        Updates an existing message template for messages that are sent through the
        voice channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.update_voice_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_voice_template)
        """
    def verify_otp_message(
        self,
        *,
        ApplicationId: str,
        VerifyOTPMessageRequestParameters: "VerifyOTPMessageRequestParametersTypeDef"
    ) -> VerifyOTPMessageResponseTypeDef:
        """
        Verify an OTP See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-2016-12-01/VerifyOTPMessage>`_
        **Request Syntax** response = client.verify_otp_message( ApplicationId='string',
        VerifyOTPMessageRequestParameters={ 'DestinationIdenti...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/pinpoint.html#Pinpoint.Client.verify_otp_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#verify_otp_message)
        """
