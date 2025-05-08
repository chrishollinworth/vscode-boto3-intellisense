"""
Type annotations for datazone service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_datazone.type_defs import AcceptChoiceTypeDef

    data: AcceptChoiceTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    AcceptRuleBehaviorType,
    AuthenticationTypeType,
    AuthTypeType,
    ChangeActionType,
    ComputeEnvironmentsType,
    ConfigurableActionTypeAuthorizationType,
    ConnectionStatusType,
    ConnectionTypeType,
    DataAssetActivityStatusType,
    DataProductStatusType,
    DataSourceErrorTypeType,
    DataSourceRunStatusType,
    DataSourceRunTypeType,
    DataSourceStatusType,
    DeploymentModeType,
    DeploymentStatusType,
    DeploymentTypeType,
    DomainStatusType,
    DomainVersionType,
    EdgeDirectionType,
    EnableSettingType,
    EntityTypeType,
    EnvironmentStatusType,
    FilterExpressionTypeType,
    FilterStatusType,
    FormTypeStatusType,
    GlossaryStatusType,
    GlossaryTermStatusType,
    GlueConnectionTypeType,
    GovernanceTypeType,
    GroupProfileStatusType,
    GroupSearchTypeType,
    HyperPodOrchestratorType,
    InventorySearchScopeType,
    JobRunModeType,
    JobRunStatusType,
    LineageEventProcessingStatusType,
    LineageImportStatusType,
    ListingStatusType,
    ManagedPolicyTypeType,
    MetadataGenerationRunStatusType,
    NotificationRoleType,
    NotificationTypeType,
    OAuth2GrantTypeType,
    OpenLineageRunStateType,
    OverallDeploymentStatusType,
    ProjectDesignationType,
    ProjectStatusType,
    ProtocolType,
    RejectRuleBehaviorType,
    RuleActionType,
    RuleScopeSelectionModeType,
    SearchOutputAdditionalAttributeType,
    SelfGrantStatusType,
    SortKeyType,
    SortOrderType,
    StatusType,
    SubscriptionGrantOverallStatusType,
    SubscriptionGrantStatusType,
    SubscriptionRequestStatusType,
    SubscriptionStatusType,
    TargetEntityTypeType,
    TaskStatusType,
    TimeSeriesEntityTypeType,
    TimezoneType,
    TypesSearchScopeType,
    UserAssignmentType,
    UserDesignationType,
    UserProfileStatusType,
    UserProfileTypeType,
    UserSearchTypeType,
    UserTypeType,
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
    "AcceptChoiceTypeDef",
    "AcceptPredictionsInputTypeDef",
    "AcceptPredictionsOutputTypeDef",
    "AcceptRuleTypeDef",
    "AcceptSubscriptionRequestInputTypeDef",
    "AcceptSubscriptionRequestOutputTypeDef",
    "AcceptedAssetScopeTypeDef",
    "ActionParametersTypeDef",
    "AddEntityOwnerInputTypeDef",
    "AddPolicyGrantInputTypeDef",
    "AddToProjectMemberPoolPolicyGrantDetailTypeDef",
    "AssetFilterConfigurationOutputTypeDef",
    "AssetFilterConfigurationTypeDef",
    "AssetFilterConfigurationUnionTypeDef",
    "AssetFilterSummaryTypeDef",
    "AssetInDataProductListingItemTypeDef",
    "AssetItemAdditionalAttributesTypeDef",
    "AssetItemTypeDef",
    "AssetListingDetailsTypeDef",
    "AssetListingItemAdditionalAttributesTypeDef",
    "AssetListingItemTypeDef",
    "AssetListingTypeDef",
    "AssetRevisionTypeDef",
    "AssetScopeTypeDef",
    "AssetTargetNameMapTypeDef",
    "AssetTypeItemTypeDef",
    "AssetTypesForRuleOutputTypeDef",
    "AssetTypesForRuleTypeDef",
    "AssociateEnvironmentRoleInputTypeDef",
    "AthenaPropertiesInputTypeDef",
    "AthenaPropertiesOutputTypeDef",
    "AthenaPropertiesPatchTypeDef",
    "AuthenticationConfigurationInputTypeDef",
    "AuthenticationConfigurationPatchTypeDef",
    "AuthenticationConfigurationTypeDef",
    "AuthorizationCodePropertiesTypeDef",
    "AwsAccountTypeDef",
    "AwsConsoleLinkParametersTypeDef",
    "AwsLocationTypeDef",
    "BasicAuthenticationCredentialsTypeDef",
    "BlobTypeDef",
    "BusinessNameGenerationConfigurationTypeDef",
    "CancelMetadataGenerationRunInputTypeDef",
    "CancelSubscriptionInputTypeDef",
    "CancelSubscriptionOutputTypeDef",
    "CloudFormationPropertiesTypeDef",
    "ColumnFilterConfigurationOutputTypeDef",
    "ColumnFilterConfigurationTypeDef",
    "ConfigurableActionParameterTypeDef",
    "ConfigurableEnvironmentActionTypeDef",
    "ConnectionCredentialsTypeDef",
    "ConnectionPropertiesInputTypeDef",
    "ConnectionPropertiesOutputTypeDef",
    "ConnectionPropertiesPatchTypeDef",
    "ConnectionSummaryTypeDef",
    "CreateAssetFilterInputTypeDef",
    "CreateAssetFilterOutputTypeDef",
    "CreateAssetInputTypeDef",
    "CreateAssetOutputTypeDef",
    "CreateAssetRevisionInputTypeDef",
    "CreateAssetRevisionOutputTypeDef",
    "CreateAssetTypeInputTypeDef",
    "CreateAssetTypeOutputTypeDef",
    "CreateAssetTypePolicyGrantDetailTypeDef",
    "CreateConnectionInputTypeDef",
    "CreateConnectionOutputTypeDef",
    "CreateDataProductInputTypeDef",
    "CreateDataProductOutputTypeDef",
    "CreateDataProductRevisionInputTypeDef",
    "CreateDataProductRevisionOutputTypeDef",
    "CreateDataSourceInputTypeDef",
    "CreateDataSourceOutputTypeDef",
    "CreateDomainInputTypeDef",
    "CreateDomainOutputTypeDef",
    "CreateDomainUnitInputTypeDef",
    "CreateDomainUnitOutputTypeDef",
    "CreateDomainUnitPolicyGrantDetailTypeDef",
    "CreateEnvironmentActionInputTypeDef",
    "CreateEnvironmentActionOutputTypeDef",
    "CreateEnvironmentInputTypeDef",
    "CreateEnvironmentOutputTypeDef",
    "CreateEnvironmentProfileInputTypeDef",
    "CreateEnvironmentProfileOutputTypeDef",
    "CreateEnvironmentProfilePolicyGrantDetailTypeDef",
    "CreateFormTypeInputTypeDef",
    "CreateFormTypeOutputTypeDef",
    "CreateFormTypePolicyGrantDetailTypeDef",
    "CreateGlossaryInputTypeDef",
    "CreateGlossaryOutputTypeDef",
    "CreateGlossaryPolicyGrantDetailTypeDef",
    "CreateGlossaryTermInputTypeDef",
    "CreateGlossaryTermOutputTypeDef",
    "CreateGroupProfileInputTypeDef",
    "CreateGroupProfileOutputTypeDef",
    "CreateListingChangeSetInputTypeDef",
    "CreateListingChangeSetOutputTypeDef",
    "CreateProjectFromProjectProfilePolicyGrantDetailOutputTypeDef",
    "CreateProjectFromProjectProfilePolicyGrantDetailTypeDef",
    "CreateProjectInputTypeDef",
    "CreateProjectMembershipInputTypeDef",
    "CreateProjectOutputTypeDef",
    "CreateProjectPolicyGrantDetailTypeDef",
    "CreateProjectProfileInputTypeDef",
    "CreateProjectProfileOutputTypeDef",
    "CreateRuleInputTypeDef",
    "CreateRuleOutputTypeDef",
    "CreateSubscriptionGrantInputTypeDef",
    "CreateSubscriptionGrantOutputTypeDef",
    "CreateSubscriptionRequestInputTypeDef",
    "CreateSubscriptionRequestOutputTypeDef",
    "CreateSubscriptionTargetInputTypeDef",
    "CreateSubscriptionTargetOutputTypeDef",
    "CreateUserProfileInputTypeDef",
    "CreateUserProfileOutputTypeDef",
    "CustomParameterTypeDef",
    "DataProductItemOutputTypeDef",
    "DataProductItemTypeDef",
    "DataProductItemUnionTypeDef",
    "DataProductListingItemAdditionalAttributesTypeDef",
    "DataProductListingItemTypeDef",
    "DataProductListingTypeDef",
    "DataProductResultItemTypeDef",
    "DataProductRevisionTypeDef",
    "DataSourceConfigurationInputTypeDef",
    "DataSourceConfigurationOutputTypeDef",
    "DataSourceErrorMessageTypeDef",
    "DataSourceRunActivityTypeDef",
    "DataSourceRunLineageSummaryTypeDef",
    "DataSourceRunSummaryTypeDef",
    "DataSourceSummaryTypeDef",
    "DeleteAssetFilterInputTypeDef",
    "DeleteAssetInputTypeDef",
    "DeleteAssetTypeInputTypeDef",
    "DeleteConnectionInputTypeDef",
    "DeleteConnectionOutputTypeDef",
    "DeleteDataProductInputTypeDef",
    "DeleteDataSourceInputTypeDef",
    "DeleteDataSourceOutputTypeDef",
    "DeleteDomainInputTypeDef",
    "DeleteDomainOutputTypeDef",
    "DeleteDomainUnitInputTypeDef",
    "DeleteEnvironmentActionInputTypeDef",
    "DeleteEnvironmentBlueprintConfigurationInputTypeDef",
    "DeleteEnvironmentInputTypeDef",
    "DeleteEnvironmentProfileInputTypeDef",
    "DeleteFormTypeInputTypeDef",
    "DeleteGlossaryInputTypeDef",
    "DeleteGlossaryTermInputTypeDef",
    "DeleteListingInputTypeDef",
    "DeleteProjectInputTypeDef",
    "DeleteProjectMembershipInputTypeDef",
    "DeleteProjectProfileInputTypeDef",
    "DeleteRuleInputTypeDef",
    "DeleteSubscriptionGrantInputTypeDef",
    "DeleteSubscriptionGrantOutputTypeDef",
    "DeleteSubscriptionRequestInputTypeDef",
    "DeleteSubscriptionTargetInputTypeDef",
    "DeleteTimeSeriesDataPointsInputTypeDef",
    "DeploymentPropertiesTypeDef",
    "DeploymentTypeDef",
    "DetailedGlossaryTermTypeDef",
    "DisassociateEnvironmentRoleInputTypeDef",
    "DomainSummaryTypeDef",
    "DomainUnitFilterForProjectTypeDef",
    "DomainUnitGrantFilterOutputTypeDef",
    "DomainUnitGrantFilterTypeDef",
    "DomainUnitGroupPropertiesTypeDef",
    "DomainUnitOwnerPropertiesTypeDef",
    "DomainUnitPolicyGrantPrincipalOutputTypeDef",
    "DomainUnitPolicyGrantPrincipalTypeDef",
    "DomainUnitSummaryTypeDef",
    "DomainUnitTargetTypeDef",
    "DomainUnitUserPropertiesTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnvironmentActionSummaryTypeDef",
    "EnvironmentBlueprintConfigurationItemTypeDef",
    "EnvironmentBlueprintSummaryTypeDef",
    "EnvironmentConfigurationOutputTypeDef",
    "EnvironmentConfigurationParameterTypeDef",
    "EnvironmentConfigurationParametersDetailsOutputTypeDef",
    "EnvironmentConfigurationParametersDetailsTypeDef",
    "EnvironmentConfigurationParametersDetailsUnionTypeDef",
    "EnvironmentConfigurationTypeDef",
    "EnvironmentConfigurationUnionTypeDef",
    "EnvironmentConfigurationUserParameterOutputTypeDef",
    "EnvironmentConfigurationUserParameterTypeDef",
    "EnvironmentConfigurationUserParameterUnionTypeDef",
    "EnvironmentDeploymentDetailsOutputTypeDef",
    "EnvironmentDeploymentDetailsTypeDef",
    "EnvironmentDeploymentDetailsUnionTypeDef",
    "EnvironmentErrorTypeDef",
    "EnvironmentParameterTypeDef",
    "EnvironmentProfileSummaryTypeDef",
    "EnvironmentSummaryTypeDef",
    "EqualToExpressionTypeDef",
    "EventSummaryTypeDef",
    "FailureCauseTypeDef",
    "FilterClausePaginatorTypeDef",
    "FilterClauseTypeDef",
    "FilterExpressionTypeDef",
    "FilterTypeDef",
    "FormEntryInputTypeDef",
    "FormEntryOutputTypeDef",
    "FormInputTypeDef",
    "FormOutputTypeDef",
    "FormTypeDataTypeDef",
    "GetAssetFilterInputTypeDef",
    "GetAssetFilterOutputTypeDef",
    "GetAssetInputTypeDef",
    "GetAssetOutputTypeDef",
    "GetAssetTypeInputTypeDef",
    "GetAssetTypeOutputTypeDef",
    "GetConnectionInputTypeDef",
    "GetConnectionOutputTypeDef",
    "GetDataProductInputTypeDef",
    "GetDataProductOutputTypeDef",
    "GetDataSourceInputTypeDef",
    "GetDataSourceOutputTypeDef",
    "GetDataSourceRunInputTypeDef",
    "GetDataSourceRunOutputTypeDef",
    "GetDomainInputTypeDef",
    "GetDomainOutputTypeDef",
    "GetDomainUnitInputTypeDef",
    "GetDomainUnitOutputTypeDef",
    "GetEnvironmentActionInputTypeDef",
    "GetEnvironmentActionOutputTypeDef",
    "GetEnvironmentBlueprintConfigurationInputTypeDef",
    "GetEnvironmentBlueprintConfigurationOutputTypeDef",
    "GetEnvironmentBlueprintInputTypeDef",
    "GetEnvironmentBlueprintOutputTypeDef",
    "GetEnvironmentCredentialsInputTypeDef",
    "GetEnvironmentCredentialsOutputTypeDef",
    "GetEnvironmentInputTypeDef",
    "GetEnvironmentOutputTypeDef",
    "GetEnvironmentProfileInputTypeDef",
    "GetEnvironmentProfileOutputTypeDef",
    "GetFormTypeInputTypeDef",
    "GetFormTypeOutputTypeDef",
    "GetGlossaryInputTypeDef",
    "GetGlossaryOutputTypeDef",
    "GetGlossaryTermInputTypeDef",
    "GetGlossaryTermOutputTypeDef",
    "GetGroupProfileInputTypeDef",
    "GetGroupProfileOutputTypeDef",
    "GetIamPortalLoginUrlInputTypeDef",
    "GetIamPortalLoginUrlOutputTypeDef",
    "GetJobRunInputTypeDef",
    "GetJobRunOutputTypeDef",
    "GetLineageEventInputTypeDef",
    "GetLineageEventOutputTypeDef",
    "GetLineageNodeInputTypeDef",
    "GetLineageNodeOutputTypeDef",
    "GetListingInputTypeDef",
    "GetListingOutputTypeDef",
    "GetMetadataGenerationRunInputTypeDef",
    "GetMetadataGenerationRunOutputTypeDef",
    "GetProjectInputTypeDef",
    "GetProjectOutputTypeDef",
    "GetProjectProfileInputTypeDef",
    "GetProjectProfileOutputTypeDef",
    "GetRuleInputTypeDef",
    "GetRuleOutputTypeDef",
    "GetSubscriptionGrantInputTypeDef",
    "GetSubscriptionGrantOutputTypeDef",
    "GetSubscriptionInputTypeDef",
    "GetSubscriptionOutputTypeDef",
    "GetSubscriptionRequestDetailsInputTypeDef",
    "GetSubscriptionRequestDetailsOutputTypeDef",
    "GetSubscriptionTargetInputTypeDef",
    "GetSubscriptionTargetOutputTypeDef",
    "GetTimeSeriesDataPointInputTypeDef",
    "GetTimeSeriesDataPointOutputTypeDef",
    "GetUserProfileInputTypeDef",
    "GetUserProfileOutputTypeDef",
    "GlossaryItemTypeDef",
    "GlossaryTermItemTypeDef",
    "GlueConnectionInputTypeDef",
    "GlueConnectionPatchTypeDef",
    "GlueConnectionTypeDef",
    "GlueOAuth2CredentialsTypeDef",
    "GluePropertiesInputTypeDef",
    "GluePropertiesOutputTypeDef",
    "GluePropertiesPatchTypeDef",
    "GlueRunConfigurationInputTypeDef",
    "GlueRunConfigurationOutputTypeDef",
    "GlueSelfGrantStatusOutputTypeDef",
    "GrantedEntityInputTypeDef",
    "GrantedEntityTypeDef",
    "GreaterThanExpressionTypeDef",
    "GreaterThanOrEqualToExpressionTypeDef",
    "GroupDetailsTypeDef",
    "GroupPolicyGrantPrincipalTypeDef",
    "GroupProfileSummaryTypeDef",
    "HyperPodPropertiesInputTypeDef",
    "HyperPodPropertiesOutputTypeDef",
    "IamPropertiesInputTypeDef",
    "IamPropertiesOutputTypeDef",
    "IamPropertiesPatchTypeDef",
    "IamUserProfileDetailsTypeDef",
    "ImportTypeDef",
    "InExpressionOutputTypeDef",
    "InExpressionTypeDef",
    "IsNotNullExpressionTypeDef",
    "IsNullExpressionTypeDef",
    "JobRunDetailsTypeDef",
    "JobRunErrorTypeDef",
    "JobRunSummaryTypeDef",
    "LakeFormationConfigurationOutputTypeDef",
    "LakeFormationConfigurationTypeDef",
    "LakeFormationConfigurationUnionTypeDef",
    "LessThanExpressionTypeDef",
    "LessThanOrEqualToExpressionTypeDef",
    "LikeExpressionTypeDef",
    "LineageEventSummaryTypeDef",
    "LineageInfoTypeDef",
    "LineageNodeReferenceTypeDef",
    "LineageNodeSummaryTypeDef",
    "LineageNodeTypeItemTypeDef",
    "LineageRunDetailsTypeDef",
    "LineageSqlQueryRunDetailsTypeDef",
    "LineageSyncScheduleTypeDef",
    "ListAssetFiltersInputPaginateTypeDef",
    "ListAssetFiltersInputTypeDef",
    "ListAssetFiltersOutputTypeDef",
    "ListAssetRevisionsInputPaginateTypeDef",
    "ListAssetRevisionsInputTypeDef",
    "ListAssetRevisionsOutputTypeDef",
    "ListConnectionsInputPaginateTypeDef",
    "ListConnectionsInputTypeDef",
    "ListConnectionsOutputTypeDef",
    "ListDataProductRevisionsInputPaginateTypeDef",
    "ListDataProductRevisionsInputTypeDef",
    "ListDataProductRevisionsOutputTypeDef",
    "ListDataSourceRunActivitiesInputPaginateTypeDef",
    "ListDataSourceRunActivitiesInputTypeDef",
    "ListDataSourceRunActivitiesOutputTypeDef",
    "ListDataSourceRunsInputPaginateTypeDef",
    "ListDataSourceRunsInputTypeDef",
    "ListDataSourceRunsOutputTypeDef",
    "ListDataSourcesInputPaginateTypeDef",
    "ListDataSourcesInputTypeDef",
    "ListDataSourcesOutputTypeDef",
    "ListDomainUnitsForParentInputPaginateTypeDef",
    "ListDomainUnitsForParentInputTypeDef",
    "ListDomainUnitsForParentOutputTypeDef",
    "ListDomainsInputPaginateTypeDef",
    "ListDomainsInputTypeDef",
    "ListDomainsOutputTypeDef",
    "ListEntityOwnersInputPaginateTypeDef",
    "ListEntityOwnersInputTypeDef",
    "ListEntityOwnersOutputTypeDef",
    "ListEnvironmentActionsInputPaginateTypeDef",
    "ListEnvironmentActionsInputTypeDef",
    "ListEnvironmentActionsOutputTypeDef",
    "ListEnvironmentBlueprintConfigurationsInputPaginateTypeDef",
    "ListEnvironmentBlueprintConfigurationsInputTypeDef",
    "ListEnvironmentBlueprintConfigurationsOutputTypeDef",
    "ListEnvironmentBlueprintsInputPaginateTypeDef",
    "ListEnvironmentBlueprintsInputTypeDef",
    "ListEnvironmentBlueprintsOutputTypeDef",
    "ListEnvironmentProfilesInputPaginateTypeDef",
    "ListEnvironmentProfilesInputTypeDef",
    "ListEnvironmentProfilesOutputTypeDef",
    "ListEnvironmentsInputPaginateTypeDef",
    "ListEnvironmentsInputTypeDef",
    "ListEnvironmentsOutputTypeDef",
    "ListJobRunsInputPaginateTypeDef",
    "ListJobRunsInputTypeDef",
    "ListJobRunsOutputTypeDef",
    "ListLineageEventsInputPaginateTypeDef",
    "ListLineageEventsInputTypeDef",
    "ListLineageEventsOutputTypeDef",
    "ListLineageNodeHistoryInputPaginateTypeDef",
    "ListLineageNodeHistoryInputTypeDef",
    "ListLineageNodeHistoryOutputTypeDef",
    "ListMetadataGenerationRunsInputPaginateTypeDef",
    "ListMetadataGenerationRunsInputTypeDef",
    "ListMetadataGenerationRunsOutputTypeDef",
    "ListNotificationsInputPaginateTypeDef",
    "ListNotificationsInputTypeDef",
    "ListNotificationsOutputTypeDef",
    "ListPolicyGrantsInputPaginateTypeDef",
    "ListPolicyGrantsInputTypeDef",
    "ListPolicyGrantsOutputTypeDef",
    "ListProjectMembershipsInputPaginateTypeDef",
    "ListProjectMembershipsInputTypeDef",
    "ListProjectMembershipsOutputTypeDef",
    "ListProjectProfilesInputPaginateTypeDef",
    "ListProjectProfilesInputTypeDef",
    "ListProjectProfilesOutputTypeDef",
    "ListProjectsInputPaginateTypeDef",
    "ListProjectsInputTypeDef",
    "ListProjectsOutputTypeDef",
    "ListRulesInputPaginateTypeDef",
    "ListRulesInputTypeDef",
    "ListRulesOutputTypeDef",
    "ListSubscriptionGrantsInputPaginateTypeDef",
    "ListSubscriptionGrantsInputTypeDef",
    "ListSubscriptionGrantsOutputTypeDef",
    "ListSubscriptionRequestsInputPaginateTypeDef",
    "ListSubscriptionRequestsInputTypeDef",
    "ListSubscriptionRequestsOutputTypeDef",
    "ListSubscriptionTargetsInputPaginateTypeDef",
    "ListSubscriptionTargetsInputTypeDef",
    "ListSubscriptionTargetsOutputTypeDef",
    "ListSubscriptionsInputPaginateTypeDef",
    "ListSubscriptionsInputTypeDef",
    "ListSubscriptionsOutputTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTimeSeriesDataPointsInputPaginateTypeDef",
    "ListTimeSeriesDataPointsInputTypeDef",
    "ListTimeSeriesDataPointsOutputTypeDef",
    "ListingItemTypeDef",
    "ListingRevisionInputTypeDef",
    "ListingRevisionTypeDef",
    "ListingSummaryItemTypeDef",
    "ListingSummaryTypeDef",
    "MemberDetailsTypeDef",
    "MemberTypeDef",
    "MetadataFormEnforcementDetailOutputTypeDef",
    "MetadataFormEnforcementDetailTypeDef",
    "MetadataFormReferenceTypeDef",
    "MetadataFormSummaryTypeDef",
    "MetadataGenerationRunItemTypeDef",
    "MetadataGenerationRunTargetTypeDef",
    "ModelTypeDef",
    "NameIdentifierTypeDef",
    "NotEqualToExpressionTypeDef",
    "NotInExpressionOutputTypeDef",
    "NotInExpressionTypeDef",
    "NotLikeExpressionTypeDef",
    "NotificationOutputTypeDef",
    "NotificationResourceTypeDef",
    "OAuth2ClientApplicationTypeDef",
    "OAuth2PropertiesOutputTypeDef",
    "OAuth2PropertiesTypeDef",
    "OAuth2PropertiesUnionTypeDef",
    "OpenLineageRunEventSummaryTypeDef",
    "OverrideDomainUnitOwnersPolicyGrantDetailTypeDef",
    "OverrideProjectOwnersPolicyGrantDetailTypeDef",
    "OwnerGroupPropertiesOutputTypeDef",
    "OwnerGroupPropertiesTypeDef",
    "OwnerPropertiesOutputTypeDef",
    "OwnerPropertiesTypeDef",
    "OwnerUserPropertiesOutputTypeDef",
    "OwnerUserPropertiesTypeDef",
    "PaginatorConfigTypeDef",
    "PhysicalConnectionRequirementsOutputTypeDef",
    "PhysicalConnectionRequirementsTypeDef",
    "PhysicalConnectionRequirementsUnionTypeDef",
    "PhysicalEndpointTypeDef",
    "PolicyGrantDetailOutputTypeDef",
    "PolicyGrantDetailTypeDef",
    "PolicyGrantDetailUnionTypeDef",
    "PolicyGrantMemberTypeDef",
    "PolicyGrantPrincipalOutputTypeDef",
    "PolicyGrantPrincipalTypeDef",
    "PolicyGrantPrincipalUnionTypeDef",
    "PostLineageEventInputTypeDef",
    "PostLineageEventOutputTypeDef",
    "PostTimeSeriesDataPointsInputTypeDef",
    "PostTimeSeriesDataPointsOutputTypeDef",
    "PredictionConfigurationTypeDef",
    "ProjectDeletionErrorTypeDef",
    "ProjectGrantFilterTypeDef",
    "ProjectMemberTypeDef",
    "ProjectPolicyGrantPrincipalTypeDef",
    "ProjectProfileSummaryTypeDef",
    "ProjectSummaryTypeDef",
    "ProjectsForRuleOutputTypeDef",
    "ProjectsForRuleTypeDef",
    "ProvisioningConfigurationOutputTypeDef",
    "ProvisioningConfigurationTypeDef",
    "ProvisioningConfigurationUnionTypeDef",
    "ProvisioningPropertiesTypeDef",
    "PutEnvironmentBlueprintConfigurationInputTypeDef",
    "PutEnvironmentBlueprintConfigurationOutputTypeDef",
    "RecommendationConfigurationTypeDef",
    "RedshiftClusterStorageTypeDef",
    "RedshiftCredentialConfigurationTypeDef",
    "RedshiftCredentialsTypeDef",
    "RedshiftLineageSyncConfigurationInputTypeDef",
    "RedshiftLineageSyncConfigurationOutputTypeDef",
    "RedshiftPropertiesInputTypeDef",
    "RedshiftPropertiesOutputTypeDef",
    "RedshiftPropertiesPatchTypeDef",
    "RedshiftRunConfigurationInputTypeDef",
    "RedshiftRunConfigurationOutputTypeDef",
    "RedshiftSelfGrantStatusOutputTypeDef",
    "RedshiftServerlessStorageTypeDef",
    "RedshiftStoragePropertiesTypeDef",
    "RedshiftStorageTypeDef",
    "RegionTypeDef",
    "RejectChoiceTypeDef",
    "RejectPredictionsInputTypeDef",
    "RejectPredictionsOutputTypeDef",
    "RejectRuleTypeDef",
    "RejectSubscriptionRequestInputTypeDef",
    "RejectSubscriptionRequestOutputTypeDef",
    "RelationalFilterConfigurationOutputTypeDef",
    "RelationalFilterConfigurationTypeDef",
    "RelationalFilterConfigurationUnionTypeDef",
    "RemoveEntityOwnerInputTypeDef",
    "RemovePolicyGrantInputTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeSubscriptionInputTypeDef",
    "RevokeSubscriptionOutputTypeDef",
    "RowFilterConfigurationOutputTypeDef",
    "RowFilterConfigurationTypeDef",
    "RowFilterExpressionOutputTypeDef",
    "RowFilterExpressionTypeDef",
    "RowFilterOutputTypeDef",
    "RowFilterTypeDef",
    "RuleDetailOutputTypeDef",
    "RuleDetailTypeDef",
    "RuleDetailUnionTypeDef",
    "RuleScopeOutputTypeDef",
    "RuleScopeTypeDef",
    "RuleScopeUnionTypeDef",
    "RuleSummaryTypeDef",
    "RuleTargetTypeDef",
    "RunStatisticsForAssetsTypeDef",
    "SageMakerRunConfigurationInputTypeDef",
    "SageMakerRunConfigurationOutputTypeDef",
    "ScheduleConfigurationTypeDef",
    "SearchGroupProfilesInputPaginateTypeDef",
    "SearchGroupProfilesInputTypeDef",
    "SearchGroupProfilesOutputTypeDef",
    "SearchInItemTypeDef",
    "SearchInputPaginateTypeDef",
    "SearchInputTypeDef",
    "SearchInventoryResultItemTypeDef",
    "SearchListingsInputPaginateTypeDef",
    "SearchListingsInputTypeDef",
    "SearchListingsOutputTypeDef",
    "SearchOutputTypeDef",
    "SearchResultItemTypeDef",
    "SearchSortTypeDef",
    "SearchTypesInputPaginateTypeDef",
    "SearchTypesInputTypeDef",
    "SearchTypesOutputTypeDef",
    "SearchTypesResultItemTypeDef",
    "SearchUserProfilesInputPaginateTypeDef",
    "SearchUserProfilesInputTypeDef",
    "SearchUserProfilesOutputTypeDef",
    "SelfGrantStatusDetailTypeDef",
    "SelfGrantStatusOutputTypeDef",
    "SingleSignOnTypeDef",
    "SparkEmrPropertiesInputTypeDef",
    "SparkEmrPropertiesOutputTypeDef",
    "SparkEmrPropertiesPatchTypeDef",
    "SparkGlueArgsTypeDef",
    "SparkGluePropertiesInputTypeDef",
    "SparkGluePropertiesOutputTypeDef",
    "SsoUserProfileDetailsTypeDef",
    "StartDataSourceRunInputTypeDef",
    "StartDataSourceRunOutputTypeDef",
    "StartMetadataGenerationRunInputTypeDef",
    "StartMetadataGenerationRunOutputTypeDef",
    "SubscribedAssetListingTypeDef",
    "SubscribedAssetTypeDef",
    "SubscribedListingInputTypeDef",
    "SubscribedListingItemTypeDef",
    "SubscribedListingTypeDef",
    "SubscribedPrincipalInputTypeDef",
    "SubscribedPrincipalTypeDef",
    "SubscribedProductListingTypeDef",
    "SubscribedProjectInputTypeDef",
    "SubscribedProjectTypeDef",
    "SubscriptionGrantSummaryTypeDef",
    "SubscriptionRequestSummaryTypeDef",
    "SubscriptionSummaryTypeDef",
    "SubscriptionTargetFormTypeDef",
    "SubscriptionTargetSummaryTypeDef",
    "TagResourceRequestTypeDef",
    "TermRelationsOutputTypeDef",
    "TermRelationsTypeDef",
    "TermRelationsUnionTypeDef",
    "TimeSeriesDataPointFormInputTypeDef",
    "TimeSeriesDataPointFormOutputTypeDef",
    "TimeSeriesDataPointSummaryFormOutputTypeDef",
    "TimestampTypeDef",
    "TopicTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAssetFilterInputTypeDef",
    "UpdateAssetFilterOutputTypeDef",
    "UpdateConnectionInputTypeDef",
    "UpdateConnectionOutputTypeDef",
    "UpdateDataSourceInputTypeDef",
    "UpdateDataSourceOutputTypeDef",
    "UpdateDomainInputTypeDef",
    "UpdateDomainOutputTypeDef",
    "UpdateDomainUnitInputTypeDef",
    "UpdateDomainUnitOutputTypeDef",
    "UpdateEnvironmentActionInputTypeDef",
    "UpdateEnvironmentActionOutputTypeDef",
    "UpdateEnvironmentInputTypeDef",
    "UpdateEnvironmentOutputTypeDef",
    "UpdateEnvironmentProfileInputTypeDef",
    "UpdateEnvironmentProfileOutputTypeDef",
    "UpdateGlossaryInputTypeDef",
    "UpdateGlossaryOutputTypeDef",
    "UpdateGlossaryTermInputTypeDef",
    "UpdateGlossaryTermOutputTypeDef",
    "UpdateGroupProfileInputTypeDef",
    "UpdateGroupProfileOutputTypeDef",
    "UpdateProjectInputTypeDef",
    "UpdateProjectOutputTypeDef",
    "UpdateProjectProfileInputTypeDef",
    "UpdateProjectProfileOutputTypeDef",
    "UpdateRuleInputTypeDef",
    "UpdateRuleOutputTypeDef",
    "UpdateSubscriptionGrantStatusInputTypeDef",
    "UpdateSubscriptionGrantStatusOutputTypeDef",
    "UpdateSubscriptionRequestInputTypeDef",
    "UpdateSubscriptionRequestOutputTypeDef",
    "UpdateSubscriptionTargetInputTypeDef",
    "UpdateSubscriptionTargetOutputTypeDef",
    "UpdateUserProfileInputTypeDef",
    "UpdateUserProfileOutputTypeDef",
    "UseAssetTypePolicyGrantDetailTypeDef",
    "UserDetailsTypeDef",
    "UserPolicyGrantPrincipalOutputTypeDef",
    "UserPolicyGrantPrincipalTypeDef",
    "UserProfileDetailsTypeDef",
    "UserProfileSummaryTypeDef",
    "UsernamePasswordTypeDef",
)

class AcceptChoiceTypeDef(TypedDict):
    predictionTarget: str
    editedValue: NotRequired[str]
    predictionChoice: NotRequired[int]

class AcceptRuleTypeDef(TypedDict):
    rule: NotRequired[AcceptRuleBehaviorType]
    threshold: NotRequired[float]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AcceptedAssetScopeTypeDef(TypedDict):
    assetId: str
    filterIds: Sequence[str]

class FormOutputTypeDef(TypedDict):
    formName: str
    content: NotRequired[str]
    typeName: NotRequired[str]
    typeRevision: NotRequired[str]

class AwsConsoleLinkParametersTypeDef(TypedDict):
    uri: NotRequired[str]

class AddToProjectMemberPoolPolicyGrantDetailTypeDef(TypedDict):
    includeChildDomainUnits: NotRequired[bool]

class ColumnFilterConfigurationOutputTypeDef(TypedDict):
    includedColumnNames: NotRequired[List[str]]

class ColumnFilterConfigurationTypeDef(TypedDict):
    includedColumnNames: NotRequired[Sequence[str]]

AssetFilterSummaryTypeDef = TypedDict(
    "AssetFilterSummaryTypeDef",
    {
        "assetId": str,
        "domainId": str,
        "id": str,
        "name": str,
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "effectiveColumnNames": NotRequired[List[str]],
        "effectiveRowFilter": NotRequired[str],
        "errorMessage": NotRequired[str],
        "status": NotRequired[FilterStatusType],
    },
)

class AssetInDataProductListingItemTypeDef(TypedDict):
    entityId: NotRequired[str]
    entityRevision: NotRequired[str]
    entityType: NotRequired[str]

TimeSeriesDataPointSummaryFormOutputTypeDef = TypedDict(
    "TimeSeriesDataPointSummaryFormOutputTypeDef",
    {
        "formName": str,
        "timestamp": datetime,
        "typeIdentifier": str,
        "contentSummary": NotRequired[str],
        "id": NotRequired[str],
        "typeRevision": NotRequired[str],
    },
)

class AssetListingDetailsTypeDef(TypedDict):
    listingId: str
    listingStatus: ListingStatusType

class DetailedGlossaryTermTypeDef(TypedDict):
    name: NotRequired[str]
    shortDescription: NotRequired[str]

AssetRevisionTypeDef = TypedDict(
    "AssetRevisionTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "domainId": NotRequired[str],
        "id": NotRequired[str],
        "revision": NotRequired[str],
    },
)

class AssetScopeTypeDef(TypedDict):
    assetId: str
    filterIds: List[str]
    status: str
    errorMessage: NotRequired[str]

class AssetTargetNameMapTypeDef(TypedDict):
    assetId: str
    targetName: str

class FormEntryOutputTypeDef(TypedDict):
    typeName: str
    typeRevision: str
    required: NotRequired[bool]

class AssetTypesForRuleOutputTypeDef(TypedDict):
    selectionMode: RuleScopeSelectionModeType
    specificAssetTypes: NotRequired[List[str]]

class AssetTypesForRuleTypeDef(TypedDict):
    selectionMode: RuleScopeSelectionModeType
    specificAssetTypes: NotRequired[Sequence[str]]

class AssociateEnvironmentRoleInputTypeDef(TypedDict):
    domainIdentifier: str
    environmentIdentifier: str
    environmentRoleArn: str

class AthenaPropertiesInputTypeDef(TypedDict):
    workgroupName: NotRequired[str]

class AthenaPropertiesOutputTypeDef(TypedDict):
    workgroupName: NotRequired[str]

class AthenaPropertiesPatchTypeDef(TypedDict):
    workgroupName: NotRequired[str]

class BasicAuthenticationCredentialsTypeDef(TypedDict):
    password: NotRequired[str]
    userName: NotRequired[str]

class AuthorizationCodePropertiesTypeDef(TypedDict):
    authorizationCode: NotRequired[str]
    redirectUri: NotRequired[str]

class AwsAccountTypeDef(TypedDict):
    awsAccountId: NotRequired[str]
    awsAccountIdPath: NotRequired[str]

class AwsLocationTypeDef(TypedDict):
    accessRole: NotRequired[str]
    awsAccountId: NotRequired[str]
    awsRegion: NotRequired[str]
    iamConnectionId: NotRequired[str]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class BusinessNameGenerationConfigurationTypeDef(TypedDict):
    enabled: NotRequired[bool]

class CancelMetadataGenerationRunInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class CancelSubscriptionInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class CloudFormationPropertiesTypeDef(TypedDict):
    templateUrl: str

class ConfigurableActionParameterTypeDef(TypedDict):
    key: NotRequired[str]
    value: NotRequired[str]

class ConnectionCredentialsTypeDef(TypedDict):
    accessKeyId: NotRequired[str]
    expiration: NotRequired[datetime]
    secretAccessKey: NotRequired[str]
    sessionToken: NotRequired[str]

class HyperPodPropertiesInputTypeDef(TypedDict):
    clusterName: str

class IamPropertiesInputTypeDef(TypedDict):
    glueLineageSyncEnabled: NotRequired[bool]

class SparkEmrPropertiesInputTypeDef(TypedDict):
    computeArn: NotRequired[str]
    instanceProfileArn: NotRequired[str]
    javaVirtualEnv: NotRequired[str]
    logUri: NotRequired[str]
    pythonVirtualEnv: NotRequired[str]
    runtimeRole: NotRequired[str]
    trustedCertificatesS3Uri: NotRequired[str]

class GluePropertiesOutputTypeDef(TypedDict):
    errorMessage: NotRequired[str]
    status: NotRequired[ConnectionStatusType]

class HyperPodPropertiesOutputTypeDef(TypedDict):
    clusterName: str
    clusterArn: NotRequired[str]
    orchestrator: NotRequired[HyperPodOrchestratorType]

class IamPropertiesOutputTypeDef(TypedDict):
    environmentId: NotRequired[str]
    glueLineageSyncEnabled: NotRequired[bool]

class IamPropertiesPatchTypeDef(TypedDict):
    glueLineageSyncEnabled: NotRequired[bool]

class SparkEmrPropertiesPatchTypeDef(TypedDict):
    computeArn: NotRequired[str]
    instanceProfileArn: NotRequired[str]
    javaVirtualEnv: NotRequired[str]
    logUri: NotRequired[str]
    pythonVirtualEnv: NotRequired[str]
    runtimeRole: NotRequired[str]
    trustedCertificatesS3Uri: NotRequired[str]

class FormInputTypeDef(TypedDict):
    formName: str
    content: NotRequired[str]
    typeIdentifier: NotRequired[str]
    typeRevision: NotRequired[str]

class FormEntryInputTypeDef(TypedDict):
    typeIdentifier: str
    typeRevision: str
    required: NotRequired[bool]

class CreateAssetTypePolicyGrantDetailTypeDef(TypedDict):
    includeChildDomainUnits: NotRequired[bool]

class DataProductItemOutputTypeDef(TypedDict):
    identifier: str
    itemType: Literal["ASSET"]
    glossaryTerms: NotRequired[List[str]]
    revision: NotRequired[str]

class RecommendationConfigurationTypeDef(TypedDict):
    enableBusinessNameGeneration: NotRequired[bool]

class ScheduleConfigurationTypeDef(TypedDict):
    schedule: NotRequired[str]
    timezone: NotRequired[TimezoneType]

class DataSourceErrorMessageTypeDef(TypedDict):
    errorType: DataSourceErrorTypeType
    errorDetail: NotRequired[str]

SingleSignOnTypeDef = TypedDict(
    "SingleSignOnTypeDef",
    {
        "idcInstanceArn": NotRequired[str],
        "type": NotRequired[AuthTypeType],
        "userAssignment": NotRequired[UserAssignmentType],
    },
)

class CreateDomainUnitInputTypeDef(TypedDict):
    domainIdentifier: str
    name: str
    parentDomainUnitIdentifier: str
    clientToken: NotRequired[str]
    description: NotRequired[str]

class CreateDomainUnitPolicyGrantDetailTypeDef(TypedDict):
    includeChildDomainUnits: NotRequired[bool]

class EnvironmentParameterTypeDef(TypedDict):
    name: NotRequired[str]
    value: NotRequired[str]

class CustomParameterTypeDef(TypedDict):
    fieldType: str
    keyName: str
    defaultValue: NotRequired[str]
    description: NotRequired[str]
    isEditable: NotRequired[bool]
    isOptional: NotRequired[bool]

class DeploymentPropertiesTypeDef(TypedDict):
    endTimeoutMinutes: NotRequired[int]
    startTimeoutMinutes: NotRequired[int]

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "type": str,
        "value": str,
        "name": NotRequired[str],
        "provider": NotRequired[str],
    },
)

class CreateEnvironmentProfilePolicyGrantDetailTypeDef(TypedDict):
    domainUnitId: NotRequired[str]

class ModelTypeDef(TypedDict):
    smithy: NotRequired[str]

class CreateFormTypePolicyGrantDetailTypeDef(TypedDict):
    includeChildDomainUnits: NotRequired[bool]

class CreateGlossaryInputTypeDef(TypedDict):
    domainIdentifier: str
    name: str
    owningProjectIdentifier: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    status: NotRequired[GlossaryStatusType]

class CreateGlossaryPolicyGrantDetailTypeDef(TypedDict):
    includeChildDomainUnits: NotRequired[bool]

class TermRelationsOutputTypeDef(TypedDict):
    classifies: NotRequired[List[str]]
    isA: NotRequired[List[str]]

class CreateGroupProfileInputTypeDef(TypedDict):
    domainIdentifier: str
    groupIdentifier: str
    clientToken: NotRequired[str]

class CreateListingChangeSetInputTypeDef(TypedDict):
    action: ChangeActionType
    domainIdentifier: str
    entityIdentifier: str
    entityType: EntityTypeType
    clientToken: NotRequired[str]
    entityRevision: NotRequired[str]

class CreateProjectFromProjectProfilePolicyGrantDetailOutputTypeDef(TypedDict):
    includeChildDomainUnits: NotRequired[bool]
    projectProfiles: NotRequired[List[str]]

class CreateProjectFromProjectProfilePolicyGrantDetailTypeDef(TypedDict):
    includeChildDomainUnits: NotRequired[bool]
    projectProfiles: NotRequired[Sequence[str]]

class MemberTypeDef(TypedDict):
    groupIdentifier: NotRequired[str]
    userIdentifier: NotRequired[str]

class ProjectDeletionErrorTypeDef(TypedDict):
    code: NotRequired[str]
    message: NotRequired[str]

class CreateProjectPolicyGrantDetailTypeDef(TypedDict):
    includeChildDomainUnits: NotRequired[bool]

class SubscribedListingInputTypeDef(TypedDict):
    identifier: str

class SubscriptionTargetFormTypeDef(TypedDict):
    content: str
    formName: str

class CreateUserProfileInputTypeDef(TypedDict):
    domainIdentifier: str
    userIdentifier: str
    clientToken: NotRequired[str]
    userType: NotRequired[UserTypeType]

class DataProductItemTypeDef(TypedDict):
    identifier: str
    itemType: Literal["ASSET"]
    glossaryTerms: NotRequired[Sequence[str]]
    revision: NotRequired[str]

class DataProductListingItemAdditionalAttributesTypeDef(TypedDict):
    forms: NotRequired[str]

DataProductResultItemTypeDef = TypedDict(
    "DataProductResultItemTypeDef",
    {
        "domainId": str,
        "id": str,
        "name": str,
        "owningProjectId": str,
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "description": NotRequired[str],
        "firstRevisionCreatedAt": NotRequired[datetime],
        "firstRevisionCreatedBy": NotRequired[str],
        "glossaryTerms": NotRequired[List[str]],
    },
)
DataProductRevisionTypeDef = TypedDict(
    "DataProductRevisionTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "domainId": NotRequired[str],
        "id": NotRequired[str],
        "revision": NotRequired[str],
    },
)

class SageMakerRunConfigurationInputTypeDef(TypedDict):
    trackingAssets: Mapping[str, Sequence[str]]

class SageMakerRunConfigurationOutputTypeDef(TypedDict):
    trackingAssets: Dict[str, List[str]]
    accountId: NotRequired[str]
    region: NotRequired[str]

class LineageInfoTypeDef(TypedDict):
    errorMessage: NotRequired[str]
    eventId: NotRequired[str]
    eventStatus: NotRequired[LineageEventProcessingStatusType]

class DataSourceRunLineageSummaryTypeDef(TypedDict):
    importStatus: NotRequired[LineageImportStatusType]

class RunStatisticsForAssetsTypeDef(TypedDict):
    added: NotRequired[int]
    failed: NotRequired[int]
    skipped: NotRequired[int]
    unchanged: NotRequired[int]
    updated: NotRequired[int]

class DeleteAssetFilterInputTypeDef(TypedDict):
    assetIdentifier: str
    domainIdentifier: str
    identifier: str

class DeleteAssetInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class DeleteAssetTypeInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class DeleteConnectionInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class DeleteDataProductInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class DeleteDataSourceInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    clientToken: NotRequired[str]
    retainPermissionsOnRevokeFailure: NotRequired[bool]

class DeleteDomainInputTypeDef(TypedDict):
    identifier: str
    clientToken: NotRequired[str]
    skipDeletionCheck: NotRequired[bool]

class DeleteDomainUnitInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class DeleteEnvironmentActionInputTypeDef(TypedDict):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str

class DeleteEnvironmentBlueprintConfigurationInputTypeDef(TypedDict):
    domainIdentifier: str
    environmentBlueprintIdentifier: str

class DeleteEnvironmentInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class DeleteEnvironmentProfileInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class DeleteFormTypeInputTypeDef(TypedDict):
    domainIdentifier: str
    formTypeIdentifier: str

class DeleteGlossaryInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class DeleteGlossaryTermInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class DeleteListingInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class DeleteProjectInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    skipDeletionCheck: NotRequired[bool]

class DeleteProjectProfileInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class DeleteRuleInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class DeleteSubscriptionGrantInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class DeleteSubscriptionRequestInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class DeleteSubscriptionTargetInputTypeDef(TypedDict):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str

class DeleteTimeSeriesDataPointsInputTypeDef(TypedDict):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    formName: str
    clientToken: NotRequired[str]

class EnvironmentErrorTypeDef(TypedDict):
    message: str
    code: NotRequired[str]

class DisassociateEnvironmentRoleInputTypeDef(TypedDict):
    domainIdentifier: str
    environmentIdentifier: str
    environmentRoleArn: str

DomainSummaryTypeDef = TypedDict(
    "DomainSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "id": str,
        "managedAccountId": str,
        "name": str,
        "status": DomainStatusType,
        "description": NotRequired[str],
        "domainVersion": NotRequired[DomainVersionType],
        "lastUpdatedAt": NotRequired[datetime],
        "portalUrl": NotRequired[str],
    },
)

class DomainUnitFilterForProjectTypeDef(TypedDict):
    domainUnit: str
    includeChildDomainUnits: NotRequired[bool]

class DomainUnitGrantFilterOutputTypeDef(TypedDict):
    allDomainUnitsGrantFilter: NotRequired[Dict[str, Any]]

class DomainUnitGrantFilterTypeDef(TypedDict):
    allDomainUnitsGrantFilter: NotRequired[Mapping[str, Any]]

class DomainUnitGroupPropertiesTypeDef(TypedDict):
    groupId: NotRequired[str]

class DomainUnitUserPropertiesTypeDef(TypedDict):
    userId: NotRequired[str]

DomainUnitSummaryTypeDef = TypedDict(
    "DomainUnitSummaryTypeDef",
    {
        "id": str,
        "name": str,
    },
)

class DomainUnitTargetTypeDef(TypedDict):
    domainUnitId: str
    includeChildDomainUnits: NotRequired[bool]

class RegionTypeDef(TypedDict):
    regionName: NotRequired[str]
    regionNamePath: NotRequired[str]

class EnvironmentConfigurationParameterTypeDef(TypedDict):
    isEditable: NotRequired[bool]
    name: NotRequired[str]
    value: NotRequired[str]

EnvironmentProfileSummaryTypeDef = TypedDict(
    "EnvironmentProfileSummaryTypeDef",
    {
        "createdBy": str,
        "domainId": str,
        "environmentBlueprintId": str,
        "id": str,
        "name": str,
        "awsAccountId": NotRequired[str],
        "awsAccountRegion": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "projectId": NotRequired[str],
        "updatedAt": NotRequired[datetime],
    },
)
EnvironmentSummaryTypeDef = TypedDict(
    "EnvironmentSummaryTypeDef",
    {
        "createdBy": str,
        "domainId": str,
        "name": str,
        "projectId": str,
        "provider": str,
        "awsAccountId": NotRequired[str],
        "awsAccountRegion": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "environmentConfigurationId": NotRequired[str],
        "environmentProfileId": NotRequired[str],
        "id": NotRequired[str],
        "status": NotRequired[EnvironmentStatusType],
        "updatedAt": NotRequired[datetime],
    },
)

class EqualToExpressionTypeDef(TypedDict):
    columnName: str
    value: str

class FailureCauseTypeDef(TypedDict):
    message: NotRequired[str]

class FilterTypeDef(TypedDict):
    attribute: str
    value: str

FilterExpressionTypeDef = TypedDict(
    "FilterExpressionTypeDef",
    {
        "expression": str,
        "type": FilterExpressionTypeType,
    },
)

class ImportTypeDef(TypedDict):
    name: str
    revision: str

class GetAssetFilterInputTypeDef(TypedDict):
    assetIdentifier: str
    domainIdentifier: str
    identifier: str

class GetAssetInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    revision: NotRequired[str]

class GetAssetTypeInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    revision: NotRequired[str]

class GetConnectionInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    withSecret: NotRequired[bool]

class GetDataProductInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    revision: NotRequired[str]

class GetDataSourceInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class GetDataSourceRunInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class GetDomainInputTypeDef(TypedDict):
    identifier: str

class GetDomainUnitInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class GetEnvironmentActionInputTypeDef(TypedDict):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str

class GetEnvironmentBlueprintConfigurationInputTypeDef(TypedDict):
    domainIdentifier: str
    environmentBlueprintIdentifier: str

class GetEnvironmentBlueprintInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class GetEnvironmentCredentialsInputTypeDef(TypedDict):
    domainIdentifier: str
    environmentIdentifier: str

class GetEnvironmentInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class GetEnvironmentProfileInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class GetFormTypeInputTypeDef(TypedDict):
    domainIdentifier: str
    formTypeIdentifier: str
    revision: NotRequired[str]

class GetGlossaryInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class GetGlossaryTermInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class GetGroupProfileInputTypeDef(TypedDict):
    domainIdentifier: str
    groupIdentifier: str

class GetIamPortalLoginUrlInputTypeDef(TypedDict):
    domainIdentifier: str

class GetJobRunInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class JobRunErrorTypeDef(TypedDict):
    message: str

class GetLineageEventInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

TimestampTypeDef = Union[datetime, str]
LineageNodeReferenceTypeDef = TypedDict(
    "LineageNodeReferenceTypeDef",
    {
        "eventTimestamp": NotRequired[datetime],
        "id": NotRequired[str],
    },
)

class GetListingInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    listingRevision: NotRequired[str]

class GetMetadataGenerationRunInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

MetadataGenerationRunTargetTypeDef = TypedDict(
    "MetadataGenerationRunTargetTypeDef",
    {
        "identifier": str,
        "type": Literal["ASSET"],
        "revision": NotRequired[str],
    },
)

class GetProjectInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class GetProjectProfileInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class GetRuleInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    revision: NotRequired[str]

class GetSubscriptionGrantInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class GetSubscriptionInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class GetSubscriptionRequestDetailsInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str

class GetSubscriptionTargetInputTypeDef(TypedDict):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str

class GetTimeSeriesDataPointInputTypeDef(TypedDict):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    formName: str
    identifier: str

TimeSeriesDataPointFormOutputTypeDef = TypedDict(
    "TimeSeriesDataPointFormOutputTypeDef",
    {
        "formName": str,
        "timestamp": datetime,
        "typeIdentifier": str,
        "content": NotRequired[str],
        "id": NotRequired[str],
        "typeRevision": NotRequired[str],
    },
)
GetUserProfileInputTypeDef = TypedDict(
    "GetUserProfileInputTypeDef",
    {
        "domainIdentifier": str,
        "userIdentifier": str,
        "type": NotRequired[UserProfileTypeType],
    },
)
GlossaryItemTypeDef = TypedDict(
    "GlossaryItemTypeDef",
    {
        "domainId": str,
        "id": str,
        "name": str,
        "owningProjectId": str,
        "status": GlossaryStatusType,
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "description": NotRequired[str],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
    },
)

class PhysicalConnectionRequirementsOutputTypeDef(TypedDict):
    availabilityZone: NotRequired[str]
    securityGroupIdList: NotRequired[List[str]]
    subnetId: NotRequired[str]
    subnetIdList: NotRequired[List[str]]

class GlueOAuth2CredentialsTypeDef(TypedDict):
    accessToken: NotRequired[str]
    jwtToken: NotRequired[str]
    refreshToken: NotRequired[str]
    userManagedClientApplicationClientSecret: NotRequired[str]

class SelfGrantStatusDetailTypeDef(TypedDict):
    databaseName: str
    status: SelfGrantStatusType
    failureCause: NotRequired[str]
    schemaName: NotRequired[str]

class ListingRevisionInputTypeDef(TypedDict):
    identifier: str
    revision: str

ListingRevisionTypeDef = TypedDict(
    "ListingRevisionTypeDef",
    {
        "id": str,
        "revision": str,
    },
)

class GreaterThanExpressionTypeDef(TypedDict):
    columnName: str
    value: str

class GreaterThanOrEqualToExpressionTypeDef(TypedDict):
    columnName: str
    value: str

class GroupDetailsTypeDef(TypedDict):
    groupId: str

class GroupPolicyGrantPrincipalTypeDef(TypedDict):
    groupIdentifier: NotRequired[str]

GroupProfileSummaryTypeDef = TypedDict(
    "GroupProfileSummaryTypeDef",
    {
        "domainId": NotRequired[str],
        "groupName": NotRequired[str],
        "id": NotRequired[str],
        "status": NotRequired[GroupProfileStatusType],
    },
)

class IamUserProfileDetailsTypeDef(TypedDict):
    arn: NotRequired[str]

class InExpressionOutputTypeDef(TypedDict):
    columnName: str
    values: List[str]

class InExpressionTypeDef(TypedDict):
    columnName: str
    values: Sequence[str]

class IsNotNullExpressionTypeDef(TypedDict):
    columnName: str

class IsNullExpressionTypeDef(TypedDict):
    columnName: str

class LakeFormationConfigurationOutputTypeDef(TypedDict):
    locationRegistrationExcludeS3Locations: NotRequired[List[str]]
    locationRegistrationRole: NotRequired[str]

class LakeFormationConfigurationTypeDef(TypedDict):
    locationRegistrationExcludeS3Locations: NotRequired[Sequence[str]]
    locationRegistrationRole: NotRequired[str]

class LessThanExpressionTypeDef(TypedDict):
    columnName: str
    value: str

class LessThanOrEqualToExpressionTypeDef(TypedDict):
    columnName: str
    value: str

class LikeExpressionTypeDef(TypedDict):
    columnName: str
    value: str

LineageNodeSummaryTypeDef = TypedDict(
    "LineageNodeSummaryTypeDef",
    {
        "domainId": str,
        "id": str,
        "typeName": str,
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "description": NotRequired[str],
        "eventTimestamp": NotRequired[datetime],
        "name": NotRequired[str],
        "sourceIdentifier": NotRequired[str],
        "typeRevision": NotRequired[str],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
    },
)

class LineageSqlQueryRunDetailsTypeDef(TypedDict):
    errorMessages: NotRequired[List[str]]
    numQueriesFailed: NotRequired[int]
    queryEndTime: NotRequired[datetime]
    queryStartTime: NotRequired[datetime]
    totalQueriesProcessed: NotRequired[int]

class LineageSyncScheduleTypeDef(TypedDict):
    schedule: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAssetFiltersInputTypeDef(TypedDict):
    assetIdentifier: str
    domainIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    status: NotRequired[FilterStatusType]

class ListAssetRevisionsInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

ListConnectionsInputTypeDef = TypedDict(
    "ListConnectionsInputTypeDef",
    {
        "domainIdentifier": str,
        "projectIdentifier": str,
        "environmentIdentifier": NotRequired[str],
        "maxResults": NotRequired[int],
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[Literal["NAME"]],
        "sortOrder": NotRequired[SortOrderType],
        "type": NotRequired[ConnectionTypeType],
    },
)

class ListDataProductRevisionsInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListDataSourceRunActivitiesInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    status: NotRequired[DataAssetActivityStatusType]

class ListDataSourceRunsInputTypeDef(TypedDict):
    dataSourceIdentifier: str
    domainIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    status: NotRequired[DataSourceRunStatusType]

ListDataSourcesInputTypeDef = TypedDict(
    "ListDataSourcesInputTypeDef",
    {
        "domainIdentifier": str,
        "projectIdentifier": str,
        "connectionIdentifier": NotRequired[str],
        "environmentIdentifier": NotRequired[str],
        "maxResults": NotRequired[int],
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
        "status": NotRequired[DataSourceStatusType],
        "type": NotRequired[str],
    },
)

class ListDomainUnitsForParentInputTypeDef(TypedDict):
    domainIdentifier: str
    parentDomainUnitIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListDomainsInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    status: NotRequired[DomainStatusType]

class ListEntityOwnersInputTypeDef(TypedDict):
    domainIdentifier: str
    entityIdentifier: str
    entityType: Literal["DOMAIN_UNIT"]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListEnvironmentActionsInputTypeDef(TypedDict):
    domainIdentifier: str
    environmentIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListEnvironmentBlueprintConfigurationsInputTypeDef(TypedDict):
    domainIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListEnvironmentBlueprintsInputTypeDef(TypedDict):
    domainIdentifier: str
    managed: NotRequired[bool]
    maxResults: NotRequired[int]
    name: NotRequired[str]
    nextToken: NotRequired[str]

class ListEnvironmentProfilesInputTypeDef(TypedDict):
    domainIdentifier: str
    awsAccountId: NotRequired[str]
    awsAccountRegion: NotRequired[str]
    environmentBlueprintIdentifier: NotRequired[str]
    maxResults: NotRequired[int]
    name: NotRequired[str]
    nextToken: NotRequired[str]
    projectIdentifier: NotRequired[str]

class ListEnvironmentsInputTypeDef(TypedDict):
    domainIdentifier: str
    projectIdentifier: str
    awsAccountId: NotRequired[str]
    awsAccountRegion: NotRequired[str]
    environmentBlueprintIdentifier: NotRequired[str]
    environmentProfileIdentifier: NotRequired[str]
    maxResults: NotRequired[int]
    name: NotRequired[str]
    nextToken: NotRequired[str]
    provider: NotRequired[str]
    status: NotRequired[EnvironmentStatusType]

class ListJobRunsInputTypeDef(TypedDict):
    domainIdentifier: str
    jobIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    sortOrder: NotRequired[SortOrderType]
    status: NotRequired[JobRunStatusType]

ListMetadataGenerationRunsInputTypeDef = TypedDict(
    "ListMetadataGenerationRunsInputTypeDef",
    {
        "domainIdentifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "status": NotRequired[MetadataGenerationRunStatusType],
        "type": NotRequired[Literal["BUSINESS_DESCRIPTIONS"]],
    },
)

class ListPolicyGrantsInputTypeDef(TypedDict):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TargetEntityTypeType
    policyType: ManagedPolicyTypeType
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListProjectMembershipsInputTypeDef(TypedDict):
    domainIdentifier: str
    projectIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    sortBy: NotRequired[Literal["NAME"]]
    sortOrder: NotRequired[SortOrderType]

class ListProjectProfilesInputTypeDef(TypedDict):
    domainIdentifier: str
    maxResults: NotRequired[int]
    name: NotRequired[str]
    nextToken: NotRequired[str]
    sortBy: NotRequired[Literal["NAME"]]
    sortOrder: NotRequired[SortOrderType]

ProjectProfileSummaryTypeDef = TypedDict(
    "ProjectProfileSummaryTypeDef",
    {
        "createdBy": str,
        "domainId": str,
        "id": str,
        "name": str,
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "domainUnitId": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "status": NotRequired[StatusType],
    },
)

class ListProjectsInputTypeDef(TypedDict):
    domainIdentifier: str
    groupIdentifier: NotRequired[str]
    maxResults: NotRequired[int]
    name: NotRequired[str]
    nextToken: NotRequired[str]
    userIdentifier: NotRequired[str]

class ListRulesInputTypeDef(TypedDict):
    domainIdentifier: str
    targetIdentifier: str
    targetType: Literal["DOMAIN_UNIT"]
    action: NotRequired[RuleActionType]
    assetTypes: NotRequired[Sequence[str]]
    dataProduct: NotRequired[bool]
    includeCascaded: NotRequired[bool]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    projectIds: NotRequired[Sequence[str]]
    ruleType: NotRequired[Literal["METADATA_FORM_ENFORCEMENT"]]

class ListSubscriptionGrantsInputTypeDef(TypedDict):
    domainIdentifier: str
    environmentId: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    owningProjectId: NotRequired[str]
    sortBy: NotRequired[SortKeyType]
    sortOrder: NotRequired[SortOrderType]
    subscribedListingId: NotRequired[str]
    subscriptionId: NotRequired[str]
    subscriptionTargetId: NotRequired[str]

class ListSubscriptionRequestsInputTypeDef(TypedDict):
    domainIdentifier: str
    approverProjectId: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    owningProjectId: NotRequired[str]
    sortBy: NotRequired[SortKeyType]
    sortOrder: NotRequired[SortOrderType]
    status: NotRequired[SubscriptionRequestStatusType]
    subscribedListingId: NotRequired[str]

class ListSubscriptionTargetsInputTypeDef(TypedDict):
    domainIdentifier: str
    environmentIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    sortBy: NotRequired[SortKeyType]
    sortOrder: NotRequired[SortOrderType]

class ListSubscriptionsInputTypeDef(TypedDict):
    domainIdentifier: str
    approverProjectId: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    owningProjectId: NotRequired[str]
    sortBy: NotRequired[SortKeyType]
    sortOrder: NotRequired[SortOrderType]
    status: NotRequired[SubscriptionStatusType]
    subscribedListingId: NotRequired[str]
    subscriptionRequestIdentifier: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class UserDetailsTypeDef(TypedDict):
    userId: str

class MetadataFormReferenceTypeDef(TypedDict):
    typeIdentifier: str
    typeRevision: str

class MetadataFormSummaryTypeDef(TypedDict):
    typeName: str
    typeRevision: str
    formName: NotRequired[str]

class NameIdentifierTypeDef(TypedDict):
    name: NotRequired[str]
    namespace: NotRequired[str]

class NotEqualToExpressionTypeDef(TypedDict):
    columnName: str
    value: str

class NotInExpressionOutputTypeDef(TypedDict):
    columnName: str
    values: List[str]

class NotInExpressionTypeDef(TypedDict):
    columnName: str
    values: Sequence[str]

class NotLikeExpressionTypeDef(TypedDict):
    columnName: str
    value: str

NotificationResourceTypeDef = TypedDict(
    "NotificationResourceTypeDef",
    {
        "id": str,
        "type": Literal["PROJECT"],
        "name": NotRequired[str],
    },
)

class OAuth2ClientApplicationTypeDef(TypedDict):
    aWSManagedClientApplicationReference: NotRequired[str]
    userManagedClientApplicationClientId: NotRequired[str]

class OverrideDomainUnitOwnersPolicyGrantDetailTypeDef(TypedDict):
    includeChildDomainUnits: NotRequired[bool]

class OverrideProjectOwnersPolicyGrantDetailTypeDef(TypedDict):
    includeChildDomainUnits: NotRequired[bool]

class OwnerGroupPropertiesOutputTypeDef(TypedDict):
    groupId: NotRequired[str]

class OwnerGroupPropertiesTypeDef(TypedDict):
    groupIdentifier: str

class OwnerUserPropertiesOutputTypeDef(TypedDict):
    userId: NotRequired[str]

class OwnerUserPropertiesTypeDef(TypedDict):
    userIdentifier: str

class PhysicalConnectionRequirementsTypeDef(TypedDict):
    availabilityZone: NotRequired[str]
    securityGroupIdList: NotRequired[Sequence[str]]
    subnetId: NotRequired[str]
    subnetIdList: NotRequired[Sequence[str]]

class UseAssetTypePolicyGrantDetailTypeDef(TypedDict):
    domainUnitId: NotRequired[str]

class UserPolicyGrantPrincipalOutputTypeDef(TypedDict):
    allUsersGrantFilter: NotRequired[Dict[str, Any]]
    userIdentifier: NotRequired[str]

class UserPolicyGrantPrincipalTypeDef(TypedDict):
    allUsersGrantFilter: NotRequired[Mapping[str, Any]]
    userIdentifier: NotRequired[str]

class ProjectsForRuleOutputTypeDef(TypedDict):
    selectionMode: RuleScopeSelectionModeType
    specificProjects: NotRequired[List[str]]

class ProjectsForRuleTypeDef(TypedDict):
    selectionMode: RuleScopeSelectionModeType
    specificProjects: NotRequired[Sequence[str]]

class RedshiftClusterStorageTypeDef(TypedDict):
    clusterName: str

class RedshiftCredentialConfigurationTypeDef(TypedDict):
    secretManagerArn: str

class UsernamePasswordTypeDef(TypedDict):
    password: str
    username: str

class RedshiftStoragePropertiesTypeDef(TypedDict):
    clusterName: NotRequired[str]
    workgroupName: NotRequired[str]

class RedshiftServerlessStorageTypeDef(TypedDict):
    workgroupName: str

class RejectChoiceTypeDef(TypedDict):
    predictionTarget: str
    predictionChoices: NotRequired[Sequence[int]]

class RejectRuleTypeDef(TypedDict):
    rule: NotRequired[RejectRuleBehaviorType]
    threshold: NotRequired[float]

class RejectSubscriptionRequestInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    decisionComment: NotRequired[str]

class RevokeSubscriptionInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    retainPermissions: NotRequired[bool]

class SearchGroupProfilesInputTypeDef(TypedDict):
    domainIdentifier: str
    groupType: GroupSearchTypeType
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    searchText: NotRequired[str]

class SearchInItemTypeDef(TypedDict):
    attribute: str

class SearchSortTypeDef(TypedDict):
    attribute: str
    order: NotRequired[SortOrderType]

class SearchUserProfilesInputTypeDef(TypedDict):
    domainIdentifier: str
    userType: UserSearchTypeType
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    searchText: NotRequired[str]

class SparkGlueArgsTypeDef(TypedDict):
    connection: NotRequired[str]

class SsoUserProfileDetailsTypeDef(TypedDict):
    firstName: NotRequired[str]
    lastName: NotRequired[str]
    username: NotRequired[str]

class StartDataSourceRunInputTypeDef(TypedDict):
    dataSourceIdentifier: str
    domainIdentifier: str
    clientToken: NotRequired[str]

class SubscribedProjectInputTypeDef(TypedDict):
    identifier: NotRequired[str]

SubscribedProjectTypeDef = TypedDict(
    "SubscribedProjectTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
    },
)

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class TermRelationsTypeDef(TypedDict):
    classifies: NotRequired[Sequence[str]]
    isA: NotRequired[Sequence[str]]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateDomainUnitInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    description: NotRequired[str]
    name: NotRequired[str]

class UpdateGlossaryInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    name: NotRequired[str]
    status: NotRequired[GlossaryStatusType]

class UpdateGroupProfileInputTypeDef(TypedDict):
    domainIdentifier: str
    groupIdentifier: str
    status: GroupProfileStatusType

class UpdateSubscriptionRequestInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    requestReason: str

UpdateUserProfileInputTypeDef = TypedDict(
    "UpdateUserProfileInputTypeDef",
    {
        "domainIdentifier": str,
        "status": UserProfileStatusType,
        "userIdentifier": str,
        "type": NotRequired[UserProfileTypeType],
    },
)

class AcceptPredictionsInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    acceptChoices: NotRequired[Sequence[AcceptChoiceTypeDef]]
    acceptRule: NotRequired[AcceptRuleTypeDef]
    clientToken: NotRequired[str]
    revision: NotRequired[str]

class AcceptPredictionsOutputTypeDef(TypedDict):
    assetId: str
    domainId: str
    revision: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFormTypeOutputTypeDef(TypedDict):
    description: str
    domainId: str
    name: str
    originDomainId: str
    originProjectId: str
    owningProjectId: str
    revision: str
    ResponseMetadata: ResponseMetadataTypeDef

CreateGlossaryOutputTypeDef = TypedDict(
    "CreateGlossaryOutputTypeDef",
    {
        "description": str,
        "domainId": str,
        "id": str,
        "name": str,
        "owningProjectId": str,
        "status": GlossaryStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGroupProfileOutputTypeDef = TypedDict(
    "CreateGroupProfileOutputTypeDef",
    {
        "domainId": str,
        "groupName": str,
        "id": str,
        "status": GroupProfileStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateListingChangeSetOutputTypeDef(TypedDict):
    listingId: str
    listingRevision: str
    status: ListingStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteConnectionOutputTypeDef(TypedDict):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDomainOutputTypeDef(TypedDict):
    status: DomainStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnvironmentCredentialsOutputTypeDef(TypedDict):
    accessKeyId: str
    expiration: datetime
    secretAccessKey: str
    sessionToken: str
    ResponseMetadata: ResponseMetadataTypeDef

GetGlossaryOutputTypeDef = TypedDict(
    "GetGlossaryOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "id": str,
        "name": str,
        "owningProjectId": str,
        "status": GlossaryStatusType,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGroupProfileOutputTypeDef = TypedDict(
    "GetGroupProfileOutputTypeDef",
    {
        "domainId": str,
        "groupName": str,
        "id": str,
        "status": GroupProfileStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetIamPortalLoginUrlOutputTypeDef(TypedDict):
    authCodeUrl: str
    userProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef

GetLineageEventOutputTypeDef = TypedDict(
    "GetLineageEventOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "event": StreamingBody,
        "eventTime": datetime,
        "id": str,
        "processingStatus": LineageEventProcessingStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

PostLineageEventOutputTypeDef = TypedDict(
    "PostLineageEventOutputTypeDef",
    {
        "domainId": str,
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class RejectPredictionsOutputTypeDef(TypedDict):
    assetId: str
    assetRevision: str
    domainId: str
    ResponseMetadata: ResponseMetadataTypeDef

StartMetadataGenerationRunOutputTypeDef = TypedDict(
    "StartMetadataGenerationRunOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "id": str,
        "owningProjectId": str,
        "status": MetadataGenerationRunStatusType,
        "type": Literal["BUSINESS_DESCRIPTIONS"],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGlossaryOutputTypeDef = TypedDict(
    "UpdateGlossaryOutputTypeDef",
    {
        "description": str,
        "domainId": str,
        "id": str,
        "name": str,
        "owningProjectId": str,
        "status": GlossaryStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGroupProfileOutputTypeDef = TypedDict(
    "UpdateGroupProfileOutputTypeDef",
    {
        "domainId": str,
        "groupName": str,
        "id": str,
        "status": GroupProfileStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class AcceptSubscriptionRequestInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    assetScopes: NotRequired[Sequence[AcceptedAssetScopeTypeDef]]
    decisionComment: NotRequired[str]

class ActionParametersTypeDef(TypedDict):
    awsConsoleLink: NotRequired[AwsConsoleLinkParametersTypeDef]

class ListAssetFiltersOutputTypeDef(TypedDict):
    items: List[AssetFilterSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class AssetItemAdditionalAttributesTypeDef(TypedDict):
    formsOutput: NotRequired[List[FormOutputTypeDef]]
    latestTimeSeriesDataPointFormsOutput: NotRequired[
        List[TimeSeriesDataPointSummaryFormOutputTypeDef]
    ]
    readOnlyFormsOutput: NotRequired[List[FormOutputTypeDef]]

class AssetListingItemAdditionalAttributesTypeDef(TypedDict):
    forms: NotRequired[str]
    latestTimeSeriesDataPointForms: NotRequired[List[TimeSeriesDataPointSummaryFormOutputTypeDef]]

class ListTimeSeriesDataPointsOutputTypeDef(TypedDict):
    items: List[TimeSeriesDataPointSummaryFormOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

GetAssetOutputTypeDef = TypedDict(
    "GetAssetOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "externalIdentifier": str,
        "firstRevisionCreatedAt": datetime,
        "firstRevisionCreatedBy": str,
        "formsOutput": List[FormOutputTypeDef],
        "glossaryTerms": List[str],
        "id": str,
        "latestTimeSeriesDataPointFormsOutput": List[TimeSeriesDataPointSummaryFormOutputTypeDef],
        "listing": AssetListingDetailsTypeDef,
        "name": str,
        "owningProjectId": str,
        "readOnlyFormsOutput": List[FormOutputTypeDef],
        "revision": str,
        "typeIdentifier": str,
        "typeRevision": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class AssetListingTypeDef(TypedDict):
    assetId: NotRequired[str]
    assetRevision: NotRequired[str]
    assetType: NotRequired[str]
    createdAt: NotRequired[datetime]
    forms: NotRequired[str]
    glossaryTerms: NotRequired[List[DetailedGlossaryTermTypeDef]]
    latestTimeSeriesDataPointForms: NotRequired[List[TimeSeriesDataPointSummaryFormOutputTypeDef]]
    owningProjectId: NotRequired[str]

class ListingSummaryItemTypeDef(TypedDict):
    glossaryTerms: NotRequired[List[DetailedGlossaryTermTypeDef]]
    listingId: NotRequired[str]
    listingRevision: NotRequired[str]

class ListingSummaryTypeDef(TypedDict):
    glossaryTerms: NotRequired[List[DetailedGlossaryTermTypeDef]]
    listingId: NotRequired[str]
    listingRevision: NotRequired[str]

class SubscribedProductListingTypeDef(TypedDict):
    assetListings: NotRequired[List[AssetInDataProductListingItemTypeDef]]
    description: NotRequired[str]
    entityId: NotRequired[str]
    entityRevision: NotRequired[str]
    glossaryTerms: NotRequired[List[DetailedGlossaryTermTypeDef]]
    name: NotRequired[str]

class ListAssetRevisionsOutputTypeDef(TypedDict):
    items: List[AssetRevisionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SubscribedAssetListingTypeDef(TypedDict):
    assetScope: NotRequired[AssetScopeTypeDef]
    entityId: NotRequired[str]
    entityRevision: NotRequired[str]
    entityType: NotRequired[str]
    forms: NotRequired[str]
    glossaryTerms: NotRequired[List[DetailedGlossaryTermTypeDef]]

class AssetTypeItemTypeDef(TypedDict):
    domainId: str
    formsOutput: Dict[str, FormEntryOutputTypeDef]
    name: str
    owningProjectId: str
    revision: str
    createdAt: NotRequired[datetime]
    createdBy: NotRequired[str]
    description: NotRequired[str]
    originDomainId: NotRequired[str]
    originProjectId: NotRequired[str]
    updatedAt: NotRequired[datetime]
    updatedBy: NotRequired[str]

class CreateAssetTypeOutputTypeDef(TypedDict):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    formsOutput: Dict[str, FormEntryOutputTypeDef]
    name: str
    originDomainId: str
    originProjectId: str
    owningProjectId: str
    revision: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssetTypeOutputTypeDef(TypedDict):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    formsOutput: Dict[str, FormEntryOutputTypeDef]
    name: str
    originDomainId: str
    originProjectId: str
    owningProjectId: str
    revision: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class LineageNodeTypeItemTypeDef(TypedDict):
    domainId: str
    formsOutput: Dict[str, FormEntryOutputTypeDef]
    revision: str
    createdAt: NotRequired[datetime]
    createdBy: NotRequired[str]
    description: NotRequired[str]
    name: NotRequired[str]
    updatedAt: NotRequired[datetime]
    updatedBy: NotRequired[str]

class AuthenticationConfigurationPatchTypeDef(TypedDict):
    basicAuthenticationCredentials: NotRequired[BasicAuthenticationCredentialsTypeDef]
    secretArn: NotRequired[str]

class PostLineageEventInputTypeDef(TypedDict):
    domainIdentifier: str
    event: BlobTypeDef
    clientToken: NotRequired[str]

class PredictionConfigurationTypeDef(TypedDict):
    businessNameGeneration: NotRequired[BusinessNameGenerationConfigurationTypeDef]

class ProvisioningPropertiesTypeDef(TypedDict):
    cloudFormation: NotRequired[CloudFormationPropertiesTypeDef]

ConfigurableEnvironmentActionTypeDef = TypedDict(
    "ConfigurableEnvironmentActionTypeDef",
    {
        "parameters": List[ConfigurableActionParameterTypeDef],
        "type": str,
        "auth": NotRequired[ConfigurableActionTypeAuthorizationType],
    },
)

class CreateAssetTypeInputTypeDef(TypedDict):
    domainIdentifier: str
    formsInput: Mapping[str, FormEntryInputTypeDef]
    name: str
    owningProjectIdentifier: str
    description: NotRequired[str]

CreateDataProductOutputTypeDef = TypedDict(
    "CreateDataProductOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "firstRevisionCreatedAt": datetime,
        "firstRevisionCreatedBy": str,
        "formsOutput": List[FormOutputTypeDef],
        "glossaryTerms": List[str],
        "id": str,
        "items": List[DataProductItemOutputTypeDef],
        "name": str,
        "owningProjectId": str,
        "revision": str,
        "status": DataProductStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDataProductRevisionOutputTypeDef = TypedDict(
    "CreateDataProductRevisionOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "firstRevisionCreatedAt": datetime,
        "firstRevisionCreatedBy": str,
        "formsOutput": List[FormOutputTypeDef],
        "glossaryTerms": List[str],
        "id": str,
        "items": List[DataProductItemOutputTypeDef],
        "name": str,
        "owningProjectId": str,
        "revision": str,
        "status": DataProductStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDataProductOutputTypeDef = TypedDict(
    "GetDataProductOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "firstRevisionCreatedAt": datetime,
        "firstRevisionCreatedBy": str,
        "formsOutput": List[FormOutputTypeDef],
        "glossaryTerms": List[str],
        "id": str,
        "items": List[DataProductItemOutputTypeDef],
        "name": str,
        "owningProjectId": str,
        "revision": str,
        "status": DataProductStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataSourceSummaryTypeDef = TypedDict(
    "DataSourceSummaryTypeDef",
    {
        "dataSourceId": str,
        "domainId": str,
        "name": str,
        "status": DataSourceStatusType,
        "type": str,
        "connectionId": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "enableSetting": NotRequired[EnableSettingType],
        "environmentId": NotRequired[str],
        "lastRunAssetCount": NotRequired[int],
        "lastRunAt": NotRequired[datetime],
        "lastRunErrorMessage": NotRequired[DataSourceErrorMessageTypeDef],
        "lastRunStatus": NotRequired[DataSourceRunStatusType],
        "schedule": NotRequired[ScheduleConfigurationTypeDef],
        "updatedAt": NotRequired[datetime],
    },
)

class CreateDomainInputTypeDef(TypedDict):
    domainExecutionRole: str
    name: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    domainVersion: NotRequired[DomainVersionType]
    kmsKeyIdentifier: NotRequired[str]
    serviceRole: NotRequired[str]
    singleSignOn: NotRequired[SingleSignOnTypeDef]
    tags: NotRequired[Mapping[str, str]]

CreateDomainOutputTypeDef = TypedDict(
    "CreateDomainOutputTypeDef",
    {
        "arn": str,
        "description": str,
        "domainExecutionRole": str,
        "domainVersion": DomainVersionType,
        "id": str,
        "kmsKeyIdentifier": str,
        "name": str,
        "portalUrl": str,
        "rootDomainUnitId": str,
        "serviceRole": str,
        "singleSignOn": SingleSignOnTypeDef,
        "status": DomainStatusType,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDomainOutputTypeDef = TypedDict(
    "GetDomainOutputTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "description": str,
        "domainExecutionRole": str,
        "domainVersion": DomainVersionType,
        "id": str,
        "kmsKeyIdentifier": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "portalUrl": str,
        "rootDomainUnitId": str,
        "serviceRole": str,
        "singleSignOn": SingleSignOnTypeDef,
        "status": DomainStatusType,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class UpdateDomainInputTypeDef(TypedDict):
    identifier: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    domainExecutionRole: NotRequired[str]
    name: NotRequired[str]
    serviceRole: NotRequired[str]
    singleSignOn: NotRequired[SingleSignOnTypeDef]

UpdateDomainOutputTypeDef = TypedDict(
    "UpdateDomainOutputTypeDef",
    {
        "description": str,
        "domainExecutionRole": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "rootDomainUnitId": str,
        "serviceRole": str,
        "singleSignOn": SingleSignOnTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateEnvironmentInputTypeDef(TypedDict):
    domainIdentifier: str
    environmentProfileIdentifier: str
    name: str
    projectIdentifier: str
    deploymentOrder: NotRequired[int]
    description: NotRequired[str]
    environmentAccountIdentifier: NotRequired[str]
    environmentAccountRegion: NotRequired[str]
    environmentBlueprintIdentifier: NotRequired[str]
    environmentConfigurationId: NotRequired[str]
    glossaryTerms: NotRequired[Sequence[str]]
    userParameters: NotRequired[Sequence[EnvironmentParameterTypeDef]]

class CreateEnvironmentProfileInputTypeDef(TypedDict):
    domainIdentifier: str
    environmentBlueprintIdentifier: str
    name: str
    projectIdentifier: str
    awsAccountId: NotRequired[str]
    awsAccountRegion: NotRequired[str]
    description: NotRequired[str]
    userParameters: NotRequired[Sequence[EnvironmentParameterTypeDef]]

class EnvironmentConfigurationUserParameterOutputTypeDef(TypedDict):
    environmentConfigurationName: NotRequired[str]
    environmentId: NotRequired[str]
    environmentParameters: NotRequired[List[EnvironmentParameterTypeDef]]

class EnvironmentConfigurationUserParameterTypeDef(TypedDict):
    environmentConfigurationName: NotRequired[str]
    environmentId: NotRequired[str]
    environmentParameters: NotRequired[Sequence[EnvironmentParameterTypeDef]]

class UpdateEnvironmentInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    blueprintVersion: NotRequired[str]
    description: NotRequired[str]
    glossaryTerms: NotRequired[Sequence[str]]
    name: NotRequired[str]
    userParameters: NotRequired[Sequence[EnvironmentParameterTypeDef]]

class UpdateEnvironmentProfileInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    awsAccountId: NotRequired[str]
    awsAccountRegion: NotRequired[str]
    description: NotRequired[str]
    name: NotRequired[str]
    userParameters: NotRequired[Sequence[EnvironmentParameterTypeDef]]

CreateEnvironmentProfileOutputTypeDef = TypedDict(
    "CreateEnvironmentProfileOutputTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "environmentBlueprintId": str,
        "id": str,
        "name": str,
        "projectId": str,
        "updatedAt": datetime,
        "userParameters": List[CustomParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEnvironmentProfileOutputTypeDef = TypedDict(
    "GetEnvironmentProfileOutputTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "environmentBlueprintId": str,
        "id": str,
        "name": str,
        "projectId": str,
        "updatedAt": datetime,
        "userParameters": List[CustomParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEnvironmentProfileOutputTypeDef = TypedDict(
    "UpdateEnvironmentProfileOutputTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "environmentBlueprintId": str,
        "id": str,
        "name": str,
        "projectId": str,
        "updatedAt": datetime,
        "userParameters": List[CustomParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateFormTypeInputTypeDef(TypedDict):
    domainIdentifier: str
    model: ModelTypeDef
    name: str
    owningProjectIdentifier: str
    description: NotRequired[str]
    status: NotRequired[FormTypeStatusType]

CreateGlossaryTermOutputTypeDef = TypedDict(
    "CreateGlossaryTermOutputTypeDef",
    {
        "domainId": str,
        "glossaryId": str,
        "id": str,
        "longDescription": str,
        "name": str,
        "shortDescription": str,
        "status": GlossaryTermStatusType,
        "termRelations": TermRelationsOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGlossaryTermOutputTypeDef = TypedDict(
    "GetGlossaryTermOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "glossaryId": str,
        "id": str,
        "longDescription": str,
        "name": str,
        "shortDescription": str,
        "status": GlossaryTermStatusType,
        "termRelations": TermRelationsOutputTypeDef,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GlossaryTermItemTypeDef = TypedDict(
    "GlossaryTermItemTypeDef",
    {
        "domainId": str,
        "glossaryId": str,
        "id": str,
        "name": str,
        "status": GlossaryTermStatusType,
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "longDescription": NotRequired[str],
        "shortDescription": NotRequired[str],
        "termRelations": NotRequired[TermRelationsOutputTypeDef],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
    },
)
UpdateGlossaryTermOutputTypeDef = TypedDict(
    "UpdateGlossaryTermOutputTypeDef",
    {
        "domainId": str,
        "glossaryId": str,
        "id": str,
        "longDescription": str,
        "name": str,
        "shortDescription": str,
        "status": GlossaryTermStatusType,
        "termRelations": TermRelationsOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateProjectMembershipInputTypeDef(TypedDict):
    designation: UserDesignationType
    domainIdentifier: str
    member: MemberTypeDef
    projectIdentifier: str

class DeleteProjectMembershipInputTypeDef(TypedDict):
    domainIdentifier: str
    member: MemberTypeDef
    projectIdentifier: str

ProjectSummaryTypeDef = TypedDict(
    "ProjectSummaryTypeDef",
    {
        "createdBy": str,
        "domainId": str,
        "id": str,
        "name": str,
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "domainUnitId": NotRequired[str],
        "failureReasons": NotRequired[List[ProjectDeletionErrorTypeDef]],
        "projectStatus": NotRequired[ProjectStatusType],
        "updatedAt": NotRequired[datetime],
    },
)
CreateSubscriptionTargetInputTypeDef = TypedDict(
    "CreateSubscriptionTargetInputTypeDef",
    {
        "applicableAssetTypes": Sequence[str],
        "authorizedPrincipals": Sequence[str],
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "manageAccessRole": str,
        "name": str,
        "subscriptionTargetConfig": Sequence[SubscriptionTargetFormTypeDef],
        "type": str,
        "clientToken": NotRequired[str],
        "provider": NotRequired[str],
    },
)
CreateSubscriptionTargetOutputTypeDef = TypedDict(
    "CreateSubscriptionTargetOutputTypeDef",
    {
        "applicableAssetTypes": List[str],
        "authorizedPrincipals": List[str],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "environmentId": str,
        "id": str,
        "manageAccessRole": str,
        "name": str,
        "projectId": str,
        "provider": str,
        "subscriptionTargetConfig": List[SubscriptionTargetFormTypeDef],
        "type": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSubscriptionTargetOutputTypeDef = TypedDict(
    "GetSubscriptionTargetOutputTypeDef",
    {
        "applicableAssetTypes": List[str],
        "authorizedPrincipals": List[str],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "environmentId": str,
        "id": str,
        "manageAccessRole": str,
        "name": str,
        "projectId": str,
        "provider": str,
        "subscriptionTargetConfig": List[SubscriptionTargetFormTypeDef],
        "type": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubscriptionTargetSummaryTypeDef = TypedDict(
    "SubscriptionTargetSummaryTypeDef",
    {
        "applicableAssetTypes": List[str],
        "authorizedPrincipals": List[str],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "environmentId": str,
        "id": str,
        "name": str,
        "projectId": str,
        "provider": str,
        "subscriptionTargetConfig": List[SubscriptionTargetFormTypeDef],
        "type": str,
        "manageAccessRole": NotRequired[str],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
    },
)

class UpdateSubscriptionTargetInputTypeDef(TypedDict):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str
    applicableAssetTypes: NotRequired[Sequence[str]]
    authorizedPrincipals: NotRequired[Sequence[str]]
    manageAccessRole: NotRequired[str]
    name: NotRequired[str]
    provider: NotRequired[str]
    subscriptionTargetConfig: NotRequired[Sequence[SubscriptionTargetFormTypeDef]]

UpdateSubscriptionTargetOutputTypeDef = TypedDict(
    "UpdateSubscriptionTargetOutputTypeDef",
    {
        "applicableAssetTypes": List[str],
        "authorizedPrincipals": List[str],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "environmentId": str,
        "id": str,
        "manageAccessRole": str,
        "name": str,
        "projectId": str,
        "provider": str,
        "subscriptionTargetConfig": List[SubscriptionTargetFormTypeDef],
        "type": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataProductItemUnionTypeDef = Union[DataProductItemTypeDef, DataProductItemOutputTypeDef]

class ListDataProductRevisionsOutputTypeDef(TypedDict):
    items: List[DataProductRevisionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DataSourceRunActivityTypeDef(TypedDict):
    createdAt: datetime
    dataAssetStatus: DataAssetActivityStatusType
    dataSourceRunId: str
    database: str
    projectId: str
    technicalName: str
    updatedAt: datetime
    dataAssetId: NotRequired[str]
    errorMessage: NotRequired[DataSourceErrorMessageTypeDef]
    lineageSummary: NotRequired[LineageInfoTypeDef]
    technicalDescription: NotRequired[str]

DataSourceRunSummaryTypeDef = TypedDict(
    "DataSourceRunSummaryTypeDef",
    {
        "createdAt": datetime,
        "dataSourceId": str,
        "id": str,
        "projectId": str,
        "status": DataSourceRunStatusType,
        "type": DataSourceRunTypeType,
        "updatedAt": datetime,
        "errorMessage": NotRequired[DataSourceErrorMessageTypeDef],
        "lineageSummary": NotRequired[DataSourceRunLineageSummaryTypeDef],
        "runStatisticsForAssets": NotRequired[RunStatisticsForAssetsTypeDef],
        "startedAt": NotRequired[datetime],
        "stoppedAt": NotRequired[datetime],
    },
)
GetDataSourceRunOutputTypeDef = TypedDict(
    "GetDataSourceRunOutputTypeDef",
    {
        "createdAt": datetime,
        "dataSourceConfigurationSnapshot": str,
        "dataSourceId": str,
        "domainId": str,
        "errorMessage": DataSourceErrorMessageTypeDef,
        "id": str,
        "lineageSummary": DataSourceRunLineageSummaryTypeDef,
        "projectId": str,
        "runStatisticsForAssets": RunStatisticsForAssetsTypeDef,
        "startedAt": datetime,
        "status": DataSourceRunStatusType,
        "stoppedAt": datetime,
        "type": DataSourceRunTypeType,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDataSourceRunOutputTypeDef = TypedDict(
    "StartDataSourceRunOutputTypeDef",
    {
        "createdAt": datetime,
        "dataSourceConfigurationSnapshot": str,
        "dataSourceId": str,
        "domainId": str,
        "errorMessage": DataSourceErrorMessageTypeDef,
        "id": str,
        "projectId": str,
        "runStatisticsForAssets": RunStatisticsForAssetsTypeDef,
        "startedAt": datetime,
        "status": DataSourceRunStatusType,
        "stoppedAt": datetime,
        "type": DataSourceRunTypeType,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class DeploymentTypeDef(TypedDict):
    deploymentId: NotRequired[str]
    deploymentStatus: NotRequired[DeploymentStatusType]
    deploymentType: NotRequired[DeploymentTypeType]
    failureReason: NotRequired[EnvironmentErrorTypeDef]
    isDeploymentComplete: NotRequired[bool]
    messages: NotRequired[List[str]]

class EnvironmentDeploymentDetailsOutputTypeDef(TypedDict):
    environmentFailureReasons: NotRequired[Dict[str, List[EnvironmentErrorTypeDef]]]
    overallDeploymentStatus: NotRequired[OverallDeploymentStatusType]

class EnvironmentDeploymentDetailsTypeDef(TypedDict):
    environmentFailureReasons: NotRequired[Mapping[str, Sequence[EnvironmentErrorTypeDef]]]
    overallDeploymentStatus: NotRequired[OverallDeploymentStatusType]

class ListDomainsOutputTypeDef(TypedDict):
    items: List[DomainSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ProjectGrantFilterTypeDef(TypedDict):
    domainUnitFilter: NotRequired[DomainUnitFilterForProjectTypeDef]

class DomainUnitPolicyGrantPrincipalOutputTypeDef(TypedDict):
    domainUnitDesignation: Literal["OWNER"]
    domainUnitGrantFilter: NotRequired[DomainUnitGrantFilterOutputTypeDef]
    domainUnitIdentifier: NotRequired[str]

class DomainUnitPolicyGrantPrincipalTypeDef(TypedDict):
    domainUnitDesignation: Literal["OWNER"]
    domainUnitGrantFilter: NotRequired[DomainUnitGrantFilterTypeDef]
    domainUnitIdentifier: NotRequired[str]

class DomainUnitOwnerPropertiesTypeDef(TypedDict):
    group: NotRequired[DomainUnitGroupPropertiesTypeDef]
    user: NotRequired[DomainUnitUserPropertiesTypeDef]

class ListDomainUnitsForParentOutputTypeDef(TypedDict):
    items: List[DomainUnitSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class RuleTargetTypeDef(TypedDict):
    domainUnitTarget: NotRequired[DomainUnitTargetTypeDef]

class EnvironmentConfigurationParametersDetailsOutputTypeDef(TypedDict):
    parameterOverrides: NotRequired[List[EnvironmentConfigurationParameterTypeDef]]
    resolvedParameters: NotRequired[List[EnvironmentConfigurationParameterTypeDef]]
    ssmPath: NotRequired[str]

class EnvironmentConfigurationParametersDetailsTypeDef(TypedDict):
    parameterOverrides: NotRequired[Sequence[EnvironmentConfigurationParameterTypeDef]]
    resolvedParameters: NotRequired[Sequence[EnvironmentConfigurationParameterTypeDef]]
    ssmPath: NotRequired[str]

class ListEnvironmentProfilesOutputTypeDef(TypedDict):
    items: List[EnvironmentProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListEnvironmentsOutputTypeDef(TypedDict):
    items: List[EnvironmentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SubscribedAssetTypeDef(TypedDict):
    assetId: str
    assetRevision: str
    status: SubscriptionGrantStatusType
    assetScope: NotRequired[AssetScopeTypeDef]
    failureCause: NotRequired[FailureCauseTypeDef]
    failureTimestamp: NotRequired[datetime]
    grantedTimestamp: NotRequired[datetime]
    targetName: NotRequired[str]

class UpdateSubscriptionGrantStatusInputTypeDef(TypedDict):
    assetIdentifier: str
    domainIdentifier: str
    identifier: str
    status: SubscriptionGrantStatusType
    failureCause: NotRequired[FailureCauseTypeDef]
    targetName: NotRequired[str]

FilterClausePaginatorTypeDef = TypedDict(
    "FilterClausePaginatorTypeDef",
    {
        "and": NotRequired[Sequence[Mapping[str, Any]]],
        "filter": NotRequired[FilterTypeDef],
        "or": NotRequired[Sequence[Mapping[str, Any]]],
    },
)
FilterClauseTypeDef = TypedDict(
    "FilterClauseTypeDef",
    {
        "and": NotRequired[Sequence[Mapping[str, Any]]],
        "filter": NotRequired[FilterTypeDef],
        "or": NotRequired[Sequence[Mapping[str, Any]]],
    },
)

class RelationalFilterConfigurationOutputTypeDef(TypedDict):
    databaseName: str
    filterExpressions: NotRequired[List[FilterExpressionTypeDef]]
    schemaName: NotRequired[str]

class RelationalFilterConfigurationTypeDef(TypedDict):
    databaseName: str
    filterExpressions: NotRequired[Sequence[FilterExpressionTypeDef]]
    schemaName: NotRequired[str]

class FormTypeDataTypeDef(TypedDict):
    domainId: str
    name: str
    revision: str
    createdAt: NotRequired[datetime]
    createdBy: NotRequired[str]
    description: NotRequired[str]
    imports: NotRequired[List[ImportTypeDef]]
    model: NotRequired[ModelTypeDef]
    originDomainId: NotRequired[str]
    originProjectId: NotRequired[str]
    owningProjectId: NotRequired[str]
    status: NotRequired[FormTypeStatusType]

class GetFormTypeOutputTypeDef(TypedDict):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    imports: List[ImportTypeDef]
    model: ModelTypeDef
    name: str
    originDomainId: str
    originProjectId: str
    owningProjectId: str
    revision: str
    status: FormTypeStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class JobRunSummaryTypeDef(TypedDict):
    createdAt: NotRequired[datetime]
    createdBy: NotRequired[str]
    domainId: NotRequired[str]
    endTime: NotRequired[datetime]
    error: NotRequired[JobRunErrorTypeDef]
    jobId: NotRequired[str]
    jobType: NotRequired[Literal["LINEAGE"]]
    runId: NotRequired[str]
    runMode: NotRequired[JobRunModeType]
    startTime: NotRequired[datetime]
    status: NotRequired[JobRunStatusType]

class GetLineageNodeInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    eventTimestamp: NotRequired[TimestampTypeDef]

class ListLineageEventsInputTypeDef(TypedDict):
    domainIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    processingStatus: NotRequired[LineageEventProcessingStatusType]
    sortOrder: NotRequired[SortOrderType]
    timestampAfter: NotRequired[TimestampTypeDef]
    timestampBefore: NotRequired[TimestampTypeDef]

class ListLineageNodeHistoryInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    direction: NotRequired[EdgeDirectionType]
    eventTimestampGTE: NotRequired[TimestampTypeDef]
    eventTimestampLTE: NotRequired[TimestampTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    sortOrder: NotRequired[SortOrderType]

ListNotificationsInputTypeDef = TypedDict(
    "ListNotificationsInputTypeDef",
    {
        "domainIdentifier": str,
        "type": NotificationTypeType,
        "afterTimestamp": NotRequired[TimestampTypeDef],
        "beforeTimestamp": NotRequired[TimestampTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "subjects": NotRequired[Sequence[str]],
        "taskStatus": NotRequired[TaskStatusType],
    },
)

class ListTimeSeriesDataPointsInputTypeDef(TypedDict):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    formName: str
    endedAt: NotRequired[TimestampTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    startedAt: NotRequired[TimestampTypeDef]

class TimeSeriesDataPointFormInputTypeDef(TypedDict):
    formName: str
    timestamp: TimestampTypeDef
    typeIdentifier: str
    content: NotRequired[str]
    typeRevision: NotRequired[str]

GetLineageNodeOutputTypeDef = TypedDict(
    "GetLineageNodeOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "downstreamNodes": List[LineageNodeReferenceTypeDef],
        "eventTimestamp": datetime,
        "formsOutput": List[FormOutputTypeDef],
        "id": str,
        "name": str,
        "sourceIdentifier": str,
        "typeName": str,
        "typeRevision": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "upstreamNodes": List[LineageNodeReferenceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMetadataGenerationRunOutputTypeDef = TypedDict(
    "GetMetadataGenerationRunOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "id": str,
        "owningProjectId": str,
        "status": MetadataGenerationRunStatusType,
        "target": MetadataGenerationRunTargetTypeDef,
        "type": Literal["BUSINESS_DESCRIPTIONS"],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MetadataGenerationRunItemTypeDef = TypedDict(
    "MetadataGenerationRunItemTypeDef",
    {
        "domainId": str,
        "id": str,
        "owningProjectId": str,
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "status": NotRequired[MetadataGenerationRunStatusType],
        "target": NotRequired[MetadataGenerationRunTargetTypeDef],
        "type": NotRequired[Literal["BUSINESS_DESCRIPTIONS"]],
    },
)
StartMetadataGenerationRunInputTypeDef = TypedDict(
    "StartMetadataGenerationRunInputTypeDef",
    {
        "domainIdentifier": str,
        "owningProjectIdentifier": str,
        "target": MetadataGenerationRunTargetTypeDef,
        "type": Literal["BUSINESS_DESCRIPTIONS"],
        "clientToken": NotRequired[str],
    },
)

class GetTimeSeriesDataPointOutputTypeDef(TypedDict):
    domainId: str
    entityId: str
    entityType: TimeSeriesEntityTypeType
    form: TimeSeriesDataPointFormOutputTypeDef
    formName: str
    ResponseMetadata: ResponseMetadataTypeDef

class PostTimeSeriesDataPointsOutputTypeDef(TypedDict):
    domainId: str
    entityId: str
    entityType: TimeSeriesEntityTypeType
    forms: List[TimeSeriesDataPointFormOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GlueSelfGrantStatusOutputTypeDef(TypedDict):
    selfGrantStatusDetails: List[SelfGrantStatusDetailTypeDef]

class RedshiftSelfGrantStatusOutputTypeDef(TypedDict):
    selfGrantStatusDetails: List[SelfGrantStatusDetailTypeDef]

class GrantedEntityInputTypeDef(TypedDict):
    listing: NotRequired[ListingRevisionInputTypeDef]

class GrantedEntityTypeDef(TypedDict):
    listing: NotRequired[ListingRevisionTypeDef]

class SearchGroupProfilesOutputTypeDef(TypedDict):
    items: List[GroupProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ProvisioningConfigurationOutputTypeDef(TypedDict):
    lakeFormationConfiguration: NotRequired[LakeFormationConfigurationOutputTypeDef]

LakeFormationConfigurationUnionTypeDef = Union[
    LakeFormationConfigurationTypeDef, LakeFormationConfigurationOutputTypeDef
]

class ListLineageNodeHistoryOutputTypeDef(TypedDict):
    nodes: List[LineageNodeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class LineageRunDetailsTypeDef(TypedDict):
    sqlQueryRunDetails: NotRequired[LineageSqlQueryRunDetailsTypeDef]

class RedshiftLineageSyncConfigurationInputTypeDef(TypedDict):
    enabled: NotRequired[bool]
    schedule: NotRequired[LineageSyncScheduleTypeDef]

class RedshiftLineageSyncConfigurationOutputTypeDef(TypedDict):
    enabled: NotRequired[bool]
    lineageJobId: NotRequired[str]
    schedule: NotRequired[LineageSyncScheduleTypeDef]

class ListAssetFiltersInputPaginateTypeDef(TypedDict):
    assetIdentifier: str
    domainIdentifier: str
    status: NotRequired[FilterStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAssetRevisionsInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListConnectionsInputPaginateTypeDef = TypedDict(
    "ListConnectionsInputPaginateTypeDef",
    {
        "domainIdentifier": str,
        "projectIdentifier": str,
        "environmentIdentifier": NotRequired[str],
        "name": NotRequired[str],
        "sortBy": NotRequired[Literal["NAME"]],
        "sortOrder": NotRequired[SortOrderType],
        "type": NotRequired[ConnectionTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListDataProductRevisionsInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDataSourceRunActivitiesInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    status: NotRequired[DataAssetActivityStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDataSourceRunsInputPaginateTypeDef(TypedDict):
    dataSourceIdentifier: str
    domainIdentifier: str
    status: NotRequired[DataSourceRunStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListDataSourcesInputPaginateTypeDef = TypedDict(
    "ListDataSourcesInputPaginateTypeDef",
    {
        "domainIdentifier": str,
        "projectIdentifier": str,
        "connectionIdentifier": NotRequired[str],
        "environmentIdentifier": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[DataSourceStatusType],
        "type": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListDomainUnitsForParentInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    parentDomainUnitIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDomainsInputPaginateTypeDef(TypedDict):
    status: NotRequired[DomainStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEntityOwnersInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    entityIdentifier: str
    entityType: Literal["DOMAIN_UNIT"]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEnvironmentActionsInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    environmentIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEnvironmentBlueprintConfigurationsInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEnvironmentBlueprintsInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    managed: NotRequired[bool]
    name: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEnvironmentProfilesInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    awsAccountId: NotRequired[str]
    awsAccountRegion: NotRequired[str]
    environmentBlueprintIdentifier: NotRequired[str]
    name: NotRequired[str]
    projectIdentifier: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEnvironmentsInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    projectIdentifier: str
    awsAccountId: NotRequired[str]
    awsAccountRegion: NotRequired[str]
    environmentBlueprintIdentifier: NotRequired[str]
    environmentProfileIdentifier: NotRequired[str]
    name: NotRequired[str]
    provider: NotRequired[str]
    status: NotRequired[EnvironmentStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListJobRunsInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    jobIdentifier: str
    sortOrder: NotRequired[SortOrderType]
    status: NotRequired[JobRunStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLineageEventsInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    processingStatus: NotRequired[LineageEventProcessingStatusType]
    sortOrder: NotRequired[SortOrderType]
    timestampAfter: NotRequired[TimestampTypeDef]
    timestampBefore: NotRequired[TimestampTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLineageNodeHistoryInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    direction: NotRequired[EdgeDirectionType]
    eventTimestampGTE: NotRequired[TimestampTypeDef]
    eventTimestampLTE: NotRequired[TimestampTypeDef]
    sortOrder: NotRequired[SortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListMetadataGenerationRunsInputPaginateTypeDef = TypedDict(
    "ListMetadataGenerationRunsInputPaginateTypeDef",
    {
        "domainIdentifier": str,
        "status": NotRequired[MetadataGenerationRunStatusType],
        "type": NotRequired[Literal["BUSINESS_DESCRIPTIONS"]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListNotificationsInputPaginateTypeDef = TypedDict(
    "ListNotificationsInputPaginateTypeDef",
    {
        "domainIdentifier": str,
        "type": NotificationTypeType,
        "afterTimestamp": NotRequired[TimestampTypeDef],
        "beforeTimestamp": NotRequired[TimestampTypeDef],
        "subjects": NotRequired[Sequence[str]],
        "taskStatus": NotRequired[TaskStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListPolicyGrantsInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TargetEntityTypeType
    policyType: ManagedPolicyTypeType
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProjectMembershipsInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    projectIdentifier: str
    sortBy: NotRequired[Literal["NAME"]]
    sortOrder: NotRequired[SortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProjectProfilesInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    name: NotRequired[str]
    sortBy: NotRequired[Literal["NAME"]]
    sortOrder: NotRequired[SortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProjectsInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    groupIdentifier: NotRequired[str]
    name: NotRequired[str]
    userIdentifier: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRulesInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    targetIdentifier: str
    targetType: Literal["DOMAIN_UNIT"]
    action: NotRequired[RuleActionType]
    assetTypes: NotRequired[Sequence[str]]
    dataProduct: NotRequired[bool]
    includeCascaded: NotRequired[bool]
    projectIds: NotRequired[Sequence[str]]
    ruleType: NotRequired[Literal["METADATA_FORM_ENFORCEMENT"]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSubscriptionGrantsInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    environmentId: NotRequired[str]
    owningProjectId: NotRequired[str]
    sortBy: NotRequired[SortKeyType]
    sortOrder: NotRequired[SortOrderType]
    subscribedListingId: NotRequired[str]
    subscriptionId: NotRequired[str]
    subscriptionTargetId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSubscriptionRequestsInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    approverProjectId: NotRequired[str]
    owningProjectId: NotRequired[str]
    sortBy: NotRequired[SortKeyType]
    sortOrder: NotRequired[SortOrderType]
    status: NotRequired[SubscriptionRequestStatusType]
    subscribedListingId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSubscriptionTargetsInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    environmentIdentifier: str
    sortBy: NotRequired[SortKeyType]
    sortOrder: NotRequired[SortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSubscriptionsInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    approverProjectId: NotRequired[str]
    owningProjectId: NotRequired[str]
    sortBy: NotRequired[SortKeyType]
    sortOrder: NotRequired[SortOrderType]
    status: NotRequired[SubscriptionStatusType]
    subscribedListingId: NotRequired[str]
    subscriptionRequestIdentifier: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTimeSeriesDataPointsInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    formName: str
    endedAt: NotRequired[TimestampTypeDef]
    startedAt: NotRequired[TimestampTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchGroupProfilesInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    groupType: GroupSearchTypeType
    searchText: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchUserProfilesInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    userType: UserSearchTypeType
    searchText: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProjectProfilesOutputTypeDef(TypedDict):
    items: List[ProjectProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class MemberDetailsTypeDef(TypedDict):
    group: NotRequired[GroupDetailsTypeDef]
    user: NotRequired[UserDetailsTypeDef]

class MetadataFormEnforcementDetailOutputTypeDef(TypedDict):
    requiredMetadataForms: NotRequired[List[MetadataFormReferenceTypeDef]]

class MetadataFormEnforcementDetailTypeDef(TypedDict):
    requiredMetadataForms: NotRequired[Sequence[MetadataFormReferenceTypeDef]]

class OpenLineageRunEventSummaryTypeDef(TypedDict):
    eventType: NotRequired[OpenLineageRunStateType]
    inputs: NotRequired[List[NameIdentifierTypeDef]]
    job: NotRequired[NameIdentifierTypeDef]
    outputs: NotRequired[List[NameIdentifierTypeDef]]
    runId: NotRequired[str]

RowFilterExpressionOutputTypeDef = TypedDict(
    "RowFilterExpressionOutputTypeDef",
    {
        "equalTo": NotRequired[EqualToExpressionTypeDef],
        "greaterThan": NotRequired[GreaterThanExpressionTypeDef],
        "greaterThanOrEqualTo": NotRequired[GreaterThanOrEqualToExpressionTypeDef],
        "in": NotRequired[InExpressionOutputTypeDef],
        "isNotNull": NotRequired[IsNotNullExpressionTypeDef],
        "isNull": NotRequired[IsNullExpressionTypeDef],
        "lessThan": NotRequired[LessThanExpressionTypeDef],
        "lessThanOrEqualTo": NotRequired[LessThanOrEqualToExpressionTypeDef],
        "like": NotRequired[LikeExpressionTypeDef],
        "notEqualTo": NotRequired[NotEqualToExpressionTypeDef],
        "notIn": NotRequired[NotInExpressionOutputTypeDef],
        "notLike": NotRequired[NotLikeExpressionTypeDef],
    },
)
RowFilterExpressionTypeDef = TypedDict(
    "RowFilterExpressionTypeDef",
    {
        "equalTo": NotRequired[EqualToExpressionTypeDef],
        "greaterThan": NotRequired[GreaterThanExpressionTypeDef],
        "greaterThanOrEqualTo": NotRequired[GreaterThanOrEqualToExpressionTypeDef],
        "in": NotRequired[InExpressionTypeDef],
        "isNotNull": NotRequired[IsNotNullExpressionTypeDef],
        "isNull": NotRequired[IsNullExpressionTypeDef],
        "lessThan": NotRequired[LessThanExpressionTypeDef],
        "lessThanOrEqualTo": NotRequired[LessThanOrEqualToExpressionTypeDef],
        "like": NotRequired[LikeExpressionTypeDef],
        "notEqualTo": NotRequired[NotEqualToExpressionTypeDef],
        "notIn": NotRequired[NotInExpressionTypeDef],
        "notLike": NotRequired[NotLikeExpressionTypeDef],
    },
)

class TopicTypeDef(TypedDict):
    resource: NotificationResourceTypeDef
    role: NotificationRoleType
    subject: str

class OAuth2PropertiesOutputTypeDef(TypedDict):
    authorizationCodeProperties: NotRequired[AuthorizationCodePropertiesTypeDef]
    oAuth2ClientApplication: NotRequired[OAuth2ClientApplicationTypeDef]
    oAuth2Credentials: NotRequired[GlueOAuth2CredentialsTypeDef]
    oAuth2GrantType: NotRequired[OAuth2GrantTypeType]
    tokenUrl: NotRequired[str]
    tokenUrlParametersMap: NotRequired[Dict[str, str]]

class OAuth2PropertiesTypeDef(TypedDict):
    authorizationCodeProperties: NotRequired[AuthorizationCodePropertiesTypeDef]
    oAuth2ClientApplication: NotRequired[OAuth2ClientApplicationTypeDef]
    oAuth2Credentials: NotRequired[GlueOAuth2CredentialsTypeDef]
    oAuth2GrantType: NotRequired[OAuth2GrantTypeType]
    tokenUrl: NotRequired[str]
    tokenUrlParametersMap: NotRequired[Mapping[str, str]]

class OwnerPropertiesOutputTypeDef(TypedDict):
    group: NotRequired[OwnerGroupPropertiesOutputTypeDef]
    user: NotRequired[OwnerUserPropertiesOutputTypeDef]

class OwnerPropertiesTypeDef(TypedDict):
    group: NotRequired[OwnerGroupPropertiesTypeDef]
    user: NotRequired[OwnerUserPropertiesTypeDef]

PhysicalConnectionRequirementsUnionTypeDef = Union[
    PhysicalConnectionRequirementsTypeDef, PhysicalConnectionRequirementsOutputTypeDef
]

class PolicyGrantDetailOutputTypeDef(TypedDict):
    addToProjectMemberPool: NotRequired[AddToProjectMemberPoolPolicyGrantDetailTypeDef]
    createAssetType: NotRequired[CreateAssetTypePolicyGrantDetailTypeDef]
    createDomainUnit: NotRequired[CreateDomainUnitPolicyGrantDetailTypeDef]
    createEnvironment: NotRequired[Dict[str, Any]]
    createEnvironmentFromBlueprint: NotRequired[Dict[str, Any]]
    createEnvironmentProfile: NotRequired[CreateEnvironmentProfilePolicyGrantDetailTypeDef]
    createFormType: NotRequired[CreateFormTypePolicyGrantDetailTypeDef]
    createGlossary: NotRequired[CreateGlossaryPolicyGrantDetailTypeDef]
    createProject: NotRequired[CreateProjectPolicyGrantDetailTypeDef]
    createProjectFromProjectProfile: NotRequired[
        CreateProjectFromProjectProfilePolicyGrantDetailOutputTypeDef
    ]
    delegateCreateEnvironmentProfile: NotRequired[Dict[str, Any]]
    overrideDomainUnitOwners: NotRequired[OverrideDomainUnitOwnersPolicyGrantDetailTypeDef]
    overrideProjectOwners: NotRequired[OverrideProjectOwnersPolicyGrantDetailTypeDef]
    useAssetType: NotRequired[UseAssetTypePolicyGrantDetailTypeDef]

class PolicyGrantDetailTypeDef(TypedDict):
    addToProjectMemberPool: NotRequired[AddToProjectMemberPoolPolicyGrantDetailTypeDef]
    createAssetType: NotRequired[CreateAssetTypePolicyGrantDetailTypeDef]
    createDomainUnit: NotRequired[CreateDomainUnitPolicyGrantDetailTypeDef]
    createEnvironment: NotRequired[Mapping[str, Any]]
    createEnvironmentFromBlueprint: NotRequired[Mapping[str, Any]]
    createEnvironmentProfile: NotRequired[CreateEnvironmentProfilePolicyGrantDetailTypeDef]
    createFormType: NotRequired[CreateFormTypePolicyGrantDetailTypeDef]
    createGlossary: NotRequired[CreateGlossaryPolicyGrantDetailTypeDef]
    createProject: NotRequired[CreateProjectPolicyGrantDetailTypeDef]
    createProjectFromProjectProfile: NotRequired[
        CreateProjectFromProjectProfilePolicyGrantDetailTypeDef
    ]
    delegateCreateEnvironmentProfile: NotRequired[Mapping[str, Any]]
    overrideDomainUnitOwners: NotRequired[OverrideDomainUnitOwnersPolicyGrantDetailTypeDef]
    overrideProjectOwners: NotRequired[OverrideProjectOwnersPolicyGrantDetailTypeDef]
    useAssetType: NotRequired[UseAssetTypePolicyGrantDetailTypeDef]

class RuleScopeOutputTypeDef(TypedDict):
    assetType: NotRequired[AssetTypesForRuleOutputTypeDef]
    dataProduct: NotRequired[bool]
    project: NotRequired[ProjectsForRuleOutputTypeDef]

class RuleScopeTypeDef(TypedDict):
    assetType: NotRequired[AssetTypesForRuleTypeDef]
    dataProduct: NotRequired[bool]
    project: NotRequired[ProjectsForRuleTypeDef]

class RedshiftCredentialsTypeDef(TypedDict):
    secretArn: NotRequired[str]
    usernamePassword: NotRequired[UsernamePasswordTypeDef]

class SparkEmrPropertiesOutputTypeDef(TypedDict):
    computeArn: NotRequired[str]
    credentials: NotRequired[UsernamePasswordTypeDef]
    credentialsExpiration: NotRequired[datetime]
    governanceType: NotRequired[GovernanceTypeType]
    instanceProfileArn: NotRequired[str]
    javaVirtualEnv: NotRequired[str]
    livyEndpoint: NotRequired[str]
    logUri: NotRequired[str]
    pythonVirtualEnv: NotRequired[str]
    runtimeRole: NotRequired[str]
    trustedCertificatesS3Uri: NotRequired[str]

class RedshiftStorageTypeDef(TypedDict):
    redshiftClusterSource: NotRequired[RedshiftClusterStorageTypeDef]
    redshiftServerlessSource: NotRequired[RedshiftServerlessStorageTypeDef]

class RejectPredictionsInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    clientToken: NotRequired[str]
    rejectChoices: NotRequired[Sequence[RejectChoiceTypeDef]]
    rejectRule: NotRequired[RejectRuleTypeDef]
    revision: NotRequired[str]

class SparkGluePropertiesInputTypeDef(TypedDict):
    additionalArgs: NotRequired[SparkGlueArgsTypeDef]
    glueConnectionName: NotRequired[str]
    glueVersion: NotRequired[str]
    idleTimeout: NotRequired[int]
    javaVirtualEnv: NotRequired[str]
    numberOfWorkers: NotRequired[int]
    pythonVirtualEnv: NotRequired[str]
    workerType: NotRequired[str]

class SparkGluePropertiesOutputTypeDef(TypedDict):
    additionalArgs: NotRequired[SparkGlueArgsTypeDef]
    glueConnectionName: NotRequired[str]
    glueVersion: NotRequired[str]
    idleTimeout: NotRequired[int]
    javaVirtualEnv: NotRequired[str]
    numberOfWorkers: NotRequired[int]
    pythonVirtualEnv: NotRequired[str]
    workerType: NotRequired[str]

class UserProfileDetailsTypeDef(TypedDict):
    iam: NotRequired[IamUserProfileDetailsTypeDef]
    sso: NotRequired[SsoUserProfileDetailsTypeDef]

class SubscribedPrincipalInputTypeDef(TypedDict):
    project: NotRequired[SubscribedProjectInputTypeDef]

class SubscribedPrincipalTypeDef(TypedDict):
    project: NotRequired[SubscribedProjectTypeDef]

TermRelationsUnionTypeDef = Union[TermRelationsTypeDef, TermRelationsOutputTypeDef]

class CreateEnvironmentActionInputTypeDef(TypedDict):
    domainIdentifier: str
    environmentIdentifier: str
    name: str
    parameters: ActionParametersTypeDef
    description: NotRequired[str]

CreateEnvironmentActionOutputTypeDef = TypedDict(
    "CreateEnvironmentActionOutputTypeDef",
    {
        "description": str,
        "domainId": str,
        "environmentId": str,
        "id": str,
        "name": str,
        "parameters": ActionParametersTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnvironmentActionSummaryTypeDef = TypedDict(
    "EnvironmentActionSummaryTypeDef",
    {
        "domainId": str,
        "environmentId": str,
        "id": str,
        "name": str,
        "parameters": ActionParametersTypeDef,
        "description": NotRequired[str],
    },
)
GetEnvironmentActionOutputTypeDef = TypedDict(
    "GetEnvironmentActionOutputTypeDef",
    {
        "description": str,
        "domainId": str,
        "environmentId": str,
        "id": str,
        "name": str,
        "parameters": ActionParametersTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class UpdateEnvironmentActionInputTypeDef(TypedDict):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str
    description: NotRequired[str]
    name: NotRequired[str]
    parameters: NotRequired[ActionParametersTypeDef]

UpdateEnvironmentActionOutputTypeDef = TypedDict(
    "UpdateEnvironmentActionOutputTypeDef",
    {
        "description": str,
        "domainId": str,
        "environmentId": str,
        "id": str,
        "name": str,
        "parameters": ActionParametersTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class AssetItemTypeDef(TypedDict):
    domainId: str
    identifier: str
    name: str
    owningProjectId: str
    typeIdentifier: str
    typeRevision: str
    additionalAttributes: NotRequired[AssetItemAdditionalAttributesTypeDef]
    createdAt: NotRequired[datetime]
    createdBy: NotRequired[str]
    description: NotRequired[str]
    externalIdentifier: NotRequired[str]
    firstRevisionCreatedAt: NotRequired[datetime]
    firstRevisionCreatedBy: NotRequired[str]
    glossaryTerms: NotRequired[List[str]]

class AssetListingItemTypeDef(TypedDict):
    additionalAttributes: NotRequired[AssetListingItemAdditionalAttributesTypeDef]
    createdAt: NotRequired[datetime]
    description: NotRequired[str]
    entityId: NotRequired[str]
    entityRevision: NotRequired[str]
    entityType: NotRequired[str]
    glossaryTerms: NotRequired[List[DetailedGlossaryTermTypeDef]]
    listingCreatedBy: NotRequired[str]
    listingId: NotRequired[str]
    listingRevision: NotRequired[str]
    listingUpdatedBy: NotRequired[str]
    name: NotRequired[str]
    owningProjectId: NotRequired[str]

class DataProductListingItemTypeDef(TypedDict):
    additionalAttributes: NotRequired[DataProductListingItemAdditionalAttributesTypeDef]
    createdAt: NotRequired[datetime]
    description: NotRequired[str]
    entityId: NotRequired[str]
    entityRevision: NotRequired[str]
    glossaryTerms: NotRequired[List[DetailedGlossaryTermTypeDef]]
    items: NotRequired[List[ListingSummaryItemTypeDef]]
    listingCreatedBy: NotRequired[str]
    listingId: NotRequired[str]
    listingRevision: NotRequired[str]
    listingUpdatedBy: NotRequired[str]
    name: NotRequired[str]
    owningProjectId: NotRequired[str]

class DataProductListingTypeDef(TypedDict):
    createdAt: NotRequired[datetime]
    dataProductId: NotRequired[str]
    dataProductRevision: NotRequired[str]
    forms: NotRequired[str]
    glossaryTerms: NotRequired[List[DetailedGlossaryTermTypeDef]]
    items: NotRequired[List[ListingSummaryTypeDef]]
    owningProjectId: NotRequired[str]

class SubscribedListingItemTypeDef(TypedDict):
    assetListing: NotRequired[SubscribedAssetListingTypeDef]
    productListing: NotRequired[SubscribedProductListingTypeDef]

class GlueConnectionPatchTypeDef(TypedDict):
    authenticationConfiguration: NotRequired[AuthenticationConfigurationPatchTypeDef]
    connectionProperties: NotRequired[Mapping[str, str]]
    description: NotRequired[str]

class CreateAssetInputTypeDef(TypedDict):
    domainIdentifier: str
    name: str
    owningProjectIdentifier: str
    typeIdentifier: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    externalIdentifier: NotRequired[str]
    formsInput: NotRequired[Sequence[FormInputTypeDef]]
    glossaryTerms: NotRequired[Sequence[str]]
    predictionConfiguration: NotRequired[PredictionConfigurationTypeDef]
    typeRevision: NotRequired[str]

CreateAssetOutputTypeDef = TypedDict(
    "CreateAssetOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "externalIdentifier": str,
        "firstRevisionCreatedAt": datetime,
        "firstRevisionCreatedBy": str,
        "formsOutput": List[FormOutputTypeDef],
        "glossaryTerms": List[str],
        "id": str,
        "latestTimeSeriesDataPointFormsOutput": List[TimeSeriesDataPointSummaryFormOutputTypeDef],
        "listing": AssetListingDetailsTypeDef,
        "name": str,
        "owningProjectId": str,
        "predictionConfiguration": PredictionConfigurationTypeDef,
        "readOnlyFormsOutput": List[FormOutputTypeDef],
        "revision": str,
        "typeIdentifier": str,
        "typeRevision": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateAssetRevisionInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    name: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    formsInput: NotRequired[Sequence[FormInputTypeDef]]
    glossaryTerms: NotRequired[Sequence[str]]
    predictionConfiguration: NotRequired[PredictionConfigurationTypeDef]
    typeRevision: NotRequired[str]

CreateAssetRevisionOutputTypeDef = TypedDict(
    "CreateAssetRevisionOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "externalIdentifier": str,
        "firstRevisionCreatedAt": datetime,
        "firstRevisionCreatedBy": str,
        "formsOutput": List[FormOutputTypeDef],
        "glossaryTerms": List[str],
        "id": str,
        "latestTimeSeriesDataPointFormsOutput": List[TimeSeriesDataPointSummaryFormOutputTypeDef],
        "listing": AssetListingDetailsTypeDef,
        "name": str,
        "owningProjectId": str,
        "predictionConfiguration": PredictionConfigurationTypeDef,
        "readOnlyFormsOutput": List[FormOutputTypeDef],
        "revision": str,
        "typeIdentifier": str,
        "typeRevision": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnvironmentBlueprintSummaryTypeDef = TypedDict(
    "EnvironmentBlueprintSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "provider": str,
        "provisioningProperties": ProvisioningPropertiesTypeDef,
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "updatedAt": NotRequired[datetime],
    },
)
GetEnvironmentBlueprintOutputTypeDef = TypedDict(
    "GetEnvironmentBlueprintOutputTypeDef",
    {
        "createdAt": datetime,
        "deploymentProperties": DeploymentPropertiesTypeDef,
        "description": str,
        "glossaryTerms": List[str],
        "id": str,
        "name": str,
        "provider": str,
        "provisioningProperties": ProvisioningPropertiesTypeDef,
        "updatedAt": datetime,
        "userParameters": List[CustomParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListDataSourcesOutputTypeDef(TypedDict):
    items: List[DataSourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

EnvironmentConfigurationUserParameterUnionTypeDef = Union[
    EnvironmentConfigurationUserParameterTypeDef, EnvironmentConfigurationUserParameterOutputTypeDef
]

class ListProjectsOutputTypeDef(TypedDict):
    items: List[ProjectSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSubscriptionTargetsOutputTypeDef(TypedDict):
    items: List[SubscriptionTargetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateDataProductInputTypeDef(TypedDict):
    domainIdentifier: str
    name: str
    owningProjectIdentifier: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    formsInput: NotRequired[Sequence[FormInputTypeDef]]
    glossaryTerms: NotRequired[Sequence[str]]
    items: NotRequired[Sequence[DataProductItemUnionTypeDef]]

class CreateDataProductRevisionInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    name: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    formsInput: NotRequired[Sequence[FormInputTypeDef]]
    glossaryTerms: NotRequired[Sequence[str]]
    items: NotRequired[Sequence[DataProductItemUnionTypeDef]]

class ListDataSourceRunActivitiesOutputTypeDef(TypedDict):
    items: List[DataSourceRunActivityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListDataSourceRunsOutputTypeDef(TypedDict):
    items: List[DataSourceRunSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

CreateEnvironmentOutputTypeDef = TypedDict(
    "CreateEnvironmentOutputTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "createdAt": datetime,
        "createdBy": str,
        "deploymentProperties": DeploymentPropertiesTypeDef,
        "description": str,
        "domainId": str,
        "environmentActions": List[ConfigurableEnvironmentActionTypeDef],
        "environmentBlueprintId": str,
        "environmentConfigurationId": str,
        "environmentProfileId": str,
        "glossaryTerms": List[str],
        "id": str,
        "lastDeployment": DeploymentTypeDef,
        "name": str,
        "projectId": str,
        "provider": str,
        "provisionedResources": List[ResourceTypeDef],
        "provisioningProperties": ProvisioningPropertiesTypeDef,
        "status": EnvironmentStatusType,
        "updatedAt": datetime,
        "userParameters": List[CustomParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEnvironmentOutputTypeDef = TypedDict(
    "GetEnvironmentOutputTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "createdAt": datetime,
        "createdBy": str,
        "deploymentProperties": DeploymentPropertiesTypeDef,
        "description": str,
        "domainId": str,
        "environmentActions": List[ConfigurableEnvironmentActionTypeDef],
        "environmentBlueprintId": str,
        "environmentConfigurationId": str,
        "environmentProfileId": str,
        "glossaryTerms": List[str],
        "id": str,
        "lastDeployment": DeploymentTypeDef,
        "name": str,
        "projectId": str,
        "provider": str,
        "provisionedResources": List[ResourceTypeDef],
        "provisioningProperties": ProvisioningPropertiesTypeDef,
        "status": EnvironmentStatusType,
        "updatedAt": datetime,
        "userParameters": List[CustomParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEnvironmentOutputTypeDef = TypedDict(
    "UpdateEnvironmentOutputTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "createdAt": datetime,
        "createdBy": str,
        "deploymentProperties": DeploymentPropertiesTypeDef,
        "description": str,
        "domainId": str,
        "environmentActions": List[ConfigurableEnvironmentActionTypeDef],
        "environmentBlueprintId": str,
        "environmentConfigurationId": str,
        "environmentProfileId": str,
        "glossaryTerms": List[str],
        "id": str,
        "lastDeployment": DeploymentTypeDef,
        "name": str,
        "projectId": str,
        "provider": str,
        "provisionedResources": List[ResourceTypeDef],
        "provisioningProperties": ProvisioningPropertiesTypeDef,
        "status": EnvironmentStatusType,
        "updatedAt": datetime,
        "userParameters": List[CustomParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProjectOutputTypeDef = TypedDict(
    "CreateProjectOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "domainUnitId": str,
        "environmentDeploymentDetails": EnvironmentDeploymentDetailsOutputTypeDef,
        "failureReasons": List[ProjectDeletionErrorTypeDef],
        "glossaryTerms": List[str],
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "projectProfileId": str,
        "projectStatus": ProjectStatusType,
        "userParameters": List[EnvironmentConfigurationUserParameterOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProjectOutputTypeDef = TypedDict(
    "GetProjectOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "domainUnitId": str,
        "environmentDeploymentDetails": EnvironmentDeploymentDetailsOutputTypeDef,
        "failureReasons": List[ProjectDeletionErrorTypeDef],
        "glossaryTerms": List[str],
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "projectProfileId": str,
        "projectStatus": ProjectStatusType,
        "userParameters": List[EnvironmentConfigurationUserParameterOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProjectOutputTypeDef = TypedDict(
    "UpdateProjectOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "domainUnitId": str,
        "environmentDeploymentDetails": EnvironmentDeploymentDetailsOutputTypeDef,
        "failureReasons": List[ProjectDeletionErrorTypeDef],
        "glossaryTerms": List[str],
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "projectProfileId": str,
        "projectStatus": ProjectStatusType,
        "userParameters": List[EnvironmentConfigurationUserParameterOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnvironmentDeploymentDetailsUnionTypeDef = Union[
    EnvironmentDeploymentDetailsTypeDef, EnvironmentDeploymentDetailsOutputTypeDef
]

class ProjectPolicyGrantPrincipalTypeDef(TypedDict):
    projectDesignation: ProjectDesignationType
    projectGrantFilter: NotRequired[ProjectGrantFilterTypeDef]
    projectIdentifier: NotRequired[str]

CreateDomainUnitOutputTypeDef = TypedDict(
    "CreateDomainUnitOutputTypeDef",
    {
        "ancestorDomainUnitIds": List[str],
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "id": str,
        "name": str,
        "owners": List[DomainUnitOwnerPropertiesTypeDef],
        "parentDomainUnitId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDomainUnitOutputTypeDef = TypedDict(
    "GetDomainUnitOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "lastUpdatedBy": str,
        "name": str,
        "owners": List[DomainUnitOwnerPropertiesTypeDef],
        "parentDomainUnitId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDomainUnitOutputTypeDef = TypedDict(
    "UpdateDomainUnitOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "lastUpdatedBy": str,
        "name": str,
        "owners": List[DomainUnitOwnerPropertiesTypeDef],
        "parentDomainUnitId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnvironmentConfigurationOutputTypeDef = TypedDict(
    "EnvironmentConfigurationOutputTypeDef",
    {
        "awsAccount": AwsAccountTypeDef,
        "awsRegion": RegionTypeDef,
        "environmentBlueprintId": str,
        "name": str,
        "configurationParameters": NotRequired[
            EnvironmentConfigurationParametersDetailsOutputTypeDef
        ],
        "deploymentMode": NotRequired[DeploymentModeType],
        "deploymentOrder": NotRequired[int],
        "description": NotRequired[str],
        "id": NotRequired[str],
    },
)
EnvironmentConfigurationParametersDetailsUnionTypeDef = Union[
    EnvironmentConfigurationParametersDetailsTypeDef,
    EnvironmentConfigurationParametersDetailsOutputTypeDef,
]

class SearchInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    searchScope: InventorySearchScopeType
    additionalAttributes: NotRequired[Sequence[SearchOutputAdditionalAttributeType]]
    filters: NotRequired[FilterClausePaginatorTypeDef]
    owningProjectIdentifier: NotRequired[str]
    searchIn: NotRequired[Sequence[SearchInItemTypeDef]]
    searchText: NotRequired[str]
    sort: NotRequired[SearchSortTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchListingsInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    additionalAttributes: NotRequired[Sequence[SearchOutputAdditionalAttributeType]]
    filters: NotRequired[FilterClausePaginatorTypeDef]
    searchIn: NotRequired[Sequence[SearchInItemTypeDef]]
    searchText: NotRequired[str]
    sort: NotRequired[SearchSortTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchTypesInputPaginateTypeDef(TypedDict):
    domainIdentifier: str
    managed: bool
    searchScope: TypesSearchScopeType
    filters: NotRequired[FilterClausePaginatorTypeDef]
    searchIn: NotRequired[Sequence[SearchInItemTypeDef]]
    searchText: NotRequired[str]
    sort: NotRequired[SearchSortTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchInputTypeDef(TypedDict):
    domainIdentifier: str
    searchScope: InventorySearchScopeType
    additionalAttributes: NotRequired[Sequence[SearchOutputAdditionalAttributeType]]
    filters: NotRequired[FilterClauseTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    owningProjectIdentifier: NotRequired[str]
    searchIn: NotRequired[Sequence[SearchInItemTypeDef]]
    searchText: NotRequired[str]
    sort: NotRequired[SearchSortTypeDef]

class SearchListingsInputTypeDef(TypedDict):
    domainIdentifier: str
    additionalAttributes: NotRequired[Sequence[SearchOutputAdditionalAttributeType]]
    filters: NotRequired[FilterClauseTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    searchIn: NotRequired[Sequence[SearchInItemTypeDef]]
    searchText: NotRequired[str]
    sort: NotRequired[SearchSortTypeDef]

class SearchTypesInputTypeDef(TypedDict):
    domainIdentifier: str
    managed: bool
    searchScope: TypesSearchScopeType
    filters: NotRequired[FilterClauseTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    searchIn: NotRequired[Sequence[SearchInItemTypeDef]]
    searchText: NotRequired[str]
    sort: NotRequired[SearchSortTypeDef]

class GlueRunConfigurationOutputTypeDef(TypedDict):
    relationalFilterConfigurations: List[RelationalFilterConfigurationOutputTypeDef]
    accountId: NotRequired[str]
    autoImportDataQualityResult: NotRequired[bool]
    catalogName: NotRequired[str]
    dataAccessRole: NotRequired[str]
    region: NotRequired[str]

RelationalFilterConfigurationUnionTypeDef = Union[
    RelationalFilterConfigurationTypeDef, RelationalFilterConfigurationOutputTypeDef
]

class SearchTypesResultItemTypeDef(TypedDict):
    assetTypeItem: NotRequired[AssetTypeItemTypeDef]
    formTypeItem: NotRequired[FormTypeDataTypeDef]
    lineageNodeTypeItem: NotRequired[LineageNodeTypeItemTypeDef]

class ListJobRunsOutputTypeDef(TypedDict):
    items: List[JobRunSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class PostTimeSeriesDataPointsInputTypeDef(TypedDict):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    forms: Sequence[TimeSeriesDataPointFormInputTypeDef]
    clientToken: NotRequired[str]

class ListMetadataGenerationRunsOutputTypeDef(TypedDict):
    items: List[MetadataGenerationRunItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SelfGrantStatusOutputTypeDef(TypedDict):
    glueSelfGrantStatus: NotRequired[GlueSelfGrantStatusOutputTypeDef]
    redshiftSelfGrantStatus: NotRequired[RedshiftSelfGrantStatusOutputTypeDef]

class CreateSubscriptionGrantInputTypeDef(TypedDict):
    domainIdentifier: str
    environmentIdentifier: str
    grantedEntity: GrantedEntityInputTypeDef
    assetTargetNames: NotRequired[Sequence[AssetTargetNameMapTypeDef]]
    clientToken: NotRequired[str]
    subscriptionTargetIdentifier: NotRequired[str]

CreateSubscriptionGrantOutputTypeDef = TypedDict(
    "CreateSubscriptionGrantOutputTypeDef",
    {
        "assets": List[SubscribedAssetTypeDef],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "grantedEntity": GrantedEntityTypeDef,
        "id": str,
        "status": SubscriptionGrantOverallStatusType,
        "subscriptionId": str,
        "subscriptionTargetId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSubscriptionGrantOutputTypeDef = TypedDict(
    "DeleteSubscriptionGrantOutputTypeDef",
    {
        "assets": List[SubscribedAssetTypeDef],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "grantedEntity": GrantedEntityTypeDef,
        "id": str,
        "status": SubscriptionGrantOverallStatusType,
        "subscriptionId": str,
        "subscriptionTargetId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSubscriptionGrantOutputTypeDef = TypedDict(
    "GetSubscriptionGrantOutputTypeDef",
    {
        "assets": List[SubscribedAssetTypeDef],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "grantedEntity": GrantedEntityTypeDef,
        "id": str,
        "status": SubscriptionGrantOverallStatusType,
        "subscriptionId": str,
        "subscriptionTargetId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubscriptionGrantSummaryTypeDef = TypedDict(
    "SubscriptionGrantSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "grantedEntity": GrantedEntityTypeDef,
        "id": str,
        "status": SubscriptionGrantOverallStatusType,
        "subscriptionTargetId": str,
        "updatedAt": datetime,
        "assets": NotRequired[List[SubscribedAssetTypeDef]],
        "subscriptionId": NotRequired[str],
        "updatedBy": NotRequired[str],
    },
)
UpdateSubscriptionGrantStatusOutputTypeDef = TypedDict(
    "UpdateSubscriptionGrantStatusOutputTypeDef",
    {
        "assets": List[SubscribedAssetTypeDef],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "grantedEntity": GrantedEntityTypeDef,
        "id": str,
        "status": SubscriptionGrantOverallStatusType,
        "subscriptionId": str,
        "subscriptionTargetId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class EnvironmentBlueprintConfigurationItemTypeDef(TypedDict):
    domainId: str
    environmentBlueprintId: str
    createdAt: NotRequired[datetime]
    enabledRegions: NotRequired[List[str]]
    environmentRolePermissionBoundary: NotRequired[str]
    manageAccessRoleArn: NotRequired[str]
    provisioningConfigurations: NotRequired[List[ProvisioningConfigurationOutputTypeDef]]
    provisioningRoleArn: NotRequired[str]
    regionalParameters: NotRequired[Dict[str, Dict[str, str]]]
    updatedAt: NotRequired[datetime]

class GetEnvironmentBlueprintConfigurationOutputTypeDef(TypedDict):
    createdAt: datetime
    domainId: str
    enabledRegions: List[str]
    environmentBlueprintId: str
    environmentRolePermissionBoundary: str
    manageAccessRoleArn: str
    provisioningConfigurations: List[ProvisioningConfigurationOutputTypeDef]
    provisioningRoleArn: str
    regionalParameters: Dict[str, Dict[str, str]]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PutEnvironmentBlueprintConfigurationOutputTypeDef(TypedDict):
    createdAt: datetime
    domainId: str
    enabledRegions: List[str]
    environmentBlueprintId: str
    environmentRolePermissionBoundary: str
    manageAccessRoleArn: str
    provisioningConfigurations: List[ProvisioningConfigurationOutputTypeDef]
    provisioningRoleArn: str
    regionalParameters: Dict[str, Dict[str, str]]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ProvisioningConfigurationTypeDef(TypedDict):
    lakeFormationConfiguration: NotRequired[LakeFormationConfigurationUnionTypeDef]

class JobRunDetailsTypeDef(TypedDict):
    lineageRunDetails: NotRequired[LineageRunDetailsTypeDef]

class ProjectMemberTypeDef(TypedDict):
    designation: UserDesignationType
    memberDetails: MemberDetailsTypeDef

class RuleDetailOutputTypeDef(TypedDict):
    metadataFormEnforcementDetail: NotRequired[MetadataFormEnforcementDetailOutputTypeDef]

class RuleDetailTypeDef(TypedDict):
    metadataFormEnforcementDetail: NotRequired[MetadataFormEnforcementDetailTypeDef]

class EventSummaryTypeDef(TypedDict):
    openLineageRunEventSummary: NotRequired[OpenLineageRunEventSummaryTypeDef]

RowFilterOutputTypeDef = TypedDict(
    "RowFilterOutputTypeDef",
    {
        "and": NotRequired[List[Dict[str, Any]]],
        "expression": NotRequired[RowFilterExpressionOutputTypeDef],
        "or": NotRequired[List[Dict[str, Any]]],
    },
)
RowFilterTypeDef = TypedDict(
    "RowFilterTypeDef",
    {
        "and": NotRequired[Sequence[Mapping[str, Any]]],
        "expression": NotRequired[RowFilterExpressionTypeDef],
        "or": NotRequired[Sequence[Mapping[str, Any]]],
    },
)
NotificationOutputTypeDef = TypedDict(
    "NotificationOutputTypeDef",
    {
        "actionLink": str,
        "creationTimestamp": datetime,
        "domainIdentifier": str,
        "identifier": str,
        "lastUpdatedTimestamp": datetime,
        "message": str,
        "title": str,
        "topic": TopicTypeDef,
        "type": NotificationTypeType,
        "metadata": NotRequired[Dict[str, str]],
        "status": NotRequired[TaskStatusType],
    },
)

class AuthenticationConfigurationTypeDef(TypedDict):
    authenticationType: NotRequired[AuthenticationTypeType]
    oAuth2Properties: NotRequired[OAuth2PropertiesOutputTypeDef]
    secretArn: NotRequired[str]

OAuth2PropertiesUnionTypeDef = Union[OAuth2PropertiesTypeDef, OAuth2PropertiesOutputTypeDef]

class ListEntityOwnersOutputTypeDef(TypedDict):
    owners: List[OwnerPropertiesOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class AddEntityOwnerInputTypeDef(TypedDict):
    domainIdentifier: str
    entityIdentifier: str
    entityType: Literal["DOMAIN_UNIT"]
    owner: OwnerPropertiesTypeDef
    clientToken: NotRequired[str]

class RemoveEntityOwnerInputTypeDef(TypedDict):
    domainIdentifier: str
    entityIdentifier: str
    entityType: Literal["DOMAIN_UNIT"]
    owner: OwnerPropertiesTypeDef
    clientToken: NotRequired[str]

PolicyGrantDetailUnionTypeDef = Union[PolicyGrantDetailTypeDef, PolicyGrantDetailOutputTypeDef]

class RuleSummaryTypeDef(TypedDict):
    action: NotRequired[RuleActionType]
    identifier: NotRequired[str]
    lastUpdatedBy: NotRequired[str]
    name: NotRequired[str]
    revision: NotRequired[str]
    ruleType: NotRequired[Literal["METADATA_FORM_ENFORCEMENT"]]
    scope: NotRequired[RuleScopeOutputTypeDef]
    target: NotRequired[RuleTargetTypeDef]
    targetType: NotRequired[Literal["DOMAIN_UNIT"]]
    updatedAt: NotRequired[datetime]

RuleScopeUnionTypeDef = Union[RuleScopeTypeDef, RuleScopeOutputTypeDef]

class RedshiftPropertiesInputTypeDef(TypedDict):
    credentials: NotRequired[RedshiftCredentialsTypeDef]
    databaseName: NotRequired[str]
    host: NotRequired[str]
    lineageSync: NotRequired[RedshiftLineageSyncConfigurationInputTypeDef]
    port: NotRequired[int]
    storage: NotRequired[RedshiftStoragePropertiesTypeDef]

class RedshiftPropertiesOutputTypeDef(TypedDict):
    credentials: NotRequired[RedshiftCredentialsTypeDef]
    databaseName: NotRequired[str]
    isProvisionedSecret: NotRequired[bool]
    jdbcIamUrl: NotRequired[str]
    jdbcUrl: NotRequired[str]
    lineageSync: NotRequired[RedshiftLineageSyncConfigurationOutputTypeDef]
    redshiftTempDir: NotRequired[str]
    status: NotRequired[ConnectionStatusType]
    storage: NotRequired[RedshiftStoragePropertiesTypeDef]

class RedshiftPropertiesPatchTypeDef(TypedDict):
    credentials: NotRequired[RedshiftCredentialsTypeDef]
    databaseName: NotRequired[str]
    host: NotRequired[str]
    lineageSync: NotRequired[RedshiftLineageSyncConfigurationInputTypeDef]
    port: NotRequired[int]
    storage: NotRequired[RedshiftStoragePropertiesTypeDef]

class RedshiftRunConfigurationOutputTypeDef(TypedDict):
    redshiftStorage: RedshiftStorageTypeDef
    relationalFilterConfigurations: List[RelationalFilterConfigurationOutputTypeDef]
    accountId: NotRequired[str]
    dataAccessRole: NotRequired[str]
    redshiftCredentialConfiguration: NotRequired[RedshiftCredentialConfigurationTypeDef]
    region: NotRequired[str]

CreateUserProfileOutputTypeDef = TypedDict(
    "CreateUserProfileOutputTypeDef",
    {
        "details": UserProfileDetailsTypeDef,
        "domainId": str,
        "id": str,
        "status": UserProfileStatusType,
        "type": UserProfileTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetUserProfileOutputTypeDef = TypedDict(
    "GetUserProfileOutputTypeDef",
    {
        "details": UserProfileDetailsTypeDef,
        "domainId": str,
        "id": str,
        "status": UserProfileStatusType,
        "type": UserProfileTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateUserProfileOutputTypeDef = TypedDict(
    "UpdateUserProfileOutputTypeDef",
    {
        "details": UserProfileDetailsTypeDef,
        "domainId": str,
        "id": str,
        "status": UserProfileStatusType,
        "type": UserProfileTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UserProfileSummaryTypeDef = TypedDict(
    "UserProfileSummaryTypeDef",
    {
        "details": NotRequired[UserProfileDetailsTypeDef],
        "domainId": NotRequired[str],
        "id": NotRequired[str],
        "status": NotRequired[UserProfileStatusType],
        "type": NotRequired[UserProfileTypeType],
    },
)

class CreateSubscriptionRequestInputTypeDef(TypedDict):
    domainIdentifier: str
    requestReason: str
    subscribedListings: Sequence[SubscribedListingInputTypeDef]
    subscribedPrincipals: Sequence[SubscribedPrincipalInputTypeDef]
    clientToken: NotRequired[str]
    metadataForms: NotRequired[Sequence[FormInputTypeDef]]

class CreateGlossaryTermInputTypeDef(TypedDict):
    domainIdentifier: str
    glossaryIdentifier: str
    name: str
    clientToken: NotRequired[str]
    longDescription: NotRequired[str]
    shortDescription: NotRequired[str]
    status: NotRequired[GlossaryTermStatusType]
    termRelations: NotRequired[TermRelationsUnionTypeDef]

class UpdateGlossaryTermInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    glossaryIdentifier: NotRequired[str]
    longDescription: NotRequired[str]
    name: NotRequired[str]
    shortDescription: NotRequired[str]
    status: NotRequired[GlossaryTermStatusType]
    termRelations: NotRequired[TermRelationsUnionTypeDef]

class ListEnvironmentActionsOutputTypeDef(TypedDict):
    items: List[EnvironmentActionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SearchInventoryResultItemTypeDef(TypedDict):
    assetItem: NotRequired[AssetItemTypeDef]
    dataProductItem: NotRequired[DataProductResultItemTypeDef]
    glossaryItem: NotRequired[GlossaryItemTypeDef]
    glossaryTermItem: NotRequired[GlossaryTermItemTypeDef]

class SearchResultItemTypeDef(TypedDict):
    assetListing: NotRequired[AssetListingItemTypeDef]
    dataProductListing: NotRequired[DataProductListingItemTypeDef]

class ListingItemTypeDef(TypedDict):
    assetListing: NotRequired[AssetListingTypeDef]
    dataProductListing: NotRequired[DataProductListingTypeDef]

SubscribedListingTypeDef = TypedDict(
    "SubscribedListingTypeDef",
    {
        "description": str,
        "id": str,
        "item": SubscribedListingItemTypeDef,
        "name": str,
        "ownerProjectId": str,
        "ownerProjectName": NotRequired[str],
        "revision": NotRequired[str],
    },
)

class GluePropertiesPatchTypeDef(TypedDict):
    glueConnectionInput: NotRequired[GlueConnectionPatchTypeDef]

class ListEnvironmentBlueprintsOutputTypeDef(TypedDict):
    items: List[EnvironmentBlueprintSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateProjectInputTypeDef(TypedDict):
    domainIdentifier: str
    name: str
    description: NotRequired[str]
    domainUnitId: NotRequired[str]
    glossaryTerms: NotRequired[Sequence[str]]
    projectProfileId: NotRequired[str]
    userParameters: NotRequired[Sequence[EnvironmentConfigurationUserParameterUnionTypeDef]]

class UpdateProjectInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    description: NotRequired[str]
    environmentDeploymentDetails: NotRequired[EnvironmentDeploymentDetailsUnionTypeDef]
    glossaryTerms: NotRequired[Sequence[str]]
    name: NotRequired[str]
    projectProfileVersion: NotRequired[str]
    userParameters: NotRequired[Sequence[EnvironmentConfigurationUserParameterUnionTypeDef]]

class PolicyGrantPrincipalOutputTypeDef(TypedDict):
    domainUnit: NotRequired[DomainUnitPolicyGrantPrincipalOutputTypeDef]
    group: NotRequired[GroupPolicyGrantPrincipalTypeDef]
    project: NotRequired[ProjectPolicyGrantPrincipalTypeDef]
    user: NotRequired[UserPolicyGrantPrincipalOutputTypeDef]

class PolicyGrantPrincipalTypeDef(TypedDict):
    domainUnit: NotRequired[DomainUnitPolicyGrantPrincipalTypeDef]
    group: NotRequired[GroupPolicyGrantPrincipalTypeDef]
    project: NotRequired[ProjectPolicyGrantPrincipalTypeDef]
    user: NotRequired[UserPolicyGrantPrincipalTypeDef]

CreateProjectProfileOutputTypeDef = TypedDict(
    "CreateProjectProfileOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "domainUnitId": str,
        "environmentConfigurations": List[EnvironmentConfigurationOutputTypeDef],
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "status": StatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProjectProfileOutputTypeDef = TypedDict(
    "GetProjectProfileOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "domainUnitId": str,
        "environmentConfigurations": List[EnvironmentConfigurationOutputTypeDef],
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "status": StatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProjectProfileOutputTypeDef = TypedDict(
    "UpdateProjectProfileOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "domainUnitId": str,
        "environmentConfigurations": List[EnvironmentConfigurationOutputTypeDef],
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "status": StatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnvironmentConfigurationTypeDef = TypedDict(
    "EnvironmentConfigurationTypeDef",
    {
        "awsAccount": AwsAccountTypeDef,
        "awsRegion": RegionTypeDef,
        "environmentBlueprintId": str,
        "name": str,
        "configurationParameters": NotRequired[
            EnvironmentConfigurationParametersDetailsUnionTypeDef
        ],
        "deploymentMode": NotRequired[DeploymentModeType],
        "deploymentOrder": NotRequired[int],
        "description": NotRequired[str],
        "id": NotRequired[str],
    },
)

class GlueRunConfigurationInputTypeDef(TypedDict):
    relationalFilterConfigurations: Sequence[RelationalFilterConfigurationUnionTypeDef]
    autoImportDataQualityResult: NotRequired[bool]
    catalogName: NotRequired[str]
    dataAccessRole: NotRequired[str]

class RedshiftRunConfigurationInputTypeDef(TypedDict):
    relationalFilterConfigurations: Sequence[RelationalFilterConfigurationUnionTypeDef]
    dataAccessRole: NotRequired[str]
    redshiftCredentialConfiguration: NotRequired[RedshiftCredentialConfigurationTypeDef]
    redshiftStorage: NotRequired[RedshiftStorageTypeDef]

class SearchTypesOutputTypeDef(TypedDict):
    items: List[SearchTypesResultItemTypeDef]
    totalMatchCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSubscriptionGrantsOutputTypeDef(TypedDict):
    items: List[SubscriptionGrantSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListEnvironmentBlueprintConfigurationsOutputTypeDef(TypedDict):
    items: List[EnvironmentBlueprintConfigurationItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

ProvisioningConfigurationUnionTypeDef = Union[
    ProvisioningConfigurationTypeDef, ProvisioningConfigurationOutputTypeDef
]
GetJobRunOutputTypeDef = TypedDict(
    "GetJobRunOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "details": JobRunDetailsTypeDef,
        "domainId": str,
        "endTime": datetime,
        "error": JobRunErrorTypeDef,
        "id": str,
        "jobId": str,
        "jobType": Literal["LINEAGE"],
        "runMode": JobRunModeType,
        "startTime": datetime,
        "status": JobRunStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListProjectMembershipsOutputTypeDef(TypedDict):
    members: List[ProjectMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateRuleOutputTypeDef(TypedDict):
    action: RuleActionType
    createdAt: datetime
    createdBy: str
    description: str
    detail: RuleDetailOutputTypeDef
    identifier: str
    name: str
    ruleType: Literal["METADATA_FORM_ENFORCEMENT"]
    scope: RuleScopeOutputTypeDef
    target: RuleTargetTypeDef
    targetType: Literal["DOMAIN_UNIT"]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRuleOutputTypeDef(TypedDict):
    action: RuleActionType
    createdAt: datetime
    createdBy: str
    description: str
    detail: RuleDetailOutputTypeDef
    identifier: str
    lastUpdatedBy: str
    name: str
    revision: str
    ruleType: Literal["METADATA_FORM_ENFORCEMENT"]
    scope: RuleScopeOutputTypeDef
    target: RuleTargetTypeDef
    targetType: Literal["DOMAIN_UNIT"]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRuleOutputTypeDef(TypedDict):
    action: RuleActionType
    createdAt: datetime
    createdBy: str
    description: str
    detail: RuleDetailOutputTypeDef
    identifier: str
    lastUpdatedBy: str
    name: str
    revision: str
    ruleType: Literal["METADATA_FORM_ENFORCEMENT"]
    scope: RuleScopeOutputTypeDef
    target: RuleTargetTypeDef
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

RuleDetailUnionTypeDef = Union[RuleDetailTypeDef, RuleDetailOutputTypeDef]
LineageEventSummaryTypeDef = TypedDict(
    "LineageEventSummaryTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "domainId": NotRequired[str],
        "eventSummary": NotRequired[EventSummaryTypeDef],
        "eventTime": NotRequired[datetime],
        "id": NotRequired[str],
        "processingStatus": NotRequired[LineageEventProcessingStatusType],
    },
)

class RowFilterConfigurationOutputTypeDef(TypedDict):
    rowFilter: RowFilterOutputTypeDef
    sensitive: NotRequired[bool]

class RowFilterConfigurationTypeDef(TypedDict):
    rowFilter: RowFilterTypeDef
    sensitive: NotRequired[bool]

class ListNotificationsOutputTypeDef(TypedDict):
    notifications: List[NotificationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GlueConnectionTypeDef(TypedDict):
    athenaProperties: NotRequired[Dict[str, str]]
    authenticationConfiguration: NotRequired[AuthenticationConfigurationTypeDef]
    compatibleComputeEnvironments: NotRequired[List[ComputeEnvironmentsType]]
    connectionProperties: NotRequired[Dict[str, str]]
    connectionSchemaVersion: NotRequired[int]
    connectionType: NotRequired[ConnectionTypeType]
    creationTime: NotRequired[datetime]
    description: NotRequired[str]
    lastConnectionValidationTime: NotRequired[datetime]
    lastUpdatedBy: NotRequired[str]
    lastUpdatedTime: NotRequired[datetime]
    matchCriteria: NotRequired[List[str]]
    name: NotRequired[str]
    physicalConnectionRequirements: NotRequired[PhysicalConnectionRequirementsOutputTypeDef]
    pythonProperties: NotRequired[Dict[str, str]]
    sparkProperties: NotRequired[Dict[str, str]]
    status: NotRequired[ConnectionStatusType]
    statusReason: NotRequired[str]

class AuthenticationConfigurationInputTypeDef(TypedDict):
    authenticationType: NotRequired[AuthenticationTypeType]
    basicAuthenticationCredentials: NotRequired[BasicAuthenticationCredentialsTypeDef]
    customAuthenticationCredentials: NotRequired[Mapping[str, str]]
    kmsKeyArn: NotRequired[str]
    oAuth2Properties: NotRequired[OAuth2PropertiesUnionTypeDef]
    secretArn: NotRequired[str]

class ListRulesOutputTypeDef(TypedDict):
    items: List[RuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ConnectionPropertiesOutputTypeDef(TypedDict):
    athenaProperties: NotRequired[AthenaPropertiesOutputTypeDef]
    glueProperties: NotRequired[GluePropertiesOutputTypeDef]
    hyperPodProperties: NotRequired[HyperPodPropertiesOutputTypeDef]
    iamProperties: NotRequired[IamPropertiesOutputTypeDef]
    redshiftProperties: NotRequired[RedshiftPropertiesOutputTypeDef]
    sparkEmrProperties: NotRequired[SparkEmrPropertiesOutputTypeDef]
    sparkGlueProperties: NotRequired[SparkGluePropertiesOutputTypeDef]

class DataSourceConfigurationOutputTypeDef(TypedDict):
    glueRunConfiguration: NotRequired[GlueRunConfigurationOutputTypeDef]
    redshiftRunConfiguration: NotRequired[RedshiftRunConfigurationOutputTypeDef]
    sageMakerRunConfiguration: NotRequired[SageMakerRunConfigurationOutputTypeDef]

class SearchUserProfilesOutputTypeDef(TypedDict):
    items: List[UserProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SearchOutputTypeDef(TypedDict):
    items: List[SearchInventoryResultItemTypeDef]
    totalMatchCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SearchListingsOutputTypeDef(TypedDict):
    items: List[SearchResultItemTypeDef]
    totalMatchCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

GetListingOutputTypeDef = TypedDict(
    "GetListingOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "id": str,
        "item": ListingItemTypeDef,
        "listingRevision": str,
        "name": str,
        "status": ListingStatusType,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AcceptSubscriptionRequestOutputTypeDef = TypedDict(
    "AcceptSubscriptionRequestOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "decisionComment": str,
        "domainId": str,
        "existingSubscriptionId": str,
        "id": str,
        "metadataForms": List[FormOutputTypeDef],
        "requestReason": str,
        "reviewerId": str,
        "status": SubscriptionRequestStatusType,
        "subscribedListings": List[SubscribedListingTypeDef],
        "subscribedPrincipals": List[SubscribedPrincipalTypeDef],
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelSubscriptionOutputTypeDef = TypedDict(
    "CancelSubscriptionOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "id": str,
        "retainPermissions": bool,
        "status": SubscriptionStatusType,
        "subscribedListing": SubscribedListingTypeDef,
        "subscribedPrincipal": SubscribedPrincipalTypeDef,
        "subscriptionRequestId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSubscriptionRequestOutputTypeDef = TypedDict(
    "CreateSubscriptionRequestOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "decisionComment": str,
        "domainId": str,
        "existingSubscriptionId": str,
        "id": str,
        "metadataForms": List[FormOutputTypeDef],
        "requestReason": str,
        "reviewerId": str,
        "status": SubscriptionRequestStatusType,
        "subscribedListings": List[SubscribedListingTypeDef],
        "subscribedPrincipals": List[SubscribedPrincipalTypeDef],
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSubscriptionOutputTypeDef = TypedDict(
    "GetSubscriptionOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "id": str,
        "retainPermissions": bool,
        "status": SubscriptionStatusType,
        "subscribedListing": SubscribedListingTypeDef,
        "subscribedPrincipal": SubscribedPrincipalTypeDef,
        "subscriptionRequestId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSubscriptionRequestDetailsOutputTypeDef = TypedDict(
    "GetSubscriptionRequestDetailsOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "decisionComment": str,
        "domainId": str,
        "existingSubscriptionId": str,
        "id": str,
        "metadataForms": List[FormOutputTypeDef],
        "requestReason": str,
        "reviewerId": str,
        "status": SubscriptionRequestStatusType,
        "subscribedListings": List[SubscribedListingTypeDef],
        "subscribedPrincipals": List[SubscribedPrincipalTypeDef],
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RejectSubscriptionRequestOutputTypeDef = TypedDict(
    "RejectSubscriptionRequestOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "decisionComment": str,
        "domainId": str,
        "existingSubscriptionId": str,
        "id": str,
        "metadataForms": List[FormOutputTypeDef],
        "requestReason": str,
        "reviewerId": str,
        "status": SubscriptionRequestStatusType,
        "subscribedListings": List[SubscribedListingTypeDef],
        "subscribedPrincipals": List[SubscribedPrincipalTypeDef],
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RevokeSubscriptionOutputTypeDef = TypedDict(
    "RevokeSubscriptionOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "id": str,
        "retainPermissions": bool,
        "status": SubscriptionStatusType,
        "subscribedListing": SubscribedListingTypeDef,
        "subscribedPrincipal": SubscribedPrincipalTypeDef,
        "subscriptionRequestId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubscriptionRequestSummaryTypeDef = TypedDict(
    "SubscriptionRequestSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "id": str,
        "requestReason": str,
        "status": SubscriptionRequestStatusType,
        "subscribedListings": List[SubscribedListingTypeDef],
        "subscribedPrincipals": List[SubscribedPrincipalTypeDef],
        "updatedAt": datetime,
        "decisionComment": NotRequired[str],
        "existingSubscriptionId": NotRequired[str],
        "metadataFormsSummary": NotRequired[List[MetadataFormSummaryTypeDef]],
        "reviewerId": NotRequired[str],
        "updatedBy": NotRequired[str],
    },
)
SubscriptionSummaryTypeDef = TypedDict(
    "SubscriptionSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "id": str,
        "status": SubscriptionStatusType,
        "subscribedListing": SubscribedListingTypeDef,
        "subscribedPrincipal": SubscribedPrincipalTypeDef,
        "updatedAt": datetime,
        "retainPermissions": NotRequired[bool],
        "subscriptionRequestId": NotRequired[str],
        "updatedBy": NotRequired[str],
    },
)
UpdateSubscriptionRequestOutputTypeDef = TypedDict(
    "UpdateSubscriptionRequestOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "decisionComment": str,
        "domainId": str,
        "existingSubscriptionId": str,
        "id": str,
        "metadataForms": List[FormOutputTypeDef],
        "requestReason": str,
        "reviewerId": str,
        "status": SubscriptionRequestStatusType,
        "subscribedListings": List[SubscribedListingTypeDef],
        "subscribedPrincipals": List[SubscribedPrincipalTypeDef],
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ConnectionPropertiesPatchTypeDef(TypedDict):
    athenaProperties: NotRequired[AthenaPropertiesPatchTypeDef]
    glueProperties: NotRequired[GluePropertiesPatchTypeDef]
    iamProperties: NotRequired[IamPropertiesPatchTypeDef]
    redshiftProperties: NotRequired[RedshiftPropertiesPatchTypeDef]
    sparkEmrProperties: NotRequired[SparkEmrPropertiesPatchTypeDef]

class PolicyGrantMemberTypeDef(TypedDict):
    createdAt: NotRequired[datetime]
    createdBy: NotRequired[str]
    detail: NotRequired[PolicyGrantDetailOutputTypeDef]
    principal: NotRequired[PolicyGrantPrincipalOutputTypeDef]

PolicyGrantPrincipalUnionTypeDef = Union[
    PolicyGrantPrincipalTypeDef, PolicyGrantPrincipalOutputTypeDef
]
EnvironmentConfigurationUnionTypeDef = Union[
    EnvironmentConfigurationTypeDef, EnvironmentConfigurationOutputTypeDef
]

class DataSourceConfigurationInputTypeDef(TypedDict):
    glueRunConfiguration: NotRequired[GlueRunConfigurationInputTypeDef]
    redshiftRunConfiguration: NotRequired[RedshiftRunConfigurationInputTypeDef]
    sageMakerRunConfiguration: NotRequired[SageMakerRunConfigurationInputTypeDef]

class PutEnvironmentBlueprintConfigurationInputTypeDef(TypedDict):
    domainIdentifier: str
    enabledRegions: Sequence[str]
    environmentBlueprintIdentifier: str
    environmentRolePermissionBoundary: NotRequired[str]
    manageAccessRoleArn: NotRequired[str]
    provisioningConfigurations: NotRequired[Sequence[ProvisioningConfigurationUnionTypeDef]]
    provisioningRoleArn: NotRequired[str]
    regionalParameters: NotRequired[Mapping[str, Mapping[str, str]]]

class CreateRuleInputTypeDef(TypedDict):
    action: RuleActionType
    detail: RuleDetailUnionTypeDef
    domainIdentifier: str
    name: str
    scope: RuleScopeUnionTypeDef
    target: RuleTargetTypeDef
    clientToken: NotRequired[str]
    description: NotRequired[str]

class UpdateRuleInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    description: NotRequired[str]
    detail: NotRequired[RuleDetailUnionTypeDef]
    includeChildDomainUnits: NotRequired[bool]
    name: NotRequired[str]
    scope: NotRequired[RuleScopeUnionTypeDef]

class ListLineageEventsOutputTypeDef(TypedDict):
    items: List[LineageEventSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class AssetFilterConfigurationOutputTypeDef(TypedDict):
    columnConfiguration: NotRequired[ColumnFilterConfigurationOutputTypeDef]
    rowConfiguration: NotRequired[RowFilterConfigurationOutputTypeDef]

class AssetFilterConfigurationTypeDef(TypedDict):
    columnConfiguration: NotRequired[ColumnFilterConfigurationTypeDef]
    rowConfiguration: NotRequired[RowFilterConfigurationTypeDef]

class PhysicalEndpointTypeDef(TypedDict):
    awsLocation: NotRequired[AwsLocationTypeDef]
    glueConnection: NotRequired[GlueConnectionTypeDef]
    glueConnectionName: NotRequired[str]
    host: NotRequired[str]
    port: NotRequired[int]
    protocol: NotRequired[ProtocolType]
    stage: NotRequired[str]

class GlueConnectionInputTypeDef(TypedDict):
    athenaProperties: NotRequired[Mapping[str, str]]
    authenticationConfiguration: NotRequired[AuthenticationConfigurationInputTypeDef]
    connectionProperties: NotRequired[Mapping[str, str]]
    connectionType: NotRequired[GlueConnectionTypeType]
    description: NotRequired[str]
    matchCriteria: NotRequired[str]
    name: NotRequired[str]
    physicalConnectionRequirements: NotRequired[PhysicalConnectionRequirementsUnionTypeDef]
    pythonProperties: NotRequired[Mapping[str, str]]
    sparkProperties: NotRequired[Mapping[str, str]]
    validateCredentials: NotRequired[bool]
    validateForComputeEnvironments: NotRequired[Sequence[ComputeEnvironmentsType]]

CreateDataSourceOutputTypeDef = TypedDict(
    "CreateDataSourceOutputTypeDef",
    {
        "assetFormsOutput": List[FormOutputTypeDef],
        "configuration": DataSourceConfigurationOutputTypeDef,
        "connectionId": str,
        "createdAt": datetime,
        "description": str,
        "domainId": str,
        "enableSetting": EnableSettingType,
        "environmentId": str,
        "errorMessage": DataSourceErrorMessageTypeDef,
        "id": str,
        "lastRunAt": datetime,
        "lastRunErrorMessage": DataSourceErrorMessageTypeDef,
        "lastRunStatus": DataSourceRunStatusType,
        "name": str,
        "projectId": str,
        "publishOnImport": bool,
        "recommendation": RecommendationConfigurationTypeDef,
        "schedule": ScheduleConfigurationTypeDef,
        "status": DataSourceStatusType,
        "type": str,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDataSourceOutputTypeDef = TypedDict(
    "DeleteDataSourceOutputTypeDef",
    {
        "assetFormsOutput": List[FormOutputTypeDef],
        "configuration": DataSourceConfigurationOutputTypeDef,
        "connectionId": str,
        "createdAt": datetime,
        "description": str,
        "domainId": str,
        "enableSetting": EnableSettingType,
        "environmentId": str,
        "errorMessage": DataSourceErrorMessageTypeDef,
        "id": str,
        "lastRunAt": datetime,
        "lastRunErrorMessage": DataSourceErrorMessageTypeDef,
        "lastRunStatus": DataSourceRunStatusType,
        "name": str,
        "projectId": str,
        "publishOnImport": bool,
        "retainPermissionsOnRevokeFailure": bool,
        "schedule": ScheduleConfigurationTypeDef,
        "selfGrantStatus": SelfGrantStatusOutputTypeDef,
        "status": DataSourceStatusType,
        "type": str,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDataSourceOutputTypeDef = TypedDict(
    "GetDataSourceOutputTypeDef",
    {
        "assetFormsOutput": List[FormOutputTypeDef],
        "configuration": DataSourceConfigurationOutputTypeDef,
        "connectionId": str,
        "createdAt": datetime,
        "description": str,
        "domainId": str,
        "enableSetting": EnableSettingType,
        "environmentId": str,
        "errorMessage": DataSourceErrorMessageTypeDef,
        "id": str,
        "lastRunAssetCount": int,
        "lastRunAt": datetime,
        "lastRunErrorMessage": DataSourceErrorMessageTypeDef,
        "lastRunStatus": DataSourceRunStatusType,
        "name": str,
        "projectId": str,
        "publishOnImport": bool,
        "recommendation": RecommendationConfigurationTypeDef,
        "schedule": ScheduleConfigurationTypeDef,
        "selfGrantStatus": SelfGrantStatusOutputTypeDef,
        "status": DataSourceStatusType,
        "type": str,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDataSourceOutputTypeDef = TypedDict(
    "UpdateDataSourceOutputTypeDef",
    {
        "assetFormsOutput": List[FormOutputTypeDef],
        "configuration": DataSourceConfigurationOutputTypeDef,
        "connectionId": str,
        "createdAt": datetime,
        "description": str,
        "domainId": str,
        "enableSetting": EnableSettingType,
        "environmentId": str,
        "errorMessage": DataSourceErrorMessageTypeDef,
        "id": str,
        "lastRunAt": datetime,
        "lastRunErrorMessage": DataSourceErrorMessageTypeDef,
        "lastRunStatus": DataSourceRunStatusType,
        "name": str,
        "projectId": str,
        "publishOnImport": bool,
        "recommendation": RecommendationConfigurationTypeDef,
        "retainPermissionsOnRevokeFailure": bool,
        "schedule": ScheduleConfigurationTypeDef,
        "selfGrantStatus": SelfGrantStatusOutputTypeDef,
        "status": DataSourceStatusType,
        "type": str,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListSubscriptionRequestsOutputTypeDef(TypedDict):
    items: List[SubscriptionRequestSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSubscriptionsOutputTypeDef(TypedDict):
    items: List[SubscriptionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateConnectionInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    awsLocation: NotRequired[AwsLocationTypeDef]
    description: NotRequired[str]
    props: NotRequired[ConnectionPropertiesPatchTypeDef]

class ListPolicyGrantsOutputTypeDef(TypedDict):
    grantList: List[PolicyGrantMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class AddPolicyGrantInputTypeDef(TypedDict):
    detail: PolicyGrantDetailUnionTypeDef
    domainIdentifier: str
    entityIdentifier: str
    entityType: TargetEntityTypeType
    policyType: ManagedPolicyTypeType
    principal: PolicyGrantPrincipalUnionTypeDef
    clientToken: NotRequired[str]

class RemovePolicyGrantInputTypeDef(TypedDict):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TargetEntityTypeType
    policyType: ManagedPolicyTypeType
    principal: PolicyGrantPrincipalUnionTypeDef
    clientToken: NotRequired[str]

class CreateProjectProfileInputTypeDef(TypedDict):
    domainIdentifier: str
    name: str
    description: NotRequired[str]
    domainUnitIdentifier: NotRequired[str]
    environmentConfigurations: NotRequired[Sequence[EnvironmentConfigurationUnionTypeDef]]
    status: NotRequired[StatusType]

class UpdateProjectProfileInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    description: NotRequired[str]
    domainUnitIdentifier: NotRequired[str]
    environmentConfigurations: NotRequired[Sequence[EnvironmentConfigurationUnionTypeDef]]
    name: NotRequired[str]
    status: NotRequired[StatusType]

CreateDataSourceInputTypeDef = TypedDict(
    "CreateDataSourceInputTypeDef",
    {
        "domainIdentifier": str,
        "name": str,
        "projectIdentifier": str,
        "type": str,
        "assetFormsInput": NotRequired[Sequence[FormInputTypeDef]],
        "clientToken": NotRequired[str],
        "configuration": NotRequired[DataSourceConfigurationInputTypeDef],
        "connectionIdentifier": NotRequired[str],
        "description": NotRequired[str],
        "enableSetting": NotRequired[EnableSettingType],
        "environmentIdentifier": NotRequired[str],
        "publishOnImport": NotRequired[bool],
        "recommendation": NotRequired[RecommendationConfigurationTypeDef],
        "schedule": NotRequired[ScheduleConfigurationTypeDef],
    },
)

class UpdateDataSourceInputTypeDef(TypedDict):
    domainIdentifier: str
    identifier: str
    assetFormsInput: NotRequired[Sequence[FormInputTypeDef]]
    configuration: NotRequired[DataSourceConfigurationInputTypeDef]
    description: NotRequired[str]
    enableSetting: NotRequired[EnableSettingType]
    name: NotRequired[str]
    publishOnImport: NotRequired[bool]
    recommendation: NotRequired[RecommendationConfigurationTypeDef]
    retainPermissionsOnRevokeFailure: NotRequired[bool]
    schedule: NotRequired[ScheduleConfigurationTypeDef]

CreateAssetFilterOutputTypeDef = TypedDict(
    "CreateAssetFilterOutputTypeDef",
    {
        "assetId": str,
        "configuration": AssetFilterConfigurationOutputTypeDef,
        "createdAt": datetime,
        "description": str,
        "domainId": str,
        "effectiveColumnNames": List[str],
        "effectiveRowFilter": str,
        "errorMessage": str,
        "id": str,
        "name": str,
        "status": FilterStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAssetFilterOutputTypeDef = TypedDict(
    "GetAssetFilterOutputTypeDef",
    {
        "assetId": str,
        "configuration": AssetFilterConfigurationOutputTypeDef,
        "createdAt": datetime,
        "description": str,
        "domainId": str,
        "effectiveColumnNames": List[str],
        "effectiveRowFilter": str,
        "errorMessage": str,
        "id": str,
        "name": str,
        "status": FilterStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAssetFilterOutputTypeDef = TypedDict(
    "UpdateAssetFilterOutputTypeDef",
    {
        "assetId": str,
        "configuration": AssetFilterConfigurationOutputTypeDef,
        "createdAt": datetime,
        "description": str,
        "domainId": str,
        "effectiveColumnNames": List[str],
        "effectiveRowFilter": str,
        "errorMessage": str,
        "id": str,
        "name": str,
        "status": FilterStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssetFilterConfigurationUnionTypeDef = Union[
    AssetFilterConfigurationTypeDef, AssetFilterConfigurationOutputTypeDef
]
ConnectionSummaryTypeDef = TypedDict(
    "ConnectionSummaryTypeDef",
    {
        "connectionId": str,
        "domainId": str,
        "domainUnitId": str,
        "name": str,
        "physicalEndpoints": List[PhysicalEndpointTypeDef],
        "type": ConnectionTypeType,
        "environmentId": NotRequired[str],
        "projectId": NotRequired[str],
        "props": NotRequired[ConnectionPropertiesOutputTypeDef],
    },
)
CreateConnectionOutputTypeDef = TypedDict(
    "CreateConnectionOutputTypeDef",
    {
        "connectionId": str,
        "description": str,
        "domainId": str,
        "domainUnitId": str,
        "environmentId": str,
        "name": str,
        "physicalEndpoints": List[PhysicalEndpointTypeDef],
        "projectId": str,
        "props": ConnectionPropertiesOutputTypeDef,
        "type": ConnectionTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConnectionOutputTypeDef = TypedDict(
    "GetConnectionOutputTypeDef",
    {
        "connectionCredentials": ConnectionCredentialsTypeDef,
        "connectionId": str,
        "description": str,
        "domainId": str,
        "domainUnitId": str,
        "environmentId": str,
        "environmentUserRole": str,
        "name": str,
        "physicalEndpoints": List[PhysicalEndpointTypeDef],
        "projectId": str,
        "props": ConnectionPropertiesOutputTypeDef,
        "type": ConnectionTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateConnectionOutputTypeDef = TypedDict(
    "UpdateConnectionOutputTypeDef",
    {
        "connectionId": str,
        "description": str,
        "domainId": str,
        "domainUnitId": str,
        "environmentId": str,
        "name": str,
        "physicalEndpoints": List[PhysicalEndpointTypeDef],
        "projectId": str,
        "props": ConnectionPropertiesOutputTypeDef,
        "type": ConnectionTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GluePropertiesInputTypeDef(TypedDict):
    glueConnectionInput: NotRequired[GlueConnectionInputTypeDef]

class CreateAssetFilterInputTypeDef(TypedDict):
    assetIdentifier: str
    configuration: AssetFilterConfigurationUnionTypeDef
    domainIdentifier: str
    name: str
    clientToken: NotRequired[str]
    description: NotRequired[str]

class UpdateAssetFilterInputTypeDef(TypedDict):
    assetIdentifier: str
    domainIdentifier: str
    identifier: str
    configuration: NotRequired[AssetFilterConfigurationUnionTypeDef]
    description: NotRequired[str]
    name: NotRequired[str]

class ListConnectionsOutputTypeDef(TypedDict):
    items: List[ConnectionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ConnectionPropertiesInputTypeDef(TypedDict):
    athenaProperties: NotRequired[AthenaPropertiesInputTypeDef]
    glueProperties: NotRequired[GluePropertiesInputTypeDef]
    hyperPodProperties: NotRequired[HyperPodPropertiesInputTypeDef]
    iamProperties: NotRequired[IamPropertiesInputTypeDef]
    redshiftProperties: NotRequired[RedshiftPropertiesInputTypeDef]
    sparkEmrProperties: NotRequired[SparkEmrPropertiesInputTypeDef]
    sparkGlueProperties: NotRequired[SparkGluePropertiesInputTypeDef]

class CreateConnectionInputTypeDef(TypedDict):
    domainIdentifier: str
    environmentIdentifier: str
    name: str
    awsLocation: NotRequired[AwsLocationTypeDef]
    clientToken: NotRequired[str]
    description: NotRequired[str]
    props: NotRequired[ConnectionPropertiesInputTypeDef]
