"""
Type annotations for cloudformation service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/literals.html)

Usage::

    ```python
    from mypy_boto3_cloudformation.literals import AccountFilterTypeType

    data: AccountFilterTypeType = "DIFFERENCE"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccountFilterTypeType",
    "AccountGateStatusType",
    "AttributeChangeTypeType",
    "CallAsType",
    "CapabilityType",
    "CategoryType",
    "ChangeActionType",
    "ChangeSetCreateCompleteWaiterName",
    "ChangeSetHooksStatusType",
    "ChangeSetStatusType",
    "ChangeSetTypeType",
    "ChangeSourceType",
    "ChangeTypeType",
    "ConcurrencyModeType",
    "DeletionModeType",
    "DeprecatedStatusType",
    "DescribeAccountLimitsPaginatorName",
    "DescribeChangeSetPaginatorName",
    "DescribeStackEventsPaginatorName",
    "DescribeStacksPaginatorName",
    "DetailedStatusType",
    "DifferenceTypeType",
    "EvaluationTypeType",
    "ExecutionStatusType",
    "GeneratedTemplateDeletionPolicyType",
    "GeneratedTemplateResourceStatusType",
    "GeneratedTemplateStatusType",
    "GeneratedTemplateUpdateReplacePolicyType",
    "HandlerErrorCodeType",
    "HookFailureModeType",
    "HookInvocationPointType",
    "HookStatusType",
    "HookTargetTypeType",
    "IdentityProviderType",
    "ListChangeSetsPaginatorName",
    "ListExportsPaginatorName",
    "ListGeneratedTemplatesPaginatorName",
    "ListImportsPaginatorName",
    "ListResourceScanRelatedResourcesPaginatorName",
    "ListResourceScanResourcesPaginatorName",
    "ListResourceScansPaginatorName",
    "ListStackInstancesPaginatorName",
    "ListStackResourcesPaginatorName",
    "ListStackSetOperationResultsPaginatorName",
    "ListStackSetOperationsPaginatorName",
    "ListStackSetsPaginatorName",
    "ListStacksPaginatorName",
    "ListTypesPaginatorName",
    "OnFailureType",
    "OnStackFailureType",
    "OperationResultFilterNameType",
    "OperationStatusType",
    "OrganizationStatusType",
    "PermissionModelsType",
    "PolicyActionType",
    "ProvisioningTypeType",
    "PublisherStatusType",
    "RegionConcurrencyTypeType",
    "RegistrationStatusType",
    "RegistryTypeType",
    "ReplacementType",
    "RequiresRecreationType",
    "ResourceAttributeType",
    "ResourceScanStatusType",
    "ResourceSignalStatusType",
    "ResourceStatusType",
    "StackCreateCompleteWaiterName",
    "StackDeleteCompleteWaiterName",
    "StackDriftDetectionStatusType",
    "StackDriftStatusType",
    "StackExistsWaiterName",
    "StackImportCompleteWaiterName",
    "StackInstanceDetailedStatusType",
    "StackInstanceFilterNameType",
    "StackInstanceStatusType",
    "StackResourceDriftStatusType",
    "StackRollbackCompleteWaiterName",
    "StackSetDriftDetectionStatusType",
    "StackSetDriftStatusType",
    "StackSetOperationActionType",
    "StackSetOperationResultStatusType",
    "StackSetOperationStatusType",
    "StackSetStatusType",
    "StackStatusType",
    "StackUpdateCompleteWaiterName",
    "TemplateFormatType",
    "TemplateStageType",
    "ThirdPartyTypeType",
    "TypeRegistrationCompleteWaiterName",
    "TypeTestsStatusType",
    "VersionBumpType",
    "VisibilityType",
    "WarningTypeType",
)

AccountFilterTypeType = Literal["DIFFERENCE", "INTERSECTION", "NONE", "UNION"]
AccountGateStatusType = Literal["FAILED", "SKIPPED", "SUCCEEDED"]
AttributeChangeTypeType = Literal["Add", "Modify", "Remove"]
CallAsType = Literal["DELEGATED_ADMIN", "SELF"]
CapabilityType = Literal["CAPABILITY_AUTO_EXPAND", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]
CategoryType = Literal["ACTIVATED", "AWS_TYPES", "REGISTERED", "THIRD_PARTY"]
ChangeActionType = Literal["Add", "Dynamic", "Import", "Modify", "Remove"]
ChangeSetCreateCompleteWaiterName = Literal["change_set_create_complete"]
ChangeSetHooksStatusType = Literal["PLANNED", "PLANNING", "UNAVAILABLE"]
ChangeSetStatusType = Literal[
    "CREATE_COMPLETE",
    "CREATE_IN_PROGRESS",
    "CREATE_PENDING",
    "DELETE_COMPLETE",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_PENDING",
    "FAILED",
]
ChangeSetTypeType = Literal["CREATE", "IMPORT", "UPDATE"]
ChangeSourceType = Literal[
    "Automatic",
    "DirectModification",
    "ParameterReference",
    "ResourceAttribute",
    "ResourceReference",
]
ChangeTypeType = Literal["Resource"]
ConcurrencyModeType = Literal["SOFT_FAILURE_TOLERANCE", "STRICT_FAILURE_TOLERANCE"]
DeletionModeType = Literal["FORCE_DELETE_STACK", "STANDARD"]
DeprecatedStatusType = Literal["DEPRECATED", "LIVE"]
DescribeAccountLimitsPaginatorName = Literal["describe_account_limits"]
DescribeChangeSetPaginatorName = Literal["describe_change_set"]
DescribeStackEventsPaginatorName = Literal["describe_stack_events"]
DescribeStacksPaginatorName = Literal["describe_stacks"]
DetailedStatusType = Literal["CONFIGURATION_COMPLETE", "VALIDATION_FAILED"]
DifferenceTypeType = Literal["ADD", "NOT_EQUAL", "REMOVE"]
EvaluationTypeType = Literal["Dynamic", "Static"]
ExecutionStatusType = Literal[
    "AVAILABLE",
    "EXECUTE_COMPLETE",
    "EXECUTE_FAILED",
    "EXECUTE_IN_PROGRESS",
    "OBSOLETE",
    "UNAVAILABLE",
]
GeneratedTemplateDeletionPolicyType = Literal["DELETE", "RETAIN"]
GeneratedTemplateResourceStatusType = Literal["COMPLETE", "FAILED", "IN_PROGRESS", "PENDING"]
GeneratedTemplateStatusType = Literal[
    "COMPLETE",
    "CREATE_IN_PROGRESS",
    "CREATE_PENDING",
    "DELETE_IN_PROGRESS",
    "DELETE_PENDING",
    "FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_PENDING",
]
GeneratedTemplateUpdateReplacePolicyType = Literal["DELETE", "RETAIN"]
HandlerErrorCodeType = Literal[
    "AccessDenied",
    "AlreadyExists",
    "GeneralServiceException",
    "HandlerInternalFailure",
    "InternalFailure",
    "InvalidCredentials",
    "InvalidRequest",
    "InvalidTypeConfiguration",
    "NetworkFailure",
    "NonCompliant",
    "NotFound",
    "NotStabilized",
    "NotUpdatable",
    "ResourceConflict",
    "ServiceInternalError",
    "ServiceLimitExceeded",
    "Throttling",
    "Unknown",
    "UnsupportedTarget",
]
HookFailureModeType = Literal["FAIL", "WARN"]
HookInvocationPointType = Literal["PRE_PROVISION"]
HookStatusType = Literal[
    "HOOK_COMPLETE_FAILED", "HOOK_COMPLETE_SUCCEEDED", "HOOK_FAILED", "HOOK_IN_PROGRESS"
]
HookTargetTypeType = Literal["RESOURCE"]
IdentityProviderType = Literal["AWS_Marketplace", "Bitbucket", "GitHub"]
ListChangeSetsPaginatorName = Literal["list_change_sets"]
ListExportsPaginatorName = Literal["list_exports"]
ListGeneratedTemplatesPaginatorName = Literal["list_generated_templates"]
ListImportsPaginatorName = Literal["list_imports"]
ListResourceScanRelatedResourcesPaginatorName = Literal["list_resource_scan_related_resources"]
ListResourceScanResourcesPaginatorName = Literal["list_resource_scan_resources"]
ListResourceScansPaginatorName = Literal["list_resource_scans"]
ListStackInstancesPaginatorName = Literal["list_stack_instances"]
ListStackResourcesPaginatorName = Literal["list_stack_resources"]
ListStackSetOperationResultsPaginatorName = Literal["list_stack_set_operation_results"]
ListStackSetOperationsPaginatorName = Literal["list_stack_set_operations"]
ListStackSetsPaginatorName = Literal["list_stack_sets"]
ListStacksPaginatorName = Literal["list_stacks"]
ListTypesPaginatorName = Literal["list_types"]
OnFailureType = Literal["DELETE", "DO_NOTHING", "ROLLBACK"]
OnStackFailureType = Literal["DELETE", "DO_NOTHING", "ROLLBACK"]
OperationResultFilterNameType = Literal["OPERATION_RESULT_STATUS"]
OperationStatusType = Literal["FAILED", "IN_PROGRESS", "PENDING", "SUCCESS"]
OrganizationStatusType = Literal["DISABLED", "DISABLED_PERMANENTLY", "ENABLED"]
PermissionModelsType = Literal["SELF_MANAGED", "SERVICE_MANAGED"]
PolicyActionType = Literal[
    "Delete", "ReplaceAndDelete", "ReplaceAndRetain", "ReplaceAndSnapshot", "Retain", "Snapshot"
]
ProvisioningTypeType = Literal["FULLY_MUTABLE", "IMMUTABLE", "NON_PROVISIONABLE"]
PublisherStatusType = Literal["UNVERIFIED", "VERIFIED"]
RegionConcurrencyTypeType = Literal["PARALLEL", "SEQUENTIAL"]
RegistrationStatusType = Literal["COMPLETE", "FAILED", "IN_PROGRESS"]
RegistryTypeType = Literal["HOOK", "MODULE", "RESOURCE"]
ReplacementType = Literal["Conditional", "False", "True"]
RequiresRecreationType = Literal["Always", "Conditionally", "Never"]
ResourceAttributeType = Literal[
    "CreationPolicy",
    "DeletionPolicy",
    "Metadata",
    "Properties",
    "Tags",
    "UpdatePolicy",
    "UpdateReplacePolicy",
]
ResourceScanStatusType = Literal["COMPLETE", "EXPIRED", "FAILED", "IN_PROGRESS"]
ResourceSignalStatusType = Literal["FAILURE", "SUCCESS"]
ResourceStatusType = Literal[
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETE_COMPLETE",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_SKIPPED",
    "IMPORT_COMPLETE",
    "IMPORT_FAILED",
    "IMPORT_IN_PROGRESS",
    "IMPORT_ROLLBACK_COMPLETE",
    "IMPORT_ROLLBACK_FAILED",
    "IMPORT_ROLLBACK_IN_PROGRESS",
    "ROLLBACK_COMPLETE",
    "ROLLBACK_FAILED",
    "ROLLBACK_IN_PROGRESS",
    "UPDATE_COMPLETE",
    "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_ROLLBACK_COMPLETE",
    "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS",
    "UPDATE_ROLLBACK_FAILED",
    "UPDATE_ROLLBACK_IN_PROGRESS",
]
StackCreateCompleteWaiterName = Literal["stack_create_complete"]
StackDeleteCompleteWaiterName = Literal["stack_delete_complete"]
StackDriftDetectionStatusType = Literal[
    "DETECTION_COMPLETE", "DETECTION_FAILED", "DETECTION_IN_PROGRESS"
]
StackDriftStatusType = Literal["DRIFTED", "IN_SYNC", "NOT_CHECKED", "UNKNOWN"]
StackExistsWaiterName = Literal["stack_exists"]
StackImportCompleteWaiterName = Literal["stack_import_complete"]
StackInstanceDetailedStatusType = Literal[
    "CANCELLED",
    "FAILED",
    "FAILED_IMPORT",
    "INOPERABLE",
    "PENDING",
    "RUNNING",
    "SKIPPED_SUSPENDED_ACCOUNT",
    "SUCCEEDED",
]
StackInstanceFilterNameType = Literal["DETAILED_STATUS", "DRIFT_STATUS", "LAST_OPERATION_ID"]
StackInstanceStatusType = Literal["CURRENT", "INOPERABLE", "OUTDATED"]
StackResourceDriftStatusType = Literal["DELETED", "IN_SYNC", "MODIFIED", "NOT_CHECKED"]
StackRollbackCompleteWaiterName = Literal["stack_rollback_complete"]
StackSetDriftDetectionStatusType = Literal[
    "COMPLETED", "FAILED", "IN_PROGRESS", "PARTIAL_SUCCESS", "STOPPED"
]
StackSetDriftStatusType = Literal["DRIFTED", "IN_SYNC", "NOT_CHECKED"]
StackSetOperationActionType = Literal["CREATE", "DELETE", "DETECT_DRIFT", "UPDATE"]
StackSetOperationResultStatusType = Literal[
    "CANCELLED", "FAILED", "PENDING", "RUNNING", "SUCCEEDED"
]
StackSetOperationStatusType = Literal[
    "FAILED", "QUEUED", "RUNNING", "STOPPED", "STOPPING", "SUCCEEDED"
]
StackSetStatusType = Literal["ACTIVE", "DELETED"]
StackStatusType = Literal[
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETE_COMPLETE",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "IMPORT_COMPLETE",
    "IMPORT_IN_PROGRESS",
    "IMPORT_ROLLBACK_COMPLETE",
    "IMPORT_ROLLBACK_FAILED",
    "IMPORT_ROLLBACK_IN_PROGRESS",
    "REVIEW_IN_PROGRESS",
    "ROLLBACK_COMPLETE",
    "ROLLBACK_FAILED",
    "ROLLBACK_IN_PROGRESS",
    "UPDATE_COMPLETE",
    "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_ROLLBACK_COMPLETE",
    "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS",
    "UPDATE_ROLLBACK_FAILED",
    "UPDATE_ROLLBACK_IN_PROGRESS",
]
StackUpdateCompleteWaiterName = Literal["stack_update_complete"]
TemplateFormatType = Literal["JSON", "YAML"]
TemplateStageType = Literal["Original", "Processed"]
ThirdPartyTypeType = Literal["HOOK", "MODULE", "RESOURCE"]
TypeRegistrationCompleteWaiterName = Literal["type_registration_complete"]
TypeTestsStatusType = Literal["FAILED", "IN_PROGRESS", "NOT_TESTED", "PASSED"]
VersionBumpType = Literal["MAJOR", "MINOR"]
VisibilityType = Literal["PRIVATE", "PUBLIC"]
WarningTypeType = Literal[
    "MUTUALLY_EXCLUSIVE_PROPERTIES", "MUTUALLY_EXCLUSIVE_TYPES", "UNSUPPORTED_PROPERTIES"
]
