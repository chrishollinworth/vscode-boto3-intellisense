"""
Type annotations for cloudformation service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudformation.type_defs import AccountGateResultTypeDef

    data: AccountGateResultTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AccountGateStatusType,
    CallAsType,
    CapabilityType,
    CategoryType,
    ChangeActionType,
    ChangeSetStatusType,
    ChangeSetTypeType,
    ChangeSourceType,
    DeprecatedStatusType,
    DifferenceTypeType,
    EvaluationTypeType,
    ExecutionStatusType,
    HandlerErrorCodeType,
    IdentityProviderType,
    OnFailureType,
    OperationStatusType,
    PermissionModelsType,
    ProvisioningTypeType,
    PublisherStatusType,
    RegionConcurrencyTypeType,
    RegistrationStatusType,
    RegistryTypeType,
    ReplacementType,
    RequiresRecreationType,
    ResourceAttributeType,
    ResourceSignalStatusType,
    ResourceStatusType,
    StackDriftDetectionStatusType,
    StackDriftStatusType,
    StackInstanceDetailedStatusType,
    StackInstanceStatusType,
    StackResourceDriftStatusType,
    StackSetDriftDetectionStatusType,
    StackSetDriftStatusType,
    StackSetOperationActionType,
    StackSetOperationResultStatusType,
    StackSetOperationStatusType,
    StackSetStatusType,
    StackStatusType,
    TemplateStageType,
    ThirdPartyTypeType,
    TypeTestsStatusType,
    VersionBumpType,
    VisibilityType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountGateResultTypeDef",
    "AccountLimitTypeDef",
    "ActivateTypeInputRequestTypeDef",
    "ActivateTypeOutputTypeDef",
    "AutoDeploymentTypeDef",
    "BatchDescribeTypeConfigurationsErrorTypeDef",
    "BatchDescribeTypeConfigurationsInputRequestTypeDef",
    "BatchDescribeTypeConfigurationsOutputTypeDef",
    "CancelUpdateStackInputRequestTypeDef",
    "CancelUpdateStackInputStackTypeDef",
    "ChangeSetSummaryTypeDef",
    "ChangeTypeDef",
    "ContinueUpdateRollbackInputRequestTypeDef",
    "CreateChangeSetInputRequestTypeDef",
    "CreateChangeSetOutputTypeDef",
    "CreateStackInputRequestTypeDef",
    "CreateStackInputServiceResourceTypeDef",
    "CreateStackInstancesInputRequestTypeDef",
    "CreateStackInstancesOutputTypeDef",
    "CreateStackOutputTypeDef",
    "CreateStackSetInputRequestTypeDef",
    "CreateStackSetOutputTypeDef",
    "DeactivateTypeInputRequestTypeDef",
    "DeleteChangeSetInputRequestTypeDef",
    "DeleteStackInputRequestTypeDef",
    "DeleteStackInputStackTypeDef",
    "DeleteStackInstancesInputRequestTypeDef",
    "DeleteStackInstancesOutputTypeDef",
    "DeleteStackSetInputRequestTypeDef",
    "DeploymentTargetsTypeDef",
    "DeregisterTypeInputRequestTypeDef",
    "DescribeAccountLimitsInputRequestTypeDef",
    "DescribeAccountLimitsOutputTypeDef",
    "DescribeChangeSetInputRequestTypeDef",
    "DescribeChangeSetOutputTypeDef",
    "DescribePublisherInputRequestTypeDef",
    "DescribePublisherOutputTypeDef",
    "DescribeStackDriftDetectionStatusInputRequestTypeDef",
    "DescribeStackDriftDetectionStatusOutputTypeDef",
    "DescribeStackEventsInputRequestTypeDef",
    "DescribeStackEventsOutputTypeDef",
    "DescribeStackInstanceInputRequestTypeDef",
    "DescribeStackInstanceOutputTypeDef",
    "DescribeStackResourceDriftsInputRequestTypeDef",
    "DescribeStackResourceDriftsOutputTypeDef",
    "DescribeStackResourceInputRequestTypeDef",
    "DescribeStackResourceOutputTypeDef",
    "DescribeStackResourcesInputRequestTypeDef",
    "DescribeStackResourcesOutputTypeDef",
    "DescribeStackSetInputRequestTypeDef",
    "DescribeStackSetOperationInputRequestTypeDef",
    "DescribeStackSetOperationOutputTypeDef",
    "DescribeStackSetOutputTypeDef",
    "DescribeStacksInputRequestTypeDef",
    "DescribeStacksOutputTypeDef",
    "DescribeTypeInputRequestTypeDef",
    "DescribeTypeOutputTypeDef",
    "DescribeTypeRegistrationInputRequestTypeDef",
    "DescribeTypeRegistrationOutputTypeDef",
    "DetectStackDriftInputRequestTypeDef",
    "DetectStackDriftOutputTypeDef",
    "DetectStackResourceDriftInputRequestTypeDef",
    "DetectStackResourceDriftOutputTypeDef",
    "DetectStackSetDriftInputRequestTypeDef",
    "DetectStackSetDriftOutputTypeDef",
    "EstimateTemplateCostInputRequestTypeDef",
    "EstimateTemplateCostOutputTypeDef",
    "ExecuteChangeSetInputRequestTypeDef",
    "ExportTypeDef",
    "GetStackPolicyInputRequestTypeDef",
    "GetStackPolicyOutputTypeDef",
    "GetTemplateInputRequestTypeDef",
    "GetTemplateOutputTypeDef",
    "GetTemplateSummaryInputRequestTypeDef",
    "GetTemplateSummaryOutputTypeDef",
    "ImportStacksToStackSetInputRequestTypeDef",
    "ImportStacksToStackSetOutputTypeDef",
    "ListChangeSetsInputRequestTypeDef",
    "ListChangeSetsOutputTypeDef",
    "ListExportsInputRequestTypeDef",
    "ListExportsOutputTypeDef",
    "ListImportsInputRequestTypeDef",
    "ListImportsOutputTypeDef",
    "ListStackInstancesInputRequestTypeDef",
    "ListStackInstancesOutputTypeDef",
    "ListStackResourcesInputRequestTypeDef",
    "ListStackResourcesOutputTypeDef",
    "ListStackSetOperationResultsInputRequestTypeDef",
    "ListStackSetOperationResultsOutputTypeDef",
    "ListStackSetOperationsInputRequestTypeDef",
    "ListStackSetOperationsOutputTypeDef",
    "ListStackSetsInputRequestTypeDef",
    "ListStackSetsOutputTypeDef",
    "ListStacksInputRequestTypeDef",
    "ListStacksOutputTypeDef",
    "ListTypeRegistrationsInputRequestTypeDef",
    "ListTypeRegistrationsOutputTypeDef",
    "ListTypeVersionsInputRequestTypeDef",
    "ListTypeVersionsOutputTypeDef",
    "ListTypesInputRequestTypeDef",
    "ListTypesOutputTypeDef",
    "LoggingConfigTypeDef",
    "ModuleInfoTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterConstraintsTypeDef",
    "ParameterDeclarationTypeDef",
    "ParameterTypeDef",
    "PhysicalResourceIdContextKeyValuePairTypeDef",
    "PropertyDifferenceTypeDef",
    "PublishTypeInputRequestTypeDef",
    "PublishTypeOutputTypeDef",
    "RecordHandlerProgressInputRequestTypeDef",
    "RegisterPublisherInputRequestTypeDef",
    "RegisterPublisherOutputTypeDef",
    "RegisterTypeInputRequestTypeDef",
    "RegisterTypeOutputTypeDef",
    "RequiredActivatedTypeTypeDef",
    "ResourceChangeDetailTypeDef",
    "ResourceChangeTypeDef",
    "ResourceIdentifierSummaryTypeDef",
    "ResourceTargetDefinitionTypeDef",
    "ResourceToImportTypeDef",
    "ResponseMetadataTypeDef",
    "RollbackConfigurationTypeDef",
    "RollbackTriggerTypeDef",
    "ServiceResourceEventRequestTypeDef",
    "ServiceResourceStackRequestTypeDef",
    "ServiceResourceStackResourceRequestTypeDef",
    "ServiceResourceStackResourceSummaryRequestTypeDef",
    "SetStackPolicyInputRequestTypeDef",
    "SetTypeConfigurationInputRequestTypeDef",
    "SetTypeConfigurationOutputTypeDef",
    "SetTypeDefaultVersionInputRequestTypeDef",
    "SignalResourceInputRequestTypeDef",
    "StackDriftInformationSummaryTypeDef",
    "StackDriftInformationTypeDef",
    "StackEventTypeDef",
    "StackInstanceComprehensiveStatusTypeDef",
    "StackInstanceFilterTypeDef",
    "StackInstanceSummaryTypeDef",
    "StackInstanceTypeDef",
    "StackResourceDetailTypeDef",
    "StackResourceDriftInformationSummaryTypeDef",
    "StackResourceDriftInformationTypeDef",
    "StackResourceDriftTypeDef",
    "StackResourceRequestTypeDef",
    "StackResourceSummaryTypeDef",
    "StackResourceTypeDef",
    "StackSetDriftDetectionDetailsTypeDef",
    "StackSetOperationPreferencesTypeDef",
    "StackSetOperationResultSummaryTypeDef",
    "StackSetOperationSummaryTypeDef",
    "StackSetOperationTypeDef",
    "StackSetSummaryTypeDef",
    "StackSetTypeDef",
    "StackSummaryTypeDef",
    "StackTypeDef",
    "StopStackSetOperationInputRequestTypeDef",
    "TagTypeDef",
    "TemplateParameterTypeDef",
    "TestTypeInputRequestTypeDef",
    "TestTypeOutputTypeDef",
    "TypeConfigurationDetailsTypeDef",
    "TypeConfigurationIdentifierTypeDef",
    "TypeFiltersTypeDef",
    "TypeSummaryTypeDef",
    "TypeVersionSummaryTypeDef",
    "UpdateStackInputRequestTypeDef",
    "UpdateStackInputStackTypeDef",
    "UpdateStackInstancesInputRequestTypeDef",
    "UpdateStackInstancesOutputTypeDef",
    "UpdateStackOutputTypeDef",
    "UpdateStackSetInputRequestTypeDef",
    "UpdateStackSetOutputTypeDef",
    "UpdateTerminationProtectionInputRequestTypeDef",
    "UpdateTerminationProtectionOutputTypeDef",
    "ValidateTemplateInputRequestTypeDef",
    "ValidateTemplateOutputTypeDef",
    "WaiterConfigTypeDef",
)

AccountGateResultTypeDef = TypedDict(
    "AccountGateResultTypeDef",
    {
        "Status": AccountGateStatusType,
        "StatusReason": str,
    },
    total=False,
)

AccountLimitTypeDef = TypedDict(
    "AccountLimitTypeDef",
    {
        "Name": str,
        "Value": int,
    },
    total=False,
)

ActivateTypeInputRequestTypeDef = TypedDict(
    "ActivateTypeInputRequestTypeDef",
    {
        "Type": ThirdPartyTypeType,
        "PublicTypeArn": str,
        "PublisherId": str,
        "TypeName": str,
        "TypeNameAlias": str,
        "AutoUpdate": bool,
        "LoggingConfig": "LoggingConfigTypeDef",
        "ExecutionRoleArn": str,
        "VersionBump": VersionBumpType,
        "MajorVersion": int,
    },
    total=False,
)

ActivateTypeOutputTypeDef = TypedDict(
    "ActivateTypeOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AutoDeploymentTypeDef = TypedDict(
    "AutoDeploymentTypeDef",
    {
        "Enabled": bool,
        "RetainStacksOnAccountRemoval": bool,
    },
    total=False,
)

BatchDescribeTypeConfigurationsErrorTypeDef = TypedDict(
    "BatchDescribeTypeConfigurationsErrorTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
        "TypeConfigurationIdentifier": "TypeConfigurationIdentifierTypeDef",
    },
    total=False,
)

BatchDescribeTypeConfigurationsInputRequestTypeDef = TypedDict(
    "BatchDescribeTypeConfigurationsInputRequestTypeDef",
    {
        "TypeConfigurationIdentifiers": List["TypeConfigurationIdentifierTypeDef"],
    },
)

BatchDescribeTypeConfigurationsOutputTypeDef = TypedDict(
    "BatchDescribeTypeConfigurationsOutputTypeDef",
    {
        "Errors": List["BatchDescribeTypeConfigurationsErrorTypeDef"],
        "UnprocessedTypeConfigurations": List["TypeConfigurationIdentifierTypeDef"],
        "TypeConfigurations": List["TypeConfigurationDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCancelUpdateStackInputRequestTypeDef = TypedDict(
    "_RequiredCancelUpdateStackInputRequestTypeDef",
    {
        "StackName": str,
    },
)
_OptionalCancelUpdateStackInputRequestTypeDef = TypedDict(
    "_OptionalCancelUpdateStackInputRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

class CancelUpdateStackInputRequestTypeDef(
    _RequiredCancelUpdateStackInputRequestTypeDef, _OptionalCancelUpdateStackInputRequestTypeDef
):
    pass

CancelUpdateStackInputStackTypeDef = TypedDict(
    "CancelUpdateStackInputStackTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

ChangeSetSummaryTypeDef = TypedDict(
    "ChangeSetSummaryTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "ChangeSetId": str,
        "ChangeSetName": str,
        "ExecutionStatus": ExecutionStatusType,
        "Status": ChangeSetStatusType,
        "StatusReason": str,
        "CreationTime": datetime,
        "Description": str,
        "IncludeNestedStacks": bool,
        "ParentChangeSetId": str,
        "RootChangeSetId": str,
    },
    total=False,
)

ChangeTypeDef = TypedDict(
    "ChangeTypeDef",
    {
        "Type": Literal["Resource"],
        "ResourceChange": "ResourceChangeTypeDef",
    },
    total=False,
)

_RequiredContinueUpdateRollbackInputRequestTypeDef = TypedDict(
    "_RequiredContinueUpdateRollbackInputRequestTypeDef",
    {
        "StackName": str,
    },
)
_OptionalContinueUpdateRollbackInputRequestTypeDef = TypedDict(
    "_OptionalContinueUpdateRollbackInputRequestTypeDef",
    {
        "RoleARN": str,
        "ResourcesToSkip": List[str],
        "ClientRequestToken": str,
    },
    total=False,
)

class ContinueUpdateRollbackInputRequestTypeDef(
    _RequiredContinueUpdateRollbackInputRequestTypeDef,
    _OptionalContinueUpdateRollbackInputRequestTypeDef,
):
    pass

_RequiredCreateChangeSetInputRequestTypeDef = TypedDict(
    "_RequiredCreateChangeSetInputRequestTypeDef",
    {
        "StackName": str,
        "ChangeSetName": str,
    },
)
_OptionalCreateChangeSetInputRequestTypeDef = TypedDict(
    "_OptionalCreateChangeSetInputRequestTypeDef",
    {
        "TemplateBody": str,
        "TemplateURL": str,
        "UsePreviousTemplate": bool,
        "Parameters": List["ParameterTypeDef"],
        "Capabilities": List[CapabilityType],
        "ResourceTypes": List[str],
        "RoleARN": str,
        "RollbackConfiguration": "RollbackConfigurationTypeDef",
        "NotificationARNs": List[str],
        "Tags": List["TagTypeDef"],
        "ClientToken": str,
        "Description": str,
        "ChangeSetType": ChangeSetTypeType,
        "ResourcesToImport": List["ResourceToImportTypeDef"],
        "IncludeNestedStacks": bool,
    },
    total=False,
)

class CreateChangeSetInputRequestTypeDef(
    _RequiredCreateChangeSetInputRequestTypeDef, _OptionalCreateChangeSetInputRequestTypeDef
):
    pass

CreateChangeSetOutputTypeDef = TypedDict(
    "CreateChangeSetOutputTypeDef",
    {
        "Id": str,
        "StackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStackInputRequestTypeDef = TypedDict(
    "_RequiredCreateStackInputRequestTypeDef",
    {
        "StackName": str,
    },
)
_OptionalCreateStackInputRequestTypeDef = TypedDict(
    "_OptionalCreateStackInputRequestTypeDef",
    {
        "TemplateBody": str,
        "TemplateURL": str,
        "Parameters": List["ParameterTypeDef"],
        "DisableRollback": bool,
        "RollbackConfiguration": "RollbackConfigurationTypeDef",
        "TimeoutInMinutes": int,
        "NotificationARNs": List[str],
        "Capabilities": List[CapabilityType],
        "ResourceTypes": List[str],
        "RoleARN": str,
        "OnFailure": OnFailureType,
        "StackPolicyBody": str,
        "StackPolicyURL": str,
        "Tags": List["TagTypeDef"],
        "ClientRequestToken": str,
        "EnableTerminationProtection": bool,
    },
    total=False,
)

class CreateStackInputRequestTypeDef(
    _RequiredCreateStackInputRequestTypeDef, _OptionalCreateStackInputRequestTypeDef
):
    pass

_RequiredCreateStackInputServiceResourceTypeDef = TypedDict(
    "_RequiredCreateStackInputServiceResourceTypeDef",
    {
        "StackName": str,
    },
)
_OptionalCreateStackInputServiceResourceTypeDef = TypedDict(
    "_OptionalCreateStackInputServiceResourceTypeDef",
    {
        "TemplateBody": str,
        "TemplateURL": str,
        "Parameters": List["ParameterTypeDef"],
        "DisableRollback": bool,
        "RollbackConfiguration": "RollbackConfigurationTypeDef",
        "TimeoutInMinutes": int,
        "NotificationARNs": List[str],
        "Capabilities": List[CapabilityType],
        "ResourceTypes": List[str],
        "RoleARN": str,
        "OnFailure": OnFailureType,
        "StackPolicyBody": str,
        "StackPolicyURL": str,
        "Tags": List["TagTypeDef"],
        "ClientRequestToken": str,
        "EnableTerminationProtection": bool,
    },
    total=False,
)

class CreateStackInputServiceResourceTypeDef(
    _RequiredCreateStackInputServiceResourceTypeDef, _OptionalCreateStackInputServiceResourceTypeDef
):
    pass

_RequiredCreateStackInstancesInputRequestTypeDef = TypedDict(
    "_RequiredCreateStackInstancesInputRequestTypeDef",
    {
        "StackSetName": str,
        "Regions": List[str],
    },
)
_OptionalCreateStackInstancesInputRequestTypeDef = TypedDict(
    "_OptionalCreateStackInstancesInputRequestTypeDef",
    {
        "Accounts": List[str],
        "DeploymentTargets": "DeploymentTargetsTypeDef",
        "ParameterOverrides": List["ParameterTypeDef"],
        "OperationPreferences": "StackSetOperationPreferencesTypeDef",
        "OperationId": str,
        "CallAs": CallAsType,
    },
    total=False,
)

class CreateStackInstancesInputRequestTypeDef(
    _RequiredCreateStackInstancesInputRequestTypeDef,
    _OptionalCreateStackInstancesInputRequestTypeDef,
):
    pass

CreateStackInstancesOutputTypeDef = TypedDict(
    "CreateStackInstancesOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStackOutputTypeDef = TypedDict(
    "CreateStackOutputTypeDef",
    {
        "StackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStackSetInputRequestTypeDef = TypedDict(
    "_RequiredCreateStackSetInputRequestTypeDef",
    {
        "StackSetName": str,
    },
)
_OptionalCreateStackSetInputRequestTypeDef = TypedDict(
    "_OptionalCreateStackSetInputRequestTypeDef",
    {
        "Description": str,
        "TemplateBody": str,
        "TemplateURL": str,
        "StackId": str,
        "Parameters": List["ParameterTypeDef"],
        "Capabilities": List[CapabilityType],
        "Tags": List["TagTypeDef"],
        "AdministrationRoleARN": str,
        "ExecutionRoleName": str,
        "PermissionModel": PermissionModelsType,
        "AutoDeployment": "AutoDeploymentTypeDef",
        "CallAs": CallAsType,
        "ClientRequestToken": str,
    },
    total=False,
)

class CreateStackSetInputRequestTypeDef(
    _RequiredCreateStackSetInputRequestTypeDef, _OptionalCreateStackSetInputRequestTypeDef
):
    pass

CreateStackSetOutputTypeDef = TypedDict(
    "CreateStackSetOutputTypeDef",
    {
        "StackSetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeactivateTypeInputRequestTypeDef = TypedDict(
    "DeactivateTypeInputRequestTypeDef",
    {
        "TypeName": str,
        "Type": ThirdPartyTypeType,
        "Arn": str,
    },
    total=False,
)

_RequiredDeleteChangeSetInputRequestTypeDef = TypedDict(
    "_RequiredDeleteChangeSetInputRequestTypeDef",
    {
        "ChangeSetName": str,
    },
)
_OptionalDeleteChangeSetInputRequestTypeDef = TypedDict(
    "_OptionalDeleteChangeSetInputRequestTypeDef",
    {
        "StackName": str,
    },
    total=False,
)

class DeleteChangeSetInputRequestTypeDef(
    _RequiredDeleteChangeSetInputRequestTypeDef, _OptionalDeleteChangeSetInputRequestTypeDef
):
    pass

_RequiredDeleteStackInputRequestTypeDef = TypedDict(
    "_RequiredDeleteStackInputRequestTypeDef",
    {
        "StackName": str,
    },
)
_OptionalDeleteStackInputRequestTypeDef = TypedDict(
    "_OptionalDeleteStackInputRequestTypeDef",
    {
        "RetainResources": List[str],
        "RoleARN": str,
        "ClientRequestToken": str,
    },
    total=False,
)

class DeleteStackInputRequestTypeDef(
    _RequiredDeleteStackInputRequestTypeDef, _OptionalDeleteStackInputRequestTypeDef
):
    pass

DeleteStackInputStackTypeDef = TypedDict(
    "DeleteStackInputStackTypeDef",
    {
        "RetainResources": List[str],
        "RoleARN": str,
        "ClientRequestToken": str,
    },
    total=False,
)

_RequiredDeleteStackInstancesInputRequestTypeDef = TypedDict(
    "_RequiredDeleteStackInstancesInputRequestTypeDef",
    {
        "StackSetName": str,
        "Regions": List[str],
        "RetainStacks": bool,
    },
)
_OptionalDeleteStackInstancesInputRequestTypeDef = TypedDict(
    "_OptionalDeleteStackInstancesInputRequestTypeDef",
    {
        "Accounts": List[str],
        "DeploymentTargets": "DeploymentTargetsTypeDef",
        "OperationPreferences": "StackSetOperationPreferencesTypeDef",
        "OperationId": str,
        "CallAs": CallAsType,
    },
    total=False,
)

class DeleteStackInstancesInputRequestTypeDef(
    _RequiredDeleteStackInstancesInputRequestTypeDef,
    _OptionalDeleteStackInstancesInputRequestTypeDef,
):
    pass

DeleteStackInstancesOutputTypeDef = TypedDict(
    "DeleteStackInstancesOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteStackSetInputRequestTypeDef = TypedDict(
    "_RequiredDeleteStackSetInputRequestTypeDef",
    {
        "StackSetName": str,
    },
)
_OptionalDeleteStackSetInputRequestTypeDef = TypedDict(
    "_OptionalDeleteStackSetInputRequestTypeDef",
    {
        "CallAs": CallAsType,
    },
    total=False,
)

class DeleteStackSetInputRequestTypeDef(
    _RequiredDeleteStackSetInputRequestTypeDef, _OptionalDeleteStackSetInputRequestTypeDef
):
    pass

DeploymentTargetsTypeDef = TypedDict(
    "DeploymentTargetsTypeDef",
    {
        "Accounts": List[str],
        "AccountsUrl": str,
        "OrganizationalUnitIds": List[str],
    },
    total=False,
)

DeregisterTypeInputRequestTypeDef = TypedDict(
    "DeregisterTypeInputRequestTypeDef",
    {
        "Arn": str,
        "Type": RegistryTypeType,
        "TypeName": str,
        "VersionId": str,
    },
    total=False,
)

DescribeAccountLimitsInputRequestTypeDef = TypedDict(
    "DescribeAccountLimitsInputRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

DescribeAccountLimitsOutputTypeDef = TypedDict(
    "DescribeAccountLimitsOutputTypeDef",
    {
        "AccountLimits": List["AccountLimitTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeChangeSetInputRequestTypeDef = TypedDict(
    "_RequiredDescribeChangeSetInputRequestTypeDef",
    {
        "ChangeSetName": str,
    },
)
_OptionalDescribeChangeSetInputRequestTypeDef = TypedDict(
    "_OptionalDescribeChangeSetInputRequestTypeDef",
    {
        "StackName": str,
        "NextToken": str,
    },
    total=False,
)

class DescribeChangeSetInputRequestTypeDef(
    _RequiredDescribeChangeSetInputRequestTypeDef, _OptionalDescribeChangeSetInputRequestTypeDef
):
    pass

DescribeChangeSetOutputTypeDef = TypedDict(
    "DescribeChangeSetOutputTypeDef",
    {
        "ChangeSetName": str,
        "ChangeSetId": str,
        "StackId": str,
        "StackName": str,
        "Description": str,
        "Parameters": List["ParameterTypeDef"],
        "CreationTime": datetime,
        "ExecutionStatus": ExecutionStatusType,
        "Status": ChangeSetStatusType,
        "StatusReason": str,
        "NotificationARNs": List[str],
        "RollbackConfiguration": "RollbackConfigurationTypeDef",
        "Capabilities": List[CapabilityType],
        "Tags": List["TagTypeDef"],
        "Changes": List["ChangeTypeDef"],
        "NextToken": str,
        "IncludeNestedStacks": bool,
        "ParentChangeSetId": str,
        "RootChangeSetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePublisherInputRequestTypeDef = TypedDict(
    "DescribePublisherInputRequestTypeDef",
    {
        "PublisherId": str,
    },
    total=False,
)

DescribePublisherOutputTypeDef = TypedDict(
    "DescribePublisherOutputTypeDef",
    {
        "PublisherId": str,
        "PublisherStatus": PublisherStatusType,
        "IdentityProvider": IdentityProviderType,
        "PublisherProfile": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackDriftDetectionStatusInputRequestTypeDef = TypedDict(
    "DescribeStackDriftDetectionStatusInputRequestTypeDef",
    {
        "StackDriftDetectionId": str,
    },
)

DescribeStackDriftDetectionStatusOutputTypeDef = TypedDict(
    "DescribeStackDriftDetectionStatusOutputTypeDef",
    {
        "StackId": str,
        "StackDriftDetectionId": str,
        "StackDriftStatus": StackDriftStatusType,
        "DetectionStatus": StackDriftDetectionStatusType,
        "DetectionStatusReason": str,
        "DriftedStackResourceCount": int,
        "Timestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackEventsInputRequestTypeDef = TypedDict(
    "DescribeStackEventsInputRequestTypeDef",
    {
        "StackName": str,
        "NextToken": str,
    },
    total=False,
)

DescribeStackEventsOutputTypeDef = TypedDict(
    "DescribeStackEventsOutputTypeDef",
    {
        "StackEvents": List["StackEventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeStackInstanceInputRequestTypeDef = TypedDict(
    "_RequiredDescribeStackInstanceInputRequestTypeDef",
    {
        "StackSetName": str,
        "StackInstanceAccount": str,
        "StackInstanceRegion": str,
    },
)
_OptionalDescribeStackInstanceInputRequestTypeDef = TypedDict(
    "_OptionalDescribeStackInstanceInputRequestTypeDef",
    {
        "CallAs": CallAsType,
    },
    total=False,
)

class DescribeStackInstanceInputRequestTypeDef(
    _RequiredDescribeStackInstanceInputRequestTypeDef,
    _OptionalDescribeStackInstanceInputRequestTypeDef,
):
    pass

DescribeStackInstanceOutputTypeDef = TypedDict(
    "DescribeStackInstanceOutputTypeDef",
    {
        "StackInstance": "StackInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeStackResourceDriftsInputRequestTypeDef = TypedDict(
    "_RequiredDescribeStackResourceDriftsInputRequestTypeDef",
    {
        "StackName": str,
    },
)
_OptionalDescribeStackResourceDriftsInputRequestTypeDef = TypedDict(
    "_OptionalDescribeStackResourceDriftsInputRequestTypeDef",
    {
        "StackResourceDriftStatusFilters": List[StackResourceDriftStatusType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class DescribeStackResourceDriftsInputRequestTypeDef(
    _RequiredDescribeStackResourceDriftsInputRequestTypeDef,
    _OptionalDescribeStackResourceDriftsInputRequestTypeDef,
):
    pass

DescribeStackResourceDriftsOutputTypeDef = TypedDict(
    "DescribeStackResourceDriftsOutputTypeDef",
    {
        "StackResourceDrifts": List["StackResourceDriftTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackResourceInputRequestTypeDef = TypedDict(
    "DescribeStackResourceInputRequestTypeDef",
    {
        "StackName": str,
        "LogicalResourceId": str,
    },
)

DescribeStackResourceOutputTypeDef = TypedDict(
    "DescribeStackResourceOutputTypeDef",
    {
        "StackResourceDetail": "StackResourceDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackResourcesInputRequestTypeDef = TypedDict(
    "DescribeStackResourcesInputRequestTypeDef",
    {
        "StackName": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
    },
    total=False,
)

DescribeStackResourcesOutputTypeDef = TypedDict(
    "DescribeStackResourcesOutputTypeDef",
    {
        "StackResources": List["StackResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeStackSetInputRequestTypeDef = TypedDict(
    "_RequiredDescribeStackSetInputRequestTypeDef",
    {
        "StackSetName": str,
    },
)
_OptionalDescribeStackSetInputRequestTypeDef = TypedDict(
    "_OptionalDescribeStackSetInputRequestTypeDef",
    {
        "CallAs": CallAsType,
    },
    total=False,
)

class DescribeStackSetInputRequestTypeDef(
    _RequiredDescribeStackSetInputRequestTypeDef, _OptionalDescribeStackSetInputRequestTypeDef
):
    pass

_RequiredDescribeStackSetOperationInputRequestTypeDef = TypedDict(
    "_RequiredDescribeStackSetOperationInputRequestTypeDef",
    {
        "StackSetName": str,
        "OperationId": str,
    },
)
_OptionalDescribeStackSetOperationInputRequestTypeDef = TypedDict(
    "_OptionalDescribeStackSetOperationInputRequestTypeDef",
    {
        "CallAs": CallAsType,
    },
    total=False,
)

class DescribeStackSetOperationInputRequestTypeDef(
    _RequiredDescribeStackSetOperationInputRequestTypeDef,
    _OptionalDescribeStackSetOperationInputRequestTypeDef,
):
    pass

DescribeStackSetOperationOutputTypeDef = TypedDict(
    "DescribeStackSetOperationOutputTypeDef",
    {
        "StackSetOperation": "StackSetOperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackSetOutputTypeDef = TypedDict(
    "DescribeStackSetOutputTypeDef",
    {
        "StackSet": "StackSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStacksInputRequestTypeDef = TypedDict(
    "DescribeStacksInputRequestTypeDef",
    {
        "StackName": str,
        "NextToken": str,
    },
    total=False,
)

DescribeStacksOutputTypeDef = TypedDict(
    "DescribeStacksOutputTypeDef",
    {
        "Stacks": List["StackTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTypeInputRequestTypeDef = TypedDict(
    "DescribeTypeInputRequestTypeDef",
    {
        "Type": RegistryTypeType,
        "TypeName": str,
        "Arn": str,
        "VersionId": str,
        "PublisherId": str,
        "PublicVersionNumber": str,
    },
    total=False,
)

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
        "LoggingConfig": "LoggingConfigTypeDef",
        "RequiredActivatedTypes": List["RequiredActivatedTypeTypeDef"],
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTypeRegistrationInputRequestTypeDef = TypedDict(
    "DescribeTypeRegistrationInputRequestTypeDef",
    {
        "RegistrationToken": str,
    },
)

DescribeTypeRegistrationOutputTypeDef = TypedDict(
    "DescribeTypeRegistrationOutputTypeDef",
    {
        "ProgressStatus": RegistrationStatusType,
        "Description": str,
        "TypeArn": str,
        "TypeVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDetectStackDriftInputRequestTypeDef = TypedDict(
    "_RequiredDetectStackDriftInputRequestTypeDef",
    {
        "StackName": str,
    },
)
_OptionalDetectStackDriftInputRequestTypeDef = TypedDict(
    "_OptionalDetectStackDriftInputRequestTypeDef",
    {
        "LogicalResourceIds": List[str],
    },
    total=False,
)

class DetectStackDriftInputRequestTypeDef(
    _RequiredDetectStackDriftInputRequestTypeDef, _OptionalDetectStackDriftInputRequestTypeDef
):
    pass

DetectStackDriftOutputTypeDef = TypedDict(
    "DetectStackDriftOutputTypeDef",
    {
        "StackDriftDetectionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectStackResourceDriftInputRequestTypeDef = TypedDict(
    "DetectStackResourceDriftInputRequestTypeDef",
    {
        "StackName": str,
        "LogicalResourceId": str,
    },
)

DetectStackResourceDriftOutputTypeDef = TypedDict(
    "DetectStackResourceDriftOutputTypeDef",
    {
        "StackResourceDrift": "StackResourceDriftTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDetectStackSetDriftInputRequestTypeDef = TypedDict(
    "_RequiredDetectStackSetDriftInputRequestTypeDef",
    {
        "StackSetName": str,
    },
)
_OptionalDetectStackSetDriftInputRequestTypeDef = TypedDict(
    "_OptionalDetectStackSetDriftInputRequestTypeDef",
    {
        "OperationPreferences": "StackSetOperationPreferencesTypeDef",
        "OperationId": str,
        "CallAs": CallAsType,
    },
    total=False,
)

class DetectStackSetDriftInputRequestTypeDef(
    _RequiredDetectStackSetDriftInputRequestTypeDef, _OptionalDetectStackSetDriftInputRequestTypeDef
):
    pass

DetectStackSetDriftOutputTypeDef = TypedDict(
    "DetectStackSetDriftOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EstimateTemplateCostInputRequestTypeDef = TypedDict(
    "EstimateTemplateCostInputRequestTypeDef",
    {
        "TemplateBody": str,
        "TemplateURL": str,
        "Parameters": List["ParameterTypeDef"],
    },
    total=False,
)

EstimateTemplateCostOutputTypeDef = TypedDict(
    "EstimateTemplateCostOutputTypeDef",
    {
        "Url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExecuteChangeSetInputRequestTypeDef = TypedDict(
    "_RequiredExecuteChangeSetInputRequestTypeDef",
    {
        "ChangeSetName": str,
    },
)
_OptionalExecuteChangeSetInputRequestTypeDef = TypedDict(
    "_OptionalExecuteChangeSetInputRequestTypeDef",
    {
        "StackName": str,
        "ClientRequestToken": str,
    },
    total=False,
)

class ExecuteChangeSetInputRequestTypeDef(
    _RequiredExecuteChangeSetInputRequestTypeDef, _OptionalExecuteChangeSetInputRequestTypeDef
):
    pass

ExportTypeDef = TypedDict(
    "ExportTypeDef",
    {
        "ExportingStackId": str,
        "Name": str,
        "Value": str,
    },
    total=False,
)

GetStackPolicyInputRequestTypeDef = TypedDict(
    "GetStackPolicyInputRequestTypeDef",
    {
        "StackName": str,
    },
)

GetStackPolicyOutputTypeDef = TypedDict(
    "GetStackPolicyOutputTypeDef",
    {
        "StackPolicyBody": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTemplateInputRequestTypeDef = TypedDict(
    "GetTemplateInputRequestTypeDef",
    {
        "StackName": str,
        "ChangeSetName": str,
        "TemplateStage": TemplateStageType,
    },
    total=False,
)

GetTemplateOutputTypeDef = TypedDict(
    "GetTemplateOutputTypeDef",
    {
        "TemplateBody": str,
        "StagesAvailable": List[TemplateStageType],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTemplateSummaryInputRequestTypeDef = TypedDict(
    "GetTemplateSummaryInputRequestTypeDef",
    {
        "TemplateBody": str,
        "TemplateURL": str,
        "StackName": str,
        "StackSetName": str,
        "CallAs": CallAsType,
    },
    total=False,
)

GetTemplateSummaryOutputTypeDef = TypedDict(
    "GetTemplateSummaryOutputTypeDef",
    {
        "Parameters": List["ParameterDeclarationTypeDef"],
        "Description": str,
        "Capabilities": List[CapabilityType],
        "CapabilitiesReason": str,
        "ResourceTypes": List[str],
        "Version": str,
        "Metadata": str,
        "DeclaredTransforms": List[str],
        "ResourceIdentifierSummaries": List["ResourceIdentifierSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImportStacksToStackSetInputRequestTypeDef = TypedDict(
    "_RequiredImportStacksToStackSetInputRequestTypeDef",
    {
        "StackSetName": str,
        "StackIds": List[str],
    },
)
_OptionalImportStacksToStackSetInputRequestTypeDef = TypedDict(
    "_OptionalImportStacksToStackSetInputRequestTypeDef",
    {
        "OperationPreferences": "StackSetOperationPreferencesTypeDef",
        "OperationId": str,
        "CallAs": CallAsType,
    },
    total=False,
)

class ImportStacksToStackSetInputRequestTypeDef(
    _RequiredImportStacksToStackSetInputRequestTypeDef,
    _OptionalImportStacksToStackSetInputRequestTypeDef,
):
    pass

ImportStacksToStackSetOutputTypeDef = TypedDict(
    "ImportStacksToStackSetOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChangeSetsInputRequestTypeDef = TypedDict(
    "_RequiredListChangeSetsInputRequestTypeDef",
    {
        "StackName": str,
    },
)
_OptionalListChangeSetsInputRequestTypeDef = TypedDict(
    "_OptionalListChangeSetsInputRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListChangeSetsInputRequestTypeDef(
    _RequiredListChangeSetsInputRequestTypeDef, _OptionalListChangeSetsInputRequestTypeDef
):
    pass

ListChangeSetsOutputTypeDef = TypedDict(
    "ListChangeSetsOutputTypeDef",
    {
        "Summaries": List["ChangeSetSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExportsInputRequestTypeDef = TypedDict(
    "ListExportsInputRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

ListExportsOutputTypeDef = TypedDict(
    "ListExportsOutputTypeDef",
    {
        "Exports": List["ExportTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListImportsInputRequestTypeDef = TypedDict(
    "_RequiredListImportsInputRequestTypeDef",
    {
        "ExportName": str,
    },
)
_OptionalListImportsInputRequestTypeDef = TypedDict(
    "_OptionalListImportsInputRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListImportsInputRequestTypeDef(
    _RequiredListImportsInputRequestTypeDef, _OptionalListImportsInputRequestTypeDef
):
    pass

ListImportsOutputTypeDef = TypedDict(
    "ListImportsOutputTypeDef",
    {
        "Imports": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStackInstancesInputRequestTypeDef = TypedDict(
    "_RequiredListStackInstancesInputRequestTypeDef",
    {
        "StackSetName": str,
    },
)
_OptionalListStackInstancesInputRequestTypeDef = TypedDict(
    "_OptionalListStackInstancesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["StackInstanceFilterTypeDef"],
        "StackInstanceAccount": str,
        "StackInstanceRegion": str,
        "CallAs": CallAsType,
    },
    total=False,
)

class ListStackInstancesInputRequestTypeDef(
    _RequiredListStackInstancesInputRequestTypeDef, _OptionalListStackInstancesInputRequestTypeDef
):
    pass

ListStackInstancesOutputTypeDef = TypedDict(
    "ListStackInstancesOutputTypeDef",
    {
        "Summaries": List["StackInstanceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStackResourcesInputRequestTypeDef = TypedDict(
    "_RequiredListStackResourcesInputRequestTypeDef",
    {
        "StackName": str,
    },
)
_OptionalListStackResourcesInputRequestTypeDef = TypedDict(
    "_OptionalListStackResourcesInputRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListStackResourcesInputRequestTypeDef(
    _RequiredListStackResourcesInputRequestTypeDef, _OptionalListStackResourcesInputRequestTypeDef
):
    pass

ListStackResourcesOutputTypeDef = TypedDict(
    "ListStackResourcesOutputTypeDef",
    {
        "StackResourceSummaries": List["StackResourceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStackSetOperationResultsInputRequestTypeDef = TypedDict(
    "_RequiredListStackSetOperationResultsInputRequestTypeDef",
    {
        "StackSetName": str,
        "OperationId": str,
    },
)
_OptionalListStackSetOperationResultsInputRequestTypeDef = TypedDict(
    "_OptionalListStackSetOperationResultsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "CallAs": CallAsType,
    },
    total=False,
)

class ListStackSetOperationResultsInputRequestTypeDef(
    _RequiredListStackSetOperationResultsInputRequestTypeDef,
    _OptionalListStackSetOperationResultsInputRequestTypeDef,
):
    pass

ListStackSetOperationResultsOutputTypeDef = TypedDict(
    "ListStackSetOperationResultsOutputTypeDef",
    {
        "Summaries": List["StackSetOperationResultSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStackSetOperationsInputRequestTypeDef = TypedDict(
    "_RequiredListStackSetOperationsInputRequestTypeDef",
    {
        "StackSetName": str,
    },
)
_OptionalListStackSetOperationsInputRequestTypeDef = TypedDict(
    "_OptionalListStackSetOperationsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "CallAs": CallAsType,
    },
    total=False,
)

class ListStackSetOperationsInputRequestTypeDef(
    _RequiredListStackSetOperationsInputRequestTypeDef,
    _OptionalListStackSetOperationsInputRequestTypeDef,
):
    pass

ListStackSetOperationsOutputTypeDef = TypedDict(
    "ListStackSetOperationsOutputTypeDef",
    {
        "Summaries": List["StackSetOperationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStackSetsInputRequestTypeDef = TypedDict(
    "ListStackSetsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Status": StackSetStatusType,
        "CallAs": CallAsType,
    },
    total=False,
)

ListStackSetsOutputTypeDef = TypedDict(
    "ListStackSetsOutputTypeDef",
    {
        "Summaries": List["StackSetSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStacksInputRequestTypeDef = TypedDict(
    "ListStacksInputRequestTypeDef",
    {
        "NextToken": str,
        "StackStatusFilter": List[StackStatusType],
    },
    total=False,
)

ListStacksOutputTypeDef = TypedDict(
    "ListStacksOutputTypeDef",
    {
        "StackSummaries": List["StackSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTypeRegistrationsInputRequestTypeDef = TypedDict(
    "ListTypeRegistrationsInputRequestTypeDef",
    {
        "Type": RegistryTypeType,
        "TypeName": str,
        "TypeArn": str,
        "RegistrationStatusFilter": RegistrationStatusType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListTypeRegistrationsOutputTypeDef = TypedDict(
    "ListTypeRegistrationsOutputTypeDef",
    {
        "RegistrationTokenList": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTypeVersionsInputRequestTypeDef = TypedDict(
    "ListTypeVersionsInputRequestTypeDef",
    {
        "Type": RegistryTypeType,
        "TypeName": str,
        "Arn": str,
        "MaxResults": int,
        "NextToken": str,
        "DeprecatedStatus": DeprecatedStatusType,
        "PublisherId": str,
    },
    total=False,
)

ListTypeVersionsOutputTypeDef = TypedDict(
    "ListTypeVersionsOutputTypeDef",
    {
        "TypeVersionSummaries": List["TypeVersionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTypesInputRequestTypeDef = TypedDict(
    "ListTypesInputRequestTypeDef",
    {
        "Visibility": VisibilityType,
        "ProvisioningType": ProvisioningTypeType,
        "DeprecatedStatus": DeprecatedStatusType,
        "Type": RegistryTypeType,
        "Filters": "TypeFiltersTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListTypesOutputTypeDef = TypedDict(
    "ListTypesOutputTypeDef",
    {
        "TypeSummaries": List["TypeSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingConfigTypeDef = TypedDict(
    "LoggingConfigTypeDef",
    {
        "LogRoleArn": str,
        "LogGroupName": str,
    },
)

ModuleInfoTypeDef = TypedDict(
    "ModuleInfoTypeDef",
    {
        "TypeHierarchy": str,
        "LogicalIdHierarchy": str,
    },
    total=False,
)

OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {
        "OutputKey": str,
        "OutputValue": str,
        "Description": str,
        "ExportName": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ParameterConstraintsTypeDef = TypedDict(
    "ParameterConstraintsTypeDef",
    {
        "AllowedValues": List[str],
    },
    total=False,
)

ParameterDeclarationTypeDef = TypedDict(
    "ParameterDeclarationTypeDef",
    {
        "ParameterKey": str,
        "DefaultValue": str,
        "ParameterType": str,
        "NoEcho": bool,
        "Description": str,
        "ParameterConstraints": "ParameterConstraintsTypeDef",
    },
    total=False,
)

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "ParameterKey": str,
        "ParameterValue": str,
        "UsePreviousValue": bool,
        "ResolvedValue": str,
    },
    total=False,
)

PhysicalResourceIdContextKeyValuePairTypeDef = TypedDict(
    "PhysicalResourceIdContextKeyValuePairTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

PropertyDifferenceTypeDef = TypedDict(
    "PropertyDifferenceTypeDef",
    {
        "PropertyPath": str,
        "ExpectedValue": str,
        "ActualValue": str,
        "DifferenceType": DifferenceTypeType,
    },
)

PublishTypeInputRequestTypeDef = TypedDict(
    "PublishTypeInputRequestTypeDef",
    {
        "Type": ThirdPartyTypeType,
        "Arn": str,
        "TypeName": str,
        "PublicVersionNumber": str,
    },
    total=False,
)

PublishTypeOutputTypeDef = TypedDict(
    "PublishTypeOutputTypeDef",
    {
        "PublicTypeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRecordHandlerProgressInputRequestTypeDef = TypedDict(
    "_RequiredRecordHandlerProgressInputRequestTypeDef",
    {
        "BearerToken": str,
        "OperationStatus": OperationStatusType,
    },
)
_OptionalRecordHandlerProgressInputRequestTypeDef = TypedDict(
    "_OptionalRecordHandlerProgressInputRequestTypeDef",
    {
        "CurrentOperationStatus": OperationStatusType,
        "StatusMessage": str,
        "ErrorCode": HandlerErrorCodeType,
        "ResourceModel": str,
        "ClientRequestToken": str,
    },
    total=False,
)

class RecordHandlerProgressInputRequestTypeDef(
    _RequiredRecordHandlerProgressInputRequestTypeDef,
    _OptionalRecordHandlerProgressInputRequestTypeDef,
):
    pass

RegisterPublisherInputRequestTypeDef = TypedDict(
    "RegisterPublisherInputRequestTypeDef",
    {
        "AcceptTermsAndConditions": bool,
        "ConnectionArn": str,
    },
    total=False,
)

RegisterPublisherOutputTypeDef = TypedDict(
    "RegisterPublisherOutputTypeDef",
    {
        "PublisherId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterTypeInputRequestTypeDef = TypedDict(
    "_RequiredRegisterTypeInputRequestTypeDef",
    {
        "TypeName": str,
        "SchemaHandlerPackage": str,
    },
)
_OptionalRegisterTypeInputRequestTypeDef = TypedDict(
    "_OptionalRegisterTypeInputRequestTypeDef",
    {
        "Type": RegistryTypeType,
        "LoggingConfig": "LoggingConfigTypeDef",
        "ExecutionRoleArn": str,
        "ClientRequestToken": str,
    },
    total=False,
)

class RegisterTypeInputRequestTypeDef(
    _RequiredRegisterTypeInputRequestTypeDef, _OptionalRegisterTypeInputRequestTypeDef
):
    pass

RegisterTypeOutputTypeDef = TypedDict(
    "RegisterTypeOutputTypeDef",
    {
        "RegistrationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RequiredActivatedTypeTypeDef = TypedDict(
    "RequiredActivatedTypeTypeDef",
    {
        "TypeNameAlias": str,
        "OriginalTypeName": str,
        "PublisherId": str,
        "SupportedMajorVersions": List[int],
    },
    total=False,
)

ResourceChangeDetailTypeDef = TypedDict(
    "ResourceChangeDetailTypeDef",
    {
        "Target": "ResourceTargetDefinitionTypeDef",
        "Evaluation": EvaluationTypeType,
        "ChangeSource": ChangeSourceType,
        "CausingEntity": str,
    },
    total=False,
)

ResourceChangeTypeDef = TypedDict(
    "ResourceChangeTypeDef",
    {
        "Action": ChangeActionType,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Replacement": ReplacementType,
        "Scope": List[ResourceAttributeType],
        "Details": List["ResourceChangeDetailTypeDef"],
        "ChangeSetId": str,
        "ModuleInfo": "ModuleInfoTypeDef",
    },
    total=False,
)

ResourceIdentifierSummaryTypeDef = TypedDict(
    "ResourceIdentifierSummaryTypeDef",
    {
        "ResourceType": str,
        "LogicalResourceIds": List[str],
        "ResourceIdentifiers": List[str],
    },
    total=False,
)

ResourceTargetDefinitionTypeDef = TypedDict(
    "ResourceTargetDefinitionTypeDef",
    {
        "Attribute": ResourceAttributeType,
        "Name": str,
        "RequiresRecreation": RequiresRecreationType,
    },
    total=False,
)

ResourceToImportTypeDef = TypedDict(
    "ResourceToImportTypeDef",
    {
        "ResourceType": str,
        "LogicalResourceId": str,
        "ResourceIdentifier": Dict[str, str],
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

RollbackConfigurationTypeDef = TypedDict(
    "RollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List["RollbackTriggerTypeDef"],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)

RollbackTriggerTypeDef = TypedDict(
    "RollbackTriggerTypeDef",
    {
        "Arn": str,
        "Type": str,
    },
)

ServiceResourceEventRequestTypeDef = TypedDict(
    "ServiceResourceEventRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceStackRequestTypeDef = TypedDict(
    "ServiceResourceStackRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceStackResourceRequestTypeDef = TypedDict(
    "ServiceResourceStackResourceRequestTypeDef",
    {
        "stack_name": str,
        "logical_id": str,
    },
)

ServiceResourceStackResourceSummaryRequestTypeDef = TypedDict(
    "ServiceResourceStackResourceSummaryRequestTypeDef",
    {
        "stack_name": str,
        "logical_id": str,
    },
)

_RequiredSetStackPolicyInputRequestTypeDef = TypedDict(
    "_RequiredSetStackPolicyInputRequestTypeDef",
    {
        "StackName": str,
    },
)
_OptionalSetStackPolicyInputRequestTypeDef = TypedDict(
    "_OptionalSetStackPolicyInputRequestTypeDef",
    {
        "StackPolicyBody": str,
        "StackPolicyURL": str,
    },
    total=False,
)

class SetStackPolicyInputRequestTypeDef(
    _RequiredSetStackPolicyInputRequestTypeDef, _OptionalSetStackPolicyInputRequestTypeDef
):
    pass

_RequiredSetTypeConfigurationInputRequestTypeDef = TypedDict(
    "_RequiredSetTypeConfigurationInputRequestTypeDef",
    {
        "Configuration": str,
    },
)
_OptionalSetTypeConfigurationInputRequestTypeDef = TypedDict(
    "_OptionalSetTypeConfigurationInputRequestTypeDef",
    {
        "TypeArn": str,
        "ConfigurationAlias": str,
        "TypeName": str,
        "Type": ThirdPartyTypeType,
    },
    total=False,
)

class SetTypeConfigurationInputRequestTypeDef(
    _RequiredSetTypeConfigurationInputRequestTypeDef,
    _OptionalSetTypeConfigurationInputRequestTypeDef,
):
    pass

SetTypeConfigurationOutputTypeDef = TypedDict(
    "SetTypeConfigurationOutputTypeDef",
    {
        "ConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetTypeDefaultVersionInputRequestTypeDef = TypedDict(
    "SetTypeDefaultVersionInputRequestTypeDef",
    {
        "Arn": str,
        "Type": RegistryTypeType,
        "TypeName": str,
        "VersionId": str,
    },
    total=False,
)

SignalResourceInputRequestTypeDef = TypedDict(
    "SignalResourceInputRequestTypeDef",
    {
        "StackName": str,
        "LogicalResourceId": str,
        "UniqueId": str,
        "Status": ResourceSignalStatusType,
    },
)

_RequiredStackDriftInformationSummaryTypeDef = TypedDict(
    "_RequiredStackDriftInformationSummaryTypeDef",
    {
        "StackDriftStatus": StackDriftStatusType,
    },
)
_OptionalStackDriftInformationSummaryTypeDef = TypedDict(
    "_OptionalStackDriftInformationSummaryTypeDef",
    {
        "LastCheckTimestamp": datetime,
    },
    total=False,
)

class StackDriftInformationSummaryTypeDef(
    _RequiredStackDriftInformationSummaryTypeDef, _OptionalStackDriftInformationSummaryTypeDef
):
    pass

_RequiredStackDriftInformationTypeDef = TypedDict(
    "_RequiredStackDriftInformationTypeDef",
    {
        "StackDriftStatus": StackDriftStatusType,
    },
)
_OptionalStackDriftInformationTypeDef = TypedDict(
    "_OptionalStackDriftInformationTypeDef",
    {
        "LastCheckTimestamp": datetime,
    },
    total=False,
)

class StackDriftInformationTypeDef(
    _RequiredStackDriftInformationTypeDef, _OptionalStackDriftInformationTypeDef
):
    pass

_RequiredStackEventTypeDef = TypedDict(
    "_RequiredStackEventTypeDef",
    {
        "StackId": str,
        "EventId": str,
        "StackName": str,
        "Timestamp": datetime,
    },
)
_OptionalStackEventTypeDef = TypedDict(
    "_OptionalStackEventTypeDef",
    {
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "ResourceStatus": ResourceStatusType,
        "ResourceStatusReason": str,
        "ResourceProperties": str,
        "ClientRequestToken": str,
    },
    total=False,
)

class StackEventTypeDef(_RequiredStackEventTypeDef, _OptionalStackEventTypeDef):
    pass

StackInstanceComprehensiveStatusTypeDef = TypedDict(
    "StackInstanceComprehensiveStatusTypeDef",
    {
        "DetailedStatus": StackInstanceDetailedStatusType,
    },
    total=False,
)

StackInstanceFilterTypeDef = TypedDict(
    "StackInstanceFilterTypeDef",
    {
        "Name": Literal["DETAILED_STATUS"],
        "Values": str,
    },
    total=False,
)

StackInstanceSummaryTypeDef = TypedDict(
    "StackInstanceSummaryTypeDef",
    {
        "StackSetId": str,
        "Region": str,
        "Account": str,
        "StackId": str,
        "Status": StackInstanceStatusType,
        "StatusReason": str,
        "StackInstanceStatus": "StackInstanceComprehensiveStatusTypeDef",
        "OrganizationalUnitId": str,
        "DriftStatus": StackDriftStatusType,
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)

StackInstanceTypeDef = TypedDict(
    "StackInstanceTypeDef",
    {
        "StackSetId": str,
        "Region": str,
        "Account": str,
        "StackId": str,
        "ParameterOverrides": List["ParameterTypeDef"],
        "Status": StackInstanceStatusType,
        "StackInstanceStatus": "StackInstanceComprehensiveStatusTypeDef",
        "StatusReason": str,
        "OrganizationalUnitId": str,
        "DriftStatus": StackDriftStatusType,
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)

_RequiredStackResourceDetailTypeDef = TypedDict(
    "_RequiredStackResourceDetailTypeDef",
    {
        "LogicalResourceId": str,
        "ResourceType": str,
        "LastUpdatedTimestamp": datetime,
        "ResourceStatus": ResourceStatusType,
    },
)
_OptionalStackResourceDetailTypeDef = TypedDict(
    "_OptionalStackResourceDetailTypeDef",
    {
        "StackName": str,
        "StackId": str,
        "PhysicalResourceId": str,
        "ResourceStatusReason": str,
        "Description": str,
        "Metadata": str,
        "DriftInformation": "StackResourceDriftInformationTypeDef",
        "ModuleInfo": "ModuleInfoTypeDef",
    },
    total=False,
)

class StackResourceDetailTypeDef(
    _RequiredStackResourceDetailTypeDef, _OptionalStackResourceDetailTypeDef
):
    pass

_RequiredStackResourceDriftInformationSummaryTypeDef = TypedDict(
    "_RequiredStackResourceDriftInformationSummaryTypeDef",
    {
        "StackResourceDriftStatus": StackResourceDriftStatusType,
    },
)
_OptionalStackResourceDriftInformationSummaryTypeDef = TypedDict(
    "_OptionalStackResourceDriftInformationSummaryTypeDef",
    {
        "LastCheckTimestamp": datetime,
    },
    total=False,
)

class StackResourceDriftInformationSummaryTypeDef(
    _RequiredStackResourceDriftInformationSummaryTypeDef,
    _OptionalStackResourceDriftInformationSummaryTypeDef,
):
    pass

_RequiredStackResourceDriftInformationTypeDef = TypedDict(
    "_RequiredStackResourceDriftInformationTypeDef",
    {
        "StackResourceDriftStatus": StackResourceDriftStatusType,
    },
)
_OptionalStackResourceDriftInformationTypeDef = TypedDict(
    "_OptionalStackResourceDriftInformationTypeDef",
    {
        "LastCheckTimestamp": datetime,
    },
    total=False,
)

class StackResourceDriftInformationTypeDef(
    _RequiredStackResourceDriftInformationTypeDef, _OptionalStackResourceDriftInformationTypeDef
):
    pass

_RequiredStackResourceDriftTypeDef = TypedDict(
    "_RequiredStackResourceDriftTypeDef",
    {
        "StackId": str,
        "LogicalResourceId": str,
        "ResourceType": str,
        "StackResourceDriftStatus": StackResourceDriftStatusType,
        "Timestamp": datetime,
    },
)
_OptionalStackResourceDriftTypeDef = TypedDict(
    "_OptionalStackResourceDriftTypeDef",
    {
        "PhysicalResourceId": str,
        "PhysicalResourceIdContext": List["PhysicalResourceIdContextKeyValuePairTypeDef"],
        "ExpectedProperties": str,
        "ActualProperties": str,
        "PropertyDifferences": List["PropertyDifferenceTypeDef"],
        "ModuleInfo": "ModuleInfoTypeDef",
    },
    total=False,
)

class StackResourceDriftTypeDef(
    _RequiredStackResourceDriftTypeDef, _OptionalStackResourceDriftTypeDef
):
    pass

StackResourceRequestTypeDef = TypedDict(
    "StackResourceRequestTypeDef",
    {
        "logical_id": str,
    },
)

_RequiredStackResourceSummaryTypeDef = TypedDict(
    "_RequiredStackResourceSummaryTypeDef",
    {
        "LogicalResourceId": str,
        "ResourceType": str,
        "LastUpdatedTimestamp": datetime,
        "ResourceStatus": ResourceStatusType,
    },
)
_OptionalStackResourceSummaryTypeDef = TypedDict(
    "_OptionalStackResourceSummaryTypeDef",
    {
        "PhysicalResourceId": str,
        "ResourceStatusReason": str,
        "DriftInformation": "StackResourceDriftInformationSummaryTypeDef",
        "ModuleInfo": "ModuleInfoTypeDef",
    },
    total=False,
)

class StackResourceSummaryTypeDef(
    _RequiredStackResourceSummaryTypeDef, _OptionalStackResourceSummaryTypeDef
):
    pass

_RequiredStackResourceTypeDef = TypedDict(
    "_RequiredStackResourceTypeDef",
    {
        "LogicalResourceId": str,
        "ResourceType": str,
        "Timestamp": datetime,
        "ResourceStatus": ResourceStatusType,
    },
)
_OptionalStackResourceTypeDef = TypedDict(
    "_OptionalStackResourceTypeDef",
    {
        "StackName": str,
        "StackId": str,
        "PhysicalResourceId": str,
        "ResourceStatusReason": str,
        "Description": str,
        "DriftInformation": "StackResourceDriftInformationTypeDef",
        "ModuleInfo": "ModuleInfoTypeDef",
    },
    total=False,
)

class StackResourceTypeDef(_RequiredStackResourceTypeDef, _OptionalStackResourceTypeDef):
    pass

StackSetDriftDetectionDetailsTypeDef = TypedDict(
    "StackSetDriftDetectionDetailsTypeDef",
    {
        "DriftStatus": StackSetDriftStatusType,
        "DriftDetectionStatus": StackSetDriftDetectionStatusType,
        "LastDriftCheckTimestamp": datetime,
        "TotalStackInstancesCount": int,
        "DriftedStackInstancesCount": int,
        "InSyncStackInstancesCount": int,
        "InProgressStackInstancesCount": int,
        "FailedStackInstancesCount": int,
    },
    total=False,
)

StackSetOperationPreferencesTypeDef = TypedDict(
    "StackSetOperationPreferencesTypeDef",
    {
        "RegionConcurrencyType": RegionConcurrencyTypeType,
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)

StackSetOperationResultSummaryTypeDef = TypedDict(
    "StackSetOperationResultSummaryTypeDef",
    {
        "Account": str,
        "Region": str,
        "Status": StackSetOperationResultStatusType,
        "StatusReason": str,
        "AccountGateResult": "AccountGateResultTypeDef",
        "OrganizationalUnitId": str,
    },
    total=False,
)

StackSetOperationSummaryTypeDef = TypedDict(
    "StackSetOperationSummaryTypeDef",
    {
        "OperationId": str,
        "Action": StackSetOperationActionType,
        "Status": StackSetOperationStatusType,
        "CreationTimestamp": datetime,
        "EndTimestamp": datetime,
    },
    total=False,
)

StackSetOperationTypeDef = TypedDict(
    "StackSetOperationTypeDef",
    {
        "OperationId": str,
        "StackSetId": str,
        "Action": StackSetOperationActionType,
        "Status": StackSetOperationStatusType,
        "OperationPreferences": "StackSetOperationPreferencesTypeDef",
        "RetainStacks": bool,
        "AdministrationRoleARN": str,
        "ExecutionRoleName": str,
        "CreationTimestamp": datetime,
        "EndTimestamp": datetime,
        "DeploymentTargets": "DeploymentTargetsTypeDef",
        "StackSetDriftDetectionDetails": "StackSetDriftDetectionDetailsTypeDef",
    },
    total=False,
)

StackSetSummaryTypeDef = TypedDict(
    "StackSetSummaryTypeDef",
    {
        "StackSetName": str,
        "StackSetId": str,
        "Description": str,
        "Status": StackSetStatusType,
        "AutoDeployment": "AutoDeploymentTypeDef",
        "PermissionModel": PermissionModelsType,
        "DriftStatus": StackDriftStatusType,
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)

StackSetTypeDef = TypedDict(
    "StackSetTypeDef",
    {
        "StackSetName": str,
        "StackSetId": str,
        "Description": str,
        "Status": StackSetStatusType,
        "TemplateBody": str,
        "Parameters": List["ParameterTypeDef"],
        "Capabilities": List[CapabilityType],
        "Tags": List["TagTypeDef"],
        "StackSetARN": str,
        "AdministrationRoleARN": str,
        "ExecutionRoleName": str,
        "StackSetDriftDetectionDetails": "StackSetDriftDetectionDetailsTypeDef",
        "AutoDeployment": "AutoDeploymentTypeDef",
        "PermissionModel": PermissionModelsType,
        "OrganizationalUnitIds": List[str],
    },
    total=False,
)

_RequiredStackSummaryTypeDef = TypedDict(
    "_RequiredStackSummaryTypeDef",
    {
        "StackName": str,
        "CreationTime": datetime,
        "StackStatus": StackStatusType,
    },
)
_OptionalStackSummaryTypeDef = TypedDict(
    "_OptionalStackSummaryTypeDef",
    {
        "StackId": str,
        "TemplateDescription": str,
        "LastUpdatedTime": datetime,
        "DeletionTime": datetime,
        "StackStatusReason": str,
        "ParentId": str,
        "RootId": str,
        "DriftInformation": "StackDriftInformationSummaryTypeDef",
    },
    total=False,
)

class StackSummaryTypeDef(_RequiredStackSummaryTypeDef, _OptionalStackSummaryTypeDef):
    pass

_RequiredStackTypeDef = TypedDict(
    "_RequiredStackTypeDef",
    {
        "StackName": str,
        "CreationTime": datetime,
        "StackStatus": StackStatusType,
    },
)
_OptionalStackTypeDef = TypedDict(
    "_OptionalStackTypeDef",
    {
        "StackId": str,
        "ChangeSetId": str,
        "Description": str,
        "Parameters": List["ParameterTypeDef"],
        "DeletionTime": datetime,
        "LastUpdatedTime": datetime,
        "RollbackConfiguration": "RollbackConfigurationTypeDef",
        "StackStatusReason": str,
        "DisableRollback": bool,
        "NotificationARNs": List[str],
        "TimeoutInMinutes": int,
        "Capabilities": List[CapabilityType],
        "Outputs": List["OutputTypeDef"],
        "RoleARN": str,
        "Tags": List["TagTypeDef"],
        "EnableTerminationProtection": bool,
        "ParentId": str,
        "RootId": str,
        "DriftInformation": "StackDriftInformationTypeDef",
    },
    total=False,
)

class StackTypeDef(_RequiredStackTypeDef, _OptionalStackTypeDef):
    pass

_RequiredStopStackSetOperationInputRequestTypeDef = TypedDict(
    "_RequiredStopStackSetOperationInputRequestTypeDef",
    {
        "StackSetName": str,
        "OperationId": str,
    },
)
_OptionalStopStackSetOperationInputRequestTypeDef = TypedDict(
    "_OptionalStopStackSetOperationInputRequestTypeDef",
    {
        "CallAs": CallAsType,
    },
    total=False,
)

class StopStackSetOperationInputRequestTypeDef(
    _RequiredStopStackSetOperationInputRequestTypeDef,
    _OptionalStopStackSetOperationInputRequestTypeDef,
):
    pass

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TemplateParameterTypeDef = TypedDict(
    "TemplateParameterTypeDef",
    {
        "ParameterKey": str,
        "DefaultValue": str,
        "NoEcho": bool,
        "Description": str,
    },
    total=False,
)

TestTypeInputRequestTypeDef = TypedDict(
    "TestTypeInputRequestTypeDef",
    {
        "Arn": str,
        "Type": ThirdPartyTypeType,
        "TypeName": str,
        "VersionId": str,
        "LogDeliveryBucket": str,
    },
    total=False,
)

TestTypeOutputTypeDef = TypedDict(
    "TestTypeOutputTypeDef",
    {
        "TypeVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TypeConfigurationDetailsTypeDef = TypedDict(
    "TypeConfigurationDetailsTypeDef",
    {
        "Arn": str,
        "Alias": str,
        "Configuration": str,
        "LastUpdated": datetime,
        "TypeArn": str,
        "TypeName": str,
        "IsDefaultConfiguration": bool,
    },
    total=False,
)

TypeConfigurationIdentifierTypeDef = TypedDict(
    "TypeConfigurationIdentifierTypeDef",
    {
        "TypeArn": str,
        "TypeConfigurationAlias": str,
        "TypeConfigurationArn": str,
        "Type": ThirdPartyTypeType,
        "TypeName": str,
    },
    total=False,
)

TypeFiltersTypeDef = TypedDict(
    "TypeFiltersTypeDef",
    {
        "Category": CategoryType,
        "PublisherId": str,
        "TypeNamePrefix": str,
    },
    total=False,
)

TypeSummaryTypeDef = TypedDict(
    "TypeSummaryTypeDef",
    {
        "Type": RegistryTypeType,
        "TypeName": str,
        "DefaultVersionId": str,
        "TypeArn": str,
        "LastUpdated": datetime,
        "Description": str,
        "PublisherId": str,
        "OriginalTypeName": str,
        "PublicVersionNumber": str,
        "LatestPublicVersion": str,
        "PublisherIdentity": IdentityProviderType,
        "PublisherName": str,
        "IsActivated": bool,
    },
    total=False,
)

TypeVersionSummaryTypeDef = TypedDict(
    "TypeVersionSummaryTypeDef",
    {
        "Type": RegistryTypeType,
        "TypeName": str,
        "VersionId": str,
        "IsDefaultVersion": bool,
        "Arn": str,
        "TimeCreated": datetime,
        "Description": str,
        "PublicVersionNumber": str,
    },
    total=False,
)

_RequiredUpdateStackInputRequestTypeDef = TypedDict(
    "_RequiredUpdateStackInputRequestTypeDef",
    {
        "StackName": str,
    },
)
_OptionalUpdateStackInputRequestTypeDef = TypedDict(
    "_OptionalUpdateStackInputRequestTypeDef",
    {
        "TemplateBody": str,
        "TemplateURL": str,
        "UsePreviousTemplate": bool,
        "StackPolicyDuringUpdateBody": str,
        "StackPolicyDuringUpdateURL": str,
        "Parameters": List["ParameterTypeDef"],
        "Capabilities": List[CapabilityType],
        "ResourceTypes": List[str],
        "RoleARN": str,
        "RollbackConfiguration": "RollbackConfigurationTypeDef",
        "StackPolicyBody": str,
        "StackPolicyURL": str,
        "NotificationARNs": List[str],
        "Tags": List["TagTypeDef"],
        "ClientRequestToken": str,
    },
    total=False,
)

class UpdateStackInputRequestTypeDef(
    _RequiredUpdateStackInputRequestTypeDef, _OptionalUpdateStackInputRequestTypeDef
):
    pass

UpdateStackInputStackTypeDef = TypedDict(
    "UpdateStackInputStackTypeDef",
    {
        "TemplateBody": str,
        "TemplateURL": str,
        "UsePreviousTemplate": bool,
        "StackPolicyDuringUpdateBody": str,
        "StackPolicyDuringUpdateURL": str,
        "Parameters": List["ParameterTypeDef"],
        "Capabilities": List[CapabilityType],
        "ResourceTypes": List[str],
        "RoleARN": str,
        "RollbackConfiguration": "RollbackConfigurationTypeDef",
        "StackPolicyBody": str,
        "StackPolicyURL": str,
        "NotificationARNs": List[str],
        "Tags": List["TagTypeDef"],
        "ClientRequestToken": str,
    },
    total=False,
)

_RequiredUpdateStackInstancesInputRequestTypeDef = TypedDict(
    "_RequiredUpdateStackInstancesInputRequestTypeDef",
    {
        "StackSetName": str,
        "Regions": List[str],
    },
)
_OptionalUpdateStackInstancesInputRequestTypeDef = TypedDict(
    "_OptionalUpdateStackInstancesInputRequestTypeDef",
    {
        "Accounts": List[str],
        "DeploymentTargets": "DeploymentTargetsTypeDef",
        "ParameterOverrides": List["ParameterTypeDef"],
        "OperationPreferences": "StackSetOperationPreferencesTypeDef",
        "OperationId": str,
        "CallAs": CallAsType,
    },
    total=False,
)

class UpdateStackInstancesInputRequestTypeDef(
    _RequiredUpdateStackInstancesInputRequestTypeDef,
    _OptionalUpdateStackInstancesInputRequestTypeDef,
):
    pass

UpdateStackInstancesOutputTypeDef = TypedDict(
    "UpdateStackInstancesOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateStackOutputTypeDef = TypedDict(
    "UpdateStackOutputTypeDef",
    {
        "StackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateStackSetInputRequestTypeDef = TypedDict(
    "_RequiredUpdateStackSetInputRequestTypeDef",
    {
        "StackSetName": str,
    },
)
_OptionalUpdateStackSetInputRequestTypeDef = TypedDict(
    "_OptionalUpdateStackSetInputRequestTypeDef",
    {
        "Description": str,
        "TemplateBody": str,
        "TemplateURL": str,
        "UsePreviousTemplate": bool,
        "Parameters": List["ParameterTypeDef"],
        "Capabilities": List[CapabilityType],
        "Tags": List["TagTypeDef"],
        "OperationPreferences": "StackSetOperationPreferencesTypeDef",
        "AdministrationRoleARN": str,
        "ExecutionRoleName": str,
        "DeploymentTargets": "DeploymentTargetsTypeDef",
        "PermissionModel": PermissionModelsType,
        "AutoDeployment": "AutoDeploymentTypeDef",
        "OperationId": str,
        "Accounts": List[str],
        "Regions": List[str],
        "CallAs": CallAsType,
    },
    total=False,
)

class UpdateStackSetInputRequestTypeDef(
    _RequiredUpdateStackSetInputRequestTypeDef, _OptionalUpdateStackSetInputRequestTypeDef
):
    pass

UpdateStackSetOutputTypeDef = TypedDict(
    "UpdateStackSetOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTerminationProtectionInputRequestTypeDef = TypedDict(
    "UpdateTerminationProtectionInputRequestTypeDef",
    {
        "EnableTerminationProtection": bool,
        "StackName": str,
    },
)

UpdateTerminationProtectionOutputTypeDef = TypedDict(
    "UpdateTerminationProtectionOutputTypeDef",
    {
        "StackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValidateTemplateInputRequestTypeDef = TypedDict(
    "ValidateTemplateInputRequestTypeDef",
    {
        "TemplateBody": str,
        "TemplateURL": str,
    },
    total=False,
)

ValidateTemplateOutputTypeDef = TypedDict(
    "ValidateTemplateOutputTypeDef",
    {
        "Parameters": List["TemplateParameterTypeDef"],
        "Description": str,
        "Capabilities": List[CapabilityType],
        "CapabilitiesReason": str,
        "DeclaredTransforms": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
