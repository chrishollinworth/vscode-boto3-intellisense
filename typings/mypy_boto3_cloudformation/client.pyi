"""
Type annotations for cloudformation service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cloudformation.client import CloudFormationClient

    session = Session()
    client: CloudFormationClient = session.client("cloudformation")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeAccountLimitsPaginator,
    DescribeChangeSetPaginator,
    DescribeStackEventsPaginator,
    DescribeStacksPaginator,
    ListChangeSetsPaginator,
    ListExportsPaginator,
    ListGeneratedTemplatesPaginator,
    ListImportsPaginator,
    ListResourceScanRelatedResourcesPaginator,
    ListResourceScanResourcesPaginator,
    ListResourceScansPaginator,
    ListStackInstancesPaginator,
    ListStackRefactorActionsPaginator,
    ListStackRefactorsPaginator,
    ListStackResourcesPaginator,
    ListStackSetOperationResultsPaginator,
    ListStackSetOperationsPaginator,
    ListStackSetsPaginator,
    ListStacksPaginator,
    ListTypesPaginator,
)
from .type_defs import (
    ActivateTypeInputTypeDef,
    ActivateTypeOutputTypeDef,
    BatchDescribeTypeConfigurationsInputTypeDef,
    BatchDescribeTypeConfigurationsOutputTypeDef,
    CancelUpdateStackInputTypeDef,
    ContinueUpdateRollbackInputTypeDef,
    CreateChangeSetInputTypeDef,
    CreateChangeSetOutputTypeDef,
    CreateGeneratedTemplateInputTypeDef,
    CreateGeneratedTemplateOutputTypeDef,
    CreateStackInputTypeDef,
    CreateStackInstancesInputTypeDef,
    CreateStackInstancesOutputTypeDef,
    CreateStackOutputTypeDef,
    CreateStackRefactorInputTypeDef,
    CreateStackRefactorOutputTypeDef,
    CreateStackSetInputTypeDef,
    CreateStackSetOutputTypeDef,
    DeactivateTypeInputTypeDef,
    DeleteChangeSetInputTypeDef,
    DeleteGeneratedTemplateInputTypeDef,
    DeleteStackInputTypeDef,
    DeleteStackInstancesInputTypeDef,
    DeleteStackInstancesOutputTypeDef,
    DeleteStackSetInputTypeDef,
    DeregisterTypeInputTypeDef,
    DescribeAccountLimitsInputTypeDef,
    DescribeAccountLimitsOutputTypeDef,
    DescribeChangeSetHooksInputTypeDef,
    DescribeChangeSetHooksOutputTypeDef,
    DescribeChangeSetInputTypeDef,
    DescribeChangeSetOutputTypeDef,
    DescribeGeneratedTemplateInputTypeDef,
    DescribeGeneratedTemplateOutputTypeDef,
    DescribeOrganizationsAccessInputTypeDef,
    DescribeOrganizationsAccessOutputTypeDef,
    DescribePublisherInputTypeDef,
    DescribePublisherOutputTypeDef,
    DescribeResourceScanInputTypeDef,
    DescribeResourceScanOutputTypeDef,
    DescribeStackDriftDetectionStatusInputTypeDef,
    DescribeStackDriftDetectionStatusOutputTypeDef,
    DescribeStackEventsInputTypeDef,
    DescribeStackEventsOutputTypeDef,
    DescribeStackInstanceInputTypeDef,
    DescribeStackInstanceOutputTypeDef,
    DescribeStackRefactorInputTypeDef,
    DescribeStackRefactorOutputTypeDef,
    DescribeStackResourceDriftsInputTypeDef,
    DescribeStackResourceDriftsOutputTypeDef,
    DescribeStackResourceInputTypeDef,
    DescribeStackResourceOutputTypeDef,
    DescribeStackResourcesInputTypeDef,
    DescribeStackResourcesOutputTypeDef,
    DescribeStackSetInputTypeDef,
    DescribeStackSetOperationInputTypeDef,
    DescribeStackSetOperationOutputTypeDef,
    DescribeStackSetOutputTypeDef,
    DescribeStacksInputTypeDef,
    DescribeStacksOutputTypeDef,
    DescribeTypeInputTypeDef,
    DescribeTypeOutputTypeDef,
    DescribeTypeRegistrationInputTypeDef,
    DescribeTypeRegistrationOutputTypeDef,
    DetectStackDriftInputTypeDef,
    DetectStackDriftOutputTypeDef,
    DetectStackResourceDriftInputTypeDef,
    DetectStackResourceDriftOutputTypeDef,
    DetectStackSetDriftInputTypeDef,
    DetectStackSetDriftOutputTypeDef,
    EmptyResponseMetadataTypeDef,
    EstimateTemplateCostInputTypeDef,
    EstimateTemplateCostOutputTypeDef,
    ExecuteChangeSetInputTypeDef,
    ExecuteStackRefactorInputTypeDef,
    GetGeneratedTemplateInputTypeDef,
    GetGeneratedTemplateOutputTypeDef,
    GetStackPolicyInputTypeDef,
    GetStackPolicyOutputTypeDef,
    GetTemplateInputTypeDef,
    GetTemplateOutputTypeDef,
    GetTemplateSummaryInputTypeDef,
    GetTemplateSummaryOutputTypeDef,
    ImportStacksToStackSetInputTypeDef,
    ImportStacksToStackSetOutputTypeDef,
    ListChangeSetsInputTypeDef,
    ListChangeSetsOutputTypeDef,
    ListExportsInputTypeDef,
    ListExportsOutputTypeDef,
    ListGeneratedTemplatesInputTypeDef,
    ListGeneratedTemplatesOutputTypeDef,
    ListHookResultsInputTypeDef,
    ListHookResultsOutputTypeDef,
    ListImportsInputTypeDef,
    ListImportsOutputTypeDef,
    ListResourceScanRelatedResourcesInputTypeDef,
    ListResourceScanRelatedResourcesOutputTypeDef,
    ListResourceScanResourcesInputTypeDef,
    ListResourceScanResourcesOutputTypeDef,
    ListResourceScansInputTypeDef,
    ListResourceScansOutputTypeDef,
    ListStackInstanceResourceDriftsInputTypeDef,
    ListStackInstanceResourceDriftsOutputTypeDef,
    ListStackInstancesInputTypeDef,
    ListStackInstancesOutputTypeDef,
    ListStackRefactorActionsInputTypeDef,
    ListStackRefactorActionsOutputTypeDef,
    ListStackRefactorsInputTypeDef,
    ListStackRefactorsOutputTypeDef,
    ListStackResourcesInputTypeDef,
    ListStackResourcesOutputTypeDef,
    ListStackSetAutoDeploymentTargetsInputTypeDef,
    ListStackSetAutoDeploymentTargetsOutputTypeDef,
    ListStackSetOperationResultsInputTypeDef,
    ListStackSetOperationResultsOutputTypeDef,
    ListStackSetOperationsInputTypeDef,
    ListStackSetOperationsOutputTypeDef,
    ListStackSetsInputTypeDef,
    ListStackSetsOutputTypeDef,
    ListStacksInputTypeDef,
    ListStacksOutputTypeDef,
    ListTypeRegistrationsInputTypeDef,
    ListTypeRegistrationsOutputTypeDef,
    ListTypesInputTypeDef,
    ListTypesOutputTypeDef,
    ListTypeVersionsInputTypeDef,
    ListTypeVersionsOutputTypeDef,
    PublishTypeInputTypeDef,
    PublishTypeOutputTypeDef,
    RecordHandlerProgressInputTypeDef,
    RegisterPublisherInputTypeDef,
    RegisterPublisherOutputTypeDef,
    RegisterTypeInputTypeDef,
    RegisterTypeOutputTypeDef,
    RollbackStackInputTypeDef,
    RollbackStackOutputTypeDef,
    SetStackPolicyInputTypeDef,
    SetTypeConfigurationInputTypeDef,
    SetTypeConfigurationOutputTypeDef,
    SetTypeDefaultVersionInputTypeDef,
    SignalResourceInputTypeDef,
    StartResourceScanInputTypeDef,
    StartResourceScanOutputTypeDef,
    StopStackSetOperationInputTypeDef,
    TestTypeInputTypeDef,
    TestTypeOutputTypeDef,
    UpdateGeneratedTemplateInputTypeDef,
    UpdateGeneratedTemplateOutputTypeDef,
    UpdateStackInputTypeDef,
    UpdateStackInstancesInputTypeDef,
    UpdateStackInstancesOutputTypeDef,
    UpdateStackOutputTypeDef,
    UpdateStackSetInputTypeDef,
    UpdateStackSetOutputTypeDef,
    UpdateTerminationProtectionInputTypeDef,
    UpdateTerminationProtectionOutputTypeDef,
    ValidateTemplateInputTypeDef,
    ValidateTemplateOutputTypeDef,
)
from .waiter import (
    ChangeSetCreateCompleteWaiter,
    StackCreateCompleteWaiter,
    StackDeleteCompleteWaiter,
    StackExistsWaiter,
    StackImportCompleteWaiter,
    StackRefactorCreateCompleteWaiter,
    StackRefactorExecuteCompleteWaiter,
    StackRollbackCompleteWaiter,
    StackUpdateCompleteWaiter,
    TypeRegistrationCompleteWaiter,
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

__all__ = ("CloudFormationClient",)

class Exceptions(BaseClientExceptions):
    AlreadyExistsException: Type[BotocoreClientError]
    CFNRegistryException: Type[BotocoreClientError]
    ChangeSetNotFoundException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentResourcesLimitExceededException: Type[BotocoreClientError]
    CreatedButModifiedException: Type[BotocoreClientError]
    GeneratedTemplateNotFoundException: Type[BotocoreClientError]
    HookResultNotFoundException: Type[BotocoreClientError]
    InsufficientCapabilitiesException: Type[BotocoreClientError]
    InvalidChangeSetStatusException: Type[BotocoreClientError]
    InvalidOperationException: Type[BotocoreClientError]
    InvalidStateTransitionException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NameAlreadyExistsException: Type[BotocoreClientError]
    OperationIdAlreadyExistsException: Type[BotocoreClientError]
    OperationInProgressException: Type[BotocoreClientError]
    OperationNotFoundException: Type[BotocoreClientError]
    OperationStatusCheckFailedException: Type[BotocoreClientError]
    ResourceScanInProgressException: Type[BotocoreClientError]
    ResourceScanLimitExceededException: Type[BotocoreClientError]
    ResourceScanNotFoundException: Type[BotocoreClientError]
    StackInstanceNotFoundException: Type[BotocoreClientError]
    StackNotFoundException: Type[BotocoreClientError]
    StackRefactorNotFoundException: Type[BotocoreClientError]
    StackSetNotEmptyException: Type[BotocoreClientError]
    StackSetNotFoundException: Type[BotocoreClientError]
    StaleRequestException: Type[BotocoreClientError]
    TokenAlreadyExistsException: Type[BotocoreClientError]
    TypeConfigurationNotFoundException: Type[BotocoreClientError]
    TypeNotFoundException: Type[BotocoreClientError]

class CloudFormationClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudFormationClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#generate_presigned_url)
        """

    def activate_organizations_access(self) -> Dict[str, Any]:
        """
        Activate trusted access with Organizations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/activate_organizations_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#activate_organizations_access)
        """

    def activate_type(
        self, **kwargs: Unpack[ActivateTypeInputTypeDef]
    ) -> ActivateTypeOutputTypeDef:
        """
        Activates a public third-party extension, making it available for use in stack
        templates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/activate_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#activate_type)
        """

    def batch_describe_type_configurations(
        self, **kwargs: Unpack[BatchDescribeTypeConfigurationsInputTypeDef]
    ) -> BatchDescribeTypeConfigurationsOutputTypeDef:
        """
        Returns configuration data for the specified CloudFormation extensions, from
        the CloudFormation registry for the account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/batch_describe_type_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#batch_describe_type_configurations)
        """

    def cancel_update_stack(
        self, **kwargs: Unpack[CancelUpdateStackInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Cancels an update on the specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/cancel_update_stack.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#cancel_update_stack)
        """

    def continue_update_rollback(
        self, **kwargs: Unpack[ContinueUpdateRollbackInputTypeDef]
    ) -> Dict[str, Any]:
        """
        For a specified stack that's in the <code>UPDATE_ROLLBACK_FAILED</code> state,
        continues rolling it back to the <code>UPDATE_ROLLBACK_COMPLETE</code> state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/continue_update_rollback.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#continue_update_rollback)
        """

    def create_change_set(
        self, **kwargs: Unpack[CreateChangeSetInputTypeDef]
    ) -> CreateChangeSetOutputTypeDef:
        """
        Creates a list of changes that will be applied to a stack so that you can
        review the changes before executing them.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/create_change_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#create_change_set)
        """

    def create_generated_template(
        self, **kwargs: Unpack[CreateGeneratedTemplateInputTypeDef]
    ) -> CreateGeneratedTemplateOutputTypeDef:
        """
        Creates a template from existing resources that are not already managed with
        CloudFormation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/create_generated_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#create_generated_template)
        """

    def create_stack(self, **kwargs: Unpack[CreateStackInputTypeDef]) -> CreateStackOutputTypeDef:
        """
        Creates a stack as specified in the template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/create_stack.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#create_stack)
        """

    def create_stack_instances(
        self, **kwargs: Unpack[CreateStackInstancesInputTypeDef]
    ) -> CreateStackInstancesOutputTypeDef:
        """
        Creates stack instances for the specified accounts, within the specified Amazon
        Web Services Regions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/create_stack_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#create_stack_instances)
        """

    def create_stack_refactor(
        self, **kwargs: Unpack[CreateStackRefactorInputTypeDef]
    ) -> CreateStackRefactorOutputTypeDef:
        """
        Creates a refactor across multiple stacks, with the list of stacks and
        resources that are affected.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/create_stack_refactor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#create_stack_refactor)
        """

    def create_stack_set(
        self, **kwargs: Unpack[CreateStackSetInputTypeDef]
    ) -> CreateStackSetOutputTypeDef:
        """
        Creates a stack set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/create_stack_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#create_stack_set)
        """

    def deactivate_organizations_access(self) -> Dict[str, Any]:
        """
        Deactivates trusted access with Organizations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/deactivate_organizations_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#deactivate_organizations_access)
        """

    def deactivate_type(self, **kwargs: Unpack[DeactivateTypeInputTypeDef]) -> Dict[str, Any]:
        """
        Deactivates a public extension that was previously activated in this account
        and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/deactivate_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#deactivate_type)
        """

    def delete_change_set(self, **kwargs: Unpack[DeleteChangeSetInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified change set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/delete_change_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#delete_change_set)
        """

    def delete_generated_template(
        self, **kwargs: Unpack[DeleteGeneratedTemplateInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deleted a generated template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/delete_generated_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#delete_generated_template)
        """

    def delete_stack(
        self, **kwargs: Unpack[DeleteStackInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/delete_stack.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#delete_stack)
        """

    def delete_stack_instances(
        self, **kwargs: Unpack[DeleteStackInstancesInputTypeDef]
    ) -> DeleteStackInstancesOutputTypeDef:
        """
        Deletes stack instances for the specified accounts, in the specified Amazon Web
        Services Regions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/delete_stack_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#delete_stack_instances)
        """

    def delete_stack_set(self, **kwargs: Unpack[DeleteStackSetInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes a stack set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/delete_stack_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#delete_stack_set)
        """

    def deregister_type(self, **kwargs: Unpack[DeregisterTypeInputTypeDef]) -> Dict[str, Any]:
        """
        Marks an extension or extension version as <code>DEPRECATED</code> in the
        CloudFormation registry, removing it from active use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/deregister_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#deregister_type)
        """

    def describe_account_limits(
        self, **kwargs: Unpack[DescribeAccountLimitsInputTypeDef]
    ) -> DescribeAccountLimitsOutputTypeDef:
        """
        Retrieves your account's CloudFormation limits, such as the maximum number of
        stacks that you can create in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/describe_account_limits.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#describe_account_limits)
        """

    def describe_change_set(
        self, **kwargs: Unpack[DescribeChangeSetInputTypeDef]
    ) -> DescribeChangeSetOutputTypeDef:
        """
        Returns the inputs for the change set and a list of changes that CloudFormation
        will make if you execute the change set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/describe_change_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#describe_change_set)
        """

    def describe_change_set_hooks(
        self, **kwargs: Unpack[DescribeChangeSetHooksInputTypeDef]
    ) -> DescribeChangeSetHooksOutputTypeDef:
        """
        Returns hook-related information for the change set and a list of changes that
        CloudFormation makes when you run the change set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/describe_change_set_hooks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#describe_change_set_hooks)
        """

    def describe_generated_template(
        self, **kwargs: Unpack[DescribeGeneratedTemplateInputTypeDef]
    ) -> DescribeGeneratedTemplateOutputTypeDef:
        """
        Describes a generated template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/describe_generated_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#describe_generated_template)
        """

    def describe_organizations_access(
        self, **kwargs: Unpack[DescribeOrganizationsAccessInputTypeDef]
    ) -> DescribeOrganizationsAccessOutputTypeDef:
        """
        Retrieves information about the account's <code>OrganizationAccess</code>
        status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/describe_organizations_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#describe_organizations_access)
        """

    def describe_publisher(
        self, **kwargs: Unpack[DescribePublisherInputTypeDef]
    ) -> DescribePublisherOutputTypeDef:
        """
        Returns information about a CloudFormation extension publisher.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/describe_publisher.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#describe_publisher)
        """

    def describe_resource_scan(
        self, **kwargs: Unpack[DescribeResourceScanInputTypeDef]
    ) -> DescribeResourceScanOutputTypeDef:
        """
        Describes details of a resource scan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/describe_resource_scan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#describe_resource_scan)
        """

    def describe_stack_drift_detection_status(
        self, **kwargs: Unpack[DescribeStackDriftDetectionStatusInputTypeDef]
    ) -> DescribeStackDriftDetectionStatusOutputTypeDef:
        """
        Returns information about a stack drift detection operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/describe_stack_drift_detection_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#describe_stack_drift_detection_status)
        """

    def describe_stack_events(
        self, **kwargs: Unpack[DescribeStackEventsInputTypeDef]
    ) -> DescribeStackEventsOutputTypeDef:
        """
        Returns all stack related events for a specified stack in reverse chronological
        order.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/describe_stack_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#describe_stack_events)
        """

    def describe_stack_instance(
        self, **kwargs: Unpack[DescribeStackInstanceInputTypeDef]
    ) -> DescribeStackInstanceOutputTypeDef:
        """
        Returns the stack instance that's associated with the specified StackSet,
        Amazon Web Services account, and Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/describe_stack_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#describe_stack_instance)
        """

    def describe_stack_refactor(
        self, **kwargs: Unpack[DescribeStackRefactorInputTypeDef]
    ) -> DescribeStackRefactorOutputTypeDef:
        """
        Describes the stack refactor status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/describe_stack_refactor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#describe_stack_refactor)
        """

    def describe_stack_resource(
        self, **kwargs: Unpack[DescribeStackResourceInputTypeDef]
    ) -> DescribeStackResourceOutputTypeDef:
        """
        Returns a description of the specified resource in the specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/describe_stack_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#describe_stack_resource)
        """

    def describe_stack_resource_drifts(
        self, **kwargs: Unpack[DescribeStackResourceDriftsInputTypeDef]
    ) -> DescribeStackResourceDriftsOutputTypeDef:
        """
        Returns drift information for the resources that have been checked for drift in
        the specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/describe_stack_resource_drifts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#describe_stack_resource_drifts)
        """

    def describe_stack_resources(
        self, **kwargs: Unpack[DescribeStackResourcesInputTypeDef]
    ) -> DescribeStackResourcesOutputTypeDef:
        """
        Returns Amazon Web Services resource descriptions for running and deleted
        stacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/describe_stack_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#describe_stack_resources)
        """

    def describe_stack_set(
        self, **kwargs: Unpack[DescribeStackSetInputTypeDef]
    ) -> DescribeStackSetOutputTypeDef:
        """
        Returns the description of the specified StackSet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/describe_stack_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#describe_stack_set)
        """

    def describe_stack_set_operation(
        self, **kwargs: Unpack[DescribeStackSetOperationInputTypeDef]
    ) -> DescribeStackSetOperationOutputTypeDef:
        """
        Returns the description of the specified StackSet operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/describe_stack_set_operation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#describe_stack_set_operation)
        """

    def describe_stacks(
        self, **kwargs: Unpack[DescribeStacksInputTypeDef]
    ) -> DescribeStacksOutputTypeDef:
        """
        Returns the description for the specified stack; if no stack name was
        specified, then it returns the description for all the stacks created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/describe_stacks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#describe_stacks)
        """

    def describe_type(
        self, **kwargs: Unpack[DescribeTypeInputTypeDef]
    ) -> DescribeTypeOutputTypeDef:
        """
        Returns detailed information about an extension that has been registered.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/describe_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#describe_type)
        """

    def describe_type_registration(
        self, **kwargs: Unpack[DescribeTypeRegistrationInputTypeDef]
    ) -> DescribeTypeRegistrationOutputTypeDef:
        """
        Returns information about an extension's registration, including its current
        status and type and version identifiers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/describe_type_registration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#describe_type_registration)
        """

    def detect_stack_drift(
        self, **kwargs: Unpack[DetectStackDriftInputTypeDef]
    ) -> DetectStackDriftOutputTypeDef:
        """
        Detects whether a stack's actual configuration differs, or has <i>drifted</i>,
        from its expected configuration, as defined in the stack template and any
        values specified as template parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/detect_stack_drift.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#detect_stack_drift)
        """

    def detect_stack_resource_drift(
        self, **kwargs: Unpack[DetectStackResourceDriftInputTypeDef]
    ) -> DetectStackResourceDriftOutputTypeDef:
        """
        Returns information about whether a resource's actual configuration differs, or
        has <i>drifted</i>, from its expected configuration, as defined in the stack
        template and any values specified as template parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/detect_stack_resource_drift.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#detect_stack_resource_drift)
        """

    def detect_stack_set_drift(
        self, **kwargs: Unpack[DetectStackSetDriftInputTypeDef]
    ) -> DetectStackSetDriftOutputTypeDef:
        """
        Detect drift on a stack set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/detect_stack_set_drift.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#detect_stack_set_drift)
        """

    def estimate_template_cost(
        self, **kwargs: Unpack[EstimateTemplateCostInputTypeDef]
    ) -> EstimateTemplateCostOutputTypeDef:
        """
        Returns the estimated monthly cost of a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/estimate_template_cost.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#estimate_template_cost)
        """

    def execute_change_set(self, **kwargs: Unpack[ExecuteChangeSetInputTypeDef]) -> Dict[str, Any]:
        """
        Updates a stack using the input information that was provided when the
        specified change set was created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/execute_change_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#execute_change_set)
        """

    def execute_stack_refactor(
        self, **kwargs: Unpack[ExecuteStackRefactorInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Executes the stack refactor operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/execute_stack_refactor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#execute_stack_refactor)
        """

    def get_generated_template(
        self, **kwargs: Unpack[GetGeneratedTemplateInputTypeDef]
    ) -> GetGeneratedTemplateOutputTypeDef:
        """
        Retrieves a generated template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_generated_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_generated_template)
        """

    def get_stack_policy(
        self, **kwargs: Unpack[GetStackPolicyInputTypeDef]
    ) -> GetStackPolicyOutputTypeDef:
        """
        Returns the stack policy for a specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_stack_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_stack_policy)
        """

    def get_template(self, **kwargs: Unpack[GetTemplateInputTypeDef]) -> GetTemplateOutputTypeDef:
        """
        Returns the template body for a specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_template)
        """

    def get_template_summary(
        self, **kwargs: Unpack[GetTemplateSummaryInputTypeDef]
    ) -> GetTemplateSummaryOutputTypeDef:
        """
        Returns information about a new or existing template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_template_summary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_template_summary)
        """

    def import_stacks_to_stack_set(
        self, **kwargs: Unpack[ImportStacksToStackSetInputTypeDef]
    ) -> ImportStacksToStackSetOutputTypeDef:
        """
        Import existing stacks into a new stack sets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/import_stacks_to_stack_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#import_stacks_to_stack_set)
        """

    def list_change_sets(
        self, **kwargs: Unpack[ListChangeSetsInputTypeDef]
    ) -> ListChangeSetsOutputTypeDef:
        """
        Returns the ID and status of each active change set for a stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/list_change_sets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#list_change_sets)
        """

    def list_exports(self, **kwargs: Unpack[ListExportsInputTypeDef]) -> ListExportsOutputTypeDef:
        """
        Lists all exported output values in the account and Region in which you call
        this action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/list_exports.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#list_exports)
        """

    def list_generated_templates(
        self, **kwargs: Unpack[ListGeneratedTemplatesInputTypeDef]
    ) -> ListGeneratedTemplatesOutputTypeDef:
        """
        Lists your generated templates in this Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/list_generated_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#list_generated_templates)
        """

    def list_hook_results(
        self, **kwargs: Unpack[ListHookResultsInputTypeDef]
    ) -> ListHookResultsOutputTypeDef:
        """
        Returns summaries of invoked Hooks when a change set or Cloud Control API
        operation target is provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/list_hook_results.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#list_hook_results)
        """

    def list_imports(self, **kwargs: Unpack[ListImportsInputTypeDef]) -> ListImportsOutputTypeDef:
        """
        Lists all stacks that are importing an exported output value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/list_imports.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#list_imports)
        """

    def list_resource_scan_related_resources(
        self, **kwargs: Unpack[ListResourceScanRelatedResourcesInputTypeDef]
    ) -> ListResourceScanRelatedResourcesOutputTypeDef:
        """
        Lists the related resources for a list of resources from a resource scan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/list_resource_scan_related_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#list_resource_scan_related_resources)
        """

    def list_resource_scan_resources(
        self, **kwargs: Unpack[ListResourceScanResourcesInputTypeDef]
    ) -> ListResourceScanResourcesOutputTypeDef:
        """
        Lists the resources from a resource scan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/list_resource_scan_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#list_resource_scan_resources)
        """

    def list_resource_scans(
        self, **kwargs: Unpack[ListResourceScansInputTypeDef]
    ) -> ListResourceScansOutputTypeDef:
        """
        List the resource scans from newest to oldest.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/list_resource_scans.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#list_resource_scans)
        """

    def list_stack_instance_resource_drifts(
        self, **kwargs: Unpack[ListStackInstanceResourceDriftsInputTypeDef]
    ) -> ListStackInstanceResourceDriftsOutputTypeDef:
        """
        Returns drift information for resources in a stack instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/list_stack_instance_resource_drifts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#list_stack_instance_resource_drifts)
        """

    def list_stack_instances(
        self, **kwargs: Unpack[ListStackInstancesInputTypeDef]
    ) -> ListStackInstancesOutputTypeDef:
        """
        Returns summary information about stack instances that are associated with the
        specified stack set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/list_stack_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#list_stack_instances)
        """

    def list_stack_refactor_actions(
        self, **kwargs: Unpack[ListStackRefactorActionsInputTypeDef]
    ) -> ListStackRefactorActionsOutputTypeDef:
        """
        Lists the stack refactor actions that will be taken after calling the
        <a>ExecuteStackRefactor</a> action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/list_stack_refactor_actions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#list_stack_refactor_actions)
        """

    def list_stack_refactors(
        self, **kwargs: Unpack[ListStackRefactorsInputTypeDef]
    ) -> ListStackRefactorsOutputTypeDef:
        """
        Lists all account stack refactor operations and their statuses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/list_stack_refactors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#list_stack_refactors)
        """

    def list_stack_resources(
        self, **kwargs: Unpack[ListStackResourcesInputTypeDef]
    ) -> ListStackResourcesOutputTypeDef:
        """
        Returns descriptions of all resources of the specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/list_stack_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#list_stack_resources)
        """

    def list_stack_set_auto_deployment_targets(
        self, **kwargs: Unpack[ListStackSetAutoDeploymentTargetsInputTypeDef]
    ) -> ListStackSetAutoDeploymentTargetsOutputTypeDef:
        """
        Returns summary information about deployment targets for a stack set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/list_stack_set_auto_deployment_targets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#list_stack_set_auto_deployment_targets)
        """

    def list_stack_set_operation_results(
        self, **kwargs: Unpack[ListStackSetOperationResultsInputTypeDef]
    ) -> ListStackSetOperationResultsOutputTypeDef:
        """
        Returns summary information about the results of a stack set operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/list_stack_set_operation_results.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#list_stack_set_operation_results)
        """

    def list_stack_set_operations(
        self, **kwargs: Unpack[ListStackSetOperationsInputTypeDef]
    ) -> ListStackSetOperationsOutputTypeDef:
        """
        Returns summary information about operations performed on a stack set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/list_stack_set_operations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#list_stack_set_operations)
        """

    def list_stack_sets(
        self, **kwargs: Unpack[ListStackSetsInputTypeDef]
    ) -> ListStackSetsOutputTypeDef:
        """
        Returns summary information about stack sets that are associated with the user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/list_stack_sets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#list_stack_sets)
        """

    def list_stacks(self, **kwargs: Unpack[ListStacksInputTypeDef]) -> ListStacksOutputTypeDef:
        """
        Returns the summary information for stacks whose status matches the specified
        <code>StackStatusFilter</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/list_stacks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#list_stacks)
        """

    def list_type_registrations(
        self, **kwargs: Unpack[ListTypeRegistrationsInputTypeDef]
    ) -> ListTypeRegistrationsOutputTypeDef:
        """
        Returns a list of registration tokens for the specified extension(s).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/list_type_registrations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#list_type_registrations)
        """

    def list_type_versions(
        self, **kwargs: Unpack[ListTypeVersionsInputTypeDef]
    ) -> ListTypeVersionsOutputTypeDef:
        """
        Returns summary information about the versions of an extension.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/list_type_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#list_type_versions)
        """

    def list_types(self, **kwargs: Unpack[ListTypesInputTypeDef]) -> ListTypesOutputTypeDef:
        """
        Returns summary information about extension that have been registered with
        CloudFormation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/list_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#list_types)
        """

    def publish_type(self, **kwargs: Unpack[PublishTypeInputTypeDef]) -> PublishTypeOutputTypeDef:
        """
        Publishes the specified extension to the CloudFormation registry as a public
        extension in this Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/publish_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#publish_type)
        """

    def record_handler_progress(
        self, **kwargs: Unpack[RecordHandlerProgressInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Reports progress of a resource handler to CloudFormation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/record_handler_progress.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#record_handler_progress)
        """

    def register_publisher(
        self, **kwargs: Unpack[RegisterPublisherInputTypeDef]
    ) -> RegisterPublisherOutputTypeDef:
        """
        Registers your account as a publisher of public extensions in the
        CloudFormation registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/register_publisher.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#register_publisher)
        """

    def register_type(
        self, **kwargs: Unpack[RegisterTypeInputTypeDef]
    ) -> RegisterTypeOutputTypeDef:
        """
        Registers an extension with the CloudFormation service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/register_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#register_type)
        """

    def rollback_stack(
        self, **kwargs: Unpack[RollbackStackInputTypeDef]
    ) -> RollbackStackOutputTypeDef:
        """
        When specifying <code>RollbackStack</code>, you preserve the state of
        previously provisioned resources when an operation fails.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/rollback_stack.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#rollback_stack)
        """

    def set_stack_policy(
        self, **kwargs: Unpack[SetStackPolicyInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Sets a stack policy for a specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/set_stack_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#set_stack_policy)
        """

    def set_type_configuration(
        self, **kwargs: Unpack[SetTypeConfigurationInputTypeDef]
    ) -> SetTypeConfigurationOutputTypeDef:
        """
        Specifies the configuration data for a registered CloudFormation extension, in
        the given account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/set_type_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#set_type_configuration)
        """

    def set_type_default_version(
        self, **kwargs: Unpack[SetTypeDefaultVersionInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Specify the default version of an extension.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/set_type_default_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#set_type_default_version)
        """

    def signal_resource(
        self, **kwargs: Unpack[SignalResourceInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Sends a signal to the specified resource with a success or failure status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/signal_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#signal_resource)
        """

    def start_resource_scan(
        self, **kwargs: Unpack[StartResourceScanInputTypeDef]
    ) -> StartResourceScanOutputTypeDef:
        """
        Starts a scan of the resources in this account in this Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/start_resource_scan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#start_resource_scan)
        """

    def stop_stack_set_operation(
        self, **kwargs: Unpack[StopStackSetOperationInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Stops an in-progress operation on a stack set and its associated stack
        instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/stop_stack_set_operation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#stop_stack_set_operation)
        """

    def test_type(self, **kwargs: Unpack[TestTypeInputTypeDef]) -> TestTypeOutputTypeDef:
        """
        Tests a registered extension to make sure it meets all necessary requirements
        for being published in the CloudFormation registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/test_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#test_type)
        """

    def update_generated_template(
        self, **kwargs: Unpack[UpdateGeneratedTemplateInputTypeDef]
    ) -> UpdateGeneratedTemplateOutputTypeDef:
        """
        Updates a generated template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/update_generated_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#update_generated_template)
        """

    def update_stack(self, **kwargs: Unpack[UpdateStackInputTypeDef]) -> UpdateStackOutputTypeDef:
        """
        Updates a stack as specified in the template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/update_stack.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#update_stack)
        """

    def update_stack_instances(
        self, **kwargs: Unpack[UpdateStackInstancesInputTypeDef]
    ) -> UpdateStackInstancesOutputTypeDef:
        """
        Updates the parameter values for stack instances for the specified accounts,
        within the specified Amazon Web Services Regions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/update_stack_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#update_stack_instances)
        """

    def update_stack_set(
        self, **kwargs: Unpack[UpdateStackSetInputTypeDef]
    ) -> UpdateStackSetOutputTypeDef:
        """
        Updates the stack set and associated stack instances in the specified accounts
        and Amazon Web Services Regions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/update_stack_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#update_stack_set)
        """

    def update_termination_protection(
        self, **kwargs: Unpack[UpdateTerminationProtectionInputTypeDef]
    ) -> UpdateTerminationProtectionOutputTypeDef:
        """
        Updates termination protection for the specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/update_termination_protection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#update_termination_protection)
        """

    def validate_template(
        self, **kwargs: Unpack[ValidateTemplateInputTypeDef]
    ) -> ValidateTemplateOutputTypeDef:
        """
        Validates a specified template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/validate_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#validate_template)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_account_limits"]
    ) -> DescribeAccountLimitsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_change_set"]
    ) -> DescribeChangeSetPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_stack_events"]
    ) -> DescribeStackEventsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_stacks"]
    ) -> DescribeStacksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_change_sets"]
    ) -> ListChangeSetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_exports"]
    ) -> ListExportsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_generated_templates"]
    ) -> ListGeneratedTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_imports"]
    ) -> ListImportsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resource_scan_related_resources"]
    ) -> ListResourceScanRelatedResourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resource_scan_resources"]
    ) -> ListResourceScanResourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resource_scans"]
    ) -> ListResourceScansPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_stack_instances"]
    ) -> ListStackInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_stack_refactor_actions"]
    ) -> ListStackRefactorActionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_stack_refactors"]
    ) -> ListStackRefactorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_stack_resources"]
    ) -> ListStackResourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_stack_set_operation_results"]
    ) -> ListStackSetOperationResultsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_stack_set_operations"]
    ) -> ListStackSetOperationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_stack_sets"]
    ) -> ListStackSetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_stacks"]
    ) -> ListStacksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_types"]
    ) -> ListTypesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["change_set_create_complete"]
    ) -> ChangeSetCreateCompleteWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["stack_create_complete"]
    ) -> StackCreateCompleteWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["stack_delete_complete"]
    ) -> StackDeleteCompleteWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["stack_exists"]
    ) -> StackExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["stack_import_complete"]
    ) -> StackImportCompleteWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["stack_refactor_create_complete"]
    ) -> StackRefactorCreateCompleteWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["stack_refactor_execute_complete"]
    ) -> StackRefactorExecuteCompleteWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["stack_rollback_complete"]
    ) -> StackRollbackCompleteWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["stack_update_complete"]
    ) -> StackUpdateCompleteWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["type_registration_complete"]
    ) -> TypeRegistrationCompleteWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client/#get_waiter)
        """
