"""
Main interface for connect service client

Usage::

    ```python
    import boto3
    from mypy_boto3_connect import ConnectClient

    client: ConnectClient = boto3.client("connect")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_connect.paginator import (
    GetMetricDataPaginator,
    ListApprovedOriginsPaginator,
    ListContactFlowsPaginator,
    ListHoursOfOperationsPaginator,
    ListInstanceAttributesPaginator,
    ListInstancesPaginator,
    ListInstanceStorageConfigsPaginator,
    ListIntegrationAssociationsPaginator,
    ListLambdaFunctionsPaginator,
    ListLexBotsPaginator,
    ListPhoneNumbersPaginator,
    ListPromptsPaginator,
    ListQueueQuickConnectsPaginator,
    ListQueuesPaginator,
    ListQuickConnectsPaginator,
    ListRoutingProfileQueuesPaginator,
    ListRoutingProfilesPaginator,
    ListSecurityKeysPaginator,
    ListSecurityProfilesPaginator,
    ListUseCasesPaginator,
    ListUserHierarchyGroupsPaginator,
    ListUsersPaginator,
)
from mypy_boto3_connect.type_defs import (
    AssociateInstanceStorageConfigResponseTypeDef,
    AssociateSecurityKeyResponseTypeDef,
    ChatMessageTypeDef,
    CreateContactFlowResponseTypeDef,
    CreateInstanceResponseTypeDef,
    CreateIntegrationAssociationResponseTypeDef,
    CreateQueueResponseTypeDef,
    CreateQuickConnectResponseTypeDef,
    CreateRoutingProfileResponseTypeDef,
    CreateUseCaseResponseTypeDef,
    CreateUserHierarchyGroupResponseTypeDef,
    CreateUserResponseTypeDef,
    CurrentMetricTypeDef,
    DescribeContactFlowResponseTypeDef,
    DescribeHoursOfOperationResponseTypeDef,
    DescribeInstanceAttributeResponseTypeDef,
    DescribeInstanceResponseTypeDef,
    DescribeInstanceStorageConfigResponseTypeDef,
    DescribeQueueResponseTypeDef,
    DescribeQuickConnectResponseTypeDef,
    DescribeRoutingProfileResponseTypeDef,
    DescribeUserHierarchyGroupResponseTypeDef,
    DescribeUserHierarchyStructureResponseTypeDef,
    DescribeUserResponseTypeDef,
    FiltersTypeDef,
    GetContactAttributesResponseTypeDef,
    GetCurrentMetricDataResponseTypeDef,
    GetFederationTokenResponseTypeDef,
    GetMetricDataResponseTypeDef,
    HierarchyStructureUpdateTypeDef,
    HistoricalMetricTypeDef,
    InstanceStorageConfigTypeDef,
    LexBotTypeDef,
    ListApprovedOriginsResponseTypeDef,
    ListContactFlowsResponseTypeDef,
    ListHoursOfOperationsResponseTypeDef,
    ListInstanceAttributesResponseTypeDef,
    ListInstancesResponseTypeDef,
    ListInstanceStorageConfigsResponseTypeDef,
    ListIntegrationAssociationsResponseTypeDef,
    ListLambdaFunctionsResponseTypeDef,
    ListLexBotsResponseTypeDef,
    ListPhoneNumbersResponseTypeDef,
    ListPromptsResponseTypeDef,
    ListQueueQuickConnectsResponseTypeDef,
    ListQueuesResponseTypeDef,
    ListQuickConnectsResponseTypeDef,
    ListRoutingProfileQueuesResponseTypeDef,
    ListRoutingProfilesResponseTypeDef,
    ListSecurityKeysResponseTypeDef,
    ListSecurityProfilesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUseCasesResponseTypeDef,
    ListUserHierarchyGroupsResponseTypeDef,
    ListUsersResponseTypeDef,
    MediaConcurrencyTypeDef,
    OutboundCallerConfigTypeDef,
    ParticipantDetailsTypeDef,
    QuickConnectConfigTypeDef,
    ReferenceTypeDef,
    RoutingProfileQueueConfigTypeDef,
    RoutingProfileQueueReferenceTypeDef,
    StartChatContactResponseTypeDef,
    StartOutboundVoiceContactResponseTypeDef,
    StartTaskContactResponseTypeDef,
    UserIdentityInfoTypeDef,
    UserPhoneConfigTypeDef,
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
    ClientError: Type[BotocoreClientError]
    ContactFlowNotPublishedException: Type[BotocoreClientError]
    ContactNotFoundException: Type[BotocoreClientError]
    DestinationNotAllowedException: Type[BotocoreClientError]
    DuplicateResourceException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidContactFlowException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    OutboundContactNotPermittedException: Type[BotocoreClientError]
    ResourceConflictException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UserNotFoundException: Type[BotocoreClientError]


class ConnectClient:
    """
    [Connect.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_approved_origin(self, InstanceId: str, Origin: str) -> None:
        """
        [Client.associate_approved_origin documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.associate_approved_origin)
        """

    def associate_instance_storage_config(
        self,
        InstanceId: str,
        ResourceType: Literal[
            "CHAT_TRANSCRIPTS",
            "CALL_RECORDINGS",
            "SCHEDULED_REPORTS",
            "MEDIA_STREAMS",
            "CONTACT_TRACE_RECORDS",
            "AGENT_EVENTS",
        ],
        StorageConfig: "InstanceStorageConfigTypeDef",
    ) -> AssociateInstanceStorageConfigResponseTypeDef:
        """
        [Client.associate_instance_storage_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.associate_instance_storage_config)
        """

    def associate_lambda_function(self, InstanceId: str, FunctionArn: str) -> None:
        """
        [Client.associate_lambda_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.associate_lambda_function)
        """

    def associate_lex_bot(self, InstanceId: str, LexBot: "LexBotTypeDef") -> None:
        """
        [Client.associate_lex_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.associate_lex_bot)
        """

    def associate_queue_quick_connects(
        self, InstanceId: str, QueueId: str, QuickConnectIds: List[str]
    ) -> None:
        """
        [Client.associate_queue_quick_connects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.associate_queue_quick_connects)
        """

    def associate_routing_profile_queues(
        self,
        InstanceId: str,
        RoutingProfileId: str,
        QueueConfigs: List[RoutingProfileQueueConfigTypeDef],
    ) -> None:
        """
        [Client.associate_routing_profile_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.associate_routing_profile_queues)
        """

    def associate_security_key(
        self, InstanceId: str, Key: str
    ) -> AssociateSecurityKeyResponseTypeDef:
        """
        [Client.associate_security_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.associate_security_key)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.can_paginate)
        """

    def create_contact_flow(
        self,
        InstanceId: str,
        Name: str,
        Type: Literal[
            "CONTACT_FLOW",
            "CUSTOMER_QUEUE",
            "CUSTOMER_HOLD",
            "CUSTOMER_WHISPER",
            "AGENT_HOLD",
            "AGENT_WHISPER",
            "OUTBOUND_WHISPER",
            "AGENT_TRANSFER",
            "QUEUE_TRANSFER",
        ],
        Content: str,
        Description: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateContactFlowResponseTypeDef:
        """
        [Client.create_contact_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.create_contact_flow)
        """

    def create_instance(
        self,
        IdentityManagementType: Literal["SAML", "CONNECT_MANAGED", "EXISTING_DIRECTORY"],
        InboundCallsEnabled: bool,
        OutboundCallsEnabled: bool,
        ClientToken: str = None,
        InstanceAlias: str = None,
        DirectoryId: str = None,
    ) -> CreateInstanceResponseTypeDef:
        """
        [Client.create_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.create_instance)
        """

    def create_integration_association(
        self,
        InstanceId: str,
        IntegrationType: Literal["EVENT"],
        IntegrationArn: str,
        SourceApplicationUrl: str,
        SourceApplicationName: str,
        SourceType: Literal["SALESFORCE", "ZENDESK"],
    ) -> CreateIntegrationAssociationResponseTypeDef:
        """
        [Client.create_integration_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.create_integration_association)
        """

    def create_queue(
        self,
        InstanceId: str,
        Name: str,
        HoursOfOperationId: str,
        Description: str = None,
        OutboundCallerConfig: "OutboundCallerConfigTypeDef" = None,
        MaxContacts: int = None,
        QuickConnectIds: List[str] = None,
        Tags: Dict[str, str] = None,
    ) -> CreateQueueResponseTypeDef:
        """
        [Client.create_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.create_queue)
        """

    def create_quick_connect(
        self,
        InstanceId: str,
        Name: str,
        QuickConnectConfig: "QuickConnectConfigTypeDef",
        Description: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateQuickConnectResponseTypeDef:
        """
        [Client.create_quick_connect documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.create_quick_connect)
        """

    def create_routing_profile(
        self,
        InstanceId: str,
        Name: str,
        Description: str,
        DefaultOutboundQueueId: str,
        MediaConcurrencies: List["MediaConcurrencyTypeDef"],
        QueueConfigs: List[RoutingProfileQueueConfigTypeDef] = None,
        Tags: Dict[str, str] = None,
    ) -> CreateRoutingProfileResponseTypeDef:
        """
        [Client.create_routing_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.create_routing_profile)
        """

    def create_use_case(
        self,
        InstanceId: str,
        IntegrationAssociationId: str,
        UseCaseType: Literal["RULES_EVALUATION"],
    ) -> CreateUseCaseResponseTypeDef:
        """
        [Client.create_use_case documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.create_use_case)
        """

    def create_user(
        self,
        Username: str,
        PhoneConfig: "UserPhoneConfigTypeDef",
        SecurityProfileIds: List[str],
        RoutingProfileId: str,
        InstanceId: str,
        Password: str = None,
        IdentityInfo: "UserIdentityInfoTypeDef" = None,
        DirectoryUserId: str = None,
        HierarchyGroupId: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateUserResponseTypeDef:
        """
        [Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.create_user)
        """

    def create_user_hierarchy_group(
        self, Name: str, InstanceId: str, ParentGroupId: str = None
    ) -> CreateUserHierarchyGroupResponseTypeDef:
        """
        [Client.create_user_hierarchy_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.create_user_hierarchy_group)
        """

    def delete_instance(self, InstanceId: str) -> None:
        """
        [Client.delete_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.delete_instance)
        """

    def delete_integration_association(
        self, InstanceId: str, IntegrationAssociationId: str
    ) -> None:
        """
        [Client.delete_integration_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.delete_integration_association)
        """

    def delete_quick_connect(self, InstanceId: str, QuickConnectId: str) -> None:
        """
        [Client.delete_quick_connect documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.delete_quick_connect)
        """

    def delete_use_case(
        self, InstanceId: str, IntegrationAssociationId: str, UseCaseId: str
    ) -> None:
        """
        [Client.delete_use_case documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.delete_use_case)
        """

    def delete_user(self, InstanceId: str, UserId: str) -> None:
        """
        [Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.delete_user)
        """

    def delete_user_hierarchy_group(self, HierarchyGroupId: str, InstanceId: str) -> None:
        """
        [Client.delete_user_hierarchy_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.delete_user_hierarchy_group)
        """

    def describe_contact_flow(
        self, InstanceId: str, ContactFlowId: str
    ) -> DescribeContactFlowResponseTypeDef:
        """
        [Client.describe_contact_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.describe_contact_flow)
        """

    def describe_hours_of_operation(
        self, InstanceId: str, HoursOfOperationId: str
    ) -> DescribeHoursOfOperationResponseTypeDef:
        """
        [Client.describe_hours_of_operation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.describe_hours_of_operation)
        """

    def describe_instance(self, InstanceId: str) -> DescribeInstanceResponseTypeDef:
        """
        [Client.describe_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.describe_instance)
        """

    def describe_instance_attribute(
        self,
        InstanceId: str,
        AttributeType: Literal[
            "INBOUND_CALLS",
            "OUTBOUND_CALLS",
            "CONTACTFLOW_LOGS",
            "CONTACT_LENS",
            "AUTO_RESOLVE_BEST_VOICES",
            "USE_CUSTOM_TTS_VOICES",
            "EARLY_MEDIA",
        ],
    ) -> DescribeInstanceAttributeResponseTypeDef:
        """
        [Client.describe_instance_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.describe_instance_attribute)
        """

    def describe_instance_storage_config(
        self,
        InstanceId: str,
        AssociationId: str,
        ResourceType: Literal[
            "CHAT_TRANSCRIPTS",
            "CALL_RECORDINGS",
            "SCHEDULED_REPORTS",
            "MEDIA_STREAMS",
            "CONTACT_TRACE_RECORDS",
            "AGENT_EVENTS",
        ],
    ) -> DescribeInstanceStorageConfigResponseTypeDef:
        """
        [Client.describe_instance_storage_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.describe_instance_storage_config)
        """

    def describe_queue(self, InstanceId: str, QueueId: str) -> DescribeQueueResponseTypeDef:
        """
        [Client.describe_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.describe_queue)
        """

    def describe_quick_connect(
        self, InstanceId: str, QuickConnectId: str
    ) -> DescribeQuickConnectResponseTypeDef:
        """
        [Client.describe_quick_connect documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.describe_quick_connect)
        """

    def describe_routing_profile(
        self, InstanceId: str, RoutingProfileId: str
    ) -> DescribeRoutingProfileResponseTypeDef:
        """
        [Client.describe_routing_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.describe_routing_profile)
        """

    def describe_user(self, UserId: str, InstanceId: str) -> DescribeUserResponseTypeDef:
        """
        [Client.describe_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.describe_user)
        """

    def describe_user_hierarchy_group(
        self, HierarchyGroupId: str, InstanceId: str
    ) -> DescribeUserHierarchyGroupResponseTypeDef:
        """
        [Client.describe_user_hierarchy_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.describe_user_hierarchy_group)
        """

    def describe_user_hierarchy_structure(
        self, InstanceId: str
    ) -> DescribeUserHierarchyStructureResponseTypeDef:
        """
        [Client.describe_user_hierarchy_structure documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.describe_user_hierarchy_structure)
        """

    def disassociate_approved_origin(self, InstanceId: str, Origin: str) -> None:
        """
        [Client.disassociate_approved_origin documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.disassociate_approved_origin)
        """

    def disassociate_instance_storage_config(
        self,
        InstanceId: str,
        AssociationId: str,
        ResourceType: Literal[
            "CHAT_TRANSCRIPTS",
            "CALL_RECORDINGS",
            "SCHEDULED_REPORTS",
            "MEDIA_STREAMS",
            "CONTACT_TRACE_RECORDS",
            "AGENT_EVENTS",
        ],
    ) -> None:
        """
        [Client.disassociate_instance_storage_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.disassociate_instance_storage_config)
        """

    def disassociate_lambda_function(self, InstanceId: str, FunctionArn: str) -> None:
        """
        [Client.disassociate_lambda_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.disassociate_lambda_function)
        """

    def disassociate_lex_bot(self, InstanceId: str, BotName: str, LexRegion: str) -> None:
        """
        [Client.disassociate_lex_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.disassociate_lex_bot)
        """

    def disassociate_queue_quick_connects(
        self, InstanceId: str, QueueId: str, QuickConnectIds: List[str]
    ) -> None:
        """
        [Client.disassociate_queue_quick_connects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.disassociate_queue_quick_connects)
        """

    def disassociate_routing_profile_queues(
        self,
        InstanceId: str,
        RoutingProfileId: str,
        QueueReferences: List["RoutingProfileQueueReferenceTypeDef"],
    ) -> None:
        """
        [Client.disassociate_routing_profile_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.disassociate_routing_profile_queues)
        """

    def disassociate_security_key(self, InstanceId: str, AssociationId: str) -> None:
        """
        [Client.disassociate_security_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.disassociate_security_key)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.generate_presigned_url)
        """

    def get_contact_attributes(
        self, InstanceId: str, InitialContactId: str
    ) -> GetContactAttributesResponseTypeDef:
        """
        [Client.get_contact_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.get_contact_attributes)
        """

    def get_current_metric_data(
        self,
        InstanceId: str,
        Filters: FiltersTypeDef,
        CurrentMetrics: List["CurrentMetricTypeDef"],
        Groupings: List[Literal["QUEUE", "CHANNEL"]] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetCurrentMetricDataResponseTypeDef:
        """
        [Client.get_current_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.get_current_metric_data)
        """

    def get_federation_token(self, InstanceId: str) -> GetFederationTokenResponseTypeDef:
        """
        [Client.get_federation_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.get_federation_token)
        """

    def get_metric_data(
        self,
        InstanceId: str,
        StartTime: datetime,
        EndTime: datetime,
        Filters: FiltersTypeDef,
        HistoricalMetrics: List["HistoricalMetricTypeDef"],
        Groupings: List[Literal["QUEUE", "CHANNEL"]] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetMetricDataResponseTypeDef:
        """
        [Client.get_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.get_metric_data)
        """

    def list_approved_origins(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListApprovedOriginsResponseTypeDef:
        """
        [Client.list_approved_origins documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.list_approved_origins)
        """

    def list_contact_flows(
        self,
        InstanceId: str,
        ContactFlowTypes: List[
            Literal[
                "CONTACT_FLOW",
                "CUSTOMER_QUEUE",
                "CUSTOMER_HOLD",
                "CUSTOMER_WHISPER",
                "AGENT_HOLD",
                "AGENT_WHISPER",
                "OUTBOUND_WHISPER",
                "AGENT_TRANSFER",
                "QUEUE_TRANSFER",
            ]
        ] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListContactFlowsResponseTypeDef:
        """
        [Client.list_contact_flows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.list_contact_flows)
        """

    def list_hours_of_operations(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListHoursOfOperationsResponseTypeDef:
        """
        [Client.list_hours_of_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.list_hours_of_operations)
        """

    def list_instance_attributes(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListInstanceAttributesResponseTypeDef:
        """
        [Client.list_instance_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.list_instance_attributes)
        """

    def list_instance_storage_configs(
        self,
        InstanceId: str,
        ResourceType: Literal[
            "CHAT_TRANSCRIPTS",
            "CALL_RECORDINGS",
            "SCHEDULED_REPORTS",
            "MEDIA_STREAMS",
            "CONTACT_TRACE_RECORDS",
            "AGENT_EVENTS",
        ],
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListInstanceStorageConfigsResponseTypeDef:
        """
        [Client.list_instance_storage_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.list_instance_storage_configs)
        """

    def list_instances(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListInstancesResponseTypeDef:
        """
        [Client.list_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.list_instances)
        """

    def list_integration_associations(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListIntegrationAssociationsResponseTypeDef:
        """
        [Client.list_integration_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.list_integration_associations)
        """

    def list_lambda_functions(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListLambdaFunctionsResponseTypeDef:
        """
        [Client.list_lambda_functions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.list_lambda_functions)
        """

    def list_lex_bots(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListLexBotsResponseTypeDef:
        """
        [Client.list_lex_bots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.list_lex_bots)
        """

    def list_phone_numbers(
        self,
        InstanceId: str,
        PhoneNumberTypes: List[Literal["TOLL_FREE", "DID"]] = None,
        PhoneNumberCountryCodes: List[
            Literal[
                "AF",
                "AL",
                "DZ",
                "AS",
                "AD",
                "AO",
                "AI",
                "AQ",
                "AG",
                "AR",
                "AM",
                "AW",
                "AU",
                "AT",
                "AZ",
                "BS",
                "BH",
                "BD",
                "BB",
                "BY",
                "BE",
                "BZ",
                "BJ",
                "BM",
                "BT",
                "BO",
                "BA",
                "BW",
                "BR",
                "IO",
                "VG",
                "BN",
                "BG",
                "BF",
                "BI",
                "KH",
                "CM",
                "CA",
                "CV",
                "KY",
                "CF",
                "TD",
                "CL",
                "CN",
                "CX",
                "CC",
                "CO",
                "KM",
                "CK",
                "CR",
                "HR",
                "CU",
                "CW",
                "CY",
                "CZ",
                "CD",
                "DK",
                "DJ",
                "DM",
                "DO",
                "TL",
                "EC",
                "EG",
                "SV",
                "GQ",
                "ER",
                "EE",
                "ET",
                "FK",
                "FO",
                "FJ",
                "FI",
                "FR",
                "PF",
                "GA",
                "GM",
                "GE",
                "DE",
                "GH",
                "GI",
                "GR",
                "GL",
                "GD",
                "GU",
                "GT",
                "GG",
                "GN",
                "GW",
                "GY",
                "HT",
                "HN",
                "HK",
                "HU",
                "IS",
                "IN",
                "ID",
                "IR",
                "IQ",
                "IE",
                "IM",
                "IL",
                "IT",
                "CI",
                "JM",
                "JP",
                "JE",
                "JO",
                "KZ",
                "KE",
                "KI",
                "KW",
                "KG",
                "LA",
                "LV",
                "LB",
                "LS",
                "LR",
                "LY",
                "LI",
                "LT",
                "LU",
                "MO",
                "MK",
                "MG",
                "MW",
                "MY",
                "MV",
                "ML",
                "MT",
                "MH",
                "MR",
                "MU",
                "YT",
                "MX",
                "FM",
                "MD",
                "MC",
                "MN",
                "ME",
                "MS",
                "MA",
                "MZ",
                "MM",
                "NA",
                "NR",
                "NP",
                "NL",
                "AN",
                "NC",
                "NZ",
                "NI",
                "NE",
                "NG",
                "NU",
                "KP",
                "MP",
                "NO",
                "OM",
                "PK",
                "PW",
                "PA",
                "PG",
                "PY",
                "PE",
                "PH",
                "PN",
                "PL",
                "PT",
                "PR",
                "QA",
                "CG",
                "RE",
                "RO",
                "RU",
                "RW",
                "BL",
                "SH",
                "KN",
                "LC",
                "MF",
                "PM",
                "VC",
                "WS",
                "SM",
                "ST",
                "SA",
                "SN",
                "RS",
                "SC",
                "SL",
                "SG",
                "SX",
                "SK",
                "SI",
                "SB",
                "SO",
                "ZA",
                "KR",
                "ES",
                "LK",
                "SD",
                "SR",
                "SJ",
                "SZ",
                "SE",
                "CH",
                "SY",
                "TW",
                "TJ",
                "TZ",
                "TH",
                "TG",
                "TK",
                "TO",
                "TT",
                "TN",
                "TR",
                "TM",
                "TC",
                "TV",
                "VI",
                "UG",
                "UA",
                "AE",
                "GB",
                "US",
                "UY",
                "UZ",
                "VU",
                "VA",
                "VE",
                "VN",
                "WF",
                "EH",
                "YE",
                "ZM",
                "ZW",
            ]
        ] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListPhoneNumbersResponseTypeDef:
        """
        [Client.list_phone_numbers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.list_phone_numbers)
        """

    def list_prompts(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListPromptsResponseTypeDef:
        """
        [Client.list_prompts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.list_prompts)
        """

    def list_queue_quick_connects(
        self, InstanceId: str, QueueId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListQueueQuickConnectsResponseTypeDef:
        """
        [Client.list_queue_quick_connects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.list_queue_quick_connects)
        """

    def list_queues(
        self,
        InstanceId: str,
        QueueTypes: List[Literal["STANDARD", "AGENT"]] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListQueuesResponseTypeDef:
        """
        [Client.list_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.list_queues)
        """

    def list_quick_connects(
        self,
        InstanceId: str,
        NextToken: str = None,
        MaxResults: int = None,
        QuickConnectTypes: List[Literal["USER", "QUEUE", "PHONE_NUMBER"]] = None,
    ) -> ListQuickConnectsResponseTypeDef:
        """
        [Client.list_quick_connects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.list_quick_connects)
        """

    def list_routing_profile_queues(
        self, InstanceId: str, RoutingProfileId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListRoutingProfileQueuesResponseTypeDef:
        """
        [Client.list_routing_profile_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.list_routing_profile_queues)
        """

    def list_routing_profiles(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListRoutingProfilesResponseTypeDef:
        """
        [Client.list_routing_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.list_routing_profiles)
        """

    def list_security_keys(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListSecurityKeysResponseTypeDef:
        """
        [Client.list_security_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.list_security_keys)
        """

    def list_security_profiles(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListSecurityProfilesResponseTypeDef:
        """
        [Client.list_security_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.list_security_profiles)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.list_tags_for_resource)
        """

    def list_use_cases(
        self,
        InstanceId: str,
        IntegrationAssociationId: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListUseCasesResponseTypeDef:
        """
        [Client.list_use_cases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.list_use_cases)
        """

    def list_user_hierarchy_groups(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListUserHierarchyGroupsResponseTypeDef:
        """
        [Client.list_user_hierarchy_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.list_user_hierarchy_groups)
        """

    def list_users(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListUsersResponseTypeDef:
        """
        [Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.list_users)
        """

    def resume_contact_recording(
        self, InstanceId: str, ContactId: str, InitialContactId: str
    ) -> Dict[str, Any]:
        """
        [Client.resume_contact_recording documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.resume_contact_recording)
        """

    def start_chat_contact(
        self,
        InstanceId: str,
        ContactFlowId: str,
        ParticipantDetails: ParticipantDetailsTypeDef,
        Attributes: Dict[str, str] = None,
        InitialMessage: ChatMessageTypeDef = None,
        ClientToken: str = None,
    ) -> StartChatContactResponseTypeDef:
        """
        [Client.start_chat_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.start_chat_contact)
        """

    def start_contact_recording(
        self,
        InstanceId: str,
        ContactId: str,
        InitialContactId: str,
        VoiceRecordingConfiguration: VoiceRecordingConfigurationTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.start_contact_recording documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.start_contact_recording)
        """

    def start_outbound_voice_contact(
        self,
        DestinationPhoneNumber: str,
        ContactFlowId: str,
        InstanceId: str,
        ClientToken: str = None,
        SourcePhoneNumber: str = None,
        QueueId: str = None,
        Attributes: Dict[str, str] = None,
    ) -> StartOutboundVoiceContactResponseTypeDef:
        """
        [Client.start_outbound_voice_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.start_outbound_voice_contact)
        """

    def start_task_contact(
        self,
        InstanceId: str,
        ContactFlowId: str,
        Name: str,
        PreviousContactId: str = None,
        Attributes: Dict[str, str] = None,
        References: Dict[str, ReferenceTypeDef] = None,
        Description: str = None,
        ClientToken: str = None,
    ) -> StartTaskContactResponseTypeDef:
        """
        [Client.start_task_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.start_task_contact)
        """

    def stop_contact(self, ContactId: str, InstanceId: str) -> Dict[str, Any]:
        """
        [Client.stop_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.stop_contact)
        """

    def stop_contact_recording(
        self, InstanceId: str, ContactId: str, InitialContactId: str
    ) -> Dict[str, Any]:
        """
        [Client.stop_contact_recording documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.stop_contact_recording)
        """

    def suspend_contact_recording(
        self, InstanceId: str, ContactId: str, InitialContactId: str
    ) -> Dict[str, Any]:
        """
        [Client.suspend_contact_recording documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.suspend_contact_recording)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.untag_resource)
        """

    def update_contact_attributes(
        self, InitialContactId: str, InstanceId: str, Attributes: Dict[str, str]
    ) -> Dict[str, Any]:
        """
        [Client.update_contact_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.update_contact_attributes)
        """

    def update_contact_flow_content(
        self, InstanceId: str, ContactFlowId: str, Content: str
    ) -> None:
        """
        [Client.update_contact_flow_content documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.update_contact_flow_content)
        """

    def update_contact_flow_name(
        self, InstanceId: str, ContactFlowId: str, Name: str = None, Description: str = None
    ) -> None:
        """
        [Client.update_contact_flow_name documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.update_contact_flow_name)
        """

    def update_instance_attribute(
        self,
        InstanceId: str,
        AttributeType: Literal[
            "INBOUND_CALLS",
            "OUTBOUND_CALLS",
            "CONTACTFLOW_LOGS",
            "CONTACT_LENS",
            "AUTO_RESOLVE_BEST_VOICES",
            "USE_CUSTOM_TTS_VOICES",
            "EARLY_MEDIA",
        ],
        Value: str,
    ) -> None:
        """
        [Client.update_instance_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.update_instance_attribute)
        """

    def update_instance_storage_config(
        self,
        InstanceId: str,
        AssociationId: str,
        ResourceType: Literal[
            "CHAT_TRANSCRIPTS",
            "CALL_RECORDINGS",
            "SCHEDULED_REPORTS",
            "MEDIA_STREAMS",
            "CONTACT_TRACE_RECORDS",
            "AGENT_EVENTS",
        ],
        StorageConfig: "InstanceStorageConfigTypeDef",
    ) -> None:
        """
        [Client.update_instance_storage_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.update_instance_storage_config)
        """

    def update_queue_hours_of_operation(
        self, InstanceId: str, QueueId: str, HoursOfOperationId: str
    ) -> None:
        """
        [Client.update_queue_hours_of_operation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.update_queue_hours_of_operation)
        """

    def update_queue_max_contacts(self, InstanceId: str, QueueId: str, MaxContacts: int) -> None:
        """
        [Client.update_queue_max_contacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.update_queue_max_contacts)
        """

    def update_queue_name(
        self, InstanceId: str, QueueId: str, Name: str = None, Description: str = None
    ) -> None:
        """
        [Client.update_queue_name documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.update_queue_name)
        """

    def update_queue_outbound_caller_config(
        self, InstanceId: str, QueueId: str, OutboundCallerConfig: "OutboundCallerConfigTypeDef"
    ) -> None:
        """
        [Client.update_queue_outbound_caller_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.update_queue_outbound_caller_config)
        """

    def update_queue_status(
        self, InstanceId: str, QueueId: str, Status: Literal["ENABLED", "DISABLED"]
    ) -> None:
        """
        [Client.update_queue_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.update_queue_status)
        """

    def update_quick_connect_config(
        self, InstanceId: str, QuickConnectId: str, QuickConnectConfig: "QuickConnectConfigTypeDef"
    ) -> None:
        """
        [Client.update_quick_connect_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.update_quick_connect_config)
        """

    def update_quick_connect_name(
        self, InstanceId: str, QuickConnectId: str, Name: str = None, Description: str = None
    ) -> None:
        """
        [Client.update_quick_connect_name documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.update_quick_connect_name)
        """

    def update_routing_profile_concurrency(
        self,
        InstanceId: str,
        RoutingProfileId: str,
        MediaConcurrencies: List["MediaConcurrencyTypeDef"],
    ) -> None:
        """
        [Client.update_routing_profile_concurrency documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.update_routing_profile_concurrency)
        """

    def update_routing_profile_default_outbound_queue(
        self, InstanceId: str, RoutingProfileId: str, DefaultOutboundQueueId: str
    ) -> None:
        """
        [Client.update_routing_profile_default_outbound_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.update_routing_profile_default_outbound_queue)
        """

    def update_routing_profile_name(
        self, InstanceId: str, RoutingProfileId: str, Name: str = None, Description: str = None
    ) -> None:
        """
        [Client.update_routing_profile_name documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.update_routing_profile_name)
        """

    def update_routing_profile_queues(
        self,
        InstanceId: str,
        RoutingProfileId: str,
        QueueConfigs: List[RoutingProfileQueueConfigTypeDef],
    ) -> None:
        """
        [Client.update_routing_profile_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.update_routing_profile_queues)
        """

    def update_user_hierarchy(
        self, UserId: str, InstanceId: str, HierarchyGroupId: str = None
    ) -> None:
        """
        [Client.update_user_hierarchy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.update_user_hierarchy)
        """

    def update_user_hierarchy_group_name(
        self, Name: str, HierarchyGroupId: str, InstanceId: str
    ) -> None:
        """
        [Client.update_user_hierarchy_group_name documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.update_user_hierarchy_group_name)
        """

    def update_user_hierarchy_structure(
        self, HierarchyStructure: HierarchyStructureUpdateTypeDef, InstanceId: str
    ) -> None:
        """
        [Client.update_user_hierarchy_structure documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.update_user_hierarchy_structure)
        """

    def update_user_identity_info(
        self, IdentityInfo: "UserIdentityInfoTypeDef", UserId: str, InstanceId: str
    ) -> None:
        """
        [Client.update_user_identity_info documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.update_user_identity_info)
        """

    def update_user_phone_config(
        self, PhoneConfig: "UserPhoneConfigTypeDef", UserId: str, InstanceId: str
    ) -> None:
        """
        [Client.update_user_phone_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.update_user_phone_config)
        """

    def update_user_routing_profile(
        self, RoutingProfileId: str, UserId: str, InstanceId: str
    ) -> None:
        """
        [Client.update_user_routing_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.update_user_routing_profile)
        """

    def update_user_security_profiles(
        self, SecurityProfileIds: List[str], UserId: str, InstanceId: str
    ) -> None:
        """
        [Client.update_user_security_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Client.update_user_security_profiles)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_metric_data"]) -> GetMetricDataPaginator:
        """
        [Paginator.GetMetricData documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Paginator.GetMetricData)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_approved_origins"]
    ) -> ListApprovedOriginsPaginator:
        """
        [Paginator.ListApprovedOrigins documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Paginator.ListApprovedOrigins)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_contact_flows"]
    ) -> ListContactFlowsPaginator:
        """
        [Paginator.ListContactFlows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Paginator.ListContactFlows)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_hours_of_operations"]
    ) -> ListHoursOfOperationsPaginator:
        """
        [Paginator.ListHoursOfOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Paginator.ListHoursOfOperations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_attributes"]
    ) -> ListInstanceAttributesPaginator:
        """
        [Paginator.ListInstanceAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Paginator.ListInstanceAttributes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_storage_configs"]
    ) -> ListInstanceStorageConfigsPaginator:
        """
        [Paginator.ListInstanceStorageConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Paginator.ListInstanceStorageConfigs)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_instances"]) -> ListInstancesPaginator:
        """
        [Paginator.ListInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Paginator.ListInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_integration_associations"]
    ) -> ListIntegrationAssociationsPaginator:
        """
        [Paginator.ListIntegrationAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Paginator.ListIntegrationAssociations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_lambda_functions"]
    ) -> ListLambdaFunctionsPaginator:
        """
        [Paginator.ListLambdaFunctions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Paginator.ListLambdaFunctions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_lex_bots"]) -> ListLexBotsPaginator:
        """
        [Paginator.ListLexBots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Paginator.ListLexBots)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_phone_numbers"]
    ) -> ListPhoneNumbersPaginator:
        """
        [Paginator.ListPhoneNumbers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Paginator.ListPhoneNumbers)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_prompts"]) -> ListPromptsPaginator:
        """
        [Paginator.ListPrompts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Paginator.ListPrompts)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_queue_quick_connects"]
    ) -> ListQueueQuickConnectsPaginator:
        """
        [Paginator.ListQueueQuickConnects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Paginator.ListQueueQuickConnects)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_queues"]) -> ListQueuesPaginator:
        """
        [Paginator.ListQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Paginator.ListQueues)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_quick_connects"]
    ) -> ListQuickConnectsPaginator:
        """
        [Paginator.ListQuickConnects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Paginator.ListQuickConnects)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_routing_profile_queues"]
    ) -> ListRoutingProfileQueuesPaginator:
        """
        [Paginator.ListRoutingProfileQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Paginator.ListRoutingProfileQueues)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_routing_profiles"]
    ) -> ListRoutingProfilesPaginator:
        """
        [Paginator.ListRoutingProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Paginator.ListRoutingProfiles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_keys"]
    ) -> ListSecurityKeysPaginator:
        """
        [Paginator.ListSecurityKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Paginator.ListSecurityKeys)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_profiles"]
    ) -> ListSecurityProfilesPaginator:
        """
        [Paginator.ListSecurityProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Paginator.ListSecurityProfiles)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_use_cases"]) -> ListUseCasesPaginator:
        """
        [Paginator.ListUseCases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Paginator.ListUseCases)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_user_hierarchy_groups"]
    ) -> ListUserHierarchyGroupsPaginator:
        """
        [Paginator.ListUserHierarchyGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Paginator.ListUserHierarchyGroups)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_users"]) -> ListUsersPaginator:
        """
        [Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/connect.html#Connect.Paginator.ListUsers)
        """
