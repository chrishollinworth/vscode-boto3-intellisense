"""
Type annotations for codedeploy service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_codedeploy.client import CodeDeployClient

    session = Session()
    client: CodeDeployClient = session.client("codedeploy")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListApplicationRevisionsPaginator,
    ListApplicationsPaginator,
    ListDeploymentConfigsPaginator,
    ListDeploymentGroupsPaginator,
    ListDeploymentInstancesPaginator,
    ListDeploymentsPaginator,
    ListDeploymentTargetsPaginator,
    ListGitHubAccountTokenNamesPaginator,
    ListOnPremisesInstancesPaginator,
)
from .type_defs import (
    AddTagsToOnPremisesInstancesInputTypeDef,
    BatchGetApplicationRevisionsInputTypeDef,
    BatchGetApplicationRevisionsOutputTypeDef,
    BatchGetApplicationsInputTypeDef,
    BatchGetApplicationsOutputTypeDef,
    BatchGetDeploymentGroupsInputTypeDef,
    BatchGetDeploymentGroupsOutputTypeDef,
    BatchGetDeploymentInstancesInputTypeDef,
    BatchGetDeploymentInstancesOutputTypeDef,
    BatchGetDeploymentsInputTypeDef,
    BatchGetDeploymentsOutputTypeDef,
    BatchGetDeploymentTargetsInputTypeDef,
    BatchGetDeploymentTargetsOutputTypeDef,
    BatchGetOnPremisesInstancesInputTypeDef,
    BatchGetOnPremisesInstancesOutputTypeDef,
    ContinueDeploymentInputTypeDef,
    CreateApplicationInputTypeDef,
    CreateApplicationOutputTypeDef,
    CreateDeploymentConfigInputTypeDef,
    CreateDeploymentConfigOutputTypeDef,
    CreateDeploymentGroupInputTypeDef,
    CreateDeploymentGroupOutputTypeDef,
    CreateDeploymentInputTypeDef,
    CreateDeploymentOutputTypeDef,
    DeleteApplicationInputTypeDef,
    DeleteDeploymentConfigInputTypeDef,
    DeleteDeploymentGroupInputTypeDef,
    DeleteDeploymentGroupOutputTypeDef,
    DeleteGitHubAccountTokenInputTypeDef,
    DeleteGitHubAccountTokenOutputTypeDef,
    DeleteResourcesByExternalIdInputTypeDef,
    DeregisterOnPremisesInstanceInputTypeDef,
    EmptyResponseMetadataTypeDef,
    GetApplicationInputTypeDef,
    GetApplicationOutputTypeDef,
    GetApplicationRevisionInputTypeDef,
    GetApplicationRevisionOutputTypeDef,
    GetDeploymentConfigInputTypeDef,
    GetDeploymentConfigOutputTypeDef,
    GetDeploymentGroupInputTypeDef,
    GetDeploymentGroupOutputTypeDef,
    GetDeploymentInputTypeDef,
    GetDeploymentInstanceInputTypeDef,
    GetDeploymentInstanceOutputTypeDef,
    GetDeploymentOutputTypeDef,
    GetDeploymentTargetInputTypeDef,
    GetDeploymentTargetOutputTypeDef,
    GetOnPremisesInstanceInputTypeDef,
    GetOnPremisesInstanceOutputTypeDef,
    ListApplicationRevisionsInputTypeDef,
    ListApplicationRevisionsOutputTypeDef,
    ListApplicationsInputTypeDef,
    ListApplicationsOutputTypeDef,
    ListDeploymentConfigsInputTypeDef,
    ListDeploymentConfigsOutputTypeDef,
    ListDeploymentGroupsInputTypeDef,
    ListDeploymentGroupsOutputTypeDef,
    ListDeploymentInstancesInputTypeDef,
    ListDeploymentInstancesOutputTypeDef,
    ListDeploymentsInputTypeDef,
    ListDeploymentsOutputTypeDef,
    ListDeploymentTargetsInputTypeDef,
    ListDeploymentTargetsOutputTypeDef,
    ListGitHubAccountTokenNamesInputTypeDef,
    ListGitHubAccountTokenNamesOutputTypeDef,
    ListOnPremisesInstancesInputTypeDef,
    ListOnPremisesInstancesOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    PutLifecycleEventHookExecutionStatusInputTypeDef,
    PutLifecycleEventHookExecutionStatusOutputTypeDef,
    RegisterApplicationRevisionInputTypeDef,
    RegisterOnPremisesInstanceInputTypeDef,
    RemoveTagsFromOnPremisesInstancesInputTypeDef,
    SkipWaitTimeForInstanceTerminationInputTypeDef,
    StopDeploymentInputTypeDef,
    StopDeploymentOutputTypeDef,
    TagResourceInputTypeDef,
    UntagResourceInputTypeDef,
    UpdateApplicationInputTypeDef,
    UpdateDeploymentGroupInputTypeDef,
    UpdateDeploymentGroupOutputTypeDef,
)
from .waiter import DeploymentSuccessfulWaiter

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

__all__ = ("CodeDeployClient",)

class Exceptions(BaseClientExceptions):
    AlarmsLimitExceededException: Type[BotocoreClientError]
    ApplicationAlreadyExistsException: Type[BotocoreClientError]
    ApplicationDoesNotExistException: Type[BotocoreClientError]
    ApplicationLimitExceededException: Type[BotocoreClientError]
    ApplicationNameRequiredException: Type[BotocoreClientError]
    ArnNotSupportedException: Type[BotocoreClientError]
    BatchLimitExceededException: Type[BotocoreClientError]
    BucketNameFilterRequiredException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DeploymentAlreadyCompletedException: Type[BotocoreClientError]
    DeploymentAlreadyStartedException: Type[BotocoreClientError]
    DeploymentConfigAlreadyExistsException: Type[BotocoreClientError]
    DeploymentConfigDoesNotExistException: Type[BotocoreClientError]
    DeploymentConfigInUseException: Type[BotocoreClientError]
    DeploymentConfigLimitExceededException: Type[BotocoreClientError]
    DeploymentConfigNameRequiredException: Type[BotocoreClientError]
    DeploymentDoesNotExistException: Type[BotocoreClientError]
    DeploymentGroupAlreadyExistsException: Type[BotocoreClientError]
    DeploymentGroupDoesNotExistException: Type[BotocoreClientError]
    DeploymentGroupLimitExceededException: Type[BotocoreClientError]
    DeploymentGroupNameRequiredException: Type[BotocoreClientError]
    DeploymentIdRequiredException: Type[BotocoreClientError]
    DeploymentIsNotInReadyStateException: Type[BotocoreClientError]
    DeploymentLimitExceededException: Type[BotocoreClientError]
    DeploymentNotStartedException: Type[BotocoreClientError]
    DeploymentTargetDoesNotExistException: Type[BotocoreClientError]
    DeploymentTargetIdRequiredException: Type[BotocoreClientError]
    DeploymentTargetListSizeExceededException: Type[BotocoreClientError]
    DescriptionTooLongException: Type[BotocoreClientError]
    ECSServiceMappingLimitExceededException: Type[BotocoreClientError]
    GitHubAccountTokenDoesNotExistException: Type[BotocoreClientError]
    GitHubAccountTokenNameRequiredException: Type[BotocoreClientError]
    IamArnRequiredException: Type[BotocoreClientError]
    IamSessionArnAlreadyRegisteredException: Type[BotocoreClientError]
    IamUserArnAlreadyRegisteredException: Type[BotocoreClientError]
    IamUserArnRequiredException: Type[BotocoreClientError]
    InstanceDoesNotExistException: Type[BotocoreClientError]
    InstanceIdRequiredException: Type[BotocoreClientError]
    InstanceLimitExceededException: Type[BotocoreClientError]
    InstanceNameAlreadyRegisteredException: Type[BotocoreClientError]
    InstanceNameRequiredException: Type[BotocoreClientError]
    InstanceNotRegisteredException: Type[BotocoreClientError]
    InvalidAlarmConfigException: Type[BotocoreClientError]
    InvalidApplicationNameException: Type[BotocoreClientError]
    InvalidArnException: Type[BotocoreClientError]
    InvalidAutoRollbackConfigException: Type[BotocoreClientError]
    InvalidAutoScalingGroupException: Type[BotocoreClientError]
    InvalidBlueGreenDeploymentConfigurationException: Type[BotocoreClientError]
    InvalidBucketNameFilterException: Type[BotocoreClientError]
    InvalidComputePlatformException: Type[BotocoreClientError]
    InvalidDeployedStateFilterException: Type[BotocoreClientError]
    InvalidDeploymentConfigNameException: Type[BotocoreClientError]
    InvalidDeploymentGroupNameException: Type[BotocoreClientError]
    InvalidDeploymentIdException: Type[BotocoreClientError]
    InvalidDeploymentInstanceTypeException: Type[BotocoreClientError]
    InvalidDeploymentStatusException: Type[BotocoreClientError]
    InvalidDeploymentStyleException: Type[BotocoreClientError]
    InvalidDeploymentTargetIdException: Type[BotocoreClientError]
    InvalidDeploymentWaitTypeException: Type[BotocoreClientError]
    InvalidEC2TagCombinationException: Type[BotocoreClientError]
    InvalidEC2TagException: Type[BotocoreClientError]
    InvalidECSServiceException: Type[BotocoreClientError]
    InvalidExternalIdException: Type[BotocoreClientError]
    InvalidFileExistsBehaviorException: Type[BotocoreClientError]
    InvalidGitHubAccountTokenException: Type[BotocoreClientError]
    InvalidGitHubAccountTokenNameException: Type[BotocoreClientError]
    InvalidIamSessionArnException: Type[BotocoreClientError]
    InvalidIamUserArnException: Type[BotocoreClientError]
    InvalidIgnoreApplicationStopFailuresValueException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    InvalidInstanceIdException: Type[BotocoreClientError]
    InvalidInstanceNameException: Type[BotocoreClientError]
    InvalidInstanceStatusException: Type[BotocoreClientError]
    InvalidInstanceTypeException: Type[BotocoreClientError]
    InvalidKeyPrefixFilterException: Type[BotocoreClientError]
    InvalidLifecycleEventHookExecutionIdException: Type[BotocoreClientError]
    InvalidLifecycleEventHookExecutionStatusException: Type[BotocoreClientError]
    InvalidLoadBalancerInfoException: Type[BotocoreClientError]
    InvalidMinimumHealthyHostValueException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidOnPremisesTagCombinationException: Type[BotocoreClientError]
    InvalidOperationException: Type[BotocoreClientError]
    InvalidRegistrationStatusException: Type[BotocoreClientError]
    InvalidRevisionException: Type[BotocoreClientError]
    InvalidRoleException: Type[BotocoreClientError]
    InvalidSortByException: Type[BotocoreClientError]
    InvalidSortOrderException: Type[BotocoreClientError]
    InvalidTagException: Type[BotocoreClientError]
    InvalidTagFilterException: Type[BotocoreClientError]
    InvalidTagsToAddException: Type[BotocoreClientError]
    InvalidTargetException: Type[BotocoreClientError]
    InvalidTargetFilterNameException: Type[BotocoreClientError]
    InvalidTargetGroupPairException: Type[BotocoreClientError]
    InvalidTargetInstancesException: Type[BotocoreClientError]
    InvalidTimeRangeException: Type[BotocoreClientError]
    InvalidTrafficRoutingConfigurationException: Type[BotocoreClientError]
    InvalidTriggerConfigException: Type[BotocoreClientError]
    InvalidUpdateOutdatedInstancesOnlyValueException: Type[BotocoreClientError]
    InvalidZonalDeploymentConfigurationException: Type[BotocoreClientError]
    LifecycleEventAlreadyCompletedException: Type[BotocoreClientError]
    LifecycleHookLimitExceededException: Type[BotocoreClientError]
    MultipleIamArnsProvidedException: Type[BotocoreClientError]
    OperationNotSupportedException: Type[BotocoreClientError]
    ResourceArnRequiredException: Type[BotocoreClientError]
    ResourceValidationException: Type[BotocoreClientError]
    RevisionDoesNotExistException: Type[BotocoreClientError]
    RevisionRequiredException: Type[BotocoreClientError]
    RoleRequiredException: Type[BotocoreClientError]
    TagLimitExceededException: Type[BotocoreClientError]
    TagRequiredException: Type[BotocoreClientError]
    TagSetListLimitExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TriggerTargetsLimitExceededException: Type[BotocoreClientError]
    UnsupportedActionForDeploymentTypeException: Type[BotocoreClientError]

class CodeDeployClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CodeDeployClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#generate_presigned_url)
        """

    def add_tags_to_on_premises_instances(
        self, **kwargs: Unpack[AddTagsToOnPremisesInstancesInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds tags to on-premises instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/add_tags_to_on_premises_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#add_tags_to_on_premises_instances)
        """

    def batch_get_application_revisions(
        self, **kwargs: Unpack[BatchGetApplicationRevisionsInputTypeDef]
    ) -> BatchGetApplicationRevisionsOutputTypeDef:
        """
        Gets information about one or more application revisions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/batch_get_application_revisions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#batch_get_application_revisions)
        """

    def batch_get_applications(
        self, **kwargs: Unpack[BatchGetApplicationsInputTypeDef]
    ) -> BatchGetApplicationsOutputTypeDef:
        """
        Gets information about one or more applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/batch_get_applications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#batch_get_applications)
        """

    def batch_get_deployment_groups(
        self, **kwargs: Unpack[BatchGetDeploymentGroupsInputTypeDef]
    ) -> BatchGetDeploymentGroupsOutputTypeDef:
        """
        Gets information about one or more deployment groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/batch_get_deployment_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#batch_get_deployment_groups)
        """

    def batch_get_deployment_instances(
        self, **kwargs: Unpack[BatchGetDeploymentInstancesInputTypeDef]
    ) -> BatchGetDeploymentInstancesOutputTypeDef:
        """
        This method works, but is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/batch_get_deployment_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#batch_get_deployment_instances)
        """

    def batch_get_deployment_targets(
        self, **kwargs: Unpack[BatchGetDeploymentTargetsInputTypeDef]
    ) -> BatchGetDeploymentTargetsOutputTypeDef:
        """
        Returns an array of one or more targets associated with a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/batch_get_deployment_targets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#batch_get_deployment_targets)
        """

    def batch_get_deployments(
        self, **kwargs: Unpack[BatchGetDeploymentsInputTypeDef]
    ) -> BatchGetDeploymentsOutputTypeDef:
        """
        Gets information about one or more deployments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/batch_get_deployments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#batch_get_deployments)
        """

    def batch_get_on_premises_instances(
        self, **kwargs: Unpack[BatchGetOnPremisesInstancesInputTypeDef]
    ) -> BatchGetOnPremisesInstancesOutputTypeDef:
        """
        Gets information about one or more on-premises instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/batch_get_on_premises_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#batch_get_on_premises_instances)
        """

    def continue_deployment(
        self, **kwargs: Unpack[ContinueDeploymentInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        For a blue/green deployment, starts the process of rerouting traffic from
        instances in the original environment to instances in the replacement
        environment without waiting for a specified wait time to elapse.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/continue_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#continue_deployment)
        """

    def create_application(
        self, **kwargs: Unpack[CreateApplicationInputTypeDef]
    ) -> CreateApplicationOutputTypeDef:
        """
        Creates an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/create_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#create_application)
        """

    def create_deployment(
        self, **kwargs: Unpack[CreateDeploymentInputTypeDef]
    ) -> CreateDeploymentOutputTypeDef:
        """
        Deploys an application revision through the specified deployment group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/create_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#create_deployment)
        """

    def create_deployment_config(
        self, **kwargs: Unpack[CreateDeploymentConfigInputTypeDef]
    ) -> CreateDeploymentConfigOutputTypeDef:
        """
        Creates a deployment configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/create_deployment_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#create_deployment_config)
        """

    def create_deployment_group(
        self, **kwargs: Unpack[CreateDeploymentGroupInputTypeDef]
    ) -> CreateDeploymentGroupOutputTypeDef:
        """
        Creates a deployment group to which application revisions are deployed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/create_deployment_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#create_deployment_group)
        """

    def delete_application(
        self, **kwargs: Unpack[DeleteApplicationInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/delete_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#delete_application)
        """

    def delete_deployment_config(
        self, **kwargs: Unpack[DeleteDeploymentConfigInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a deployment configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/delete_deployment_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#delete_deployment_config)
        """

    def delete_deployment_group(
        self, **kwargs: Unpack[DeleteDeploymentGroupInputTypeDef]
    ) -> DeleteDeploymentGroupOutputTypeDef:
        """
        Deletes a deployment group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/delete_deployment_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#delete_deployment_group)
        """

    def delete_git_hub_account_token(
        self, **kwargs: Unpack[DeleteGitHubAccountTokenInputTypeDef]
    ) -> DeleteGitHubAccountTokenOutputTypeDef:
        """
        Deletes a GitHub account connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/delete_git_hub_account_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#delete_git_hub_account_token)
        """

    def delete_resources_by_external_id(
        self, **kwargs: Unpack[DeleteResourcesByExternalIdInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes resources linked to an external ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/delete_resources_by_external_id.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#delete_resources_by_external_id)
        """

    def deregister_on_premises_instance(
        self, **kwargs: Unpack[DeregisterOnPremisesInstanceInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deregisters an on-premises instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/deregister_on_premises_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#deregister_on_premises_instance)
        """

    def get_application(
        self, **kwargs: Unpack[GetApplicationInputTypeDef]
    ) -> GetApplicationOutputTypeDef:
        """
        Gets information about an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/get_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#get_application)
        """

    def get_application_revision(
        self, **kwargs: Unpack[GetApplicationRevisionInputTypeDef]
    ) -> GetApplicationRevisionOutputTypeDef:
        """
        Gets information about an application revision.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/get_application_revision.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#get_application_revision)
        """

    def get_deployment(
        self, **kwargs: Unpack[GetDeploymentInputTypeDef]
    ) -> GetDeploymentOutputTypeDef:
        """
        Gets information about a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/get_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#get_deployment)
        """

    def get_deployment_config(
        self, **kwargs: Unpack[GetDeploymentConfigInputTypeDef]
    ) -> GetDeploymentConfigOutputTypeDef:
        """
        Gets information about a deployment configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/get_deployment_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#get_deployment_config)
        """

    def get_deployment_group(
        self, **kwargs: Unpack[GetDeploymentGroupInputTypeDef]
    ) -> GetDeploymentGroupOutputTypeDef:
        """
        Gets information about a deployment group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/get_deployment_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#get_deployment_group)
        """

    def get_deployment_instance(
        self, **kwargs: Unpack[GetDeploymentInstanceInputTypeDef]
    ) -> GetDeploymentInstanceOutputTypeDef:
        """
        Gets information about an instance as part of a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/get_deployment_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#get_deployment_instance)
        """

    def get_deployment_target(
        self, **kwargs: Unpack[GetDeploymentTargetInputTypeDef]
    ) -> GetDeploymentTargetOutputTypeDef:
        """
        Returns information about a deployment target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/get_deployment_target.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#get_deployment_target)
        """

    def get_on_premises_instance(
        self, **kwargs: Unpack[GetOnPremisesInstanceInputTypeDef]
    ) -> GetOnPremisesInstanceOutputTypeDef:
        """
        Gets information about an on-premises instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/get_on_premises_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#get_on_premises_instance)
        """

    def list_application_revisions(
        self, **kwargs: Unpack[ListApplicationRevisionsInputTypeDef]
    ) -> ListApplicationRevisionsOutputTypeDef:
        """
        Lists information about revisions for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/list_application_revisions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#list_application_revisions)
        """

    def list_applications(
        self, **kwargs: Unpack[ListApplicationsInputTypeDef]
    ) -> ListApplicationsOutputTypeDef:
        """
        Lists the applications registered with the user or Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/list_applications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#list_applications)
        """

    def list_deployment_configs(
        self, **kwargs: Unpack[ListDeploymentConfigsInputTypeDef]
    ) -> ListDeploymentConfigsOutputTypeDef:
        """
        Lists the deployment configurations with the user or Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/list_deployment_configs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#list_deployment_configs)
        """

    def list_deployment_groups(
        self, **kwargs: Unpack[ListDeploymentGroupsInputTypeDef]
    ) -> ListDeploymentGroupsOutputTypeDef:
        """
        Lists the deployment groups for an application registered with the Amazon Web
        Services user or Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/list_deployment_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#list_deployment_groups)
        """

    def list_deployment_instances(
        self, **kwargs: Unpack[ListDeploymentInstancesInputTypeDef]
    ) -> ListDeploymentInstancesOutputTypeDef:
        """
        The newer <code>BatchGetDeploymentTargets</code> should be used instead because
        it works with all compute types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/list_deployment_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#list_deployment_instances)
        """

    def list_deployment_targets(
        self, **kwargs: Unpack[ListDeploymentTargetsInputTypeDef]
    ) -> ListDeploymentTargetsOutputTypeDef:
        """
        Returns an array of target IDs that are associated a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/list_deployment_targets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#list_deployment_targets)
        """

    def list_deployments(
        self, **kwargs: Unpack[ListDeploymentsInputTypeDef]
    ) -> ListDeploymentsOutputTypeDef:
        """
        Lists the deployments in a deployment group for an application registered with
        the user or Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/list_deployments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#list_deployments)
        """

    def list_git_hub_account_token_names(
        self, **kwargs: Unpack[ListGitHubAccountTokenNamesInputTypeDef]
    ) -> ListGitHubAccountTokenNamesOutputTypeDef:
        """
        Lists the names of stored connections to GitHub accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/list_git_hub_account_token_names.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#list_git_hub_account_token_names)
        """

    def list_on_premises_instances(
        self, **kwargs: Unpack[ListOnPremisesInstancesInputTypeDef]
    ) -> ListOnPremisesInstancesOutputTypeDef:
        """
        Gets a list of names for one or more on-premises instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/list_on_premises_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#list_on_premises_instances)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Returns a list of tags for the resource identified by a specified Amazon
        Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#list_tags_for_resource)
        """

    def put_lifecycle_event_hook_execution_status(
        self, **kwargs: Unpack[PutLifecycleEventHookExecutionStatusInputTypeDef]
    ) -> PutLifecycleEventHookExecutionStatusOutputTypeDef:
        """
        Sets the result of a Lambda validation function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/put_lifecycle_event_hook_execution_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#put_lifecycle_event_hook_execution_status)
        """

    def register_application_revision(
        self, **kwargs: Unpack[RegisterApplicationRevisionInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Registers with CodeDeploy a revision for the specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/register_application_revision.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#register_application_revision)
        """

    def register_on_premises_instance(
        self, **kwargs: Unpack[RegisterOnPremisesInstanceInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Registers an on-premises instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/register_on_premises_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#register_on_premises_instance)
        """

    def remove_tags_from_on_premises_instances(
        self, **kwargs: Unpack[RemoveTagsFromOnPremisesInstancesInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes one or more tags from one or more on-premises instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/remove_tags_from_on_premises_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#remove_tags_from_on_premises_instances)
        """

    def skip_wait_time_for_instance_termination(
        self, **kwargs: Unpack[SkipWaitTimeForInstanceTerminationInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        In a blue/green deployment, overrides any specified wait time and starts
        terminating instances immediately after the traffic routing is complete.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/skip_wait_time_for_instance_termination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#skip_wait_time_for_instance_termination)
        """

    def stop_deployment(
        self, **kwargs: Unpack[StopDeploymentInputTypeDef]
    ) -> StopDeploymentOutputTypeDef:
        """
        Attempts to stop an ongoing deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/stop_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#stop_deployment)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Associates the list of tags in the input <code>Tags</code> parameter with the
        resource identified by the <code>ResourceArn</code> input parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Disassociates a resource from a list of tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#untag_resource)
        """

    def update_application(
        self, **kwargs: Unpack[UpdateApplicationInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Changes the name of an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/update_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#update_application)
        """

    def update_deployment_group(
        self, **kwargs: Unpack[UpdateDeploymentGroupInputTypeDef]
    ) -> UpdateDeploymentGroupOutputTypeDef:
        """
        Changes information about a deployment group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/update_deployment_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#update_deployment_group)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_application_revisions"]
    ) -> ListApplicationRevisionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_deployment_configs"]
    ) -> ListDeploymentConfigsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_deployment_groups"]
    ) -> ListDeploymentGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_deployment_instances"]
    ) -> ListDeploymentInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_deployment_targets"]
    ) -> ListDeploymentTargetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_deployments"]
    ) -> ListDeploymentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_git_hub_account_token_names"]
    ) -> ListGitHubAccountTokenNamesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_on_premises_instances"]
    ) -> ListOnPremisesInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#get_paginator)
        """

    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["deployment_successful"]
    ) -> DeploymentSuccessfulWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/client/#get_waiter)
        """
