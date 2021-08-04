"""
Type annotations for servicecatalog service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/type_defs.html)

Usage::

    ```python
    from mypy_boto3_servicecatalog.type_defs import AcceptPortfolioShareInputRequestTypeDef

    data: AcceptPortfolioShareInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AccessLevelFilterKeyType,
    AccessStatusType,
    ChangeActionType,
    CopyProductStatusType,
    DescribePortfolioShareTypeType,
    EvaluationTypeType,
    OrganizationNodeTypeType,
    PortfolioShareTypeType,
    ProductTypeType,
    ProductViewFilterByType,
    ProductViewSortByType,
    PropertyKeyType,
    ProvisionedProductPlanStatusType,
    ProvisionedProductStatusType,
    ProvisioningArtifactGuidanceType,
    ProvisioningArtifactTypeType,
    RecordStatusType,
    ReplacementType,
    RequiresRecreationType,
    ResourceAttributeType,
    ServiceActionAssociationErrorCodeType,
    ServiceActionDefinitionKeyType,
    ShareStatusType,
    SortOrderType,
    StackInstanceStatusType,
    StackSetOperationTypeType,
    StatusType,
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
    "AcceptPortfolioShareInputRequestTypeDef",
    "AccessLevelFilterTypeDef",
    "AssociateBudgetWithResourceInputRequestTypeDef",
    "AssociatePrincipalWithPortfolioInputRequestTypeDef",
    "AssociateProductWithPortfolioInputRequestTypeDef",
    "AssociateServiceActionWithProvisioningArtifactInputRequestTypeDef",
    "AssociateTagOptionWithResourceInputRequestTypeDef",
    "BatchAssociateServiceActionWithProvisioningArtifactInputRequestTypeDef",
    "BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef",
    "BatchDisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef",
    "BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef",
    "BudgetDetailTypeDef",
    "CloudWatchDashboardTypeDef",
    "ConstraintDetailTypeDef",
    "ConstraintSummaryTypeDef",
    "CopyProductInputRequestTypeDef",
    "CopyProductOutputTypeDef",
    "CreateConstraintInputRequestTypeDef",
    "CreateConstraintOutputTypeDef",
    "CreatePortfolioInputRequestTypeDef",
    "CreatePortfolioOutputTypeDef",
    "CreatePortfolioShareInputRequestTypeDef",
    "CreatePortfolioShareOutputTypeDef",
    "CreateProductInputRequestTypeDef",
    "CreateProductOutputTypeDef",
    "CreateProvisionedProductPlanInputRequestTypeDef",
    "CreateProvisionedProductPlanOutputTypeDef",
    "CreateProvisioningArtifactInputRequestTypeDef",
    "CreateProvisioningArtifactOutputTypeDef",
    "CreateServiceActionInputRequestTypeDef",
    "CreateServiceActionOutputTypeDef",
    "CreateTagOptionInputRequestTypeDef",
    "CreateTagOptionOutputTypeDef",
    "DeleteConstraintInputRequestTypeDef",
    "DeletePortfolioInputRequestTypeDef",
    "DeletePortfolioShareInputRequestTypeDef",
    "DeletePortfolioShareOutputTypeDef",
    "DeleteProductInputRequestTypeDef",
    "DeleteProvisionedProductPlanInputRequestTypeDef",
    "DeleteProvisioningArtifactInputRequestTypeDef",
    "DeleteServiceActionInputRequestTypeDef",
    "DeleteTagOptionInputRequestTypeDef",
    "DescribeConstraintInputRequestTypeDef",
    "DescribeConstraintOutputTypeDef",
    "DescribeCopyProductStatusInputRequestTypeDef",
    "DescribeCopyProductStatusOutputTypeDef",
    "DescribePortfolioInputRequestTypeDef",
    "DescribePortfolioOutputTypeDef",
    "DescribePortfolioShareStatusInputRequestTypeDef",
    "DescribePortfolioShareStatusOutputTypeDef",
    "DescribePortfolioSharesInputRequestTypeDef",
    "DescribePortfolioSharesOutputTypeDef",
    "DescribeProductAsAdminInputRequestTypeDef",
    "DescribeProductAsAdminOutputTypeDef",
    "DescribeProductInputRequestTypeDef",
    "DescribeProductOutputTypeDef",
    "DescribeProductViewInputRequestTypeDef",
    "DescribeProductViewOutputTypeDef",
    "DescribeProvisionedProductInputRequestTypeDef",
    "DescribeProvisionedProductOutputTypeDef",
    "DescribeProvisionedProductPlanInputRequestTypeDef",
    "DescribeProvisionedProductPlanOutputTypeDef",
    "DescribeProvisioningArtifactInputRequestTypeDef",
    "DescribeProvisioningArtifactOutputTypeDef",
    "DescribeProvisioningParametersInputRequestTypeDef",
    "DescribeProvisioningParametersOutputTypeDef",
    "DescribeRecordInputRequestTypeDef",
    "DescribeRecordOutputTypeDef",
    "DescribeServiceActionExecutionParametersInputRequestTypeDef",
    "DescribeServiceActionExecutionParametersOutputTypeDef",
    "DescribeServiceActionInputRequestTypeDef",
    "DescribeServiceActionOutputTypeDef",
    "DescribeTagOptionInputRequestTypeDef",
    "DescribeTagOptionOutputTypeDef",
    "DisassociateBudgetFromResourceInputRequestTypeDef",
    "DisassociatePrincipalFromPortfolioInputRequestTypeDef",
    "DisassociateProductFromPortfolioInputRequestTypeDef",
    "DisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef",
    "DisassociateTagOptionFromResourceInputRequestTypeDef",
    "ExecuteProvisionedProductPlanInputRequestTypeDef",
    "ExecuteProvisionedProductPlanOutputTypeDef",
    "ExecuteProvisionedProductServiceActionInputRequestTypeDef",
    "ExecuteProvisionedProductServiceActionOutputTypeDef",
    "ExecutionParameterTypeDef",
    "FailedServiceActionAssociationTypeDef",
    "GetAWSOrganizationsAccessStatusOutputTypeDef",
    "GetProvisionedProductOutputsInputRequestTypeDef",
    "GetProvisionedProductOutputsOutputTypeDef",
    "ImportAsProvisionedProductInputRequestTypeDef",
    "ImportAsProvisionedProductOutputTypeDef",
    "LaunchPathSummaryTypeDef",
    "LaunchPathTypeDef",
    "ListAcceptedPortfolioSharesInputRequestTypeDef",
    "ListAcceptedPortfolioSharesOutputTypeDef",
    "ListBudgetsForResourceInputRequestTypeDef",
    "ListBudgetsForResourceOutputTypeDef",
    "ListConstraintsForPortfolioInputRequestTypeDef",
    "ListConstraintsForPortfolioOutputTypeDef",
    "ListLaunchPathsInputRequestTypeDef",
    "ListLaunchPathsOutputTypeDef",
    "ListOrganizationPortfolioAccessInputRequestTypeDef",
    "ListOrganizationPortfolioAccessOutputTypeDef",
    "ListPortfolioAccessInputRequestTypeDef",
    "ListPortfolioAccessOutputTypeDef",
    "ListPortfoliosForProductInputRequestTypeDef",
    "ListPortfoliosForProductOutputTypeDef",
    "ListPortfoliosInputRequestTypeDef",
    "ListPortfoliosOutputTypeDef",
    "ListPrincipalsForPortfolioInputRequestTypeDef",
    "ListPrincipalsForPortfolioOutputTypeDef",
    "ListProvisionedProductPlansInputRequestTypeDef",
    "ListProvisionedProductPlansOutputTypeDef",
    "ListProvisioningArtifactsForServiceActionInputRequestTypeDef",
    "ListProvisioningArtifactsForServiceActionOutputTypeDef",
    "ListProvisioningArtifactsInputRequestTypeDef",
    "ListProvisioningArtifactsOutputTypeDef",
    "ListRecordHistoryInputRequestTypeDef",
    "ListRecordHistoryOutputTypeDef",
    "ListRecordHistorySearchFilterTypeDef",
    "ListResourcesForTagOptionInputRequestTypeDef",
    "ListResourcesForTagOptionOutputTypeDef",
    "ListServiceActionsForProvisioningArtifactInputRequestTypeDef",
    "ListServiceActionsForProvisioningArtifactOutputTypeDef",
    "ListServiceActionsInputRequestTypeDef",
    "ListServiceActionsOutputTypeDef",
    "ListStackInstancesForProvisionedProductInputRequestTypeDef",
    "ListStackInstancesForProvisionedProductOutputTypeDef",
    "ListTagOptionsFiltersTypeDef",
    "ListTagOptionsInputRequestTypeDef",
    "ListTagOptionsOutputTypeDef",
    "OrganizationNodeTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterConstraintsTypeDef",
    "PortfolioDetailTypeDef",
    "PortfolioShareDetailTypeDef",
    "PrincipalTypeDef",
    "ProductViewAggregationValueTypeDef",
    "ProductViewDetailTypeDef",
    "ProductViewSummaryTypeDef",
    "ProvisionProductInputRequestTypeDef",
    "ProvisionProductOutputTypeDef",
    "ProvisionedProductAttributeTypeDef",
    "ProvisionedProductDetailTypeDef",
    "ProvisionedProductPlanDetailsTypeDef",
    "ProvisionedProductPlanSummaryTypeDef",
    "ProvisioningArtifactDetailTypeDef",
    "ProvisioningArtifactOutputTypeDef",
    "ProvisioningArtifactParameterTypeDef",
    "ProvisioningArtifactPreferencesTypeDef",
    "ProvisioningArtifactPropertiesTypeDef",
    "ProvisioningArtifactSummaryTypeDef",
    "ProvisioningArtifactTypeDef",
    "ProvisioningArtifactViewTypeDef",
    "ProvisioningParameterTypeDef",
    "ProvisioningPreferencesTypeDef",
    "RecordDetailTypeDef",
    "RecordErrorTypeDef",
    "RecordOutputTypeDef",
    "RecordTagTypeDef",
    "RejectPortfolioShareInputRequestTypeDef",
    "ResourceChangeDetailTypeDef",
    "ResourceChangeTypeDef",
    "ResourceDetailTypeDef",
    "ResourceTargetDefinitionTypeDef",
    "ResponseMetadataTypeDef",
    "ScanProvisionedProductsInputRequestTypeDef",
    "ScanProvisionedProductsOutputTypeDef",
    "SearchProductsAsAdminInputRequestTypeDef",
    "SearchProductsAsAdminOutputTypeDef",
    "SearchProductsInputRequestTypeDef",
    "SearchProductsOutputTypeDef",
    "SearchProvisionedProductsInputRequestTypeDef",
    "SearchProvisionedProductsOutputTypeDef",
    "ServiceActionAssociationTypeDef",
    "ServiceActionDetailTypeDef",
    "ServiceActionSummaryTypeDef",
    "ShareDetailsTypeDef",
    "ShareErrorTypeDef",
    "StackInstanceTypeDef",
    "TagOptionDetailTypeDef",
    "TagOptionSummaryTypeDef",
    "TagTypeDef",
    "TerminateProvisionedProductInputRequestTypeDef",
    "TerminateProvisionedProductOutputTypeDef",
    "UpdateConstraintInputRequestTypeDef",
    "UpdateConstraintOutputTypeDef",
    "UpdatePortfolioInputRequestTypeDef",
    "UpdatePortfolioOutputTypeDef",
    "UpdatePortfolioShareInputRequestTypeDef",
    "UpdatePortfolioShareOutputTypeDef",
    "UpdateProductInputRequestTypeDef",
    "UpdateProductOutputTypeDef",
    "UpdateProvisionedProductInputRequestTypeDef",
    "UpdateProvisionedProductOutputTypeDef",
    "UpdateProvisionedProductPropertiesInputRequestTypeDef",
    "UpdateProvisionedProductPropertiesOutputTypeDef",
    "UpdateProvisioningArtifactInputRequestTypeDef",
    "UpdateProvisioningArtifactOutputTypeDef",
    "UpdateProvisioningParameterTypeDef",
    "UpdateProvisioningPreferencesTypeDef",
    "UpdateServiceActionInputRequestTypeDef",
    "UpdateServiceActionOutputTypeDef",
    "UpdateTagOptionInputRequestTypeDef",
    "UpdateTagOptionOutputTypeDef",
    "UsageInstructionTypeDef",
)

_RequiredAcceptPortfolioShareInputRequestTypeDef = TypedDict(
    "_RequiredAcceptPortfolioShareInputRequestTypeDef",
    {
        "PortfolioId": str,
    },
)
_OptionalAcceptPortfolioShareInputRequestTypeDef = TypedDict(
    "_OptionalAcceptPortfolioShareInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "PortfolioShareType": PortfolioShareTypeType,
    },
    total=False,
)

class AcceptPortfolioShareInputRequestTypeDef(
    _RequiredAcceptPortfolioShareInputRequestTypeDef,
    _OptionalAcceptPortfolioShareInputRequestTypeDef,
):
    pass

AccessLevelFilterTypeDef = TypedDict(
    "AccessLevelFilterTypeDef",
    {
        "Key": AccessLevelFilterKeyType,
        "Value": str,
    },
    total=False,
)

AssociateBudgetWithResourceInputRequestTypeDef = TypedDict(
    "AssociateBudgetWithResourceInputRequestTypeDef",
    {
        "BudgetName": str,
        "ResourceId": str,
    },
)

_RequiredAssociatePrincipalWithPortfolioInputRequestTypeDef = TypedDict(
    "_RequiredAssociatePrincipalWithPortfolioInputRequestTypeDef",
    {
        "PortfolioId": str,
        "PrincipalARN": str,
        "PrincipalType": Literal["IAM"],
    },
)
_OptionalAssociatePrincipalWithPortfolioInputRequestTypeDef = TypedDict(
    "_OptionalAssociatePrincipalWithPortfolioInputRequestTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)

class AssociatePrincipalWithPortfolioInputRequestTypeDef(
    _RequiredAssociatePrincipalWithPortfolioInputRequestTypeDef,
    _OptionalAssociatePrincipalWithPortfolioInputRequestTypeDef,
):
    pass

_RequiredAssociateProductWithPortfolioInputRequestTypeDef = TypedDict(
    "_RequiredAssociateProductWithPortfolioInputRequestTypeDef",
    {
        "ProductId": str,
        "PortfolioId": str,
    },
)
_OptionalAssociateProductWithPortfolioInputRequestTypeDef = TypedDict(
    "_OptionalAssociateProductWithPortfolioInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "SourcePortfolioId": str,
    },
    total=False,
)

class AssociateProductWithPortfolioInputRequestTypeDef(
    _RequiredAssociateProductWithPortfolioInputRequestTypeDef,
    _OptionalAssociateProductWithPortfolioInputRequestTypeDef,
):
    pass

_RequiredAssociateServiceActionWithProvisioningArtifactInputRequestTypeDef = TypedDict(
    "_RequiredAssociateServiceActionWithProvisioningArtifactInputRequestTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "ServiceActionId": str,
    },
)
_OptionalAssociateServiceActionWithProvisioningArtifactInputRequestTypeDef = TypedDict(
    "_OptionalAssociateServiceActionWithProvisioningArtifactInputRequestTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)

class AssociateServiceActionWithProvisioningArtifactInputRequestTypeDef(
    _RequiredAssociateServiceActionWithProvisioningArtifactInputRequestTypeDef,
    _OptionalAssociateServiceActionWithProvisioningArtifactInputRequestTypeDef,
):
    pass

AssociateTagOptionWithResourceInputRequestTypeDef = TypedDict(
    "AssociateTagOptionWithResourceInputRequestTypeDef",
    {
        "ResourceId": str,
        "TagOptionId": str,
    },
)

_RequiredBatchAssociateServiceActionWithProvisioningArtifactInputRequestTypeDef = TypedDict(
    "_RequiredBatchAssociateServiceActionWithProvisioningArtifactInputRequestTypeDef",
    {
        "ServiceActionAssociations": List["ServiceActionAssociationTypeDef"],
    },
)
_OptionalBatchAssociateServiceActionWithProvisioningArtifactInputRequestTypeDef = TypedDict(
    "_OptionalBatchAssociateServiceActionWithProvisioningArtifactInputRequestTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)

class BatchAssociateServiceActionWithProvisioningArtifactInputRequestTypeDef(
    _RequiredBatchAssociateServiceActionWithProvisioningArtifactInputRequestTypeDef,
    _OptionalBatchAssociateServiceActionWithProvisioningArtifactInputRequestTypeDef,
):
    pass

BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef = TypedDict(
    "BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef",
    {
        "FailedServiceActionAssociations": List["FailedServiceActionAssociationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchDisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef = TypedDict(
    "_RequiredBatchDisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef",
    {
        "ServiceActionAssociations": List["ServiceActionAssociationTypeDef"],
    },
)
_OptionalBatchDisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef = TypedDict(
    "_OptionalBatchDisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)

class BatchDisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef(
    _RequiredBatchDisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef,
    _OptionalBatchDisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef,
):
    pass

BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef = TypedDict(
    "BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef",
    {
        "FailedServiceActionAssociations": List["FailedServiceActionAssociationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BudgetDetailTypeDef = TypedDict(
    "BudgetDetailTypeDef",
    {
        "BudgetName": str,
    },
    total=False,
)

CloudWatchDashboardTypeDef = TypedDict(
    "CloudWatchDashboardTypeDef",
    {
        "Name": str,
    },
    total=False,
)

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
    "ConstraintSummaryTypeDef",
    {
        "Type": str,
        "Description": str,
    },
    total=False,
)

_RequiredCopyProductInputRequestTypeDef = TypedDict(
    "_RequiredCopyProductInputRequestTypeDef",
    {
        "SourceProductArn": str,
        "IdempotencyToken": str,
    },
)
_OptionalCopyProductInputRequestTypeDef = TypedDict(
    "_OptionalCopyProductInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "TargetProductId": str,
        "TargetProductName": str,
        "SourceProvisioningArtifactIdentifiers": List[Dict[Literal["Id"], str]],
        "CopyOptions": List[Literal["CopyTags"]],
    },
    total=False,
)

class CopyProductInputRequestTypeDef(
    _RequiredCopyProductInputRequestTypeDef, _OptionalCopyProductInputRequestTypeDef
):
    pass

CopyProductOutputTypeDef = TypedDict(
    "CopyProductOutputTypeDef",
    {
        "CopyProductToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConstraintInputRequestTypeDef = TypedDict(
    "_RequiredCreateConstraintInputRequestTypeDef",
    {
        "PortfolioId": str,
        "ProductId": str,
        "Parameters": str,
        "Type": str,
        "IdempotencyToken": str,
    },
)
_OptionalCreateConstraintInputRequestTypeDef = TypedDict(
    "_OptionalCreateConstraintInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "Description": str,
    },
    total=False,
)

class CreateConstraintInputRequestTypeDef(
    _RequiredCreateConstraintInputRequestTypeDef, _OptionalCreateConstraintInputRequestTypeDef
):
    pass

CreateConstraintOutputTypeDef = TypedDict(
    "CreateConstraintOutputTypeDef",
    {
        "ConstraintDetail": "ConstraintDetailTypeDef",
        "ConstraintParameters": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePortfolioInputRequestTypeDef = TypedDict(
    "_RequiredCreatePortfolioInputRequestTypeDef",
    {
        "DisplayName": str,
        "ProviderName": str,
        "IdempotencyToken": str,
    },
)
_OptionalCreatePortfolioInputRequestTypeDef = TypedDict(
    "_OptionalCreatePortfolioInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreatePortfolioInputRequestTypeDef(
    _RequiredCreatePortfolioInputRequestTypeDef, _OptionalCreatePortfolioInputRequestTypeDef
):
    pass

CreatePortfolioOutputTypeDef = TypedDict(
    "CreatePortfolioOutputTypeDef",
    {
        "PortfolioDetail": "PortfolioDetailTypeDef",
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePortfolioShareInputRequestTypeDef = TypedDict(
    "_RequiredCreatePortfolioShareInputRequestTypeDef",
    {
        "PortfolioId": str,
    },
)
_OptionalCreatePortfolioShareInputRequestTypeDef = TypedDict(
    "_OptionalCreatePortfolioShareInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "AccountId": str,
        "OrganizationNode": "OrganizationNodeTypeDef",
        "ShareTagOptions": bool,
    },
    total=False,
)

class CreatePortfolioShareInputRequestTypeDef(
    _RequiredCreatePortfolioShareInputRequestTypeDef,
    _OptionalCreatePortfolioShareInputRequestTypeDef,
):
    pass

CreatePortfolioShareOutputTypeDef = TypedDict(
    "CreatePortfolioShareOutputTypeDef",
    {
        "PortfolioShareToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProductInputRequestTypeDef = TypedDict(
    "_RequiredCreateProductInputRequestTypeDef",
    {
        "Name": str,
        "Owner": str,
        "ProductType": ProductTypeType,
        "ProvisioningArtifactParameters": "ProvisioningArtifactPropertiesTypeDef",
        "IdempotencyToken": str,
    },
)
_OptionalCreateProductInputRequestTypeDef = TypedDict(
    "_OptionalCreateProductInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "Description": str,
        "Distributor": str,
        "SupportDescription": str,
        "SupportEmail": str,
        "SupportUrl": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateProductInputRequestTypeDef(
    _RequiredCreateProductInputRequestTypeDef, _OptionalCreateProductInputRequestTypeDef
):
    pass

CreateProductOutputTypeDef = TypedDict(
    "CreateProductOutputTypeDef",
    {
        "ProductViewDetail": "ProductViewDetailTypeDef",
        "ProvisioningArtifactDetail": "ProvisioningArtifactDetailTypeDef",
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProvisionedProductPlanInputRequestTypeDef = TypedDict(
    "_RequiredCreateProvisionedProductPlanInputRequestTypeDef",
    {
        "PlanName": str,
        "PlanType": Literal["CLOUDFORMATION"],
        "ProductId": str,
        "ProvisionedProductName": str,
        "ProvisioningArtifactId": str,
        "IdempotencyToken": str,
    },
)
_OptionalCreateProvisionedProductPlanInputRequestTypeDef = TypedDict(
    "_OptionalCreateProvisionedProductPlanInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "NotificationArns": List[str],
        "PathId": str,
        "ProvisioningParameters": List["UpdateProvisioningParameterTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateProvisionedProductPlanInputRequestTypeDef(
    _RequiredCreateProvisionedProductPlanInputRequestTypeDef,
    _OptionalCreateProvisionedProductPlanInputRequestTypeDef,
):
    pass

CreateProvisionedProductPlanOutputTypeDef = TypedDict(
    "CreateProvisionedProductPlanOutputTypeDef",
    {
        "PlanName": str,
        "PlanId": str,
        "ProvisionProductId": str,
        "ProvisionedProductName": str,
        "ProvisioningArtifactId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProvisioningArtifactInputRequestTypeDef = TypedDict(
    "_RequiredCreateProvisioningArtifactInputRequestTypeDef",
    {
        "ProductId": str,
        "Parameters": "ProvisioningArtifactPropertiesTypeDef",
        "IdempotencyToken": str,
    },
)
_OptionalCreateProvisioningArtifactInputRequestTypeDef = TypedDict(
    "_OptionalCreateProvisioningArtifactInputRequestTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)

class CreateProvisioningArtifactInputRequestTypeDef(
    _RequiredCreateProvisioningArtifactInputRequestTypeDef,
    _OptionalCreateProvisioningArtifactInputRequestTypeDef,
):
    pass

CreateProvisioningArtifactOutputTypeDef = TypedDict(
    "CreateProvisioningArtifactOutputTypeDef",
    {
        "ProvisioningArtifactDetail": "ProvisioningArtifactDetailTypeDef",
        "Info": Dict[str, str],
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateServiceActionInputRequestTypeDef = TypedDict(
    "_RequiredCreateServiceActionInputRequestTypeDef",
    {
        "Name": str,
        "DefinitionType": Literal["SSM_AUTOMATION"],
        "Definition": Dict[ServiceActionDefinitionKeyType, str],
        "IdempotencyToken": str,
    },
)
_OptionalCreateServiceActionInputRequestTypeDef = TypedDict(
    "_OptionalCreateServiceActionInputRequestTypeDef",
    {
        "Description": str,
        "AcceptLanguage": str,
    },
    total=False,
)

class CreateServiceActionInputRequestTypeDef(
    _RequiredCreateServiceActionInputRequestTypeDef, _OptionalCreateServiceActionInputRequestTypeDef
):
    pass

CreateServiceActionOutputTypeDef = TypedDict(
    "CreateServiceActionOutputTypeDef",
    {
        "ServiceActionDetail": "ServiceActionDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTagOptionInputRequestTypeDef = TypedDict(
    "CreateTagOptionInputRequestTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

CreateTagOptionOutputTypeDef = TypedDict(
    "CreateTagOptionOutputTypeDef",
    {
        "TagOptionDetail": "TagOptionDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteConstraintInputRequestTypeDef = TypedDict(
    "_RequiredDeleteConstraintInputRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteConstraintInputRequestTypeDef = TypedDict(
    "_OptionalDeleteConstraintInputRequestTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)

class DeleteConstraintInputRequestTypeDef(
    _RequiredDeleteConstraintInputRequestTypeDef, _OptionalDeleteConstraintInputRequestTypeDef
):
    pass

_RequiredDeletePortfolioInputRequestTypeDef = TypedDict(
    "_RequiredDeletePortfolioInputRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeletePortfolioInputRequestTypeDef = TypedDict(
    "_OptionalDeletePortfolioInputRequestTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)

class DeletePortfolioInputRequestTypeDef(
    _RequiredDeletePortfolioInputRequestTypeDef, _OptionalDeletePortfolioInputRequestTypeDef
):
    pass

_RequiredDeletePortfolioShareInputRequestTypeDef = TypedDict(
    "_RequiredDeletePortfolioShareInputRequestTypeDef",
    {
        "PortfolioId": str,
    },
)
_OptionalDeletePortfolioShareInputRequestTypeDef = TypedDict(
    "_OptionalDeletePortfolioShareInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "AccountId": str,
        "OrganizationNode": "OrganizationNodeTypeDef",
    },
    total=False,
)

class DeletePortfolioShareInputRequestTypeDef(
    _RequiredDeletePortfolioShareInputRequestTypeDef,
    _OptionalDeletePortfolioShareInputRequestTypeDef,
):
    pass

DeletePortfolioShareOutputTypeDef = TypedDict(
    "DeletePortfolioShareOutputTypeDef",
    {
        "PortfolioShareToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteProductInputRequestTypeDef = TypedDict(
    "_RequiredDeleteProductInputRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteProductInputRequestTypeDef = TypedDict(
    "_OptionalDeleteProductInputRequestTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)

class DeleteProductInputRequestTypeDef(
    _RequiredDeleteProductInputRequestTypeDef, _OptionalDeleteProductInputRequestTypeDef
):
    pass

_RequiredDeleteProvisionedProductPlanInputRequestTypeDef = TypedDict(
    "_RequiredDeleteProvisionedProductPlanInputRequestTypeDef",
    {
        "PlanId": str,
    },
)
_OptionalDeleteProvisionedProductPlanInputRequestTypeDef = TypedDict(
    "_OptionalDeleteProvisionedProductPlanInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "IgnoreErrors": bool,
    },
    total=False,
)

class DeleteProvisionedProductPlanInputRequestTypeDef(
    _RequiredDeleteProvisionedProductPlanInputRequestTypeDef,
    _OptionalDeleteProvisionedProductPlanInputRequestTypeDef,
):
    pass

_RequiredDeleteProvisioningArtifactInputRequestTypeDef = TypedDict(
    "_RequiredDeleteProvisioningArtifactInputRequestTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
    },
)
_OptionalDeleteProvisioningArtifactInputRequestTypeDef = TypedDict(
    "_OptionalDeleteProvisioningArtifactInputRequestTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)

class DeleteProvisioningArtifactInputRequestTypeDef(
    _RequiredDeleteProvisioningArtifactInputRequestTypeDef,
    _OptionalDeleteProvisioningArtifactInputRequestTypeDef,
):
    pass

_RequiredDeleteServiceActionInputRequestTypeDef = TypedDict(
    "_RequiredDeleteServiceActionInputRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteServiceActionInputRequestTypeDef = TypedDict(
    "_OptionalDeleteServiceActionInputRequestTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)

class DeleteServiceActionInputRequestTypeDef(
    _RequiredDeleteServiceActionInputRequestTypeDef, _OptionalDeleteServiceActionInputRequestTypeDef
):
    pass

DeleteTagOptionInputRequestTypeDef = TypedDict(
    "DeleteTagOptionInputRequestTypeDef",
    {
        "Id": str,
    },
)

_RequiredDescribeConstraintInputRequestTypeDef = TypedDict(
    "_RequiredDescribeConstraintInputRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDescribeConstraintInputRequestTypeDef = TypedDict(
    "_OptionalDescribeConstraintInputRequestTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)

class DescribeConstraintInputRequestTypeDef(
    _RequiredDescribeConstraintInputRequestTypeDef, _OptionalDescribeConstraintInputRequestTypeDef
):
    pass

DescribeConstraintOutputTypeDef = TypedDict(
    "DescribeConstraintOutputTypeDef",
    {
        "ConstraintDetail": "ConstraintDetailTypeDef",
        "ConstraintParameters": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeCopyProductStatusInputRequestTypeDef = TypedDict(
    "_RequiredDescribeCopyProductStatusInputRequestTypeDef",
    {
        "CopyProductToken": str,
    },
)
_OptionalDescribeCopyProductStatusInputRequestTypeDef = TypedDict(
    "_OptionalDescribeCopyProductStatusInputRequestTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)

class DescribeCopyProductStatusInputRequestTypeDef(
    _RequiredDescribeCopyProductStatusInputRequestTypeDef,
    _OptionalDescribeCopyProductStatusInputRequestTypeDef,
):
    pass

DescribeCopyProductStatusOutputTypeDef = TypedDict(
    "DescribeCopyProductStatusOutputTypeDef",
    {
        "CopyProductStatus": CopyProductStatusType,
        "TargetProductId": str,
        "StatusDetail": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribePortfolioInputRequestTypeDef = TypedDict(
    "_RequiredDescribePortfolioInputRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDescribePortfolioInputRequestTypeDef = TypedDict(
    "_OptionalDescribePortfolioInputRequestTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)

class DescribePortfolioInputRequestTypeDef(
    _RequiredDescribePortfolioInputRequestTypeDef, _OptionalDescribePortfolioInputRequestTypeDef
):
    pass

DescribePortfolioOutputTypeDef = TypedDict(
    "DescribePortfolioOutputTypeDef",
    {
        "PortfolioDetail": "PortfolioDetailTypeDef",
        "Tags": List["TagTypeDef"],
        "TagOptions": List["TagOptionDetailTypeDef"],
        "Budgets": List["BudgetDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePortfolioShareStatusInputRequestTypeDef = TypedDict(
    "DescribePortfolioShareStatusInputRequestTypeDef",
    {
        "PortfolioShareToken": str,
    },
)

DescribePortfolioShareStatusOutputTypeDef = TypedDict(
    "DescribePortfolioShareStatusOutputTypeDef",
    {
        "PortfolioShareToken": str,
        "PortfolioId": str,
        "OrganizationNodeValue": str,
        "Status": ShareStatusType,
        "ShareDetails": "ShareDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribePortfolioSharesInputRequestTypeDef = TypedDict(
    "_RequiredDescribePortfolioSharesInputRequestTypeDef",
    {
        "PortfolioId": str,
        "Type": DescribePortfolioShareTypeType,
    },
)
_OptionalDescribePortfolioSharesInputRequestTypeDef = TypedDict(
    "_OptionalDescribePortfolioSharesInputRequestTypeDef",
    {
        "PageToken": str,
        "PageSize": int,
    },
    total=False,
)

class DescribePortfolioSharesInputRequestTypeDef(
    _RequiredDescribePortfolioSharesInputRequestTypeDef,
    _OptionalDescribePortfolioSharesInputRequestTypeDef,
):
    pass

DescribePortfolioSharesOutputTypeDef = TypedDict(
    "DescribePortfolioSharesOutputTypeDef",
    {
        "NextPageToken": str,
        "PortfolioShareDetails": List["PortfolioShareDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProductAsAdminInputRequestTypeDef = TypedDict(
    "DescribeProductAsAdminInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "Id": str,
        "Name": str,
        "SourcePortfolioId": str,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProductInputRequestTypeDef = TypedDict(
    "DescribeProductInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "Id": str,
        "Name": str,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeProductViewInputRequestTypeDef = TypedDict(
    "_RequiredDescribeProductViewInputRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDescribeProductViewInputRequestTypeDef = TypedDict(
    "_OptionalDescribeProductViewInputRequestTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)

class DescribeProductViewInputRequestTypeDef(
    _RequiredDescribeProductViewInputRequestTypeDef, _OptionalDescribeProductViewInputRequestTypeDef
):
    pass

DescribeProductViewOutputTypeDef = TypedDict(
    "DescribeProductViewOutputTypeDef",
    {
        "ProductViewSummary": "ProductViewSummaryTypeDef",
        "ProvisioningArtifacts": List["ProvisioningArtifactTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProvisionedProductInputRequestTypeDef = TypedDict(
    "DescribeProvisionedProductInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "Id": str,
        "Name": str,
    },
    total=False,
)

DescribeProvisionedProductOutputTypeDef = TypedDict(
    "DescribeProvisionedProductOutputTypeDef",
    {
        "ProvisionedProductDetail": "ProvisionedProductDetailTypeDef",
        "CloudWatchDashboards": List["CloudWatchDashboardTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeProvisionedProductPlanInputRequestTypeDef = TypedDict(
    "_RequiredDescribeProvisionedProductPlanInputRequestTypeDef",
    {
        "PlanId": str,
    },
)
_OptionalDescribeProvisionedProductPlanInputRequestTypeDef = TypedDict(
    "_OptionalDescribeProvisionedProductPlanInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "PageSize": int,
        "PageToken": str,
    },
    total=False,
)

class DescribeProvisionedProductPlanInputRequestTypeDef(
    _RequiredDescribeProvisionedProductPlanInputRequestTypeDef,
    _OptionalDescribeProvisionedProductPlanInputRequestTypeDef,
):
    pass

DescribeProvisionedProductPlanOutputTypeDef = TypedDict(
    "DescribeProvisionedProductPlanOutputTypeDef",
    {
        "ProvisionedProductPlanDetails": "ProvisionedProductPlanDetailsTypeDef",
        "ResourceChanges": List["ResourceChangeTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProvisioningArtifactInputRequestTypeDef = TypedDict(
    "DescribeProvisioningArtifactInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "ProvisioningArtifactId": str,
        "ProductId": str,
        "ProvisioningArtifactName": str,
        "ProductName": str,
        "Verbose": bool,
    },
    total=False,
)

DescribeProvisioningArtifactOutputTypeDef = TypedDict(
    "DescribeProvisioningArtifactOutputTypeDef",
    {
        "ProvisioningArtifactDetail": "ProvisioningArtifactDetailTypeDef",
        "Info": Dict[str, str],
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProvisioningParametersInputRequestTypeDef = TypedDict(
    "DescribeProvisioningParametersInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "ProductId": str,
        "ProductName": str,
        "ProvisioningArtifactId": str,
        "ProvisioningArtifactName": str,
        "PathId": str,
        "PathName": str,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRecordInputRequestTypeDef = TypedDict(
    "_RequiredDescribeRecordInputRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDescribeRecordInputRequestTypeDef = TypedDict(
    "_OptionalDescribeRecordInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "PageToken": str,
        "PageSize": int,
    },
    total=False,
)

class DescribeRecordInputRequestTypeDef(
    _RequiredDescribeRecordInputRequestTypeDef, _OptionalDescribeRecordInputRequestTypeDef
):
    pass

DescribeRecordOutputTypeDef = TypedDict(
    "DescribeRecordOutputTypeDef",
    {
        "RecordDetail": "RecordDetailTypeDef",
        "RecordOutputs": List["RecordOutputTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeServiceActionExecutionParametersInputRequestTypeDef = TypedDict(
    "_RequiredDescribeServiceActionExecutionParametersInputRequestTypeDef",
    {
        "ProvisionedProductId": str,
        "ServiceActionId": str,
    },
)
_OptionalDescribeServiceActionExecutionParametersInputRequestTypeDef = TypedDict(
    "_OptionalDescribeServiceActionExecutionParametersInputRequestTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)

class DescribeServiceActionExecutionParametersInputRequestTypeDef(
    _RequiredDescribeServiceActionExecutionParametersInputRequestTypeDef,
    _OptionalDescribeServiceActionExecutionParametersInputRequestTypeDef,
):
    pass

DescribeServiceActionExecutionParametersOutputTypeDef = TypedDict(
    "DescribeServiceActionExecutionParametersOutputTypeDef",
    {
        "ServiceActionParameters": List["ExecutionParameterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeServiceActionInputRequestTypeDef = TypedDict(
    "_RequiredDescribeServiceActionInputRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDescribeServiceActionInputRequestTypeDef = TypedDict(
    "_OptionalDescribeServiceActionInputRequestTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)

class DescribeServiceActionInputRequestTypeDef(
    _RequiredDescribeServiceActionInputRequestTypeDef,
    _OptionalDescribeServiceActionInputRequestTypeDef,
):
    pass

DescribeServiceActionOutputTypeDef = TypedDict(
    "DescribeServiceActionOutputTypeDef",
    {
        "ServiceActionDetail": "ServiceActionDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTagOptionInputRequestTypeDef = TypedDict(
    "DescribeTagOptionInputRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeTagOptionOutputTypeDef = TypedDict(
    "DescribeTagOptionOutputTypeDef",
    {
        "TagOptionDetail": "TagOptionDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateBudgetFromResourceInputRequestTypeDef = TypedDict(
    "DisassociateBudgetFromResourceInputRequestTypeDef",
    {
        "BudgetName": str,
        "ResourceId": str,
    },
)

_RequiredDisassociatePrincipalFromPortfolioInputRequestTypeDef = TypedDict(
    "_RequiredDisassociatePrincipalFromPortfolioInputRequestTypeDef",
    {
        "PortfolioId": str,
        "PrincipalARN": str,
    },
)
_OptionalDisassociatePrincipalFromPortfolioInputRequestTypeDef = TypedDict(
    "_OptionalDisassociatePrincipalFromPortfolioInputRequestTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)

class DisassociatePrincipalFromPortfolioInputRequestTypeDef(
    _RequiredDisassociatePrincipalFromPortfolioInputRequestTypeDef,
    _OptionalDisassociatePrincipalFromPortfolioInputRequestTypeDef,
):
    pass

_RequiredDisassociateProductFromPortfolioInputRequestTypeDef = TypedDict(
    "_RequiredDisassociateProductFromPortfolioInputRequestTypeDef",
    {
        "ProductId": str,
        "PortfolioId": str,
    },
)
_OptionalDisassociateProductFromPortfolioInputRequestTypeDef = TypedDict(
    "_OptionalDisassociateProductFromPortfolioInputRequestTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)

class DisassociateProductFromPortfolioInputRequestTypeDef(
    _RequiredDisassociateProductFromPortfolioInputRequestTypeDef,
    _OptionalDisassociateProductFromPortfolioInputRequestTypeDef,
):
    pass

_RequiredDisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef = TypedDict(
    "_RequiredDisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "ServiceActionId": str,
    },
)
_OptionalDisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef = TypedDict(
    "_OptionalDisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)

class DisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef(
    _RequiredDisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef,
    _OptionalDisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef,
):
    pass

DisassociateTagOptionFromResourceInputRequestTypeDef = TypedDict(
    "DisassociateTagOptionFromResourceInputRequestTypeDef",
    {
        "ResourceId": str,
        "TagOptionId": str,
    },
)

_RequiredExecuteProvisionedProductPlanInputRequestTypeDef = TypedDict(
    "_RequiredExecuteProvisionedProductPlanInputRequestTypeDef",
    {
        "PlanId": str,
        "IdempotencyToken": str,
    },
)
_OptionalExecuteProvisionedProductPlanInputRequestTypeDef = TypedDict(
    "_OptionalExecuteProvisionedProductPlanInputRequestTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)

class ExecuteProvisionedProductPlanInputRequestTypeDef(
    _RequiredExecuteProvisionedProductPlanInputRequestTypeDef,
    _OptionalExecuteProvisionedProductPlanInputRequestTypeDef,
):
    pass

ExecuteProvisionedProductPlanOutputTypeDef = TypedDict(
    "ExecuteProvisionedProductPlanOutputTypeDef",
    {
        "RecordDetail": "RecordDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExecuteProvisionedProductServiceActionInputRequestTypeDef = TypedDict(
    "_RequiredExecuteProvisionedProductServiceActionInputRequestTypeDef",
    {
        "ProvisionedProductId": str,
        "ServiceActionId": str,
        "ExecuteToken": str,
    },
)
_OptionalExecuteProvisionedProductServiceActionInputRequestTypeDef = TypedDict(
    "_OptionalExecuteProvisionedProductServiceActionInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "Parameters": Dict[str, List[str]],
    },
    total=False,
)

class ExecuteProvisionedProductServiceActionInputRequestTypeDef(
    _RequiredExecuteProvisionedProductServiceActionInputRequestTypeDef,
    _OptionalExecuteProvisionedProductServiceActionInputRequestTypeDef,
):
    pass

ExecuteProvisionedProductServiceActionOutputTypeDef = TypedDict(
    "ExecuteProvisionedProductServiceActionOutputTypeDef",
    {
        "RecordDetail": "RecordDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExecutionParameterTypeDef = TypedDict(
    "ExecutionParameterTypeDef",
    {
        "Name": str,
        "Type": str,
        "DefaultValues": List[str],
    },
    total=False,
)

FailedServiceActionAssociationTypeDef = TypedDict(
    "FailedServiceActionAssociationTypeDef",
    {
        "ServiceActionId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "ErrorCode": ServiceActionAssociationErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

GetAWSOrganizationsAccessStatusOutputTypeDef = TypedDict(
    "GetAWSOrganizationsAccessStatusOutputTypeDef",
    {
        "AccessStatus": AccessStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProvisionedProductOutputsInputRequestTypeDef = TypedDict(
    "GetProvisionedProductOutputsInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "ProvisionedProductId": str,
        "ProvisionedProductName": str,
        "OutputKeys": List[str],
        "PageSize": int,
        "PageToken": str,
    },
    total=False,
)

GetProvisionedProductOutputsOutputTypeDef = TypedDict(
    "GetProvisionedProductOutputsOutputTypeDef",
    {
        "Outputs": List["RecordOutputTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImportAsProvisionedProductInputRequestTypeDef = TypedDict(
    "_RequiredImportAsProvisionedProductInputRequestTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "ProvisionedProductName": str,
        "PhysicalId": str,
        "IdempotencyToken": str,
    },
)
_OptionalImportAsProvisionedProductInputRequestTypeDef = TypedDict(
    "_OptionalImportAsProvisionedProductInputRequestTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)

class ImportAsProvisionedProductInputRequestTypeDef(
    _RequiredImportAsProvisionedProductInputRequestTypeDef,
    _OptionalImportAsProvisionedProductInputRequestTypeDef,
):
    pass

ImportAsProvisionedProductOutputTypeDef = TypedDict(
    "ImportAsProvisionedProductOutputTypeDef",
    {
        "RecordDetail": "RecordDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

LaunchPathTypeDef = TypedDict(
    "LaunchPathTypeDef",
    {
        "Id": str,
        "Name": str,
    },
    total=False,
)

ListAcceptedPortfolioSharesInputRequestTypeDef = TypedDict(
    "ListAcceptedPortfolioSharesInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "PageToken": str,
        "PageSize": int,
        "PortfolioShareType": PortfolioShareTypeType,
    },
    total=False,
)

ListAcceptedPortfolioSharesOutputTypeDef = TypedDict(
    "ListAcceptedPortfolioSharesOutputTypeDef",
    {
        "PortfolioDetails": List["PortfolioDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBudgetsForResourceInputRequestTypeDef = TypedDict(
    "_RequiredListBudgetsForResourceInputRequestTypeDef",
    {
        "ResourceId": str,
    },
)
_OptionalListBudgetsForResourceInputRequestTypeDef = TypedDict(
    "_OptionalListBudgetsForResourceInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "PageSize": int,
        "PageToken": str,
    },
    total=False,
)

class ListBudgetsForResourceInputRequestTypeDef(
    _RequiredListBudgetsForResourceInputRequestTypeDef,
    _OptionalListBudgetsForResourceInputRequestTypeDef,
):
    pass

ListBudgetsForResourceOutputTypeDef = TypedDict(
    "ListBudgetsForResourceOutputTypeDef",
    {
        "Budgets": List["BudgetDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListConstraintsForPortfolioInputRequestTypeDef = TypedDict(
    "_RequiredListConstraintsForPortfolioInputRequestTypeDef",
    {
        "PortfolioId": str,
    },
)
_OptionalListConstraintsForPortfolioInputRequestTypeDef = TypedDict(
    "_OptionalListConstraintsForPortfolioInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "ProductId": str,
        "PageSize": int,
        "PageToken": str,
    },
    total=False,
)

class ListConstraintsForPortfolioInputRequestTypeDef(
    _RequiredListConstraintsForPortfolioInputRequestTypeDef,
    _OptionalListConstraintsForPortfolioInputRequestTypeDef,
):
    pass

ListConstraintsForPortfolioOutputTypeDef = TypedDict(
    "ListConstraintsForPortfolioOutputTypeDef",
    {
        "ConstraintDetails": List["ConstraintDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLaunchPathsInputRequestTypeDef = TypedDict(
    "_RequiredListLaunchPathsInputRequestTypeDef",
    {
        "ProductId": str,
    },
)
_OptionalListLaunchPathsInputRequestTypeDef = TypedDict(
    "_OptionalListLaunchPathsInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "PageSize": int,
        "PageToken": str,
    },
    total=False,
)

class ListLaunchPathsInputRequestTypeDef(
    _RequiredListLaunchPathsInputRequestTypeDef, _OptionalListLaunchPathsInputRequestTypeDef
):
    pass

ListLaunchPathsOutputTypeDef = TypedDict(
    "ListLaunchPathsOutputTypeDef",
    {
        "LaunchPathSummaries": List["LaunchPathSummaryTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListOrganizationPortfolioAccessInputRequestTypeDef = TypedDict(
    "_RequiredListOrganizationPortfolioAccessInputRequestTypeDef",
    {
        "PortfolioId": str,
        "OrganizationNodeType": OrganizationNodeTypeType,
    },
)
_OptionalListOrganizationPortfolioAccessInputRequestTypeDef = TypedDict(
    "_OptionalListOrganizationPortfolioAccessInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "PageToken": str,
        "PageSize": int,
    },
    total=False,
)

class ListOrganizationPortfolioAccessInputRequestTypeDef(
    _RequiredListOrganizationPortfolioAccessInputRequestTypeDef,
    _OptionalListOrganizationPortfolioAccessInputRequestTypeDef,
):
    pass

ListOrganizationPortfolioAccessOutputTypeDef = TypedDict(
    "ListOrganizationPortfolioAccessOutputTypeDef",
    {
        "OrganizationNodes": List["OrganizationNodeTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPortfolioAccessInputRequestTypeDef = TypedDict(
    "_RequiredListPortfolioAccessInputRequestTypeDef",
    {
        "PortfolioId": str,
    },
)
_OptionalListPortfolioAccessInputRequestTypeDef = TypedDict(
    "_OptionalListPortfolioAccessInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "OrganizationParentId": str,
        "PageToken": str,
        "PageSize": int,
    },
    total=False,
)

class ListPortfolioAccessInputRequestTypeDef(
    _RequiredListPortfolioAccessInputRequestTypeDef, _OptionalListPortfolioAccessInputRequestTypeDef
):
    pass

ListPortfolioAccessOutputTypeDef = TypedDict(
    "ListPortfolioAccessOutputTypeDef",
    {
        "AccountIds": List[str],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPortfoliosForProductInputRequestTypeDef = TypedDict(
    "_RequiredListPortfoliosForProductInputRequestTypeDef",
    {
        "ProductId": str,
    },
)
_OptionalListPortfoliosForProductInputRequestTypeDef = TypedDict(
    "_OptionalListPortfoliosForProductInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "PageToken": str,
        "PageSize": int,
    },
    total=False,
)

class ListPortfoliosForProductInputRequestTypeDef(
    _RequiredListPortfoliosForProductInputRequestTypeDef,
    _OptionalListPortfoliosForProductInputRequestTypeDef,
):
    pass

ListPortfoliosForProductOutputTypeDef = TypedDict(
    "ListPortfoliosForProductOutputTypeDef",
    {
        "PortfolioDetails": List["PortfolioDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPortfoliosInputRequestTypeDef = TypedDict(
    "ListPortfoliosInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "PageToken": str,
        "PageSize": int,
    },
    total=False,
)

ListPortfoliosOutputTypeDef = TypedDict(
    "ListPortfoliosOutputTypeDef",
    {
        "PortfolioDetails": List["PortfolioDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPrincipalsForPortfolioInputRequestTypeDef = TypedDict(
    "_RequiredListPrincipalsForPortfolioInputRequestTypeDef",
    {
        "PortfolioId": str,
    },
)
_OptionalListPrincipalsForPortfolioInputRequestTypeDef = TypedDict(
    "_OptionalListPrincipalsForPortfolioInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "PageSize": int,
        "PageToken": str,
    },
    total=False,
)

class ListPrincipalsForPortfolioInputRequestTypeDef(
    _RequiredListPrincipalsForPortfolioInputRequestTypeDef,
    _OptionalListPrincipalsForPortfolioInputRequestTypeDef,
):
    pass

ListPrincipalsForPortfolioOutputTypeDef = TypedDict(
    "ListPrincipalsForPortfolioOutputTypeDef",
    {
        "Principals": List["PrincipalTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProvisionedProductPlansInputRequestTypeDef = TypedDict(
    "ListProvisionedProductPlansInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "ProvisionProductId": str,
        "PageSize": int,
        "PageToken": str,
        "AccessLevelFilter": "AccessLevelFilterTypeDef",
    },
    total=False,
)

ListProvisionedProductPlansOutputTypeDef = TypedDict(
    "ListProvisionedProductPlansOutputTypeDef",
    {
        "ProvisionedProductPlans": List["ProvisionedProductPlanSummaryTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProvisioningArtifactsForServiceActionInputRequestTypeDef = TypedDict(
    "_RequiredListProvisioningArtifactsForServiceActionInputRequestTypeDef",
    {
        "ServiceActionId": str,
    },
)
_OptionalListProvisioningArtifactsForServiceActionInputRequestTypeDef = TypedDict(
    "_OptionalListProvisioningArtifactsForServiceActionInputRequestTypeDef",
    {
        "PageSize": int,
        "PageToken": str,
        "AcceptLanguage": str,
    },
    total=False,
)

class ListProvisioningArtifactsForServiceActionInputRequestTypeDef(
    _RequiredListProvisioningArtifactsForServiceActionInputRequestTypeDef,
    _OptionalListProvisioningArtifactsForServiceActionInputRequestTypeDef,
):
    pass

ListProvisioningArtifactsForServiceActionOutputTypeDef = TypedDict(
    "ListProvisioningArtifactsForServiceActionOutputTypeDef",
    {
        "ProvisioningArtifactViews": List["ProvisioningArtifactViewTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProvisioningArtifactsInputRequestTypeDef = TypedDict(
    "_RequiredListProvisioningArtifactsInputRequestTypeDef",
    {
        "ProductId": str,
    },
)
_OptionalListProvisioningArtifactsInputRequestTypeDef = TypedDict(
    "_OptionalListProvisioningArtifactsInputRequestTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)

class ListProvisioningArtifactsInputRequestTypeDef(
    _RequiredListProvisioningArtifactsInputRequestTypeDef,
    _OptionalListProvisioningArtifactsInputRequestTypeDef,
):
    pass

ListProvisioningArtifactsOutputTypeDef = TypedDict(
    "ListProvisioningArtifactsOutputTypeDef",
    {
        "ProvisioningArtifactDetails": List["ProvisioningArtifactDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecordHistoryInputRequestTypeDef = TypedDict(
    "ListRecordHistoryInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "AccessLevelFilter": "AccessLevelFilterTypeDef",
        "SearchFilter": "ListRecordHistorySearchFilterTypeDef",
        "PageSize": int,
        "PageToken": str,
    },
    total=False,
)

ListRecordHistoryOutputTypeDef = TypedDict(
    "ListRecordHistoryOutputTypeDef",
    {
        "RecordDetails": List["RecordDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecordHistorySearchFilterTypeDef = TypedDict(
    "ListRecordHistorySearchFilterTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

_RequiredListResourcesForTagOptionInputRequestTypeDef = TypedDict(
    "_RequiredListResourcesForTagOptionInputRequestTypeDef",
    {
        "TagOptionId": str,
    },
)
_OptionalListResourcesForTagOptionInputRequestTypeDef = TypedDict(
    "_OptionalListResourcesForTagOptionInputRequestTypeDef",
    {
        "ResourceType": str,
        "PageSize": int,
        "PageToken": str,
    },
    total=False,
)

class ListResourcesForTagOptionInputRequestTypeDef(
    _RequiredListResourcesForTagOptionInputRequestTypeDef,
    _OptionalListResourcesForTagOptionInputRequestTypeDef,
):
    pass

ListResourcesForTagOptionOutputTypeDef = TypedDict(
    "ListResourcesForTagOptionOutputTypeDef",
    {
        "ResourceDetails": List["ResourceDetailTypeDef"],
        "PageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListServiceActionsForProvisioningArtifactInputRequestTypeDef = TypedDict(
    "_RequiredListServiceActionsForProvisioningArtifactInputRequestTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
    },
)
_OptionalListServiceActionsForProvisioningArtifactInputRequestTypeDef = TypedDict(
    "_OptionalListServiceActionsForProvisioningArtifactInputRequestTypeDef",
    {
        "PageSize": int,
        "PageToken": str,
        "AcceptLanguage": str,
    },
    total=False,
)

class ListServiceActionsForProvisioningArtifactInputRequestTypeDef(
    _RequiredListServiceActionsForProvisioningArtifactInputRequestTypeDef,
    _OptionalListServiceActionsForProvisioningArtifactInputRequestTypeDef,
):
    pass

ListServiceActionsForProvisioningArtifactOutputTypeDef = TypedDict(
    "ListServiceActionsForProvisioningArtifactOutputTypeDef",
    {
        "ServiceActionSummaries": List["ServiceActionSummaryTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceActionsInputRequestTypeDef = TypedDict(
    "ListServiceActionsInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "PageSize": int,
        "PageToken": str,
    },
    total=False,
)

ListServiceActionsOutputTypeDef = TypedDict(
    "ListServiceActionsOutputTypeDef",
    {
        "ServiceActionSummaries": List["ServiceActionSummaryTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStackInstancesForProvisionedProductInputRequestTypeDef = TypedDict(
    "_RequiredListStackInstancesForProvisionedProductInputRequestTypeDef",
    {
        "ProvisionedProductId": str,
    },
)
_OptionalListStackInstancesForProvisionedProductInputRequestTypeDef = TypedDict(
    "_OptionalListStackInstancesForProvisionedProductInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "PageToken": str,
        "PageSize": int,
    },
    total=False,
)

class ListStackInstancesForProvisionedProductInputRequestTypeDef(
    _RequiredListStackInstancesForProvisionedProductInputRequestTypeDef,
    _OptionalListStackInstancesForProvisionedProductInputRequestTypeDef,
):
    pass

ListStackInstancesForProvisionedProductOutputTypeDef = TypedDict(
    "ListStackInstancesForProvisionedProductOutputTypeDef",
    {
        "StackInstances": List["StackInstanceTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagOptionsFiltersTypeDef = TypedDict(
    "ListTagOptionsFiltersTypeDef",
    {
        "Key": str,
        "Value": str,
        "Active": bool,
    },
    total=False,
)

ListTagOptionsInputRequestTypeDef = TypedDict(
    "ListTagOptionsInputRequestTypeDef",
    {
        "Filters": "ListTagOptionsFiltersTypeDef",
        "PageSize": int,
        "PageToken": str,
    },
    total=False,
)

ListTagOptionsOutputTypeDef = TypedDict(
    "ListTagOptionsOutputTypeDef",
    {
        "TagOptionDetails": List["TagOptionDetailTypeDef"],
        "PageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OrganizationNodeTypeDef = TypedDict(
    "OrganizationNodeTypeDef",
    {
        "Type": OrganizationNodeTypeType,
        "Value": str,
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
        "AllowedPattern": str,
        "ConstraintDescription": str,
        "MaxLength": str,
        "MinLength": str,
        "MaxValue": str,
        "MinValue": str,
    },
    total=False,
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

PortfolioShareDetailTypeDef = TypedDict(
    "PortfolioShareDetailTypeDef",
    {
        "PrincipalId": str,
        "Type": DescribePortfolioShareTypeType,
        "Accepted": bool,
        "ShareTagOptions": bool,
    },
    total=False,
)

PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "PrincipalARN": str,
        "PrincipalType": Literal["IAM"],
    },
    total=False,
)

ProductViewAggregationValueTypeDef = TypedDict(
    "ProductViewAggregationValueTypeDef",
    {
        "Value": str,
        "ApproximateCount": int,
    },
    total=False,
)

ProductViewDetailTypeDef = TypedDict(
    "ProductViewDetailTypeDef",
    {
        "ProductViewSummary": "ProductViewSummaryTypeDef",
        "Status": StatusType,
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
        "Type": ProductTypeType,
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)

_RequiredProvisionProductInputRequestTypeDef = TypedDict(
    "_RequiredProvisionProductInputRequestTypeDef",
    {
        "ProvisionedProductName": str,
        "ProvisionToken": str,
    },
)
_OptionalProvisionProductInputRequestTypeDef = TypedDict(
    "_OptionalProvisionProductInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "ProductId": str,
        "ProductName": str,
        "ProvisioningArtifactId": str,
        "ProvisioningArtifactName": str,
        "PathId": str,
        "PathName": str,
        "ProvisioningParameters": List["ProvisioningParameterTypeDef"],
        "ProvisioningPreferences": "ProvisioningPreferencesTypeDef",
        "Tags": List["TagTypeDef"],
        "NotificationArns": List[str],
    },
    total=False,
)

class ProvisionProductInputRequestTypeDef(
    _RequiredProvisionProductInputRequestTypeDef, _OptionalProvisionProductInputRequestTypeDef
):
    pass

ProvisionProductOutputTypeDef = TypedDict(
    "ProvisionProductOutputTypeDef",
    {
        "RecordDetail": "RecordDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ProvisionedProductAttributeTypeDef = TypedDict(
    "ProvisionedProductAttributeTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Type": str,
        "Id": str,
        "Status": ProvisionedProductStatusType,
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
        "Status": ProvisionedProductStatusType,
        "StatusMessage": str,
        "CreatedTime": datetime,
        "IdempotencyToken": str,
        "LastRecordId": str,
        "LastProvisioningRecordId": str,
        "LastSuccessfulProvisioningRecordId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "LaunchRoleArn": str,
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
        "Status": ProvisionedProductPlanStatusType,
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
        "Type": ProvisioningArtifactTypeType,
        "CreatedTime": datetime,
        "Active": bool,
        "Guidance": ProvisioningArtifactGuidanceType,
    },
    total=False,
)

ProvisioningArtifactOutputTypeDef = TypedDict(
    "ProvisioningArtifactOutputTypeDef",
    {
        "Key": str,
        "Description": str,
    },
    total=False,
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
    {
        "StackSetAccounts": List[str],
        "StackSetRegions": List[str],
    },
    total=False,
)

_RequiredProvisioningArtifactPropertiesTypeDef = TypedDict(
    "_RequiredProvisioningArtifactPropertiesTypeDef",
    {
        "Info": Dict[str, str],
    },
)
_OptionalProvisioningArtifactPropertiesTypeDef = TypedDict(
    "_OptionalProvisioningArtifactPropertiesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Type": ProvisioningArtifactTypeType,
        "DisableTemplateValidation": bool,
    },
    total=False,
)

class ProvisioningArtifactPropertiesTypeDef(
    _RequiredProvisioningArtifactPropertiesTypeDef, _OptionalProvisioningArtifactPropertiesTypeDef
):
    pass

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
        "Guidance": ProvisioningArtifactGuidanceType,
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

ProvisioningParameterTypeDef = TypedDict(
    "ProvisioningParameterTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
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

RecordDetailTypeDef = TypedDict(
    "RecordDetailTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": RecordStatusType,
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
        "LaunchRoleArn": str,
    },
    total=False,
)

RecordErrorTypeDef = TypedDict(
    "RecordErrorTypeDef",
    {
        "Code": str,
        "Description": str,
    },
    total=False,
)

RecordOutputTypeDef = TypedDict(
    "RecordOutputTypeDef",
    {
        "OutputKey": str,
        "OutputValue": str,
        "Description": str,
    },
    total=False,
)

RecordTagTypeDef = TypedDict(
    "RecordTagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

_RequiredRejectPortfolioShareInputRequestTypeDef = TypedDict(
    "_RequiredRejectPortfolioShareInputRequestTypeDef",
    {
        "PortfolioId": str,
    },
)
_OptionalRejectPortfolioShareInputRequestTypeDef = TypedDict(
    "_OptionalRejectPortfolioShareInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "PortfolioShareType": PortfolioShareTypeType,
    },
    total=False,
)

class RejectPortfolioShareInputRequestTypeDef(
    _RequiredRejectPortfolioShareInputRequestTypeDef,
    _OptionalRejectPortfolioShareInputRequestTypeDef,
):
    pass

ResourceChangeDetailTypeDef = TypedDict(
    "ResourceChangeDetailTypeDef",
    {
        "Target": "ResourceTargetDefinitionTypeDef",
        "Evaluation": EvaluationTypeType,
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
    },
    total=False,
)

ResourceDetailTypeDef = TypedDict(
    "ResourceDetailTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Name": str,
        "Description": str,
        "CreatedTime": datetime,
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

ScanProvisionedProductsInputRequestTypeDef = TypedDict(
    "ScanProvisionedProductsInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "AccessLevelFilter": "AccessLevelFilterTypeDef",
        "PageSize": int,
        "PageToken": str,
    },
    total=False,
)

ScanProvisionedProductsOutputTypeDef = TypedDict(
    "ScanProvisionedProductsOutputTypeDef",
    {
        "ProvisionedProducts": List["ProvisionedProductDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchProductsAsAdminInputRequestTypeDef = TypedDict(
    "SearchProductsAsAdminInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "PortfolioId": str,
        "Filters": Dict[ProductViewFilterByType, List[str]],
        "SortBy": ProductViewSortByType,
        "SortOrder": SortOrderType,
        "PageToken": str,
        "PageSize": int,
        "ProductSource": Literal["ACCOUNT"],
    },
    total=False,
)

SearchProductsAsAdminOutputTypeDef = TypedDict(
    "SearchProductsAsAdminOutputTypeDef",
    {
        "ProductViewDetails": List["ProductViewDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchProductsInputRequestTypeDef = TypedDict(
    "SearchProductsInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "Filters": Dict[ProductViewFilterByType, List[str]],
        "PageSize": int,
        "SortBy": ProductViewSortByType,
        "SortOrder": SortOrderType,
        "PageToken": str,
    },
    total=False,
)

SearchProductsOutputTypeDef = TypedDict(
    "SearchProductsOutputTypeDef",
    {
        "ProductViewSummaries": List["ProductViewSummaryTypeDef"],
        "ProductViewAggregations": Dict[str, List["ProductViewAggregationValueTypeDef"]],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchProvisionedProductsInputRequestTypeDef = TypedDict(
    "SearchProvisionedProductsInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "AccessLevelFilter": "AccessLevelFilterTypeDef",
        "Filters": Dict[Literal["SearchQuery"], List[str]],
        "SortBy": str,
        "SortOrder": SortOrderType,
        "PageSize": int,
        "PageToken": str,
    },
    total=False,
)

SearchProvisionedProductsOutputTypeDef = TypedDict(
    "SearchProvisionedProductsOutputTypeDef",
    {
        "ProvisionedProducts": List["ProvisionedProductAttributeTypeDef"],
        "TotalResultsCount": int,
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceActionAssociationTypeDef = TypedDict(
    "ServiceActionAssociationTypeDef",
    {
        "ServiceActionId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
    },
)

ServiceActionDetailTypeDef = TypedDict(
    "ServiceActionDetailTypeDef",
    {
        "ServiceActionSummary": "ServiceActionSummaryTypeDef",
        "Definition": Dict[ServiceActionDefinitionKeyType, str],
    },
    total=False,
)

ServiceActionSummaryTypeDef = TypedDict(
    "ServiceActionSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "DefinitionType": Literal["SSM_AUTOMATION"],
    },
    total=False,
)

ShareDetailsTypeDef = TypedDict(
    "ShareDetailsTypeDef",
    {
        "SuccessfulShares": List[str],
        "ShareErrors": List["ShareErrorTypeDef"],
    },
    total=False,
)

ShareErrorTypeDef = TypedDict(
    "ShareErrorTypeDef",
    {
        "Accounts": List[str],
        "Message": str,
        "Error": str,
    },
    total=False,
)

StackInstanceTypeDef = TypedDict(
    "StackInstanceTypeDef",
    {
        "Account": str,
        "Region": str,
        "StackInstanceStatus": StackInstanceStatusType,
    },
    total=False,
)

TagOptionDetailTypeDef = TypedDict(
    "TagOptionDetailTypeDef",
    {
        "Key": str,
        "Value": str,
        "Active": bool,
        "Id": str,
        "Owner": str,
    },
    total=False,
)

TagOptionSummaryTypeDef = TypedDict(
    "TagOptionSummaryTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

_RequiredTerminateProvisionedProductInputRequestTypeDef = TypedDict(
    "_RequiredTerminateProvisionedProductInputRequestTypeDef",
    {
        "TerminateToken": str,
    },
)
_OptionalTerminateProvisionedProductInputRequestTypeDef = TypedDict(
    "_OptionalTerminateProvisionedProductInputRequestTypeDef",
    {
        "ProvisionedProductName": str,
        "ProvisionedProductId": str,
        "IgnoreErrors": bool,
        "AcceptLanguage": str,
        "RetainPhysicalResources": bool,
    },
    total=False,
)

class TerminateProvisionedProductInputRequestTypeDef(
    _RequiredTerminateProvisionedProductInputRequestTypeDef,
    _OptionalTerminateProvisionedProductInputRequestTypeDef,
):
    pass

TerminateProvisionedProductOutputTypeDef = TypedDict(
    "TerminateProvisionedProductOutputTypeDef",
    {
        "RecordDetail": "RecordDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateConstraintInputRequestTypeDef = TypedDict(
    "_RequiredUpdateConstraintInputRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateConstraintInputRequestTypeDef = TypedDict(
    "_OptionalUpdateConstraintInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "Description": str,
        "Parameters": str,
    },
    total=False,
)

class UpdateConstraintInputRequestTypeDef(
    _RequiredUpdateConstraintInputRequestTypeDef, _OptionalUpdateConstraintInputRequestTypeDef
):
    pass

UpdateConstraintOutputTypeDef = TypedDict(
    "UpdateConstraintOutputTypeDef",
    {
        "ConstraintDetail": "ConstraintDetailTypeDef",
        "ConstraintParameters": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePortfolioInputRequestTypeDef = TypedDict(
    "_RequiredUpdatePortfolioInputRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdatePortfolioInputRequestTypeDef = TypedDict(
    "_OptionalUpdatePortfolioInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "DisplayName": str,
        "Description": str,
        "ProviderName": str,
        "AddTags": List["TagTypeDef"],
        "RemoveTags": List[str],
    },
    total=False,
)

class UpdatePortfolioInputRequestTypeDef(
    _RequiredUpdatePortfolioInputRequestTypeDef, _OptionalUpdatePortfolioInputRequestTypeDef
):
    pass

UpdatePortfolioOutputTypeDef = TypedDict(
    "UpdatePortfolioOutputTypeDef",
    {
        "PortfolioDetail": "PortfolioDetailTypeDef",
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePortfolioShareInputRequestTypeDef = TypedDict(
    "_RequiredUpdatePortfolioShareInputRequestTypeDef",
    {
        "PortfolioId": str,
    },
)
_OptionalUpdatePortfolioShareInputRequestTypeDef = TypedDict(
    "_OptionalUpdatePortfolioShareInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "AccountId": str,
        "OrganizationNode": "OrganizationNodeTypeDef",
        "ShareTagOptions": bool,
    },
    total=False,
)

class UpdatePortfolioShareInputRequestTypeDef(
    _RequiredUpdatePortfolioShareInputRequestTypeDef,
    _OptionalUpdatePortfolioShareInputRequestTypeDef,
):
    pass

UpdatePortfolioShareOutputTypeDef = TypedDict(
    "UpdatePortfolioShareOutputTypeDef",
    {
        "PortfolioShareToken": str,
        "Status": ShareStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProductInputRequestTypeDef = TypedDict(
    "_RequiredUpdateProductInputRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateProductInputRequestTypeDef = TypedDict(
    "_OptionalUpdateProductInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "Name": str,
        "Owner": str,
        "Description": str,
        "Distributor": str,
        "SupportDescription": str,
        "SupportEmail": str,
        "SupportUrl": str,
        "AddTags": List["TagTypeDef"],
        "RemoveTags": List[str],
    },
    total=False,
)

class UpdateProductInputRequestTypeDef(
    _RequiredUpdateProductInputRequestTypeDef, _OptionalUpdateProductInputRequestTypeDef
):
    pass

UpdateProductOutputTypeDef = TypedDict(
    "UpdateProductOutputTypeDef",
    {
        "ProductViewDetail": "ProductViewDetailTypeDef",
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProvisionedProductInputRequestTypeDef = TypedDict(
    "_RequiredUpdateProvisionedProductInputRequestTypeDef",
    {
        "UpdateToken": str,
    },
)
_OptionalUpdateProvisionedProductInputRequestTypeDef = TypedDict(
    "_OptionalUpdateProvisionedProductInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "ProvisionedProductName": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProductName": str,
        "ProvisioningArtifactId": str,
        "ProvisioningArtifactName": str,
        "PathId": str,
        "PathName": str,
        "ProvisioningParameters": List["UpdateProvisioningParameterTypeDef"],
        "ProvisioningPreferences": "UpdateProvisioningPreferencesTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class UpdateProvisionedProductInputRequestTypeDef(
    _RequiredUpdateProvisionedProductInputRequestTypeDef,
    _OptionalUpdateProvisionedProductInputRequestTypeDef,
):
    pass

UpdateProvisionedProductOutputTypeDef = TypedDict(
    "UpdateProvisionedProductOutputTypeDef",
    {
        "RecordDetail": "RecordDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProvisionedProductPropertiesInputRequestTypeDef = TypedDict(
    "_RequiredUpdateProvisionedProductPropertiesInputRequestTypeDef",
    {
        "ProvisionedProductId": str,
        "ProvisionedProductProperties": Dict[PropertyKeyType, str],
        "IdempotencyToken": str,
    },
)
_OptionalUpdateProvisionedProductPropertiesInputRequestTypeDef = TypedDict(
    "_OptionalUpdateProvisionedProductPropertiesInputRequestTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)

class UpdateProvisionedProductPropertiesInputRequestTypeDef(
    _RequiredUpdateProvisionedProductPropertiesInputRequestTypeDef,
    _OptionalUpdateProvisionedProductPropertiesInputRequestTypeDef,
):
    pass

UpdateProvisionedProductPropertiesOutputTypeDef = TypedDict(
    "UpdateProvisionedProductPropertiesOutputTypeDef",
    {
        "ProvisionedProductId": str,
        "ProvisionedProductProperties": Dict[PropertyKeyType, str],
        "RecordId": str,
        "Status": RecordStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProvisioningArtifactInputRequestTypeDef = TypedDict(
    "_RequiredUpdateProvisioningArtifactInputRequestTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
    },
)
_OptionalUpdateProvisioningArtifactInputRequestTypeDef = TypedDict(
    "_OptionalUpdateProvisioningArtifactInputRequestTypeDef",
    {
        "AcceptLanguage": str,
        "Name": str,
        "Description": str,
        "Active": bool,
        "Guidance": ProvisioningArtifactGuidanceType,
    },
    total=False,
)

class UpdateProvisioningArtifactInputRequestTypeDef(
    _RequiredUpdateProvisioningArtifactInputRequestTypeDef,
    _OptionalUpdateProvisioningArtifactInputRequestTypeDef,
):
    pass

UpdateProvisioningArtifactOutputTypeDef = TypedDict(
    "UpdateProvisioningArtifactOutputTypeDef",
    {
        "ProvisioningArtifactDetail": "ProvisioningArtifactDetailTypeDef",
        "Info": Dict[str, str],
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateProvisioningParameterTypeDef = TypedDict(
    "UpdateProvisioningParameterTypeDef",
    {
        "Key": str,
        "Value": str,
        "UsePreviousValue": bool,
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
        "StackSetOperationType": StackSetOperationTypeType,
    },
    total=False,
)

_RequiredUpdateServiceActionInputRequestTypeDef = TypedDict(
    "_RequiredUpdateServiceActionInputRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateServiceActionInputRequestTypeDef = TypedDict(
    "_OptionalUpdateServiceActionInputRequestTypeDef",
    {
        "Name": str,
        "Definition": Dict[ServiceActionDefinitionKeyType, str],
        "Description": str,
        "AcceptLanguage": str,
    },
    total=False,
)

class UpdateServiceActionInputRequestTypeDef(
    _RequiredUpdateServiceActionInputRequestTypeDef, _OptionalUpdateServiceActionInputRequestTypeDef
):
    pass

UpdateServiceActionOutputTypeDef = TypedDict(
    "UpdateServiceActionOutputTypeDef",
    {
        "ServiceActionDetail": "ServiceActionDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTagOptionInputRequestTypeDef = TypedDict(
    "_RequiredUpdateTagOptionInputRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateTagOptionInputRequestTypeDef = TypedDict(
    "_OptionalUpdateTagOptionInputRequestTypeDef",
    {
        "Value": str,
        "Active": bool,
    },
    total=False,
)

class UpdateTagOptionInputRequestTypeDef(
    _RequiredUpdateTagOptionInputRequestTypeDef, _OptionalUpdateTagOptionInputRequestTypeDef
):
    pass

UpdateTagOptionOutputTypeDef = TypedDict(
    "UpdateTagOptionOutputTypeDef",
    {
        "TagOptionDetail": "TagOptionDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsageInstructionTypeDef = TypedDict(
    "UsageInstructionTypeDef",
    {
        "Type": str,
        "Value": str,
    },
    total=False,
)
