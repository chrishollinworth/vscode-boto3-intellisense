# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for robomaker service client

Usage::

    ```python
    import boto3
    from mypy_boto3_robomaker import RoboMakerClient

    client: RoboMakerClient = boto3.client("robomaker")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_robomaker.paginator import (
    ListDeploymentJobsPaginator,
    ListFleetsPaginator,
    ListRobotApplicationsPaginator,
    ListRobotsPaginator,
    ListSimulationApplicationsPaginator,
    ListSimulationJobBatchesPaginator,
    ListSimulationJobsPaginator,
    ListWorldExportJobsPaginator,
    ListWorldGenerationJobsPaginator,
    ListWorldsPaginator,
    ListWorldTemplatesPaginator,
)
from mypy_boto3_robomaker.type_defs import (
    BatchDeleteWorldsResponseTypeDef,
    BatchDescribeSimulationJobResponseTypeDef,
    BatchPolicyTypeDef,
    ComputeTypeDef,
    CreateDeploymentJobResponseTypeDef,
    CreateFleetResponseTypeDef,
    CreateRobotApplicationResponseTypeDef,
    CreateRobotApplicationVersionResponseTypeDef,
    CreateRobotResponseTypeDef,
    CreateSimulationApplicationResponseTypeDef,
    CreateSimulationApplicationVersionResponseTypeDef,
    CreateSimulationJobResponseTypeDef,
    CreateWorldExportJobResponseTypeDef,
    CreateWorldGenerationJobResponseTypeDef,
    CreateWorldTemplateResponseTypeDef,
    DataSourceConfigTypeDef,
    DeploymentApplicationConfigTypeDef,
    DeploymentConfigTypeDef,
    DeregisterRobotResponseTypeDef,
    DescribeDeploymentJobResponseTypeDef,
    DescribeFleetResponseTypeDef,
    DescribeRobotApplicationResponseTypeDef,
    DescribeRobotResponseTypeDef,
    DescribeSimulationApplicationResponseTypeDef,
    DescribeSimulationJobBatchResponseTypeDef,
    DescribeSimulationJobResponseTypeDef,
    DescribeWorldExportJobResponseTypeDef,
    DescribeWorldGenerationJobResponseTypeDef,
    DescribeWorldResponseTypeDef,
    DescribeWorldTemplateResponseTypeDef,
    FilterTypeDef,
    GetWorldTemplateBodyResponseTypeDef,
    ListDeploymentJobsResponseTypeDef,
    ListFleetsResponseTypeDef,
    ListRobotApplicationsResponseTypeDef,
    ListRobotsResponseTypeDef,
    ListSimulationApplicationsResponseTypeDef,
    ListSimulationJobBatchesResponseTypeDef,
    ListSimulationJobsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWorldExportJobsResponseTypeDef,
    ListWorldGenerationJobsResponseTypeDef,
    ListWorldsResponseTypeDef,
    ListWorldTemplatesResponseTypeDef,
    LoggingConfigTypeDef,
    OutputLocationTypeDef,
    RegisterRobotResponseTypeDef,
    RenderingEngineTypeDef,
    RobotApplicationConfigTypeDef,
    RobotSoftwareSuiteTypeDef,
    SimulationApplicationConfigTypeDef,
    SimulationJobRequestTypeDef,
    SimulationSoftwareSuiteTypeDef,
    SourceConfigTypeDef,
    StartSimulationJobBatchResponseTypeDef,
    SyncDeploymentJobResponseTypeDef,
    TemplateLocationTypeDef,
    UpdateRobotApplicationResponseTypeDef,
    UpdateSimulationApplicationResponseTypeDef,
    UpdateWorldTemplateResponseTypeDef,
    VPCConfigTypeDef,
    WorldCountTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("RoboMakerClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentDeploymentException: Type[BotocoreClientError]
    IdempotentParameterMismatchException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]


class RoboMakerClient:
    """
    [RoboMaker.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_delete_worlds(self, worlds: List[str]) -> BatchDeleteWorldsResponseTypeDef:
        """
        [Client.batch_delete_worlds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.batch_delete_worlds)
        """

    def batch_describe_simulation_job(
        self, jobs: List[str]
    ) -> BatchDescribeSimulationJobResponseTypeDef:
        """
        [Client.batch_describe_simulation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.batch_describe_simulation_job)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.can_paginate)
        """

    def cancel_deployment_job(self, job: str) -> Dict[str, Any]:
        """
        [Client.cancel_deployment_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.cancel_deployment_job)
        """

    def cancel_simulation_job(self, job: str) -> Dict[str, Any]:
        """
        [Client.cancel_simulation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.cancel_simulation_job)
        """

    def cancel_simulation_job_batch(self, batch: str) -> Dict[str, Any]:
        """
        [Client.cancel_simulation_job_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.cancel_simulation_job_batch)
        """

    def cancel_world_export_job(self, job: str) -> Dict[str, Any]:
        """
        [Client.cancel_world_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.cancel_world_export_job)
        """

    def cancel_world_generation_job(self, job: str) -> Dict[str, Any]:
        """
        [Client.cancel_world_generation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.cancel_world_generation_job)
        """

    def create_deployment_job(
        self,
        clientRequestToken: str,
        fleet: str,
        deploymentApplicationConfigs: List["DeploymentApplicationConfigTypeDef"],
        deploymentConfig: "DeploymentConfigTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> CreateDeploymentJobResponseTypeDef:
        """
        [Client.create_deployment_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.create_deployment_job)
        """

    def create_fleet(self, name: str, tags: Dict[str, str] = None) -> CreateFleetResponseTypeDef:
        """
        [Client.create_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.create_fleet)
        """

    def create_robot(
        self,
        name: str,
        architecture: Literal["X86_64", "ARM64", "ARMHF"],
        greengrassGroupId: str,
        tags: Dict[str, str] = None,
    ) -> CreateRobotResponseTypeDef:
        """
        [Client.create_robot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.create_robot)
        """

    def create_robot_application(
        self,
        name: str,
        sources: List[SourceConfigTypeDef],
        robotSoftwareSuite: "RobotSoftwareSuiteTypeDef",
        tags: Dict[str, str] = None,
    ) -> CreateRobotApplicationResponseTypeDef:
        """
        [Client.create_robot_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.create_robot_application)
        """

    def create_robot_application_version(
        self, application: str, currentRevisionId: str = None
    ) -> CreateRobotApplicationVersionResponseTypeDef:
        """
        [Client.create_robot_application_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.create_robot_application_version)
        """

    def create_simulation_application(
        self,
        name: str,
        sources: List[SourceConfigTypeDef],
        simulationSoftwareSuite: "SimulationSoftwareSuiteTypeDef",
        robotSoftwareSuite: "RobotSoftwareSuiteTypeDef",
        renderingEngine: "RenderingEngineTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> CreateSimulationApplicationResponseTypeDef:
        """
        [Client.create_simulation_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.create_simulation_application)
        """

    def create_simulation_application_version(
        self, application: str, currentRevisionId: str = None
    ) -> CreateSimulationApplicationVersionResponseTypeDef:
        """
        [Client.create_simulation_application_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.create_simulation_application_version)
        """

    def create_simulation_job(
        self,
        maxJobDurationInSeconds: int,
        iamRole: str,
        clientRequestToken: str = None,
        outputLocation: "OutputLocationTypeDef" = None,
        loggingConfig: "LoggingConfigTypeDef" = None,
        failureBehavior: Literal["Fail", "Continue"] = None,
        robotApplications: List["RobotApplicationConfigTypeDef"] = None,
        simulationApplications: List["SimulationApplicationConfigTypeDef"] = None,
        dataSources: List["DataSourceConfigTypeDef"] = None,
        tags: Dict[str, str] = None,
        vpcConfig: "VPCConfigTypeDef" = None,
        compute: "ComputeTypeDef" = None,
    ) -> CreateSimulationJobResponseTypeDef:
        """
        [Client.create_simulation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.create_simulation_job)
        """

    def create_world_export_job(
        self,
        worlds: List[str],
        outputLocation: "OutputLocationTypeDef",
        iamRole: str,
        clientRequestToken: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateWorldExportJobResponseTypeDef:
        """
        [Client.create_world_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.create_world_export_job)
        """

    def create_world_generation_job(
        self,
        template: str,
        worldCount: "WorldCountTypeDef",
        clientRequestToken: str = None,
        tags: Dict[str, str] = None,
        worldTags: Dict[str, str] = None,
    ) -> CreateWorldGenerationJobResponseTypeDef:
        """
        [Client.create_world_generation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.create_world_generation_job)
        """

    def create_world_template(
        self,
        clientRequestToken: str = None,
        name: str = None,
        templateBody: str = None,
        templateLocation: TemplateLocationTypeDef = None,
        tags: Dict[str, str] = None,
    ) -> CreateWorldTemplateResponseTypeDef:
        """
        [Client.create_world_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.create_world_template)
        """

    def delete_fleet(self, fleet: str) -> Dict[str, Any]:
        """
        [Client.delete_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.delete_fleet)
        """

    def delete_robot(self, robot: str) -> Dict[str, Any]:
        """
        [Client.delete_robot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.delete_robot)
        """

    def delete_robot_application(
        self, application: str, applicationVersion: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_robot_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.delete_robot_application)
        """

    def delete_simulation_application(
        self, application: str, applicationVersion: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_simulation_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.delete_simulation_application)
        """

    def delete_world_template(self, template: str) -> Dict[str, Any]:
        """
        [Client.delete_world_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.delete_world_template)
        """

    def deregister_robot(self, fleet: str, robot: str) -> DeregisterRobotResponseTypeDef:
        """
        [Client.deregister_robot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.deregister_robot)
        """

    def describe_deployment_job(self, job: str) -> DescribeDeploymentJobResponseTypeDef:
        """
        [Client.describe_deployment_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.describe_deployment_job)
        """

    def describe_fleet(self, fleet: str) -> DescribeFleetResponseTypeDef:
        """
        [Client.describe_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.describe_fleet)
        """

    def describe_robot(self, robot: str) -> DescribeRobotResponseTypeDef:
        """
        [Client.describe_robot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.describe_robot)
        """

    def describe_robot_application(
        self, application: str, applicationVersion: str = None
    ) -> DescribeRobotApplicationResponseTypeDef:
        """
        [Client.describe_robot_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.describe_robot_application)
        """

    def describe_simulation_application(
        self, application: str, applicationVersion: str = None
    ) -> DescribeSimulationApplicationResponseTypeDef:
        """
        [Client.describe_simulation_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.describe_simulation_application)
        """

    def describe_simulation_job(self, job: str) -> DescribeSimulationJobResponseTypeDef:
        """
        [Client.describe_simulation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.describe_simulation_job)
        """

    def describe_simulation_job_batch(
        self, batch: str
    ) -> DescribeSimulationJobBatchResponseTypeDef:
        """
        [Client.describe_simulation_job_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.describe_simulation_job_batch)
        """

    def describe_world(self, world: str) -> DescribeWorldResponseTypeDef:
        """
        [Client.describe_world documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.describe_world)
        """

    def describe_world_export_job(self, job: str) -> DescribeWorldExportJobResponseTypeDef:
        """
        [Client.describe_world_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.describe_world_export_job)
        """

    def describe_world_generation_job(self, job: str) -> DescribeWorldGenerationJobResponseTypeDef:
        """
        [Client.describe_world_generation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.describe_world_generation_job)
        """

    def describe_world_template(self, template: str) -> DescribeWorldTemplateResponseTypeDef:
        """
        [Client.describe_world_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.describe_world_template)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.generate_presigned_url)
        """

    def get_world_template_body(
        self, template: str = None, generationJob: str = None
    ) -> GetWorldTemplateBodyResponseTypeDef:
        """
        [Client.get_world_template_body documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.get_world_template_body)
        """

    def list_deployment_jobs(
        self, filters: List[FilterTypeDef] = None, nextToken: str = None, maxResults: int = None
    ) -> ListDeploymentJobsResponseTypeDef:
        """
        [Client.list_deployment_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.list_deployment_jobs)
        """

    def list_fleets(
        self, nextToken: str = None, maxResults: int = None, filters: List[FilterTypeDef] = None
    ) -> ListFleetsResponseTypeDef:
        """
        [Client.list_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.list_fleets)
        """

    def list_robot_applications(
        self,
        versionQualifier: str = None,
        nextToken: str = None,
        maxResults: int = None,
        filters: List[FilterTypeDef] = None,
    ) -> ListRobotApplicationsResponseTypeDef:
        """
        [Client.list_robot_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.list_robot_applications)
        """

    def list_robots(
        self, nextToken: str = None, maxResults: int = None, filters: List[FilterTypeDef] = None
    ) -> ListRobotsResponseTypeDef:
        """
        [Client.list_robots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.list_robots)
        """

    def list_simulation_applications(
        self,
        versionQualifier: str = None,
        nextToken: str = None,
        maxResults: int = None,
        filters: List[FilterTypeDef] = None,
    ) -> ListSimulationApplicationsResponseTypeDef:
        """
        [Client.list_simulation_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.list_simulation_applications)
        """

    def list_simulation_job_batches(
        self, nextToken: str = None, maxResults: int = None, filters: List[FilterTypeDef] = None
    ) -> ListSimulationJobBatchesResponseTypeDef:
        """
        [Client.list_simulation_job_batches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.list_simulation_job_batches)
        """

    def list_simulation_jobs(
        self, nextToken: str = None, maxResults: int = None, filters: List[FilterTypeDef] = None
    ) -> ListSimulationJobsResponseTypeDef:
        """
        [Client.list_simulation_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.list_simulation_jobs)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.list_tags_for_resource)
        """

    def list_world_export_jobs(
        self, nextToken: str = None, maxResults: int = None, filters: List[FilterTypeDef] = None
    ) -> ListWorldExportJobsResponseTypeDef:
        """
        [Client.list_world_export_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.list_world_export_jobs)
        """

    def list_world_generation_jobs(
        self, nextToken: str = None, maxResults: int = None, filters: List[FilterTypeDef] = None
    ) -> ListWorldGenerationJobsResponseTypeDef:
        """
        [Client.list_world_generation_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.list_world_generation_jobs)
        """

    def list_world_templates(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListWorldTemplatesResponseTypeDef:
        """
        [Client.list_world_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.list_world_templates)
        """

    def list_worlds(
        self, nextToken: str = None, maxResults: int = None, filters: List[FilterTypeDef] = None
    ) -> ListWorldsResponseTypeDef:
        """
        [Client.list_worlds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.list_worlds)
        """

    def register_robot(self, fleet: str, robot: str) -> RegisterRobotResponseTypeDef:
        """
        [Client.register_robot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.register_robot)
        """

    def restart_simulation_job(self, job: str) -> Dict[str, Any]:
        """
        [Client.restart_simulation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.restart_simulation_job)
        """

    def start_simulation_job_batch(
        self,
        createSimulationJobRequests: List["SimulationJobRequestTypeDef"],
        clientRequestToken: str = None,
        batchPolicy: "BatchPolicyTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> StartSimulationJobBatchResponseTypeDef:
        """
        [Client.start_simulation_job_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.start_simulation_job_batch)
        """

    def sync_deployment_job(
        self, clientRequestToken: str, fleet: str
    ) -> SyncDeploymentJobResponseTypeDef:
        """
        [Client.sync_deployment_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.sync_deployment_job)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.untag_resource)
        """

    def update_robot_application(
        self,
        application: str,
        sources: List[SourceConfigTypeDef],
        robotSoftwareSuite: "RobotSoftwareSuiteTypeDef",
        currentRevisionId: str = None,
    ) -> UpdateRobotApplicationResponseTypeDef:
        """
        [Client.update_robot_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.update_robot_application)
        """

    def update_simulation_application(
        self,
        application: str,
        sources: List[SourceConfigTypeDef],
        simulationSoftwareSuite: "SimulationSoftwareSuiteTypeDef",
        robotSoftwareSuite: "RobotSoftwareSuiteTypeDef",
        renderingEngine: "RenderingEngineTypeDef" = None,
        currentRevisionId: str = None,
    ) -> UpdateSimulationApplicationResponseTypeDef:
        """
        [Client.update_simulation_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.update_simulation_application)
        """

    def update_world_template(
        self,
        template: str,
        name: str = None,
        templateBody: str = None,
        templateLocation: TemplateLocationTypeDef = None,
    ) -> UpdateWorldTemplateResponseTypeDef:
        """
        [Client.update_world_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Client.update_world_template)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployment_jobs"]
    ) -> ListDeploymentJobsPaginator:
        """
        [Paginator.ListDeploymentJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListDeploymentJobs)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_fleets"]) -> ListFleetsPaginator:
        """
        [Paginator.ListFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListFleets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_robot_applications"]
    ) -> ListRobotApplicationsPaginator:
        """
        [Paginator.ListRobotApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListRobotApplications)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_robots"]) -> ListRobotsPaginator:
        """
        [Paginator.ListRobots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListRobots)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_simulation_applications"]
    ) -> ListSimulationApplicationsPaginator:
        """
        [Paginator.ListSimulationApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListSimulationApplications)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_simulation_job_batches"]
    ) -> ListSimulationJobBatchesPaginator:
        """
        [Paginator.ListSimulationJobBatches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListSimulationJobBatches)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_simulation_jobs"]
    ) -> ListSimulationJobsPaginator:
        """
        [Paginator.ListSimulationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListSimulationJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_world_export_jobs"]
    ) -> ListWorldExportJobsPaginator:
        """
        [Paginator.ListWorldExportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListWorldExportJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_world_generation_jobs"]
    ) -> ListWorldGenerationJobsPaginator:
        """
        [Paginator.ListWorldGenerationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListWorldGenerationJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_world_templates"]
    ) -> ListWorldTemplatesPaginator:
        """
        [Paginator.ListWorldTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListWorldTemplates)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_worlds"]) -> ListWorldsPaginator:
        """
        [Paginator.ListWorlds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListWorlds)
        """
