"""
Type annotations for servicecatalog service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/literals.html)

Usage::

    ```python
    from mypy_boto3_servicecatalog.literals import AccessLevelFilterKeyType

    data: AccessLevelFilterKeyType = "Account"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccessLevelFilterKeyType",
    "AccessStatusType",
    "ChangeActionType",
    "CopyOptionType",
    "CopyProductStatusType",
    "DescribePortfolioShareTypeType",
    "EvaluationTypeType",
    "ListAcceptedPortfolioSharesPaginatorName",
    "ListConstraintsForPortfolioPaginatorName",
    "ListLaunchPathsPaginatorName",
    "ListOrganizationPortfolioAccessPaginatorName",
    "ListPortfoliosForProductPaginatorName",
    "ListPortfoliosPaginatorName",
    "ListPrincipalsForPortfolioPaginatorName",
    "ListProvisionedProductPlansPaginatorName",
    "ListProvisioningArtifactsForServiceActionPaginatorName",
    "ListRecordHistoryPaginatorName",
    "ListResourcesForTagOptionPaginatorName",
    "ListServiceActionsForProvisioningArtifactPaginatorName",
    "ListServiceActionsPaginatorName",
    "ListTagOptionsPaginatorName",
    "OrganizationNodeTypeType",
    "PortfolioShareTypeType",
    "PrincipalTypeType",
    "ProductSourceType",
    "ProductTypeType",
    "ProductViewFilterByType",
    "ProductViewSortByType",
    "PropertyKeyType",
    "ProvisionedProductPlanStatusType",
    "ProvisionedProductPlanTypeType",
    "ProvisionedProductStatusType",
    "ProvisionedProductViewFilterByType",
    "ProvisioningArtifactGuidanceType",
    "ProvisioningArtifactPropertyNameType",
    "ProvisioningArtifactTypeType",
    "RecordStatusType",
    "ReplacementType",
    "RequiresRecreationType",
    "ResourceAttributeType",
    "ScanProvisionedProductsPaginatorName",
    "SearchProductsAsAdminPaginatorName",
    "ServiceActionAssociationErrorCodeType",
    "ServiceActionDefinitionKeyType",
    "ServiceActionDefinitionTypeType",
    "ShareStatusType",
    "SortOrderType",
    "StackInstanceStatusType",
    "StackSetOperationTypeType",
    "StatusType",
)

AccessLevelFilterKeyType = Literal["Account", "Role", "User"]
AccessStatusType = Literal["DISABLED", "ENABLED", "UNDER_CHANGE"]
ChangeActionType = Literal["ADD", "MODIFY", "REMOVE"]
CopyOptionType = Literal["CopyTags"]
CopyProductStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
DescribePortfolioShareTypeType = Literal[
    "ACCOUNT", "ORGANIZATION", "ORGANIZATIONAL_UNIT", "ORGANIZATION_MEMBER_ACCOUNT"
]
EvaluationTypeType = Literal["DYNAMIC", "STATIC"]
ListAcceptedPortfolioSharesPaginatorName = Literal["list_accepted_portfolio_shares"]
ListConstraintsForPortfolioPaginatorName = Literal["list_constraints_for_portfolio"]
ListLaunchPathsPaginatorName = Literal["list_launch_paths"]
ListOrganizationPortfolioAccessPaginatorName = Literal["list_organization_portfolio_access"]
ListPortfoliosForProductPaginatorName = Literal["list_portfolios_for_product"]
ListPortfoliosPaginatorName = Literal["list_portfolios"]
ListPrincipalsForPortfolioPaginatorName = Literal["list_principals_for_portfolio"]
ListProvisionedProductPlansPaginatorName = Literal["list_provisioned_product_plans"]
ListProvisioningArtifactsForServiceActionPaginatorName = Literal[
    "list_provisioning_artifacts_for_service_action"
]
ListRecordHistoryPaginatorName = Literal["list_record_history"]
ListResourcesForTagOptionPaginatorName = Literal["list_resources_for_tag_option"]
ListServiceActionsForProvisioningArtifactPaginatorName = Literal[
    "list_service_actions_for_provisioning_artifact"
]
ListServiceActionsPaginatorName = Literal["list_service_actions"]
ListTagOptionsPaginatorName = Literal["list_tag_options"]
OrganizationNodeTypeType = Literal["ACCOUNT", "ORGANIZATION", "ORGANIZATIONAL_UNIT"]
PortfolioShareTypeType = Literal["AWS_ORGANIZATIONS", "AWS_SERVICECATALOG", "IMPORTED"]
PrincipalTypeType = Literal["IAM"]
ProductSourceType = Literal["ACCOUNT"]
ProductTypeType = Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"]
ProductViewFilterByType = Literal["FullTextSearch", "Owner", "ProductType", "SourceProductId"]
ProductViewSortByType = Literal["CreationDate", "Title", "VersionCount"]
PropertyKeyType = Literal["LAUNCH_ROLE", "OWNER"]
ProvisionedProductPlanStatusType = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "CREATE_SUCCESS",
    "EXECUTE_FAILED",
    "EXECUTE_IN_PROGRESS",
    "EXECUTE_SUCCESS",
]
ProvisionedProductPlanTypeType = Literal["CLOUDFORMATION"]
ProvisionedProductStatusType = Literal[
    "AVAILABLE", "ERROR", "PLAN_IN_PROGRESS", "TAINTED", "UNDER_CHANGE"
]
ProvisionedProductViewFilterByType = Literal["SearchQuery"]
ProvisioningArtifactGuidanceType = Literal["DEFAULT", "DEPRECATED"]
ProvisioningArtifactPropertyNameType = Literal["Id"]
ProvisioningArtifactTypeType = Literal[
    "CLOUD_FORMATION_TEMPLATE", "MARKETPLACE_AMI", "MARKETPLACE_CAR"
]
RecordStatusType = Literal["CREATED", "FAILED", "IN_PROGRESS", "IN_PROGRESS_IN_ERROR", "SUCCEEDED"]
ReplacementType = Literal["CONDITIONAL", "FALSE", "TRUE"]
RequiresRecreationType = Literal["ALWAYS", "CONDITIONALLY", "NEVER"]
ResourceAttributeType = Literal[
    "CREATIONPOLICY", "DELETIONPOLICY", "METADATA", "PROPERTIES", "TAGS", "UPDATEPOLICY"
]
ScanProvisionedProductsPaginatorName = Literal["scan_provisioned_products"]
SearchProductsAsAdminPaginatorName = Literal["search_products_as_admin"]
ServiceActionAssociationErrorCodeType = Literal[
    "DUPLICATE_RESOURCE", "INTERNAL_FAILURE", "LIMIT_EXCEEDED", "RESOURCE_NOT_FOUND", "THROTTLING"
]
ServiceActionDefinitionKeyType = Literal["AssumeRole", "Name", "Parameters", "Version"]
ServiceActionDefinitionTypeType = Literal["SSM_AUTOMATION"]
ShareStatusType = Literal[
    "COMPLETED", "COMPLETED_WITH_ERRORS", "ERROR", "IN_PROGRESS", "NOT_STARTED"
]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
StackInstanceStatusType = Literal["CURRENT", "INOPERABLE", "OUTDATED"]
StackSetOperationTypeType = Literal["CREATE", "DELETE", "UPDATE"]
StatusType = Literal["AVAILABLE", "CREATING", "FAILED"]
