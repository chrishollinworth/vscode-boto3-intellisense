"""
Main interface for servicecatalog service type definitions.

Usage::

    ```python
    from mypy_boto3_servicecatalog.type_defs import BudgetDetailTypeDef

    data: BudgetDetailTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BudgetDetailTypeDef",
    "CloudWatchDashboardTypeDef",
    "ConstraintDetailTypeDef",
    "ConstraintSummaryTypeDef",
    "ExecutionParameterTypeDef",
    "FailedServiceActionAssociationTypeDef",
    "LaunchPathSummaryTypeDef",
    "LaunchPathTypeDef",
    "OrganizationNodeTypeDef",
    "ParameterConstraintsTypeDef",
    "PortfolioDetailTypeDef",
    "PrincipalTypeDef",
    "ProductViewAggregationValueTypeDef",
    "ProductViewDetailTypeDef",
    "ProductViewSummaryTypeDef",
    "ProvisionedProductAttributeTypeDef",
    "ProvisionedProductDetailTypeDef",
    "ProvisionedProductPlanDetailsTypeDef",
    "ProvisionedProductPlanSummaryTypeDef",
    "ProvisioningArtifactDetailTypeDef",
    "ProvisioningArtifactOutputTypeDef",
    "ProvisioningArtifactParameterTypeDef",
    "ProvisioningArtifactPreferencesTypeDef",
    "ProvisioningArtifactSummaryTypeDef",
    "ProvisioningArtifactTypeDef",
    "ProvisioningArtifactViewTypeDef",
    "RecordDetailTypeDef",
    "RecordErrorTypeDef",
    "RecordOutputTypeDef",
    "RecordTagTypeDef",
    "ResourceChangeDetailTypeDef",
    "ResourceChangeTypeDef",
    "ResourceDetailTypeDef",
    "ResourceTargetDefinitionTypeDef",
    "ServiceActionDetailTypeDef",
    "ServiceActionSummaryTypeDef",
    "ShareDetailsTypeDef",
    "ShareErrorTypeDef",
    "StackInstanceTypeDef",
    "TagOptionDetailTypeDef",
    "TagOptionSummaryTypeDef",
    "TagTypeDef",
    "UpdateProvisioningParameterTypeDef",
    "UsageInstructionTypeDef",
    "AccessLevelFilterTypeDef",
    "BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef",
    "BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef",
    "CopyProductOutputTypeDef",
    "CreateConstraintOutputTypeDef",
    "CreatePortfolioOutputTypeDef",
    "CreatePortfolioShareOutputTypeDef",
    "CreateProductOutputTypeDef",
    "CreateProvisionedProductPlanOutputTypeDef",
    "CreateProvisioningArtifactOutputTypeDef",
    "CreateServiceActionOutputTypeDef",
    "CreateTagOptionOutputTypeDef",
    "DeletePortfolioShareOutputTypeDef",
    "DescribeConstraintOutputTypeDef",
    "DescribeCopyProductStatusOutputTypeDef",
    "DescribePortfolioOutputTypeDef",
    "DescribePortfolioShareStatusOutputTypeDef",
    "DescribeProductAsAdminOutputTypeDef",
    "DescribeProductOutputTypeDef",
    "DescribeProductViewOutputTypeDef",
    "DescribeProvisionedProductOutputTypeDef",
    "DescribeProvisionedProductPlanOutputTypeDef",
    "DescribeProvisioningArtifactOutputTypeDef",
    "DescribeProvisioningParametersOutputTypeDef",
    "DescribeRecordOutputTypeDef",
    "DescribeServiceActionExecutionParametersOutputTypeDef",
    "DescribeServiceActionOutputTypeDef",
    "DescribeTagOptionOutputTypeDef",
    "ExecuteProvisionedProductPlanOutputTypeDef",
    "ExecuteProvisionedProductServiceActionOutputTypeDef",
    "GetAWSOrganizationsAccessStatusOutputTypeDef",
    "ListAcceptedPortfolioSharesOutputTypeDef",
    "ListBudgetsForResourceOutputTypeDef",
    "ListConstraintsForPortfolioOutputTypeDef",
    "ListLaunchPathsOutputTypeDef",
    "ListOrganizationPortfolioAccessOutputTypeDef",
    "ListPortfolioAccessOutputTypeDef",
    "ListPortfoliosForProductOutputTypeDef",
    "ListPortfoliosOutputTypeDef",
    "ListPrincipalsForPortfolioOutputTypeDef",
    "ListProvisionedProductPlansOutputTypeDef",
    "ListProvisioningArtifactsForServiceActionOutputTypeDef",
    "ListProvisioningArtifactsOutputTypeDef",
    "ListRecordHistoryOutputTypeDef",
    "ListRecordHistorySearchFilterTypeDef",
    "ListResourcesForTagOptionOutputTypeDef",
    "ListServiceActionsForProvisioningArtifactOutputTypeDef",
    "ListServiceActionsOutputTypeDef",
    "ListStackInstancesForProvisionedProductOutputTypeDef",
    "ListTagOptionsFiltersTypeDef",
    "ListTagOptionsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ProvisionProductOutputTypeDef",
    "ProvisioningArtifactPropertiesTypeDef",
    "ProvisioningParameterTypeDef",
    "ProvisioningPreferencesTypeDef",
    "ScanProvisionedProductsOutputTypeDef",
    "SearchProductsAsAdminOutputTypeDef",
    "SearchProductsOutputTypeDef",
    "SearchProvisionedProductsOutputTypeDef",
    "ServiceActionAssociationTypeDef",
    "TerminateProvisionedProductOutputTypeDef",
    "UpdateConstraintOutputTypeDef",
    "UpdatePortfolioOutputTypeDef",
    "UpdateProductOutputTypeDef",
    "UpdateProvisionedProductOutputTypeDef",
    "UpdateProvisionedProductPropertiesOutputTypeDef",
    "UpdateProvisioningArtifactOutputTypeDef",
    "UpdateProvisioningPreferencesTypeDef",
    "UpdateServiceActionOutputTypeDef",
    "UpdateTagOptionOutputTypeDef",
)

BudgetDetailTypeDef = TypedDict("BudgetDetailTypeDef", {"BudgetName": str}, total=False)

CloudWatchDashboardTypeDef = TypedDict("CloudWatchDashboardTypeDef", {"Name": str}, total=False)

ConstraintDetailTypeDef = TypedDict(
    "ConstraintDetailTypeDef",
    {
        "ConstraintId": str,
        "Type": str,
        "Description": str,
        "Owner": str,
        "ProductId": str,
        "PortfolioId": str,
    },
    total=False,
)

ConstraintSummaryTypeDef = TypedDict(
    "ConstraintSummaryTypeDef", {"Type": str, "Description": str}, total=False
)

ExecutionParameterTypeDef = TypedDict(
    "ExecutionParameterTypeDef", {"Name": str, "Type": str, "DefaultValues": List[str]}, total=False
)

FailedServiceActionAssociationTypeDef = TypedDict(
    "FailedServiceActionAssociationTypeDef",
    {
        "ServiceActionId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "ErrorCode": Literal[
            "DUPLICATE_RESOURCE",
            "INTERNAL_FAILURE",
            "LIMIT_EXCEEDED",
            "RESOURCE_NOT_FOUND",
            "THROTTLING",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

LaunchPathSummaryTypeDef = TypedDict(
    "LaunchPathSummaryTypeDef",
    {
        "Id": str,
        "ConstraintSummaries": List["ConstraintSummaryTypeDef"],
        "Tags": List["TagTypeDef"],
        "Name": str,
    },
    total=False,
)

LaunchPathTypeDef = TypedDict("LaunchPathTypeDef", {"Id": str, "Name": str}, total=False)

OrganizationNodeTypeDef = TypedDict(
    "OrganizationNodeTypeDef",
    {"Type": Literal["ORGANIZATION", "ORGANIZATIONAL_UNIT", "ACCOUNT"], "Value": str},
    total=False,
)

ParameterConstraintsTypeDef = TypedDict(
    "ParameterConstraintsTypeDef", {"AllowedValues": List[str]}, total=False
)

PortfolioDetailTypeDef = TypedDict(
    "PortfolioDetailTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)

PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef", {"PrincipalARN": str, "PrincipalType": Literal["IAM"]}, total=False
)

ProductViewAggregationValueTypeDef = TypedDict(
    "ProductViewAggregationValueTypeDef", {"Value": str, "ApproximateCount": int}, total=False
)

ProductViewDetailTypeDef = TypedDict(
    "ProductViewDetailTypeDef",
    {
        "ProductViewSummary": "ProductViewSummaryTypeDef",
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
        "ProductARN": str,
        "CreatedTime": datetime,
    },
    total=False,
)

ProductViewSummaryTypeDef = TypedDict(
    "ProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"],
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)

ProvisionedProductAttributeTypeDef = TypedDict(
    "ProvisionedProductAttributeTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Type": str,
        "Id": str,
        "Status": Literal["AVAILABLE", "UNDER_CHANGE", "TAINTED", "ERROR", "PLAN_IN_PROGRESS"],
        "StatusMessage": str,
        "CreatedTime": datetime,
        "IdempotencyToken": str,
        "LastRecordId": str,
        "LastProvisioningRecordId": str,
        "LastSuccessfulProvisioningRecordId": str,
        "Tags": List["TagTypeDef"],
        "PhysicalId": str,
        "ProductId": str,
        "ProductName": str,
        "ProvisioningArtifactId": str,
        "ProvisioningArtifactName": str,
        "UserArn": str,
        "UserArnSession": str,
    },
    total=False,
)

ProvisionedProductDetailTypeDef = TypedDict(
    "ProvisionedProductDetailTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Type": str,
        "Id": str,
        "Status": Literal["AVAILABLE", "UNDER_CHANGE", "TAINTED", "ERROR", "PLAN_IN_PROGRESS"],
        "StatusMessage": str,
        "CreatedTime": datetime,
        "IdempotencyToken": str,
        "LastRecordId": str,
        "LastProvisioningRecordId": str,
        "LastSuccessfulProvisioningRecordId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
    },
    total=False,
)

ProvisionedProductPlanDetailsTypeDef = TypedDict(
    "ProvisionedProductPlanDetailsTypeDef",
    {
        "CreatedTime": datetime,
        "PathId": str,
        "ProductId": str,
        "PlanName": str,
        "PlanId": str,
        "ProvisionProductId": str,
        "ProvisionProductName": str,
        "PlanType": Literal["CLOUDFORMATION"],
        "ProvisioningArtifactId": str,
        "Status": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_SUCCESS",
            "CREATE_FAILED",
            "EXECUTE_IN_PROGRESS",
            "EXECUTE_SUCCESS",
            "EXECUTE_FAILED",
        ],
        "UpdatedTime": datetime,
        "NotificationArns": List[str],
        "ProvisioningParameters": List["UpdateProvisioningParameterTypeDef"],
        "Tags": List["TagTypeDef"],
        "StatusMessage": str,
    },
    total=False,
)

ProvisionedProductPlanSummaryTypeDef = TypedDict(
    "ProvisionedProductPlanSummaryTypeDef",
    {
        "PlanName": str,
        "PlanId": str,
        "ProvisionProductId": str,
        "ProvisionProductName": str,
        "PlanType": Literal["CLOUDFORMATION"],
        "ProvisioningArtifactId": str,
    },
    total=False,
)

ProvisioningArtifactDetailTypeDef = TypedDict(
    "ProvisioningArtifactDetailTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE_AMI", "MARKETPLACE_CAR"],
        "CreatedTime": datetime,
        "Active": bool,
        "Guidance": Literal["DEFAULT", "DEPRECATED"],
    },
    total=False,
)

ProvisioningArtifactOutputTypeDef = TypedDict(
    "ProvisioningArtifactOutputTypeDef", {"Key": str, "Description": str}, total=False
)

ProvisioningArtifactParameterTypeDef = TypedDict(
    "ProvisioningArtifactParameterTypeDef",
    {
        "ParameterKey": str,
        "DefaultValue": str,
        "ParameterType": str,
        "IsNoEcho": bool,
        "Description": str,
        "ParameterConstraints": "ParameterConstraintsTypeDef",
    },
    total=False,
)

ProvisioningArtifactPreferencesTypeDef = TypedDict(
    "ProvisioningArtifactPreferencesTypeDef",
    {"StackSetAccounts": List[str], "StackSetRegions": List[str]},
    total=False,
)

ProvisioningArtifactSummaryTypeDef = TypedDict(
    "ProvisioningArtifactSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProvisioningArtifactMetadata": Dict[str, str],
    },
    total=False,
)

ProvisioningArtifactTypeDef = TypedDict(
    "ProvisioningArtifactTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "CreatedTime": datetime,
        "Guidance": Literal["DEFAULT", "DEPRECATED"],
    },
    total=False,
)

ProvisioningArtifactViewTypeDef = TypedDict(
    "ProvisioningArtifactViewTypeDef",
    {
        "ProductViewSummary": "ProductViewSummaryTypeDef",
        "ProvisioningArtifact": "ProvisioningArtifactTypeDef",
    },
    total=False,
)

RecordDetailTypeDef = TypedDict(
    "RecordDetailTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": Literal["CREATED", "IN_PROGRESS", "IN_PROGRESS_IN_ERROR", "SUCCEEDED", "FAILED"],
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List["RecordErrorTypeDef"],
        "RecordTags": List["RecordTagTypeDef"],
    },
    total=False,
)

RecordErrorTypeDef = TypedDict("RecordErrorTypeDef", {"Code": str, "Description": str}, total=False)

RecordOutputTypeDef = TypedDict(
    "RecordOutputTypeDef", {"OutputKey": str, "OutputValue": str, "Description": str}, total=False
)

RecordTagTypeDef = TypedDict("RecordTagTypeDef", {"Key": str, "Value": str}, total=False)

ResourceChangeDetailTypeDef = TypedDict(
    "ResourceChangeDetailTypeDef",
    {
        "Target": "ResourceTargetDefinitionTypeDef",
        "Evaluation": Literal["STATIC", "DYNAMIC"],
        "CausingEntity": str,
    },
    total=False,
)

ResourceChangeTypeDef = TypedDict(
    "ResourceChangeTypeDef",
    {
        "Action": Literal["ADD", "MODIFY", "REMOVE"],
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Replacement": Literal["TRUE", "FALSE", "CONDITIONAL"],
        "Scope": List[
            Literal[
                "PROPERTIES", "METADATA", "CREATIONPOLICY", "UPDATEPOLICY", "DELETIONPOLICY", "TAGS"
            ]
        ],
        "Details": List["ResourceChangeDetailTypeDef"],
    },
    total=False,
)

ResourceDetailTypeDef = TypedDict(
    "ResourceDetailTypeDef",
    {"Id": str, "ARN": str, "Name": str, "Description": str, "CreatedTime": datetime},
    total=False,
)

ResourceTargetDefinitionTypeDef = TypedDict(
    "ResourceTargetDefinitionTypeDef",
    {
        "Attribute": Literal[
            "PROPERTIES", "METADATA", "CREATIONPOLICY", "UPDATEPOLICY", "DELETIONPOLICY", "TAGS"
        ],
        "Name": str,
        "RequiresRecreation": Literal["NEVER", "CONDITIONALLY", "ALWAYS"],
    },
    total=False,
)

ServiceActionDetailTypeDef = TypedDict(
    "ServiceActionDetailTypeDef",
    {
        "ServiceActionSummary": "ServiceActionSummaryTypeDef",
        "Definition": Dict[Literal["Name", "Version", "AssumeRole", "Parameters"], str],
    },
    total=False,
)

ServiceActionSummaryTypeDef = TypedDict(
    "ServiceActionSummaryTypeDef",
    {"Id": str, "Name": str, "Description": str, "DefinitionType": Literal["SSM_AUTOMATION"]},
    total=False,
)

ShareDetailsTypeDef = TypedDict(
    "ShareDetailsTypeDef",
    {"SuccessfulShares": List[str], "ShareErrors": List["ShareErrorTypeDef"]},
    total=False,
)

ShareErrorTypeDef = TypedDict(
    "ShareErrorTypeDef", {"Accounts": List[str], "Message": str, "Error": str}, total=False
)

StackInstanceTypeDef = TypedDict(
    "StackInstanceTypeDef",
    {
        "Account": str,
        "Region": str,
        "StackInstanceStatus": Literal["CURRENT", "OUTDATED", "INOPERABLE"],
    },
    total=False,
)

TagOptionDetailTypeDef = TypedDict(
    "TagOptionDetailTypeDef", {"Key": str, "Value": str, "Active": bool, "Id": str}, total=False
)

TagOptionSummaryTypeDef = TypedDict(
    "TagOptionSummaryTypeDef", {"Key": str, "Values": List[str]}, total=False
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

UpdateProvisioningParameterTypeDef = TypedDict(
    "UpdateProvisioningParameterTypeDef",
    {"Key": str, "Value": str, "UsePreviousValue": bool},
    total=False,
)

UsageInstructionTypeDef = TypedDict(
    "UsageInstructionTypeDef", {"Type": str, "Value": str}, total=False
)

AccessLevelFilterTypeDef = TypedDict(
    "AccessLevelFilterTypeDef",
    {"Key": Literal["Account", "Role", "User"], "Value": str},
    total=False,
)

BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef = TypedDict(
    "BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef",
    {"FailedServiceActionAssociations": List["FailedServiceActionAssociationTypeDef"]},
    total=False,
)

BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef = TypedDict(
    "BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef",
    {"FailedServiceActionAssociations": List["FailedServiceActionAssociationTypeDef"]},
    total=False,
)

CopyProductOutputTypeDef = TypedDict(
    "CopyProductOutputTypeDef", {"CopyProductToken": str}, total=False
)

CreateConstraintOutputTypeDef = TypedDict(
    "CreateConstraintOutputTypeDef",
    {
        "ConstraintDetail": "ConstraintDetailTypeDef",
        "ConstraintParameters": str,
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
    },
    total=False,
)

CreatePortfolioOutputTypeDef = TypedDict(
    "CreatePortfolioOutputTypeDef",
    {"PortfolioDetail": "PortfolioDetailTypeDef", "Tags": List["TagTypeDef"]},
    total=False,
)

CreatePortfolioShareOutputTypeDef = TypedDict(
    "CreatePortfolioShareOutputTypeDef", {"PortfolioShareToken": str}, total=False
)

CreateProductOutputTypeDef = TypedDict(
    "CreateProductOutputTypeDef",
    {
        "ProductViewDetail": "ProductViewDetailTypeDef",
        "ProvisioningArtifactDetail": "ProvisioningArtifactDetailTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

CreateProvisionedProductPlanOutputTypeDef = TypedDict(
    "CreateProvisionedProductPlanOutputTypeDef",
    {
        "PlanName": str,
        "PlanId": str,
        "ProvisionProductId": str,
        "ProvisionedProductName": str,
        "ProvisioningArtifactId": str,
    },
    total=False,
)

CreateProvisioningArtifactOutputTypeDef = TypedDict(
    "CreateProvisioningArtifactOutputTypeDef",
    {
        "ProvisioningArtifactDetail": "ProvisioningArtifactDetailTypeDef",
        "Info": Dict[str, str],
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
    },
    total=False,
)

CreateServiceActionOutputTypeDef = TypedDict(
    "CreateServiceActionOutputTypeDef",
    {"ServiceActionDetail": "ServiceActionDetailTypeDef"},
    total=False,
)

CreateTagOptionOutputTypeDef = TypedDict(
    "CreateTagOptionOutputTypeDef", {"TagOptionDetail": "TagOptionDetailTypeDef"}, total=False
)

DeletePortfolioShareOutputTypeDef = TypedDict(
    "DeletePortfolioShareOutputTypeDef", {"PortfolioShareToken": str}, total=False
)

DescribeConstraintOutputTypeDef = TypedDict(
    "DescribeConstraintOutputTypeDef",
    {
        "ConstraintDetail": "ConstraintDetailTypeDef",
        "ConstraintParameters": str,
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
    },
    total=False,
)

DescribeCopyProductStatusOutputTypeDef = TypedDict(
    "DescribeCopyProductStatusOutputTypeDef",
    {
        "CopyProductStatus": Literal["SUCCEEDED", "IN_PROGRESS", "FAILED"],
        "TargetProductId": str,
        "StatusDetail": str,
    },
    total=False,
)

DescribePortfolioOutputTypeDef = TypedDict(
    "DescribePortfolioOutputTypeDef",
    {
        "PortfolioDetail": "PortfolioDetailTypeDef",
        "Tags": List["TagTypeDef"],
        "TagOptions": List["TagOptionDetailTypeDef"],
        "Budgets": List["BudgetDetailTypeDef"],
    },
    total=False,
)

DescribePortfolioShareStatusOutputTypeDef = TypedDict(
    "DescribePortfolioShareStatusOutputTypeDef",
    {
        "PortfolioShareToken": str,
        "PortfolioId": str,
        "OrganizationNodeValue": str,
        "Status": Literal[
            "NOT_STARTED", "IN_PROGRESS", "COMPLETED", "COMPLETED_WITH_ERRORS", "ERROR"
        ],
        "ShareDetails": "ShareDetailsTypeDef",
    },
    total=False,
)

DescribeProductAsAdminOutputTypeDef = TypedDict(
    "DescribeProductAsAdminOutputTypeDef",
    {
        "ProductViewDetail": "ProductViewDetailTypeDef",
        "ProvisioningArtifactSummaries": List["ProvisioningArtifactSummaryTypeDef"],
        "Tags": List["TagTypeDef"],
        "TagOptions": List["TagOptionDetailTypeDef"],
        "Budgets": List["BudgetDetailTypeDef"],
    },
    total=False,
)

DescribeProductOutputTypeDef = TypedDict(
    "DescribeProductOutputTypeDef",
    {
        "ProductViewSummary": "ProductViewSummaryTypeDef",
        "ProvisioningArtifacts": List["ProvisioningArtifactTypeDef"],
        "Budgets": List["BudgetDetailTypeDef"],
        "LaunchPaths": List["LaunchPathTypeDef"],
    },
    total=False,
)

DescribeProductViewOutputTypeDef = TypedDict(
    "DescribeProductViewOutputTypeDef",
    {
        "ProductViewSummary": "ProductViewSummaryTypeDef",
        "ProvisioningArtifacts": List["ProvisioningArtifactTypeDef"],
    },
    total=False,
)

DescribeProvisionedProductOutputTypeDef = TypedDict(
    "DescribeProvisionedProductOutputTypeDef",
    {
        "ProvisionedProductDetail": "ProvisionedProductDetailTypeDef",
        "CloudWatchDashboards": List["CloudWatchDashboardTypeDef"],
    },
    total=False,
)

DescribeProvisionedProductPlanOutputTypeDef = TypedDict(
    "DescribeProvisionedProductPlanOutputTypeDef",
    {
        "ProvisionedProductPlanDetails": "ProvisionedProductPlanDetailsTypeDef",
        "ResourceChanges": List["ResourceChangeTypeDef"],
        "NextPageToken": str,
    },
    total=False,
)

DescribeProvisioningArtifactOutputTypeDef = TypedDict(
    "DescribeProvisioningArtifactOutputTypeDef",
    {
        "ProvisioningArtifactDetail": "ProvisioningArtifactDetailTypeDef",
        "Info": Dict[str, str],
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
    },
    total=False,
)

DescribeProvisioningParametersOutputTypeDef = TypedDict(
    "DescribeProvisioningParametersOutputTypeDef",
    {
        "ProvisioningArtifactParameters": List["ProvisioningArtifactParameterTypeDef"],
        "ConstraintSummaries": List["ConstraintSummaryTypeDef"],
        "UsageInstructions": List["UsageInstructionTypeDef"],
        "TagOptions": List["TagOptionSummaryTypeDef"],
        "ProvisioningArtifactPreferences": "ProvisioningArtifactPreferencesTypeDef",
        "ProvisioningArtifactOutputs": List["ProvisioningArtifactOutputTypeDef"],
    },
    total=False,
)

DescribeRecordOutputTypeDef = TypedDict(
    "DescribeRecordOutputTypeDef",
    {
        "RecordDetail": "RecordDetailTypeDef",
        "RecordOutputs": List["RecordOutputTypeDef"],
        "NextPageToken": str,
    },
    total=False,
)

DescribeServiceActionExecutionParametersOutputTypeDef = TypedDict(
    "DescribeServiceActionExecutionParametersOutputTypeDef",
    {"ServiceActionParameters": List["ExecutionParameterTypeDef"]},
    total=False,
)

DescribeServiceActionOutputTypeDef = TypedDict(
    "DescribeServiceActionOutputTypeDef",
    {"ServiceActionDetail": "ServiceActionDetailTypeDef"},
    total=False,
)

DescribeTagOptionOutputTypeDef = TypedDict(
    "DescribeTagOptionOutputTypeDef", {"TagOptionDetail": "TagOptionDetailTypeDef"}, total=False
)

ExecuteProvisionedProductPlanOutputTypeDef = TypedDict(
    "ExecuteProvisionedProductPlanOutputTypeDef",
    {"RecordDetail": "RecordDetailTypeDef"},
    total=False,
)

ExecuteProvisionedProductServiceActionOutputTypeDef = TypedDict(
    "ExecuteProvisionedProductServiceActionOutputTypeDef",
    {"RecordDetail": "RecordDetailTypeDef"},
    total=False,
)

GetAWSOrganizationsAccessStatusOutputTypeDef = TypedDict(
    "GetAWSOrganizationsAccessStatusOutputTypeDef",
    {"AccessStatus": Literal["ENABLED", "UNDER_CHANGE", "DISABLED"]},
    total=False,
)

ListAcceptedPortfolioSharesOutputTypeDef = TypedDict(
    "ListAcceptedPortfolioSharesOutputTypeDef",
    {"PortfolioDetails": List["PortfolioDetailTypeDef"], "NextPageToken": str},
    total=False,
)

ListBudgetsForResourceOutputTypeDef = TypedDict(
    "ListBudgetsForResourceOutputTypeDef",
    {"Budgets": List["BudgetDetailTypeDef"], "NextPageToken": str},
    total=False,
)

ListConstraintsForPortfolioOutputTypeDef = TypedDict(
    "ListConstraintsForPortfolioOutputTypeDef",
    {"ConstraintDetails": List["ConstraintDetailTypeDef"], "NextPageToken": str},
    total=False,
)

ListLaunchPathsOutputTypeDef = TypedDict(
    "ListLaunchPathsOutputTypeDef",
    {"LaunchPathSummaries": List["LaunchPathSummaryTypeDef"], "NextPageToken": str},
    total=False,
)

ListOrganizationPortfolioAccessOutputTypeDef = TypedDict(
    "ListOrganizationPortfolioAccessOutputTypeDef",
    {"OrganizationNodes": List["OrganizationNodeTypeDef"], "NextPageToken": str},
    total=False,
)

ListPortfolioAccessOutputTypeDef = TypedDict(
    "ListPortfolioAccessOutputTypeDef", {"AccountIds": List[str], "NextPageToken": str}, total=False
)

ListPortfoliosForProductOutputTypeDef = TypedDict(
    "ListPortfoliosForProductOutputTypeDef",
    {"PortfolioDetails": List["PortfolioDetailTypeDef"], "NextPageToken": str},
    total=False,
)

ListPortfoliosOutputTypeDef = TypedDict(
    "ListPortfoliosOutputTypeDef",
    {"PortfolioDetails": List["PortfolioDetailTypeDef"], "NextPageToken": str},
    total=False,
)

ListPrincipalsForPortfolioOutputTypeDef = TypedDict(
    "ListPrincipalsForPortfolioOutputTypeDef",
    {"Principals": List["PrincipalTypeDef"], "NextPageToken": str},
    total=False,
)

ListProvisionedProductPlansOutputTypeDef = TypedDict(
    "ListProvisionedProductPlansOutputTypeDef",
    {"ProvisionedProductPlans": List["ProvisionedProductPlanSummaryTypeDef"], "NextPageToken": str},
    total=False,
)

ListProvisioningArtifactsForServiceActionOutputTypeDef = TypedDict(
    "ListProvisioningArtifactsForServiceActionOutputTypeDef",
    {"ProvisioningArtifactViews": List["ProvisioningArtifactViewTypeDef"], "NextPageToken": str},
    total=False,
)

ListProvisioningArtifactsOutputTypeDef = TypedDict(
    "ListProvisioningArtifactsOutputTypeDef",
    {
        "ProvisioningArtifactDetails": List["ProvisioningArtifactDetailTypeDef"],
        "NextPageToken": str,
    },
    total=False,
)

ListRecordHistoryOutputTypeDef = TypedDict(
    "ListRecordHistoryOutputTypeDef",
    {"RecordDetails": List["RecordDetailTypeDef"], "NextPageToken": str},
    total=False,
)

ListRecordHistorySearchFilterTypeDef = TypedDict(
    "ListRecordHistorySearchFilterTypeDef", {"Key": str, "Value": str}, total=False
)

ListResourcesForTagOptionOutputTypeDef = TypedDict(
    "ListResourcesForTagOptionOutputTypeDef",
    {"ResourceDetails": List["ResourceDetailTypeDef"], "PageToken": str},
    total=False,
)

ListServiceActionsForProvisioningArtifactOutputTypeDef = TypedDict(
    "ListServiceActionsForProvisioningArtifactOutputTypeDef",
    {"ServiceActionSummaries": List["ServiceActionSummaryTypeDef"], "NextPageToken": str},
    total=False,
)

ListServiceActionsOutputTypeDef = TypedDict(
    "ListServiceActionsOutputTypeDef",
    {"ServiceActionSummaries": List["ServiceActionSummaryTypeDef"], "NextPageToken": str},
    total=False,
)

ListStackInstancesForProvisionedProductOutputTypeDef = TypedDict(
    "ListStackInstancesForProvisionedProductOutputTypeDef",
    {"StackInstances": List["StackInstanceTypeDef"], "NextPageToken": str},
    total=False,
)

ListTagOptionsFiltersTypeDef = TypedDict(
    "ListTagOptionsFiltersTypeDef", {"Key": str, "Value": str, "Active": bool}, total=False
)

ListTagOptionsOutputTypeDef = TypedDict(
    "ListTagOptionsOutputTypeDef",
    {"TagOptionDetails": List["TagOptionDetailTypeDef"], "PageToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

ProvisionProductOutputTypeDef = TypedDict(
    "ProvisionProductOutputTypeDef", {"RecordDetail": "RecordDetailTypeDef"}, total=False
)

_RequiredProvisioningArtifactPropertiesTypeDef = TypedDict(
    "_RequiredProvisioningArtifactPropertiesTypeDef", {"Info": Dict[str, str]}
)
_OptionalProvisioningArtifactPropertiesTypeDef = TypedDict(
    "_OptionalProvisioningArtifactPropertiesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE_AMI", "MARKETPLACE_CAR"],
        "DisableTemplateValidation": bool,
    },
    total=False,
)


class ProvisioningArtifactPropertiesTypeDef(
    _RequiredProvisioningArtifactPropertiesTypeDef, _OptionalProvisioningArtifactPropertiesTypeDef
):
    pass


ProvisioningParameterTypeDef = TypedDict(
    "ProvisioningParameterTypeDef", {"Key": str, "Value": str}, total=False
)

ProvisioningPreferencesTypeDef = TypedDict(
    "ProvisioningPreferencesTypeDef",
    {
        "StackSetAccounts": List[str],
        "StackSetRegions": List[str],
        "StackSetFailureToleranceCount": int,
        "StackSetFailureTolerancePercentage": int,
        "StackSetMaxConcurrencyCount": int,
        "StackSetMaxConcurrencyPercentage": int,
    },
    total=False,
)

ScanProvisionedProductsOutputTypeDef = TypedDict(
    "ScanProvisionedProductsOutputTypeDef",
    {"ProvisionedProducts": List["ProvisionedProductDetailTypeDef"], "NextPageToken": str},
    total=False,
)

SearchProductsAsAdminOutputTypeDef = TypedDict(
    "SearchProductsAsAdminOutputTypeDef",
    {"ProductViewDetails": List["ProductViewDetailTypeDef"], "NextPageToken": str},
    total=False,
)

SearchProductsOutputTypeDef = TypedDict(
    "SearchProductsOutputTypeDef",
    {
        "ProductViewSummaries": List["ProductViewSummaryTypeDef"],
        "ProductViewAggregations": Dict[str, List["ProductViewAggregationValueTypeDef"]],
        "NextPageToken": str,
    },
    total=False,
)

SearchProvisionedProductsOutputTypeDef = TypedDict(
    "SearchProvisionedProductsOutputTypeDef",
    {
        "ProvisionedProducts": List["ProvisionedProductAttributeTypeDef"],
        "TotalResultsCount": int,
        "NextPageToken": str,
    },
    total=False,
)

ServiceActionAssociationTypeDef = TypedDict(
    "ServiceActionAssociationTypeDef",
    {"ServiceActionId": str, "ProductId": str, "ProvisioningArtifactId": str},
)

TerminateProvisionedProductOutputTypeDef = TypedDict(
    "TerminateProvisionedProductOutputTypeDef", {"RecordDetail": "RecordDetailTypeDef"}, total=False
)

UpdateConstraintOutputTypeDef = TypedDict(
    "UpdateConstraintOutputTypeDef",
    {
        "ConstraintDetail": "ConstraintDetailTypeDef",
        "ConstraintParameters": str,
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
    },
    total=False,
)

UpdatePortfolioOutputTypeDef = TypedDict(
    "UpdatePortfolioOutputTypeDef",
    {"PortfolioDetail": "PortfolioDetailTypeDef", "Tags": List["TagTypeDef"]},
    total=False,
)

UpdateProductOutputTypeDef = TypedDict(
    "UpdateProductOutputTypeDef",
    {"ProductViewDetail": "ProductViewDetailTypeDef", "Tags": List["TagTypeDef"]},
    total=False,
)

UpdateProvisionedProductOutputTypeDef = TypedDict(
    "UpdateProvisionedProductOutputTypeDef", {"RecordDetail": "RecordDetailTypeDef"}, total=False
)

UpdateProvisionedProductPropertiesOutputTypeDef = TypedDict(
    "UpdateProvisionedProductPropertiesOutputTypeDef",
    {
        "ProvisionedProductId": str,
        "ProvisionedProductProperties": Dict[Literal["OWNER"], str],
        "RecordId": str,
        "Status": Literal["CREATED", "IN_PROGRESS", "IN_PROGRESS_IN_ERROR", "SUCCEEDED", "FAILED"],
    },
    total=False,
)

UpdateProvisioningArtifactOutputTypeDef = TypedDict(
    "UpdateProvisioningArtifactOutputTypeDef",
    {
        "ProvisioningArtifactDetail": "ProvisioningArtifactDetailTypeDef",
        "Info": Dict[str, str],
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
    },
    total=False,
)

UpdateProvisioningPreferencesTypeDef = TypedDict(
    "UpdateProvisioningPreferencesTypeDef",
    {
        "StackSetAccounts": List[str],
        "StackSetRegions": List[str],
        "StackSetFailureToleranceCount": int,
        "StackSetFailureTolerancePercentage": int,
        "StackSetMaxConcurrencyCount": int,
        "StackSetMaxConcurrencyPercentage": int,
        "StackSetOperationType": Literal["CREATE", "UPDATE", "DELETE"],
    },
    total=False,
)

UpdateServiceActionOutputTypeDef = TypedDict(
    "UpdateServiceActionOutputTypeDef",
    {"ServiceActionDetail": "ServiceActionDetailTypeDef"},
    total=False,
)

UpdateTagOptionOutputTypeDef = TypedDict(
    "UpdateTagOptionOutputTypeDef", {"TagOptionDetail": "TagOptionDetailTypeDef"}, total=False
)
