"""
Type annotations for cloudformation service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudformation import CloudFormationClient

    client: CloudFormationClient = boto3.client("cloudformation")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    CallAsType,
    CapabilityType,
    ChangeSetTypeType,
    DeprecatedStatusType,
    HandlerErrorCodeType,
    OnFailureType,
    OperationStatusType,
    PermissionModelsType,
    ProvisioningTypeType,
    RegistrationStatusType,
    RegistryTypeType,
    ResourceSignalStatusType,
    StackResourceDriftStatusType,
    StackSetStatusType,
    StackStatusType,
    TemplateStageType,
    ThirdPartyTypeType,
    VersionBumpType,
    VisibilityType,
)
from .paginator import (
    DescribeAccountLimitsPaginator,
    DescribeChangeSetPaginator,
    DescribeStackEventsPaginator,
    DescribeStacksPaginator,
    ListChangeSetsPaginator,
    ListExportsPaginator,
    ListImportsPaginator,
    ListStackInstancesPaginator,
    ListStackResourcesPaginator,
    ListStackSetOperationResultsPaginator,
    ListStackSetOperationsPaginator,
    ListStackSetsPaginator,
    ListStacksPaginator,
    ListTypesPaginator,
)
from .type_defs import (
    ActivateTypeOutputTypeDef,
    AutoDeploymentTypeDef,
    BatchDescribeTypeConfigurationsOutputTypeDef,
    CreateChangeSetOutputTypeDef,
    CreateStackInstancesOutputTypeDef,
    CreateStackOutputTypeDef,
    CreateStackSetOutputTypeDef,
    DeleteStackInstancesOutputTypeDef,
    DeploymentTargetsTypeDef,
    DescribeAccountLimitsOutputTypeDef,
    DescribeChangeSetOutputTypeDef,
    DescribePublisherOutputTypeDef,
    DescribeStackDriftDetectionStatusOutputTypeDef,
    DescribeStackEventsOutputTypeDef,
    DescribeStackInstanceOutputTypeDef,
    DescribeStackResourceDriftsOutputTypeDef,
    DescribeStackResourceOutputTypeDef,
    DescribeStackResourcesOutputTypeDef,
    DescribeStackSetOperationOutputTypeDef,
    DescribeStackSetOutputTypeDef,
    DescribeStacksOutputTypeDef,
    DescribeTypeOutputTypeDef,
    DescribeTypeRegistrationOutputTypeDef,
    DetectStackDriftOutputTypeDef,
    DetectStackResourceDriftOutputTypeDef,
    DetectStackSetDriftOutputTypeDef,
    EstimateTemplateCostOutputTypeDef,
    GetStackPolicyOutputTypeDef,
    GetTemplateOutputTypeDef,
    GetTemplateSummaryOutputTypeDef,
    ImportStacksToStackSetOutputTypeDef,
    ListChangeSetsOutputTypeDef,
    ListExportsOutputTypeDef,
    ListImportsOutputTypeDef,
    ListStackInstancesOutputTypeDef,
    ListStackResourcesOutputTypeDef,
    ListStackSetOperationResultsOutputTypeDef,
    ListStackSetOperationsOutputTypeDef,
    ListStackSetsOutputTypeDef,
    ListStacksOutputTypeDef,
    ListTypeRegistrationsOutputTypeDef,
    ListTypesOutputTypeDef,
    ListTypeVersionsOutputTypeDef,
    LoggingConfigTypeDef,
    ManagedExecutionTypeDef,
    ParameterTypeDef,
    PublishTypeOutputTypeDef,
    RegisterPublisherOutputTypeDef,
    RegisterTypeOutputTypeDef,
    ResourceToImportTypeDef,
    RollbackConfigurationTypeDef,
    RollbackStackOutputTypeDef,
    SetTypeConfigurationOutputTypeDef,
    StackInstanceFilterTypeDef,
    StackSetOperationPreferencesTypeDef,
    TagTypeDef,
    TestTypeOutputTypeDef,
    TypeConfigurationIdentifierTypeDef,
    TypeFiltersTypeDef,
    UpdateStackInstancesOutputTypeDef,
    UpdateStackOutputTypeDef,
    UpdateStackSetOutputTypeDef,
    UpdateTerminationProtectionOutputTypeDef,
    ValidateTemplateOutputTypeDef,
)
from .waiter import (
    ChangeSetCreateCompleteWaiter,
    StackCreateCompleteWaiter,
    StackDeleteCompleteWaiter,
    StackExistsWaiter,
    StackImportCompleteWaiter,
    StackRollbackCompleteWaiter,
    StackUpdateCompleteWaiter,
    TypeRegistrationCompleteWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CloudFormationClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AlreadyExistsException: Type[BotocoreClientError]
    CFNRegistryException: Type[BotocoreClientError]
    ChangeSetNotFoundException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    CreatedButModifiedException: Type[BotocoreClientError]
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
    StackInstanceNotFoundException: Type[BotocoreClientError]
    StackNotFoundException: Type[BotocoreClientError]
    StackSetNotEmptyException: Type[BotocoreClientError]
    StackSetNotFoundException: Type[BotocoreClientError]
    StaleRequestException: Type[BotocoreClientError]
    TokenAlreadyExistsException: Type[BotocoreClientError]
    TypeConfigurationNotFoundException: Type[BotocoreClientError]
    TypeNotFoundException: Type[BotocoreClientError]

class CloudFormationClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        CloudFormationClient exceptions.
        """
    def activate_type(
        self,
        *,
        Type: ThirdPartyTypeType = None,
        PublicTypeArn: str = None,
        PublisherId: str = None,
        TypeName: str = None,
        TypeNameAlias: str = None,
        AutoUpdate: bool = None,
        LoggingConfig: "LoggingConfigTypeDef" = None,
        ExecutionRoleArn: str = None,
        VersionBump: VersionBumpType = None,
        MajorVersion: int = None
    ) -> ActivateTypeOutputTypeDef:
        """
        Activates a public third-party extension, making it available for use in stack
        templates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.activate_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#activate_type)
        """
    def batch_describe_type_configurations(
        self, *, TypeConfigurationIdentifiers: List["TypeConfigurationIdentifierTypeDef"]
    ) -> BatchDescribeTypeConfigurationsOutputTypeDef:
        """
        Returns configuration data for the specified CloudFormation extensions, from the
        CloudFormation registry for the account and region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.batch_describe_type_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#batch_describe_type_configurations)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#can_paginate)
        """
    def cancel_update_stack(self, *, StackName: str, ClientRequestToken: str = None) -> None:
        """
        Cancels an update on the specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.cancel_update_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#cancel_update_stack)
        """
    def continue_update_rollback(
        self,
        *,
        StackName: str,
        RoleARN: str = None,
        ResourcesToSkip: List[str] = None,
        ClientRequestToken: str = None
    ) -> Dict[str, Any]:
        """
        For a specified stack that is in the `UPDATE_ROLLBACK_FAILED` state, continues
        rolling it back to the `UPDATE_ROLLBACK_COMPLETE` state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.continue_update_rollback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#continue_update_rollback)
        """
    def create_change_set(
        self,
        *,
        StackName: str,
        ChangeSetName: str,
        TemplateBody: str = None,
        TemplateURL: str = None,
        UsePreviousTemplate: bool = None,
        Parameters: List["ParameterTypeDef"] = None,
        Capabilities: List[CapabilityType] = None,
        ResourceTypes: List[str] = None,
        RoleARN: str = None,
        RollbackConfiguration: "RollbackConfigurationTypeDef" = None,
        NotificationARNs: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        ClientToken: str = None,
        Description: str = None,
        ChangeSetType: ChangeSetTypeType = None,
        ResourcesToImport: List["ResourceToImportTypeDef"] = None,
        IncludeNestedStacks: bool = None
    ) -> CreateChangeSetOutputTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.create_change_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#create_change_set)
        """
    def create_stack(
        self,
        *,
        StackName: str,
        TemplateBody: str = None,
        TemplateURL: str = None,
        Parameters: List["ParameterTypeDef"] = None,
        DisableRollback: bool = None,
        RollbackConfiguration: "RollbackConfigurationTypeDef" = None,
        TimeoutInMinutes: int = None,
        NotificationARNs: List[str] = None,
        Capabilities: List[CapabilityType] = None,
        ResourceTypes: List[str] = None,
        RoleARN: str = None,
        OnFailure: OnFailureType = None,
        StackPolicyBody: str = None,
        StackPolicyURL: str = None,
        Tags: List["TagTypeDef"] = None,
        ClientRequestToken: str = None,
        EnableTerminationProtection: bool = None
    ) -> CreateStackOutputTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.create_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#create_stack)
        """
    def create_stack_instances(
        self,
        *,
        StackSetName: str,
        Regions: List[str],
        Accounts: List[str] = None,
        DeploymentTargets: "DeploymentTargetsTypeDef" = None,
        ParameterOverrides: List["ParameterTypeDef"] = None,
        OperationPreferences: "StackSetOperationPreferencesTypeDef" = None,
        OperationId: str = None,
        CallAs: CallAsType = None
    ) -> CreateStackInstancesOutputTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.create_stack_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#create_stack_instances)
        """
    def create_stack_set(
        self,
        *,
        StackSetName: str,
        Description: str = None,
        TemplateBody: str = None,
        TemplateURL: str = None,
        StackId: str = None,
        Parameters: List["ParameterTypeDef"] = None,
        Capabilities: List[CapabilityType] = None,
        Tags: List["TagTypeDef"] = None,
        AdministrationRoleARN: str = None,
        ExecutionRoleName: str = None,
        PermissionModel: PermissionModelsType = None,
        AutoDeployment: "AutoDeploymentTypeDef" = None,
        CallAs: CallAsType = None,
        ClientRequestToken: str = None,
        ManagedExecution: "ManagedExecutionTypeDef" = None
    ) -> CreateStackSetOutputTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.create_stack_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#create_stack_set)
        """
    def deactivate_type(
        self, *, TypeName: str = None, Type: ThirdPartyTypeType = None, Arn: str = None
    ) -> Dict[str, Any]:
        """
        Deactivates a public extension that was previously activated in this account and
        region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.deactivate_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#deactivate_type)
        """
    def delete_change_set(self, *, ChangeSetName: str, StackName: str = None) -> Dict[str, Any]:
        """
        Deletes the specified change set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.delete_change_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#delete_change_set)
        """
    def delete_stack(
        self,
        *,
        StackName: str,
        RetainResources: List[str] = None,
        RoleARN: str = None,
        ClientRequestToken: str = None
    ) -> None:
        """
        Deletes a specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.delete_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#delete_stack)
        """
    def delete_stack_instances(
        self,
        *,
        StackSetName: str,
        Regions: List[str],
        RetainStacks: bool,
        Accounts: List[str] = None,
        DeploymentTargets: "DeploymentTargetsTypeDef" = None,
        OperationPreferences: "StackSetOperationPreferencesTypeDef" = None,
        OperationId: str = None,
        CallAs: CallAsType = None
    ) -> DeleteStackInstancesOutputTypeDef:
        """
        Deletes stack instances for the specified accounts, in the specified Regions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.delete_stack_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#delete_stack_instances)
        """
    def delete_stack_set(self, *, StackSetName: str, CallAs: CallAsType = None) -> Dict[str, Any]:
        """
        Deletes a stack set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.delete_stack_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#delete_stack_set)
        """
    def deregister_type(
        self,
        *,
        Arn: str = None,
        Type: RegistryTypeType = None,
        TypeName: str = None,
        VersionId: str = None
    ) -> Dict[str, Any]:
        """
        Marks an extension or extension version as `DEPRECATED` in the CloudFormation
        registry, removing it from active use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.deregister_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#deregister_type)
        """
    def describe_account_limits(
        self, *, NextToken: str = None
    ) -> DescribeAccountLimitsOutputTypeDef:
        """
        Retrieves your account's CloudFormation limits, such as the maximum number of
        stacks that you can create in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.describe_account_limits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#describe_account_limits)
        """
    def describe_change_set(
        self, *, ChangeSetName: str, StackName: str = None, NextToken: str = None
    ) -> DescribeChangeSetOutputTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.describe_change_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#describe_change_set)
        """
    def describe_publisher(self, *, PublisherId: str = None) -> DescribePublisherOutputTypeDef:
        """
        Returns information about a CloudFormation extension publisher.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.describe_publisher)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#describe_publisher)
        """
    def describe_stack_drift_detection_status(
        self, *, StackDriftDetectionId: str
    ) -> DescribeStackDriftDetectionStatusOutputTypeDef:
        """
        Returns information about a stack drift detection operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_drift_detection_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#describe_stack_drift_detection_status)
        """
    def describe_stack_events(
        self, *, StackName: str = None, NextToken: str = None
    ) -> DescribeStackEventsOutputTypeDef:
        """
        Returns all stack related events for a specified stack in reverse chronological
        order.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#describe_stack_events)
        """
    def describe_stack_instance(
        self,
        *,
        StackSetName: str,
        StackInstanceAccount: str,
        StackInstanceRegion: str,
        CallAs: CallAsType = None
    ) -> DescribeStackInstanceOutputTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#describe_stack_instance)
        """
    def describe_stack_resource(
        self, *, StackName: str, LogicalResourceId: str
    ) -> DescribeStackResourceOutputTypeDef:
        """
        Returns a description of the specified resource in the specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#describe_stack_resource)
        """
    def describe_stack_resource_drifts(
        self,
        *,
        StackName: str,
        StackResourceDriftStatusFilters: List[StackResourceDriftStatusType] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeStackResourceDriftsOutputTypeDef:
        """
        Returns drift information for the resources that have been checked for drift in
        the specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_resource_drifts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#describe_stack_resource_drifts)
        """
    def describe_stack_resources(
        self,
        *,
        StackName: str = None,
        LogicalResourceId: str = None,
        PhysicalResourceId: str = None
    ) -> DescribeStackResourcesOutputTypeDef:
        """
        Returns Amazon Web Services resource descriptions for running and deleted
        stacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#describe_stack_resources)
        """
    def describe_stack_set(
        self, *, StackSetName: str, CallAs: CallAsType = None
    ) -> DescribeStackSetOutputTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#describe_stack_set)
        """
    def describe_stack_set_operation(
        self, *, StackSetName: str, OperationId: str, CallAs: CallAsType = None
    ) -> DescribeStackSetOperationOutputTypeDef:
        """
        Returns the description of the specified stack set operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_set_operation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#describe_stack_set_operation)
        """
    def describe_stacks(
        self, *, StackName: str = None, NextToken: str = None
    ) -> DescribeStacksOutputTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.describe_stacks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#describe_stacks)
        """
    def describe_type(
        self,
        *,
        Type: RegistryTypeType = None,
        TypeName: str = None,
        Arn: str = None,
        VersionId: str = None,
        PublisherId: str = None,
        PublicVersionNumber: str = None
    ) -> DescribeTypeOutputTypeDef:
        """
        Returns detailed information about an extension that has been registered.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.describe_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#describe_type)
        """
    def describe_type_registration(
        self, *, RegistrationToken: str
    ) -> DescribeTypeRegistrationOutputTypeDef:
        """
        Returns information about an extension's registration, including its current
        status and type and version identifiers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.describe_type_registration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#describe_type_registration)
        """
    def detect_stack_drift(
        self, *, StackName: str, LogicalResourceIds: List[str] = None
    ) -> DetectStackDriftOutputTypeDef:
        """
        Detects whether a stack's actual configuration differs, or has *drifted* , from
        it's expected configuration, as defined in the stack template and any values
        specified as template parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.detect_stack_drift)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#detect_stack_drift)
        """
    def detect_stack_resource_drift(
        self, *, StackName: str, LogicalResourceId: str
    ) -> DetectStackResourceDriftOutputTypeDef:
        """
        Returns information about whether a resource's actual configuration differs, or
        has *drifted* , from it's expected configuration, as defined in the stack
        template and any values specified as template parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.detect_stack_resource_drift)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#detect_stack_resource_drift)
        """
    def detect_stack_set_drift(
        self,
        *,
        StackSetName: str,
        OperationPreferences: "StackSetOperationPreferencesTypeDef" = None,
        OperationId: str = None,
        CallAs: CallAsType = None
    ) -> DetectStackSetDriftOutputTypeDef:
        """
        Detect drift on a stack set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.detect_stack_set_drift)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#detect_stack_set_drift)
        """
    def estimate_template_cost(
        self,
        *,
        TemplateBody: str = None,
        TemplateURL: str = None,
        Parameters: List["ParameterTypeDef"] = None
    ) -> EstimateTemplateCostOutputTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.estimate_template_cost)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#estimate_template_cost)
        """
    def execute_change_set(
        self,
        *,
        ChangeSetName: str,
        StackName: str = None,
        ClientRequestToken: str = None,
        DisableRollback: bool = None
    ) -> Dict[str, Any]:
        """
        Updates a stack using the input information that was provided when the specified
        change set was created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.execute_change_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#execute_change_set)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#generate_presigned_url)
        """
    def get_stack_policy(self, *, StackName: str) -> GetStackPolicyOutputTypeDef:
        """
        Returns the stack policy for a specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.get_stack_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#get_stack_policy)
        """
    def get_template(
        self,
        *,
        StackName: str = None,
        ChangeSetName: str = None,
        TemplateStage: TemplateStageType = None
    ) -> GetTemplateOutputTypeDef:
        """
        Returns the template body for a specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.get_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#get_template)
        """
    def get_template_summary(
        self,
        *,
        TemplateBody: str = None,
        TemplateURL: str = None,
        StackName: str = None,
        StackSetName: str = None,
        CallAs: CallAsType = None
    ) -> GetTemplateSummaryOutputTypeDef:
        """
        Returns information about a new or existing template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.get_template_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#get_template_summary)
        """
    def import_stacks_to_stack_set(
        self,
        *,
        StackSetName: str,
        StackIds: List[str] = None,
        StackIdsUrl: str = None,
        OrganizationalUnitIds: List[str] = None,
        OperationPreferences: "StackSetOperationPreferencesTypeDef" = None,
        OperationId: str = None,
        CallAs: CallAsType = None
    ) -> ImportStacksToStackSetOutputTypeDef:
        """
        Use the stack import operations for self-managed or service-managed StackSets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.import_stacks_to_stack_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#import_stacks_to_stack_set)
        """
    def list_change_sets(
        self, *, StackName: str, NextToken: str = None
    ) -> ListChangeSetsOutputTypeDef:
        """
        Returns the ID and status of each active change set for a stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.list_change_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#list_change_sets)
        """
    def list_exports(self, *, NextToken: str = None) -> ListExportsOutputTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.list_exports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#list_exports)
        """
    def list_imports(self, *, ExportName: str, NextToken: str = None) -> ListImportsOutputTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.list_imports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#list_imports)
        """
    def list_stack_instances(
        self,
        *,
        StackSetName: str,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["StackInstanceFilterTypeDef"] = None,
        StackInstanceAccount: str = None,
        StackInstanceRegion: str = None,
        CallAs: CallAsType = None
    ) -> ListStackInstancesOutputTypeDef:
        """
        Returns summary information about stack instances that are associated with the
        specified stack set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.list_stack_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#list_stack_instances)
        """
    def list_stack_resources(
        self, *, StackName: str, NextToken: str = None
    ) -> ListStackResourcesOutputTypeDef:
        """
        Returns descriptions of all resources of the specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.list_stack_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#list_stack_resources)
        """
    def list_stack_set_operation_results(
        self,
        *,
        StackSetName: str,
        OperationId: str,
        NextToken: str = None,
        MaxResults: int = None,
        CallAs: CallAsType = None
    ) -> ListStackSetOperationResultsOutputTypeDef:
        """
        Returns summary information about the results of a stack set operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.list_stack_set_operation_results)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#list_stack_set_operation_results)
        """
    def list_stack_set_operations(
        self,
        *,
        StackSetName: str,
        NextToken: str = None,
        MaxResults: int = None,
        CallAs: CallAsType = None
    ) -> ListStackSetOperationsOutputTypeDef:
        """
        Returns summary information about operations performed on a stack set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.list_stack_set_operations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#list_stack_set_operations)
        """
    def list_stack_sets(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Status: StackSetStatusType = None,
        CallAs: CallAsType = None
    ) -> ListStackSetsOutputTypeDef:
        """
        Returns summary information about stack sets that are associated with the user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.list_stack_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#list_stack_sets)
        """
    def list_stacks(
        self, *, NextToken: str = None, StackStatusFilter: List[StackStatusType] = None
    ) -> ListStacksOutputTypeDef:
        """
        Returns the summary information for stacks whose status matches the specified
        StackStatusFilter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.list_stacks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#list_stacks)
        """
    def list_type_registrations(
        self,
        *,
        Type: RegistryTypeType = None,
        TypeName: str = None,
        TypeArn: str = None,
        RegistrationStatusFilter: RegistrationStatusType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListTypeRegistrationsOutputTypeDef:
        """
        Returns a list of registration tokens for the specified extension(s).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.list_type_registrations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#list_type_registrations)
        """
    def list_type_versions(
        self,
        *,
        Type: RegistryTypeType = None,
        TypeName: str = None,
        Arn: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        DeprecatedStatus: DeprecatedStatusType = None,
        PublisherId: str = None
    ) -> ListTypeVersionsOutputTypeDef:
        """
        Returns summary information about the versions of an extension.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.list_type_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#list_type_versions)
        """
    def list_types(
        self,
        *,
        Visibility: VisibilityType = None,
        ProvisioningType: ProvisioningTypeType = None,
        DeprecatedStatus: DeprecatedStatusType = None,
        Type: RegistryTypeType = None,
        Filters: "TypeFiltersTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListTypesOutputTypeDef:
        """
        Returns summary information about extension that have been registered with
        CloudFormation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.list_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#list_types)
        """
    def publish_type(
        self,
        *,
        Type: ThirdPartyTypeType = None,
        Arn: str = None,
        TypeName: str = None,
        PublicVersionNumber: str = None
    ) -> PublishTypeOutputTypeDef:
        """
        Publishes the specified extension to the CloudFormation registry as a public
        extension in this region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.publish_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#publish_type)
        """
    def record_handler_progress(
        self,
        *,
        BearerToken: str,
        OperationStatus: OperationStatusType,
        CurrentOperationStatus: OperationStatusType = None,
        StatusMessage: str = None,
        ErrorCode: HandlerErrorCodeType = None,
        ResourceModel: str = None,
        ClientRequestToken: str = None
    ) -> Dict[str, Any]:
        """
        Reports progress of a resource handler to CloudFormation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.record_handler_progress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#record_handler_progress)
        """
    def register_publisher(
        self, *, AcceptTermsAndConditions: bool = None, ConnectionArn: str = None
    ) -> RegisterPublisherOutputTypeDef:
        """
        Registers your account as a publisher of public extensions in the CloudFormation
        registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.register_publisher)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#register_publisher)
        """
    def register_type(
        self,
        *,
        TypeName: str,
        SchemaHandlerPackage: str,
        Type: RegistryTypeType = None,
        LoggingConfig: "LoggingConfigTypeDef" = None,
        ExecutionRoleArn: str = None,
        ClientRequestToken: str = None
    ) -> RegisterTypeOutputTypeDef:
        """
        Registers an extension with the CloudFormation service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.register_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#register_type)
        """
    def rollback_stack(
        self, *, StackName: str, RoleARN: str = None, ClientRequestToken: str = None
    ) -> RollbackStackOutputTypeDef:
        """
        When specifying `RollbackStack` , you preserve the state of previously
        provisioned resources when an operation fails.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.rollback_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#rollback_stack)
        """
    def set_stack_policy(
        self, *, StackName: str, StackPolicyBody: str = None, StackPolicyURL: str = None
    ) -> None:
        """
        Sets a stack policy for a specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.set_stack_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#set_stack_policy)
        """
    def set_type_configuration(
        self,
        *,
        Configuration: str,
        TypeArn: str = None,
        ConfigurationAlias: str = None,
        TypeName: str = None,
        Type: ThirdPartyTypeType = None
    ) -> SetTypeConfigurationOutputTypeDef:
        """
        Specifies the configuration data for a registered CloudFormation extension, in
        the given account and region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.set_type_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#set_type_configuration)
        """
    def set_type_default_version(
        self,
        *,
        Arn: str = None,
        Type: RegistryTypeType = None,
        TypeName: str = None,
        VersionId: str = None
    ) -> Dict[str, Any]:
        """
        Specify the default version of an extension.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.set_type_default_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#set_type_default_version)
        """
    def signal_resource(
        self,
        *,
        StackName: str,
        LogicalResourceId: str,
        UniqueId: str,
        Status: ResourceSignalStatusType
    ) -> None:
        """
        Sends a signal to the specified resource with a success or failure status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.signal_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#signal_resource)
        """
    def stop_stack_set_operation(
        self, *, StackSetName: str, OperationId: str, CallAs: CallAsType = None
    ) -> Dict[str, Any]:
        """
        Stops an in-progress operation on a stack set and its associated stack
        instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.stop_stack_set_operation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#stop_stack_set_operation)
        """
    def test_type(
        self,
        *,
        Arn: str = None,
        Type: ThirdPartyTypeType = None,
        TypeName: str = None,
        VersionId: str = None,
        LogDeliveryBucket: str = None
    ) -> TestTypeOutputTypeDef:
        """
        Tests a registered extension to make sure it meets all necessary requirements
        for being published in the CloudFormation registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.test_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#test_type)
        """
    def update_stack(
        self,
        *,
        StackName: str,
        TemplateBody: str = None,
        TemplateURL: str = None,
        UsePreviousTemplate: bool = None,
        StackPolicyDuringUpdateBody: str = None,
        StackPolicyDuringUpdateURL: str = None,
        Parameters: List["ParameterTypeDef"] = None,
        Capabilities: List[CapabilityType] = None,
        ResourceTypes: List[str] = None,
        RoleARN: str = None,
        RollbackConfiguration: "RollbackConfigurationTypeDef" = None,
        StackPolicyBody: str = None,
        StackPolicyURL: str = None,
        NotificationARNs: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        DisableRollback: bool = None,
        ClientRequestToken: str = None
    ) -> UpdateStackOutputTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.update_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#update_stack)
        """
    def update_stack_instances(
        self,
        *,
        StackSetName: str,
        Regions: List[str],
        Accounts: List[str] = None,
        DeploymentTargets: "DeploymentTargetsTypeDef" = None,
        ParameterOverrides: List["ParameterTypeDef"] = None,
        OperationPreferences: "StackSetOperationPreferencesTypeDef" = None,
        OperationId: str = None,
        CallAs: CallAsType = None
    ) -> UpdateStackInstancesOutputTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.update_stack_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#update_stack_instances)
        """
    def update_stack_set(
        self,
        *,
        StackSetName: str,
        Description: str = None,
        TemplateBody: str = None,
        TemplateURL: str = None,
        UsePreviousTemplate: bool = None,
        Parameters: List["ParameterTypeDef"] = None,
        Capabilities: List[CapabilityType] = None,
        Tags: List["TagTypeDef"] = None,
        OperationPreferences: "StackSetOperationPreferencesTypeDef" = None,
        AdministrationRoleARN: str = None,
        ExecutionRoleName: str = None,
        DeploymentTargets: "DeploymentTargetsTypeDef" = None,
        PermissionModel: PermissionModelsType = None,
        AutoDeployment: "AutoDeploymentTypeDef" = None,
        OperationId: str = None,
        Accounts: List[str] = None,
        Regions: List[str] = None,
        CallAs: CallAsType = None,
        ManagedExecution: "ManagedExecutionTypeDef" = None
    ) -> UpdateStackSetOutputTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.update_stack_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#update_stack_set)
        """
    def update_termination_protection(
        self, *, EnableTerminationProtection: bool, StackName: str
    ) -> UpdateTerminationProtectionOutputTypeDef:
        """
        Updates termination protection for the specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.update_termination_protection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#update_termination_protection)
        """
    def validate_template(
        self, *, TemplateBody: str = None, TemplateURL: str = None
    ) -> ValidateTemplateOutputTypeDef:
        """
        Validates a specified template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Client.validate_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/client.html#validate_template)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_account_limits"]
    ) -> DescribeAccountLimitsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeAccountLimits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#describeaccountlimitspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_change_set"]
    ) -> DescribeChangeSetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeChangeSet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#describechangesetpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_stack_events"]
    ) -> DescribeStackEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeStackEvents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#describestackeventspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["describe_stacks"]) -> DescribeStacksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeStacks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#describestackspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_change_sets"]) -> ListChangeSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Paginator.ListChangeSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#listchangesetspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_exports"]) -> ListExportsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Paginator.ListExports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#listexportspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_imports"]) -> ListImportsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Paginator.ListImports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#listimportspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_stack_instances"]
    ) -> ListStackInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#liststackinstancespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_stack_resources"]
    ) -> ListStackResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackResources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#liststackresourcespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_stack_set_operation_results"]
    ) -> ListStackSetOperationResultsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSetOperationResults)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#liststacksetoperationresultspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_stack_set_operations"]
    ) -> ListStackSetOperationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSetOperations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#liststacksetoperationspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_stack_sets"]) -> ListStackSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#liststacksetspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_stacks"]) -> ListStacksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Paginator.ListStacks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#liststackspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_types"]) -> ListTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Paginator.ListTypes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#listtypespaginator)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["change_set_create_complete"]
    ) -> ChangeSetCreateCompleteWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Waiter.ChangeSetCreateComplete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html#changesetcreatecompletewaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["stack_create_complete"]
    ) -> StackCreateCompleteWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Waiter.StackCreateComplete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html#stackcreatecompletewaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["stack_delete_complete"]
    ) -> StackDeleteCompleteWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Waiter.StackDeleteComplete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html#stackdeletecompletewaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["stack_exists"]) -> StackExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Waiter.StackExists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html#stackexistswaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["stack_import_complete"]
    ) -> StackImportCompleteWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Waiter.StackImportComplete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html#stackimportcompletewaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["stack_rollback_complete"]
    ) -> StackRollbackCompleteWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Waiter.StackRollbackComplete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html#stackrollbackcompletewaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["stack_update_complete"]
    ) -> StackUpdateCompleteWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Waiter.StackUpdateComplete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html#stackupdatecompletewaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["type_registration_complete"]
    ) -> TypeRegistrationCompleteWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudformation.html#CloudFormation.Waiter.TypeRegistrationComplete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/waiters.html#typeregistrationcompletewaiter)
        """
