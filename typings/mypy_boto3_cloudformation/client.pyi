# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for cloudformation service client

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudformation import CloudFormationClient

    client: CloudFormationClient = boto3.client("cloudformation")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_cloudformation.paginator import (
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
)
from mypy_boto3_cloudformation.type_defs import (
    AutoDeploymentTypeDef,
    CreateChangeSetOutputTypeDef,
    CreateStackInstancesOutputTypeDef,
    CreateStackOutputTypeDef,
    CreateStackSetOutputTypeDef,
    DeleteStackInstancesOutputTypeDef,
    DeploymentTargetsTypeDef,
    DescribeAccountLimitsOutputTypeDef,
    DescribeChangeSetOutputTypeDef,
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
    ParameterTypeDef,
    RegisterTypeOutputTypeDef,
    ResourceToImportTypeDef,
    RollbackConfigurationTypeDef,
    StackInstanceFilterTypeDef,
    StackSetOperationPreferencesTypeDef,
    TagTypeDef,
    UpdateStackInstancesOutputTypeDef,
    UpdateStackOutputTypeDef,
    UpdateStackSetOutputTypeDef,
    UpdateTerminationProtectionOutputTypeDef,
    ValidateTemplateOutputTypeDef,
)
from mypy_boto3_cloudformation.waiter import (
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


class Exceptions:
    AlreadyExistsException: Type[Boto3ClientError]
    CFNRegistryException: Type[Boto3ClientError]
    ChangeSetNotFoundException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    CreatedButModifiedException: Type[Boto3ClientError]
    InsufficientCapabilitiesException: Type[Boto3ClientError]
    InvalidChangeSetStatusException: Type[Boto3ClientError]
    InvalidOperationException: Type[Boto3ClientError]
    InvalidStateTransitionException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    NameAlreadyExistsException: Type[Boto3ClientError]
    OperationIdAlreadyExistsException: Type[Boto3ClientError]
    OperationInProgressException: Type[Boto3ClientError]
    OperationNotFoundException: Type[Boto3ClientError]
    OperationStatusCheckFailedException: Type[Boto3ClientError]
    StackInstanceNotFoundException: Type[Boto3ClientError]
    StackSetNotEmptyException: Type[Boto3ClientError]
    StackSetNotFoundException: Type[Boto3ClientError]
    StaleRequestException: Type[Boto3ClientError]
    TokenAlreadyExistsException: Type[Boto3ClientError]
    TypeNotFoundException: Type[Boto3ClientError]


class CloudFormationClient:
    """
    [CloudFormation.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.can_paginate)
        """

    def cancel_update_stack(self, StackName: str, ClientRequestToken: str = None) -> None:
        """
        [Client.cancel_update_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.cancel_update_stack)
        """

    def continue_update_rollback(
        self,
        StackName: str,
        RoleARN: str = None,
        ResourcesToSkip: List[str] = None,
        ClientRequestToken: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.continue_update_rollback documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.continue_update_rollback)
        """

    def create_change_set(
        self,
        StackName: str,
        ChangeSetName: str,
        TemplateBody: str = None,
        TemplateURL: str = None,
        UsePreviousTemplate: bool = None,
        Parameters: List["ParameterTypeDef"] = None,
        Capabilities: List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ] = None,
        ResourceTypes: List[str] = None,
        RoleARN: str = None,
        RollbackConfiguration: "RollbackConfigurationTypeDef" = None,
        NotificationARNs: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        ClientToken: str = None,
        Description: str = None,
        ChangeSetType: Literal["CREATE", "UPDATE", "IMPORT"] = None,
        ResourcesToImport: List[ResourceToImportTypeDef] = None,
    ) -> CreateChangeSetOutputTypeDef:
        """
        [Client.create_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.create_change_set)
        """

    def create_stack(
        self,
        StackName: str,
        TemplateBody: str = None,
        TemplateURL: str = None,
        Parameters: List["ParameterTypeDef"] = None,
        DisableRollback: bool = None,
        RollbackConfiguration: "RollbackConfigurationTypeDef" = None,
        TimeoutInMinutes: int = None,
        NotificationARNs: List[str] = None,
        Capabilities: List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ] = None,
        ResourceTypes: List[str] = None,
        RoleARN: str = None,
        OnFailure: Literal["DO_NOTHING", "ROLLBACK", "DELETE"] = None,
        StackPolicyBody: str = None,
        StackPolicyURL: str = None,
        Tags: List["TagTypeDef"] = None,
        ClientRequestToken: str = None,
        EnableTerminationProtection: bool = None,
    ) -> CreateStackOutputTypeDef:
        """
        [Client.create_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.create_stack)
        """

    def create_stack_instances(
        self,
        StackSetName: str,
        Regions: List[str],
        Accounts: List[str] = None,
        DeploymentTargets: "DeploymentTargetsTypeDef" = None,
        ParameterOverrides: List["ParameterTypeDef"] = None,
        OperationPreferences: "StackSetOperationPreferencesTypeDef" = None,
        OperationId: str = None,
    ) -> CreateStackInstancesOutputTypeDef:
        """
        [Client.create_stack_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.create_stack_instances)
        """

    def create_stack_set(
        self,
        StackSetName: str,
        Description: str = None,
        TemplateBody: str = None,
        TemplateURL: str = None,
        Parameters: List["ParameterTypeDef"] = None,
        Capabilities: List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ] = None,
        Tags: List["TagTypeDef"] = None,
        AdministrationRoleARN: str = None,
        ExecutionRoleName: str = None,
        PermissionModel: Literal["SERVICE_MANAGED", "SELF_MANAGED"] = None,
        AutoDeployment: "AutoDeploymentTypeDef" = None,
        ClientRequestToken: str = None,
    ) -> CreateStackSetOutputTypeDef:
        """
        [Client.create_stack_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.create_stack_set)
        """

    def delete_change_set(self, ChangeSetName: str, StackName: str = None) -> Dict[str, Any]:
        """
        [Client.delete_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.delete_change_set)
        """

    def delete_stack(
        self,
        StackName: str,
        RetainResources: List[str] = None,
        RoleARN: str = None,
        ClientRequestToken: str = None,
    ) -> None:
        """
        [Client.delete_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.delete_stack)
        """

    def delete_stack_instances(
        self,
        StackSetName: str,
        Regions: List[str],
        RetainStacks: bool,
        Accounts: List[str] = None,
        DeploymentTargets: "DeploymentTargetsTypeDef" = None,
        OperationPreferences: "StackSetOperationPreferencesTypeDef" = None,
        OperationId: str = None,
    ) -> DeleteStackInstancesOutputTypeDef:
        """
        [Client.delete_stack_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.delete_stack_instances)
        """

    def delete_stack_set(self, StackSetName: str) -> Dict[str, Any]:
        """
        [Client.delete_stack_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.delete_stack_set)
        """

    def deregister_type(
        self,
        Arn: str = None,
        Type: Literal["RESOURCE"] = None,
        TypeName: str = None,
        VersionId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.deregister_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.deregister_type)
        """

    def describe_account_limits(self, NextToken: str = None) -> DescribeAccountLimitsOutputTypeDef:
        """
        [Client.describe_account_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.describe_account_limits)
        """

    def describe_change_set(
        self, ChangeSetName: str, StackName: str = None, NextToken: str = None
    ) -> DescribeChangeSetOutputTypeDef:
        """
        [Client.describe_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.describe_change_set)
        """

    def describe_stack_drift_detection_status(
        self, StackDriftDetectionId: str
    ) -> DescribeStackDriftDetectionStatusOutputTypeDef:
        """
        [Client.describe_stack_drift_detection_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_drift_detection_status)
        """

    def describe_stack_events(
        self, StackName: str = None, NextToken: str = None
    ) -> DescribeStackEventsOutputTypeDef:
        """
        [Client.describe_stack_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_events)
        """

    def describe_stack_instance(
        self, StackSetName: str, StackInstanceAccount: str, StackInstanceRegion: str
    ) -> DescribeStackInstanceOutputTypeDef:
        """
        [Client.describe_stack_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_instance)
        """

    def describe_stack_resource(
        self, StackName: str, LogicalResourceId: str
    ) -> DescribeStackResourceOutputTypeDef:
        """
        [Client.describe_stack_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_resource)
        """

    def describe_stack_resource_drifts(
        self,
        StackName: str,
        StackResourceDriftStatusFilters: List[
            Literal["IN_SYNC", "MODIFIED", "DELETED", "NOT_CHECKED"]
        ] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeStackResourceDriftsOutputTypeDef:
        """
        [Client.describe_stack_resource_drifts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_resource_drifts)
        """

    def describe_stack_resources(
        self, StackName: str = None, LogicalResourceId: str = None, PhysicalResourceId: str = None
    ) -> DescribeStackResourcesOutputTypeDef:
        """
        [Client.describe_stack_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_resources)
        """

    def describe_stack_set(self, StackSetName: str) -> DescribeStackSetOutputTypeDef:
        """
        [Client.describe_stack_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_set)
        """

    def describe_stack_set_operation(
        self, StackSetName: str, OperationId: str
    ) -> DescribeStackSetOperationOutputTypeDef:
        """
        [Client.describe_stack_set_operation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_set_operation)
        """

    def describe_stacks(
        self, StackName: str = None, NextToken: str = None
    ) -> DescribeStacksOutputTypeDef:
        """
        [Client.describe_stacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.describe_stacks)
        """

    def describe_type(
        self,
        Type: Literal["RESOURCE"] = None,
        TypeName: str = None,
        Arn: str = None,
        VersionId: str = None,
    ) -> DescribeTypeOutputTypeDef:
        """
        [Client.describe_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.describe_type)
        """

    def describe_type_registration(
        self, RegistrationToken: str
    ) -> DescribeTypeRegistrationOutputTypeDef:
        """
        [Client.describe_type_registration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.describe_type_registration)
        """

    def detect_stack_drift(
        self, StackName: str, LogicalResourceIds: List[str] = None
    ) -> DetectStackDriftOutputTypeDef:
        """
        [Client.detect_stack_drift documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.detect_stack_drift)
        """

    def detect_stack_resource_drift(
        self, StackName: str, LogicalResourceId: str
    ) -> DetectStackResourceDriftOutputTypeDef:
        """
        [Client.detect_stack_resource_drift documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.detect_stack_resource_drift)
        """

    def detect_stack_set_drift(
        self,
        StackSetName: str,
        OperationPreferences: "StackSetOperationPreferencesTypeDef" = None,
        OperationId: str = None,
    ) -> DetectStackSetDriftOutputTypeDef:
        """
        [Client.detect_stack_set_drift documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.detect_stack_set_drift)
        """

    def estimate_template_cost(
        self,
        TemplateBody: str = None,
        TemplateURL: str = None,
        Parameters: List["ParameterTypeDef"] = None,
    ) -> EstimateTemplateCostOutputTypeDef:
        """
        [Client.estimate_template_cost documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.estimate_template_cost)
        """

    def execute_change_set(
        self, ChangeSetName: str, StackName: str = None, ClientRequestToken: str = None
    ) -> Dict[str, Any]:
        """
        [Client.execute_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.execute_change_set)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.generate_presigned_url)
        """

    def get_stack_policy(self, StackName: str) -> GetStackPolicyOutputTypeDef:
        """
        [Client.get_stack_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.get_stack_policy)
        """

    def get_template(
        self,
        StackName: str = None,
        ChangeSetName: str = None,
        TemplateStage: Literal["Original", "Processed"] = None,
    ) -> GetTemplateOutputTypeDef:
        """
        [Client.get_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.get_template)
        """

    def get_template_summary(
        self,
        TemplateBody: str = None,
        TemplateURL: str = None,
        StackName: str = None,
        StackSetName: str = None,
    ) -> GetTemplateSummaryOutputTypeDef:
        """
        [Client.get_template_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.get_template_summary)
        """

    def list_change_sets(
        self, StackName: str, NextToken: str = None
    ) -> ListChangeSetsOutputTypeDef:
        """
        [Client.list_change_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.list_change_sets)
        """

    def list_exports(self, NextToken: str = None) -> ListExportsOutputTypeDef:
        """
        [Client.list_exports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.list_exports)
        """

    def list_imports(self, ExportName: str, NextToken: str = None) -> ListImportsOutputTypeDef:
        """
        [Client.list_imports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.list_imports)
        """

    def list_stack_instances(
        self,
        StackSetName: str,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List[StackInstanceFilterTypeDef] = None,
        StackInstanceAccount: str = None,
        StackInstanceRegion: str = None,
    ) -> ListStackInstancesOutputTypeDef:
        """
        [Client.list_stack_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.list_stack_instances)
        """

    def list_stack_resources(
        self, StackName: str, NextToken: str = None
    ) -> ListStackResourcesOutputTypeDef:
        """
        [Client.list_stack_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.list_stack_resources)
        """

    def list_stack_set_operation_results(
        self, StackSetName: str, OperationId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListStackSetOperationResultsOutputTypeDef:
        """
        [Client.list_stack_set_operation_results documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.list_stack_set_operation_results)
        """

    def list_stack_set_operations(
        self, StackSetName: str, NextToken: str = None, MaxResults: int = None
    ) -> ListStackSetOperationsOutputTypeDef:
        """
        [Client.list_stack_set_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.list_stack_set_operations)
        """

    def list_stack_sets(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Status: Literal["ACTIVE", "DELETED"] = None,
    ) -> ListStackSetsOutputTypeDef:
        """
        [Client.list_stack_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.list_stack_sets)
        """

    def list_stacks(
        self,
        NextToken: str = None,
        StackStatusFilter: List[
            Literal[
                "CREATE_IN_PROGRESS",
                "CREATE_FAILED",
                "CREATE_COMPLETE",
                "ROLLBACK_IN_PROGRESS",
                "ROLLBACK_FAILED",
                "ROLLBACK_COMPLETE",
                "DELETE_IN_PROGRESS",
                "DELETE_FAILED",
                "DELETE_COMPLETE",
                "UPDATE_IN_PROGRESS",
                "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS",
                "UPDATE_COMPLETE",
                "UPDATE_ROLLBACK_IN_PROGRESS",
                "UPDATE_ROLLBACK_FAILED",
                "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS",
                "UPDATE_ROLLBACK_COMPLETE",
                "REVIEW_IN_PROGRESS",
                "IMPORT_IN_PROGRESS",
                "IMPORT_COMPLETE",
                "IMPORT_ROLLBACK_IN_PROGRESS",
                "IMPORT_ROLLBACK_FAILED",
                "IMPORT_ROLLBACK_COMPLETE",
            ]
        ] = None,
    ) -> ListStacksOutputTypeDef:
        """
        [Client.list_stacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.list_stacks)
        """

    def list_type_registrations(
        self,
        Type: Literal["RESOURCE"] = None,
        TypeName: str = None,
        TypeArn: str = None,
        RegistrationStatusFilter: Literal["COMPLETE", "IN_PROGRESS", "FAILED"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListTypeRegistrationsOutputTypeDef:
        """
        [Client.list_type_registrations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.list_type_registrations)
        """

    def list_type_versions(
        self,
        Type: Literal["RESOURCE"] = None,
        TypeName: str = None,
        Arn: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        DeprecatedStatus: Literal["LIVE", "DEPRECATED"] = None,
    ) -> ListTypeVersionsOutputTypeDef:
        """
        [Client.list_type_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.list_type_versions)
        """

    def list_types(
        self,
        Visibility: Literal["PUBLIC", "PRIVATE"] = None,
        ProvisioningType: Literal["NON_PROVISIONABLE", "IMMUTABLE", "FULLY_MUTABLE"] = None,
        DeprecatedStatus: Literal["LIVE", "DEPRECATED"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListTypesOutputTypeDef:
        """
        [Client.list_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.list_types)
        """

    def record_handler_progress(
        self,
        BearerToken: str,
        OperationStatus: Literal["PENDING", "IN_PROGRESS", "SUCCESS", "FAILED"],
        CurrentOperationStatus: Literal["PENDING", "IN_PROGRESS", "SUCCESS", "FAILED"] = None,
        StatusMessage: str = None,
        ErrorCode: Literal[
            "NotUpdatable",
            "InvalidRequest",
            "AccessDenied",
            "InvalidCredentials",
            "AlreadyExists",
            "NotFound",
            "ResourceConflict",
            "Throttling",
            "ServiceLimitExceeded",
            "NotStabilized",
            "GeneralServiceException",
            "ServiceInternalError",
            "NetworkFailure",
            "InternalFailure",
        ] = None,
        ResourceModel: str = None,
        ClientRequestToken: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.record_handler_progress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.record_handler_progress)
        """

    def register_type(
        self,
        TypeName: str,
        SchemaHandlerPackage: str,
        Type: Literal["RESOURCE"] = None,
        LoggingConfig: "LoggingConfigTypeDef" = None,
        ExecutionRoleArn: str = None,
        ClientRequestToken: str = None,
    ) -> RegisterTypeOutputTypeDef:
        """
        [Client.register_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.register_type)
        """

    def set_stack_policy(
        self, StackName: str, StackPolicyBody: str = None, StackPolicyURL: str = None
    ) -> None:
        """
        [Client.set_stack_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.set_stack_policy)
        """

    def set_type_default_version(
        self,
        Arn: str = None,
        Type: Literal["RESOURCE"] = None,
        TypeName: str = None,
        VersionId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.set_type_default_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.set_type_default_version)
        """

    def signal_resource(
        self,
        StackName: str,
        LogicalResourceId: str,
        UniqueId: str,
        Status: Literal["SUCCESS", "FAILURE"],
    ) -> None:
        """
        [Client.signal_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.signal_resource)
        """

    def stop_stack_set_operation(self, StackSetName: str, OperationId: str) -> Dict[str, Any]:
        """
        [Client.stop_stack_set_operation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.stop_stack_set_operation)
        """

    def update_stack(
        self,
        StackName: str,
        TemplateBody: str = None,
        TemplateURL: str = None,
        UsePreviousTemplate: bool = None,
        StackPolicyDuringUpdateBody: str = None,
        StackPolicyDuringUpdateURL: str = None,
        Parameters: List["ParameterTypeDef"] = None,
        Capabilities: List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ] = None,
        ResourceTypes: List[str] = None,
        RoleARN: str = None,
        RollbackConfiguration: "RollbackConfigurationTypeDef" = None,
        StackPolicyBody: str = None,
        StackPolicyURL: str = None,
        NotificationARNs: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        ClientRequestToken: str = None,
    ) -> UpdateStackOutputTypeDef:
        """
        [Client.update_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.update_stack)
        """

    def update_stack_instances(
        self,
        StackSetName: str,
        Regions: List[str],
        Accounts: List[str] = None,
        DeploymentTargets: "DeploymentTargetsTypeDef" = None,
        ParameterOverrides: List["ParameterTypeDef"] = None,
        OperationPreferences: "StackSetOperationPreferencesTypeDef" = None,
        OperationId: str = None,
    ) -> UpdateStackInstancesOutputTypeDef:
        """
        [Client.update_stack_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.update_stack_instances)
        """

    def update_stack_set(
        self,
        StackSetName: str,
        Description: str = None,
        TemplateBody: str = None,
        TemplateURL: str = None,
        UsePreviousTemplate: bool = None,
        Parameters: List["ParameterTypeDef"] = None,
        Capabilities: List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ] = None,
        Tags: List["TagTypeDef"] = None,
        OperationPreferences: "StackSetOperationPreferencesTypeDef" = None,
        AdministrationRoleARN: str = None,
        ExecutionRoleName: str = None,
        DeploymentTargets: "DeploymentTargetsTypeDef" = None,
        PermissionModel: Literal["SERVICE_MANAGED", "SELF_MANAGED"] = None,
        AutoDeployment: "AutoDeploymentTypeDef" = None,
        OperationId: str = None,
        Accounts: List[str] = None,
        Regions: List[str] = None,
    ) -> UpdateStackSetOutputTypeDef:
        """
        [Client.update_stack_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.update_stack_set)
        """

    def update_termination_protection(
        self, EnableTerminationProtection: bool, StackName: str
    ) -> UpdateTerminationProtectionOutputTypeDef:
        """
        [Client.update_termination_protection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.update_termination_protection)
        """

    def validate_template(
        self, TemplateBody: str = None, TemplateURL: str = None
    ) -> ValidateTemplateOutputTypeDef:
        """
        [Client.validate_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Client.validate_template)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_account_limits"]
    ) -> DescribeAccountLimitsPaginator:
        """
        [Paginator.DescribeAccountLimits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeAccountLimits)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_change_set"]
    ) -> DescribeChangeSetPaginator:
        """
        [Paginator.DescribeChangeSet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeChangeSet)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_stack_events"]
    ) -> DescribeStackEventsPaginator:
        """
        [Paginator.DescribeStackEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeStackEvents)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_stacks"]) -> DescribeStacksPaginator:
        """
        [Paginator.DescribeStacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeStacks)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_change_sets"]) -> ListChangeSetsPaginator:
        """
        [Paginator.ListChangeSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Paginator.ListChangeSets)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_exports"]) -> ListExportsPaginator:
        """
        [Paginator.ListExports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Paginator.ListExports)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_imports"]) -> ListImportsPaginator:
        """
        [Paginator.ListImports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Paginator.ListImports)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_stack_instances"]
    ) -> ListStackInstancesPaginator:
        """
        [Paginator.ListStackInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_stack_resources"]
    ) -> ListStackResourcesPaginator:
        """
        [Paginator.ListStackResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackResources)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_stack_set_operation_results"]
    ) -> ListStackSetOperationResultsPaginator:
        """
        [Paginator.ListStackSetOperationResults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSetOperationResults)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_stack_set_operations"]
    ) -> ListStackSetOperationsPaginator:
        """
        [Paginator.ListStackSetOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSetOperations)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_stack_sets"]) -> ListStackSetsPaginator:
        """
        [Paginator.ListStackSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSets)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_stacks"]) -> ListStacksPaginator:
        """
        [Paginator.ListStacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Paginator.ListStacks)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass

    @overload
    def get_waiter(
        self, waiter_name: Literal["change_set_create_complete"]
    ) -> ChangeSetCreateCompleteWaiter:
        """
        [Waiter.ChangeSetCreateComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Waiter.ChangeSetCreateComplete)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["stack_create_complete"]
    ) -> StackCreateCompleteWaiter:
        """
        [Waiter.StackCreateComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Waiter.StackCreateComplete)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["stack_delete_complete"]
    ) -> StackDeleteCompleteWaiter:
        """
        [Waiter.StackDeleteComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Waiter.StackDeleteComplete)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["stack_exists"]) -> StackExistsWaiter:
        """
        [Waiter.StackExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Waiter.StackExists)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["stack_import_complete"]
    ) -> StackImportCompleteWaiter:
        """
        [Waiter.StackImportComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Waiter.StackImportComplete)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["stack_rollback_complete"]
    ) -> StackRollbackCompleteWaiter:
        """
        [Waiter.StackRollbackComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Waiter.StackRollbackComplete)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["stack_update_complete"]
    ) -> StackUpdateCompleteWaiter:
        """
        [Waiter.StackUpdateComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Waiter.StackUpdateComplete)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["type_registration_complete"]
    ) -> TypeRegistrationCompleteWaiter:
        """
        [Waiter.TypeRegistrationComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudformation.html#CloudFormation.Waiter.TypeRegistrationComplete)
        """

    def get_waiter(self, waiter_name: str) -> Boto3Waiter:
        pass
