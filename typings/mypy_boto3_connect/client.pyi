"""
Type annotations for connect service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_connect import ConnectClient

    client: ConnectClient = boto3.client("connect")
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AgentAvailabilityTimerType,
    AgentStatusStateType,
    AgentStatusTypeType,
    ContactFlowModuleStateType,
    ContactFlowStateType,
    ContactFlowStatusType,
    ContactFlowTypeType,
    DirectoryTypeType,
    EventSourceNameType,
    GroupingType,
    InstanceAttributeTypeType,
    InstanceStorageResourceTypeType,
    IntegrationTypeType,
    LexVersionType,
    MonitorCapabilityType,
    PhoneNumberCountryCodeType,
    PhoneNumberTypeType,
    QueueStatusType,
    QueueTypeType,
    QuickConnectTypeType,
    RealTimeContactAnalysisOutputTypeType,
    RealTimeContactAnalysisSegmentTypeType,
    ReferenceTypeType,
    RehydrationTypeType,
    RulePublishStatusType,
    SourceTypeType,
    TaskTemplateStatusType,
    TrafficTypeType,
    UseCaseTypeType,
    ViewStatusType,
    ViewTypeType,
    VocabularyLanguageCodeType,
    VocabularyStateType,
)
from .paginator import (
    GetMetricDataPaginator,
    ListAgentStatusesPaginator,
    ListApprovedOriginsPaginator,
    ListAuthenticationProfilesPaginator,
    ListBotsPaginator,
    ListContactEvaluationsPaginator,
    ListContactFlowModulesPaginator,
    ListContactFlowsPaginator,
    ListContactReferencesPaginator,
    ListDefaultVocabulariesPaginator,
    ListEvaluationFormsPaginator,
    ListEvaluationFormVersionsPaginator,
    ListFlowAssociationsPaginator,
    ListHoursOfOperationsPaginator,
    ListInstanceAttributesPaginator,
    ListInstancesPaginator,
    ListInstanceStorageConfigsPaginator,
    ListIntegrationAssociationsPaginator,
    ListLambdaFunctionsPaginator,
    ListLexBotsPaginator,
    ListPhoneNumbersPaginator,
    ListPhoneNumbersV2Paginator,
    ListPredefinedAttributesPaginator,
    ListPromptsPaginator,
    ListQueueQuickConnectsPaginator,
    ListQueuesPaginator,
    ListQuickConnectsPaginator,
    ListRoutingProfileQueuesPaginator,
    ListRoutingProfilesPaginator,
    ListRulesPaginator,
    ListSecurityKeysPaginator,
    ListSecurityProfileApplicationsPaginator,
    ListSecurityProfilePermissionsPaginator,
    ListSecurityProfilesPaginator,
    ListTaskTemplatesPaginator,
    ListTrafficDistributionGroupsPaginator,
    ListTrafficDistributionGroupUsersPaginator,
    ListUseCasesPaginator,
    ListUserHierarchyGroupsPaginator,
    ListUserProficienciesPaginator,
    ListUsersPaginator,
    ListViewsPaginator,
    ListViewVersionsPaginator,
    SearchAvailablePhoneNumbersPaginator,
    SearchContactFlowModulesPaginator,
    SearchContactFlowsPaginator,
    SearchContactsPaginator,
    SearchHoursOfOperationsPaginator,
    SearchPredefinedAttributesPaginator,
    SearchPromptsPaginator,
    SearchQueuesPaginator,
    SearchQuickConnectsPaginator,
    SearchResourceTagsPaginator,
    SearchRoutingProfilesPaginator,
    SearchSecurityProfilesPaginator,
    SearchUsersPaginator,
    SearchVocabulariesPaginator,
)
from .type_defs import (
    ActivateEvaluationFormResponseTypeDef,
    AgentConfigTypeDef,
    AllowedCapabilitiesTypeDef,
    AnswerMachineDetectionConfigTypeDef,
    ApplicationTypeDef,
    AssociateAnalyticsDataSetResponseTypeDef,
    AssociateInstanceStorageConfigResponseTypeDef,
    AssociateSecurityKeyResponseTypeDef,
    BatchAssociateAnalyticsDataSetResponseTypeDef,
    BatchDisassociateAnalyticsDataSetResponseTypeDef,
    BatchGetAttachedFileMetadataResponseTypeDef,
    BatchGetFlowAssociationResponseTypeDef,
    BatchPutContactResponseTypeDef,
    ChatEventTypeDef,
    ChatMessageTypeDef,
    ChatStreamingConfigurationTypeDef,
    ClaimPhoneNumberResponseTypeDef,
    ContactDataRequestTypeDef,
    ContactFlowModuleSearchCriteriaTypeDef,
    ContactFlowModuleSearchFilterTypeDef,
    ContactFlowSearchCriteriaTypeDef,
    ContactFlowSearchFilterTypeDef,
    CreateAgentStatusResponseTypeDef,
    CreateContactFlowModuleResponseTypeDef,
    CreateContactFlowResponseTypeDef,
    CreatedByInfoTypeDef,
    CreateEvaluationFormResponseTypeDef,
    CreateHoursOfOperationResponseTypeDef,
    CreateInstanceResponseTypeDef,
    CreateIntegrationAssociationResponseTypeDef,
    CreateParticipantResponseTypeDef,
    CreatePersistentContactAssociationResponseTypeDef,
    CreatePromptResponseTypeDef,
    CreateQueueResponseTypeDef,
    CreateQuickConnectResponseTypeDef,
    CreateRoutingProfileResponseTypeDef,
    CreateRuleResponseTypeDef,
    CreateSecurityProfileResponseTypeDef,
    CreateTaskTemplateResponseTypeDef,
    CreateTrafficDistributionGroupResponseTypeDef,
    CreateUseCaseResponseTypeDef,
    CreateUserHierarchyGroupResponseTypeDef,
    CreateUserResponseTypeDef,
    CreateViewResponseTypeDef,
    CreateViewVersionResponseTypeDef,
    CreateVocabularyResponseTypeDef,
    CurrentMetricSortCriteriaTypeDef,
    CurrentMetricTypeDef,
    DeactivateEvaluationFormResponseTypeDef,
    DeleteVocabularyResponseTypeDef,
    DescribeAgentStatusResponseTypeDef,
    DescribeAuthenticationProfileResponseTypeDef,
    DescribeContactEvaluationResponseTypeDef,
    DescribeContactFlowModuleResponseTypeDef,
    DescribeContactFlowResponseTypeDef,
    DescribeContactResponseTypeDef,
    DescribeEvaluationFormResponseTypeDef,
    DescribeHoursOfOperationResponseTypeDef,
    DescribeInstanceAttributeResponseTypeDef,
    DescribeInstanceResponseTypeDef,
    DescribeInstanceStorageConfigResponseTypeDef,
    DescribePhoneNumberResponseTypeDef,
    DescribePredefinedAttributeResponseTypeDef,
    DescribePromptResponseTypeDef,
    DescribeQueueResponseTypeDef,
    DescribeQuickConnectResponseTypeDef,
    DescribeRoutingProfileResponseTypeDef,
    DescribeRuleResponseTypeDef,
    DescribeSecurityProfileResponseTypeDef,
    DescribeTrafficDistributionGroupResponseTypeDef,
    DescribeUserHierarchyGroupResponseTypeDef,
    DescribeUserHierarchyStructureResponseTypeDef,
    DescribeUserResponseTypeDef,
    DescribeViewResponseTypeDef,
    DescribeVocabularyResponseTypeDef,
    DisconnectReasonTypeDef,
    EvaluationAnswerInputTypeDef,
    EvaluationFormItemTypeDef,
    EvaluationFormScoringStrategyTypeDef,
    EvaluationNoteTypeDef,
    FiltersTypeDef,
    FilterV2TypeDef,
    GetAttachedFileResponseTypeDef,
    GetContactAttributesResponseTypeDef,
    GetCurrentMetricDataResponseTypeDef,
    GetCurrentUserDataResponseTypeDef,
    GetFederationTokenResponseTypeDef,
    GetFlowAssociationResponseTypeDef,
    GetMetricDataResponseTypeDef,
    GetMetricDataV2ResponseTypeDef,
    GetPromptFileResponseTypeDef,
    GetTaskTemplateResponseTypeDef,
    GetTrafficDistributionResponseTypeDef,
    HierarchyStructureUpdateTypeDef,
    HistoricalMetricTypeDef,
    HoursOfOperationConfigTypeDef,
    HoursOfOperationSearchCriteriaTypeDef,
    HoursOfOperationSearchFilterTypeDef,
    ImportPhoneNumberResponseTypeDef,
    InstanceStorageConfigTypeDef,
    IntervalDetailsTypeDef,
    LexBotTypeDef,
    LexV2BotTypeDef,
    ListAgentStatusResponseTypeDef,
    ListAnalyticsDataAssociationsResponseTypeDef,
    ListApprovedOriginsResponseTypeDef,
    ListAuthenticationProfilesResponseTypeDef,
    ListBotsResponseTypeDef,
    ListContactEvaluationsResponseTypeDef,
    ListContactFlowModulesResponseTypeDef,
    ListContactFlowsResponseTypeDef,
    ListContactReferencesResponseTypeDef,
    ListDefaultVocabulariesResponseTypeDef,
    ListEvaluationFormsResponseTypeDef,
    ListEvaluationFormVersionsResponseTypeDef,
    ListFlowAssociationsResponseTypeDef,
    ListHoursOfOperationsResponseTypeDef,
    ListInstanceAttributesResponseTypeDef,
    ListInstancesResponseTypeDef,
    ListInstanceStorageConfigsResponseTypeDef,
    ListIntegrationAssociationsResponseTypeDef,
    ListLambdaFunctionsResponseTypeDef,
    ListLexBotsResponseTypeDef,
    ListPhoneNumbersResponseTypeDef,
    ListPhoneNumbersV2ResponseTypeDef,
    ListPredefinedAttributesResponseTypeDef,
    ListPromptsResponseTypeDef,
    ListQueueQuickConnectsResponseTypeDef,
    ListQueuesResponseTypeDef,
    ListQuickConnectsResponseTypeDef,
    ListRealtimeContactAnalysisSegmentsV2ResponseTypeDef,
    ListRoutingProfileQueuesResponseTypeDef,
    ListRoutingProfilesResponseTypeDef,
    ListRulesResponseTypeDef,
    ListSecurityKeysResponseTypeDef,
    ListSecurityProfileApplicationsResponseTypeDef,
    ListSecurityProfilePermissionsResponseTypeDef,
    ListSecurityProfilesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTaskTemplatesResponseTypeDef,
    ListTrafficDistributionGroupsResponseTypeDef,
    ListTrafficDistributionGroupUsersResponseTypeDef,
    ListUseCasesResponseTypeDef,
    ListUserHierarchyGroupsResponseTypeDef,
    ListUserProficienciesResponseTypeDef,
    ListUsersResponseTypeDef,
    ListViewsResponseTypeDef,
    ListViewVersionsResponseTypeDef,
    MediaConcurrencyTypeDef,
    MetricV2TypeDef,
    MonitorContactResponseTypeDef,
    NewSessionDetailsTypeDef,
    OutboundCallerConfigTypeDef,
    ParticipantDetailsToAddTypeDef,
    ParticipantDetailsTypeDef,
    PersistentChatTypeDef,
    PredefinedAttributeSearchCriteriaTypeDef,
    PredefinedAttributeValuesTypeDef,
    PromptSearchCriteriaTypeDef,
    PromptSearchFilterTypeDef,
    QueueSearchCriteriaTypeDef,
    QueueSearchFilterTypeDef,
    QuickConnectConfigTypeDef,
    QuickConnectSearchCriteriaTypeDef,
    QuickConnectSearchFilterTypeDef,
    ReferenceTypeDef,
    ReplicateInstanceResponseTypeDef,
    ResourceTagsSearchCriteriaTypeDef,
    RoutingProfileQueueConfigTypeDef,
    RoutingProfileQueueReferenceTypeDef,
    RoutingProfileSearchCriteriaTypeDef,
    RoutingProfileSearchFilterTypeDef,
    RuleActionTypeDef,
    RuleTriggerEventSourceTypeDef,
    SearchAvailablePhoneNumbersResponseTypeDef,
    SearchContactFlowModulesResponseTypeDef,
    SearchContactFlowsResponseTypeDef,
    SearchContactsResponseTypeDef,
    SearchContactsTimeRangeTypeDef,
    SearchCriteriaTypeDef,
    SearchHoursOfOperationsResponseTypeDef,
    SearchPredefinedAttributesResponseTypeDef,
    SearchPromptsResponseTypeDef,
    SearchQueuesResponseTypeDef,
    SearchQuickConnectsResponseTypeDef,
    SearchResourceTagsResponseTypeDef,
    SearchRoutingProfilesResponseTypeDef,
    SearchSecurityProfilesResponseTypeDef,
    SearchUsersResponseTypeDef,
    SearchVocabulariesResponseTypeDef,
    SecurityProfileSearchCriteriaTypeDef,
    SecurityProfilesSearchFilterTypeDef,
    SegmentAttributeValueTypeDef,
    SendChatIntegrationEventResponseTypeDef,
    SignInConfigTypeDef,
    SortTypeDef,
    StartAttachedFileUploadResponseTypeDef,
    StartChatContactResponseTypeDef,
    StartContactEvaluationResponseTypeDef,
    StartContactStreamingResponseTypeDef,
    StartOutboundVoiceContactResponseTypeDef,
    StartTaskContactResponseTypeDef,
    StartWebRTCContactResponseTypeDef,
    SubmitContactEvaluationResponseTypeDef,
    TaskTemplateConstraintsTypeDef,
    TaskTemplateDefaultsTypeDef,
    TaskTemplateFieldTypeDef,
    TelephonyConfigTypeDef,
    TransferContactResponseTypeDef,
    UpdateContactEvaluationResponseTypeDef,
    UpdateEvaluationFormResponseTypeDef,
    UpdateParticipantRoleConfigChannelInfoTypeDef,
    UpdatePhoneNumberResponseTypeDef,
    UpdatePromptResponseTypeDef,
    UpdateTaskTemplateResponseTypeDef,
    UpdateViewContentResponseTypeDef,
    UserDataFiltersTypeDef,
    UserIdentityInfoTypeDef,
    UserPhoneConfigTypeDef,
    UserProficiencyDisassociateTypeDef,
    UserProficiencyTypeDef,
    UserSearchCriteriaTypeDef,
    UserSearchFilterTypeDef,
    ViewInputContentTypeDef,
    VoiceRecordingConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ConnectClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ContactFlowNotPublishedException: Type[BotocoreClientError]
    ContactNotFoundException: Type[BotocoreClientError]
    DestinationNotAllowedException: Type[BotocoreClientError]
    DuplicateResourceException: Type[BotocoreClientError]
    IdempotencyException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidContactFlowException: Type[BotocoreClientError]
    InvalidContactFlowModuleException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MaximumResultReturnedException: Type[BotocoreClientError]
    OutboundContactNotPermittedException: Type[BotocoreClientError]
    OutputTypeNotFoundException: Type[BotocoreClientError]
    PropertyValidationException: Type[BotocoreClientError]
    ResourceConflictException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceNotReadyException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UserNotFoundException: Type[BotocoreClientError]

class ConnectClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ConnectClient exceptions.
        """

    def activate_evaluation_form(
        self, *, InstanceId: str, EvaluationFormId: str, EvaluationFormVersion: int
    ) -> ActivateEvaluationFormResponseTypeDef:
        """
        Activates an evaluation form in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.activate_evaluation_form)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#activate_evaluation_form)
        """

    def associate_analytics_data_set(
        self, *, InstanceId: str, DataSetId: str, TargetAccountId: str = None
    ) -> AssociateAnalyticsDataSetResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.associate_analytics_data_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#associate_analytics_data_set)
        """

    def associate_approved_origin(self, *, InstanceId: str, Origin: str) -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.associate_approved_origin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#associate_approved_origin)
        """

    def associate_bot(
        self, *, InstanceId: str, LexBot: "LexBotTypeDef" = None, LexV2Bot: "LexV2BotTypeDef" = None
    ) -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.associate_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#associate_bot)
        """

    def associate_default_vocabulary(
        self, *, InstanceId: str, LanguageCode: VocabularyLanguageCodeType, VocabularyId: str = None
    ) -> Dict[str, Any]:
        """
        Associates an existing vocabulary as the default.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.associate_default_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#associate_default_vocabulary)
        """

    def associate_flow(
        self,
        *,
        InstanceId: str,
        ResourceId: str,
        FlowId: str,
        ResourceType: Literal["SMS_PHONE_NUMBER"]
    ) -> Dict[str, Any]:
        """
        Associates a connect resource to a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.associate_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#associate_flow)
        """

    def associate_instance_storage_config(
        self,
        *,
        InstanceId: str,
        ResourceType: InstanceStorageResourceTypeType,
        StorageConfig: "InstanceStorageConfigTypeDef"
    ) -> AssociateInstanceStorageConfigResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.associate_instance_storage_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#associate_instance_storage_config)
        """

    def associate_lambda_function(self, *, InstanceId: str, FunctionArn: str) -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.associate_lambda_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#associate_lambda_function)
        """

    def associate_lex_bot(self, *, InstanceId: str, LexBot: "LexBotTypeDef") -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.associate_lex_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#associate_lex_bot)
        """

    def associate_phone_number_contact_flow(
        self, *, PhoneNumberId: str, InstanceId: str, ContactFlowId: str
    ) -> None:
        """
        Associates a flow with a phone number claimed to your Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.associate_phone_number_contact_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#associate_phone_number_contact_flow)
        """

    def associate_queue_quick_connects(
        self, *, InstanceId: str, QueueId: str, QuickConnectIds: List[str]
    ) -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.associate_queue_quick_connects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#associate_queue_quick_connects)
        """

    def associate_routing_profile_queues(
        self,
        *,
        InstanceId: str,
        RoutingProfileId: str,
        QueueConfigs: List["RoutingProfileQueueConfigTypeDef"]
    ) -> None:
        """
        Associates a set of queues with a routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.associate_routing_profile_queues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#associate_routing_profile_queues)
        """

    def associate_security_key(
        self, *, InstanceId: str, Key: str
    ) -> AssociateSecurityKeyResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.associate_security_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#associate_security_key)
        """

    def associate_traffic_distribution_group_user(
        self, *, TrafficDistributionGroupId: str, UserId: str, InstanceId: str
    ) -> Dict[str, Any]:
        """
        Associates an agent with a traffic distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.associate_traffic_distribution_group_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#associate_traffic_distribution_group_user)
        """

    def associate_user_proficiencies(
        self, *, InstanceId: str, UserId: str, UserProficiencies: List["UserProficiencyTypeDef"]
    ) -> None:
        """
        >Associates a set of proficiencies with a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.associate_user_proficiencies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#associate_user_proficiencies)
        """

    def batch_associate_analytics_data_set(
        self, *, InstanceId: str, DataSetIds: List[str], TargetAccountId: str = None
    ) -> BatchAssociateAnalyticsDataSetResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.batch_associate_analytics_data_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#batch_associate_analytics_data_set)
        """

    def batch_disassociate_analytics_data_set(
        self, *, InstanceId: str, DataSetIds: List[str], TargetAccountId: str = None
    ) -> BatchDisassociateAnalyticsDataSetResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.batch_disassociate_analytics_data_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#batch_disassociate_analytics_data_set)
        """

    def batch_get_attached_file_metadata(
        self, *, FileIds: List[str], InstanceId: str, AssociatedResourceArn: str
    ) -> BatchGetAttachedFileMetadataResponseTypeDef:
        """
        Allows you to retrieve metadata about multiple attached files on an associated
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.batch_get_attached_file_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#batch_get_attached_file_metadata)
        """

    def batch_get_flow_association(
        self,
        *,
        InstanceId: str,
        ResourceIds: List[str],
        ResourceType: Literal["VOICE_PHONE_NUMBER"] = None
    ) -> BatchGetFlowAssociationResponseTypeDef:
        """
        Retrieve the flow associations for the given resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.batch_get_flow_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#batch_get_flow_association)
        """

    def batch_put_contact(
        self,
        *,
        InstanceId: str,
        ContactDataRequestList: List["ContactDataRequestTypeDef"],
        ClientToken: str = None
    ) -> BatchPutContactResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.batch_put_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#batch_put_contact)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#can_paginate)
        """

    def claim_phone_number(
        self,
        *,
        PhoneNumber: str,
        TargetArn: str = None,
        InstanceId: str = None,
        PhoneNumberDescription: str = None,
        Tags: Dict[str, str] = None,
        ClientToken: str = None
    ) -> ClaimPhoneNumberResponseTypeDef:
        """
        Claims an available phone number to your Amazon Connect instance or traffic
        distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.claim_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#claim_phone_number)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#close)
        """

    def complete_attached_file_upload(
        self, *, InstanceId: str, FileId: str, AssociatedResourceArn: str
    ) -> Dict[str, Any]:
        """
        Allows you to confirm that the attached file has been uploaded using the pre-
        signed URL provided in the StartAttachedFileUpload API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.complete_attached_file_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#complete_attached_file_upload)
        """

    def create_agent_status(
        self,
        *,
        InstanceId: str,
        Name: str,
        State: AgentStatusStateType,
        Description: str = None,
        DisplayOrder: int = None,
        Tags: Dict[str, str] = None
    ) -> CreateAgentStatusResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.create_agent_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#create_agent_status)
        """

    def create_contact_flow(
        self,
        *,
        InstanceId: str,
        Name: str,
        Type: ContactFlowTypeType,
        Content: str,
        Description: str = None,
        Status: ContactFlowStatusType = None,
        Tags: Dict[str, str] = None
    ) -> CreateContactFlowResponseTypeDef:
        """
        Creates a flow for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.create_contact_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#create_contact_flow)
        """

    def create_contact_flow_module(
        self,
        *,
        InstanceId: str,
        Name: str,
        Content: str,
        Description: str = None,
        Tags: Dict[str, str] = None,
        ClientToken: str = None
    ) -> CreateContactFlowModuleResponseTypeDef:
        """
        Creates a flow module for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.create_contact_flow_module)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#create_contact_flow_module)
        """

    def create_evaluation_form(
        self,
        *,
        InstanceId: str,
        Title: str,
        Items: List["EvaluationFormItemTypeDef"],
        Description: str = None,
        ScoringStrategy: "EvaluationFormScoringStrategyTypeDef" = None,
        ClientToken: str = None
    ) -> CreateEvaluationFormResponseTypeDef:
        """
        Creates an evaluation form in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.create_evaluation_form)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#create_evaluation_form)
        """

    def create_hours_of_operation(
        self,
        *,
        InstanceId: str,
        Name: str,
        TimeZone: str,
        Config: List["HoursOfOperationConfigTypeDef"],
        Description: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateHoursOfOperationResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.create_hours_of_operation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#create_hours_of_operation)
        """

    def create_instance(
        self,
        *,
        IdentityManagementType: DirectoryTypeType,
        InboundCallsEnabled: bool,
        OutboundCallsEnabled: bool,
        ClientToken: str = None,
        InstanceAlias: str = None,
        DirectoryId: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateInstanceResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.create_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#create_instance)
        """

    def create_integration_association(
        self,
        *,
        InstanceId: str,
        IntegrationType: IntegrationTypeType,
        IntegrationArn: str,
        SourceApplicationUrl: str = None,
        SourceApplicationName: str = None,
        SourceType: SourceTypeType = None,
        Tags: Dict[str, str] = None
    ) -> CreateIntegrationAssociationResponseTypeDef:
        """
        Creates an Amazon Web Services resource association with an Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.create_integration_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#create_integration_association)
        """

    def create_participant(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        ParticipantDetails: "ParticipantDetailsToAddTypeDef",
        ClientToken: str = None
    ) -> CreateParticipantResponseTypeDef:
        """
        Adds a new participant into an on-going chat contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.create_participant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#create_participant)
        """

    def create_persistent_contact_association(
        self,
        *,
        InstanceId: str,
        InitialContactId: str,
        RehydrationType: RehydrationTypeType,
        SourceContactId: str,
        ClientToken: str = None
    ) -> CreatePersistentContactAssociationResponseTypeDef:
        """
        Enables rehydration of chats for the lifespan of a contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.create_persistent_contact_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#create_persistent_contact_association)
        """

    def create_predefined_attribute(
        self, *, InstanceId: str, Name: str, Values: "PredefinedAttributeValuesTypeDef"
    ) -> None:
        """
        Creates a new predefined attribute for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.create_predefined_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#create_predefined_attribute)
        """

    def create_prompt(
        self,
        *,
        InstanceId: str,
        Name: str,
        S3Uri: str,
        Description: str = None,
        Tags: Dict[str, str] = None
    ) -> CreatePromptResponseTypeDef:
        """
        Creates a prompt.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.create_prompt)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#create_prompt)
        """

    def create_queue(
        self,
        *,
        InstanceId: str,
        Name: str,
        HoursOfOperationId: str,
        Description: str = None,
        OutboundCallerConfig: "OutboundCallerConfigTypeDef" = None,
        MaxContacts: int = None,
        QuickConnectIds: List[str] = None,
        Tags: Dict[str, str] = None
    ) -> CreateQueueResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.create_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#create_queue)
        """

    def create_quick_connect(
        self,
        *,
        InstanceId: str,
        Name: str,
        QuickConnectConfig: "QuickConnectConfigTypeDef",
        Description: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateQuickConnectResponseTypeDef:
        """
        Creates a quick connect for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.create_quick_connect)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#create_quick_connect)
        """

    def create_routing_profile(
        self,
        *,
        InstanceId: str,
        Name: str,
        Description: str,
        DefaultOutboundQueueId: str,
        MediaConcurrencies: List["MediaConcurrencyTypeDef"],
        QueueConfigs: List["RoutingProfileQueueConfigTypeDef"] = None,
        Tags: Dict[str, str] = None,
        AgentAvailabilityTimer: AgentAvailabilityTimerType = None
    ) -> CreateRoutingProfileResponseTypeDef:
        """
        Creates a new routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.create_routing_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#create_routing_profile)
        """

    def create_rule(
        self,
        *,
        InstanceId: str,
        Name: str,
        TriggerEventSource: "RuleTriggerEventSourceTypeDef",
        Function: str,
        Actions: List["RuleActionTypeDef"],
        PublishStatus: RulePublishStatusType,
        ClientToken: str = None
    ) -> CreateRuleResponseTypeDef:
        """
        Creates a rule for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.create_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#create_rule)
        """

    def create_security_profile(
        self,
        *,
        SecurityProfileName: str,
        InstanceId: str,
        Description: str = None,
        Permissions: List[str] = None,
        Tags: Dict[str, str] = None,
        AllowedAccessControlTags: Dict[str, str] = None,
        TagRestrictedResources: List[str] = None,
        Applications: List["ApplicationTypeDef"] = None,
        HierarchyRestrictedResources: List[str] = None,
        AllowedAccessControlHierarchyGroupId: str = None
    ) -> CreateSecurityProfileResponseTypeDef:
        """
        Creates a security profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.create_security_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#create_security_profile)
        """

    def create_task_template(
        self,
        *,
        InstanceId: str,
        Name: str,
        Fields: List["TaskTemplateFieldTypeDef"],
        Description: str = None,
        ContactFlowId: str = None,
        Constraints: "TaskTemplateConstraintsTypeDef" = None,
        Defaults: "TaskTemplateDefaultsTypeDef" = None,
        Status: TaskTemplateStatusType = None,
        ClientToken: str = None
    ) -> CreateTaskTemplateResponseTypeDef:
        """
        Creates a new task template in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.create_task_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#create_task_template)
        """

    def create_traffic_distribution_group(
        self,
        *,
        Name: str,
        InstanceId: str,
        Description: str = None,
        ClientToken: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateTrafficDistributionGroupResponseTypeDef:
        """
        Creates a traffic distribution group given an Amazon Connect instance that has
        been replicated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.create_traffic_distribution_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#create_traffic_distribution_group)
        """

    def create_use_case(
        self,
        *,
        InstanceId: str,
        IntegrationAssociationId: str,
        UseCaseType: UseCaseTypeType,
        Tags: Dict[str, str] = None
    ) -> CreateUseCaseResponseTypeDef:
        """
        Creates a use case for an integration association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.create_use_case)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#create_use_case)
        """

    def create_user(
        self,
        *,
        Username: str,
        PhoneConfig: "UserPhoneConfigTypeDef",
        SecurityProfileIds: List[str],
        RoutingProfileId: str,
        InstanceId: str,
        Password: str = None,
        IdentityInfo: "UserIdentityInfoTypeDef" = None,
        DirectoryUserId: str = None,
        HierarchyGroupId: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateUserResponseTypeDef:
        """
        Creates a user account for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.create_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#create_user)
        """

    def create_user_hierarchy_group(
        self, *, Name: str, InstanceId: str, ParentGroupId: str = None, Tags: Dict[str, str] = None
    ) -> CreateUserHierarchyGroupResponseTypeDef:
        """
        Creates a new user hierarchy group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.create_user_hierarchy_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#create_user_hierarchy_group)
        """

    def create_view(
        self,
        *,
        InstanceId: str,
        Status: ViewStatusType,
        Content: "ViewInputContentTypeDef",
        Name: str,
        ClientToken: str = None,
        Description: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateViewResponseTypeDef:
        """
        Creates a new view with the possible status of `SAVED` or `PUBLISHED`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.create_view)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#create_view)
        """

    def create_view_version(
        self,
        *,
        InstanceId: str,
        ViewId: str,
        VersionDescription: str = None,
        ViewContentSha256: str = None
    ) -> CreateViewVersionResponseTypeDef:
        """
        Publishes a new version of the view identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.create_view_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#create_view_version)
        """

    def create_vocabulary(
        self,
        *,
        InstanceId: str,
        VocabularyName: str,
        LanguageCode: VocabularyLanguageCodeType,
        Content: str,
        ClientToken: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateVocabularyResponseTypeDef:
        """
        Creates a custom vocabulary associated with your Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.create_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#create_vocabulary)
        """

    def deactivate_evaluation_form(
        self, *, InstanceId: str, EvaluationFormId: str, EvaluationFormVersion: int
    ) -> DeactivateEvaluationFormResponseTypeDef:
        """
        Deactivates an evaluation form in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.deactivate_evaluation_form)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#deactivate_evaluation_form)
        """

    def delete_attached_file(
        self, *, InstanceId: str, FileId: str, AssociatedResourceArn: str
    ) -> Dict[str, Any]:
        """
        Deletes an attached file along with the underlying S3 Object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.delete_attached_file)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#delete_attached_file)
        """

    def delete_contact_evaluation(self, *, InstanceId: str, EvaluationId: str) -> None:
        """
        Deletes a contact evaluation in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.delete_contact_evaluation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#delete_contact_evaluation)
        """

    def delete_contact_flow(self, *, InstanceId: str, ContactFlowId: str) -> Dict[str, Any]:
        """
        Deletes a flow for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.delete_contact_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#delete_contact_flow)
        """

    def delete_contact_flow_module(
        self, *, InstanceId: str, ContactFlowModuleId: str
    ) -> Dict[str, Any]:
        """
        Deletes the specified flow module.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.delete_contact_flow_module)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#delete_contact_flow_module)
        """

    def delete_evaluation_form(
        self, *, InstanceId: str, EvaluationFormId: str, EvaluationFormVersion: int = None
    ) -> None:
        """
        Deletes an evaluation form in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.delete_evaluation_form)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#delete_evaluation_form)
        """

    def delete_hours_of_operation(self, *, InstanceId: str, HoursOfOperationId: str) -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.delete_hours_of_operation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#delete_hours_of_operation)
        """

    def delete_instance(self, *, InstanceId: str) -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.delete_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#delete_instance)
        """

    def delete_integration_association(
        self, *, InstanceId: str, IntegrationAssociationId: str
    ) -> None:
        """
        Deletes an Amazon Web Services resource association from an Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.delete_integration_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#delete_integration_association)
        """

    def delete_predefined_attribute(self, *, InstanceId: str, Name: str) -> None:
        """
        Deletes a predefined attribute from the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.delete_predefined_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#delete_predefined_attribute)
        """

    def delete_prompt(self, *, InstanceId: str, PromptId: str) -> None:
        """
        Deletes a prompt.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.delete_prompt)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#delete_prompt)
        """

    def delete_queue(self, *, InstanceId: str, QueueId: str) -> None:
        """
        Deletes a queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.delete_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#delete_queue)
        """

    def delete_quick_connect(self, *, InstanceId: str, QuickConnectId: str) -> None:
        """
        Deletes a quick connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.delete_quick_connect)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#delete_quick_connect)
        """

    def delete_routing_profile(self, *, InstanceId: str, RoutingProfileId: str) -> None:
        """
        Deletes a routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.delete_routing_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#delete_routing_profile)
        """

    def delete_rule(self, *, InstanceId: str, RuleId: str) -> None:
        """
        Deletes a rule for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.delete_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#delete_rule)
        """

    def delete_security_profile(self, *, InstanceId: str, SecurityProfileId: str) -> None:
        """
        Deletes a security profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.delete_security_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#delete_security_profile)
        """

    def delete_task_template(self, *, InstanceId: str, TaskTemplateId: str) -> Dict[str, Any]:
        """
        Deletes the task template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.delete_task_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#delete_task_template)
        """

    def delete_traffic_distribution_group(
        self, *, TrafficDistributionGroupId: str
    ) -> Dict[str, Any]:
        """
        Deletes a traffic distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.delete_traffic_distribution_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#delete_traffic_distribution_group)
        """

    def delete_use_case(
        self, *, InstanceId: str, IntegrationAssociationId: str, UseCaseId: str
    ) -> None:
        """
        Deletes a use case from an integration association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.delete_use_case)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#delete_use_case)
        """

    def delete_user(self, *, InstanceId: str, UserId: str) -> None:
        """
        Deletes a user account from the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.delete_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#delete_user)
        """

    def delete_user_hierarchy_group(self, *, HierarchyGroupId: str, InstanceId: str) -> None:
        """
        Deletes an existing user hierarchy group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.delete_user_hierarchy_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#delete_user_hierarchy_group)
        """

    def delete_view(self, *, InstanceId: str, ViewId: str) -> Dict[str, Any]:
        """
        Deletes the view entirely.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.delete_view)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#delete_view)
        """

    def delete_view_version(
        self, *, InstanceId: str, ViewId: str, ViewVersion: int
    ) -> Dict[str, Any]:
        """
        Deletes the particular version specified in `ViewVersion` identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.delete_view_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#delete_view_version)
        """

    def delete_vocabulary(
        self, *, InstanceId: str, VocabularyId: str
    ) -> DeleteVocabularyResponseTypeDef:
        """
        Deletes the vocabulary that has the given identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.delete_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#delete_vocabulary)
        """

    def describe_agent_status(
        self, *, InstanceId: str, AgentStatusId: str
    ) -> DescribeAgentStatusResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_agent_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_agent_status)
        """

    def describe_authentication_profile(
        self, *, AuthenticationProfileId: str, InstanceId: str
    ) -> DescribeAuthenticationProfileResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_authentication_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_authentication_profile)
        """

    def describe_contact(
        self, *, InstanceId: str, ContactId: str
    ) -> DescribeContactResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_contact)
        """

    def describe_contact_evaluation(
        self, *, InstanceId: str, EvaluationId: str
    ) -> DescribeContactEvaluationResponseTypeDef:
        """
        Describes a contact evaluation in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_contact_evaluation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_contact_evaluation)
        """

    def describe_contact_flow(
        self, *, InstanceId: str, ContactFlowId: str
    ) -> DescribeContactFlowResponseTypeDef:
        """
        Describes the specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_contact_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_contact_flow)
        """

    def describe_contact_flow_module(
        self, *, InstanceId: str, ContactFlowModuleId: str
    ) -> DescribeContactFlowModuleResponseTypeDef:
        """
        Describes the specified flow module.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_contact_flow_module)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_contact_flow_module)
        """

    def describe_evaluation_form(
        self, *, InstanceId: str, EvaluationFormId: str, EvaluationFormVersion: int = None
    ) -> DescribeEvaluationFormResponseTypeDef:
        """
        Describes an evaluation form in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_evaluation_form)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_evaluation_form)
        """

    def describe_hours_of_operation(
        self, *, InstanceId: str, HoursOfOperationId: str
    ) -> DescribeHoursOfOperationResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_hours_of_operation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_hours_of_operation)
        """

    def describe_instance(self, *, InstanceId: str) -> DescribeInstanceResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_instance)
        """

    def describe_instance_attribute(
        self, *, InstanceId: str, AttributeType: InstanceAttributeTypeType
    ) -> DescribeInstanceAttributeResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_instance_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_instance_attribute)
        """

    def describe_instance_storage_config(
        self, *, InstanceId: str, AssociationId: str, ResourceType: InstanceStorageResourceTypeType
    ) -> DescribeInstanceStorageConfigResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_instance_storage_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_instance_storage_config)
        """

    def describe_phone_number(self, *, PhoneNumberId: str) -> DescribePhoneNumberResponseTypeDef:
        """
        Gets details and status of a phone number that’s claimed to your Amazon Connect
        instance or traffic distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_phone_number)
        """

    def describe_predefined_attribute(
        self, *, InstanceId: str, Name: str
    ) -> DescribePredefinedAttributeResponseTypeDef:
        """
        Describes a predefined attribute for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_predefined_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_predefined_attribute)
        """

    def describe_prompt(self, *, InstanceId: str, PromptId: str) -> DescribePromptResponseTypeDef:
        """
        Describes the prompt.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_prompt)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_prompt)
        """

    def describe_queue(self, *, InstanceId: str, QueueId: str) -> DescribeQueueResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_queue)
        """

    def describe_quick_connect(
        self, *, InstanceId: str, QuickConnectId: str
    ) -> DescribeQuickConnectResponseTypeDef:
        """
        Describes the quick connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_quick_connect)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_quick_connect)
        """

    def describe_routing_profile(
        self, *, InstanceId: str, RoutingProfileId: str
    ) -> DescribeRoutingProfileResponseTypeDef:
        """
        Describes the specified routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_routing_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_routing_profile)
        """

    def describe_rule(self, *, InstanceId: str, RuleId: str) -> DescribeRuleResponseTypeDef:
        """
        Describes a rule for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_rule)
        """

    def describe_security_profile(
        self, *, SecurityProfileId: str, InstanceId: str
    ) -> DescribeSecurityProfileResponseTypeDef:
        """
        Gets basic information about the security profle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_security_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_security_profile)
        """

    def describe_traffic_distribution_group(
        self, *, TrafficDistributionGroupId: str
    ) -> DescribeTrafficDistributionGroupResponseTypeDef:
        """
        Gets details and status of a traffic distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_traffic_distribution_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_traffic_distribution_group)
        """

    def describe_user(self, *, UserId: str, InstanceId: str) -> DescribeUserResponseTypeDef:
        """
        Describes the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_user)
        """

    def describe_user_hierarchy_group(
        self, *, HierarchyGroupId: str, InstanceId: str
    ) -> DescribeUserHierarchyGroupResponseTypeDef:
        """
        Describes the specified hierarchy group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_user_hierarchy_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_user_hierarchy_group)
        """

    def describe_user_hierarchy_structure(
        self, *, InstanceId: str
    ) -> DescribeUserHierarchyStructureResponseTypeDef:
        """
        Describes the hierarchy structure of the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_user_hierarchy_structure)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_user_hierarchy_structure)
        """

    def describe_view(self, *, InstanceId: str, ViewId: str) -> DescribeViewResponseTypeDef:
        """
        Retrieves the view for the specified Amazon Connect instance and view
        identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_view)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_view)
        """

    def describe_vocabulary(
        self, *, InstanceId: str, VocabularyId: str
    ) -> DescribeVocabularyResponseTypeDef:
        """
        Describes the specified vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.describe_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#describe_vocabulary)
        """

    def disassociate_analytics_data_set(
        self, *, InstanceId: str, DataSetId: str, TargetAccountId: str = None
    ) -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.disassociate_analytics_data_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#disassociate_analytics_data_set)
        """

    def disassociate_approved_origin(self, *, InstanceId: str, Origin: str) -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.disassociate_approved_origin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#disassociate_approved_origin)
        """

    def disassociate_bot(
        self, *, InstanceId: str, LexBot: "LexBotTypeDef" = None, LexV2Bot: "LexV2BotTypeDef" = None
    ) -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.disassociate_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#disassociate_bot)
        """

    def disassociate_flow(
        self, *, InstanceId: str, ResourceId: str, ResourceType: Literal["SMS_PHONE_NUMBER"]
    ) -> Dict[str, Any]:
        """
        Disassociates a connect resource from a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.disassociate_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#disassociate_flow)
        """

    def disassociate_instance_storage_config(
        self, *, InstanceId: str, AssociationId: str, ResourceType: InstanceStorageResourceTypeType
    ) -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.disassociate_instance_storage_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#disassociate_instance_storage_config)
        """

    def disassociate_lambda_function(self, *, InstanceId: str, FunctionArn: str) -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.disassociate_lambda_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#disassociate_lambda_function)
        """

    def disassociate_lex_bot(self, *, InstanceId: str, BotName: str, LexRegion: str) -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.disassociate_lex_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#disassociate_lex_bot)
        """

    def disassociate_phone_number_contact_flow(
        self, *, PhoneNumberId: str, InstanceId: str
    ) -> None:
        """
        Removes the flow association from a phone number claimed to your Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.disassociate_phone_number_contact_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#disassociate_phone_number_contact_flow)
        """

    def disassociate_queue_quick_connects(
        self, *, InstanceId: str, QueueId: str, QuickConnectIds: List[str]
    ) -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.disassociate_queue_quick_connects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#disassociate_queue_quick_connects)
        """

    def disassociate_routing_profile_queues(
        self,
        *,
        InstanceId: str,
        RoutingProfileId: str,
        QueueReferences: List["RoutingProfileQueueReferenceTypeDef"]
    ) -> None:
        """
        Disassociates a set of queues from a routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.disassociate_routing_profile_queues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#disassociate_routing_profile_queues)
        """

    def disassociate_security_key(self, *, InstanceId: str, AssociationId: str) -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.disassociate_security_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#disassociate_security_key)
        """

    def disassociate_traffic_distribution_group_user(
        self, *, TrafficDistributionGroupId: str, UserId: str, InstanceId: str
    ) -> Dict[str, Any]:
        """
        Disassociates an agent from a traffic distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.disassociate_traffic_distribution_group_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#disassociate_traffic_distribution_group_user)
        """

    def disassociate_user_proficiencies(
        self,
        *,
        InstanceId: str,
        UserId: str,
        UserProficiencies: List["UserProficiencyDisassociateTypeDef"]
    ) -> None:
        """
        Disassociates a set of proficiencies from a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.disassociate_user_proficiencies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#disassociate_user_proficiencies)
        """

    def dismiss_user_contact(
        self, *, UserId: str, InstanceId: str, ContactId: str
    ) -> Dict[str, Any]:
        """
        Dismisses contacts from an agent’s CCP and returns the agent to an available
        state, which allows the agent to receive a new routed contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.dismiss_user_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#dismiss_user_contact)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#generate_presigned_url)
        """

    def get_attached_file(
        self,
        *,
        InstanceId: str,
        FileId: str,
        AssociatedResourceArn: str,
        UrlExpiryInSeconds: int = None
    ) -> GetAttachedFileResponseTypeDef:
        """
        Provides a pre-signed URL for download of an approved attached file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.get_attached_file)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#get_attached_file)
        """

    def get_contact_attributes(
        self, *, InstanceId: str, InitialContactId: str
    ) -> GetContactAttributesResponseTypeDef:
        """
        Retrieves the contact attributes for the specified contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.get_contact_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#get_contact_attributes)
        """

    def get_current_metric_data(
        self,
        *,
        InstanceId: str,
        Filters: "FiltersTypeDef",
        CurrentMetrics: List["CurrentMetricTypeDef"],
        Groupings: List[GroupingType] = None,
        NextToken: str = None,
        MaxResults: int = None,
        SortCriteria: List["CurrentMetricSortCriteriaTypeDef"] = None
    ) -> GetCurrentMetricDataResponseTypeDef:
        """
        Gets the real-time metric data from the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.get_current_metric_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#get_current_metric_data)
        """

    def get_current_user_data(
        self,
        *,
        InstanceId: str,
        Filters: "UserDataFiltersTypeDef",
        NextToken: str = None,
        MaxResults: int = None
    ) -> GetCurrentUserDataResponseTypeDef:
        """
        Gets the real-time active user data from the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.get_current_user_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#get_current_user_data)
        """

    def get_federation_token(self, *, InstanceId: str) -> GetFederationTokenResponseTypeDef:
        """
        Supports SAML sign-in for Amazon Connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.get_federation_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#get_federation_token)
        """

    def get_flow_association(
        self, *, InstanceId: str, ResourceId: str, ResourceType: Literal["SMS_PHONE_NUMBER"]
    ) -> GetFlowAssociationResponseTypeDef:
        """
        Retrieves the flow associated for a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.get_flow_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#get_flow_association)
        """

    def get_metric_data(
        self,
        *,
        InstanceId: str,
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        Filters: "FiltersTypeDef",
        HistoricalMetrics: List["HistoricalMetricTypeDef"],
        Groupings: List[GroupingType] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> GetMetricDataResponseTypeDef:
        """
        Gets historical metric data from the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.get_metric_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#get_metric_data)
        """

    def get_metric_data_v2(
        self,
        *,
        ResourceArn: str,
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        Filters: List["FilterV2TypeDef"],
        Metrics: List["MetricV2TypeDef"],
        Interval: "IntervalDetailsTypeDef" = None,
        Groupings: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> GetMetricDataV2ResponseTypeDef:
        """
        Gets metric data from the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.get_metric_data_v2)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#get_metric_data_v2)
        """

    def get_prompt_file(self, *, InstanceId: str, PromptId: str) -> GetPromptFileResponseTypeDef:
        """
        Gets the prompt file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.get_prompt_file)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#get_prompt_file)
        """

    def get_task_template(
        self, *, InstanceId: str, TaskTemplateId: str, SnapshotVersion: str = None
    ) -> GetTaskTemplateResponseTypeDef:
        """
        Gets details about a specific task template in the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.get_task_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#get_task_template)
        """

    def get_traffic_distribution(self, *, Id: str) -> GetTrafficDistributionResponseTypeDef:
        """
        Retrieves the current traffic distribution for a given traffic distribution
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.get_traffic_distribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#get_traffic_distribution)
        """

    def import_phone_number(
        self,
        *,
        InstanceId: str,
        SourcePhoneNumberArn: str,
        PhoneNumberDescription: str = None,
        Tags: Dict[str, str] = None,
        ClientToken: str = None
    ) -> ImportPhoneNumberResponseTypeDef:
        """
        Imports a claimed phone number from an external service, such as Amazon
        Pinpoint, into an Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.import_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#import_phone_number)
        """

    def list_agent_statuses(
        self,
        *,
        InstanceId: str,
        NextToken: str = None,
        MaxResults: int = None,
        AgentStatusTypes: List[AgentStatusTypeType] = None
    ) -> ListAgentStatusResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_agent_statuses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_agent_statuses)
        """

    def list_analytics_data_associations(
        self,
        *,
        InstanceId: str,
        DataSetId: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListAnalyticsDataAssociationsResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_analytics_data_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_analytics_data_associations)
        """

    def list_approved_origins(
        self, *, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListApprovedOriginsResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_approved_origins)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_approved_origins)
        """

    def list_authentication_profiles(
        self, *, InstanceId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAuthenticationProfilesResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_authentication_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_authentication_profiles)
        """

    def list_bots(
        self,
        *,
        InstanceId: str,
        LexVersion: LexVersionType,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListBotsResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_bots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_bots)
        """

    def list_contact_evaluations(
        self, *, InstanceId: str, ContactId: str, NextToken: str = None
    ) -> ListContactEvaluationsResponseTypeDef:
        """
        Lists contact evaluations in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_contact_evaluations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_contact_evaluations)
        """

    def list_contact_flow_modules(
        self,
        *,
        InstanceId: str,
        NextToken: str = None,
        MaxResults: int = None,
        ContactFlowModuleState: ContactFlowModuleStateType = None
    ) -> ListContactFlowModulesResponseTypeDef:
        """
        Provides information about the flow modules for the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_contact_flow_modules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_contact_flow_modules)
        """

    def list_contact_flows(
        self,
        *,
        InstanceId: str,
        ContactFlowTypes: List[ContactFlowTypeType] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListContactFlowsResponseTypeDef:
        """
        Provides information about the flows for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_contact_flows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_contact_flows)
        """

    def list_contact_references(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        ReferenceTypes: List[ReferenceTypeType],
        NextToken: str = None
    ) -> ListContactReferencesResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_contact_references)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_contact_references)
        """

    def list_default_vocabularies(
        self,
        *,
        InstanceId: str,
        LanguageCode: VocabularyLanguageCodeType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListDefaultVocabulariesResponseTypeDef:
        """
        Lists the default vocabularies for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_default_vocabularies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_default_vocabularies)
        """

    def list_evaluation_form_versions(
        self,
        *,
        InstanceId: str,
        EvaluationFormId: str,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListEvaluationFormVersionsResponseTypeDef:
        """
        Lists versions of an evaluation form in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_evaluation_form_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_evaluation_form_versions)
        """

    def list_evaluation_forms(
        self, *, InstanceId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListEvaluationFormsResponseTypeDef:
        """
        Lists evaluation forms in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_evaluation_forms)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_evaluation_forms)
        """

    def list_flow_associations(
        self,
        *,
        InstanceId: str,
        ResourceType: Literal["VOICE_PHONE_NUMBER"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListFlowAssociationsResponseTypeDef:
        """
        List the flow association based on the filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_flow_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_flow_associations)
        """

    def list_hours_of_operations(
        self, *, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListHoursOfOperationsResponseTypeDef:
        """
        Provides information about the hours of operation for the specified Amazon
        Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_hours_of_operations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_hours_of_operations)
        """

    def list_instance_attributes(
        self, *, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListInstanceAttributesResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_instance_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_instance_attributes)
        """

    def list_instance_storage_configs(
        self,
        *,
        InstanceId: str,
        ResourceType: InstanceStorageResourceTypeType,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListInstanceStorageConfigsResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_instance_storage_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_instance_storage_configs)
        """

    def list_instances(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListInstancesResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_instances)
        """

    def list_integration_associations(
        self,
        *,
        InstanceId: str,
        IntegrationType: IntegrationTypeType = None,
        NextToken: str = None,
        MaxResults: int = None,
        IntegrationArn: str = None
    ) -> ListIntegrationAssociationsResponseTypeDef:
        """
        Provides summary information about the Amazon Web Services resource associations
        for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_integration_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_integration_associations)
        """

    def list_lambda_functions(
        self, *, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListLambdaFunctionsResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_lambda_functions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_lambda_functions)
        """

    def list_lex_bots(
        self, *, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListLexBotsResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_lex_bots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_lex_bots)
        """

    def list_phone_numbers(
        self,
        *,
        InstanceId: str,
        PhoneNumberTypes: List[PhoneNumberTypeType] = None,
        PhoneNumberCountryCodes: List[PhoneNumberCountryCodeType] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListPhoneNumbersResponseTypeDef:
        """
        Provides information about the phone numbers for the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_phone_numbers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_phone_numbers)
        """

    def list_phone_numbers_v2(
        self,
        *,
        TargetArn: str = None,
        InstanceId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        PhoneNumberCountryCodes: List[PhoneNumberCountryCodeType] = None,
        PhoneNumberTypes: List[PhoneNumberTypeType] = None,
        PhoneNumberPrefix: str = None
    ) -> ListPhoneNumbersV2ResponseTypeDef:
        """
        Lists phone numbers claimed to your Amazon Connect instance or traffic
        distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_phone_numbers_v2)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_phone_numbers_v2)
        """

    def list_predefined_attributes(
        self, *, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListPredefinedAttributesResponseTypeDef:
        """
        Lists predefined attributes for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_predefined_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_predefined_attributes)
        """

    def list_prompts(
        self, *, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListPromptsResponseTypeDef:
        """
        Provides information about the prompts for the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_prompts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_prompts)
        """

    def list_queue_quick_connects(
        self, *, InstanceId: str, QueueId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListQueueQuickConnectsResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_queue_quick_connects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_queue_quick_connects)
        """

    def list_queues(
        self,
        *,
        InstanceId: str,
        QueueTypes: List[QueueTypeType] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListQueuesResponseTypeDef:
        """
        Provides information about the queues for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_queues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_queues)
        """

    def list_quick_connects(
        self,
        *,
        InstanceId: str,
        NextToken: str = None,
        MaxResults: int = None,
        QuickConnectTypes: List[QuickConnectTypeType] = None
    ) -> ListQuickConnectsResponseTypeDef:
        """
        Provides information about the quick connects for the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_quick_connects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_quick_connects)
        """

    def list_realtime_contact_analysis_segments_v2(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        OutputType: RealTimeContactAnalysisOutputTypeType,
        SegmentTypes: List[RealTimeContactAnalysisSegmentTypeType],
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListRealtimeContactAnalysisSegmentsV2ResponseTypeDef:
        """
        Provides a list of analysis segments for a real-time analysis session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_realtime_contact_analysis_segments_v2)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_realtime_contact_analysis_segments_v2)
        """

    def list_routing_profile_queues(
        self,
        *,
        InstanceId: str,
        RoutingProfileId: str,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListRoutingProfileQueuesResponseTypeDef:
        """
        Lists the queues associated with a routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_routing_profile_queues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_routing_profile_queues)
        """

    def list_routing_profiles(
        self, *, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListRoutingProfilesResponseTypeDef:
        """
        Provides summary information about the routing profiles for the specified Amazon
        Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_routing_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_routing_profiles)
        """

    def list_rules(
        self,
        *,
        InstanceId: str,
        PublishStatus: RulePublishStatusType = None,
        EventSourceName: EventSourceNameType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListRulesResponseTypeDef:
        """
        List all rules for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_rules)
        """

    def list_security_keys(
        self, *, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListSecurityKeysResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_security_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_security_keys)
        """

    def list_security_profile_applications(
        self,
        *,
        SecurityProfileId: str,
        InstanceId: str,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListSecurityProfileApplicationsResponseTypeDef:
        """
        Returns a list of third-party applications in a specific security profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_security_profile_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_security_profile_applications)
        """

    def list_security_profile_permissions(
        self,
        *,
        SecurityProfileId: str,
        InstanceId: str,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListSecurityProfilePermissionsResponseTypeDef:
        """
        Lists the permissions granted to a security profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_security_profile_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_security_profile_permissions)
        """

    def list_security_profiles(
        self, *, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListSecurityProfilesResponseTypeDef:
        """
        Provides summary information about the security profiles for the specified
        Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_security_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_security_profiles)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_tags_for_resource)
        """

    def list_task_templates(
        self,
        *,
        InstanceId: str,
        NextToken: str = None,
        MaxResults: int = None,
        Status: TaskTemplateStatusType = None,
        Name: str = None
    ) -> ListTaskTemplatesResponseTypeDef:
        """
        Lists task templates for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_task_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_task_templates)
        """

    def list_traffic_distribution_group_users(
        self, *, TrafficDistributionGroupId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTrafficDistributionGroupUsersResponseTypeDef:
        """
        Lists traffic distribution group users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_traffic_distribution_group_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_traffic_distribution_group_users)
        """

    def list_traffic_distribution_groups(
        self, *, MaxResults: int = None, NextToken: str = None, InstanceId: str = None
    ) -> ListTrafficDistributionGroupsResponseTypeDef:
        """
        Lists traffic distribution groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_traffic_distribution_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_traffic_distribution_groups)
        """

    def list_use_cases(
        self,
        *,
        InstanceId: str,
        IntegrationAssociationId: str,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListUseCasesResponseTypeDef:
        """
        Lists the use cases for the integration association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_use_cases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_use_cases)
        """

    def list_user_hierarchy_groups(
        self, *, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListUserHierarchyGroupsResponseTypeDef:
        """
        Provides summary information about the hierarchy groups for the specified Amazon
        Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_user_hierarchy_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_user_hierarchy_groups)
        """

    def list_user_proficiencies(
        self, *, InstanceId: str, UserId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListUserProficienciesResponseTypeDef:
        """
        Lists proficiencies associated with a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_user_proficiencies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_user_proficiencies)
        """

    def list_users(
        self, *, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListUsersResponseTypeDef:
        """
        Provides summary information about the users for the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_users)
        """

    def list_view_versions(
        self, *, InstanceId: str, ViewId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListViewVersionsResponseTypeDef:
        """
        Returns all the available versions for the specified Amazon Connect instance and
        view identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_view_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_view_versions)
        """

    def list_views(
        self,
        *,
        InstanceId: str,
        Type: ViewTypeType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListViewsResponseTypeDef:
        """
        Returns views in the given instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.list_views)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#list_views)
        """

    def monitor_contact(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        UserId: str,
        AllowedMonitorCapabilities: List[MonitorCapabilityType] = None,
        ClientToken: str = None
    ) -> MonitorContactResponseTypeDef:
        """
        Initiates silent monitoring of a contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.monitor_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#monitor_contact)
        """

    def pause_contact(
        self, *, ContactId: str, InstanceId: str, ContactFlowId: str = None
    ) -> Dict[str, Any]:
        """
        Allows pausing an ongoing task contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.pause_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#pause_contact)
        """

    def put_user_status(
        self, *, UserId: str, InstanceId: str, AgentStatusId: str
    ) -> Dict[str, Any]:
        """
        Changes the current status of a user or agent in Amazon Connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.put_user_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#put_user_status)
        """

    def release_phone_number(self, *, PhoneNumberId: str, ClientToken: str = None) -> None:
        """
        Releases a phone number previously claimed to an Amazon Connect instance or
        traffic distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.release_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#release_phone_number)
        """

    def replicate_instance(
        self, *, InstanceId: str, ReplicaRegion: str, ReplicaAlias: str, ClientToken: str = None
    ) -> ReplicateInstanceResponseTypeDef:
        """
        Replicates an Amazon Connect instance in the specified Amazon Web Services
        Region and copies configuration information for Amazon Connect resources across
        Amazon Web Services Regions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.replicate_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#replicate_instance)
        """

    def resume_contact(
        self, *, ContactId: str, InstanceId: str, ContactFlowId: str = None
    ) -> Dict[str, Any]:
        """
        Allows resuming a task contact in a paused state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.resume_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#resume_contact)
        """

    def resume_contact_recording(
        self, *, InstanceId: str, ContactId: str, InitialContactId: str
    ) -> Dict[str, Any]:
        """
        When a contact is being recorded, and the recording has been suspended using
        SuspendContactRecording, this API resumes recording whatever recording is
        selected in the flow configuration: call, screen, or both.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.resume_contact_recording)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#resume_contact_recording)
        """

    def search_available_phone_numbers(
        self,
        *,
        PhoneNumberCountryCode: PhoneNumberCountryCodeType,
        PhoneNumberType: PhoneNumberTypeType,
        TargetArn: str = None,
        InstanceId: str = None,
        PhoneNumberPrefix: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> SearchAvailablePhoneNumbersResponseTypeDef:
        """
        Searches for available phone numbers that you can claim to your Amazon Connect
        instance or traffic distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.search_available_phone_numbers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#search_available_phone_numbers)
        """

    def search_contact_flow_modules(
        self,
        *,
        InstanceId: str,
        NextToken: str = None,
        MaxResults: int = None,
        SearchFilter: "ContactFlowModuleSearchFilterTypeDef" = None,
        SearchCriteria: "ContactFlowModuleSearchCriteriaTypeDef" = None
    ) -> SearchContactFlowModulesResponseTypeDef:
        """
        Searches the flow modules in an Amazon Connect instance, with optional
        filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.search_contact_flow_modules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#search_contact_flow_modules)
        """

    def search_contact_flows(
        self,
        *,
        InstanceId: str,
        NextToken: str = None,
        MaxResults: int = None,
        SearchFilter: "ContactFlowSearchFilterTypeDef" = None,
        SearchCriteria: "ContactFlowSearchCriteriaTypeDef" = None
    ) -> SearchContactFlowsResponseTypeDef:
        """
        Searches the contact flows in an Amazon Connect instance, with optional
        filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.search_contact_flows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#search_contact_flows)
        """

    def search_contacts(
        self,
        *,
        InstanceId: str,
        TimeRange: "SearchContactsTimeRangeTypeDef",
        SearchCriteria: "SearchCriteriaTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None,
        Sort: "SortTypeDef" = None
    ) -> SearchContactsResponseTypeDef:
        """
        Searches contacts in an Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.search_contacts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#search_contacts)
        """

    def search_hours_of_operations(
        self,
        *,
        InstanceId: str,
        NextToken: str = None,
        MaxResults: int = None,
        SearchFilter: "HoursOfOperationSearchFilterTypeDef" = None,
        SearchCriteria: "HoursOfOperationSearchCriteriaTypeDef" = None
    ) -> SearchHoursOfOperationsResponseTypeDef:
        """
        Searches the hours of operation in an Amazon Connect instance, with optional
        filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.search_hours_of_operations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#search_hours_of_operations)
        """

    def search_predefined_attributes(
        self,
        *,
        InstanceId: str,
        NextToken: str = None,
        MaxResults: int = None,
        SearchCriteria: "PredefinedAttributeSearchCriteriaTypeDef" = None
    ) -> SearchPredefinedAttributesResponseTypeDef:
        """
        Predefined attributes that meet certain criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.search_predefined_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#search_predefined_attributes)
        """

    def search_prompts(
        self,
        *,
        InstanceId: str,
        NextToken: str = None,
        MaxResults: int = None,
        SearchFilter: "PromptSearchFilterTypeDef" = None,
        SearchCriteria: "PromptSearchCriteriaTypeDef" = None
    ) -> SearchPromptsResponseTypeDef:
        """
        Searches prompts in an Amazon Connect instance, with optional filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.search_prompts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#search_prompts)
        """

    def search_queues(
        self,
        *,
        InstanceId: str,
        NextToken: str = None,
        MaxResults: int = None,
        SearchFilter: "QueueSearchFilterTypeDef" = None,
        SearchCriteria: "QueueSearchCriteriaTypeDef" = None
    ) -> SearchQueuesResponseTypeDef:
        """
        Searches queues in an Amazon Connect instance, with optional filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.search_queues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#search_queues)
        """

    def search_quick_connects(
        self,
        *,
        InstanceId: str,
        NextToken: str = None,
        MaxResults: int = None,
        SearchFilter: "QuickConnectSearchFilterTypeDef" = None,
        SearchCriteria: "QuickConnectSearchCriteriaTypeDef" = None
    ) -> SearchQuickConnectsResponseTypeDef:
        """
        Searches quick connects in an Amazon Connect instance, with optional filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.search_quick_connects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#search_quick_connects)
        """

    def search_resource_tags(
        self,
        *,
        InstanceId: str,
        ResourceTypes: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        SearchCriteria: "ResourceTagsSearchCriteriaTypeDef" = None
    ) -> SearchResourceTagsResponseTypeDef:
        """
        Searches tags used in an Amazon Connect instance using optional search criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.search_resource_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#search_resource_tags)
        """

    def search_routing_profiles(
        self,
        *,
        InstanceId: str,
        NextToken: str = None,
        MaxResults: int = None,
        SearchFilter: "RoutingProfileSearchFilterTypeDef" = None,
        SearchCriteria: "RoutingProfileSearchCriteriaTypeDef" = None
    ) -> SearchRoutingProfilesResponseTypeDef:
        """
        Searches routing profiles in an Amazon Connect instance, with optional
        filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.search_routing_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#search_routing_profiles)
        """

    def search_security_profiles(
        self,
        *,
        InstanceId: str,
        NextToken: str = None,
        MaxResults: int = None,
        SearchCriteria: "SecurityProfileSearchCriteriaTypeDef" = None,
        SearchFilter: "SecurityProfilesSearchFilterTypeDef" = None
    ) -> SearchSecurityProfilesResponseTypeDef:
        """
        Searches security profiles in an Amazon Connect instance, with optional
        filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.search_security_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#search_security_profiles)
        """

    def search_users(
        self,
        *,
        InstanceId: str,
        NextToken: str = None,
        MaxResults: int = None,
        SearchFilter: "UserSearchFilterTypeDef" = None,
        SearchCriteria: "UserSearchCriteriaTypeDef" = None
    ) -> SearchUsersResponseTypeDef:
        """
        Searches users in an Amazon Connect instance, with optional filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.search_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#search_users)
        """

    def search_vocabularies(
        self,
        *,
        InstanceId: str,
        MaxResults: int = None,
        NextToken: str = None,
        State: VocabularyStateType = None,
        NameStartsWith: str = None,
        LanguageCode: VocabularyLanguageCodeType = None
    ) -> SearchVocabulariesResponseTypeDef:
        """
        Searches for vocabularies within a specific Amazon Connect instance using
        `State`, `NameStartsWith`, and `LanguageCode`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.search_vocabularies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#search_vocabularies)
        """

    def send_chat_integration_event(
        self,
        *,
        SourceId: str,
        DestinationId: str,
        Event: "ChatEventTypeDef",
        Subtype: str = None,
        NewSessionDetails: "NewSessionDetailsTypeDef" = None
    ) -> SendChatIntegrationEventResponseTypeDef:
        """
        Processes chat integration events from Amazon Web Services or external
        integrations to Amazon Connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.send_chat_integration_event)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#send_chat_integration_event)
        """

    def start_attached_file_upload(
        self,
        *,
        InstanceId: str,
        FileName: str,
        FileSizeInBytes: int,
        FileUseCaseType: Literal["ATTACHMENT"],
        AssociatedResourceArn: str,
        ClientToken: str = None,
        UrlExpiryInSeconds: int = None,
        CreatedBy: "CreatedByInfoTypeDef" = None,
        Tags: Dict[str, str] = None
    ) -> StartAttachedFileUploadResponseTypeDef:
        """
        Provides a pre-signed Amazon S3 URL in response for uploading your content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.start_attached_file_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#start_attached_file_upload)
        """

    def start_chat_contact(
        self,
        *,
        InstanceId: str,
        ContactFlowId: str,
        ParticipantDetails: "ParticipantDetailsTypeDef",
        Attributes: Dict[str, str] = None,
        InitialMessage: "ChatMessageTypeDef" = None,
        ClientToken: str = None,
        ChatDurationInMinutes: int = None,
        SupportedMessagingContentTypes: List[str] = None,
        PersistentChat: "PersistentChatTypeDef" = None,
        RelatedContactId: str = None,
        SegmentAttributes: Dict[str, "SegmentAttributeValueTypeDef"] = None
    ) -> StartChatContactResponseTypeDef:
        """
        Initiates a flow to start a new chat for the customer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.start_chat_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#start_chat_contact)
        """

    def start_contact_evaluation(
        self, *, InstanceId: str, ContactId: str, EvaluationFormId: str, ClientToken: str = None
    ) -> StartContactEvaluationResponseTypeDef:
        """
        Starts an empty evaluation in the specified Amazon Connect instance, using the
        given evaluation form for the particular contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.start_contact_evaluation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#start_contact_evaluation)
        """

    def start_contact_recording(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        InitialContactId: str,
        VoiceRecordingConfiguration: "VoiceRecordingConfigurationTypeDef"
    ) -> Dict[str, Any]:
        """
        Starts recording the contact * If the API is called *before* the agent joins the
        call, recording starts when the agent joins the call.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.start_contact_recording)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#start_contact_recording)
        """

    def start_contact_streaming(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        ChatStreamingConfiguration: "ChatStreamingConfigurationTypeDef",
        ClientToken: str
    ) -> StartContactStreamingResponseTypeDef:
        """
        Initiates real-time message streaming for a new chat contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.start_contact_streaming)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#start_contact_streaming)
        """

    def start_outbound_voice_contact(
        self,
        *,
        DestinationPhoneNumber: str,
        ContactFlowId: str,
        InstanceId: str,
        Name: str = None,
        Description: str = None,
        References: Dict[str, "ReferenceTypeDef"] = None,
        RelatedContactId: str = None,
        ClientToken: str = None,
        SourcePhoneNumber: str = None,
        QueueId: str = None,
        Attributes: Dict[str, str] = None,
        AnswerMachineDetectionConfig: "AnswerMachineDetectionConfigTypeDef" = None,
        CampaignId: str = None,
        TrafficType: TrafficTypeType = None
    ) -> StartOutboundVoiceContactResponseTypeDef:
        """
        Places an outbound call to a contact, and then initiates the flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.start_outbound_voice_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#start_outbound_voice_contact)
        """

    def start_task_contact(
        self,
        *,
        InstanceId: str,
        Name: str,
        PreviousContactId: str = None,
        ContactFlowId: str = None,
        Attributes: Dict[str, str] = None,
        References: Dict[str, "ReferenceTypeDef"] = None,
        Description: str = None,
        ClientToken: str = None,
        ScheduledTime: Union[datetime, str] = None,
        TaskTemplateId: str = None,
        QuickConnectId: str = None,
        RelatedContactId: str = None
    ) -> StartTaskContactResponseTypeDef:
        """
        Initiates a flow to start a new task contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.start_task_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#start_task_contact)
        """

    def start_web_rtc_contact(
        self,
        *,
        ContactFlowId: str,
        InstanceId: str,
        ParticipantDetails: "ParticipantDetailsTypeDef",
        Attributes: Dict[str, str] = None,
        ClientToken: str = None,
        AllowedCapabilities: "AllowedCapabilitiesTypeDef" = None,
        RelatedContactId: str = None,
        References: Dict[str, "ReferenceTypeDef"] = None,
        Description: str = None
    ) -> StartWebRTCContactResponseTypeDef:
        """
        Places an inbound in-app, web, or video call to a contact, and then initiates
        the flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.start_web_rtc_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#start_web_rtc_contact)
        """

    def stop_contact(
        self, *, ContactId: str, InstanceId: str, DisconnectReason: "DisconnectReasonTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Ends the specified contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.stop_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#stop_contact)
        """

    def stop_contact_recording(
        self, *, InstanceId: str, ContactId: str, InitialContactId: str
    ) -> Dict[str, Any]:
        """
        Stops recording a call when a contact is being recorded.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.stop_contact_recording)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#stop_contact_recording)
        """

    def stop_contact_streaming(
        self, *, InstanceId: str, ContactId: str, StreamingId: str
    ) -> Dict[str, Any]:
        """
        Ends message streaming on a specified contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.stop_contact_streaming)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#stop_contact_streaming)
        """

    def submit_contact_evaluation(
        self,
        *,
        InstanceId: str,
        EvaluationId: str,
        Answers: Dict[str, "EvaluationAnswerInputTypeDef"] = None,
        Notes: Dict[str, "EvaluationNoteTypeDef"] = None
    ) -> SubmitContactEvaluationResponseTypeDef:
        """
        Submits a contact evaluation in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.submit_contact_evaluation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#submit_contact_evaluation)
        """

    def suspend_contact_recording(
        self, *, InstanceId: str, ContactId: str, InitialContactId: str
    ) -> Dict[str, Any]:
        """
        When a contact is being recorded, this API suspends recording whatever is
        selected in the flow configuration: call, screen, or both.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.suspend_contact_recording)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#suspend_contact_recording)
        """

    def tag_contact(
        self, *, ContactId: str, InstanceId: str, Tags: Dict[str, str]
    ) -> Dict[str, Any]:
        """
        Adds the specified tags to the contact resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.tag_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#tag_contact)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> None:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#tag_resource)
        """

    def transfer_contact(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        ContactFlowId: str,
        QueueId: str = None,
        UserId: str = None,
        ClientToken: str = None
    ) -> TransferContactResponseTypeDef:
        """
        Transfers contacts from one agent or queue to another agent or queue at any
        point after a contact is created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.transfer_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#transfer_contact)
        """

    def untag_contact(
        self, *, ContactId: str, InstanceId: str, TagKeys: List[str]
    ) -> Dict[str, Any]:
        """
        Removes the specified tags from the contact resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.untag_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#untag_contact)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> None:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#untag_resource)
        """

    def update_agent_status(
        self,
        *,
        InstanceId: str,
        AgentStatusId: str,
        Name: str = None,
        Description: str = None,
        State: AgentStatusStateType = None,
        DisplayOrder: int = None,
        ResetOrderNumber: bool = None
    ) -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_agent_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_agent_status)
        """

    def update_authentication_profile(
        self,
        *,
        AuthenticationProfileId: str,
        InstanceId: str,
        Name: str = None,
        Description: str = None,
        AllowedIps: List[str] = None,
        BlockedIps: List[str] = None,
        PeriodicSessionDuration: int = None
    ) -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_authentication_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_authentication_profile)
        """

    def update_contact(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        Name: str = None,
        Description: str = None,
        References: Dict[str, "ReferenceTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_contact)
        """

    def update_contact_attributes(
        self, *, InitialContactId: str, InstanceId: str, Attributes: Dict[str, str]
    ) -> Dict[str, Any]:
        """
        Creates or updates user-defined contact attributes associated with the specified
        contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_contact_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_contact_attributes)
        """

    def update_contact_evaluation(
        self,
        *,
        InstanceId: str,
        EvaluationId: str,
        Answers: Dict[str, "EvaluationAnswerInputTypeDef"] = None,
        Notes: Dict[str, "EvaluationNoteTypeDef"] = None
    ) -> UpdateContactEvaluationResponseTypeDef:
        """
        Updates details about a contact evaluation in the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_contact_evaluation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_contact_evaluation)
        """

    def update_contact_flow_content(
        self, *, InstanceId: str, ContactFlowId: str, Content: str
    ) -> Dict[str, Any]:
        """
        Updates the specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_contact_flow_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_contact_flow_content)
        """

    def update_contact_flow_metadata(
        self,
        *,
        InstanceId: str,
        ContactFlowId: str,
        Name: str = None,
        Description: str = None,
        ContactFlowState: ContactFlowStateType = None
    ) -> Dict[str, Any]:
        """
        Updates metadata about specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_contact_flow_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_contact_flow_metadata)
        """

    def update_contact_flow_module_content(
        self, *, InstanceId: str, ContactFlowModuleId: str, Content: str
    ) -> Dict[str, Any]:
        """
        Updates specified flow module for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_contact_flow_module_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_contact_flow_module_content)
        """

    def update_contact_flow_module_metadata(
        self,
        *,
        InstanceId: str,
        ContactFlowModuleId: str,
        Name: str = None,
        Description: str = None,
        State: ContactFlowModuleStateType = None
    ) -> Dict[str, Any]:
        """
        Updates metadata about specified flow module.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_contact_flow_module_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_contact_flow_module_metadata)
        """

    def update_contact_flow_name(
        self, *, InstanceId: str, ContactFlowId: str, Name: str = None, Description: str = None
    ) -> Dict[str, Any]:
        """
        The name of the flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_contact_flow_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_contact_flow_name)
        """

    def update_contact_routing_data(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        QueueTimeAdjustmentSeconds: int = None,
        QueuePriority: int = None
    ) -> Dict[str, Any]:
        """
        Updates routing priority and age on the contact (**QueuePriority** and
        **QueueTimeAdjustmentInSeconds**).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_contact_routing_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_contact_routing_data)
        """

    def update_contact_schedule(
        self, *, InstanceId: str, ContactId: str, ScheduledTime: Union[datetime, str]
    ) -> Dict[str, Any]:
        """
        Updates the scheduled time of a task contact that is already scheduled.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_contact_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_contact_schedule)
        """

    def update_evaluation_form(
        self,
        *,
        InstanceId: str,
        EvaluationFormId: str,
        EvaluationFormVersion: int,
        Title: str,
        Items: List["EvaluationFormItemTypeDef"],
        CreateNewVersion: bool = None,
        Description: str = None,
        ScoringStrategy: "EvaluationFormScoringStrategyTypeDef" = None,
        ClientToken: str = None
    ) -> UpdateEvaluationFormResponseTypeDef:
        """
        Updates details about a specific evaluation form version in the specified Amazon
        Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_evaluation_form)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_evaluation_form)
        """

    def update_hours_of_operation(
        self,
        *,
        InstanceId: str,
        HoursOfOperationId: str,
        Name: str = None,
        Description: str = None,
        TimeZone: str = None,
        Config: List["HoursOfOperationConfigTypeDef"] = None
    ) -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_hours_of_operation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_hours_of_operation)
        """

    def update_instance_attribute(
        self, *, InstanceId: str, AttributeType: InstanceAttributeTypeType, Value: str
    ) -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_instance_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_instance_attribute)
        """

    def update_instance_storage_config(
        self,
        *,
        InstanceId: str,
        AssociationId: str,
        ResourceType: InstanceStorageResourceTypeType,
        StorageConfig: "InstanceStorageConfigTypeDef"
    ) -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_instance_storage_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_instance_storage_config)
        """

    def update_participant_role_config(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        ChannelConfiguration: "UpdateParticipantRoleConfigChannelInfoTypeDef"
    ) -> Dict[str, Any]:
        """
        Updates timeouts for when human chat participants are to be considered idle, and
        when agents are automatically disconnected from a chat due to idleness.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_participant_role_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_participant_role_config)
        """

    def update_phone_number(
        self,
        *,
        PhoneNumberId: str,
        TargetArn: str = None,
        InstanceId: str = None,
        ClientToken: str = None
    ) -> UpdatePhoneNumberResponseTypeDef:
        """
        Updates your claimed phone number from its current Amazon Connect instance or
        traffic distribution group to another Amazon Connect instance or traffic
        distribution group in the same Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_phone_number)
        """

    def update_phone_number_metadata(
        self, *, PhoneNumberId: str, PhoneNumberDescription: str = None, ClientToken: str = None
    ) -> None:
        """
        Updates a phone number’s metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_phone_number_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_phone_number_metadata)
        """

    def update_predefined_attribute(
        self, *, InstanceId: str, Name: str, Values: "PredefinedAttributeValuesTypeDef" = None
    ) -> None:
        """
        Updates a predefined attribute for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_predefined_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_predefined_attribute)
        """

    def update_prompt(
        self,
        *,
        InstanceId: str,
        PromptId: str,
        Name: str = None,
        Description: str = None,
        S3Uri: str = None
    ) -> UpdatePromptResponseTypeDef:
        """
        Updates a prompt.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_prompt)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_prompt)
        """

    def update_queue_hours_of_operation(
        self, *, InstanceId: str, QueueId: str, HoursOfOperationId: str
    ) -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_queue_hours_of_operation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_queue_hours_of_operation)
        """

    def update_queue_max_contacts(
        self, *, InstanceId: str, QueueId: str, MaxContacts: int = None
    ) -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_queue_max_contacts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_queue_max_contacts)
        """

    def update_queue_name(
        self, *, InstanceId: str, QueueId: str, Name: str = None, Description: str = None
    ) -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_queue_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_queue_name)
        """

    def update_queue_outbound_caller_config(
        self, *, InstanceId: str, QueueId: str, OutboundCallerConfig: "OutboundCallerConfigTypeDef"
    ) -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_queue_outbound_caller_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_queue_outbound_caller_config)
        """

    def update_queue_status(
        self, *, InstanceId: str, QueueId: str, Status: QueueStatusType
    ) -> None:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_queue_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_queue_status)
        """

    def update_quick_connect_config(
        self,
        *,
        InstanceId: str,
        QuickConnectId: str,
        QuickConnectConfig: "QuickConnectConfigTypeDef"
    ) -> None:
        """
        Updates the configuration settings for the specified quick connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_quick_connect_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_quick_connect_config)
        """

    def update_quick_connect_name(
        self, *, InstanceId: str, QuickConnectId: str, Name: str = None, Description: str = None
    ) -> None:
        """
        Updates the name and description of a quick connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_quick_connect_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_quick_connect_name)
        """

    def update_routing_profile_agent_availability_timer(
        self,
        *,
        InstanceId: str,
        RoutingProfileId: str,
        AgentAvailabilityTimer: AgentAvailabilityTimerType
    ) -> None:
        """
        Whether agents with this routing profile will have their routing order
        calculated based on *time since their last inbound contact* or *longest idle
        time*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_routing_profile_agent_availability_timer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_routing_profile_agent_availability_timer)
        """

    def update_routing_profile_concurrency(
        self,
        *,
        InstanceId: str,
        RoutingProfileId: str,
        MediaConcurrencies: List["MediaConcurrencyTypeDef"]
    ) -> None:
        """
        Updates the channels that agents can handle in the Contact Control Panel (CCP)
        for a routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_routing_profile_concurrency)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_routing_profile_concurrency)
        """

    def update_routing_profile_default_outbound_queue(
        self, *, InstanceId: str, RoutingProfileId: str, DefaultOutboundQueueId: str
    ) -> None:
        """
        Updates the default outbound queue of a routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_routing_profile_default_outbound_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_routing_profile_default_outbound_queue)
        """

    def update_routing_profile_name(
        self, *, InstanceId: str, RoutingProfileId: str, Name: str = None, Description: str = None
    ) -> None:
        """
        Updates the name and description of a routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_routing_profile_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_routing_profile_name)
        """

    def update_routing_profile_queues(
        self,
        *,
        InstanceId: str,
        RoutingProfileId: str,
        QueueConfigs: List["RoutingProfileQueueConfigTypeDef"]
    ) -> None:
        """
        Updates the properties associated with a set of queues for a routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_routing_profile_queues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_routing_profile_queues)
        """

    def update_rule(
        self,
        *,
        RuleId: str,
        InstanceId: str,
        Name: str,
        Function: str,
        Actions: List["RuleActionTypeDef"],
        PublishStatus: RulePublishStatusType
    ) -> None:
        """
        Updates a rule for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_rule)
        """

    def update_security_profile(
        self,
        *,
        SecurityProfileId: str,
        InstanceId: str,
        Description: str = None,
        Permissions: List[str] = None,
        AllowedAccessControlTags: Dict[str, str] = None,
        TagRestrictedResources: List[str] = None,
        Applications: List["ApplicationTypeDef"] = None,
        HierarchyRestrictedResources: List[str] = None,
        AllowedAccessControlHierarchyGroupId: str = None
    ) -> None:
        """
        Updates a security profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_security_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_security_profile)
        """

    def update_task_template(
        self,
        *,
        TaskTemplateId: str,
        InstanceId: str,
        Name: str = None,
        Description: str = None,
        ContactFlowId: str = None,
        Constraints: "TaskTemplateConstraintsTypeDef" = None,
        Defaults: "TaskTemplateDefaultsTypeDef" = None,
        Status: TaskTemplateStatusType = None,
        Fields: List["TaskTemplateFieldTypeDef"] = None
    ) -> UpdateTaskTemplateResponseTypeDef:
        """
        Updates details about a specific task template in the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_task_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_task_template)
        """

    def update_traffic_distribution(
        self,
        *,
        Id: str,
        TelephonyConfig: "TelephonyConfigTypeDef" = None,
        SignInConfig: "SignInConfigTypeDef" = None,
        AgentConfig: "AgentConfigTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates the traffic distribution for a given traffic distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_traffic_distribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_traffic_distribution)
        """

    def update_user_hierarchy(
        self, *, UserId: str, InstanceId: str, HierarchyGroupId: str = None
    ) -> None:
        """
        Assigns the specified hierarchy group to the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_user_hierarchy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_user_hierarchy)
        """

    def update_user_hierarchy_group_name(
        self, *, Name: str, HierarchyGroupId: str, InstanceId: str
    ) -> None:
        """
        Updates the name of the user hierarchy group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_user_hierarchy_group_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_user_hierarchy_group_name)
        """

    def update_user_hierarchy_structure(
        self, *, HierarchyStructure: "HierarchyStructureUpdateTypeDef", InstanceId: str
    ) -> None:
        """
        Updates the user hierarchy structure: add, remove, and rename user hierarchy
        levels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_user_hierarchy_structure)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_user_hierarchy_structure)
        """

    def update_user_identity_info(
        self, *, IdentityInfo: "UserIdentityInfoTypeDef", UserId: str, InstanceId: str
    ) -> None:
        """
        Updates the identity information for the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_user_identity_info)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_user_identity_info)
        """

    def update_user_phone_config(
        self, *, PhoneConfig: "UserPhoneConfigTypeDef", UserId: str, InstanceId: str
    ) -> None:
        """
        Updates the phone configuration settings for the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_user_phone_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_user_phone_config)
        """

    def update_user_proficiencies(
        self, *, InstanceId: str, UserId: str, UserProficiencies: List["UserProficiencyTypeDef"]
    ) -> None:
        """
        Updates the properties associated with the proficiencies of a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_user_proficiencies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_user_proficiencies)
        """

    def update_user_routing_profile(
        self, *, RoutingProfileId: str, UserId: str, InstanceId: str
    ) -> None:
        """
        Assigns the specified routing profile to the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_user_routing_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_user_routing_profile)
        """

    def update_user_security_profiles(
        self, *, SecurityProfileIds: List[str], UserId: str, InstanceId: str
    ) -> None:
        """
        Assigns the specified security profiles to the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_user_security_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_user_security_profiles)
        """

    def update_view_content(
        self,
        *,
        InstanceId: str,
        ViewId: str,
        Status: ViewStatusType,
        Content: "ViewInputContentTypeDef"
    ) -> UpdateViewContentResponseTypeDef:
        """
        Updates the view content of the given view identifier in the specified Amazon
        Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_view_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_view_content)
        """

    def update_view_metadata(
        self, *, InstanceId: str, ViewId: str, Name: str = None, Description: str = None
    ) -> Dict[str, Any]:
        """
        Updates the view metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Client.update_view_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/client.html#update_view_metadata)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_metric_data"]) -> GetMetricDataPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.GetMetricData)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#getmetricdatapaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_agent_statuses"]
    ) -> ListAgentStatusesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListAgentStatuses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listagentstatusespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_approved_origins"]
    ) -> ListApprovedOriginsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListApprovedOrigins)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listapprovedoriginspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_authentication_profiles"]
    ) -> ListAuthenticationProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListAuthenticationProfiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listauthenticationprofilespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_bots"]) -> ListBotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListBots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listbotspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_contact_evaluations"]
    ) -> ListContactEvaluationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListContactEvaluations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listcontactevaluationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_contact_flow_modules"]
    ) -> ListContactFlowModulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListContactFlowModules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listcontactflowmodulespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_contact_flows"]
    ) -> ListContactFlowsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListContactFlows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listcontactflowspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_contact_references"]
    ) -> ListContactReferencesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListContactReferences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listcontactreferencespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_default_vocabularies"]
    ) -> ListDefaultVocabulariesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListDefaultVocabularies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listdefaultvocabulariespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_evaluation_form_versions"]
    ) -> ListEvaluationFormVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListEvaluationFormVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listevaluationformversionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_evaluation_forms"]
    ) -> ListEvaluationFormsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListEvaluationForms)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listevaluationformspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_flow_associations"]
    ) -> ListFlowAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListFlowAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listflowassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_hours_of_operations"]
    ) -> ListHoursOfOperationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListHoursOfOperations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listhoursofoperationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_attributes"]
    ) -> ListInstanceAttributesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListInstanceAttributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listinstanceattributespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_storage_configs"]
    ) -> ListInstanceStorageConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListInstanceStorageConfigs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listinstancestorageconfigspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_instances"]) -> ListInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listinstancespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_integration_associations"]
    ) -> ListIntegrationAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListIntegrationAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listintegrationassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_lambda_functions"]
    ) -> ListLambdaFunctionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListLambdaFunctions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listlambdafunctionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_lex_bots"]) -> ListLexBotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListLexBots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listlexbotspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_phone_numbers"]
    ) -> ListPhoneNumbersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListPhoneNumbers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listphonenumberspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_phone_numbers_v2"]
    ) -> ListPhoneNumbersV2Paginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListPhoneNumbersV2)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listphonenumbersv2paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_predefined_attributes"]
    ) -> ListPredefinedAttributesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListPredefinedAttributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listpredefinedattributespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_prompts"]) -> ListPromptsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListPrompts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listpromptspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_queue_quick_connects"]
    ) -> ListQueueQuickConnectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListQueueQuickConnects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listqueuequickconnectspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_queues"]) -> ListQueuesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListQueues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listqueuespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_quick_connects"]
    ) -> ListQuickConnectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListQuickConnects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listquickconnectspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_routing_profile_queues"]
    ) -> ListRoutingProfileQueuesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListRoutingProfileQueues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listroutingprofilequeuespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_routing_profiles"]
    ) -> ListRoutingProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListRoutingProfiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listroutingprofilespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_rules"]) -> ListRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListRules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listrulespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_keys"]
    ) -> ListSecurityKeysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListSecurityKeys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listsecuritykeyspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_profile_applications"]
    ) -> ListSecurityProfileApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListSecurityProfileApplications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listsecurityprofileapplicationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_profile_permissions"]
    ) -> ListSecurityProfilePermissionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListSecurityProfilePermissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listsecurityprofilepermissionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_profiles"]
    ) -> ListSecurityProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListSecurityProfiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listsecurityprofilespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_task_templates"]
    ) -> ListTaskTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListTaskTemplates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listtasktemplatespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_traffic_distribution_group_users"]
    ) -> ListTrafficDistributionGroupUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListTrafficDistributionGroupUsers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listtrafficdistributiongroupuserspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_traffic_distribution_groups"]
    ) -> ListTrafficDistributionGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListTrafficDistributionGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listtrafficdistributiongroupspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_use_cases"]) -> ListUseCasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListUseCases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listusecasespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_user_hierarchy_groups"]
    ) -> ListUserHierarchyGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListUserHierarchyGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listuserhierarchygroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_user_proficiencies"]
    ) -> ListUserProficienciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListUserProficiencies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listuserproficienciespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_users"]) -> ListUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListUsers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listuserspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_view_versions"]
    ) -> ListViewVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListViewVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listviewversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_views"]) -> ListViewsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.ListViews)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#listviewspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_available_phone_numbers"]
    ) -> SearchAvailablePhoneNumbersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.SearchAvailablePhoneNumbers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#searchavailablephonenumberspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_contact_flow_modules"]
    ) -> SearchContactFlowModulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.SearchContactFlowModules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#searchcontactflowmodulespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_contact_flows"]
    ) -> SearchContactFlowsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.SearchContactFlows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#searchcontactflowspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_contacts"]) -> SearchContactsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.SearchContacts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#searchcontactspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_hours_of_operations"]
    ) -> SearchHoursOfOperationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.SearchHoursOfOperations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#searchhoursofoperationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_predefined_attributes"]
    ) -> SearchPredefinedAttributesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.SearchPredefinedAttributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#searchpredefinedattributespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_prompts"]) -> SearchPromptsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.SearchPrompts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#searchpromptspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_queues"]) -> SearchQueuesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.SearchQueues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#searchqueuespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_quick_connects"]
    ) -> SearchQuickConnectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.SearchQuickConnects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#searchquickconnectspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_resource_tags"]
    ) -> SearchResourceTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.SearchResourceTags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#searchresourcetagspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_routing_profiles"]
    ) -> SearchRoutingProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.SearchRoutingProfiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#searchroutingprofilespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_security_profiles"]
    ) -> SearchSecurityProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.SearchSecurityProfiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#searchsecurityprofilespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_users"]) -> SearchUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.SearchUsers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#searchuserspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_vocabularies"]
    ) -> SearchVocabulariesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/connect.html#Connect.Paginator.SearchVocabularies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/paginators.html#searchvocabulariespaginator)
        """
