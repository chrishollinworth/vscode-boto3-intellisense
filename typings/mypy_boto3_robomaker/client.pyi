"""
Type annotations for robomaker service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_robomaker.client import RoboMakerClient

    session = Session()
    client: RoboMakerClient = session.client("robomaker")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
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
from .type_defs import (
    BatchDeleteWorldsRequestTypeDef,
    BatchDeleteWorldsResponseTypeDef,
    BatchDescribeSimulationJobRequestTypeDef,
    BatchDescribeSimulationJobResponseTypeDef,
    CancelDeploymentJobRequestTypeDef,
    CancelSimulationJobBatchRequestTypeDef,
    CancelSimulationJobRequestTypeDef,
    CancelWorldExportJobRequestTypeDef,
    CancelWorldGenerationJobRequestTypeDef,
    CreateDeploymentJobRequestTypeDef,
    CreateDeploymentJobResponseTypeDef,
    CreateFleetRequestTypeDef,
    CreateFleetResponseTypeDef,
    CreateRobotApplicationRequestTypeDef,
    CreateRobotApplicationResponseTypeDef,
    CreateRobotApplicationVersionRequestTypeDef,
    CreateRobotApplicationVersionResponseTypeDef,
    CreateRobotRequestTypeDef,
    CreateRobotResponseTypeDef,
    CreateSimulationApplicationRequestTypeDef,
    CreateSimulationApplicationResponseTypeDef,
    CreateSimulationApplicationVersionRequestTypeDef,
    CreateSimulationApplicationVersionResponseTypeDef,
    CreateSimulationJobRequestTypeDef,
    CreateSimulationJobResponseTypeDef,
    CreateWorldExportJobRequestTypeDef,
    CreateWorldExportJobResponseTypeDef,
    CreateWorldGenerationJobRequestTypeDef,
    CreateWorldGenerationJobResponseTypeDef,
    CreateWorldTemplateRequestTypeDef,
    CreateWorldTemplateResponseTypeDef,
    DeleteFleetRequestTypeDef,
    DeleteRobotApplicationRequestTypeDef,
    DeleteRobotRequestTypeDef,
    DeleteSimulationApplicationRequestTypeDef,
    DeleteWorldTemplateRequestTypeDef,
    DeregisterRobotRequestTypeDef,
    DeregisterRobotResponseTypeDef,
    DescribeDeploymentJobRequestTypeDef,
    DescribeDeploymentJobResponseTypeDef,
    DescribeFleetRequestTypeDef,
    DescribeFleetResponseTypeDef,
    DescribeRobotApplicationRequestTypeDef,
    DescribeRobotApplicationResponseTypeDef,
    DescribeRobotRequestTypeDef,
    DescribeRobotResponseTypeDef,
    DescribeSimulationApplicationRequestTypeDef,
    DescribeSimulationApplicationResponseTypeDef,
    DescribeSimulationJobBatchRequestTypeDef,
    DescribeSimulationJobBatchResponseTypeDef,
    DescribeSimulationJobRequestTypeDef,
    DescribeSimulationJobResponseTypeDef,
    DescribeWorldExportJobRequestTypeDef,
    DescribeWorldExportJobResponseTypeDef,
    DescribeWorldGenerationJobRequestTypeDef,
    DescribeWorldGenerationJobResponseTypeDef,
    DescribeWorldRequestTypeDef,
    DescribeWorldResponseTypeDef,
    DescribeWorldTemplateRequestTypeDef,
    DescribeWorldTemplateResponseTypeDef,
    GetWorldTemplateBodyRequestTypeDef,
    GetWorldTemplateBodyResponseTypeDef,
    ListDeploymentJobsRequestTypeDef,
    ListDeploymentJobsResponseTypeDef,
    ListFleetsRequestTypeDef,
    ListFleetsResponseTypeDef,
    ListRobotApplicationsRequestTypeDef,
    ListRobotApplicationsResponseTypeDef,
    ListRobotsRequestTypeDef,
    ListRobotsResponseTypeDef,
    ListSimulationApplicationsRequestTypeDef,
    ListSimulationApplicationsResponseTypeDef,
    ListSimulationJobBatchesRequestTypeDef,
    ListSimulationJobBatchesResponseTypeDef,
    ListSimulationJobsRequestTypeDef,
    ListSimulationJobsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWorldExportJobsRequestTypeDef,
    ListWorldExportJobsResponseTypeDef,
    ListWorldGenerationJobsRequestTypeDef,
    ListWorldGenerationJobsResponseTypeDef,
    ListWorldsRequestTypeDef,
    ListWorldsResponseTypeDef,
    ListWorldTemplatesRequestTypeDef,
    ListWorldTemplatesResponseTypeDef,
    RegisterRobotRequestTypeDef,
    RegisterRobotResponseTypeDef,
    RestartSimulationJobRequestTypeDef,
    StartSimulationJobBatchRequestTypeDef,
    StartSimulationJobBatchResponseTypeDef,
    SyncDeploymentJobRequestTypeDef,
    SyncDeploymentJobResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateRobotApplicationRequestTypeDef,
    UpdateRobotApplicationResponseTypeDef,
    UpdateSimulationApplicationRequestTypeDef,
    UpdateSimulationApplicationResponseTypeDef,
    UpdateWorldTemplateRequestTypeDef,
    UpdateWorldTemplateResponseTypeDef,
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

__all__ = ("RoboMakerClient",)

class Exceptions(BaseClientExceptions):
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

class RoboMakerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        RoboMakerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#generate_presigned_url)
        """

    def batch_delete_worlds(
        self, **kwargs: Unpack[BatchDeleteWorldsRequestTypeDef]
    ) -> BatchDeleteWorldsResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/batch_delete_worlds.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#batch_delete_worlds)
        """

    def batch_describe_simulation_job(
        self, **kwargs: Unpack[BatchDescribeSimulationJobRequestTypeDef]
    ) -> BatchDescribeSimulationJobResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/batch_describe_simulation_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#batch_describe_simulation_job)
        """

    def cancel_deployment_job(
        self, **kwargs: Unpack[CancelDeploymentJobRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This API is no longer supported.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/cancel_deployment_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#cancel_deployment_job)
        """

    def cancel_simulation_job(
        self, **kwargs: Unpack[CancelSimulationJobRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/cancel_simulation_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#cancel_simulation_job)
        """

    def cancel_simulation_job_batch(
        self, **kwargs: Unpack[CancelSimulationJobBatchRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/cancel_simulation_job_batch.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#cancel_simulation_job_batch)
        """

    def cancel_world_export_job(
        self, **kwargs: Unpack[CancelWorldExportJobRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/cancel_world_export_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#cancel_world_export_job)
        """

    def cancel_world_generation_job(
        self, **kwargs: Unpack[CancelWorldGenerationJobRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/cancel_world_generation_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#cancel_world_generation_job)
        """

    def create_deployment_job(
        self, **kwargs: Unpack[CreateDeploymentJobRequestTypeDef]
    ) -> CreateDeploymentJobResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/create_deployment_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#create_deployment_job)
        """

    def create_fleet(
        self, **kwargs: Unpack[CreateFleetRequestTypeDef]
    ) -> CreateFleetResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/create_fleet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#create_fleet)
        """

    def create_robot(
        self, **kwargs: Unpack[CreateRobotRequestTypeDef]
    ) -> CreateRobotResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/create_robot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#create_robot)
        """

    def create_robot_application(
        self, **kwargs: Unpack[CreateRobotApplicationRequestTypeDef]
    ) -> CreateRobotApplicationResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/create_robot_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#create_robot_application)
        """

    def create_robot_application_version(
        self, **kwargs: Unpack[CreateRobotApplicationVersionRequestTypeDef]
    ) -> CreateRobotApplicationVersionResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/create_robot_application_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#create_robot_application_version)
        """

    def create_simulation_application(
        self, **kwargs: Unpack[CreateSimulationApplicationRequestTypeDef]
    ) -> CreateSimulationApplicationResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/create_simulation_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#create_simulation_application)
        """

    def create_simulation_application_version(
        self, **kwargs: Unpack[CreateSimulationApplicationVersionRequestTypeDef]
    ) -> CreateSimulationApplicationVersionResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/create_simulation_application_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#create_simulation_application_version)
        """

    def create_simulation_job(
        self, **kwargs: Unpack[CreateSimulationJobRequestTypeDef]
    ) -> CreateSimulationJobResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/create_simulation_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#create_simulation_job)
        """

    def create_world_export_job(
        self, **kwargs: Unpack[CreateWorldExportJobRequestTypeDef]
    ) -> CreateWorldExportJobResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/create_world_export_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#create_world_export_job)
        """

    def create_world_generation_job(
        self, **kwargs: Unpack[CreateWorldGenerationJobRequestTypeDef]
    ) -> CreateWorldGenerationJobResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/create_world_generation_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#create_world_generation_job)
        """

    def create_world_template(
        self, **kwargs: Unpack[CreateWorldTemplateRequestTypeDef]
    ) -> CreateWorldTemplateResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/create_world_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#create_world_template)
        """

    def delete_fleet(self, **kwargs: Unpack[DeleteFleetRequestTypeDef]) -> Dict[str, Any]:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/delete_fleet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#delete_fleet)
        """

    def delete_robot(self, **kwargs: Unpack[DeleteRobotRequestTypeDef]) -> Dict[str, Any]:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/delete_robot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#delete_robot)
        """

    def delete_robot_application(
        self, **kwargs: Unpack[DeleteRobotApplicationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/delete_robot_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#delete_robot_application)
        """

    def delete_simulation_application(
        self, **kwargs: Unpack[DeleteSimulationApplicationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/delete_simulation_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#delete_simulation_application)
        """

    def delete_world_template(
        self, **kwargs: Unpack[DeleteWorldTemplateRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/delete_world_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#delete_world_template)
        """

    def deregister_robot(
        self, **kwargs: Unpack[DeregisterRobotRequestTypeDef]
    ) -> DeregisterRobotResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/deregister_robot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#deregister_robot)
        """

    def describe_deployment_job(
        self, **kwargs: Unpack[DescribeDeploymentJobRequestTypeDef]
    ) -> DescribeDeploymentJobResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/describe_deployment_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#describe_deployment_job)
        """

    def describe_fleet(
        self, **kwargs: Unpack[DescribeFleetRequestTypeDef]
    ) -> DescribeFleetResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/describe_fleet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#describe_fleet)
        """

    def describe_robot(
        self, **kwargs: Unpack[DescribeRobotRequestTypeDef]
    ) -> DescribeRobotResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/describe_robot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#describe_robot)
        """

    def describe_robot_application(
        self, **kwargs: Unpack[DescribeRobotApplicationRequestTypeDef]
    ) -> DescribeRobotApplicationResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/describe_robot_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#describe_robot_application)
        """

    def describe_simulation_application(
        self, **kwargs: Unpack[DescribeSimulationApplicationRequestTypeDef]
    ) -> DescribeSimulationApplicationResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/describe_simulation_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#describe_simulation_application)
        """

    def describe_simulation_job(
        self, **kwargs: Unpack[DescribeSimulationJobRequestTypeDef]
    ) -> DescribeSimulationJobResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/describe_simulation_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#describe_simulation_job)
        """

    def describe_simulation_job_batch(
        self, **kwargs: Unpack[DescribeSimulationJobBatchRequestTypeDef]
    ) -> DescribeSimulationJobBatchResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/describe_simulation_job_batch.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#describe_simulation_job_batch)
        """

    def describe_world(
        self, **kwargs: Unpack[DescribeWorldRequestTypeDef]
    ) -> DescribeWorldResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/describe_world.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#describe_world)
        """

    def describe_world_export_job(
        self, **kwargs: Unpack[DescribeWorldExportJobRequestTypeDef]
    ) -> DescribeWorldExportJobResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/describe_world_export_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#describe_world_export_job)
        """

    def describe_world_generation_job(
        self, **kwargs: Unpack[DescribeWorldGenerationJobRequestTypeDef]
    ) -> DescribeWorldGenerationJobResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/describe_world_generation_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#describe_world_generation_job)
        """

    def describe_world_template(
        self, **kwargs: Unpack[DescribeWorldTemplateRequestTypeDef]
    ) -> DescribeWorldTemplateResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/describe_world_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#describe_world_template)
        """

    def get_world_template_body(
        self, **kwargs: Unpack[GetWorldTemplateBodyRequestTypeDef]
    ) -> GetWorldTemplateBodyResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/get_world_template_body.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#get_world_template_body)
        """

    def list_deployment_jobs(
        self, **kwargs: Unpack[ListDeploymentJobsRequestTypeDef]
    ) -> ListDeploymentJobsResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/list_deployment_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#list_deployment_jobs)
        """

    def list_fleets(self, **kwargs: Unpack[ListFleetsRequestTypeDef]) -> ListFleetsResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/list_fleets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#list_fleets)
        """

    def list_robot_applications(
        self, **kwargs: Unpack[ListRobotApplicationsRequestTypeDef]
    ) -> ListRobotApplicationsResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/list_robot_applications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#list_robot_applications)
        """

    def list_robots(self, **kwargs: Unpack[ListRobotsRequestTypeDef]) -> ListRobotsResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/list_robots.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#list_robots)
        """

    def list_simulation_applications(
        self, **kwargs: Unpack[ListSimulationApplicationsRequestTypeDef]
    ) -> ListSimulationApplicationsResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/list_simulation_applications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#list_simulation_applications)
        """

    def list_simulation_job_batches(
        self, **kwargs: Unpack[ListSimulationJobBatchesRequestTypeDef]
    ) -> ListSimulationJobBatchesResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/list_simulation_job_batches.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#list_simulation_job_batches)
        """

    def list_simulation_jobs(
        self, **kwargs: Unpack[ListSimulationJobsRequestTypeDef]
    ) -> ListSimulationJobsResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/list_simulation_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#list_simulation_jobs)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#list_tags_for_resource)
        """

    def list_world_export_jobs(
        self, **kwargs: Unpack[ListWorldExportJobsRequestTypeDef]
    ) -> ListWorldExportJobsResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/list_world_export_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#list_world_export_jobs)
        """

    def list_world_generation_jobs(
        self, **kwargs: Unpack[ListWorldGenerationJobsRequestTypeDef]
    ) -> ListWorldGenerationJobsResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/list_world_generation_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#list_world_generation_jobs)
        """

    def list_world_templates(
        self, **kwargs: Unpack[ListWorldTemplatesRequestTypeDef]
    ) -> ListWorldTemplatesResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/list_world_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#list_world_templates)
        """

    def list_worlds(self, **kwargs: Unpack[ListWorldsRequestTypeDef]) -> ListWorldsResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/list_worlds.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#list_worlds)
        """

    def register_robot(
        self, **kwargs: Unpack[RegisterRobotRequestTypeDef]
    ) -> RegisterRobotResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/register_robot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#register_robot)
        """

    def restart_simulation_job(
        self, **kwargs: Unpack[RestartSimulationJobRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/restart_simulation_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#restart_simulation_job)
        """

    def start_simulation_job_batch(
        self, **kwargs: Unpack[StartSimulationJobBatchRequestTypeDef]
    ) -> StartSimulationJobBatchResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/start_simulation_job_batch.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#start_simulation_job_batch)
        """

    def sync_deployment_job(
        self, **kwargs: Unpack[SyncDeploymentJobRequestTypeDef]
    ) -> SyncDeploymentJobResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/sync_deployment_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#sync_deployment_job)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#untag_resource)
        """

    def update_robot_application(
        self, **kwargs: Unpack[UpdateRobotApplicationRequestTypeDef]
    ) -> UpdateRobotApplicationResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/update_robot_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#update_robot_application)
        """

    def update_simulation_application(
        self, **kwargs: Unpack[UpdateSimulationApplicationRequestTypeDef]
    ) -> UpdateSimulationApplicationResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/update_simulation_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#update_simulation_application)
        """

    def update_world_template(
        self, **kwargs: Unpack[UpdateWorldTemplateRequestTypeDef]
    ) -> UpdateWorldTemplateResponseTypeDef:
        """
        End of support notice: On September 10, 2025, Amazon Web Services will
        discontinue support for Amazon Web Services RoboMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/update_world_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#update_world_template)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_deployment_jobs"]
    ) -> ListDeploymentJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_fleets"]
    ) -> ListFleetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_robot_applications"]
    ) -> ListRobotApplicationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_robots"]
    ) -> ListRobotsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_simulation_applications"]
    ) -> ListSimulationApplicationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_simulation_job_batches"]
    ) -> ListSimulationJobBatchesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_simulation_jobs"]
    ) -> ListSimulationJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_world_export_jobs"]
    ) -> ListWorldExportJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_world_generation_jobs"]
    ) -> ListWorldGenerationJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_world_templates"]
    ) -> ListWorldTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_worlds"]
    ) -> ListWorldsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client/#get_paginator)
        """
