"""
Type annotations for cloudformation service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_cloudformation.type_defs import AccountGateResultTypeDef

    data: AccountGateResultTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    AccountFilterTypeType,
    AccountGateStatusType,
    AttributeChangeTypeType,
    CallAsType,
    CapabilityType,
    CategoryType,
    ChangeActionType,
    ChangeSetHooksStatusType,
    ChangeSetStatusType,
    ChangeSetTypeType,
    ChangeSourceType,
    ConcurrencyModeType,
    DeletionModeType,
    DeprecatedStatusType,
    DetailedStatusType,
    DifferenceTypeType,
    EvaluationTypeType,
    ExecutionStatusType,
    GeneratedTemplateDeletionPolicyType,
    GeneratedTemplateResourceStatusType,
    GeneratedTemplateStatusType,
    GeneratedTemplateUpdateReplacePolicyType,
    HandlerErrorCodeType,
    HookFailureModeType,
    HookStatusType,
    IdentityProviderType,
    ListHookResultsTargetTypeType,
    OnFailureType,
    OnStackFailureType,
    OperationStatusType,
    OrganizationStatusType,
    PermissionModelsType,
    PolicyActionType,
    ProvisioningTypeType,
    PublisherStatusType,
    RegionConcurrencyTypeType,
    RegistrationStatusType,
    RegistryTypeType,
    ReplacementType,
    RequiresRecreationType,
    ResourceAttributeType,
    ResourceScanStatusType,
    ResourceSignalStatusType,
    ResourceStatusType,
    ScanTypeType,
    StackDriftDetectionStatusType,
    StackDriftStatusType,
    StackInstanceDetailedStatusType,
    StackInstanceFilterNameType,
    StackInstanceStatusType,
    StackRefactorActionEntityType,
    StackRefactorActionTypeType,
    StackRefactorDetectionType,
    StackRefactorExecutionStatusType,
    StackRefactorStatusType,
    StackResourceDriftStatusType,
    StackSetDriftDetectionStatusType,
    StackSetDriftStatusType,
    StackSetOperationActionType,
    StackSetOperationResultStatusType,
    StackSetOperationStatusType,
    StackSetStatusType,
    StackStatusType,
    TemplateFormatType,
    TemplateStageType,
    ThirdPartyTypeType,
    TypeTestsStatusType,
    VersionBumpType,
    VisibilityType,
    WarningTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccountGateResultTypeDef",
    "AccountLimitTypeDef",
    "ActivateTypeInputTypeDef",
    "ActivateTypeOutputTypeDef",
    "AutoDeploymentTypeDef",
    "BatchDescribeTypeConfigurationsErrorTypeDef",
    "BatchDescribeTypeConfigurationsInputTypeDef",
    "BatchDescribeTypeConfigurationsOutputTypeDef",
    "CancelUpdateStackInputStackCancelUpdateTypeDef",
    "CancelUpdateStackInputTypeDef",
    "ChangeSetHookResourceTargetDetailsTypeDef",
    "ChangeSetHookTargetDetailsTypeDef",
    "ChangeSetHookTypeDef",
    "ChangeSetSummaryTypeDef",
    "ChangeTypeDef",
    "ContinueUpdateRollbackInputTypeDef",
    "CreateChangeSetInputTypeDef",
    "CreateChangeSetOutputTypeDef",
    "CreateGeneratedTemplateInputTypeDef",
    "CreateGeneratedTemplateOutputTypeDef",
    "CreateStackInputServiceResourceCreateStackTypeDef",
    "CreateStackInputTypeDef",
    "CreateStackInstancesInputTypeDef",
    "CreateStackInstancesOutputTypeDef",
    "CreateStackOutputTypeDef",
    "CreateStackRefactorInputTypeDef",
    "CreateStackRefactorOutputTypeDef",
    "CreateStackSetInputTypeDef",
    "CreateStackSetOutputTypeDef",
    "DeactivateTypeInputTypeDef",
    "DeleteChangeSetInputTypeDef",
    "DeleteGeneratedTemplateInputTypeDef",
    "DeleteStackInputStackDeleteTypeDef",
    "DeleteStackInputTypeDef",
    "DeleteStackInstancesInputTypeDef",
    "DeleteStackInstancesOutputTypeDef",
    "DeleteStackSetInputTypeDef",
    "DeploymentTargetsOutputTypeDef",
    "DeploymentTargetsTypeDef",
    "DeploymentTargetsUnionTypeDef",
    "DeregisterTypeInputTypeDef",
    "DescribeAccountLimitsInputPaginateTypeDef",
    "DescribeAccountLimitsInputTypeDef",
    "DescribeAccountLimitsOutputTypeDef",
    "DescribeChangeSetHooksInputTypeDef",
    "DescribeChangeSetHooksOutputTypeDef",
    "DescribeChangeSetInputPaginateTypeDef",
    "DescribeChangeSetInputTypeDef",
    "DescribeChangeSetInputWaitTypeDef",
    "DescribeChangeSetOutputTypeDef",
    "DescribeGeneratedTemplateInputTypeDef",
    "DescribeGeneratedTemplateOutputTypeDef",
    "DescribeOrganizationsAccessInputTypeDef",
    "DescribeOrganizationsAccessOutputTypeDef",
    "DescribePublisherInputTypeDef",
    "DescribePublisherOutputTypeDef",
    "DescribeResourceScanInputTypeDef",
    "DescribeResourceScanOutputTypeDef",
    "DescribeStackDriftDetectionStatusInputTypeDef",
    "DescribeStackDriftDetectionStatusOutputTypeDef",
    "DescribeStackEventsInputPaginateTypeDef",
    "DescribeStackEventsInputTypeDef",
    "DescribeStackEventsOutputTypeDef",
    "DescribeStackInstanceInputTypeDef",
    "DescribeStackInstanceOutputTypeDef",
    "DescribeStackRefactorInputTypeDef",
    "DescribeStackRefactorInputWaitExtraTypeDef",
    "DescribeStackRefactorInputWaitTypeDef",
    "DescribeStackRefactorOutputTypeDef",
    "DescribeStackResourceDriftsInputTypeDef",
    "DescribeStackResourceDriftsOutputTypeDef",
    "DescribeStackResourceInputTypeDef",
    "DescribeStackResourceOutputTypeDef",
    "DescribeStackResourcesInputTypeDef",
    "DescribeStackResourcesOutputTypeDef",
    "DescribeStackSetInputTypeDef",
    "DescribeStackSetOperationInputTypeDef",
    "DescribeStackSetOperationOutputTypeDef",
    "DescribeStackSetOutputTypeDef",
    "DescribeStacksInputPaginateTypeDef",
    "DescribeStacksInputTypeDef",
    "DescribeStacksInputWaitExtraExtraExtraExtraExtraTypeDef",
    "DescribeStacksInputWaitExtraExtraExtraExtraTypeDef",
    "DescribeStacksInputWaitExtraExtraExtraTypeDef",
    "DescribeStacksInputWaitExtraExtraTypeDef",
    "DescribeStacksInputWaitExtraTypeDef",
    "DescribeStacksInputWaitTypeDef",
    "DescribeStacksOutputTypeDef",
    "DescribeTypeInputTypeDef",
    "DescribeTypeOutputTypeDef",
    "DescribeTypeRegistrationInputTypeDef",
    "DescribeTypeRegistrationInputWaitTypeDef",
    "DescribeTypeRegistrationOutputTypeDef",
    "DetectStackDriftInputTypeDef",
    "DetectStackDriftOutputTypeDef",
    "DetectStackResourceDriftInputTypeDef",
    "DetectStackResourceDriftOutputTypeDef",
    "DetectStackSetDriftInputTypeDef",
    "DetectStackSetDriftOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EstimateTemplateCostInputTypeDef",
    "EstimateTemplateCostOutputTypeDef",
    "ExecuteChangeSetInputTypeDef",
    "ExecuteStackRefactorInputTypeDef",
    "ExportTypeDef",
    "GetGeneratedTemplateInputTypeDef",
    "GetGeneratedTemplateOutputTypeDef",
    "GetStackPolicyInputTypeDef",
    "GetStackPolicyOutputTypeDef",
    "GetTemplateInputTypeDef",
    "GetTemplateOutputTypeDef",
    "GetTemplateSummaryInputTypeDef",
    "GetTemplateSummaryOutputTypeDef",
    "HookResultSummaryTypeDef",
    "ImportStacksToStackSetInputTypeDef",
    "ImportStacksToStackSetOutputTypeDef",
    "ListChangeSetsInputPaginateTypeDef",
    "ListChangeSetsInputTypeDef",
    "ListChangeSetsOutputTypeDef",
    "ListExportsInputPaginateTypeDef",
    "ListExportsInputTypeDef",
    "ListExportsOutputTypeDef",
    "ListGeneratedTemplatesInputPaginateTypeDef",
    "ListGeneratedTemplatesInputTypeDef",
    "ListGeneratedTemplatesOutputTypeDef",
    "ListHookResultsInputTypeDef",
    "ListHookResultsOutputTypeDef",
    "ListImportsInputPaginateTypeDef",
    "ListImportsInputTypeDef",
    "ListImportsOutputTypeDef",
    "ListResourceScanRelatedResourcesInputPaginateTypeDef",
    "ListResourceScanRelatedResourcesInputTypeDef",
    "ListResourceScanRelatedResourcesOutputTypeDef",
    "ListResourceScanResourcesInputPaginateTypeDef",
    "ListResourceScanResourcesInputTypeDef",
    "ListResourceScanResourcesOutputTypeDef",
    "ListResourceScansInputPaginateTypeDef",
    "ListResourceScansInputTypeDef",
    "ListResourceScansOutputTypeDef",
    "ListStackInstanceResourceDriftsInputTypeDef",
    "ListStackInstanceResourceDriftsOutputTypeDef",
    "ListStackInstancesInputPaginateTypeDef",
    "ListStackInstancesInputTypeDef",
    "ListStackInstancesOutputTypeDef",
    "ListStackRefactorActionsInputPaginateTypeDef",
    "ListStackRefactorActionsInputTypeDef",
    "ListStackRefactorActionsOutputTypeDef",
    "ListStackRefactorsInputPaginateTypeDef",
    "ListStackRefactorsInputTypeDef",
    "ListStackRefactorsOutputTypeDef",
    "ListStackResourcesInputPaginateTypeDef",
    "ListStackResourcesInputTypeDef",
    "ListStackResourcesOutputTypeDef",
    "ListStackSetAutoDeploymentTargetsInputTypeDef",
    "ListStackSetAutoDeploymentTargetsOutputTypeDef",
    "ListStackSetOperationResultsInputPaginateTypeDef",
    "ListStackSetOperationResultsInputTypeDef",
    "ListStackSetOperationResultsOutputTypeDef",
    "ListStackSetOperationsInputPaginateTypeDef",
    "ListStackSetOperationsInputTypeDef",
    "ListStackSetOperationsOutputTypeDef",
    "ListStackSetsInputPaginateTypeDef",
    "ListStackSetsInputTypeDef",
    "ListStackSetsOutputTypeDef",
    "ListStacksInputPaginateTypeDef",
    "ListStacksInputTypeDef",
    "ListStacksOutputTypeDef",
    "ListTypeRegistrationsInputTypeDef",
    "ListTypeRegistrationsOutputTypeDef",
    "ListTypeVersionsInputTypeDef",
    "ListTypeVersionsOutputTypeDef",
    "ListTypesInputPaginateTypeDef",
    "ListTypesInputTypeDef",
    "ListTypesOutputTypeDef",
    "LoggingConfigTypeDef",
    "ManagedExecutionTypeDef",
    "ModuleInfoTypeDef",
    "OperationResultFilterTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterConstraintsTypeDef",
    "ParameterDeclarationTypeDef",
    "ParameterTypeDef",
    "PhysicalResourceIdContextKeyValuePairTypeDef",
    "PropertyDifferenceTypeDef",
    "PublishTypeInputTypeDef",
    "PublishTypeOutputTypeDef",
    "RecordHandlerProgressInputTypeDef",
    "RegisterPublisherInputTypeDef",
    "RegisterPublisherOutputTypeDef",
    "RegisterTypeInputTypeDef",
    "RegisterTypeOutputTypeDef",
    "RequiredActivatedTypeTypeDef",
    "ResourceChangeDetailTypeDef",
    "ResourceChangeTypeDef",
    "ResourceDefinitionTypeDef",
    "ResourceDetailTypeDef",
    "ResourceIdentifierSummaryTypeDef",
    "ResourceLocationTypeDef",
    "ResourceMappingTypeDef",
    "ResourceScanSummaryTypeDef",
    "ResourceTargetDefinitionTypeDef",
    "ResourceToImportTypeDef",
    "ResponseMetadataTypeDef",
    "RollbackConfigurationOutputTypeDef",
    "RollbackConfigurationTypeDef",
    "RollbackConfigurationUnionTypeDef",
    "RollbackStackInputTypeDef",
    "RollbackStackOutputTypeDef",
    "RollbackTriggerTypeDef",
    "ScanFilterOutputTypeDef",
    "ScanFilterTypeDef",
    "ScanFilterUnionTypeDef",
    "ScannedResourceIdentifierTypeDef",
    "ScannedResourceTypeDef",
    "SetStackPolicyInputTypeDef",
    "SetTypeConfigurationInputTypeDef",
    "SetTypeConfigurationOutputTypeDef",
    "SetTypeDefaultVersionInputTypeDef",
    "SignalResourceInputTypeDef",
    "StackDefinitionTypeDef",
    "StackDriftInformationSummaryTypeDef",
    "StackDriftInformationTypeDef",
    "StackEventTypeDef",
    "StackInstanceComprehensiveStatusTypeDef",
    "StackInstanceFilterTypeDef",
    "StackInstanceResourceDriftsSummaryTypeDef",
    "StackInstanceSummaryTypeDef",
    "StackInstanceTypeDef",
    "StackRefactorActionTypeDef",
    "StackRefactorSummaryTypeDef",
    "StackResourceDetailTypeDef",
    "StackResourceDriftInformationSummaryTypeDef",
    "StackResourceDriftInformationTypeDef",
    "StackResourceDriftTypeDef",
    "StackResourceSummaryTypeDef",
    "StackResourceTypeDef",
    "StackSetAutoDeploymentTargetSummaryTypeDef",
    "StackSetDriftDetectionDetailsTypeDef",
    "StackSetOperationPreferencesOutputTypeDef",
    "StackSetOperationPreferencesTypeDef",
    "StackSetOperationPreferencesUnionTypeDef",
    "StackSetOperationResultSummaryTypeDef",
    "StackSetOperationStatusDetailsTypeDef",
    "StackSetOperationSummaryTypeDef",
    "StackSetOperationTypeDef",
    "StackSetSummaryTypeDef",
    "StackSetTypeDef",
    "StackSummaryTypeDef",
    "StackTypeDef",
    "StartResourceScanInputTypeDef",
    "StartResourceScanOutputTypeDef",
    "StopStackSetOperationInputTypeDef",
    "TagTypeDef",
    "TemplateConfigurationTypeDef",
    "TemplateParameterTypeDef",
    "TemplateProgressTypeDef",
    "TemplateSummaryConfigTypeDef",
    "TemplateSummaryTypeDef",
    "TestTypeInputTypeDef",
    "TestTypeOutputTypeDef",
    "TypeConfigurationDetailsTypeDef",
    "TypeConfigurationIdentifierTypeDef",
    "TypeFiltersTypeDef",
    "TypeSummaryTypeDef",
    "TypeVersionSummaryTypeDef",
    "UpdateGeneratedTemplateInputTypeDef",
    "UpdateGeneratedTemplateOutputTypeDef",
    "UpdateStackInputStackUpdateTypeDef",
    "UpdateStackInputTypeDef",
    "UpdateStackInstancesInputTypeDef",
    "UpdateStackInstancesOutputTypeDef",
    "UpdateStackOutputTypeDef",
    "UpdateStackSetInputTypeDef",
    "UpdateStackSetOutputTypeDef",
    "UpdateTerminationProtectionInputTypeDef",
    "UpdateTerminationProtectionOutputTypeDef",
    "ValidateTemplateInputTypeDef",
    "ValidateTemplateOutputTypeDef",
    "WaiterConfigTypeDef",
    "WarningDetailTypeDef",
    "WarningPropertyTypeDef",
    "WarningsTypeDef",
)

class AccountGateResultTypeDef(TypedDict):
    Status: NotRequired[AccountGateStatusType]
    StatusReason: NotRequired[str]

class AccountLimitTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[int]

class LoggingConfigTypeDef(TypedDict):
    LogRoleArn: str
    LogGroupName: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AutoDeploymentTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    RetainStacksOnAccountRemoval: NotRequired[bool]

TypeConfigurationIdentifierTypeDef = TypedDict(
    "TypeConfigurationIdentifierTypeDef",
    {
        "TypeArn": NotRequired[str],
        "TypeConfigurationAlias": NotRequired[str],
        "TypeConfigurationArn": NotRequired[str],
        "Type": NotRequired[ThirdPartyTypeType],
        "TypeName": NotRequired[str],
    },
)

class TypeConfigurationDetailsTypeDef(TypedDict):
    Arn: NotRequired[str]
    Alias: NotRequired[str]
    Configuration: NotRequired[str]
    LastUpdated: NotRequired[datetime]
    TypeArn: NotRequired[str]
    TypeName: NotRequired[str]
    IsDefaultConfiguration: NotRequired[bool]

class CancelUpdateStackInputStackCancelUpdateTypeDef(TypedDict):
    ClientRequestToken: NotRequired[str]

class CancelUpdateStackInputTypeDef(TypedDict):
    StackName: str
    ClientRequestToken: NotRequired[str]

class ChangeSetHookResourceTargetDetailsTypeDef(TypedDict):
    LogicalResourceId: NotRequired[str]
    ResourceType: NotRequired[str]
    ResourceAction: NotRequired[ChangeActionType]

class ChangeSetSummaryTypeDef(TypedDict):
    StackId: NotRequired[str]
    StackName: NotRequired[str]
    ChangeSetId: NotRequired[str]
    ChangeSetName: NotRequired[str]
    ExecutionStatus: NotRequired[ExecutionStatusType]
    Status: NotRequired[ChangeSetStatusType]
    StatusReason: NotRequired[str]
    CreationTime: NotRequired[datetime]
    Description: NotRequired[str]
    IncludeNestedStacks: NotRequired[bool]
    ParentChangeSetId: NotRequired[str]
    RootChangeSetId: NotRequired[str]
    ImportExistingResources: NotRequired[bool]

class ContinueUpdateRollbackInputTypeDef(TypedDict):
    StackName: str
    RoleARN: NotRequired[str]
    ResourcesToSkip: NotRequired[Sequence[str]]
    ClientRequestToken: NotRequired[str]

class ParameterTypeDef(TypedDict):
    ParameterKey: NotRequired[str]
    ParameterValue: NotRequired[str]
    UsePreviousValue: NotRequired[bool]
    ResolvedValue: NotRequired[str]

class ResourceToImportTypeDef(TypedDict):
    ResourceType: str
    LogicalResourceId: str
    ResourceIdentifier: Mapping[str, str]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class ResourceDefinitionTypeDef(TypedDict):
    ResourceType: str
    ResourceIdentifier: Mapping[str, str]
    LogicalResourceId: NotRequired[str]

class TemplateConfigurationTypeDef(TypedDict):
    DeletionPolicy: NotRequired[GeneratedTemplateDeletionPolicyType]
    UpdateReplacePolicy: NotRequired[GeneratedTemplateUpdateReplacePolicyType]

class StackDefinitionTypeDef(TypedDict):
    StackName: NotRequired[str]
    TemplateBody: NotRequired[str]
    TemplateURL: NotRequired[str]

class ManagedExecutionTypeDef(TypedDict):
    Active: NotRequired[bool]

DeactivateTypeInputTypeDef = TypedDict(
    "DeactivateTypeInputTypeDef",
    {
        "TypeName": NotRequired[str],
        "Type": NotRequired[ThirdPartyTypeType],
        "Arn": NotRequired[str],
    },
)

class DeleteChangeSetInputTypeDef(TypedDict):
    ChangeSetName: str
    StackName: NotRequired[str]

class DeleteGeneratedTemplateInputTypeDef(TypedDict):
    GeneratedTemplateName: str

class DeleteStackInputStackDeleteTypeDef(TypedDict):
    RetainResources: NotRequired[Sequence[str]]
    RoleARN: NotRequired[str]
    ClientRequestToken: NotRequired[str]
    DeletionMode: NotRequired[DeletionModeType]

class DeleteStackInputTypeDef(TypedDict):
    StackName: str
    RetainResources: NotRequired[Sequence[str]]
    RoleARN: NotRequired[str]
    ClientRequestToken: NotRequired[str]
    DeletionMode: NotRequired[DeletionModeType]

class DeleteStackSetInputTypeDef(TypedDict):
    StackSetName: str
    CallAs: NotRequired[CallAsType]

class DeploymentTargetsOutputTypeDef(TypedDict):
    Accounts: NotRequired[List[str]]
    AccountsUrl: NotRequired[str]
    OrganizationalUnitIds: NotRequired[List[str]]
    AccountFilterType: NotRequired[AccountFilterTypeType]

class DeploymentTargetsTypeDef(TypedDict):
    Accounts: NotRequired[Sequence[str]]
    AccountsUrl: NotRequired[str]
    OrganizationalUnitIds: NotRequired[Sequence[str]]
    AccountFilterType: NotRequired[AccountFilterTypeType]

DeregisterTypeInputTypeDef = TypedDict(
    "DeregisterTypeInputTypeDef",
    {
        "Arn": NotRequired[str],
        "Type": NotRequired[RegistryTypeType],
        "TypeName": NotRequired[str],
        "VersionId": NotRequired[str],
    },
)

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeAccountLimitsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]

class DescribeChangeSetHooksInputTypeDef(TypedDict):
    ChangeSetName: str
    StackName: NotRequired[str]
    NextToken: NotRequired[str]
    LogicalResourceId: NotRequired[str]

class DescribeChangeSetInputTypeDef(TypedDict):
    ChangeSetName: str
    StackName: NotRequired[str]
    NextToken: NotRequired[str]
    IncludePropertyValues: NotRequired[bool]

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class DescribeGeneratedTemplateInputTypeDef(TypedDict):
    GeneratedTemplateName: str

class TemplateProgressTypeDef(TypedDict):
    ResourcesSucceeded: NotRequired[int]
    ResourcesFailed: NotRequired[int]
    ResourcesProcessing: NotRequired[int]
    ResourcesPending: NotRequired[int]

class DescribeOrganizationsAccessInputTypeDef(TypedDict):
    CallAs: NotRequired[CallAsType]

class DescribePublisherInputTypeDef(TypedDict):
    PublisherId: NotRequired[str]

class DescribeResourceScanInputTypeDef(TypedDict):
    ResourceScanId: str

class ScanFilterOutputTypeDef(TypedDict):
    Types: NotRequired[List[str]]

class DescribeStackDriftDetectionStatusInputTypeDef(TypedDict):
    StackDriftDetectionId: str

class DescribeStackEventsInputTypeDef(TypedDict):
    StackName: NotRequired[str]
    NextToken: NotRequired[str]

class StackEventTypeDef(TypedDict):
    StackId: str
    EventId: str
    StackName: str
    Timestamp: datetime
    LogicalResourceId: NotRequired[str]
    PhysicalResourceId: NotRequired[str]
    ResourceType: NotRequired[str]
    ResourceStatus: NotRequired[ResourceStatusType]
    ResourceStatusReason: NotRequired[str]
    ResourceProperties: NotRequired[str]
    ClientRequestToken: NotRequired[str]
    HookType: NotRequired[str]
    HookStatus: NotRequired[HookStatusType]
    HookStatusReason: NotRequired[str]
    HookInvocationPoint: NotRequired[Literal["PRE_PROVISION"]]
    HookFailureMode: NotRequired[HookFailureModeType]
    DetailedStatus: NotRequired[DetailedStatusType]

class DescribeStackInstanceInputTypeDef(TypedDict):
    StackSetName: str
    StackInstanceAccount: str
    StackInstanceRegion: str
    CallAs: NotRequired[CallAsType]

class DescribeStackRefactorInputTypeDef(TypedDict):
    StackRefactorId: str

class DescribeStackResourceDriftsInputTypeDef(TypedDict):
    StackName: str
    StackResourceDriftStatusFilters: NotRequired[Sequence[StackResourceDriftStatusType]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeStackResourceInputTypeDef(TypedDict):
    StackName: str
    LogicalResourceId: str

class DescribeStackResourcesInputTypeDef(TypedDict):
    StackName: NotRequired[str]
    LogicalResourceId: NotRequired[str]
    PhysicalResourceId: NotRequired[str]

class DescribeStackSetInputTypeDef(TypedDict):
    StackSetName: str
    CallAs: NotRequired[CallAsType]

class DescribeStackSetOperationInputTypeDef(TypedDict):
    StackSetName: str
    OperationId: str
    CallAs: NotRequired[CallAsType]

class DescribeStacksInputTypeDef(TypedDict):
    StackName: NotRequired[str]
    NextToken: NotRequired[str]

DescribeTypeInputTypeDef = TypedDict(
    "DescribeTypeInputTypeDef",
    {
        "Type": NotRequired[RegistryTypeType],
        "TypeName": NotRequired[str],
        "Arn": NotRequired[str],
        "VersionId": NotRequired[str],
        "PublisherId": NotRequired[str],
        "PublicVersionNumber": NotRequired[str],
    },
)

class RequiredActivatedTypeTypeDef(TypedDict):
    TypeNameAlias: NotRequired[str]
    OriginalTypeName: NotRequired[str]
    PublisherId: NotRequired[str]
    SupportedMajorVersions: NotRequired[List[int]]

class DescribeTypeRegistrationInputTypeDef(TypedDict):
    RegistrationToken: str

class DetectStackDriftInputTypeDef(TypedDict):
    StackName: str
    LogicalResourceIds: NotRequired[Sequence[str]]

class DetectStackResourceDriftInputTypeDef(TypedDict):
    StackName: str
    LogicalResourceId: str

class ExecuteChangeSetInputTypeDef(TypedDict):
    ChangeSetName: str
    StackName: NotRequired[str]
    ClientRequestToken: NotRequired[str]
    DisableRollback: NotRequired[bool]
    RetainExceptOnCreate: NotRequired[bool]

class ExecuteStackRefactorInputTypeDef(TypedDict):
    StackRefactorId: str

class ExportTypeDef(TypedDict):
    ExportingStackId: NotRequired[str]
    Name: NotRequired[str]
    Value: NotRequired[str]

class GetGeneratedTemplateInputTypeDef(TypedDict):
    GeneratedTemplateName: str
    Format: NotRequired[TemplateFormatType]

class GetStackPolicyInputTypeDef(TypedDict):
    StackName: str

class GetTemplateInputTypeDef(TypedDict):
    StackName: NotRequired[str]
    ChangeSetName: NotRequired[str]
    TemplateStage: NotRequired[TemplateStageType]

class TemplateSummaryConfigTypeDef(TypedDict):
    TreatUnrecognizedResourceTypesAsWarnings: NotRequired[bool]

class ResourceIdentifierSummaryTypeDef(TypedDict):
    ResourceType: NotRequired[str]
    LogicalResourceIds: NotRequired[List[str]]
    ResourceIdentifiers: NotRequired[List[str]]

class WarningsTypeDef(TypedDict):
    UnrecognizedResourceTypes: NotRequired[List[str]]

class HookResultSummaryTypeDef(TypedDict):
    InvocationPoint: NotRequired[Literal["PRE_PROVISION"]]
    FailureMode: NotRequired[HookFailureModeType]
    TypeName: NotRequired[str]
    TypeVersionId: NotRequired[str]
    TypeConfigurationVersionId: NotRequired[str]
    Status: NotRequired[HookStatusType]
    HookStatusReason: NotRequired[str]

class ListChangeSetsInputTypeDef(TypedDict):
    StackName: str
    NextToken: NotRequired[str]

class ListExportsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]

class ListGeneratedTemplatesInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class TemplateSummaryTypeDef(TypedDict):
    GeneratedTemplateId: NotRequired[str]
    GeneratedTemplateName: NotRequired[str]
    Status: NotRequired[GeneratedTemplateStatusType]
    StatusReason: NotRequired[str]
    CreationTime: NotRequired[datetime]
    LastUpdatedTime: NotRequired[datetime]
    NumberOfResources: NotRequired[int]

class ListHookResultsInputTypeDef(TypedDict):
    TargetType: ListHookResultsTargetTypeType
    TargetId: str
    NextToken: NotRequired[str]

class ListImportsInputTypeDef(TypedDict):
    ExportName: str
    NextToken: NotRequired[str]

class ScannedResourceIdentifierTypeDef(TypedDict):
    ResourceType: str
    ResourceIdentifier: Mapping[str, str]

class ScannedResourceTypeDef(TypedDict):
    ResourceType: NotRequired[str]
    ResourceIdentifier: NotRequired[Dict[str, str]]
    ManagedByStack: NotRequired[bool]

class ListResourceScanResourcesInputTypeDef(TypedDict):
    ResourceScanId: str
    ResourceIdentifier: NotRequired[str]
    ResourceTypePrefix: NotRequired[str]
    TagKey: NotRequired[str]
    TagValue: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListResourceScansInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ScanTypeFilter: NotRequired[ScanTypeType]

class ResourceScanSummaryTypeDef(TypedDict):
    ResourceScanId: NotRequired[str]
    Status: NotRequired[ResourceScanStatusType]
    StatusReason: NotRequired[str]
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    PercentageCompleted: NotRequired[float]
    ScanType: NotRequired[ScanTypeType]

class ListStackInstanceResourceDriftsInputTypeDef(TypedDict):
    StackSetName: str
    StackInstanceAccount: str
    StackInstanceRegion: str
    OperationId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    StackInstanceResourceDriftStatuses: NotRequired[Sequence[StackResourceDriftStatusType]]
    CallAs: NotRequired[CallAsType]

class StackInstanceFilterTypeDef(TypedDict):
    Name: NotRequired[StackInstanceFilterNameType]
    Values: NotRequired[str]

class ListStackRefactorActionsInputTypeDef(TypedDict):
    StackRefactorId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListStackRefactorsInputTypeDef(TypedDict):
    ExecutionStatusFilter: NotRequired[Sequence[StackRefactorExecutionStatusType]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class StackRefactorSummaryTypeDef(TypedDict):
    StackRefactorId: NotRequired[str]
    Description: NotRequired[str]
    ExecutionStatus: NotRequired[StackRefactorExecutionStatusType]
    ExecutionStatusReason: NotRequired[str]
    Status: NotRequired[StackRefactorStatusType]
    StatusReason: NotRequired[str]

class ListStackResourcesInputTypeDef(TypedDict):
    StackName: str
    NextToken: NotRequired[str]

class ListStackSetAutoDeploymentTargetsInputTypeDef(TypedDict):
    StackSetName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    CallAs: NotRequired[CallAsType]

class StackSetAutoDeploymentTargetSummaryTypeDef(TypedDict):
    OrganizationalUnitId: NotRequired[str]
    Regions: NotRequired[List[str]]

class OperationResultFilterTypeDef(TypedDict):
    Name: NotRequired[Literal["OPERATION_RESULT_STATUS"]]
    Values: NotRequired[str]

class ListStackSetOperationsInputTypeDef(TypedDict):
    StackSetName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    CallAs: NotRequired[CallAsType]

class ListStackSetsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Status: NotRequired[StackSetStatusType]
    CallAs: NotRequired[CallAsType]

class ListStacksInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    StackStatusFilter: NotRequired[Sequence[StackStatusType]]

ListTypeRegistrationsInputTypeDef = TypedDict(
    "ListTypeRegistrationsInputTypeDef",
    {
        "Type": NotRequired[RegistryTypeType],
        "TypeName": NotRequired[str],
        "TypeArn": NotRequired[str],
        "RegistrationStatusFilter": NotRequired[RegistrationStatusType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTypeVersionsInputTypeDef = TypedDict(
    "ListTypeVersionsInputTypeDef",
    {
        "Type": NotRequired[RegistryTypeType],
        "TypeName": NotRequired[str],
        "Arn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DeprecatedStatus": NotRequired[DeprecatedStatusType],
        "PublisherId": NotRequired[str],
    },
)
TypeVersionSummaryTypeDef = TypedDict(
    "TypeVersionSummaryTypeDef",
    {
        "Type": NotRequired[RegistryTypeType],
        "TypeName": NotRequired[str],
        "VersionId": NotRequired[str],
        "IsDefaultVersion": NotRequired[bool],
        "Arn": NotRequired[str],
        "TimeCreated": NotRequired[datetime],
        "Description": NotRequired[str],
        "PublicVersionNumber": NotRequired[str],
    },
)

class TypeFiltersTypeDef(TypedDict):
    Category: NotRequired[CategoryType]
    PublisherId: NotRequired[str]
    TypeNamePrefix: NotRequired[str]

TypeSummaryTypeDef = TypedDict(
    "TypeSummaryTypeDef",
    {
        "Type": NotRequired[RegistryTypeType],
        "TypeName": NotRequired[str],
        "DefaultVersionId": NotRequired[str],
        "TypeArn": NotRequired[str],
        "LastUpdated": NotRequired[datetime],
        "Description": NotRequired[str],
        "PublisherId": NotRequired[str],
        "OriginalTypeName": NotRequired[str],
        "PublicVersionNumber": NotRequired[str],
        "LatestPublicVersion": NotRequired[str],
        "PublisherIdentity": NotRequired[IdentityProviderType],
        "PublisherName": NotRequired[str],
        "IsActivated": NotRequired[bool],
    },
)

class ModuleInfoTypeDef(TypedDict):
    TypeHierarchy: NotRequired[str]
    LogicalIdHierarchy: NotRequired[str]

class OutputTypeDef(TypedDict):
    OutputKey: NotRequired[str]
    OutputValue: NotRequired[str]
    Description: NotRequired[str]
    ExportName: NotRequired[str]

class ParameterConstraintsTypeDef(TypedDict):
    AllowedValues: NotRequired[List[str]]

class PhysicalResourceIdContextKeyValuePairTypeDef(TypedDict):
    Key: str
    Value: str

class PropertyDifferenceTypeDef(TypedDict):
    PropertyPath: str
    ExpectedValue: str
    ActualValue: str
    DifferenceType: DifferenceTypeType

PublishTypeInputTypeDef = TypedDict(
    "PublishTypeInputTypeDef",
    {
        "Type": NotRequired[ThirdPartyTypeType],
        "Arn": NotRequired[str],
        "TypeName": NotRequired[str],
        "PublicVersionNumber": NotRequired[str],
    },
)

class RecordHandlerProgressInputTypeDef(TypedDict):
    BearerToken: str
    OperationStatus: OperationStatusType
    CurrentOperationStatus: NotRequired[OperationStatusType]
    StatusMessage: NotRequired[str]
    ErrorCode: NotRequired[HandlerErrorCodeType]
    ResourceModel: NotRequired[str]
    ClientRequestToken: NotRequired[str]

class RegisterPublisherInputTypeDef(TypedDict):
    AcceptTermsAndConditions: NotRequired[bool]
    ConnectionArn: NotRequired[str]

class ResourceTargetDefinitionTypeDef(TypedDict):
    Attribute: NotRequired[ResourceAttributeType]
    Name: NotRequired[str]
    RequiresRecreation: NotRequired[RequiresRecreationType]
    Path: NotRequired[str]
    BeforeValue: NotRequired[str]
    AfterValue: NotRequired[str]
    AttributeChangeType: NotRequired[AttributeChangeTypeType]

class ResourceLocationTypeDef(TypedDict):
    StackName: str
    LogicalResourceId: str

RollbackTriggerTypeDef = TypedDict(
    "RollbackTriggerTypeDef",
    {
        "Arn": str,
        "Type": str,
    },
)

class RollbackStackInputTypeDef(TypedDict):
    StackName: str
    RoleARN: NotRequired[str]
    ClientRequestToken: NotRequired[str]
    RetainExceptOnCreate: NotRequired[bool]

class ScanFilterTypeDef(TypedDict):
    Types: NotRequired[Sequence[str]]

class SetStackPolicyInputTypeDef(TypedDict):
    StackName: str
    StackPolicyBody: NotRequired[str]
    StackPolicyURL: NotRequired[str]

SetTypeConfigurationInputTypeDef = TypedDict(
    "SetTypeConfigurationInputTypeDef",
    {
        "Configuration": str,
        "TypeArn": NotRequired[str],
        "ConfigurationAlias": NotRequired[str],
        "TypeName": NotRequired[str],
        "Type": NotRequired[ThirdPartyTypeType],
    },
)
SetTypeDefaultVersionInputTypeDef = TypedDict(
    "SetTypeDefaultVersionInputTypeDef",
    {
        "Arn": NotRequired[str],
        "Type": NotRequired[RegistryTypeType],
        "TypeName": NotRequired[str],
        "VersionId": NotRequired[str],
    },
)

class SignalResourceInputTypeDef(TypedDict):
    StackName: str
    LogicalResourceId: str
    UniqueId: str
    Status: ResourceSignalStatusType

class StackDriftInformationSummaryTypeDef(TypedDict):
    StackDriftStatus: StackDriftStatusType
    LastCheckTimestamp: NotRequired[datetime]

class StackDriftInformationTypeDef(TypedDict):
    StackDriftStatus: StackDriftStatusType
    LastCheckTimestamp: NotRequired[datetime]

class StackInstanceComprehensiveStatusTypeDef(TypedDict):
    DetailedStatus: NotRequired[StackInstanceDetailedStatusType]

class StackResourceDriftInformationTypeDef(TypedDict):
    StackResourceDriftStatus: StackResourceDriftStatusType
    LastCheckTimestamp: NotRequired[datetime]

class StackResourceDriftInformationSummaryTypeDef(TypedDict):
    StackResourceDriftStatus: StackResourceDriftStatusType
    LastCheckTimestamp: NotRequired[datetime]

class StackSetDriftDetectionDetailsTypeDef(TypedDict):
    DriftStatus: NotRequired[StackSetDriftStatusType]
    DriftDetectionStatus: NotRequired[StackSetDriftDetectionStatusType]
    LastDriftCheckTimestamp: NotRequired[datetime]
    TotalStackInstancesCount: NotRequired[int]
    DriftedStackInstancesCount: NotRequired[int]
    InSyncStackInstancesCount: NotRequired[int]
    InProgressStackInstancesCount: NotRequired[int]
    FailedStackInstancesCount: NotRequired[int]

class StackSetOperationPreferencesOutputTypeDef(TypedDict):
    RegionConcurrencyType: NotRequired[RegionConcurrencyTypeType]
    RegionOrder: NotRequired[List[str]]
    FailureToleranceCount: NotRequired[int]
    FailureTolerancePercentage: NotRequired[int]
    MaxConcurrentCount: NotRequired[int]
    MaxConcurrentPercentage: NotRequired[int]
    ConcurrencyMode: NotRequired[ConcurrencyModeType]

class StackSetOperationPreferencesTypeDef(TypedDict):
    RegionConcurrencyType: NotRequired[RegionConcurrencyTypeType]
    RegionOrder: NotRequired[Sequence[str]]
    FailureToleranceCount: NotRequired[int]
    FailureTolerancePercentage: NotRequired[int]
    MaxConcurrentCount: NotRequired[int]
    MaxConcurrentPercentage: NotRequired[int]
    ConcurrencyMode: NotRequired[ConcurrencyModeType]

class StackSetOperationStatusDetailsTypeDef(TypedDict):
    FailedStackInstancesCount: NotRequired[int]

class StopStackSetOperationInputTypeDef(TypedDict):
    StackSetName: str
    OperationId: str
    CallAs: NotRequired[CallAsType]

class TemplateParameterTypeDef(TypedDict):
    ParameterKey: NotRequired[str]
    DefaultValue: NotRequired[str]
    NoEcho: NotRequired[bool]
    Description: NotRequired[str]

TestTypeInputTypeDef = TypedDict(
    "TestTypeInputTypeDef",
    {
        "Arn": NotRequired[str],
        "Type": NotRequired[ThirdPartyTypeType],
        "TypeName": NotRequired[str],
        "VersionId": NotRequired[str],
        "LogDeliveryBucket": NotRequired[str],
    },
)

class UpdateTerminationProtectionInputTypeDef(TypedDict):
    EnableTerminationProtection: bool
    StackName: str

class ValidateTemplateInputTypeDef(TypedDict):
    TemplateBody: NotRequired[str]
    TemplateURL: NotRequired[str]

WarningPropertyTypeDef = TypedDict(
    "WarningPropertyTypeDef",
    {
        "PropertyPath": NotRequired[str],
        "Required": NotRequired[bool],
        "Description": NotRequired[str],
    },
)

class StackSetOperationResultSummaryTypeDef(TypedDict):
    Account: NotRequired[str]
    Region: NotRequired[str]
    Status: NotRequired[StackSetOperationResultStatusType]
    StatusReason: NotRequired[str]
    AccountGateResult: NotRequired[AccountGateResultTypeDef]
    OrganizationalUnitId: NotRequired[str]

ActivateTypeInputTypeDef = TypedDict(
    "ActivateTypeInputTypeDef",
    {
        "Type": NotRequired[ThirdPartyTypeType],
        "PublicTypeArn": NotRequired[str],
        "PublisherId": NotRequired[str],
        "TypeName": NotRequired[str],
        "TypeNameAlias": NotRequired[str],
        "AutoUpdate": NotRequired[bool],
        "LoggingConfig": NotRequired[LoggingConfigTypeDef],
        "ExecutionRoleArn": NotRequired[str],
        "VersionBump": NotRequired[VersionBumpType],
        "MajorVersion": NotRequired[int],
    },
)
RegisterTypeInputTypeDef = TypedDict(
    "RegisterTypeInputTypeDef",
    {
        "TypeName": str,
        "SchemaHandlerPackage": str,
        "Type": NotRequired[RegistryTypeType],
        "LoggingConfig": NotRequired[LoggingConfigTypeDef],
        "ExecutionRoleArn": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
    },
)

class ActivateTypeOutputTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChangeSetOutputTypeDef(TypedDict):
    Id: str
    StackId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGeneratedTemplateOutputTypeDef(TypedDict):
    GeneratedTemplateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStackInstancesOutputTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStackOutputTypeDef(TypedDict):
    StackId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStackRefactorOutputTypeDef(TypedDict):
    StackRefactorId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStackSetOutputTypeDef(TypedDict):
    StackSetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteStackInstancesOutputTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountLimitsOutputTypeDef(TypedDict):
    AccountLimits: List[AccountLimitTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeOrganizationsAccessOutputTypeDef(TypedDict):
    Status: OrganizationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePublisherOutputTypeDef(TypedDict):
    PublisherId: str
    PublisherStatus: PublisherStatusType
    IdentityProvider: IdentityProviderType
    PublisherProfile: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStackDriftDetectionStatusOutputTypeDef(TypedDict):
    StackId: str
    StackDriftDetectionId: str
    StackDriftStatus: StackDriftStatusType
    DetectionStatus: StackDriftDetectionStatusType
    DetectionStatusReason: str
    DriftedStackResourceCount: int
    Timestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStackRefactorOutputTypeDef(TypedDict):
    Description: str
    StackRefactorId: str
    StackIds: List[str]
    ExecutionStatus: StackRefactorExecutionStatusType
    ExecutionStatusReason: str
    Status: StackRefactorStatusType
    StatusReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTypeRegistrationOutputTypeDef(TypedDict):
    ProgressStatus: RegistrationStatusType
    Description: str
    TypeArn: str
    TypeVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetectStackDriftOutputTypeDef(TypedDict):
    StackDriftDetectionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetectStackSetDriftOutputTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class EstimateTemplateCostOutputTypeDef(TypedDict):
    Url: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetGeneratedTemplateOutputTypeDef(TypedDict):
    Status: GeneratedTemplateStatusType
    TemplateBody: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetStackPolicyOutputTypeDef(TypedDict):
    StackPolicyBody: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTemplateOutputTypeDef(TypedDict):
    TemplateBody: Dict[str, Any]
    StagesAvailable: List[TemplateStageType]
    ResponseMetadata: ResponseMetadataTypeDef

class ImportStacksToStackSetOutputTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListImportsOutputTypeDef(TypedDict):
    Imports: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTypeRegistrationsOutputTypeDef(TypedDict):
    RegistrationTokenList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PublishTypeOutputTypeDef(TypedDict):
    PublicTypeArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterPublisherOutputTypeDef(TypedDict):
    PublisherId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterTypeOutputTypeDef(TypedDict):
    RegistrationToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RollbackStackOutputTypeDef(TypedDict):
    StackId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SetTypeConfigurationOutputTypeDef(TypedDict):
    ConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartResourceScanOutputTypeDef(TypedDict):
    ResourceScanId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestTypeOutputTypeDef(TypedDict):
    TypeVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGeneratedTemplateOutputTypeDef(TypedDict):
    GeneratedTemplateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStackInstancesOutputTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStackOutputTypeDef(TypedDict):
    StackId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStackSetOutputTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTerminationProtectionOutputTypeDef(TypedDict):
    StackId: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDescribeTypeConfigurationsErrorTypeDef(TypedDict):
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]
    TypeConfigurationIdentifier: NotRequired[TypeConfigurationIdentifierTypeDef]

class BatchDescribeTypeConfigurationsInputTypeDef(TypedDict):
    TypeConfigurationIdentifiers: Sequence[TypeConfigurationIdentifierTypeDef]

class ChangeSetHookTargetDetailsTypeDef(TypedDict):
    TargetType: NotRequired[Literal["RESOURCE"]]
    ResourceTargetDetails: NotRequired[ChangeSetHookResourceTargetDetailsTypeDef]

class ListChangeSetsOutputTypeDef(TypedDict):
    Summaries: List[ChangeSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class EstimateTemplateCostInputTypeDef(TypedDict):
    TemplateBody: NotRequired[str]
    TemplateURL: NotRequired[str]
    Parameters: NotRequired[Sequence[ParameterTypeDef]]

class CreateGeneratedTemplateInputTypeDef(TypedDict):
    GeneratedTemplateName: str
    Resources: NotRequired[Sequence[ResourceDefinitionTypeDef]]
    StackName: NotRequired[str]
    TemplateConfiguration: NotRequired[TemplateConfigurationTypeDef]

class UpdateGeneratedTemplateInputTypeDef(TypedDict):
    GeneratedTemplateName: str
    NewGeneratedTemplateName: NotRequired[str]
    AddResources: NotRequired[Sequence[ResourceDefinitionTypeDef]]
    RemoveResources: NotRequired[Sequence[str]]
    RefreshAllResources: NotRequired[bool]
    TemplateConfiguration: NotRequired[TemplateConfigurationTypeDef]

class CreateStackSetInputTypeDef(TypedDict):
    StackSetName: str
    Description: NotRequired[str]
    TemplateBody: NotRequired[str]
    TemplateURL: NotRequired[str]
    StackId: NotRequired[str]
    Parameters: NotRequired[Sequence[ParameterTypeDef]]
    Capabilities: NotRequired[Sequence[CapabilityType]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    AdministrationRoleARN: NotRequired[str]
    ExecutionRoleName: NotRequired[str]
    PermissionModel: NotRequired[PermissionModelsType]
    AutoDeployment: NotRequired[AutoDeploymentTypeDef]
    CallAs: NotRequired[CallAsType]
    ClientRequestToken: NotRequired[str]
    ManagedExecution: NotRequired[ManagedExecutionTypeDef]

class StackSetSummaryTypeDef(TypedDict):
    StackSetName: NotRequired[str]
    StackSetId: NotRequired[str]
    Description: NotRequired[str]
    Status: NotRequired[StackSetStatusType]
    AutoDeployment: NotRequired[AutoDeploymentTypeDef]
    PermissionModel: NotRequired[PermissionModelsType]
    DriftStatus: NotRequired[StackDriftStatusType]
    LastDriftCheckTimestamp: NotRequired[datetime]
    ManagedExecution: NotRequired[ManagedExecutionTypeDef]

DeploymentTargetsUnionTypeDef = Union[DeploymentTargetsTypeDef, DeploymentTargetsOutputTypeDef]

class DescribeAccountLimitsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeChangeSetInputPaginateTypeDef(TypedDict):
    ChangeSetName: str
    StackName: NotRequired[str]
    IncludePropertyValues: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeStackEventsInputPaginateTypeDef(TypedDict):
    StackName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeStacksInputPaginateTypeDef(TypedDict):
    StackName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListChangeSetsInputPaginateTypeDef(TypedDict):
    StackName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListExportsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGeneratedTemplatesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListImportsInputPaginateTypeDef(TypedDict):
    ExportName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceScanResourcesInputPaginateTypeDef(TypedDict):
    ResourceScanId: str
    ResourceIdentifier: NotRequired[str]
    ResourceTypePrefix: NotRequired[str]
    TagKey: NotRequired[str]
    TagValue: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceScansInputPaginateTypeDef(TypedDict):
    ScanTypeFilter: NotRequired[ScanTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStackRefactorActionsInputPaginateTypeDef(TypedDict):
    StackRefactorId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStackRefactorsInputPaginateTypeDef(TypedDict):
    ExecutionStatusFilter: NotRequired[Sequence[StackRefactorExecutionStatusType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStackResourcesInputPaginateTypeDef(TypedDict):
    StackName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStackSetOperationsInputPaginateTypeDef(TypedDict):
    StackSetName: str
    CallAs: NotRequired[CallAsType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStackSetsInputPaginateTypeDef(TypedDict):
    Status: NotRequired[StackSetStatusType]
    CallAs: NotRequired[CallAsType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStacksInputPaginateTypeDef(TypedDict):
    StackStatusFilter: NotRequired[Sequence[StackStatusType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeChangeSetInputWaitTypeDef(TypedDict):
    ChangeSetName: str
    StackName: NotRequired[str]
    NextToken: NotRequired[str]
    IncludePropertyValues: NotRequired[bool]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeStackRefactorInputWaitExtraTypeDef(TypedDict):
    StackRefactorId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeStackRefactorInputWaitTypeDef(TypedDict):
    StackRefactorId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeStacksInputWaitExtraExtraExtraExtraExtraTypeDef(TypedDict):
    StackName: NotRequired[str]
    NextToken: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeStacksInputWaitExtraExtraExtraExtraTypeDef(TypedDict):
    StackName: NotRequired[str]
    NextToken: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeStacksInputWaitExtraExtraExtraTypeDef(TypedDict):
    StackName: NotRequired[str]
    NextToken: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeStacksInputWaitExtraExtraTypeDef(TypedDict):
    StackName: NotRequired[str]
    NextToken: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeStacksInputWaitExtraTypeDef(TypedDict):
    StackName: NotRequired[str]
    NextToken: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeStacksInputWaitTypeDef(TypedDict):
    StackName: NotRequired[str]
    NextToken: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeTypeRegistrationInputWaitTypeDef(TypedDict):
    RegistrationToken: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeResourceScanOutputTypeDef(TypedDict):
    ResourceScanId: str
    Status: ResourceScanStatusType
    StatusReason: str
    StartTime: datetime
    EndTime: datetime
    PercentageCompleted: float
    ResourceTypes: List[str]
    ResourcesScanned: int
    ResourcesRead: int
    ScanFilters: List[ScanFilterOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStackEventsOutputTypeDef(TypedDict):
    StackEvents: List[StackEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

DescribeTypeOutputTypeDef = TypedDict(
    "DescribeTypeOutputTypeDef",
    {
        "Arn": str,
        "Type": RegistryTypeType,
        "TypeName": str,
        "DefaultVersionId": str,
        "IsDefaultVersion": bool,
        "TypeTestsStatus": TypeTestsStatusType,
        "TypeTestsStatusDescription": str,
        "Description": str,
        "Schema": str,
        "ProvisioningType": ProvisioningTypeType,
        "DeprecatedStatus": DeprecatedStatusType,
        "LoggingConfig": LoggingConfigTypeDef,
        "RequiredActivatedTypes": List[RequiredActivatedTypeTypeDef],
        "ExecutionRoleArn": str,
        "Visibility": VisibilityType,
        "SourceUrl": str,
        "DocumentationUrl": str,
        "LastUpdated": datetime,
        "TimeCreated": datetime,
        "ConfigurationSchema": str,
        "PublisherId": str,
        "OriginalTypeName": str,
        "OriginalTypeArn": str,
        "PublicVersionNumber": str,
        "LatestPublicVersion": str,
        "IsActivated": bool,
        "AutoUpdate": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListExportsOutputTypeDef(TypedDict):
    Exports: List[ExportTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetTemplateSummaryInputTypeDef(TypedDict):
    TemplateBody: NotRequired[str]
    TemplateURL: NotRequired[str]
    StackName: NotRequired[str]
    StackSetName: NotRequired[str]
    CallAs: NotRequired[CallAsType]
    TemplateSummaryConfig: NotRequired[TemplateSummaryConfigTypeDef]

class ListHookResultsOutputTypeDef(TypedDict):
    TargetType: ListHookResultsTargetTypeType
    TargetId: str
    HookResults: List[HookResultSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListGeneratedTemplatesOutputTypeDef(TypedDict):
    Summaries: List[TemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListResourceScanRelatedResourcesInputPaginateTypeDef(TypedDict):
    ResourceScanId: str
    Resources: Sequence[ScannedResourceIdentifierTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceScanRelatedResourcesInputTypeDef(TypedDict):
    ResourceScanId: str
    Resources: Sequence[ScannedResourceIdentifierTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListResourceScanRelatedResourcesOutputTypeDef(TypedDict):
    RelatedResources: List[ScannedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListResourceScanResourcesOutputTypeDef(TypedDict):
    Resources: List[ScannedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListResourceScansOutputTypeDef(TypedDict):
    ResourceScanSummaries: List[ResourceScanSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListStackInstancesInputPaginateTypeDef(TypedDict):
    StackSetName: str
    Filters: NotRequired[Sequence[StackInstanceFilterTypeDef]]
    StackInstanceAccount: NotRequired[str]
    StackInstanceRegion: NotRequired[str]
    CallAs: NotRequired[CallAsType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStackInstancesInputTypeDef(TypedDict):
    StackSetName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filters: NotRequired[Sequence[StackInstanceFilterTypeDef]]
    StackInstanceAccount: NotRequired[str]
    StackInstanceRegion: NotRequired[str]
    CallAs: NotRequired[CallAsType]

class ListStackRefactorsOutputTypeDef(TypedDict):
    StackRefactorSummaries: List[StackRefactorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListStackSetAutoDeploymentTargetsOutputTypeDef(TypedDict):
    Summaries: List[StackSetAutoDeploymentTargetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListStackSetOperationResultsInputPaginateTypeDef(TypedDict):
    StackSetName: str
    OperationId: str
    CallAs: NotRequired[CallAsType]
    Filters: NotRequired[Sequence[OperationResultFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStackSetOperationResultsInputTypeDef(TypedDict):
    StackSetName: str
    OperationId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    CallAs: NotRequired[CallAsType]
    Filters: NotRequired[Sequence[OperationResultFilterTypeDef]]

class ListTypeVersionsOutputTypeDef(TypedDict):
    TypeVersionSummaries: List[TypeVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

ListTypesInputPaginateTypeDef = TypedDict(
    "ListTypesInputPaginateTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
        "ProvisioningType": NotRequired[ProvisioningTypeType],
        "DeprecatedStatus": NotRequired[DeprecatedStatusType],
        "Type": NotRequired[RegistryTypeType],
        "Filters": NotRequired[TypeFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTypesInputTypeDef = TypedDict(
    "ListTypesInputTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
        "ProvisioningType": NotRequired[ProvisioningTypeType],
        "DeprecatedStatus": NotRequired[DeprecatedStatusType],
        "Type": NotRequired[RegistryTypeType],
        "Filters": NotRequired[TypeFiltersTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

class ListTypesOutputTypeDef(TypedDict):
    TypeSummaries: List[TypeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ParameterDeclarationTypeDef(TypedDict):
    ParameterKey: NotRequired[str]
    DefaultValue: NotRequired[str]
    ParameterType: NotRequired[str]
    NoEcho: NotRequired[bool]
    Description: NotRequired[str]
    ParameterConstraints: NotRequired[ParameterConstraintsTypeDef]

class StackInstanceResourceDriftsSummaryTypeDef(TypedDict):
    StackId: str
    LogicalResourceId: str
    ResourceType: str
    StackResourceDriftStatus: StackResourceDriftStatusType
    Timestamp: datetime
    PhysicalResourceId: NotRequired[str]
    PhysicalResourceIdContext: NotRequired[List[PhysicalResourceIdContextKeyValuePairTypeDef]]
    PropertyDifferences: NotRequired[List[PropertyDifferenceTypeDef]]

class StackResourceDriftTypeDef(TypedDict):
    StackId: str
    LogicalResourceId: str
    ResourceType: str
    StackResourceDriftStatus: StackResourceDriftStatusType
    Timestamp: datetime
    PhysicalResourceId: NotRequired[str]
    PhysicalResourceIdContext: NotRequired[List[PhysicalResourceIdContextKeyValuePairTypeDef]]
    ExpectedProperties: NotRequired[str]
    ActualProperties: NotRequired[str]
    PropertyDifferences: NotRequired[List[PropertyDifferenceTypeDef]]
    ModuleInfo: NotRequired[ModuleInfoTypeDef]

class ResourceChangeDetailTypeDef(TypedDict):
    Target: NotRequired[ResourceTargetDefinitionTypeDef]
    Evaluation: NotRequired[EvaluationTypeType]
    ChangeSource: NotRequired[ChangeSourceType]
    CausingEntity: NotRequired[str]

class ResourceMappingTypeDef(TypedDict):
    Source: ResourceLocationTypeDef
    Destination: ResourceLocationTypeDef

class RollbackConfigurationOutputTypeDef(TypedDict):
    RollbackTriggers: NotRequired[List[RollbackTriggerTypeDef]]
    MonitoringTimeInMinutes: NotRequired[int]

class RollbackConfigurationTypeDef(TypedDict):
    RollbackTriggers: NotRequired[Sequence[RollbackTriggerTypeDef]]
    MonitoringTimeInMinutes: NotRequired[int]

ScanFilterUnionTypeDef = Union[ScanFilterTypeDef, ScanFilterOutputTypeDef]

class StackSummaryTypeDef(TypedDict):
    StackName: str
    CreationTime: datetime
    StackStatus: StackStatusType
    StackId: NotRequired[str]
    TemplateDescription: NotRequired[str]
    LastUpdatedTime: NotRequired[datetime]
    DeletionTime: NotRequired[datetime]
    StackStatusReason: NotRequired[str]
    ParentId: NotRequired[str]
    RootId: NotRequired[str]
    DriftInformation: NotRequired[StackDriftInformationSummaryTypeDef]

class StackInstanceSummaryTypeDef(TypedDict):
    StackSetId: NotRequired[str]
    Region: NotRequired[str]
    Account: NotRequired[str]
    StackId: NotRequired[str]
    Status: NotRequired[StackInstanceStatusType]
    StatusReason: NotRequired[str]
    StackInstanceStatus: NotRequired[StackInstanceComprehensiveStatusTypeDef]
    OrganizationalUnitId: NotRequired[str]
    DriftStatus: NotRequired[StackDriftStatusType]
    LastDriftCheckTimestamp: NotRequired[datetime]
    LastOperationId: NotRequired[str]

class StackInstanceTypeDef(TypedDict):
    StackSetId: NotRequired[str]
    Region: NotRequired[str]
    Account: NotRequired[str]
    StackId: NotRequired[str]
    ParameterOverrides: NotRequired[List[ParameterTypeDef]]
    Status: NotRequired[StackInstanceStatusType]
    StackInstanceStatus: NotRequired[StackInstanceComprehensiveStatusTypeDef]
    StatusReason: NotRequired[str]
    OrganizationalUnitId: NotRequired[str]
    DriftStatus: NotRequired[StackDriftStatusType]
    LastDriftCheckTimestamp: NotRequired[datetime]
    LastOperationId: NotRequired[str]

class StackResourceDetailTypeDef(TypedDict):
    LogicalResourceId: str
    ResourceType: str
    LastUpdatedTimestamp: datetime
    ResourceStatus: ResourceStatusType
    StackName: NotRequired[str]
    StackId: NotRequired[str]
    PhysicalResourceId: NotRequired[str]
    ResourceStatusReason: NotRequired[str]
    Description: NotRequired[str]
    Metadata: NotRequired[str]
    DriftInformation: NotRequired[StackResourceDriftInformationTypeDef]
    ModuleInfo: NotRequired[ModuleInfoTypeDef]

class StackResourceTypeDef(TypedDict):
    LogicalResourceId: str
    ResourceType: str
    Timestamp: datetime
    ResourceStatus: ResourceStatusType
    StackName: NotRequired[str]
    StackId: NotRequired[str]
    PhysicalResourceId: NotRequired[str]
    ResourceStatusReason: NotRequired[str]
    Description: NotRequired[str]
    DriftInformation: NotRequired[StackResourceDriftInformationTypeDef]
    ModuleInfo: NotRequired[ModuleInfoTypeDef]

class StackResourceSummaryTypeDef(TypedDict):
    LogicalResourceId: str
    ResourceType: str
    LastUpdatedTimestamp: datetime
    ResourceStatus: ResourceStatusType
    PhysicalResourceId: NotRequired[str]
    ResourceStatusReason: NotRequired[str]
    DriftInformation: NotRequired[StackResourceDriftInformationSummaryTypeDef]
    ModuleInfo: NotRequired[ModuleInfoTypeDef]

class StackSetTypeDef(TypedDict):
    StackSetName: NotRequired[str]
    StackSetId: NotRequired[str]
    Description: NotRequired[str]
    Status: NotRequired[StackSetStatusType]
    TemplateBody: NotRequired[str]
    Parameters: NotRequired[List[ParameterTypeDef]]
    Capabilities: NotRequired[List[CapabilityType]]
    Tags: NotRequired[List[TagTypeDef]]
    StackSetARN: NotRequired[str]
    AdministrationRoleARN: NotRequired[str]
    ExecutionRoleName: NotRequired[str]
    StackSetDriftDetectionDetails: NotRequired[StackSetDriftDetectionDetailsTypeDef]
    AutoDeployment: NotRequired[AutoDeploymentTypeDef]
    PermissionModel: NotRequired[PermissionModelsType]
    OrganizationalUnitIds: NotRequired[List[str]]
    ManagedExecution: NotRequired[ManagedExecutionTypeDef]
    Regions: NotRequired[List[str]]

StackSetOperationPreferencesUnionTypeDef = Union[
    StackSetOperationPreferencesTypeDef, StackSetOperationPreferencesOutputTypeDef
]

class StackSetOperationSummaryTypeDef(TypedDict):
    OperationId: NotRequired[str]
    Action: NotRequired[StackSetOperationActionType]
    Status: NotRequired[StackSetOperationStatusType]
    CreationTimestamp: NotRequired[datetime]
    EndTimestamp: NotRequired[datetime]
    StatusReason: NotRequired[str]
    StatusDetails: NotRequired[StackSetOperationStatusDetailsTypeDef]
    OperationPreferences: NotRequired[StackSetOperationPreferencesOutputTypeDef]

class StackSetOperationTypeDef(TypedDict):
    OperationId: NotRequired[str]
    StackSetId: NotRequired[str]
    Action: NotRequired[StackSetOperationActionType]
    Status: NotRequired[StackSetOperationStatusType]
    OperationPreferences: NotRequired[StackSetOperationPreferencesOutputTypeDef]
    RetainStacks: NotRequired[bool]
    AdministrationRoleARN: NotRequired[str]
    ExecutionRoleName: NotRequired[str]
    CreationTimestamp: NotRequired[datetime]
    EndTimestamp: NotRequired[datetime]
    DeploymentTargets: NotRequired[DeploymentTargetsOutputTypeDef]
    StackSetDriftDetectionDetails: NotRequired[StackSetDriftDetectionDetailsTypeDef]
    StatusReason: NotRequired[str]
    StatusDetails: NotRequired[StackSetOperationStatusDetailsTypeDef]

class ValidateTemplateOutputTypeDef(TypedDict):
    Parameters: List[TemplateParameterTypeDef]
    Description: str
    Capabilities: List[CapabilityType]
    CapabilitiesReason: str
    DeclaredTransforms: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

WarningDetailTypeDef = TypedDict(
    "WarningDetailTypeDef",
    {
        "Type": NotRequired[WarningTypeType],
        "Properties": NotRequired[List[WarningPropertyTypeDef]],
    },
)

class ListStackSetOperationResultsOutputTypeDef(TypedDict):
    Summaries: List[StackSetOperationResultSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class BatchDescribeTypeConfigurationsOutputTypeDef(TypedDict):
    Errors: List[BatchDescribeTypeConfigurationsErrorTypeDef]
    UnprocessedTypeConfigurations: List[TypeConfigurationIdentifierTypeDef]
    TypeConfigurations: List[TypeConfigurationDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ChangeSetHookTypeDef(TypedDict):
    InvocationPoint: NotRequired[Literal["PRE_PROVISION"]]
    FailureMode: NotRequired[HookFailureModeType]
    TypeName: NotRequired[str]
    TypeVersionId: NotRequired[str]
    TypeConfigurationVersionId: NotRequired[str]
    TargetDetails: NotRequired[ChangeSetHookTargetDetailsTypeDef]

class ListStackSetsOutputTypeDef(TypedDict):
    Summaries: List[StackSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetTemplateSummaryOutputTypeDef(TypedDict):
    Parameters: List[ParameterDeclarationTypeDef]
    Description: str
    Capabilities: List[CapabilityType]
    CapabilitiesReason: str
    ResourceTypes: List[str]
    Version: str
    Metadata: str
    DeclaredTransforms: List[str]
    ResourceIdentifierSummaries: List[ResourceIdentifierSummaryTypeDef]
    Warnings: WarningsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListStackInstanceResourceDriftsOutputTypeDef(TypedDict):
    Summaries: List[StackInstanceResourceDriftsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeStackResourceDriftsOutputTypeDef(TypedDict):
    StackResourceDrifts: List[StackResourceDriftTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DetectStackResourceDriftOutputTypeDef(TypedDict):
    StackResourceDrift: StackResourceDriftTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceChangeTypeDef(TypedDict):
    PolicyAction: NotRequired[PolicyActionType]
    Action: NotRequired[ChangeActionType]
    LogicalResourceId: NotRequired[str]
    PhysicalResourceId: NotRequired[str]
    ResourceType: NotRequired[str]
    Replacement: NotRequired[ReplacementType]
    Scope: NotRequired[List[ResourceAttributeType]]
    Details: NotRequired[List[ResourceChangeDetailTypeDef]]
    ChangeSetId: NotRequired[str]
    ModuleInfo: NotRequired[ModuleInfoTypeDef]
    BeforeContext: NotRequired[str]
    AfterContext: NotRequired[str]

class CreateStackRefactorInputTypeDef(TypedDict):
    StackDefinitions: Sequence[StackDefinitionTypeDef]
    Description: NotRequired[str]
    EnableStackCreation: NotRequired[bool]
    ResourceMappings: NotRequired[Sequence[ResourceMappingTypeDef]]

class StackRefactorActionTypeDef(TypedDict):
    Action: NotRequired[StackRefactorActionTypeType]
    Entity: NotRequired[StackRefactorActionEntityType]
    PhysicalResourceId: NotRequired[str]
    ResourceIdentifier: NotRequired[str]
    Description: NotRequired[str]
    Detection: NotRequired[StackRefactorDetectionType]
    DetectionReason: NotRequired[str]
    TagResources: NotRequired[List[TagTypeDef]]
    UntagResources: NotRequired[List[str]]
    ResourceMapping: NotRequired[ResourceMappingTypeDef]

class StackTypeDef(TypedDict):
    StackName: str
    CreationTime: datetime
    StackStatus: StackStatusType
    StackId: NotRequired[str]
    ChangeSetId: NotRequired[str]
    Description: NotRequired[str]
    Parameters: NotRequired[List[ParameterTypeDef]]
    DeletionTime: NotRequired[datetime]
    LastUpdatedTime: NotRequired[datetime]
    RollbackConfiguration: NotRequired[RollbackConfigurationOutputTypeDef]
    StackStatusReason: NotRequired[str]
    DisableRollback: NotRequired[bool]
    NotificationARNs: NotRequired[List[str]]
    TimeoutInMinutes: NotRequired[int]
    Capabilities: NotRequired[List[CapabilityType]]
    Outputs: NotRequired[List[OutputTypeDef]]
    RoleARN: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]
    EnableTerminationProtection: NotRequired[bool]
    ParentId: NotRequired[str]
    RootId: NotRequired[str]
    DriftInformation: NotRequired[StackDriftInformationTypeDef]
    RetainExceptOnCreate: NotRequired[bool]
    DeletionMode: NotRequired[DeletionModeType]
    DetailedStatus: NotRequired[DetailedStatusType]

RollbackConfigurationUnionTypeDef = Union[
    RollbackConfigurationTypeDef, RollbackConfigurationOutputTypeDef
]

class StartResourceScanInputTypeDef(TypedDict):
    ClientRequestToken: NotRequired[str]
    ScanFilters: NotRequired[Sequence[ScanFilterUnionTypeDef]]

class ListStacksOutputTypeDef(TypedDict):
    StackSummaries: List[StackSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListStackInstancesOutputTypeDef(TypedDict):
    Summaries: List[StackInstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeStackInstanceOutputTypeDef(TypedDict):
    StackInstance: StackInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStackResourceOutputTypeDef(TypedDict):
    StackResourceDetail: StackResourceDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStackResourcesOutputTypeDef(TypedDict):
    StackResources: List[StackResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListStackResourcesOutputTypeDef(TypedDict):
    StackResourceSummaries: List[StackResourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeStackSetOutputTypeDef(TypedDict):
    StackSet: StackSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStackInstancesInputTypeDef(TypedDict):
    StackSetName: str
    Regions: Sequence[str]
    Accounts: NotRequired[Sequence[str]]
    DeploymentTargets: NotRequired[DeploymentTargetsUnionTypeDef]
    ParameterOverrides: NotRequired[Sequence[ParameterTypeDef]]
    OperationPreferences: NotRequired[StackSetOperationPreferencesUnionTypeDef]
    OperationId: NotRequired[str]
    CallAs: NotRequired[CallAsType]

class DeleteStackInstancesInputTypeDef(TypedDict):
    StackSetName: str
    Regions: Sequence[str]
    RetainStacks: bool
    Accounts: NotRequired[Sequence[str]]
    DeploymentTargets: NotRequired[DeploymentTargetsUnionTypeDef]
    OperationPreferences: NotRequired[StackSetOperationPreferencesUnionTypeDef]
    OperationId: NotRequired[str]
    CallAs: NotRequired[CallAsType]

class DetectStackSetDriftInputTypeDef(TypedDict):
    StackSetName: str
    OperationPreferences: NotRequired[StackSetOperationPreferencesUnionTypeDef]
    OperationId: NotRequired[str]
    CallAs: NotRequired[CallAsType]

class ImportStacksToStackSetInputTypeDef(TypedDict):
    StackSetName: str
    StackIds: NotRequired[Sequence[str]]
    StackIdsUrl: NotRequired[str]
    OrganizationalUnitIds: NotRequired[Sequence[str]]
    OperationPreferences: NotRequired[StackSetOperationPreferencesUnionTypeDef]
    OperationId: NotRequired[str]
    CallAs: NotRequired[CallAsType]

class UpdateStackInstancesInputTypeDef(TypedDict):
    StackSetName: str
    Regions: Sequence[str]
    Accounts: NotRequired[Sequence[str]]
    DeploymentTargets: NotRequired[DeploymentTargetsUnionTypeDef]
    ParameterOverrides: NotRequired[Sequence[ParameterTypeDef]]
    OperationPreferences: NotRequired[StackSetOperationPreferencesUnionTypeDef]
    OperationId: NotRequired[str]
    CallAs: NotRequired[CallAsType]

class UpdateStackSetInputTypeDef(TypedDict):
    StackSetName: str
    Description: NotRequired[str]
    TemplateBody: NotRequired[str]
    TemplateURL: NotRequired[str]
    UsePreviousTemplate: NotRequired[bool]
    Parameters: NotRequired[Sequence[ParameterTypeDef]]
    Capabilities: NotRequired[Sequence[CapabilityType]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    OperationPreferences: NotRequired[StackSetOperationPreferencesUnionTypeDef]
    AdministrationRoleARN: NotRequired[str]
    ExecutionRoleName: NotRequired[str]
    DeploymentTargets: NotRequired[DeploymentTargetsUnionTypeDef]
    PermissionModel: NotRequired[PermissionModelsType]
    AutoDeployment: NotRequired[AutoDeploymentTypeDef]
    OperationId: NotRequired[str]
    Accounts: NotRequired[Sequence[str]]
    Regions: NotRequired[Sequence[str]]
    CallAs: NotRequired[CallAsType]
    ManagedExecution: NotRequired[ManagedExecutionTypeDef]

class ListStackSetOperationsOutputTypeDef(TypedDict):
    Summaries: List[StackSetOperationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeStackSetOperationOutputTypeDef(TypedDict):
    StackSetOperation: StackSetOperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceDetailTypeDef(TypedDict):
    ResourceType: NotRequired[str]
    LogicalResourceId: NotRequired[str]
    ResourceIdentifier: NotRequired[Dict[str, str]]
    ResourceStatus: NotRequired[GeneratedTemplateResourceStatusType]
    ResourceStatusReason: NotRequired[str]
    Warnings: NotRequired[List[WarningDetailTypeDef]]

class DescribeChangeSetHooksOutputTypeDef(TypedDict):
    ChangeSetId: str
    ChangeSetName: str
    Hooks: List[ChangeSetHookTypeDef]
    Status: ChangeSetHooksStatusType
    StackId: str
    StackName: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

ChangeTypeDef = TypedDict(
    "ChangeTypeDef",
    {
        "Type": NotRequired[Literal["Resource"]],
        "HookInvocationCount": NotRequired[int],
        "ResourceChange": NotRequired[ResourceChangeTypeDef],
    },
)

class ListStackRefactorActionsOutputTypeDef(TypedDict):
    StackRefactorActions: List[StackRefactorActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeStacksOutputTypeDef(TypedDict):
    Stacks: List[StackTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateChangeSetInputTypeDef(TypedDict):
    StackName: str
    ChangeSetName: str
    TemplateBody: NotRequired[str]
    TemplateURL: NotRequired[str]
    UsePreviousTemplate: NotRequired[bool]
    Parameters: NotRequired[Sequence[ParameterTypeDef]]
    Capabilities: NotRequired[Sequence[CapabilityType]]
    ResourceTypes: NotRequired[Sequence[str]]
    RoleARN: NotRequired[str]
    RollbackConfiguration: NotRequired[RollbackConfigurationUnionTypeDef]
    NotificationARNs: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    ClientToken: NotRequired[str]
    Description: NotRequired[str]
    ChangeSetType: NotRequired[ChangeSetTypeType]
    ResourcesToImport: NotRequired[Sequence[ResourceToImportTypeDef]]
    IncludeNestedStacks: NotRequired[bool]
    OnStackFailure: NotRequired[OnStackFailureType]
    ImportExistingResources: NotRequired[bool]

class CreateStackInputServiceResourceCreateStackTypeDef(TypedDict):
    StackName: str
    TemplateBody: NotRequired[str]
    TemplateURL: NotRequired[str]
    Parameters: NotRequired[Sequence[ParameterTypeDef]]
    DisableRollback: NotRequired[bool]
    RollbackConfiguration: NotRequired[RollbackConfigurationUnionTypeDef]
    TimeoutInMinutes: NotRequired[int]
    NotificationARNs: NotRequired[Sequence[str]]
    Capabilities: NotRequired[Sequence[CapabilityType]]
    ResourceTypes: NotRequired[Sequence[str]]
    RoleARN: NotRequired[str]
    OnFailure: NotRequired[OnFailureType]
    StackPolicyBody: NotRequired[str]
    StackPolicyURL: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    ClientRequestToken: NotRequired[str]
    EnableTerminationProtection: NotRequired[bool]
    RetainExceptOnCreate: NotRequired[bool]

class CreateStackInputTypeDef(TypedDict):
    StackName: str
    TemplateBody: NotRequired[str]
    TemplateURL: NotRequired[str]
    Parameters: NotRequired[Sequence[ParameterTypeDef]]
    DisableRollback: NotRequired[bool]
    RollbackConfiguration: NotRequired[RollbackConfigurationUnionTypeDef]
    TimeoutInMinutes: NotRequired[int]
    NotificationARNs: NotRequired[Sequence[str]]
    Capabilities: NotRequired[Sequence[CapabilityType]]
    ResourceTypes: NotRequired[Sequence[str]]
    RoleARN: NotRequired[str]
    OnFailure: NotRequired[OnFailureType]
    StackPolicyBody: NotRequired[str]
    StackPolicyURL: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    ClientRequestToken: NotRequired[str]
    EnableTerminationProtection: NotRequired[bool]
    RetainExceptOnCreate: NotRequired[bool]

class UpdateStackInputStackUpdateTypeDef(TypedDict):
    TemplateBody: NotRequired[str]
    TemplateURL: NotRequired[str]
    UsePreviousTemplate: NotRequired[bool]
    StackPolicyDuringUpdateBody: NotRequired[str]
    StackPolicyDuringUpdateURL: NotRequired[str]
    Parameters: NotRequired[Sequence[ParameterTypeDef]]
    Capabilities: NotRequired[Sequence[CapabilityType]]
    ResourceTypes: NotRequired[Sequence[str]]
    RoleARN: NotRequired[str]
    RollbackConfiguration: NotRequired[RollbackConfigurationUnionTypeDef]
    StackPolicyBody: NotRequired[str]
    StackPolicyURL: NotRequired[str]
    NotificationARNs: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    DisableRollback: NotRequired[bool]
    ClientRequestToken: NotRequired[str]
    RetainExceptOnCreate: NotRequired[bool]

class UpdateStackInputTypeDef(TypedDict):
    StackName: str
    TemplateBody: NotRequired[str]
    TemplateURL: NotRequired[str]
    UsePreviousTemplate: NotRequired[bool]
    StackPolicyDuringUpdateBody: NotRequired[str]
    StackPolicyDuringUpdateURL: NotRequired[str]
    Parameters: NotRequired[Sequence[ParameterTypeDef]]
    Capabilities: NotRequired[Sequence[CapabilityType]]
    ResourceTypes: NotRequired[Sequence[str]]
    RoleARN: NotRequired[str]
    RollbackConfiguration: NotRequired[RollbackConfigurationUnionTypeDef]
    StackPolicyBody: NotRequired[str]
    StackPolicyURL: NotRequired[str]
    NotificationARNs: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    DisableRollback: NotRequired[bool]
    ClientRequestToken: NotRequired[str]
    RetainExceptOnCreate: NotRequired[bool]

class DescribeGeneratedTemplateOutputTypeDef(TypedDict):
    GeneratedTemplateId: str
    GeneratedTemplateName: str
    Resources: List[ResourceDetailTypeDef]
    Status: GeneratedTemplateStatusType
    StatusReason: str
    CreationTime: datetime
    LastUpdatedTime: datetime
    Progress: TemplateProgressTypeDef
    StackId: str
    TemplateConfiguration: TemplateConfigurationTypeDef
    TotalWarnings: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChangeSetOutputTypeDef(TypedDict):
    ChangeSetName: str
    ChangeSetId: str
    StackId: str
    StackName: str
    Description: str
    Parameters: List[ParameterTypeDef]
    CreationTime: datetime
    ExecutionStatus: ExecutionStatusType
    Status: ChangeSetStatusType
    StatusReason: str
    NotificationARNs: List[str]
    RollbackConfiguration: RollbackConfigurationOutputTypeDef
    Capabilities: List[CapabilityType]
    Tags: List[TagTypeDef]
    Changes: List[ChangeTypeDef]
    IncludeNestedStacks: bool
    ParentChangeSetId: str
    RootChangeSetId: str
    OnStackFailure: OnStackFailureType
    ImportExistingResources: bool
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
