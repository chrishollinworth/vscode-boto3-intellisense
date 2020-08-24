# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for emr service client

Usage::

    ```python
    import boto3
    from mypy_boto3_emr import EMRClient

    client: EMRClient = boto3.client("emr")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_emr.paginator import (
    ListBootstrapActionsPaginator,
    ListClustersPaginator,
    ListInstanceFleetsPaginator,
    ListInstanceGroupsPaginator,
    ListInstancesPaginator,
    ListSecurityConfigurationsPaginator,
    ListStepsPaginator,
)
from mypy_boto3_emr.type_defs import (
    AddInstanceFleetOutputTypeDef,
    AddInstanceGroupsOutputTypeDef,
    AddJobFlowStepsOutputTypeDef,
    ApplicationTypeDef,
    AutoScalingPolicyTypeDef,
    BlockPublicAccessConfigurationTypeDef,
    BootstrapActionConfigTypeDef,
    CancelStepsOutputTypeDef,
    CreateSecurityConfigurationOutputTypeDef,
    DescribeClusterOutputTypeDef,
    DescribeJobFlowsOutputTypeDef,
    DescribeSecurityConfigurationOutputTypeDef,
    DescribeStepOutputTypeDef,
    GetBlockPublicAccessConfigurationOutputTypeDef,
    GetManagedScalingPolicyOutputTypeDef,
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
    ListSecurityConfigurationsOutputTypeDef,
    ListStepsOutputTypeDef,
    ManagedScalingPolicyTypeDef,
    ModifyClusterOutputTypeDef,
    PutAutoScalingPolicyOutputTypeDef,
    RunJobFlowOutputTypeDef,
    StepConfigTypeDef,
    SupportedProductConfigTypeDef,
    TagTypeDef,
)
from mypy_boto3_emr.waiter import ClusterRunningWaiter, ClusterTerminatedWaiter, StepCompleteWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("EMRClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    InternalServerError: Type[Boto3ClientError]
    InternalServerException: Type[Boto3ClientError]
    InvalidRequestException: Type[Boto3ClientError]


class EMRClient:
    """
    [EMR.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client)
    """

    exceptions: Exceptions

    def add_instance_fleet(
        self, ClusterId: str, InstanceFleet: "InstanceFleetConfigTypeDef"
    ) -> AddInstanceFleetOutputTypeDef:
        """
        [Client.add_instance_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.add_instance_fleet)
        """

    def add_instance_groups(
        self, InstanceGroups: List["InstanceGroupConfigTypeDef"], JobFlowId: str
    ) -> AddInstanceGroupsOutputTypeDef:
        """
        [Client.add_instance_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.add_instance_groups)
        """

    def add_job_flow_steps(
        self, JobFlowId: str, Steps: List["StepConfigTypeDef"]
    ) -> AddJobFlowStepsOutputTypeDef:
        """
        [Client.add_job_flow_steps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.add_job_flow_steps)
        """

    def add_tags(self, ResourceId: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.add_tags)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.can_paginate)
        """

    def cancel_steps(
        self,
        ClusterId: str,
        StepIds: List[str],
        StepCancellationOption: Literal["SEND_INTERRUPT", "TERMINATE_PROCESS"] = None,
    ) -> CancelStepsOutputTypeDef:
        """
        [Client.cancel_steps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.cancel_steps)
        """

    def create_security_configuration(
        self, Name: str, SecurityConfiguration: str
    ) -> CreateSecurityConfigurationOutputTypeDef:
        """
        [Client.create_security_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.create_security_configuration)
        """

    def delete_security_configuration(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_security_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.delete_security_configuration)
        """

    def describe_cluster(self, ClusterId: str) -> DescribeClusterOutputTypeDef:
        """
        [Client.describe_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.describe_cluster)
        """

    def describe_job_flows(
        self,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        JobFlowIds: List[str] = None,
        JobFlowStates: List[
            Literal[
                "STARTING",
                "BOOTSTRAPPING",
                "RUNNING",
                "WAITING",
                "SHUTTING_DOWN",
                "TERMINATED",
                "COMPLETED",
                "FAILED",
            ]
        ] = None,
    ) -> DescribeJobFlowsOutputTypeDef:
        """
        [Client.describe_job_flows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.describe_job_flows)
        """

    def describe_security_configuration(
        self, Name: str
    ) -> DescribeSecurityConfigurationOutputTypeDef:
        """
        [Client.describe_security_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.describe_security_configuration)
        """

    def describe_step(self, ClusterId: str, StepId: str) -> DescribeStepOutputTypeDef:
        """
        [Client.describe_step documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.describe_step)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.generate_presigned_url)
        """

    def get_block_public_access_configuration(
        self,
    ) -> GetBlockPublicAccessConfigurationOutputTypeDef:
        """
        [Client.get_block_public_access_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.get_block_public_access_configuration)
        """

    def get_managed_scaling_policy(self, ClusterId: str) -> GetManagedScalingPolicyOutputTypeDef:
        """
        [Client.get_managed_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.get_managed_scaling_policy)
        """

    def list_bootstrap_actions(
        self, ClusterId: str, Marker: str = None
    ) -> ListBootstrapActionsOutputTypeDef:
        """
        [Client.list_bootstrap_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.list_bootstrap_actions)
        """

    def list_clusters(
        self,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        ClusterStates: List[
            Literal[
                "STARTING",
                "BOOTSTRAPPING",
                "RUNNING",
                "WAITING",
                "TERMINATING",
                "TERMINATED",
                "TERMINATED_WITH_ERRORS",
            ]
        ] = None,
        Marker: str = None,
    ) -> ListClustersOutputTypeDef:
        """
        [Client.list_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.list_clusters)
        """

    def list_instance_fleets(
        self, ClusterId: str, Marker: str = None
    ) -> ListInstanceFleetsOutputTypeDef:
        """
        [Client.list_instance_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.list_instance_fleets)
        """

    def list_instance_groups(
        self, ClusterId: str, Marker: str = None
    ) -> ListInstanceGroupsOutputTypeDef:
        """
        [Client.list_instance_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.list_instance_groups)
        """

    def list_instances(
        self,
        ClusterId: str,
        InstanceGroupId: str = None,
        InstanceGroupTypes: List[Literal["MASTER", "CORE", "TASK"]] = None,
        InstanceFleetId: str = None,
        InstanceFleetType: Literal["MASTER", "CORE", "TASK"] = None,
        InstanceStates: List[
            Literal[
                "AWAITING_FULFILLMENT", "PROVISIONING", "BOOTSTRAPPING", "RUNNING", "TERMINATED"
            ]
        ] = None,
        Marker: str = None,
    ) -> ListInstancesOutputTypeDef:
        """
        [Client.list_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.list_instances)
        """

    def list_security_configurations(
        self, Marker: str = None
    ) -> ListSecurityConfigurationsOutputTypeDef:
        """
        [Client.list_security_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.list_security_configurations)
        """

    def list_steps(
        self,
        ClusterId: str,
        StepStates: List[
            Literal[
                "PENDING",
                "CANCEL_PENDING",
                "RUNNING",
                "COMPLETED",
                "CANCELLED",
                "FAILED",
                "INTERRUPTED",
            ]
        ] = None,
        StepIds: List[str] = None,
        Marker: str = None,
    ) -> ListStepsOutputTypeDef:
        """
        [Client.list_steps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.list_steps)
        """

    def modify_cluster(
        self, ClusterId: str, StepConcurrencyLevel: int = None
    ) -> ModifyClusterOutputTypeDef:
        """
        [Client.modify_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.modify_cluster)
        """

    def modify_instance_fleet(
        self, ClusterId: str, InstanceFleet: InstanceFleetModifyConfigTypeDef
    ) -> None:
        """
        [Client.modify_instance_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.modify_instance_fleet)
        """

    def modify_instance_groups(
        self, ClusterId: str = None, InstanceGroups: List[InstanceGroupModifyConfigTypeDef] = None
    ) -> None:
        """
        [Client.modify_instance_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.modify_instance_groups)
        """

    def put_auto_scaling_policy(
        self, ClusterId: str, InstanceGroupId: str, AutoScalingPolicy: "AutoScalingPolicyTypeDef"
    ) -> PutAutoScalingPolicyOutputTypeDef:
        """
        [Client.put_auto_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.put_auto_scaling_policy)
        """

    def put_block_public_access_configuration(
        self, BlockPublicAccessConfiguration: "BlockPublicAccessConfigurationTypeDef"
    ) -> Dict[str, Any]:
        """
        [Client.put_block_public_access_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.put_block_public_access_configuration)
        """

    def put_managed_scaling_policy(
        self, ClusterId: str, ManagedScalingPolicy: "ManagedScalingPolicyTypeDef"
    ) -> Dict[str, Any]:
        """
        [Client.put_managed_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.put_managed_scaling_policy)
        """

    def remove_auto_scaling_policy(self, ClusterId: str, InstanceGroupId: str) -> Dict[str, Any]:
        """
        [Client.remove_auto_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.remove_auto_scaling_policy)
        """

    def remove_managed_scaling_policy(self, ClusterId: str) -> Dict[str, Any]:
        """
        [Client.remove_managed_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.remove_managed_scaling_policy)
        """

    def remove_tags(self, ResourceId: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.remove_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.remove_tags)
        """

    def run_job_flow(
        self,
        Name: str,
        Instances: JobFlowInstancesConfigTypeDef,
        LogUri: str = None,
        LogEncryptionKmsKeyId: str = None,
        AdditionalInfo: str = None,
        AmiVersion: str = None,
        ReleaseLabel: str = None,
        Steps: List["StepConfigTypeDef"] = None,
        BootstrapActions: List["BootstrapActionConfigTypeDef"] = None,
        SupportedProducts: List[str] = None,
        NewSupportedProducts: List[SupportedProductConfigTypeDef] = None,
        Applications: List["ApplicationTypeDef"] = None,
        Configurations: List[Dict[str, Any]] = None,
        VisibleToAllUsers: bool = None,
        JobFlowRole: str = None,
        ServiceRole: str = None,
        Tags: List["TagTypeDef"] = None,
        SecurityConfiguration: str = None,
        AutoScalingRole: str = None,
        ScaleDownBehavior: Literal[
            "TERMINATE_AT_INSTANCE_HOUR", "TERMINATE_AT_TASK_COMPLETION"
        ] = None,
        CustomAmiId: str = None,
        EbsRootVolumeSize: int = None,
        RepoUpgradeOnBoot: Literal["SECURITY", "NONE"] = None,
        KerberosAttributes: "KerberosAttributesTypeDef" = None,
        StepConcurrencyLevel: int = None,
        ManagedScalingPolicy: "ManagedScalingPolicyTypeDef" = None,
    ) -> RunJobFlowOutputTypeDef:
        """
        [Client.run_job_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.run_job_flow)
        """

    def set_termination_protection(self, JobFlowIds: List[str], TerminationProtected: bool) -> None:
        """
        [Client.set_termination_protection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.set_termination_protection)
        """

    def set_visible_to_all_users(self, JobFlowIds: List[str], VisibleToAllUsers: bool) -> None:
        """
        [Client.set_visible_to_all_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.set_visible_to_all_users)
        """

    def terminate_job_flows(self, JobFlowIds: List[str]) -> None:
        """
        [Client.terminate_job_flows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Client.terminate_job_flows)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_bootstrap_actions"]
    ) -> ListBootstrapActionsPaginator:
        """
        [Paginator.ListBootstrapActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Paginator.ListBootstrapActions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_clusters"]) -> ListClustersPaginator:
        """
        [Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Paginator.ListClusters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_fleets"]
    ) -> ListInstanceFleetsPaginator:
        """
        [Paginator.ListInstanceFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Paginator.ListInstanceFleets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_groups"]
    ) -> ListInstanceGroupsPaginator:
        """
        [Paginator.ListInstanceGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Paginator.ListInstanceGroups)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_instances"]) -> ListInstancesPaginator:
        """
        [Paginator.ListInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Paginator.ListInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_configurations"]
    ) -> ListSecurityConfigurationsPaginator:
        """
        [Paginator.ListSecurityConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Paginator.ListSecurityConfigurations)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_steps"]) -> ListStepsPaginator:
        """
        [Paginator.ListSteps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Paginator.ListSteps)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass

    @overload
    def get_waiter(self, waiter_name: Literal["cluster_running"]) -> ClusterRunningWaiter:
        """
        [Waiter.ClusterRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Waiter.ClusterRunning)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["cluster_terminated"]) -> ClusterTerminatedWaiter:
        """
        [Waiter.ClusterTerminated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Waiter.ClusterTerminated)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["step_complete"]) -> StepCompleteWaiter:
        """
        [Waiter.StepComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/emr.html#EMR.Waiter.StepComplete)
        """

    def get_waiter(self, waiter_name: str) -> Boto3Waiter:
        pass
