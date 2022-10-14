"""
Type annotations for ssm-incidents service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_ssm_incidents import SSMIncidentsClient

    client: SSMIncidentsClient = boto3.client("ssm-incidents")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import IncidentRecordStatusType, SortOrderType
from .paginator import (
    GetResourcePoliciesPaginator,
    ListIncidentRecordsPaginator,
    ListRelatedItemsPaginator,
    ListReplicationSetsPaginator,
    ListResponsePlansPaginator,
    ListTimelineEventsPaginator,
)
from .type_defs import (
    ActionTypeDef,
    ChatChannelTypeDef,
    CreateReplicationSetOutputTypeDef,
    CreateResponsePlanOutputTypeDef,
    CreateTimelineEventOutputTypeDef,
    FilterTypeDef,
    GetIncidentRecordOutputTypeDef,
    GetReplicationSetOutputTypeDef,
    GetResourcePoliciesOutputTypeDef,
    GetResponsePlanOutputTypeDef,
    GetTimelineEventOutputTypeDef,
    IncidentTemplateTypeDef,
    ListIncidentRecordsOutputTypeDef,
    ListRelatedItemsOutputTypeDef,
    ListReplicationSetsOutputTypeDef,
    ListResponsePlansOutputTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTimelineEventsOutputTypeDef,
    NotificationTargetItemTypeDef,
    PutResourcePolicyOutputTypeDef,
    RegionMapInputValueTypeDef,
    RelatedItemsUpdateTypeDef,
    RelatedItemTypeDef,
    StartIncidentOutputTypeDef,
    TriggerDetailsTypeDef,
    UpdateReplicationSetActionTypeDef,
)
from .waiter import WaitForReplicationSetActiveWaiter, WaitForReplicationSetDeletedWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("SSMIncidentsClient",)

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
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class SSMIncidentsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SSMIncidentsClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#close)
        """
    def create_replication_set(
        self, *, regions: Dict[str, "RegionMapInputValueTypeDef"], clientToken: str = None
    ) -> CreateReplicationSetOutputTypeDef:
        """
        A replication set replicates and encrypts your data to the provided Regions with
        the provided KMS key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.create_replication_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#create_replication_set)
        """
    def create_response_plan(
        self,
        *,
        incidentTemplate: "IncidentTemplateTypeDef",
        name: str,
        actions: List["ActionTypeDef"] = None,
        chatChannel: "ChatChannelTypeDef" = None,
        clientToken: str = None,
        displayName: str = None,
        engagements: List[str] = None,
        tags: Dict[str, str] = None
    ) -> CreateResponsePlanOutputTypeDef:
        """
        Creates a response plan that automates the initial response to incidents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.create_response_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#create_response_plan)
        """
    def create_timeline_event(
        self,
        *,
        eventData: str,
        eventTime: Union[datetime, str],
        eventType: str,
        incidentRecordArn: str,
        clientToken: str = None
    ) -> CreateTimelineEventOutputTypeDef:
        """
        Creates a custom timeline event on the incident details page of an incident
        record.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.create_timeline_event)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#create_timeline_event)
        """
    def delete_incident_record(self, *, arn: str) -> Dict[str, Any]:
        """
        Delete an incident record from Incident Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.delete_incident_record)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#delete_incident_record)
        """
    def delete_replication_set(self, *, arn: str) -> Dict[str, Any]:
        """
        Deletes all Regions in your replication set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.delete_replication_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#delete_replication_set)
        """
    def delete_resource_policy(self, *, policyId: str, resourceArn: str) -> Dict[str, Any]:
        """
        Deletes the resource policy that Resource Access Manager uses to share your
        Incident Manager resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#delete_resource_policy)
        """
    def delete_response_plan(self, *, arn: str) -> Dict[str, Any]:
        """
        Deletes the specified response plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.delete_response_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#delete_response_plan)
        """
    def delete_timeline_event(self, *, eventId: str, incidentRecordArn: str) -> Dict[str, Any]:
        """
        Deletes a timeline event from an incident.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.delete_timeline_event)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#delete_timeline_event)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#generate_presigned_url)
        """
    def get_incident_record(self, *, arn: str) -> GetIncidentRecordOutputTypeDef:
        """
        Returns the details for the specified incident record.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.get_incident_record)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#get_incident_record)
        """
    def get_replication_set(self, *, arn: str) -> GetReplicationSetOutputTypeDef:
        """
        Retrieve your Incident Manager replication set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.get_replication_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#get_replication_set)
        """
    def get_resource_policies(
        self, *, resourceArn: str, maxResults: int = None, nextToken: str = None
    ) -> GetResourcePoliciesOutputTypeDef:
        """
        Retrieves the resource policies attached to the specified response plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.get_resource_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#get_resource_policies)
        """
    def get_response_plan(self, *, arn: str) -> GetResponsePlanOutputTypeDef:
        """
        Retrieves the details of the specified response plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.get_response_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#get_response_plan)
        """
    def get_timeline_event(
        self, *, eventId: str, incidentRecordArn: str
    ) -> GetTimelineEventOutputTypeDef:
        """
        Retrieves a timeline event based on its ID and incident record.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.get_timeline_event)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#get_timeline_event)
        """
    def list_incident_records(
        self,
        *,
        filters: List["FilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListIncidentRecordsOutputTypeDef:
        """
        Lists all incident records in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.list_incident_records)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#list_incident_records)
        """
    def list_related_items(
        self, *, incidentRecordArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListRelatedItemsOutputTypeDef:
        """
        List all related items for an incident record.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.list_related_items)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#list_related_items)
        """
    def list_replication_sets(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListReplicationSetsOutputTypeDef:
        """
        Lists details about the replication set configured in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.list_replication_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#list_replication_sets)
        """
    def list_response_plans(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListResponsePlansOutputTypeDef:
        """
        Lists all response plans in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.list_response_plans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#list_response_plans)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags that are attached to the specified response plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#list_tags_for_resource)
        """
    def list_timeline_events(
        self,
        *,
        incidentRecordArn: str,
        filters: List["FilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None,
        sortBy: Literal["EVENT_TIME"] = None,
        sortOrder: SortOrderType = None
    ) -> ListTimelineEventsOutputTypeDef:
        """
        Lists timeline events for the specified incident record.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.list_timeline_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#list_timeline_events)
        """
    def put_resource_policy(
        self, *, policy: str, resourceArn: str
    ) -> PutResourcePolicyOutputTypeDef:
        """
        Adds a resource policy to the specified response plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.put_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#put_resource_policy)
        """
    def start_incident(
        self,
        *,
        responsePlanArn: str,
        clientToken: str = None,
        impact: int = None,
        relatedItems: List["RelatedItemTypeDef"] = None,
        title: str = None,
        triggerDetails: "TriggerDetailsTypeDef" = None
    ) -> StartIncidentOutputTypeDef:
        """
        Used to start an incident from CloudWatch alarms, EventBridge events, or
        manually.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.start_incident)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#start_incident)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds a tag to a response plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a tag from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#untag_resource)
        """
    def update_deletion_protection(
        self, *, arn: str, deletionProtected: bool, clientToken: str = None
    ) -> Dict[str, Any]:
        """
        Update deletion protection to either allow or deny deletion of the final Region
        in a replication set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.update_deletion_protection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#update_deletion_protection)
        """
    def update_incident_record(
        self,
        *,
        arn: str,
        chatChannel: "ChatChannelTypeDef" = None,
        clientToken: str = None,
        impact: int = None,
        notificationTargets: List["NotificationTargetItemTypeDef"] = None,
        status: IncidentRecordStatusType = None,
        summary: str = None,
        title: str = None
    ) -> Dict[str, Any]:
        """
        Update the details of an incident record.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.update_incident_record)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#update_incident_record)
        """
    def update_related_items(
        self,
        *,
        incidentRecordArn: str,
        relatedItemsUpdate: "RelatedItemsUpdateTypeDef",
        clientToken: str = None
    ) -> Dict[str, Any]:
        """
        Add or remove related items from the related items tab of an incident record.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.update_related_items)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#update_related_items)
        """
    def update_replication_set(
        self,
        *,
        actions: List["UpdateReplicationSetActionTypeDef"],
        arn: str,
        clientToken: str = None
    ) -> Dict[str, Any]:
        """
        Add or delete Regions from your replication set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.update_replication_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#update_replication_set)
        """
    def update_response_plan(
        self,
        *,
        arn: str,
        actions: List["ActionTypeDef"] = None,
        chatChannel: "ChatChannelTypeDef" = None,
        clientToken: str = None,
        displayName: str = None,
        engagements: List[str] = None,
        incidentTemplateDedupeString: str = None,
        incidentTemplateImpact: int = None,
        incidentTemplateNotificationTargets: List["NotificationTargetItemTypeDef"] = None,
        incidentTemplateSummary: str = None,
        incidentTemplateTags: Dict[str, str] = None,
        incidentTemplateTitle: str = None
    ) -> Dict[str, Any]:
        """
        Updates the specified response plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.update_response_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#update_response_plan)
        """
    def update_timeline_event(
        self,
        *,
        eventId: str,
        incidentRecordArn: str,
        clientToken: str = None,
        eventData: str = None,
        eventTime: Union[datetime, str] = None,
        eventType: str = None
    ) -> Dict[str, Any]:
        """
        Updates a timeline event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Client.update_timeline_event)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#update_timeline_event)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_resource_policies"]
    ) -> GetResourcePoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Paginator.GetResourcePolicies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#getresourcepoliciespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_incident_records"]
    ) -> ListIncidentRecordsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Paginator.ListIncidentRecords)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#listincidentrecordspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_related_items"]
    ) -> ListRelatedItemsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Paginator.ListRelatedItems)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#listrelateditemspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_replication_sets"]
    ) -> ListReplicationSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Paginator.ListReplicationSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#listreplicationsetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_response_plans"]
    ) -> ListResponsePlansPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Paginator.ListResponsePlans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#listresponseplanspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_timeline_events"]
    ) -> ListTimelineEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Paginator.ListTimelineEvents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#listtimelineeventspaginator)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["wait_for_replication_set_active"]
    ) -> WaitForReplicationSetActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Waiter.WaitForReplicationSetActive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/waiters.html#waitforreplicationsetactivewaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["wait_for_replication_set_deleted"]
    ) -> WaitForReplicationSetDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ssm-incidents.html#SSMIncidents.Waiter.WaitForReplicationSetDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/waiters.html#waitforreplicationsetdeletedwaiter)
        """
