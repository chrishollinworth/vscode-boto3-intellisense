"""
Type annotations for emr service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_emr import EMRClient

    client: EMRClient = boto3.client("emr")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AuthModeType,
    ClusterStateType,
    IdentityTypeType,
    InstanceFleetTypeType,
    InstanceGroupTypeType,
    InstanceStateType,
    JobFlowExecutionStateType,
    NotebookExecutionStatusType,
    RepoUpgradeOnBootType,
    ScaleDownBehaviorType,
    StepCancellationOptionType,
    StepStateType,
)
from .paginator import (
    ListBootstrapActionsPaginator,
    ListClustersPaginator,
    ListInstanceFleetsPaginator,
    ListInstanceGroupsPaginator,
    ListInstancesPaginator,
    ListNotebookExecutionsPaginator,
    ListSecurityConfigurationsPaginator,
    ListStepsPaginator,
    ListStudioSessionMappingsPaginator,
    ListStudiosPaginator,
)
from .type_defs import (
    AddInstanceFleetOutputTypeDef,
    AddInstanceGroupsOutputTypeDef,
    AddJobFlowStepsOutputTypeDef,
    ApplicationTypeDef,
    AutoScalingPolicyTypeDef,
    AutoTerminationPolicyTypeDef,
    BlockPublicAccessConfigurationTypeDef,
    BootstrapActionConfigTypeDef,
    CancelStepsOutputTypeDef,
    ConfigurationTypeDef,
    CreateSecurityConfigurationOutputTypeDef,
    CreateStudioOutputTypeDef,
    DescribeClusterOutputTypeDef,
    DescribeJobFlowsOutputTypeDef,
    DescribeNotebookExecutionOutputTypeDef,
    DescribeReleaseLabelOutputTypeDef,
    DescribeSecurityConfigurationOutputTypeDef,
    DescribeStepOutputTypeDef,
    DescribeStudioOutputTypeDef,
    ExecutionEngineConfigTypeDef,
    GetAutoTerminationPolicyOutputTypeDef,
    GetBlockPublicAccessConfigurationOutputTypeDef,
    GetManagedScalingPolicyOutputTypeDef,
    GetStudioSessionMappingOutputTypeDef,
    InstanceFleetConfigTypeDef,
    InstanceFleetModifyConfigTypeDef,
    InstanceGroupConfigTypeDef,
    InstanceGroupModifyConfigTypeDef,
    JobFlowInstancesConfigTypeDef,
    KerberosAttributesTypeDef,
    ListBootstrapActionsOutputTypeDef,
    ListClustersOutputTypeDef,
    ListInstanceFleetsOutputTypeDef,
    ListInstanceGroupsOutputTypeDef,
    ListInstancesOutputTypeDef,
    ListNotebookExecutionsOutputTypeDef,
    ListReleaseLabelsOutputTypeDef,
    ListSecurityConfigurationsOutputTypeDef,
    ListStepsOutputTypeDef,
    ListStudioSessionMappingsOutputTypeDef,
    ListStudiosOutputTypeDef,
    ManagedScalingPolicyTypeDef,
    ModifyClusterOutputTypeDef,
    PlacementGroupConfigTypeDef,
    PutAutoScalingPolicyOutputTypeDef,
    ReleaseLabelFilterTypeDef,
    RunJobFlowOutputTypeDef,
    StartNotebookExecutionOutputTypeDef,
    StepConfigTypeDef,
    SupportedProductConfigTypeDef,
    TagTypeDef,
)
from .waiter import ClusterRunningWaiter, ClusterTerminatedWaiter, StepCompleteWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("EMRClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]

class EMRClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        EMRClient exceptions.
        """
    def add_instance_fleet(
        self, *, ClusterId: str, InstanceFleet: "InstanceFleetConfigTypeDef"
    ) -> AddInstanceFleetOutputTypeDef:
        """
        Adds an instance fleet to a running cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.add_instance_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#add_instance_fleet)
        """
    def add_instance_groups(
        self, *, InstanceGroups: List["InstanceGroupConfigTypeDef"], JobFlowId: str
    ) -> AddInstanceGroupsOutputTypeDef:
        """
        Adds one or more instance groups to a running cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.add_instance_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#add_instance_groups)
        """
    def add_job_flow_steps(
        self, *, JobFlowId: str, Steps: List["StepConfigTypeDef"], ExecutionRoleArn: str = None
    ) -> AddJobFlowStepsOutputTypeDef:
        """
        AddJobFlowSteps adds new steps to a running cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.add_job_flow_steps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#add_job_flow_steps)
        """
    def add_tags(self, *, ResourceId: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds tags to an Amazon EMR resource, such as a cluster or an Amazon EMR Studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.add_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#add_tags)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#can_paginate)
        """
    def cancel_steps(
        self,
        *,
        ClusterId: str,
        StepIds: List[str],
        StepCancellationOption: StepCancellationOptionType = None
    ) -> CancelStepsOutputTypeDef:
        """
        Cancels a pending step or steps in a running cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.cancel_steps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#cancel_steps)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#close)
        """
    def create_security_configuration(
        self, *, Name: str, SecurityConfiguration: str
    ) -> CreateSecurityConfigurationOutputTypeDef:
        """
        Creates a security configuration, which is stored in the service and can be
        specified when a cluster is created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.create_security_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#create_security_configuration)
        """
    def create_studio(
        self,
        *,
        Name: str,
        AuthMode: AuthModeType,
        VpcId: str,
        SubnetIds: List[str],
        ServiceRole: str,
        WorkspaceSecurityGroupId: str,
        EngineSecurityGroupId: str,
        DefaultS3Location: str,
        Description: str = None,
        UserRole: str = None,
        IdpAuthUrl: str = None,
        IdpRelayStateParameterName: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateStudioOutputTypeDef:
        """
        Creates a new Amazon EMR Studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.create_studio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#create_studio)
        """
    def create_studio_session_mapping(
        self,
        *,
        StudioId: str,
        IdentityType: IdentityTypeType,
        SessionPolicyArn: str,
        IdentityId: str = None,
        IdentityName: str = None
    ) -> None:
        """
        Maps a user or group to the Amazon EMR Studio specified by `StudioId` , and
        applies a session policy to refine Studio permissions for that user or group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.create_studio_session_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#create_studio_session_mapping)
        """
    def delete_security_configuration(self, *, Name: str) -> Dict[str, Any]:
        """
        Deletes a security configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.delete_security_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#delete_security_configuration)
        """
    def delete_studio(self, *, StudioId: str) -> None:
        """
        Removes an Amazon EMR Studio from the Studio metadata store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.delete_studio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#delete_studio)
        """
    def delete_studio_session_mapping(
        self,
        *,
        StudioId: str,
        IdentityType: IdentityTypeType,
        IdentityId: str = None,
        IdentityName: str = None
    ) -> None:
        """
        Removes a user or group from an Amazon EMR Studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.delete_studio_session_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#delete_studio_session_mapping)
        """
    def describe_cluster(self, *, ClusterId: str) -> DescribeClusterOutputTypeDef:
        """
        Provides cluster-level details including status, hardware and software
        configuration, VPC settings, and so on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.describe_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#describe_cluster)
        """
    def describe_job_flows(
        self,
        *,
        CreatedAfter: Union[datetime, str] = None,
        CreatedBefore: Union[datetime, str] = None,
        JobFlowIds: List[str] = None,
        JobFlowStates: List[JobFlowExecutionStateType] = None
    ) -> DescribeJobFlowsOutputTypeDef:
        """
        This API is no longer supported and will eventually be removed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.describe_job_flows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#describe_job_flows)
        """
    def describe_notebook_execution(
        self, *, NotebookExecutionId: str
    ) -> DescribeNotebookExecutionOutputTypeDef:
        """
        Provides details of a notebook execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.describe_notebook_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#describe_notebook_execution)
        """
    def describe_release_label(
        self, *, ReleaseLabel: str = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeReleaseLabelOutputTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.describe_release_label)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#describe_release_label)
        """
    def describe_security_configuration(
        self, *, Name: str
    ) -> DescribeSecurityConfigurationOutputTypeDef:
        """
        Provides the details of a security configuration by returning the configuration
        JSON.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.describe_security_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#describe_security_configuration)
        """
    def describe_step(self, *, ClusterId: str, StepId: str) -> DescribeStepOutputTypeDef:
        """
        Provides more detail about the cluster step.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.describe_step)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#describe_step)
        """
    def describe_studio(self, *, StudioId: str) -> DescribeStudioOutputTypeDef:
        """
        Returns details for the specified Amazon EMR Studio including ID, Name, VPC,
        Studio access URL, and so on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.describe_studio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#describe_studio)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#generate_presigned_url)
        """
    def get_auto_termination_policy(
        self, *, ClusterId: str
    ) -> GetAutoTerminationPolicyOutputTypeDef:
        """
        Returns the auto-termination policy for an Amazon EMR cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.get_auto_termination_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#get_auto_termination_policy)
        """
    def get_block_public_access_configuration(
        self,
    ) -> GetBlockPublicAccessConfigurationOutputTypeDef:
        """
        Returns the Amazon EMR block public access configuration for your Amazon Web
        Services account in the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.get_block_public_access_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#get_block_public_access_configuration)
        """
    def get_managed_scaling_policy(self, *, ClusterId: str) -> GetManagedScalingPolicyOutputTypeDef:
        """
        Fetches the attached managed scaling policy for an Amazon EMR cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.get_managed_scaling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#get_managed_scaling_policy)
        """
    def get_studio_session_mapping(
        self,
        *,
        StudioId: str,
        IdentityType: IdentityTypeType,
        IdentityId: str = None,
        IdentityName: str = None
    ) -> GetStudioSessionMappingOutputTypeDef:
        """
        Fetches mapping details for the specified Amazon EMR Studio and identity (user
        or group).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.get_studio_session_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#get_studio_session_mapping)
        """
    def list_bootstrap_actions(
        self, *, ClusterId: str, Marker: str = None
    ) -> ListBootstrapActionsOutputTypeDef:
        """
        Provides information about the bootstrap actions associated with a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.list_bootstrap_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list_bootstrap_actions)
        """
    def list_clusters(
        self,
        *,
        CreatedAfter: Union[datetime, str] = None,
        CreatedBefore: Union[datetime, str] = None,
        ClusterStates: List[ClusterStateType] = None,
        Marker: str = None
    ) -> ListClustersOutputTypeDef:
        """
        Provides the status of all clusters visible to this Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.list_clusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list_clusters)
        """
    def list_instance_fleets(
        self, *, ClusterId: str, Marker: str = None
    ) -> ListInstanceFleetsOutputTypeDef:
        """
        Lists all available details about the instance fleets in a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.list_instance_fleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list_instance_fleets)
        """
    def list_instance_groups(
        self, *, ClusterId: str, Marker: str = None
    ) -> ListInstanceGroupsOutputTypeDef:
        """
        Provides all available details about the instance groups in a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.list_instance_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list_instance_groups)
        """
    def list_instances(
        self,
        *,
        ClusterId: str,
        InstanceGroupId: str = None,
        InstanceGroupTypes: List[InstanceGroupTypeType] = None,
        InstanceFleetId: str = None,
        InstanceFleetType: InstanceFleetTypeType = None,
        InstanceStates: List[InstanceStateType] = None,
        Marker: str = None
    ) -> ListInstancesOutputTypeDef:
        """
        Provides information for all active EC2 instances and EC2 instances terminated
        in the last 30 days, up to a maximum of 2,000.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.list_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list_instances)
        """
    def list_notebook_executions(
        self,
        *,
        EditorId: str = None,
        Status: NotebookExecutionStatusType = None,
        From: Union[datetime, str] = None,
        To: Union[datetime, str] = None,
        Marker: str = None
    ) -> ListNotebookExecutionsOutputTypeDef:
        """
        Provides summaries of all notebook executions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.list_notebook_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list_notebook_executions)
        """
    def list_release_labels(
        self,
        *,
        Filters: "ReleaseLabelFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListReleaseLabelsOutputTypeDef:
        """
        Retrieves release labels of EMR services in the region where the API is called.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.list_release_labels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list_release_labels)
        """
    def list_security_configurations(
        self, *, Marker: str = None
    ) -> ListSecurityConfigurationsOutputTypeDef:
        """
        Lists all the security configurations visible to this account, providing their
        creation dates and times, and their names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.list_security_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list_security_configurations)
        """
    def list_steps(
        self,
        *,
        ClusterId: str,
        StepStates: List[StepStateType] = None,
        StepIds: List[str] = None,
        Marker: str = None
    ) -> ListStepsOutputTypeDef:
        """
        Provides a list of steps for the cluster in reverse order unless you specify
        `stepIds` with the request or filter by `StepStates`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.list_steps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list_steps)
        """
    def list_studio_session_mappings(
        self, *, StudioId: str = None, IdentityType: IdentityTypeType = None, Marker: str = None
    ) -> ListStudioSessionMappingsOutputTypeDef:
        """
        Returns a list of all user or group session mappings for the Amazon EMR Studio
        specified by `StudioId` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.list_studio_session_mappings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list_studio_session_mappings)
        """
    def list_studios(self, *, Marker: str = None) -> ListStudiosOutputTypeDef:
        """
        Returns a list of all Amazon EMR Studios associated with the Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.list_studios)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list_studios)
        """
    def modify_cluster(
        self, *, ClusterId: str, StepConcurrencyLevel: int = None
    ) -> ModifyClusterOutputTypeDef:
        """
        Modifies the number of steps that can be executed concurrently for the cluster
        specified using ClusterID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.modify_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#modify_cluster)
        """
    def modify_instance_fleet(
        self, *, ClusterId: str, InstanceFleet: "InstanceFleetModifyConfigTypeDef"
    ) -> None:
        """
        Modifies the target On-Demand and target Spot capacities for the instance fleet
        with the specified InstanceFleetID within the cluster specified using ClusterID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.modify_instance_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#modify_instance_fleet)
        """
    def modify_instance_groups(
        self,
        *,
        ClusterId: str = None,
        InstanceGroups: List["InstanceGroupModifyConfigTypeDef"] = None
    ) -> None:
        """
        ModifyInstanceGroups modifies the number of nodes and configuration settings of
        an instance group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.modify_instance_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#modify_instance_groups)
        """
    def put_auto_scaling_policy(
        self, *, ClusterId: str, InstanceGroupId: str, AutoScalingPolicy: "AutoScalingPolicyTypeDef"
    ) -> PutAutoScalingPolicyOutputTypeDef:
        """
        Creates or updates an automatic scaling policy for a core instance group or task
        instance group in an Amazon EMR cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.put_auto_scaling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#put_auto_scaling_policy)
        """
    def put_auto_termination_policy(
        self, *, ClusterId: str, AutoTerminationPolicy: "AutoTerminationPolicyTypeDef" = None
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.put_auto_termination_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#put_auto_termination_policy)
        """
    def put_block_public_access_configuration(
        self, *, BlockPublicAccessConfiguration: "BlockPublicAccessConfigurationTypeDef"
    ) -> Dict[str, Any]:
        """
        Creates or updates an Amazon EMR block public access configuration for your
        Amazon Web Services account in the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.put_block_public_access_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#put_block_public_access_configuration)
        """
    def put_managed_scaling_policy(
        self, *, ClusterId: str, ManagedScalingPolicy: "ManagedScalingPolicyTypeDef"
    ) -> Dict[str, Any]:
        """
        Creates or updates a managed scaling policy for an Amazon EMR cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.put_managed_scaling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#put_managed_scaling_policy)
        """
    def remove_auto_scaling_policy(self, *, ClusterId: str, InstanceGroupId: str) -> Dict[str, Any]:
        """
        Removes an automatic scaling policy from a specified instance group within an
        EMR cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.remove_auto_scaling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#remove_auto_scaling_policy)
        """
    def remove_auto_termination_policy(self, *, ClusterId: str) -> Dict[str, Any]:
        """
        Removes an auto-termination policy from an Amazon EMR cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.remove_auto_termination_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#remove_auto_termination_policy)
        """
    def remove_managed_scaling_policy(self, *, ClusterId: str) -> Dict[str, Any]:
        """
        Removes a managed scaling policy from a specified EMR cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.remove_managed_scaling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#remove_managed_scaling_policy)
        """
    def remove_tags(self, *, ResourceId: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from an Amazon EMR resource, such as a cluster or Amazon EMR
        Studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.remove_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#remove_tags)
        """
    def run_job_flow(
        self,
        *,
        Name: str,
        Instances: "JobFlowInstancesConfigTypeDef",
        LogUri: str = None,
        LogEncryptionKmsKeyId: str = None,
        AdditionalInfo: str = None,
        AmiVersion: str = None,
        ReleaseLabel: str = None,
        Steps: List["StepConfigTypeDef"] = None,
        BootstrapActions: List["BootstrapActionConfigTypeDef"] = None,
        SupportedProducts: List[str] = None,
        NewSupportedProducts: List["SupportedProductConfigTypeDef"] = None,
        Applications: List["ApplicationTypeDef"] = None,
        Configurations: List["ConfigurationTypeDef"] = None,
        VisibleToAllUsers: bool = None,
        JobFlowRole: str = None,
        ServiceRole: str = None,
        Tags: List["TagTypeDef"] = None,
        SecurityConfiguration: str = None,
        AutoScalingRole: str = None,
        ScaleDownBehavior: ScaleDownBehaviorType = None,
        CustomAmiId: str = None,
        EbsRootVolumeSize: int = None,
        RepoUpgradeOnBoot: RepoUpgradeOnBootType = None,
        KerberosAttributes: "KerberosAttributesTypeDef" = None,
        StepConcurrencyLevel: int = None,
        ManagedScalingPolicy: "ManagedScalingPolicyTypeDef" = None,
        PlacementGroupConfigs: List["PlacementGroupConfigTypeDef"] = None,
        AutoTerminationPolicy: "AutoTerminationPolicyTypeDef" = None,
        OSReleaseLabel: str = None
    ) -> RunJobFlowOutputTypeDef:
        """
        RunJobFlow creates and starts running a new cluster (job flow).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.run_job_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#run_job_flow)
        """
    def set_termination_protection(
        self, *, JobFlowIds: List[str], TerminationProtected: bool
    ) -> None:
        """
        SetTerminationProtection locks a cluster (job flow) so the EC2 instances in the
        cluster cannot be terminated by user intervention, an API call, or in the event
        of a job-flow error.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.set_termination_protection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#set_termination_protection)
        """
    def set_visible_to_all_users(self, *, JobFlowIds: List[str], VisibleToAllUsers: bool) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.set_visible_to_all_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#set_visible_to_all_users)
        """
    def start_notebook_execution(
        self,
        *,
        EditorId: str,
        RelativePath: str,
        ExecutionEngine: "ExecutionEngineConfigTypeDef",
        ServiceRole: str,
        NotebookExecutionName: str = None,
        NotebookParams: str = None,
        NotebookInstanceSecurityGroupId: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> StartNotebookExecutionOutputTypeDef:
        """
        Starts a notebook execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.start_notebook_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#start_notebook_execution)
        """
    def stop_notebook_execution(self, *, NotebookExecutionId: str) -> None:
        """
        Stops a notebook execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.stop_notebook_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#stop_notebook_execution)
        """
    def terminate_job_flows(self, *, JobFlowIds: List[str]) -> None:
        """
        TerminateJobFlows shuts a list of clusters (job flows) down.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.terminate_job_flows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#terminate_job_flows)
        """
    def update_studio(
        self,
        *,
        StudioId: str,
        Name: str = None,
        Description: str = None,
        SubnetIds: List[str] = None,
        DefaultS3Location: str = None
    ) -> None:
        """
        Updates an Amazon EMR Studio configuration, including attributes such as name,
        description, and subnets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.update_studio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#update_studio)
        """
    def update_studio_session_mapping(
        self,
        *,
        StudioId: str,
        IdentityType: IdentityTypeType,
        SessionPolicyArn: str,
        IdentityId: str = None,
        IdentityName: str = None
    ) -> None:
        """
        Updates the session policy attached to the user or group for the specified
        Amazon EMR Studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Client.update_studio_session_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#update_studio_session_mapping)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_bootstrap_actions"]
    ) -> ListBootstrapActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Paginator.ListBootstrapActions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listbootstrapactionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_clusters"]) -> ListClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Paginator.ListClusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listclusterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_fleets"]
    ) -> ListInstanceFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Paginator.ListInstanceFleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listinstancefleetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_groups"]
    ) -> ListInstanceGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Paginator.ListInstanceGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listinstancegroupspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_instances"]) -> ListInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Paginator.ListInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listinstancespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_notebook_executions"]
    ) -> ListNotebookExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Paginator.ListNotebookExecutions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listnotebookexecutionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_configurations"]
    ) -> ListSecurityConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Paginator.ListSecurityConfigurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listsecurityconfigurationspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_steps"]) -> ListStepsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Paginator.ListSteps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#liststepspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_studio_session_mappings"]
    ) -> ListStudioSessionMappingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Paginator.ListStudioSessionMappings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#liststudiosessionmappingspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_studios"]) -> ListStudiosPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Paginator.ListStudios)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#liststudiospaginator)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["cluster_running"]) -> ClusterRunningWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Waiter.ClusterRunning)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/waiters.html#clusterrunningwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["cluster_terminated"]) -> ClusterTerminatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Waiter.ClusterTerminated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/waiters.html#clusterterminatedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["step_complete"]) -> StepCompleteWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/emr.html#EMR.Waiter.StepComplete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/waiters.html#stepcompletewaiter)
        """
