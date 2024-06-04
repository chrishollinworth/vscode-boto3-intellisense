"""
Type annotations for datazone service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/type_defs.html)

Usage::

    ```python
    from mypy_boto3_datazone.type_defs import AcceptChoiceTypeDef

    data: AcceptChoiceTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AcceptRuleBehaviorType,
    AuthTypeType,
    ChangeActionType,
    ConfigurableActionTypeAuthorizationType,
    DataAssetActivityStatusType,
    DataSourceErrorTypeType,
    DataSourceRunStatusType,
    DataSourceRunTypeType,
    DataSourceStatusType,
    DeploymentStatusType,
    DeploymentTypeType,
    DomainStatusType,
    EnableSettingType,
    EnvironmentStatusType,
    FilterExpressionTypeType,
    FormTypeStatusType,
    GlossaryStatusType,
    GlossaryTermStatusType,
    GroupProfileStatusType,
    GroupSearchTypeType,
    InventorySearchScopeType,
    ListingStatusType,
    MetadataGenerationRunStatusType,
    NotificationRoleType,
    NotificationTypeType,
    ProjectStatusType,
    RejectRuleBehaviorType,
    SearchOutputAdditionalAttributeType,
    SortKeyType,
    SortOrderType,
    SubscriptionGrantOverallStatusType,
    SubscriptionGrantStatusType,
    SubscriptionRequestStatusType,
    SubscriptionStatusType,
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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AcceptChoiceTypeDef",
    "AcceptPredictionsInputRequestTypeDef",
    "AcceptPredictionsOutputTypeDef",
    "AcceptRuleTypeDef",
    "AcceptSubscriptionRequestInputRequestTypeDef",
    "AcceptSubscriptionRequestOutputTypeDef",
    "AssetItemAdditionalAttributesTypeDef",
    "AssetItemTypeDef",
    "AssetListingDetailsTypeDef",
    "AssetListingItemAdditionalAttributesTypeDef",
    "AssetListingItemTypeDef",
    "AssetListingTypeDef",
    "AssetRevisionTypeDef",
    "AssetTargetNameMapTypeDef",
    "AssetTypeItemTypeDef",
    "BusinessNameGenerationConfigurationTypeDef",
    "CancelMetadataGenerationRunInputRequestTypeDef",
    "CancelSubscriptionInputRequestTypeDef",
    "CancelSubscriptionOutputTypeDef",
    "CloudFormationPropertiesTypeDef",
    "ConfigurableActionParameterTypeDef",
    "ConfigurableEnvironmentActionTypeDef",
    "CreateAssetInputRequestTypeDef",
    "CreateAssetOutputTypeDef",
    "CreateAssetRevisionInputRequestTypeDef",
    "CreateAssetRevisionOutputTypeDef",
    "CreateAssetTypeInputRequestTypeDef",
    "CreateAssetTypeOutputTypeDef",
    "CreateDataSourceInputRequestTypeDef",
    "CreateDataSourceOutputTypeDef",
    "CreateDomainInputRequestTypeDef",
    "CreateDomainOutputTypeDef",
    "CreateEnvironmentInputRequestTypeDef",
    "CreateEnvironmentOutputTypeDef",
    "CreateEnvironmentProfileInputRequestTypeDef",
    "CreateEnvironmentProfileOutputTypeDef",
    "CreateFormTypeInputRequestTypeDef",
    "CreateFormTypeOutputTypeDef",
    "CreateGlossaryInputRequestTypeDef",
    "CreateGlossaryOutputTypeDef",
    "CreateGlossaryTermInputRequestTypeDef",
    "CreateGlossaryTermOutputTypeDef",
    "CreateGroupProfileInputRequestTypeDef",
    "CreateGroupProfileOutputTypeDef",
    "CreateListingChangeSetInputRequestTypeDef",
    "CreateListingChangeSetOutputTypeDef",
    "CreateProjectInputRequestTypeDef",
    "CreateProjectMembershipInputRequestTypeDef",
    "CreateProjectOutputTypeDef",
    "CreateSubscriptionGrantInputRequestTypeDef",
    "CreateSubscriptionGrantOutputTypeDef",
    "CreateSubscriptionRequestInputRequestTypeDef",
    "CreateSubscriptionRequestOutputTypeDef",
    "CreateSubscriptionTargetInputRequestTypeDef",
    "CreateSubscriptionTargetOutputTypeDef",
    "CreateUserProfileInputRequestTypeDef",
    "CreateUserProfileOutputTypeDef",
    "CustomParameterTypeDef",
    "DataProductItemTypeDef",
    "DataProductSummaryTypeDef",
    "DataSourceConfigurationInputTypeDef",
    "DataSourceConfigurationOutputTypeDef",
    "DataSourceErrorMessageTypeDef",
    "DataSourceRunActivityTypeDef",
    "DataSourceRunSummaryTypeDef",
    "DataSourceSummaryTypeDef",
    "DeleteAssetInputRequestTypeDef",
    "DeleteAssetTypeInputRequestTypeDef",
    "DeleteDataSourceInputRequestTypeDef",
    "DeleteDataSourceOutputTypeDef",
    "DeleteDomainInputRequestTypeDef",
    "DeleteDomainOutputTypeDef",
    "DeleteEnvironmentBlueprintConfigurationInputRequestTypeDef",
    "DeleteEnvironmentInputRequestTypeDef",
    "DeleteEnvironmentProfileInputRequestTypeDef",
    "DeleteFormTypeInputRequestTypeDef",
    "DeleteGlossaryInputRequestTypeDef",
    "DeleteGlossaryTermInputRequestTypeDef",
    "DeleteListingInputRequestTypeDef",
    "DeleteProjectInputRequestTypeDef",
    "DeleteProjectMembershipInputRequestTypeDef",
    "DeleteSubscriptionGrantInputRequestTypeDef",
    "DeleteSubscriptionGrantOutputTypeDef",
    "DeleteSubscriptionRequestInputRequestTypeDef",
    "DeleteSubscriptionTargetInputRequestTypeDef",
    "DeleteTimeSeriesDataPointsInputRequestTypeDef",
    "DeploymentPropertiesTypeDef",
    "DeploymentTypeDef",
    "DetailedGlossaryTermTypeDef",
    "DomainSummaryTypeDef",
    "EnvironmentBlueprintConfigurationItemTypeDef",
    "EnvironmentBlueprintSummaryTypeDef",
    "EnvironmentErrorTypeDef",
    "EnvironmentParameterTypeDef",
    "EnvironmentProfileSummaryTypeDef",
    "EnvironmentSummaryTypeDef",
    "FailureCauseTypeDef",
    "FilterClauseTypeDef",
    "FilterExpressionTypeDef",
    "FilterTypeDef",
    "FormEntryInputTypeDef",
    "FormEntryOutputTypeDef",
    "FormInputTypeDef",
    "FormOutputTypeDef",
    "FormTypeDataTypeDef",
    "GetAssetInputRequestTypeDef",
    "GetAssetOutputTypeDef",
    "GetAssetTypeInputRequestTypeDef",
    "GetAssetTypeOutputTypeDef",
    "GetDataSourceInputRequestTypeDef",
    "GetDataSourceOutputTypeDef",
    "GetDataSourceRunInputRequestTypeDef",
    "GetDataSourceRunOutputTypeDef",
    "GetDomainInputRequestTypeDef",
    "GetDomainOutputTypeDef",
    "GetEnvironmentBlueprintConfigurationInputRequestTypeDef",
    "GetEnvironmentBlueprintConfigurationOutputTypeDef",
    "GetEnvironmentBlueprintInputRequestTypeDef",
    "GetEnvironmentBlueprintOutputTypeDef",
    "GetEnvironmentInputRequestTypeDef",
    "GetEnvironmentOutputTypeDef",
    "GetEnvironmentProfileInputRequestTypeDef",
    "GetEnvironmentProfileOutputTypeDef",
    "GetFormTypeInputRequestTypeDef",
    "GetFormTypeOutputTypeDef",
    "GetGlossaryInputRequestTypeDef",
    "GetGlossaryOutputTypeDef",
    "GetGlossaryTermInputRequestTypeDef",
    "GetGlossaryTermOutputTypeDef",
    "GetGroupProfileInputRequestTypeDef",
    "GetGroupProfileOutputTypeDef",
    "GetIamPortalLoginUrlInputRequestTypeDef",
    "GetIamPortalLoginUrlOutputTypeDef",
    "GetListingInputRequestTypeDef",
    "GetListingOutputTypeDef",
    "GetMetadataGenerationRunInputRequestTypeDef",
    "GetMetadataGenerationRunOutputTypeDef",
    "GetProjectInputRequestTypeDef",
    "GetProjectOutputTypeDef",
    "GetSubscriptionGrantInputRequestTypeDef",
    "GetSubscriptionGrantOutputTypeDef",
    "GetSubscriptionInputRequestTypeDef",
    "GetSubscriptionOutputTypeDef",
    "GetSubscriptionRequestDetailsInputRequestTypeDef",
    "GetSubscriptionRequestDetailsOutputTypeDef",
    "GetSubscriptionTargetInputRequestTypeDef",
    "GetSubscriptionTargetOutputTypeDef",
    "GetTimeSeriesDataPointInputRequestTypeDef",
    "GetTimeSeriesDataPointOutputTypeDef",
    "GetUserProfileInputRequestTypeDef",
    "GetUserProfileOutputTypeDef",
    "GlossaryItemTypeDef",
    "GlossaryTermItemTypeDef",
    "GlueRunConfigurationInputTypeDef",
    "GlueRunConfigurationOutputTypeDef",
    "GrantedEntityInputTypeDef",
    "GrantedEntityTypeDef",
    "GroupDetailsTypeDef",
    "GroupProfileSummaryTypeDef",
    "IamUserProfileDetailsTypeDef",
    "ImportTypeDef",
    "ListAssetRevisionsInputRequestTypeDef",
    "ListAssetRevisionsOutputTypeDef",
    "ListDataSourceRunActivitiesInputRequestTypeDef",
    "ListDataSourceRunActivitiesOutputTypeDef",
    "ListDataSourceRunsInputRequestTypeDef",
    "ListDataSourceRunsOutputTypeDef",
    "ListDataSourcesInputRequestTypeDef",
    "ListDataSourcesOutputTypeDef",
    "ListDomainsInputRequestTypeDef",
    "ListDomainsOutputTypeDef",
    "ListEnvironmentBlueprintConfigurationsInputRequestTypeDef",
    "ListEnvironmentBlueprintConfigurationsOutputTypeDef",
    "ListEnvironmentBlueprintsInputRequestTypeDef",
    "ListEnvironmentBlueprintsOutputTypeDef",
    "ListEnvironmentProfilesInputRequestTypeDef",
    "ListEnvironmentProfilesOutputTypeDef",
    "ListEnvironmentsInputRequestTypeDef",
    "ListEnvironmentsOutputTypeDef",
    "ListMetadataGenerationRunsInputRequestTypeDef",
    "ListMetadataGenerationRunsOutputTypeDef",
    "ListNotificationsInputRequestTypeDef",
    "ListNotificationsOutputTypeDef",
    "ListProjectMembershipsInputRequestTypeDef",
    "ListProjectMembershipsOutputTypeDef",
    "ListProjectsInputRequestTypeDef",
    "ListProjectsOutputTypeDef",
    "ListSubscriptionGrantsInputRequestTypeDef",
    "ListSubscriptionGrantsOutputTypeDef",
    "ListSubscriptionRequestsInputRequestTypeDef",
    "ListSubscriptionRequestsOutputTypeDef",
    "ListSubscriptionTargetsInputRequestTypeDef",
    "ListSubscriptionTargetsOutputTypeDef",
    "ListSubscriptionsInputRequestTypeDef",
    "ListSubscriptionsOutputTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTimeSeriesDataPointsInputRequestTypeDef",
    "ListTimeSeriesDataPointsOutputTypeDef",
    "ListingItemTypeDef",
    "ListingRevisionInputTypeDef",
    "ListingRevisionTypeDef",
    "MemberDetailsTypeDef",
    "MemberTypeDef",
    "MetadataGenerationRunItemTypeDef",
    "MetadataGenerationRunTargetTypeDef",
    "ModelTypeDef",
    "NotificationOutputTypeDef",
    "NotificationResourceTypeDef",
    "PaginatorConfigTypeDef",
    "PostTimeSeriesDataPointsInputRequestTypeDef",
    "PostTimeSeriesDataPointsOutputTypeDef",
    "PredictionConfigurationTypeDef",
    "ProjectDeletionErrorTypeDef",
    "ProjectMemberTypeDef",
    "ProjectSummaryTypeDef",
    "ProvisioningPropertiesTypeDef",
    "PutEnvironmentBlueprintConfigurationInputRequestTypeDef",
    "PutEnvironmentBlueprintConfigurationOutputTypeDef",
    "RecommendationConfigurationTypeDef",
    "RedshiftClusterStorageTypeDef",
    "RedshiftCredentialConfigurationTypeDef",
    "RedshiftRunConfigurationInputTypeDef",
    "RedshiftRunConfigurationOutputTypeDef",
    "RedshiftServerlessStorageTypeDef",
    "RedshiftStorageTypeDef",
    "RejectChoiceTypeDef",
    "RejectPredictionsInputRequestTypeDef",
    "RejectPredictionsOutputTypeDef",
    "RejectRuleTypeDef",
    "RejectSubscriptionRequestInputRequestTypeDef",
    "RejectSubscriptionRequestOutputTypeDef",
    "RelationalFilterConfigurationTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeSubscriptionInputRequestTypeDef",
    "RevokeSubscriptionOutputTypeDef",
    "RunStatisticsForAssetsTypeDef",
    "ScheduleConfigurationTypeDef",
    "SearchGroupProfilesInputRequestTypeDef",
    "SearchGroupProfilesOutputTypeDef",
    "SearchInItemTypeDef",
    "SearchInputRequestTypeDef",
    "SearchInventoryResultItemTypeDef",
    "SearchListingsInputRequestTypeDef",
    "SearchListingsOutputTypeDef",
    "SearchOutputTypeDef",
    "SearchResultItemTypeDef",
    "SearchSortTypeDef",
    "SearchTypesInputRequestTypeDef",
    "SearchTypesOutputTypeDef",
    "SearchTypesResultItemTypeDef",
    "SearchUserProfilesInputRequestTypeDef",
    "SearchUserProfilesOutputTypeDef",
    "SingleSignOnTypeDef",
    "SsoUserProfileDetailsTypeDef",
    "StartDataSourceRunInputRequestTypeDef",
    "StartDataSourceRunOutputTypeDef",
    "StartMetadataGenerationRunInputRequestTypeDef",
    "StartMetadataGenerationRunOutputTypeDef",
    "SubscribedAssetListingTypeDef",
    "SubscribedAssetTypeDef",
    "SubscribedListingInputTypeDef",
    "SubscribedListingItemTypeDef",
    "SubscribedListingTypeDef",
    "SubscribedPrincipalInputTypeDef",
    "SubscribedPrincipalTypeDef",
    "SubscribedProjectInputTypeDef",
    "SubscribedProjectTypeDef",
    "SubscriptionGrantSummaryTypeDef",
    "SubscriptionRequestSummaryTypeDef",
    "SubscriptionSummaryTypeDef",
    "SubscriptionTargetFormTypeDef",
    "SubscriptionTargetSummaryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TermRelationsTypeDef",
    "TimeSeriesDataPointFormInputTypeDef",
    "TimeSeriesDataPointFormOutputTypeDef",
    "TimeSeriesDataPointSummaryFormOutputTypeDef",
    "TopicTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDataSourceInputRequestTypeDef",
    "UpdateDataSourceOutputTypeDef",
    "UpdateDomainInputRequestTypeDef",
    "UpdateDomainOutputTypeDef",
    "UpdateEnvironmentInputRequestTypeDef",
    "UpdateEnvironmentOutputTypeDef",
    "UpdateEnvironmentProfileInputRequestTypeDef",
    "UpdateEnvironmentProfileOutputTypeDef",
    "UpdateGlossaryInputRequestTypeDef",
    "UpdateGlossaryOutputTypeDef",
    "UpdateGlossaryTermInputRequestTypeDef",
    "UpdateGlossaryTermOutputTypeDef",
    "UpdateGroupProfileInputRequestTypeDef",
    "UpdateGroupProfileOutputTypeDef",
    "UpdateProjectInputRequestTypeDef",
    "UpdateProjectOutputTypeDef",
    "UpdateSubscriptionGrantStatusInputRequestTypeDef",
    "UpdateSubscriptionGrantStatusOutputTypeDef",
    "UpdateSubscriptionRequestInputRequestTypeDef",
    "UpdateSubscriptionRequestOutputTypeDef",
    "UpdateSubscriptionTargetInputRequestTypeDef",
    "UpdateSubscriptionTargetOutputTypeDef",
    "UpdateUserProfileInputRequestTypeDef",
    "UpdateUserProfileOutputTypeDef",
    "UserDetailsTypeDef",
    "UserProfileDetailsTypeDef",
    "UserProfileSummaryTypeDef",
)

_RequiredAcceptChoiceTypeDef = TypedDict(
    "_RequiredAcceptChoiceTypeDef",
    {
        "predictionTarget": str,
    },
)
_OptionalAcceptChoiceTypeDef = TypedDict(
    "_OptionalAcceptChoiceTypeDef",
    {
        "editedValue": str,
        "predictionChoice": int,
    },
    total=False,
)

class AcceptChoiceTypeDef(_RequiredAcceptChoiceTypeDef, _OptionalAcceptChoiceTypeDef):
    pass

_RequiredAcceptPredictionsInputRequestTypeDef = TypedDict(
    "_RequiredAcceptPredictionsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
_OptionalAcceptPredictionsInputRequestTypeDef = TypedDict(
    "_OptionalAcceptPredictionsInputRequestTypeDef",
    {
        "acceptChoices": List["AcceptChoiceTypeDef"],
        "acceptRule": "AcceptRuleTypeDef",
        "clientToken": str,
        "revision": str,
    },
    total=False,
)

class AcceptPredictionsInputRequestTypeDef(
    _RequiredAcceptPredictionsInputRequestTypeDef, _OptionalAcceptPredictionsInputRequestTypeDef
):
    pass

AcceptPredictionsOutputTypeDef = TypedDict(
    "AcceptPredictionsOutputTypeDef",
    {
        "assetId": str,
        "domainId": str,
        "revision": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AcceptRuleTypeDef = TypedDict(
    "AcceptRuleTypeDef",
    {
        "rule": AcceptRuleBehaviorType,
        "threshold": float,
    },
    total=False,
)

_RequiredAcceptSubscriptionRequestInputRequestTypeDef = TypedDict(
    "_RequiredAcceptSubscriptionRequestInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
_OptionalAcceptSubscriptionRequestInputRequestTypeDef = TypedDict(
    "_OptionalAcceptSubscriptionRequestInputRequestTypeDef",
    {
        "decisionComment": str,
    },
    total=False,
)

class AcceptSubscriptionRequestInputRequestTypeDef(
    _RequiredAcceptSubscriptionRequestInputRequestTypeDef,
    _OptionalAcceptSubscriptionRequestInputRequestTypeDef,
):
    pass

AcceptSubscriptionRequestOutputTypeDef = TypedDict(
    "AcceptSubscriptionRequestOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "decisionComment": str,
        "domainId": str,
        "id": str,
        "requestReason": str,
        "reviewerId": str,
        "status": SubscriptionRequestStatusType,
        "subscribedListings": List["SubscribedListingTypeDef"],
        "subscribedPrincipals": List["SubscribedPrincipalTypeDef"],
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssetItemAdditionalAttributesTypeDef = TypedDict(
    "AssetItemAdditionalAttributesTypeDef",
    {
        "formsOutput": List["FormOutputTypeDef"],
        "latestTimeSeriesDataPointFormsOutput": List["TimeSeriesDataPointSummaryFormOutputTypeDef"],
        "readOnlyFormsOutput": List["FormOutputTypeDef"],
    },
    total=False,
)

_RequiredAssetItemTypeDef = TypedDict(
    "_RequiredAssetItemTypeDef",
    {
        "domainId": str,
        "identifier": str,
        "name": str,
        "owningProjectId": str,
        "typeIdentifier": str,
        "typeRevision": str,
    },
)
_OptionalAssetItemTypeDef = TypedDict(
    "_OptionalAssetItemTypeDef",
    {
        "additionalAttributes": "AssetItemAdditionalAttributesTypeDef",
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "externalIdentifier": str,
        "firstRevisionCreatedAt": datetime,
        "firstRevisionCreatedBy": str,
        "glossaryTerms": List[str],
    },
    total=False,
)

class AssetItemTypeDef(_RequiredAssetItemTypeDef, _OptionalAssetItemTypeDef):
    pass

AssetListingDetailsTypeDef = TypedDict(
    "AssetListingDetailsTypeDef",
    {
        "listingId": str,
        "listingStatus": ListingStatusType,
    },
)

AssetListingItemAdditionalAttributesTypeDef = TypedDict(
    "AssetListingItemAdditionalAttributesTypeDef",
    {
        "forms": str,
        "latestTimeSeriesDataPointForms": List["TimeSeriesDataPointSummaryFormOutputTypeDef"],
    },
    total=False,
)

AssetListingItemTypeDef = TypedDict(
    "AssetListingItemTypeDef",
    {
        "additionalAttributes": "AssetListingItemAdditionalAttributesTypeDef",
        "createdAt": datetime,
        "description": str,
        "entityId": str,
        "entityRevision": str,
        "entityType": str,
        "glossaryTerms": List["DetailedGlossaryTermTypeDef"],
        "listingCreatedBy": str,
        "listingId": str,
        "listingRevision": str,
        "listingUpdatedBy": str,
        "name": str,
        "owningProjectId": str,
    },
    total=False,
)

AssetListingTypeDef = TypedDict(
    "AssetListingTypeDef",
    {
        "assetId": str,
        "assetRevision": str,
        "assetType": str,
        "createdAt": datetime,
        "forms": str,
        "glossaryTerms": List["DetailedGlossaryTermTypeDef"],
        "latestTimeSeriesDataPointForms": List["TimeSeriesDataPointSummaryFormOutputTypeDef"],
        "owningProjectId": str,
    },
    total=False,
)

AssetRevisionTypeDef = TypedDict(
    "AssetRevisionTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "id": str,
        "revision": str,
    },
    total=False,
)

AssetTargetNameMapTypeDef = TypedDict(
    "AssetTargetNameMapTypeDef",
    {
        "assetId": str,
        "targetName": str,
    },
)

_RequiredAssetTypeItemTypeDef = TypedDict(
    "_RequiredAssetTypeItemTypeDef",
    {
        "domainId": str,
        "formsOutput": Dict[str, "FormEntryOutputTypeDef"],
        "name": str,
        "owningProjectId": str,
        "revision": str,
    },
)
_OptionalAssetTypeItemTypeDef = TypedDict(
    "_OptionalAssetTypeItemTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "originDomainId": str,
        "originProjectId": str,
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

class AssetTypeItemTypeDef(_RequiredAssetTypeItemTypeDef, _OptionalAssetTypeItemTypeDef):
    pass

BusinessNameGenerationConfigurationTypeDef = TypedDict(
    "BusinessNameGenerationConfigurationTypeDef",
    {
        "enabled": bool,
    },
    total=False,
)

CancelMetadataGenerationRunInputRequestTypeDef = TypedDict(
    "CancelMetadataGenerationRunInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)

CancelSubscriptionInputRequestTypeDef = TypedDict(
    "CancelSubscriptionInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
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
        "subscribedListing": "SubscribedListingTypeDef",
        "subscribedPrincipal": "SubscribedPrincipalTypeDef",
        "subscriptionRequestId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CloudFormationPropertiesTypeDef = TypedDict(
    "CloudFormationPropertiesTypeDef",
    {
        "templateUrl": str,
    },
)

ConfigurableActionParameterTypeDef = TypedDict(
    "ConfigurableActionParameterTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

_RequiredConfigurableEnvironmentActionTypeDef = TypedDict(
    "_RequiredConfigurableEnvironmentActionTypeDef",
    {
        "parameters": List["ConfigurableActionParameterTypeDef"],
        "type": str,
    },
)
_OptionalConfigurableEnvironmentActionTypeDef = TypedDict(
    "_OptionalConfigurableEnvironmentActionTypeDef",
    {
        "auth": ConfigurableActionTypeAuthorizationType,
    },
    total=False,
)

class ConfigurableEnvironmentActionTypeDef(
    _RequiredConfigurableEnvironmentActionTypeDef, _OptionalConfigurableEnvironmentActionTypeDef
):
    pass

_RequiredCreateAssetInputRequestTypeDef = TypedDict(
    "_RequiredCreateAssetInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "name": str,
        "owningProjectIdentifier": str,
        "typeIdentifier": str,
    },
)
_OptionalCreateAssetInputRequestTypeDef = TypedDict(
    "_OptionalCreateAssetInputRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "externalIdentifier": str,
        "formsInput": List["FormInputTypeDef"],
        "glossaryTerms": List[str],
        "predictionConfiguration": "PredictionConfigurationTypeDef",
        "typeRevision": str,
    },
    total=False,
)

class CreateAssetInputRequestTypeDef(
    _RequiredCreateAssetInputRequestTypeDef, _OptionalCreateAssetInputRequestTypeDef
):
    pass

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
        "formsOutput": List["FormOutputTypeDef"],
        "glossaryTerms": List[str],
        "id": str,
        "latestTimeSeriesDataPointFormsOutput": List["TimeSeriesDataPointSummaryFormOutputTypeDef"],
        "listing": "AssetListingDetailsTypeDef",
        "name": str,
        "owningProjectId": str,
        "predictionConfiguration": "PredictionConfigurationTypeDef",
        "readOnlyFormsOutput": List["FormOutputTypeDef"],
        "revision": str,
        "typeIdentifier": str,
        "typeRevision": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAssetRevisionInputRequestTypeDef = TypedDict(
    "_RequiredCreateAssetRevisionInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "name": str,
    },
)
_OptionalCreateAssetRevisionInputRequestTypeDef = TypedDict(
    "_OptionalCreateAssetRevisionInputRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "formsInput": List["FormInputTypeDef"],
        "glossaryTerms": List[str],
        "predictionConfiguration": "PredictionConfigurationTypeDef",
        "typeRevision": str,
    },
    total=False,
)

class CreateAssetRevisionInputRequestTypeDef(
    _RequiredCreateAssetRevisionInputRequestTypeDef, _OptionalCreateAssetRevisionInputRequestTypeDef
):
    pass

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
        "formsOutput": List["FormOutputTypeDef"],
        "glossaryTerms": List[str],
        "id": str,
        "latestTimeSeriesDataPointFormsOutput": List["TimeSeriesDataPointSummaryFormOutputTypeDef"],
        "listing": "AssetListingDetailsTypeDef",
        "name": str,
        "owningProjectId": str,
        "predictionConfiguration": "PredictionConfigurationTypeDef",
        "readOnlyFormsOutput": List["FormOutputTypeDef"],
        "revision": str,
        "typeIdentifier": str,
        "typeRevision": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAssetTypeInputRequestTypeDef = TypedDict(
    "_RequiredCreateAssetTypeInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "formsInput": Dict[str, "FormEntryInputTypeDef"],
        "name": str,
        "owningProjectIdentifier": str,
    },
)
_OptionalCreateAssetTypeInputRequestTypeDef = TypedDict(
    "_OptionalCreateAssetTypeInputRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class CreateAssetTypeInputRequestTypeDef(
    _RequiredCreateAssetTypeInputRequestTypeDef, _OptionalCreateAssetTypeInputRequestTypeDef
):
    pass

CreateAssetTypeOutputTypeDef = TypedDict(
    "CreateAssetTypeOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "formsOutput": Dict[str, "FormEntryOutputTypeDef"],
        "name": str,
        "originDomainId": str,
        "originProjectId": str,
        "owningProjectId": str,
        "revision": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataSourceInputRequestTypeDef = TypedDict(
    "_RequiredCreateDataSourceInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "name": str,
        "projectIdentifier": str,
        "type": str,
    },
)
_OptionalCreateDataSourceInputRequestTypeDef = TypedDict(
    "_OptionalCreateDataSourceInputRequestTypeDef",
    {
        "assetFormsInput": List["FormInputTypeDef"],
        "clientToken": str,
        "configuration": "DataSourceConfigurationInputTypeDef",
        "description": str,
        "enableSetting": EnableSettingType,
        "publishOnImport": bool,
        "recommendation": "RecommendationConfigurationTypeDef",
        "schedule": "ScheduleConfigurationTypeDef",
    },
    total=False,
)

class CreateDataSourceInputRequestTypeDef(
    _RequiredCreateDataSourceInputRequestTypeDef, _OptionalCreateDataSourceInputRequestTypeDef
):
    pass

CreateDataSourceOutputTypeDef = TypedDict(
    "CreateDataSourceOutputTypeDef",
    {
        "assetFormsOutput": List["FormOutputTypeDef"],
        "configuration": "DataSourceConfigurationOutputTypeDef",
        "createdAt": datetime,
        "description": str,
        "domainId": str,
        "enableSetting": EnableSettingType,
        "environmentId": str,
        "errorMessage": "DataSourceErrorMessageTypeDef",
        "id": str,
        "lastRunAt": datetime,
        "lastRunErrorMessage": "DataSourceErrorMessageTypeDef",
        "lastRunStatus": DataSourceRunStatusType,
        "name": str,
        "projectId": str,
        "publishOnImport": bool,
        "recommendation": "RecommendationConfigurationTypeDef",
        "schedule": "ScheduleConfigurationTypeDef",
        "status": DataSourceStatusType,
        "type": str,
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDomainInputRequestTypeDef = TypedDict(
    "_RequiredCreateDomainInputRequestTypeDef",
    {
        "domainExecutionRole": str,
        "name": str,
    },
)
_OptionalCreateDomainInputRequestTypeDef = TypedDict(
    "_OptionalCreateDomainInputRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "kmsKeyIdentifier": str,
        "singleSignOn": "SingleSignOnTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateDomainInputRequestTypeDef(
    _RequiredCreateDomainInputRequestTypeDef, _OptionalCreateDomainInputRequestTypeDef
):
    pass

CreateDomainOutputTypeDef = TypedDict(
    "CreateDomainOutputTypeDef",
    {
        "arn": str,
        "description": str,
        "domainExecutionRole": str,
        "id": str,
        "kmsKeyIdentifier": str,
        "name": str,
        "portalUrl": str,
        "singleSignOn": "SingleSignOnTypeDef",
        "status": DomainStatusType,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEnvironmentInputRequestTypeDef = TypedDict(
    "_RequiredCreateEnvironmentInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentProfileIdentifier": str,
        "name": str,
        "projectIdentifier": str,
    },
)
_OptionalCreateEnvironmentInputRequestTypeDef = TypedDict(
    "_OptionalCreateEnvironmentInputRequestTypeDef",
    {
        "description": str,
        "glossaryTerms": List[str],
        "userParameters": List["EnvironmentParameterTypeDef"],
    },
    total=False,
)

class CreateEnvironmentInputRequestTypeDef(
    _RequiredCreateEnvironmentInputRequestTypeDef, _OptionalCreateEnvironmentInputRequestTypeDef
):
    pass

CreateEnvironmentOutputTypeDef = TypedDict(
    "CreateEnvironmentOutputTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "createdAt": datetime,
        "createdBy": str,
        "deploymentProperties": "DeploymentPropertiesTypeDef",
        "description": str,
        "domainId": str,
        "environmentActions": List["ConfigurableEnvironmentActionTypeDef"],
        "environmentBlueprintId": str,
        "environmentProfileId": str,
        "glossaryTerms": List[str],
        "id": str,
        "lastDeployment": "DeploymentTypeDef",
        "name": str,
        "projectId": str,
        "provider": str,
        "provisionedResources": List["ResourceTypeDef"],
        "provisioningProperties": "ProvisioningPropertiesTypeDef",
        "status": EnvironmentStatusType,
        "updatedAt": datetime,
        "userParameters": List["CustomParameterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEnvironmentProfileInputRequestTypeDef = TypedDict(
    "_RequiredCreateEnvironmentProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentBlueprintIdentifier": str,
        "name": str,
        "projectIdentifier": str,
    },
)
_OptionalCreateEnvironmentProfileInputRequestTypeDef = TypedDict(
    "_OptionalCreateEnvironmentProfileInputRequestTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "description": str,
        "userParameters": List["EnvironmentParameterTypeDef"],
    },
    total=False,
)

class CreateEnvironmentProfileInputRequestTypeDef(
    _RequiredCreateEnvironmentProfileInputRequestTypeDef,
    _OptionalCreateEnvironmentProfileInputRequestTypeDef,
):
    pass

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
        "userParameters": List["CustomParameterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFormTypeInputRequestTypeDef = TypedDict(
    "_RequiredCreateFormTypeInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "model": "ModelTypeDef",
        "name": str,
        "owningProjectIdentifier": str,
    },
)
_OptionalCreateFormTypeInputRequestTypeDef = TypedDict(
    "_OptionalCreateFormTypeInputRequestTypeDef",
    {
        "description": str,
        "status": FormTypeStatusType,
    },
    total=False,
)

class CreateFormTypeInputRequestTypeDef(
    _RequiredCreateFormTypeInputRequestTypeDef, _OptionalCreateFormTypeInputRequestTypeDef
):
    pass

CreateFormTypeOutputTypeDef = TypedDict(
    "CreateFormTypeOutputTypeDef",
    {
        "description": str,
        "domainId": str,
        "name": str,
        "originDomainId": str,
        "originProjectId": str,
        "owningProjectId": str,
        "revision": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGlossaryInputRequestTypeDef = TypedDict(
    "_RequiredCreateGlossaryInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "name": str,
        "owningProjectIdentifier": str,
    },
)
_OptionalCreateGlossaryInputRequestTypeDef = TypedDict(
    "_OptionalCreateGlossaryInputRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "status": GlossaryStatusType,
    },
    total=False,
)

class CreateGlossaryInputRequestTypeDef(
    _RequiredCreateGlossaryInputRequestTypeDef, _OptionalCreateGlossaryInputRequestTypeDef
):
    pass

CreateGlossaryOutputTypeDef = TypedDict(
    "CreateGlossaryOutputTypeDef",
    {
        "description": str,
        "domainId": str,
        "id": str,
        "name": str,
        "owningProjectId": str,
        "status": GlossaryStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGlossaryTermInputRequestTypeDef = TypedDict(
    "_RequiredCreateGlossaryTermInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "glossaryIdentifier": str,
        "name": str,
    },
)
_OptionalCreateGlossaryTermInputRequestTypeDef = TypedDict(
    "_OptionalCreateGlossaryTermInputRequestTypeDef",
    {
        "clientToken": str,
        "longDescription": str,
        "shortDescription": str,
        "status": GlossaryTermStatusType,
        "termRelations": "TermRelationsTypeDef",
    },
    total=False,
)

class CreateGlossaryTermInputRequestTypeDef(
    _RequiredCreateGlossaryTermInputRequestTypeDef, _OptionalCreateGlossaryTermInputRequestTypeDef
):
    pass

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
        "termRelations": "TermRelationsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGroupProfileInputRequestTypeDef = TypedDict(
    "_RequiredCreateGroupProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "groupIdentifier": str,
    },
)
_OptionalCreateGroupProfileInputRequestTypeDef = TypedDict(
    "_OptionalCreateGroupProfileInputRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateGroupProfileInputRequestTypeDef(
    _RequiredCreateGroupProfileInputRequestTypeDef, _OptionalCreateGroupProfileInputRequestTypeDef
):
    pass

CreateGroupProfileOutputTypeDef = TypedDict(
    "CreateGroupProfileOutputTypeDef",
    {
        "domainId": str,
        "groupName": str,
        "id": str,
        "status": GroupProfileStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateListingChangeSetInputRequestTypeDef = TypedDict(
    "_RequiredCreateListingChangeSetInputRequestTypeDef",
    {
        "action": ChangeActionType,
        "domainIdentifier": str,
        "entityIdentifier": str,
        "entityType": Literal["ASSET"],
    },
)
_OptionalCreateListingChangeSetInputRequestTypeDef = TypedDict(
    "_OptionalCreateListingChangeSetInputRequestTypeDef",
    {
        "clientToken": str,
        "entityRevision": str,
    },
    total=False,
)

class CreateListingChangeSetInputRequestTypeDef(
    _RequiredCreateListingChangeSetInputRequestTypeDef,
    _OptionalCreateListingChangeSetInputRequestTypeDef,
):
    pass

CreateListingChangeSetOutputTypeDef = TypedDict(
    "CreateListingChangeSetOutputTypeDef",
    {
        "listingId": str,
        "listingRevision": str,
        "status": ListingStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProjectInputRequestTypeDef = TypedDict(
    "_RequiredCreateProjectInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "name": str,
    },
)
_OptionalCreateProjectInputRequestTypeDef = TypedDict(
    "_OptionalCreateProjectInputRequestTypeDef",
    {
        "description": str,
        "glossaryTerms": List[str],
    },
    total=False,
)

class CreateProjectInputRequestTypeDef(
    _RequiredCreateProjectInputRequestTypeDef, _OptionalCreateProjectInputRequestTypeDef
):
    pass

CreateProjectMembershipInputRequestTypeDef = TypedDict(
    "CreateProjectMembershipInputRequestTypeDef",
    {
        "designation": UserDesignationType,
        "domainIdentifier": str,
        "member": "MemberTypeDef",
        "projectIdentifier": str,
    },
)

CreateProjectOutputTypeDef = TypedDict(
    "CreateProjectOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "failureReasons": List["ProjectDeletionErrorTypeDef"],
        "glossaryTerms": List[str],
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "projectStatus": ProjectStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSubscriptionGrantInputRequestTypeDef = TypedDict(
    "_RequiredCreateSubscriptionGrantInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "grantedEntity": "GrantedEntityInputTypeDef",
        "subscriptionTargetIdentifier": str,
    },
)
_OptionalCreateSubscriptionGrantInputRequestTypeDef = TypedDict(
    "_OptionalCreateSubscriptionGrantInputRequestTypeDef",
    {
        "assetTargetNames": List["AssetTargetNameMapTypeDef"],
        "clientToken": str,
    },
    total=False,
)

class CreateSubscriptionGrantInputRequestTypeDef(
    _RequiredCreateSubscriptionGrantInputRequestTypeDef,
    _OptionalCreateSubscriptionGrantInputRequestTypeDef,
):
    pass

CreateSubscriptionGrantOutputTypeDef = TypedDict(
    "CreateSubscriptionGrantOutputTypeDef",
    {
        "assets": List["SubscribedAssetTypeDef"],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "grantedEntity": "GrantedEntityTypeDef",
        "id": str,
        "status": SubscriptionGrantOverallStatusType,
        "subscriptionId": str,
        "subscriptionTargetId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSubscriptionRequestInputRequestTypeDef = TypedDict(
    "_RequiredCreateSubscriptionRequestInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "requestReason": str,
        "subscribedListings": List["SubscribedListingInputTypeDef"],
        "subscribedPrincipals": List["SubscribedPrincipalInputTypeDef"],
    },
)
_OptionalCreateSubscriptionRequestInputRequestTypeDef = TypedDict(
    "_OptionalCreateSubscriptionRequestInputRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateSubscriptionRequestInputRequestTypeDef(
    _RequiredCreateSubscriptionRequestInputRequestTypeDef,
    _OptionalCreateSubscriptionRequestInputRequestTypeDef,
):
    pass

CreateSubscriptionRequestOutputTypeDef = TypedDict(
    "CreateSubscriptionRequestOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "decisionComment": str,
        "domainId": str,
        "id": str,
        "requestReason": str,
        "reviewerId": str,
        "status": SubscriptionRequestStatusType,
        "subscribedListings": List["SubscribedListingTypeDef"],
        "subscribedPrincipals": List["SubscribedPrincipalTypeDef"],
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSubscriptionTargetInputRequestTypeDef = TypedDict(
    "_RequiredCreateSubscriptionTargetInputRequestTypeDef",
    {
        "applicableAssetTypes": List[str],
        "authorizedPrincipals": List[str],
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "manageAccessRole": str,
        "name": str,
        "subscriptionTargetConfig": List["SubscriptionTargetFormTypeDef"],
        "type": str,
    },
)
_OptionalCreateSubscriptionTargetInputRequestTypeDef = TypedDict(
    "_OptionalCreateSubscriptionTargetInputRequestTypeDef",
    {
        "clientToken": str,
        "provider": str,
    },
    total=False,
)

class CreateSubscriptionTargetInputRequestTypeDef(
    _RequiredCreateSubscriptionTargetInputRequestTypeDef,
    _OptionalCreateSubscriptionTargetInputRequestTypeDef,
):
    pass

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
        "subscriptionTargetConfig": List["SubscriptionTargetFormTypeDef"],
        "type": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserProfileInputRequestTypeDef = TypedDict(
    "_RequiredCreateUserProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "userIdentifier": str,
    },
)
_OptionalCreateUserProfileInputRequestTypeDef = TypedDict(
    "_OptionalCreateUserProfileInputRequestTypeDef",
    {
        "clientToken": str,
        "userType": UserTypeType,
    },
    total=False,
)

class CreateUserProfileInputRequestTypeDef(
    _RequiredCreateUserProfileInputRequestTypeDef, _OptionalCreateUserProfileInputRequestTypeDef
):
    pass

CreateUserProfileOutputTypeDef = TypedDict(
    "CreateUserProfileOutputTypeDef",
    {
        "details": "UserProfileDetailsTypeDef",
        "domainId": str,
        "id": str,
        "status": UserProfileStatusType,
        "type": UserProfileTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCustomParameterTypeDef = TypedDict(
    "_RequiredCustomParameterTypeDef",
    {
        "fieldType": str,
        "keyName": str,
    },
)
_OptionalCustomParameterTypeDef = TypedDict(
    "_OptionalCustomParameterTypeDef",
    {
        "defaultValue": str,
        "description": str,
        "isEditable": bool,
        "isOptional": bool,
    },
    total=False,
)

class CustomParameterTypeDef(_RequiredCustomParameterTypeDef, _OptionalCustomParameterTypeDef):
    pass

DataProductItemTypeDef = TypedDict(
    "DataProductItemTypeDef",
    {
        "domainId": str,
        "itemId": str,
    },
    total=False,
)

_RequiredDataProductSummaryTypeDef = TypedDict(
    "_RequiredDataProductSummaryTypeDef",
    {
        "domainId": str,
        "id": str,
        "name": str,
        "owningProjectId": str,
    },
)
_OptionalDataProductSummaryTypeDef = TypedDict(
    "_OptionalDataProductSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "dataProductItems": List["DataProductItemTypeDef"],
        "description": str,
        "glossaryTerms": List[str],
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

class DataProductSummaryTypeDef(
    _RequiredDataProductSummaryTypeDef, _OptionalDataProductSummaryTypeDef
):
    pass

DataSourceConfigurationInputTypeDef = TypedDict(
    "DataSourceConfigurationInputTypeDef",
    {
        "glueRunConfiguration": "GlueRunConfigurationInputTypeDef",
        "redshiftRunConfiguration": "RedshiftRunConfigurationInputTypeDef",
    },
    total=False,
)

DataSourceConfigurationOutputTypeDef = TypedDict(
    "DataSourceConfigurationOutputTypeDef",
    {
        "glueRunConfiguration": "GlueRunConfigurationOutputTypeDef",
        "redshiftRunConfiguration": "RedshiftRunConfigurationOutputTypeDef",
    },
    total=False,
)

_RequiredDataSourceErrorMessageTypeDef = TypedDict(
    "_RequiredDataSourceErrorMessageTypeDef",
    {
        "errorType": DataSourceErrorTypeType,
    },
)
_OptionalDataSourceErrorMessageTypeDef = TypedDict(
    "_OptionalDataSourceErrorMessageTypeDef",
    {
        "errorDetail": str,
    },
    total=False,
)

class DataSourceErrorMessageTypeDef(
    _RequiredDataSourceErrorMessageTypeDef, _OptionalDataSourceErrorMessageTypeDef
):
    pass

_RequiredDataSourceRunActivityTypeDef = TypedDict(
    "_RequiredDataSourceRunActivityTypeDef",
    {
        "createdAt": datetime,
        "dataAssetStatus": DataAssetActivityStatusType,
        "dataSourceRunId": str,
        "database": str,
        "projectId": str,
        "technicalName": str,
        "updatedAt": datetime,
    },
)
_OptionalDataSourceRunActivityTypeDef = TypedDict(
    "_OptionalDataSourceRunActivityTypeDef",
    {
        "dataAssetId": str,
        "errorMessage": "DataSourceErrorMessageTypeDef",
        "technicalDescription": str,
    },
    total=False,
)

class DataSourceRunActivityTypeDef(
    _RequiredDataSourceRunActivityTypeDef, _OptionalDataSourceRunActivityTypeDef
):
    pass

_RequiredDataSourceRunSummaryTypeDef = TypedDict(
    "_RequiredDataSourceRunSummaryTypeDef",
    {
        "createdAt": datetime,
        "dataSourceId": str,
        "id": str,
        "projectId": str,
        "status": DataSourceRunStatusType,
        "type": DataSourceRunTypeType,
        "updatedAt": datetime,
    },
)
_OptionalDataSourceRunSummaryTypeDef = TypedDict(
    "_OptionalDataSourceRunSummaryTypeDef",
    {
        "errorMessage": "DataSourceErrorMessageTypeDef",
        "runStatisticsForAssets": "RunStatisticsForAssetsTypeDef",
        "startedAt": datetime,
        "stoppedAt": datetime,
    },
    total=False,
)

class DataSourceRunSummaryTypeDef(
    _RequiredDataSourceRunSummaryTypeDef, _OptionalDataSourceRunSummaryTypeDef
):
    pass

_RequiredDataSourceSummaryTypeDef = TypedDict(
    "_RequiredDataSourceSummaryTypeDef",
    {
        "dataSourceId": str,
        "domainId": str,
        "environmentId": str,
        "name": str,
        "status": DataSourceStatusType,
        "type": str,
    },
)
_OptionalDataSourceSummaryTypeDef = TypedDict(
    "_OptionalDataSourceSummaryTypeDef",
    {
        "createdAt": datetime,
        "enableSetting": EnableSettingType,
        "lastRunAssetCount": int,
        "lastRunAt": datetime,
        "lastRunErrorMessage": "DataSourceErrorMessageTypeDef",
        "lastRunStatus": DataSourceRunStatusType,
        "schedule": "ScheduleConfigurationTypeDef",
        "updatedAt": datetime,
    },
    total=False,
)

class DataSourceSummaryTypeDef(
    _RequiredDataSourceSummaryTypeDef, _OptionalDataSourceSummaryTypeDef
):
    pass

DeleteAssetInputRequestTypeDef = TypedDict(
    "DeleteAssetInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)

DeleteAssetTypeInputRequestTypeDef = TypedDict(
    "DeleteAssetTypeInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)

_RequiredDeleteDataSourceInputRequestTypeDef = TypedDict(
    "_RequiredDeleteDataSourceInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
_OptionalDeleteDataSourceInputRequestTypeDef = TypedDict(
    "_OptionalDeleteDataSourceInputRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteDataSourceInputRequestTypeDef(
    _RequiredDeleteDataSourceInputRequestTypeDef, _OptionalDeleteDataSourceInputRequestTypeDef
):
    pass

DeleteDataSourceOutputTypeDef = TypedDict(
    "DeleteDataSourceOutputTypeDef",
    {
        "assetFormsOutput": List["FormOutputTypeDef"],
        "configuration": "DataSourceConfigurationOutputTypeDef",
        "createdAt": datetime,
        "description": str,
        "domainId": str,
        "enableSetting": EnableSettingType,
        "environmentId": str,
        "errorMessage": "DataSourceErrorMessageTypeDef",
        "id": str,
        "lastRunAt": datetime,
        "lastRunErrorMessage": "DataSourceErrorMessageTypeDef",
        "lastRunStatus": DataSourceRunStatusType,
        "name": str,
        "projectId": str,
        "publishOnImport": bool,
        "schedule": "ScheduleConfigurationTypeDef",
        "status": DataSourceStatusType,
        "type": str,
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteDomainInputRequestTypeDef = TypedDict(
    "_RequiredDeleteDomainInputRequestTypeDef",
    {
        "identifier": str,
    },
)
_OptionalDeleteDomainInputRequestTypeDef = TypedDict(
    "_OptionalDeleteDomainInputRequestTypeDef",
    {
        "clientToken": str,
        "skipDeletionCheck": bool,
    },
    total=False,
)

class DeleteDomainInputRequestTypeDef(
    _RequiredDeleteDomainInputRequestTypeDef, _OptionalDeleteDomainInputRequestTypeDef
):
    pass

DeleteDomainOutputTypeDef = TypedDict(
    "DeleteDomainOutputTypeDef",
    {
        "status": DomainStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEnvironmentBlueprintConfigurationInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentBlueprintConfigurationInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentBlueprintIdentifier": str,
    },
)

DeleteEnvironmentInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)

DeleteEnvironmentProfileInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)

DeleteFormTypeInputRequestTypeDef = TypedDict(
    "DeleteFormTypeInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "formTypeIdentifier": str,
    },
)

DeleteGlossaryInputRequestTypeDef = TypedDict(
    "DeleteGlossaryInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)

DeleteGlossaryTermInputRequestTypeDef = TypedDict(
    "DeleteGlossaryTermInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)

DeleteListingInputRequestTypeDef = TypedDict(
    "DeleteListingInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)

_RequiredDeleteProjectInputRequestTypeDef = TypedDict(
    "_RequiredDeleteProjectInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
_OptionalDeleteProjectInputRequestTypeDef = TypedDict(
    "_OptionalDeleteProjectInputRequestTypeDef",
    {
        "skipDeletionCheck": bool,
    },
    total=False,
)

class DeleteProjectInputRequestTypeDef(
    _RequiredDeleteProjectInputRequestTypeDef, _OptionalDeleteProjectInputRequestTypeDef
):
    pass

DeleteProjectMembershipInputRequestTypeDef = TypedDict(
    "DeleteProjectMembershipInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "member": "MemberTypeDef",
        "projectIdentifier": str,
    },
)

DeleteSubscriptionGrantInputRequestTypeDef = TypedDict(
    "DeleteSubscriptionGrantInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)

DeleteSubscriptionGrantOutputTypeDef = TypedDict(
    "DeleteSubscriptionGrantOutputTypeDef",
    {
        "assets": List["SubscribedAssetTypeDef"],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "grantedEntity": "GrantedEntityTypeDef",
        "id": str,
        "status": SubscriptionGrantOverallStatusType,
        "subscriptionId": str,
        "subscriptionTargetId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSubscriptionRequestInputRequestTypeDef = TypedDict(
    "DeleteSubscriptionRequestInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)

DeleteSubscriptionTargetInputRequestTypeDef = TypedDict(
    "DeleteSubscriptionTargetInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "identifier": str,
    },
)

_RequiredDeleteTimeSeriesDataPointsInputRequestTypeDef = TypedDict(
    "_RequiredDeleteTimeSeriesDataPointsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "entityIdentifier": str,
        "entityType": TimeSeriesEntityTypeType,
        "formName": str,
    },
)
_OptionalDeleteTimeSeriesDataPointsInputRequestTypeDef = TypedDict(
    "_OptionalDeleteTimeSeriesDataPointsInputRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteTimeSeriesDataPointsInputRequestTypeDef(
    _RequiredDeleteTimeSeriesDataPointsInputRequestTypeDef,
    _OptionalDeleteTimeSeriesDataPointsInputRequestTypeDef,
):
    pass

DeploymentPropertiesTypeDef = TypedDict(
    "DeploymentPropertiesTypeDef",
    {
        "endTimeoutMinutes": int,
        "startTimeoutMinutes": int,
    },
    total=False,
)

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "deploymentId": str,
        "deploymentStatus": DeploymentStatusType,
        "deploymentType": DeploymentTypeType,
        "failureReason": "EnvironmentErrorTypeDef",
        "isDeploymentComplete": bool,
        "messages": List[str],
    },
    total=False,
)

DetailedGlossaryTermTypeDef = TypedDict(
    "DetailedGlossaryTermTypeDef",
    {
        "name": str,
        "shortDescription": str,
    },
    total=False,
)

_RequiredDomainSummaryTypeDef = TypedDict(
    "_RequiredDomainSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "id": str,
        "managedAccountId": str,
        "name": str,
        "status": DomainStatusType,
    },
)
_OptionalDomainSummaryTypeDef = TypedDict(
    "_OptionalDomainSummaryTypeDef",
    {
        "description": str,
        "lastUpdatedAt": datetime,
        "portalUrl": str,
    },
    total=False,
)

class DomainSummaryTypeDef(_RequiredDomainSummaryTypeDef, _OptionalDomainSummaryTypeDef):
    pass

_RequiredEnvironmentBlueprintConfigurationItemTypeDef = TypedDict(
    "_RequiredEnvironmentBlueprintConfigurationItemTypeDef",
    {
        "domainId": str,
        "environmentBlueprintId": str,
    },
)
_OptionalEnvironmentBlueprintConfigurationItemTypeDef = TypedDict(
    "_OptionalEnvironmentBlueprintConfigurationItemTypeDef",
    {
        "createdAt": datetime,
        "enabledRegions": List[str],
        "manageAccessRoleArn": str,
        "provisioningRoleArn": str,
        "regionalParameters": Dict[str, Dict[str, str]],
        "updatedAt": datetime,
    },
    total=False,
)

class EnvironmentBlueprintConfigurationItemTypeDef(
    _RequiredEnvironmentBlueprintConfigurationItemTypeDef,
    _OptionalEnvironmentBlueprintConfigurationItemTypeDef,
):
    pass

_RequiredEnvironmentBlueprintSummaryTypeDef = TypedDict(
    "_RequiredEnvironmentBlueprintSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "provider": str,
        "provisioningProperties": "ProvisioningPropertiesTypeDef",
    },
)
_OptionalEnvironmentBlueprintSummaryTypeDef = TypedDict(
    "_OptionalEnvironmentBlueprintSummaryTypeDef",
    {
        "createdAt": datetime,
        "description": str,
        "updatedAt": datetime,
    },
    total=False,
)

class EnvironmentBlueprintSummaryTypeDef(
    _RequiredEnvironmentBlueprintSummaryTypeDef, _OptionalEnvironmentBlueprintSummaryTypeDef
):
    pass

_RequiredEnvironmentErrorTypeDef = TypedDict(
    "_RequiredEnvironmentErrorTypeDef",
    {
        "message": str,
    },
)
_OptionalEnvironmentErrorTypeDef = TypedDict(
    "_OptionalEnvironmentErrorTypeDef",
    {
        "code": str,
    },
    total=False,
)

class EnvironmentErrorTypeDef(_RequiredEnvironmentErrorTypeDef, _OptionalEnvironmentErrorTypeDef):
    pass

EnvironmentParameterTypeDef = TypedDict(
    "EnvironmentParameterTypeDef",
    {
        "name": str,
        "value": str,
    },
    total=False,
)

_RequiredEnvironmentProfileSummaryTypeDef = TypedDict(
    "_RequiredEnvironmentProfileSummaryTypeDef",
    {
        "createdBy": str,
        "domainId": str,
        "environmentBlueprintId": str,
        "id": str,
        "name": str,
    },
)
_OptionalEnvironmentProfileSummaryTypeDef = TypedDict(
    "_OptionalEnvironmentProfileSummaryTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "createdAt": datetime,
        "description": str,
        "projectId": str,
        "updatedAt": datetime,
    },
    total=False,
)

class EnvironmentProfileSummaryTypeDef(
    _RequiredEnvironmentProfileSummaryTypeDef, _OptionalEnvironmentProfileSummaryTypeDef
):
    pass

_RequiredEnvironmentSummaryTypeDef = TypedDict(
    "_RequiredEnvironmentSummaryTypeDef",
    {
        "createdBy": str,
        "domainId": str,
        "environmentProfileId": str,
        "name": str,
        "projectId": str,
        "provider": str,
    },
)
_OptionalEnvironmentSummaryTypeDef = TypedDict(
    "_OptionalEnvironmentSummaryTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "createdAt": datetime,
        "description": str,
        "id": str,
        "status": EnvironmentStatusType,
        "updatedAt": datetime,
    },
    total=False,
)

class EnvironmentSummaryTypeDef(
    _RequiredEnvironmentSummaryTypeDef, _OptionalEnvironmentSummaryTypeDef
):
    pass

FailureCauseTypeDef = TypedDict(
    "FailureCauseTypeDef",
    {
        "message": str,
    },
    total=False,
)

FilterClauseTypeDef = TypedDict(
    "FilterClauseTypeDef",
    {
        "and": List[Dict[str, Any]],
        "filter": "FilterTypeDef",
        "or": List[Dict[str, Any]],
    },
    total=False,
)

FilterExpressionTypeDef = TypedDict(
    "FilterExpressionTypeDef",
    {
        "expression": str,
        "type": FilterExpressionTypeType,
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "attribute": str,
        "value": str,
    },
)

_RequiredFormEntryInputTypeDef = TypedDict(
    "_RequiredFormEntryInputTypeDef",
    {
        "typeIdentifier": str,
        "typeRevision": str,
    },
)
_OptionalFormEntryInputTypeDef = TypedDict(
    "_OptionalFormEntryInputTypeDef",
    {
        "required": bool,
    },
    total=False,
)

class FormEntryInputTypeDef(_RequiredFormEntryInputTypeDef, _OptionalFormEntryInputTypeDef):
    pass

_RequiredFormEntryOutputTypeDef = TypedDict(
    "_RequiredFormEntryOutputTypeDef",
    {
        "typeName": str,
        "typeRevision": str,
    },
)
_OptionalFormEntryOutputTypeDef = TypedDict(
    "_OptionalFormEntryOutputTypeDef",
    {
        "required": bool,
    },
    total=False,
)

class FormEntryOutputTypeDef(_RequiredFormEntryOutputTypeDef, _OptionalFormEntryOutputTypeDef):
    pass

_RequiredFormInputTypeDef = TypedDict(
    "_RequiredFormInputTypeDef",
    {
        "formName": str,
    },
)
_OptionalFormInputTypeDef = TypedDict(
    "_OptionalFormInputTypeDef",
    {
        "content": str,
        "typeIdentifier": str,
        "typeRevision": str,
    },
    total=False,
)

class FormInputTypeDef(_RequiredFormInputTypeDef, _OptionalFormInputTypeDef):
    pass

_RequiredFormOutputTypeDef = TypedDict(
    "_RequiredFormOutputTypeDef",
    {
        "formName": str,
    },
)
_OptionalFormOutputTypeDef = TypedDict(
    "_OptionalFormOutputTypeDef",
    {
        "content": str,
        "typeName": str,
        "typeRevision": str,
    },
    total=False,
)

class FormOutputTypeDef(_RequiredFormOutputTypeDef, _OptionalFormOutputTypeDef):
    pass

_RequiredFormTypeDataTypeDef = TypedDict(
    "_RequiredFormTypeDataTypeDef",
    {
        "domainId": str,
        "name": str,
        "revision": str,
    },
)
_OptionalFormTypeDataTypeDef = TypedDict(
    "_OptionalFormTypeDataTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "imports": List["ImportTypeDef"],
        "model": "ModelTypeDef",
        "originDomainId": str,
        "originProjectId": str,
        "owningProjectId": str,
        "status": FormTypeStatusType,
    },
    total=False,
)

class FormTypeDataTypeDef(_RequiredFormTypeDataTypeDef, _OptionalFormTypeDataTypeDef):
    pass

_RequiredGetAssetInputRequestTypeDef = TypedDict(
    "_RequiredGetAssetInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
_OptionalGetAssetInputRequestTypeDef = TypedDict(
    "_OptionalGetAssetInputRequestTypeDef",
    {
        "revision": str,
    },
    total=False,
)

class GetAssetInputRequestTypeDef(
    _RequiredGetAssetInputRequestTypeDef, _OptionalGetAssetInputRequestTypeDef
):
    pass

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
        "formsOutput": List["FormOutputTypeDef"],
        "glossaryTerms": List[str],
        "id": str,
        "latestTimeSeriesDataPointFormsOutput": List["TimeSeriesDataPointSummaryFormOutputTypeDef"],
        "listing": "AssetListingDetailsTypeDef",
        "name": str,
        "owningProjectId": str,
        "readOnlyFormsOutput": List["FormOutputTypeDef"],
        "revision": str,
        "typeIdentifier": str,
        "typeRevision": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetAssetTypeInputRequestTypeDef = TypedDict(
    "_RequiredGetAssetTypeInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
_OptionalGetAssetTypeInputRequestTypeDef = TypedDict(
    "_OptionalGetAssetTypeInputRequestTypeDef",
    {
        "revision": str,
    },
    total=False,
)

class GetAssetTypeInputRequestTypeDef(
    _RequiredGetAssetTypeInputRequestTypeDef, _OptionalGetAssetTypeInputRequestTypeDef
):
    pass

GetAssetTypeOutputTypeDef = TypedDict(
    "GetAssetTypeOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "formsOutput": Dict[str, "FormEntryOutputTypeDef"],
        "name": str,
        "originDomainId": str,
        "originProjectId": str,
        "owningProjectId": str,
        "revision": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataSourceInputRequestTypeDef = TypedDict(
    "GetDataSourceInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)

GetDataSourceOutputTypeDef = TypedDict(
    "GetDataSourceOutputTypeDef",
    {
        "assetFormsOutput": List["FormOutputTypeDef"],
        "configuration": "DataSourceConfigurationOutputTypeDef",
        "createdAt": datetime,
        "description": str,
        "domainId": str,
        "enableSetting": EnableSettingType,
        "environmentId": str,
        "errorMessage": "DataSourceErrorMessageTypeDef",
        "id": str,
        "lastRunAssetCount": int,
        "lastRunAt": datetime,
        "lastRunErrorMessage": "DataSourceErrorMessageTypeDef",
        "lastRunStatus": DataSourceRunStatusType,
        "name": str,
        "projectId": str,
        "publishOnImport": bool,
        "recommendation": "RecommendationConfigurationTypeDef",
        "schedule": "ScheduleConfigurationTypeDef",
        "status": DataSourceStatusType,
        "type": str,
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataSourceRunInputRequestTypeDef = TypedDict(
    "GetDataSourceRunInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)

GetDataSourceRunOutputTypeDef = TypedDict(
    "GetDataSourceRunOutputTypeDef",
    {
        "createdAt": datetime,
        "dataSourceConfigurationSnapshot": str,
        "dataSourceId": str,
        "domainId": str,
        "errorMessage": "DataSourceErrorMessageTypeDef",
        "id": str,
        "projectId": str,
        "runStatisticsForAssets": "RunStatisticsForAssetsTypeDef",
        "startedAt": datetime,
        "status": DataSourceRunStatusType,
        "stoppedAt": datetime,
        "type": DataSourceRunTypeType,
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainInputRequestTypeDef = TypedDict(
    "GetDomainInputRequestTypeDef",
    {
        "identifier": str,
    },
)

GetDomainOutputTypeDef = TypedDict(
    "GetDomainOutputTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "description": str,
        "domainExecutionRole": str,
        "id": str,
        "kmsKeyIdentifier": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "portalUrl": str,
        "singleSignOn": "SingleSignOnTypeDef",
        "status": DomainStatusType,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnvironmentBlueprintConfigurationInputRequestTypeDef = TypedDict(
    "GetEnvironmentBlueprintConfigurationInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentBlueprintIdentifier": str,
    },
)

GetEnvironmentBlueprintConfigurationOutputTypeDef = TypedDict(
    "GetEnvironmentBlueprintConfigurationOutputTypeDef",
    {
        "createdAt": datetime,
        "domainId": str,
        "enabledRegions": List[str],
        "environmentBlueprintId": str,
        "manageAccessRoleArn": str,
        "provisioningRoleArn": str,
        "regionalParameters": Dict[str, Dict[str, str]],
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnvironmentBlueprintInputRequestTypeDef = TypedDict(
    "GetEnvironmentBlueprintInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)

GetEnvironmentBlueprintOutputTypeDef = TypedDict(
    "GetEnvironmentBlueprintOutputTypeDef",
    {
        "createdAt": datetime,
        "deploymentProperties": "DeploymentPropertiesTypeDef",
        "description": str,
        "glossaryTerms": List[str],
        "id": str,
        "name": str,
        "provider": str,
        "provisioningProperties": "ProvisioningPropertiesTypeDef",
        "updatedAt": datetime,
        "userParameters": List["CustomParameterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnvironmentInputRequestTypeDef = TypedDict(
    "GetEnvironmentInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)

GetEnvironmentOutputTypeDef = TypedDict(
    "GetEnvironmentOutputTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "createdAt": datetime,
        "createdBy": str,
        "deploymentProperties": "DeploymentPropertiesTypeDef",
        "description": str,
        "domainId": str,
        "environmentActions": List["ConfigurableEnvironmentActionTypeDef"],
        "environmentBlueprintId": str,
        "environmentProfileId": str,
        "glossaryTerms": List[str],
        "id": str,
        "lastDeployment": "DeploymentTypeDef",
        "name": str,
        "projectId": str,
        "provider": str,
        "provisionedResources": List["ResourceTypeDef"],
        "provisioningProperties": "ProvisioningPropertiesTypeDef",
        "status": EnvironmentStatusType,
        "updatedAt": datetime,
        "userParameters": List["CustomParameterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnvironmentProfileInputRequestTypeDef = TypedDict(
    "GetEnvironmentProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
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
        "userParameters": List["CustomParameterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFormTypeInputRequestTypeDef = TypedDict(
    "_RequiredGetFormTypeInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "formTypeIdentifier": str,
    },
)
_OptionalGetFormTypeInputRequestTypeDef = TypedDict(
    "_OptionalGetFormTypeInputRequestTypeDef",
    {
        "revision": str,
    },
    total=False,
)

class GetFormTypeInputRequestTypeDef(
    _RequiredGetFormTypeInputRequestTypeDef, _OptionalGetFormTypeInputRequestTypeDef
):
    pass

GetFormTypeOutputTypeDef = TypedDict(
    "GetFormTypeOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "imports": List["ImportTypeDef"],
        "model": "ModelTypeDef",
        "name": str,
        "originDomainId": str,
        "originProjectId": str,
        "owningProjectId": str,
        "revision": str,
        "status": FormTypeStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGlossaryInputRequestTypeDef = TypedDict(
    "GetGlossaryInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGlossaryTermInputRequestTypeDef = TypedDict(
    "GetGlossaryTermInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
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
        "termRelations": "TermRelationsTypeDef",
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupProfileInputRequestTypeDef = TypedDict(
    "GetGroupProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "groupIdentifier": str,
    },
)

GetGroupProfileOutputTypeDef = TypedDict(
    "GetGroupProfileOutputTypeDef",
    {
        "domainId": str,
        "groupName": str,
        "id": str,
        "status": GroupProfileStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIamPortalLoginUrlInputRequestTypeDef = TypedDict(
    "GetIamPortalLoginUrlInputRequestTypeDef",
    {
        "domainIdentifier": str,
    },
)

GetIamPortalLoginUrlOutputTypeDef = TypedDict(
    "GetIamPortalLoginUrlOutputTypeDef",
    {
        "authCodeUrl": str,
        "userProfileId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetListingInputRequestTypeDef = TypedDict(
    "_RequiredGetListingInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
_OptionalGetListingInputRequestTypeDef = TypedDict(
    "_OptionalGetListingInputRequestTypeDef",
    {
        "listingRevision": str,
    },
    total=False,
)

class GetListingInputRequestTypeDef(
    _RequiredGetListingInputRequestTypeDef, _OptionalGetListingInputRequestTypeDef
):
    pass

GetListingOutputTypeDef = TypedDict(
    "GetListingOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "id": str,
        "item": "ListingItemTypeDef",
        "listingRevision": str,
        "name": str,
        "status": ListingStatusType,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMetadataGenerationRunInputRequestTypeDef = TypedDict(
    "GetMetadataGenerationRunInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
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
        "target": "MetadataGenerationRunTargetTypeDef",
        "type": Literal["BUSINESS_DESCRIPTIONS"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProjectInputRequestTypeDef = TypedDict(
    "GetProjectInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)

GetProjectOutputTypeDef = TypedDict(
    "GetProjectOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "failureReasons": List["ProjectDeletionErrorTypeDef"],
        "glossaryTerms": List[str],
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "projectStatus": ProjectStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSubscriptionGrantInputRequestTypeDef = TypedDict(
    "GetSubscriptionGrantInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)

GetSubscriptionGrantOutputTypeDef = TypedDict(
    "GetSubscriptionGrantOutputTypeDef",
    {
        "assets": List["SubscribedAssetTypeDef"],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "grantedEntity": "GrantedEntityTypeDef",
        "id": str,
        "status": SubscriptionGrantOverallStatusType,
        "subscriptionId": str,
        "subscriptionTargetId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSubscriptionInputRequestTypeDef = TypedDict(
    "GetSubscriptionInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
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
        "subscribedListing": "SubscribedListingTypeDef",
        "subscribedPrincipal": "SubscribedPrincipalTypeDef",
        "subscriptionRequestId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSubscriptionRequestDetailsInputRequestTypeDef = TypedDict(
    "GetSubscriptionRequestDetailsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)

GetSubscriptionRequestDetailsOutputTypeDef = TypedDict(
    "GetSubscriptionRequestDetailsOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "decisionComment": str,
        "domainId": str,
        "id": str,
        "requestReason": str,
        "reviewerId": str,
        "status": SubscriptionRequestStatusType,
        "subscribedListings": List["SubscribedListingTypeDef"],
        "subscribedPrincipals": List["SubscribedPrincipalTypeDef"],
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSubscriptionTargetInputRequestTypeDef = TypedDict(
    "GetSubscriptionTargetInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "identifier": str,
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
        "subscriptionTargetConfig": List["SubscriptionTargetFormTypeDef"],
        "type": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTimeSeriesDataPointInputRequestTypeDef = TypedDict(
    "GetTimeSeriesDataPointInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "entityIdentifier": str,
        "entityType": TimeSeriesEntityTypeType,
        "formName": str,
        "identifier": str,
    },
)

GetTimeSeriesDataPointOutputTypeDef = TypedDict(
    "GetTimeSeriesDataPointOutputTypeDef",
    {
        "domainId": str,
        "entityId": str,
        "entityType": TimeSeriesEntityTypeType,
        "form": "TimeSeriesDataPointFormOutputTypeDef",
        "formName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetUserProfileInputRequestTypeDef = TypedDict(
    "_RequiredGetUserProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "userIdentifier": str,
    },
)
_OptionalGetUserProfileInputRequestTypeDef = TypedDict(
    "_OptionalGetUserProfileInputRequestTypeDef",
    {
        "type": UserProfileTypeType,
    },
    total=False,
)

class GetUserProfileInputRequestTypeDef(
    _RequiredGetUserProfileInputRequestTypeDef, _OptionalGetUserProfileInputRequestTypeDef
):
    pass

GetUserProfileOutputTypeDef = TypedDict(
    "GetUserProfileOutputTypeDef",
    {
        "details": "UserProfileDetailsTypeDef",
        "domainId": str,
        "id": str,
        "status": UserProfileStatusType,
        "type": UserProfileTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGlossaryItemTypeDef = TypedDict(
    "_RequiredGlossaryItemTypeDef",
    {
        "domainId": str,
        "id": str,
        "name": str,
        "owningProjectId": str,
        "status": GlossaryStatusType,
    },
)
_OptionalGlossaryItemTypeDef = TypedDict(
    "_OptionalGlossaryItemTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

class GlossaryItemTypeDef(_RequiredGlossaryItemTypeDef, _OptionalGlossaryItemTypeDef):
    pass

_RequiredGlossaryTermItemTypeDef = TypedDict(
    "_RequiredGlossaryTermItemTypeDef",
    {
        "domainId": str,
        "glossaryId": str,
        "id": str,
        "name": str,
        "status": GlossaryTermStatusType,
    },
)
_OptionalGlossaryTermItemTypeDef = TypedDict(
    "_OptionalGlossaryTermItemTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "longDescription": str,
        "shortDescription": str,
        "termRelations": "TermRelationsTypeDef",
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

class GlossaryTermItemTypeDef(_RequiredGlossaryTermItemTypeDef, _OptionalGlossaryTermItemTypeDef):
    pass

_RequiredGlueRunConfigurationInputTypeDef = TypedDict(
    "_RequiredGlueRunConfigurationInputTypeDef",
    {
        "relationalFilterConfigurations": List["RelationalFilterConfigurationTypeDef"],
    },
)
_OptionalGlueRunConfigurationInputTypeDef = TypedDict(
    "_OptionalGlueRunConfigurationInputTypeDef",
    {
        "autoImportDataQualityResult": bool,
        "dataAccessRole": str,
    },
    total=False,
)

class GlueRunConfigurationInputTypeDef(
    _RequiredGlueRunConfigurationInputTypeDef, _OptionalGlueRunConfigurationInputTypeDef
):
    pass

_RequiredGlueRunConfigurationOutputTypeDef = TypedDict(
    "_RequiredGlueRunConfigurationOutputTypeDef",
    {
        "relationalFilterConfigurations": List["RelationalFilterConfigurationTypeDef"],
    },
)
_OptionalGlueRunConfigurationOutputTypeDef = TypedDict(
    "_OptionalGlueRunConfigurationOutputTypeDef",
    {
        "accountId": str,
        "autoImportDataQualityResult": bool,
        "dataAccessRole": str,
        "region": str,
    },
    total=False,
)

class GlueRunConfigurationOutputTypeDef(
    _RequiredGlueRunConfigurationOutputTypeDef, _OptionalGlueRunConfigurationOutputTypeDef
):
    pass

GrantedEntityInputTypeDef = TypedDict(
    "GrantedEntityInputTypeDef",
    {
        "listing": "ListingRevisionInputTypeDef",
    },
    total=False,
)

GrantedEntityTypeDef = TypedDict(
    "GrantedEntityTypeDef",
    {
        "listing": "ListingRevisionTypeDef",
    },
    total=False,
)

GroupDetailsTypeDef = TypedDict(
    "GroupDetailsTypeDef",
    {
        "groupId": str,
    },
)

GroupProfileSummaryTypeDef = TypedDict(
    "GroupProfileSummaryTypeDef",
    {
        "domainId": str,
        "groupName": str,
        "id": str,
        "status": GroupProfileStatusType,
    },
    total=False,
)

IamUserProfileDetailsTypeDef = TypedDict(
    "IamUserProfileDetailsTypeDef",
    {
        "arn": str,
    },
    total=False,
)

ImportTypeDef = TypedDict(
    "ImportTypeDef",
    {
        "name": str,
        "revision": str,
    },
)

_RequiredListAssetRevisionsInputRequestTypeDef = TypedDict(
    "_RequiredListAssetRevisionsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
_OptionalListAssetRevisionsInputRequestTypeDef = TypedDict(
    "_OptionalListAssetRevisionsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAssetRevisionsInputRequestTypeDef(
    _RequiredListAssetRevisionsInputRequestTypeDef, _OptionalListAssetRevisionsInputRequestTypeDef
):
    pass

ListAssetRevisionsOutputTypeDef = TypedDict(
    "ListAssetRevisionsOutputTypeDef",
    {
        "items": List["AssetRevisionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDataSourceRunActivitiesInputRequestTypeDef = TypedDict(
    "_RequiredListDataSourceRunActivitiesInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
_OptionalListDataSourceRunActivitiesInputRequestTypeDef = TypedDict(
    "_OptionalListDataSourceRunActivitiesInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "status": DataAssetActivityStatusType,
    },
    total=False,
)

class ListDataSourceRunActivitiesInputRequestTypeDef(
    _RequiredListDataSourceRunActivitiesInputRequestTypeDef,
    _OptionalListDataSourceRunActivitiesInputRequestTypeDef,
):
    pass

ListDataSourceRunActivitiesOutputTypeDef = TypedDict(
    "ListDataSourceRunActivitiesOutputTypeDef",
    {
        "items": List["DataSourceRunActivityTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDataSourceRunsInputRequestTypeDef = TypedDict(
    "_RequiredListDataSourceRunsInputRequestTypeDef",
    {
        "dataSourceIdentifier": str,
        "domainIdentifier": str,
    },
)
_OptionalListDataSourceRunsInputRequestTypeDef = TypedDict(
    "_OptionalListDataSourceRunsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "status": DataSourceRunStatusType,
    },
    total=False,
)

class ListDataSourceRunsInputRequestTypeDef(
    _RequiredListDataSourceRunsInputRequestTypeDef, _OptionalListDataSourceRunsInputRequestTypeDef
):
    pass

ListDataSourceRunsOutputTypeDef = TypedDict(
    "ListDataSourceRunsOutputTypeDef",
    {
        "items": List["DataSourceRunSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDataSourcesInputRequestTypeDef = TypedDict(
    "_RequiredListDataSourcesInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "projectIdentifier": str,
    },
)
_OptionalListDataSourcesInputRequestTypeDef = TypedDict(
    "_OptionalListDataSourcesInputRequestTypeDef",
    {
        "environmentIdentifier": str,
        "maxResults": int,
        "name": str,
        "nextToken": str,
        "status": DataSourceStatusType,
        "type": str,
    },
    total=False,
)

class ListDataSourcesInputRequestTypeDef(
    _RequiredListDataSourcesInputRequestTypeDef, _OptionalListDataSourcesInputRequestTypeDef
):
    pass

ListDataSourcesOutputTypeDef = TypedDict(
    "ListDataSourcesOutputTypeDef",
    {
        "items": List["DataSourceSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDomainsInputRequestTypeDef = TypedDict(
    "ListDomainsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "status": DomainStatusType,
    },
    total=False,
)

ListDomainsOutputTypeDef = TypedDict(
    "ListDomainsOutputTypeDef",
    {
        "items": List["DomainSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEnvironmentBlueprintConfigurationsInputRequestTypeDef = TypedDict(
    "_RequiredListEnvironmentBlueprintConfigurationsInputRequestTypeDef",
    {
        "domainIdentifier": str,
    },
)
_OptionalListEnvironmentBlueprintConfigurationsInputRequestTypeDef = TypedDict(
    "_OptionalListEnvironmentBlueprintConfigurationsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListEnvironmentBlueprintConfigurationsInputRequestTypeDef(
    _RequiredListEnvironmentBlueprintConfigurationsInputRequestTypeDef,
    _OptionalListEnvironmentBlueprintConfigurationsInputRequestTypeDef,
):
    pass

ListEnvironmentBlueprintConfigurationsOutputTypeDef = TypedDict(
    "ListEnvironmentBlueprintConfigurationsOutputTypeDef",
    {
        "items": List["EnvironmentBlueprintConfigurationItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEnvironmentBlueprintsInputRequestTypeDef = TypedDict(
    "_RequiredListEnvironmentBlueprintsInputRequestTypeDef",
    {
        "domainIdentifier": str,
    },
)
_OptionalListEnvironmentBlueprintsInputRequestTypeDef = TypedDict(
    "_OptionalListEnvironmentBlueprintsInputRequestTypeDef",
    {
        "managed": bool,
        "maxResults": int,
        "name": str,
        "nextToken": str,
    },
    total=False,
)

class ListEnvironmentBlueprintsInputRequestTypeDef(
    _RequiredListEnvironmentBlueprintsInputRequestTypeDef,
    _OptionalListEnvironmentBlueprintsInputRequestTypeDef,
):
    pass

ListEnvironmentBlueprintsOutputTypeDef = TypedDict(
    "ListEnvironmentBlueprintsOutputTypeDef",
    {
        "items": List["EnvironmentBlueprintSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEnvironmentProfilesInputRequestTypeDef = TypedDict(
    "_RequiredListEnvironmentProfilesInputRequestTypeDef",
    {
        "domainIdentifier": str,
    },
)
_OptionalListEnvironmentProfilesInputRequestTypeDef = TypedDict(
    "_OptionalListEnvironmentProfilesInputRequestTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "environmentBlueprintIdentifier": str,
        "maxResults": int,
        "name": str,
        "nextToken": str,
        "projectIdentifier": str,
    },
    total=False,
)

class ListEnvironmentProfilesInputRequestTypeDef(
    _RequiredListEnvironmentProfilesInputRequestTypeDef,
    _OptionalListEnvironmentProfilesInputRequestTypeDef,
):
    pass

ListEnvironmentProfilesOutputTypeDef = TypedDict(
    "ListEnvironmentProfilesOutputTypeDef",
    {
        "items": List["EnvironmentProfileSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEnvironmentsInputRequestTypeDef = TypedDict(
    "_RequiredListEnvironmentsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "projectIdentifier": str,
    },
)
_OptionalListEnvironmentsInputRequestTypeDef = TypedDict(
    "_OptionalListEnvironmentsInputRequestTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "environmentBlueprintIdentifier": str,
        "environmentProfileIdentifier": str,
        "maxResults": int,
        "name": str,
        "nextToken": str,
        "provider": str,
        "status": EnvironmentStatusType,
    },
    total=False,
)

class ListEnvironmentsInputRequestTypeDef(
    _RequiredListEnvironmentsInputRequestTypeDef, _OptionalListEnvironmentsInputRequestTypeDef
):
    pass

ListEnvironmentsOutputTypeDef = TypedDict(
    "ListEnvironmentsOutputTypeDef",
    {
        "items": List["EnvironmentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMetadataGenerationRunsInputRequestTypeDef = TypedDict(
    "_RequiredListMetadataGenerationRunsInputRequestTypeDef",
    {
        "domainIdentifier": str,
    },
)
_OptionalListMetadataGenerationRunsInputRequestTypeDef = TypedDict(
    "_OptionalListMetadataGenerationRunsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "status": MetadataGenerationRunStatusType,
        "type": Literal["BUSINESS_DESCRIPTIONS"],
    },
    total=False,
)

class ListMetadataGenerationRunsInputRequestTypeDef(
    _RequiredListMetadataGenerationRunsInputRequestTypeDef,
    _OptionalListMetadataGenerationRunsInputRequestTypeDef,
):
    pass

ListMetadataGenerationRunsOutputTypeDef = TypedDict(
    "ListMetadataGenerationRunsOutputTypeDef",
    {
        "items": List["MetadataGenerationRunItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListNotificationsInputRequestTypeDef = TypedDict(
    "_RequiredListNotificationsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "type": NotificationTypeType,
    },
)
_OptionalListNotificationsInputRequestTypeDef = TypedDict(
    "_OptionalListNotificationsInputRequestTypeDef",
    {
        "afterTimestamp": Union[datetime, str],
        "beforeTimestamp": Union[datetime, str],
        "maxResults": int,
        "nextToken": str,
        "subjects": List[str],
        "taskStatus": TaskStatusType,
    },
    total=False,
)

class ListNotificationsInputRequestTypeDef(
    _RequiredListNotificationsInputRequestTypeDef, _OptionalListNotificationsInputRequestTypeDef
):
    pass

ListNotificationsOutputTypeDef = TypedDict(
    "ListNotificationsOutputTypeDef",
    {
        "nextToken": str,
        "notifications": List["NotificationOutputTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProjectMembershipsInputRequestTypeDef = TypedDict(
    "_RequiredListProjectMembershipsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "projectIdentifier": str,
    },
)
_OptionalListProjectMembershipsInputRequestTypeDef = TypedDict(
    "_OptionalListProjectMembershipsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "sortBy": Literal["NAME"],
        "sortOrder": SortOrderType,
    },
    total=False,
)

class ListProjectMembershipsInputRequestTypeDef(
    _RequiredListProjectMembershipsInputRequestTypeDef,
    _OptionalListProjectMembershipsInputRequestTypeDef,
):
    pass

ListProjectMembershipsOutputTypeDef = TypedDict(
    "ListProjectMembershipsOutputTypeDef",
    {
        "members": List["ProjectMemberTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProjectsInputRequestTypeDef = TypedDict(
    "_RequiredListProjectsInputRequestTypeDef",
    {
        "domainIdentifier": str,
    },
)
_OptionalListProjectsInputRequestTypeDef = TypedDict(
    "_OptionalListProjectsInputRequestTypeDef",
    {
        "groupIdentifier": str,
        "maxResults": int,
        "name": str,
        "nextToken": str,
        "userIdentifier": str,
    },
    total=False,
)

class ListProjectsInputRequestTypeDef(
    _RequiredListProjectsInputRequestTypeDef, _OptionalListProjectsInputRequestTypeDef
):
    pass

ListProjectsOutputTypeDef = TypedDict(
    "ListProjectsOutputTypeDef",
    {
        "items": List["ProjectSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSubscriptionGrantsInputRequestTypeDef = TypedDict(
    "_RequiredListSubscriptionGrantsInputRequestTypeDef",
    {
        "domainIdentifier": str,
    },
)
_OptionalListSubscriptionGrantsInputRequestTypeDef = TypedDict(
    "_OptionalListSubscriptionGrantsInputRequestTypeDef",
    {
        "environmentId": str,
        "maxResults": int,
        "nextToken": str,
        "sortBy": SortKeyType,
        "sortOrder": SortOrderType,
        "subscribedListingId": str,
        "subscriptionId": str,
        "subscriptionTargetId": str,
    },
    total=False,
)

class ListSubscriptionGrantsInputRequestTypeDef(
    _RequiredListSubscriptionGrantsInputRequestTypeDef,
    _OptionalListSubscriptionGrantsInputRequestTypeDef,
):
    pass

ListSubscriptionGrantsOutputTypeDef = TypedDict(
    "ListSubscriptionGrantsOutputTypeDef",
    {
        "items": List["SubscriptionGrantSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSubscriptionRequestsInputRequestTypeDef = TypedDict(
    "_RequiredListSubscriptionRequestsInputRequestTypeDef",
    {
        "domainIdentifier": str,
    },
)
_OptionalListSubscriptionRequestsInputRequestTypeDef = TypedDict(
    "_OptionalListSubscriptionRequestsInputRequestTypeDef",
    {
        "approverProjectId": str,
        "maxResults": int,
        "nextToken": str,
        "owningProjectId": str,
        "sortBy": SortKeyType,
        "sortOrder": SortOrderType,
        "status": SubscriptionRequestStatusType,
        "subscribedListingId": str,
    },
    total=False,
)

class ListSubscriptionRequestsInputRequestTypeDef(
    _RequiredListSubscriptionRequestsInputRequestTypeDef,
    _OptionalListSubscriptionRequestsInputRequestTypeDef,
):
    pass

ListSubscriptionRequestsOutputTypeDef = TypedDict(
    "ListSubscriptionRequestsOutputTypeDef",
    {
        "items": List["SubscriptionRequestSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSubscriptionTargetsInputRequestTypeDef = TypedDict(
    "_RequiredListSubscriptionTargetsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
    },
)
_OptionalListSubscriptionTargetsInputRequestTypeDef = TypedDict(
    "_OptionalListSubscriptionTargetsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "sortBy": SortKeyType,
        "sortOrder": SortOrderType,
    },
    total=False,
)

class ListSubscriptionTargetsInputRequestTypeDef(
    _RequiredListSubscriptionTargetsInputRequestTypeDef,
    _OptionalListSubscriptionTargetsInputRequestTypeDef,
):
    pass

ListSubscriptionTargetsOutputTypeDef = TypedDict(
    "ListSubscriptionTargetsOutputTypeDef",
    {
        "items": List["SubscriptionTargetSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSubscriptionsInputRequestTypeDef = TypedDict(
    "_RequiredListSubscriptionsInputRequestTypeDef",
    {
        "domainIdentifier": str,
    },
)
_OptionalListSubscriptionsInputRequestTypeDef = TypedDict(
    "_OptionalListSubscriptionsInputRequestTypeDef",
    {
        "approverProjectId": str,
        "maxResults": int,
        "nextToken": str,
        "owningProjectId": str,
        "sortBy": SortKeyType,
        "sortOrder": SortOrderType,
        "status": SubscriptionStatusType,
        "subscribedListingId": str,
        "subscriptionRequestIdentifier": str,
    },
    total=False,
)

class ListSubscriptionsInputRequestTypeDef(
    _RequiredListSubscriptionsInputRequestTypeDef, _OptionalListSubscriptionsInputRequestTypeDef
):
    pass

ListSubscriptionsOutputTypeDef = TypedDict(
    "ListSubscriptionsOutputTypeDef",
    {
        "items": List["SubscriptionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTimeSeriesDataPointsInputRequestTypeDef = TypedDict(
    "_RequiredListTimeSeriesDataPointsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "entityIdentifier": str,
        "entityType": TimeSeriesEntityTypeType,
        "formName": str,
    },
)
_OptionalListTimeSeriesDataPointsInputRequestTypeDef = TypedDict(
    "_OptionalListTimeSeriesDataPointsInputRequestTypeDef",
    {
        "endedAt": Union[datetime, str],
        "maxResults": int,
        "nextToken": str,
        "startedAt": Union[datetime, str],
    },
    total=False,
)

class ListTimeSeriesDataPointsInputRequestTypeDef(
    _RequiredListTimeSeriesDataPointsInputRequestTypeDef,
    _OptionalListTimeSeriesDataPointsInputRequestTypeDef,
):
    pass

ListTimeSeriesDataPointsOutputTypeDef = TypedDict(
    "ListTimeSeriesDataPointsOutputTypeDef",
    {
        "items": List["TimeSeriesDataPointSummaryFormOutputTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListingItemTypeDef = TypedDict(
    "ListingItemTypeDef",
    {
        "assetListing": "AssetListingTypeDef",
    },
    total=False,
)

ListingRevisionInputTypeDef = TypedDict(
    "ListingRevisionInputTypeDef",
    {
        "identifier": str,
        "revision": str,
    },
)

ListingRevisionTypeDef = TypedDict(
    "ListingRevisionTypeDef",
    {
        "id": str,
        "revision": str,
    },
)

MemberDetailsTypeDef = TypedDict(
    "MemberDetailsTypeDef",
    {
        "group": "GroupDetailsTypeDef",
        "user": "UserDetailsTypeDef",
    },
    total=False,
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "groupIdentifier": str,
        "userIdentifier": str,
    },
    total=False,
)

_RequiredMetadataGenerationRunItemTypeDef = TypedDict(
    "_RequiredMetadataGenerationRunItemTypeDef",
    {
        "domainId": str,
        "id": str,
        "owningProjectId": str,
    },
)
_OptionalMetadataGenerationRunItemTypeDef = TypedDict(
    "_OptionalMetadataGenerationRunItemTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "status": MetadataGenerationRunStatusType,
        "target": "MetadataGenerationRunTargetTypeDef",
        "type": Literal["BUSINESS_DESCRIPTIONS"],
    },
    total=False,
)

class MetadataGenerationRunItemTypeDef(
    _RequiredMetadataGenerationRunItemTypeDef, _OptionalMetadataGenerationRunItemTypeDef
):
    pass

_RequiredMetadataGenerationRunTargetTypeDef = TypedDict(
    "_RequiredMetadataGenerationRunTargetTypeDef",
    {
        "identifier": str,
        "type": Literal["ASSET"],
    },
)
_OptionalMetadataGenerationRunTargetTypeDef = TypedDict(
    "_OptionalMetadataGenerationRunTargetTypeDef",
    {
        "revision": str,
    },
    total=False,
)

class MetadataGenerationRunTargetTypeDef(
    _RequiredMetadataGenerationRunTargetTypeDef, _OptionalMetadataGenerationRunTargetTypeDef
):
    pass

ModelTypeDef = TypedDict(
    "ModelTypeDef",
    {
        "smithy": str,
    },
    total=False,
)

_RequiredNotificationOutputTypeDef = TypedDict(
    "_RequiredNotificationOutputTypeDef",
    {
        "actionLink": str,
        "creationTimestamp": datetime,
        "domainIdentifier": str,
        "identifier": str,
        "lastUpdatedTimestamp": datetime,
        "message": str,
        "title": str,
        "topic": "TopicTypeDef",
        "type": NotificationTypeType,
    },
)
_OptionalNotificationOutputTypeDef = TypedDict(
    "_OptionalNotificationOutputTypeDef",
    {
        "metadata": Dict[str, str],
        "status": TaskStatusType,
    },
    total=False,
)

class NotificationOutputTypeDef(
    _RequiredNotificationOutputTypeDef, _OptionalNotificationOutputTypeDef
):
    pass

_RequiredNotificationResourceTypeDef = TypedDict(
    "_RequiredNotificationResourceTypeDef",
    {
        "id": str,
        "type": Literal["PROJECT"],
    },
)
_OptionalNotificationResourceTypeDef = TypedDict(
    "_OptionalNotificationResourceTypeDef",
    {
        "name": str,
    },
    total=False,
)

class NotificationResourceTypeDef(
    _RequiredNotificationResourceTypeDef, _OptionalNotificationResourceTypeDef
):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredPostTimeSeriesDataPointsInputRequestTypeDef = TypedDict(
    "_RequiredPostTimeSeriesDataPointsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "entityIdentifier": str,
        "entityType": TimeSeriesEntityTypeType,
        "forms": List["TimeSeriesDataPointFormInputTypeDef"],
    },
)
_OptionalPostTimeSeriesDataPointsInputRequestTypeDef = TypedDict(
    "_OptionalPostTimeSeriesDataPointsInputRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class PostTimeSeriesDataPointsInputRequestTypeDef(
    _RequiredPostTimeSeriesDataPointsInputRequestTypeDef,
    _OptionalPostTimeSeriesDataPointsInputRequestTypeDef,
):
    pass

PostTimeSeriesDataPointsOutputTypeDef = TypedDict(
    "PostTimeSeriesDataPointsOutputTypeDef",
    {
        "domainId": str,
        "entityId": str,
        "entityType": TimeSeriesEntityTypeType,
        "forms": List["TimeSeriesDataPointFormOutputTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PredictionConfigurationTypeDef = TypedDict(
    "PredictionConfigurationTypeDef",
    {
        "businessNameGeneration": "BusinessNameGenerationConfigurationTypeDef",
    },
    total=False,
)

ProjectDeletionErrorTypeDef = TypedDict(
    "ProjectDeletionErrorTypeDef",
    {
        "code": str,
        "message": str,
    },
    total=False,
)

ProjectMemberTypeDef = TypedDict(
    "ProjectMemberTypeDef",
    {
        "designation": UserDesignationType,
        "memberDetails": "MemberDetailsTypeDef",
    },
)

_RequiredProjectSummaryTypeDef = TypedDict(
    "_RequiredProjectSummaryTypeDef",
    {
        "createdBy": str,
        "domainId": str,
        "id": str,
        "name": str,
    },
)
_OptionalProjectSummaryTypeDef = TypedDict(
    "_OptionalProjectSummaryTypeDef",
    {
        "createdAt": datetime,
        "description": str,
        "failureReasons": List["ProjectDeletionErrorTypeDef"],
        "projectStatus": ProjectStatusType,
        "updatedAt": datetime,
    },
    total=False,
)

class ProjectSummaryTypeDef(_RequiredProjectSummaryTypeDef, _OptionalProjectSummaryTypeDef):
    pass

ProvisioningPropertiesTypeDef = TypedDict(
    "ProvisioningPropertiesTypeDef",
    {
        "cloudFormation": "CloudFormationPropertiesTypeDef",
    },
    total=False,
)

_RequiredPutEnvironmentBlueprintConfigurationInputRequestTypeDef = TypedDict(
    "_RequiredPutEnvironmentBlueprintConfigurationInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "enabledRegions": List[str],
        "environmentBlueprintIdentifier": str,
    },
)
_OptionalPutEnvironmentBlueprintConfigurationInputRequestTypeDef = TypedDict(
    "_OptionalPutEnvironmentBlueprintConfigurationInputRequestTypeDef",
    {
        "manageAccessRoleArn": str,
        "provisioningRoleArn": str,
        "regionalParameters": Dict[str, Dict[str, str]],
    },
    total=False,
)

class PutEnvironmentBlueprintConfigurationInputRequestTypeDef(
    _RequiredPutEnvironmentBlueprintConfigurationInputRequestTypeDef,
    _OptionalPutEnvironmentBlueprintConfigurationInputRequestTypeDef,
):
    pass

PutEnvironmentBlueprintConfigurationOutputTypeDef = TypedDict(
    "PutEnvironmentBlueprintConfigurationOutputTypeDef",
    {
        "createdAt": datetime,
        "domainId": str,
        "enabledRegions": List[str],
        "environmentBlueprintId": str,
        "manageAccessRoleArn": str,
        "provisioningRoleArn": str,
        "regionalParameters": Dict[str, Dict[str, str]],
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecommendationConfigurationTypeDef = TypedDict(
    "RecommendationConfigurationTypeDef",
    {
        "enableBusinessNameGeneration": bool,
    },
    total=False,
)

RedshiftClusterStorageTypeDef = TypedDict(
    "RedshiftClusterStorageTypeDef",
    {
        "clusterName": str,
    },
)

RedshiftCredentialConfigurationTypeDef = TypedDict(
    "RedshiftCredentialConfigurationTypeDef",
    {
        "secretManagerArn": str,
    },
)

_RequiredRedshiftRunConfigurationInputTypeDef = TypedDict(
    "_RequiredRedshiftRunConfigurationInputTypeDef",
    {
        "redshiftCredentialConfiguration": "RedshiftCredentialConfigurationTypeDef",
        "redshiftStorage": "RedshiftStorageTypeDef",
        "relationalFilterConfigurations": List["RelationalFilterConfigurationTypeDef"],
    },
)
_OptionalRedshiftRunConfigurationInputTypeDef = TypedDict(
    "_OptionalRedshiftRunConfigurationInputTypeDef",
    {
        "dataAccessRole": str,
    },
    total=False,
)

class RedshiftRunConfigurationInputTypeDef(
    _RequiredRedshiftRunConfigurationInputTypeDef, _OptionalRedshiftRunConfigurationInputTypeDef
):
    pass

_RequiredRedshiftRunConfigurationOutputTypeDef = TypedDict(
    "_RequiredRedshiftRunConfigurationOutputTypeDef",
    {
        "redshiftCredentialConfiguration": "RedshiftCredentialConfigurationTypeDef",
        "redshiftStorage": "RedshiftStorageTypeDef",
        "relationalFilterConfigurations": List["RelationalFilterConfigurationTypeDef"],
    },
)
_OptionalRedshiftRunConfigurationOutputTypeDef = TypedDict(
    "_OptionalRedshiftRunConfigurationOutputTypeDef",
    {
        "accountId": str,
        "dataAccessRole": str,
        "region": str,
    },
    total=False,
)

class RedshiftRunConfigurationOutputTypeDef(
    _RequiredRedshiftRunConfigurationOutputTypeDef, _OptionalRedshiftRunConfigurationOutputTypeDef
):
    pass

RedshiftServerlessStorageTypeDef = TypedDict(
    "RedshiftServerlessStorageTypeDef",
    {
        "workgroupName": str,
    },
)

RedshiftStorageTypeDef = TypedDict(
    "RedshiftStorageTypeDef",
    {
        "redshiftClusterSource": "RedshiftClusterStorageTypeDef",
        "redshiftServerlessSource": "RedshiftServerlessStorageTypeDef",
    },
    total=False,
)

_RequiredRejectChoiceTypeDef = TypedDict(
    "_RequiredRejectChoiceTypeDef",
    {
        "predictionTarget": str,
    },
)
_OptionalRejectChoiceTypeDef = TypedDict(
    "_OptionalRejectChoiceTypeDef",
    {
        "predictionChoices": List[int],
    },
    total=False,
)

class RejectChoiceTypeDef(_RequiredRejectChoiceTypeDef, _OptionalRejectChoiceTypeDef):
    pass

_RequiredRejectPredictionsInputRequestTypeDef = TypedDict(
    "_RequiredRejectPredictionsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
_OptionalRejectPredictionsInputRequestTypeDef = TypedDict(
    "_OptionalRejectPredictionsInputRequestTypeDef",
    {
        "clientToken": str,
        "rejectChoices": List["RejectChoiceTypeDef"],
        "rejectRule": "RejectRuleTypeDef",
        "revision": str,
    },
    total=False,
)

class RejectPredictionsInputRequestTypeDef(
    _RequiredRejectPredictionsInputRequestTypeDef, _OptionalRejectPredictionsInputRequestTypeDef
):
    pass

RejectPredictionsOutputTypeDef = TypedDict(
    "RejectPredictionsOutputTypeDef",
    {
        "assetId": str,
        "assetRevision": str,
        "domainId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RejectRuleTypeDef = TypedDict(
    "RejectRuleTypeDef",
    {
        "rule": RejectRuleBehaviorType,
        "threshold": float,
    },
    total=False,
)

_RequiredRejectSubscriptionRequestInputRequestTypeDef = TypedDict(
    "_RequiredRejectSubscriptionRequestInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
_OptionalRejectSubscriptionRequestInputRequestTypeDef = TypedDict(
    "_OptionalRejectSubscriptionRequestInputRequestTypeDef",
    {
        "decisionComment": str,
    },
    total=False,
)

class RejectSubscriptionRequestInputRequestTypeDef(
    _RequiredRejectSubscriptionRequestInputRequestTypeDef,
    _OptionalRejectSubscriptionRequestInputRequestTypeDef,
):
    pass

RejectSubscriptionRequestOutputTypeDef = TypedDict(
    "RejectSubscriptionRequestOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "decisionComment": str,
        "domainId": str,
        "id": str,
        "requestReason": str,
        "reviewerId": str,
        "status": SubscriptionRequestStatusType,
        "subscribedListings": List["SubscribedListingTypeDef"],
        "subscribedPrincipals": List["SubscribedPrincipalTypeDef"],
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRelationalFilterConfigurationTypeDef = TypedDict(
    "_RequiredRelationalFilterConfigurationTypeDef",
    {
        "databaseName": str,
    },
)
_OptionalRelationalFilterConfigurationTypeDef = TypedDict(
    "_OptionalRelationalFilterConfigurationTypeDef",
    {
        "filterExpressions": List["FilterExpressionTypeDef"],
        "schemaName": str,
    },
    total=False,
)

class RelationalFilterConfigurationTypeDef(
    _RequiredRelationalFilterConfigurationTypeDef, _OptionalRelationalFilterConfigurationTypeDef
):
    pass

_RequiredResourceTypeDef = TypedDict(
    "_RequiredResourceTypeDef",
    {
        "type": str,
        "value": str,
    },
)
_OptionalResourceTypeDef = TypedDict(
    "_OptionalResourceTypeDef",
    {
        "name": str,
        "provider": str,
    },
    total=False,
)

class ResourceTypeDef(_RequiredResourceTypeDef, _OptionalResourceTypeDef):
    pass

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

_RequiredRevokeSubscriptionInputRequestTypeDef = TypedDict(
    "_RequiredRevokeSubscriptionInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
_OptionalRevokeSubscriptionInputRequestTypeDef = TypedDict(
    "_OptionalRevokeSubscriptionInputRequestTypeDef",
    {
        "retainPermissions": bool,
    },
    total=False,
)

class RevokeSubscriptionInputRequestTypeDef(
    _RequiredRevokeSubscriptionInputRequestTypeDef, _OptionalRevokeSubscriptionInputRequestTypeDef
):
    pass

RevokeSubscriptionOutputTypeDef = TypedDict(
    "RevokeSubscriptionOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "id": str,
        "retainPermissions": bool,
        "status": SubscriptionStatusType,
        "subscribedListing": "SubscribedListingTypeDef",
        "subscribedPrincipal": "SubscribedPrincipalTypeDef",
        "subscriptionRequestId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RunStatisticsForAssetsTypeDef = TypedDict(
    "RunStatisticsForAssetsTypeDef",
    {
        "added": int,
        "failed": int,
        "skipped": int,
        "unchanged": int,
        "updated": int,
    },
    total=False,
)

ScheduleConfigurationTypeDef = TypedDict(
    "ScheduleConfigurationTypeDef",
    {
        "schedule": str,
        "timezone": TimezoneType,
    },
    total=False,
)

_RequiredSearchGroupProfilesInputRequestTypeDef = TypedDict(
    "_RequiredSearchGroupProfilesInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "groupType": GroupSearchTypeType,
    },
)
_OptionalSearchGroupProfilesInputRequestTypeDef = TypedDict(
    "_OptionalSearchGroupProfilesInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "searchText": str,
    },
    total=False,
)

class SearchGroupProfilesInputRequestTypeDef(
    _RequiredSearchGroupProfilesInputRequestTypeDef, _OptionalSearchGroupProfilesInputRequestTypeDef
):
    pass

SearchGroupProfilesOutputTypeDef = TypedDict(
    "SearchGroupProfilesOutputTypeDef",
    {
        "items": List["GroupProfileSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchInItemTypeDef = TypedDict(
    "SearchInItemTypeDef",
    {
        "attribute": str,
    },
)

_RequiredSearchInputRequestTypeDef = TypedDict(
    "_RequiredSearchInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "searchScope": InventorySearchScopeType,
    },
)
_OptionalSearchInputRequestTypeDef = TypedDict(
    "_OptionalSearchInputRequestTypeDef",
    {
        "additionalAttributes": List[SearchOutputAdditionalAttributeType],
        "filters": "FilterClauseTypeDef",
        "maxResults": int,
        "nextToken": str,
        "owningProjectIdentifier": str,
        "searchIn": List["SearchInItemTypeDef"],
        "searchText": str,
        "sort": "SearchSortTypeDef",
    },
    total=False,
)

class SearchInputRequestTypeDef(
    _RequiredSearchInputRequestTypeDef, _OptionalSearchInputRequestTypeDef
):
    pass

SearchInventoryResultItemTypeDef = TypedDict(
    "SearchInventoryResultItemTypeDef",
    {
        "assetItem": "AssetItemTypeDef",
        "dataProductItem": "DataProductSummaryTypeDef",
        "glossaryItem": "GlossaryItemTypeDef",
        "glossaryTermItem": "GlossaryTermItemTypeDef",
    },
    total=False,
)

_RequiredSearchListingsInputRequestTypeDef = TypedDict(
    "_RequiredSearchListingsInputRequestTypeDef",
    {
        "domainIdentifier": str,
    },
)
_OptionalSearchListingsInputRequestTypeDef = TypedDict(
    "_OptionalSearchListingsInputRequestTypeDef",
    {
        "additionalAttributes": List[SearchOutputAdditionalAttributeType],
        "filters": "FilterClauseTypeDef",
        "maxResults": int,
        "nextToken": str,
        "searchIn": List["SearchInItemTypeDef"],
        "searchText": str,
        "sort": "SearchSortTypeDef",
    },
    total=False,
)

class SearchListingsInputRequestTypeDef(
    _RequiredSearchListingsInputRequestTypeDef, _OptionalSearchListingsInputRequestTypeDef
):
    pass

SearchListingsOutputTypeDef = TypedDict(
    "SearchListingsOutputTypeDef",
    {
        "items": List["SearchResultItemTypeDef"],
        "nextToken": str,
        "totalMatchCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchOutputTypeDef = TypedDict(
    "SearchOutputTypeDef",
    {
        "items": List["SearchInventoryResultItemTypeDef"],
        "nextToken": str,
        "totalMatchCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchResultItemTypeDef = TypedDict(
    "SearchResultItemTypeDef",
    {
        "assetListing": "AssetListingItemTypeDef",
    },
    total=False,
)

_RequiredSearchSortTypeDef = TypedDict(
    "_RequiredSearchSortTypeDef",
    {
        "attribute": str,
    },
)
_OptionalSearchSortTypeDef = TypedDict(
    "_OptionalSearchSortTypeDef",
    {
        "order": SortOrderType,
    },
    total=False,
)

class SearchSortTypeDef(_RequiredSearchSortTypeDef, _OptionalSearchSortTypeDef):
    pass

_RequiredSearchTypesInputRequestTypeDef = TypedDict(
    "_RequiredSearchTypesInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "managed": bool,
        "searchScope": TypesSearchScopeType,
    },
)
_OptionalSearchTypesInputRequestTypeDef = TypedDict(
    "_OptionalSearchTypesInputRequestTypeDef",
    {
        "filters": "FilterClauseTypeDef",
        "maxResults": int,
        "nextToken": str,
        "searchIn": List["SearchInItemTypeDef"],
        "searchText": str,
        "sort": "SearchSortTypeDef",
    },
    total=False,
)

class SearchTypesInputRequestTypeDef(
    _RequiredSearchTypesInputRequestTypeDef, _OptionalSearchTypesInputRequestTypeDef
):
    pass

SearchTypesOutputTypeDef = TypedDict(
    "SearchTypesOutputTypeDef",
    {
        "items": List["SearchTypesResultItemTypeDef"],
        "nextToken": str,
        "totalMatchCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchTypesResultItemTypeDef = TypedDict(
    "SearchTypesResultItemTypeDef",
    {
        "assetTypeItem": "AssetTypeItemTypeDef",
        "formTypeItem": "FormTypeDataTypeDef",
    },
    total=False,
)

_RequiredSearchUserProfilesInputRequestTypeDef = TypedDict(
    "_RequiredSearchUserProfilesInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "userType": UserSearchTypeType,
    },
)
_OptionalSearchUserProfilesInputRequestTypeDef = TypedDict(
    "_OptionalSearchUserProfilesInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "searchText": str,
    },
    total=False,
)

class SearchUserProfilesInputRequestTypeDef(
    _RequiredSearchUserProfilesInputRequestTypeDef, _OptionalSearchUserProfilesInputRequestTypeDef
):
    pass

SearchUserProfilesOutputTypeDef = TypedDict(
    "SearchUserProfilesOutputTypeDef",
    {
        "items": List["UserProfileSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SingleSignOnTypeDef = TypedDict(
    "SingleSignOnTypeDef",
    {
        "type": AuthTypeType,
        "userAssignment": UserAssignmentType,
    },
    total=False,
)

SsoUserProfileDetailsTypeDef = TypedDict(
    "SsoUserProfileDetailsTypeDef",
    {
        "firstName": str,
        "lastName": str,
        "username": str,
    },
    total=False,
)

_RequiredStartDataSourceRunInputRequestTypeDef = TypedDict(
    "_RequiredStartDataSourceRunInputRequestTypeDef",
    {
        "dataSourceIdentifier": str,
        "domainIdentifier": str,
    },
)
_OptionalStartDataSourceRunInputRequestTypeDef = TypedDict(
    "_OptionalStartDataSourceRunInputRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class StartDataSourceRunInputRequestTypeDef(
    _RequiredStartDataSourceRunInputRequestTypeDef, _OptionalStartDataSourceRunInputRequestTypeDef
):
    pass

StartDataSourceRunOutputTypeDef = TypedDict(
    "StartDataSourceRunOutputTypeDef",
    {
        "createdAt": datetime,
        "dataSourceConfigurationSnapshot": str,
        "dataSourceId": str,
        "domainId": str,
        "errorMessage": "DataSourceErrorMessageTypeDef",
        "id": str,
        "projectId": str,
        "runStatisticsForAssets": "RunStatisticsForAssetsTypeDef",
        "startedAt": datetime,
        "status": DataSourceRunStatusType,
        "stoppedAt": datetime,
        "type": DataSourceRunTypeType,
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartMetadataGenerationRunInputRequestTypeDef = TypedDict(
    "_RequiredStartMetadataGenerationRunInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "owningProjectIdentifier": str,
        "target": "MetadataGenerationRunTargetTypeDef",
        "type": Literal["BUSINESS_DESCRIPTIONS"],
    },
)
_OptionalStartMetadataGenerationRunInputRequestTypeDef = TypedDict(
    "_OptionalStartMetadataGenerationRunInputRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class StartMetadataGenerationRunInputRequestTypeDef(
    _RequiredStartMetadataGenerationRunInputRequestTypeDef,
    _OptionalStartMetadataGenerationRunInputRequestTypeDef,
):
    pass

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubscribedAssetListingTypeDef = TypedDict(
    "SubscribedAssetListingTypeDef",
    {
        "entityId": str,
        "entityRevision": str,
        "entityType": str,
        "forms": str,
        "glossaryTerms": List["DetailedGlossaryTermTypeDef"],
    },
    total=False,
)

_RequiredSubscribedAssetTypeDef = TypedDict(
    "_RequiredSubscribedAssetTypeDef",
    {
        "assetId": str,
        "assetRevision": str,
        "status": SubscriptionGrantStatusType,
    },
)
_OptionalSubscribedAssetTypeDef = TypedDict(
    "_OptionalSubscribedAssetTypeDef",
    {
        "failureCause": "FailureCauseTypeDef",
        "failureTimestamp": datetime,
        "grantedTimestamp": datetime,
        "targetName": str,
    },
    total=False,
)

class SubscribedAssetTypeDef(_RequiredSubscribedAssetTypeDef, _OptionalSubscribedAssetTypeDef):
    pass

SubscribedListingInputTypeDef = TypedDict(
    "SubscribedListingInputTypeDef",
    {
        "identifier": str,
    },
)

SubscribedListingItemTypeDef = TypedDict(
    "SubscribedListingItemTypeDef",
    {
        "assetListing": "SubscribedAssetListingTypeDef",
    },
    total=False,
)

_RequiredSubscribedListingTypeDef = TypedDict(
    "_RequiredSubscribedListingTypeDef",
    {
        "description": str,
        "id": str,
        "item": "SubscribedListingItemTypeDef",
        "name": str,
        "ownerProjectId": str,
    },
)
_OptionalSubscribedListingTypeDef = TypedDict(
    "_OptionalSubscribedListingTypeDef",
    {
        "ownerProjectName": str,
        "revision": str,
    },
    total=False,
)

class SubscribedListingTypeDef(
    _RequiredSubscribedListingTypeDef, _OptionalSubscribedListingTypeDef
):
    pass

SubscribedPrincipalInputTypeDef = TypedDict(
    "SubscribedPrincipalInputTypeDef",
    {
        "project": "SubscribedProjectInputTypeDef",
    },
    total=False,
)

SubscribedPrincipalTypeDef = TypedDict(
    "SubscribedPrincipalTypeDef",
    {
        "project": "SubscribedProjectTypeDef",
    },
    total=False,
)

SubscribedProjectInputTypeDef = TypedDict(
    "SubscribedProjectInputTypeDef",
    {
        "identifier": str,
    },
    total=False,
)

SubscribedProjectTypeDef = TypedDict(
    "SubscribedProjectTypeDef",
    {
        "id": str,
        "name": str,
    },
    total=False,
)

_RequiredSubscriptionGrantSummaryTypeDef = TypedDict(
    "_RequiredSubscriptionGrantSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "grantedEntity": "GrantedEntityTypeDef",
        "id": str,
        "status": SubscriptionGrantOverallStatusType,
        "subscriptionTargetId": str,
        "updatedAt": datetime,
    },
)
_OptionalSubscriptionGrantSummaryTypeDef = TypedDict(
    "_OptionalSubscriptionGrantSummaryTypeDef",
    {
        "assets": List["SubscribedAssetTypeDef"],
        "subscriptionId": str,
        "updatedBy": str,
    },
    total=False,
)

class SubscriptionGrantSummaryTypeDef(
    _RequiredSubscriptionGrantSummaryTypeDef, _OptionalSubscriptionGrantSummaryTypeDef
):
    pass

_RequiredSubscriptionRequestSummaryTypeDef = TypedDict(
    "_RequiredSubscriptionRequestSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "id": str,
        "requestReason": str,
        "status": SubscriptionRequestStatusType,
        "subscribedListings": List["SubscribedListingTypeDef"],
        "subscribedPrincipals": List["SubscribedPrincipalTypeDef"],
        "updatedAt": datetime,
    },
)
_OptionalSubscriptionRequestSummaryTypeDef = TypedDict(
    "_OptionalSubscriptionRequestSummaryTypeDef",
    {
        "decisionComment": str,
        "reviewerId": str,
        "updatedBy": str,
    },
    total=False,
)

class SubscriptionRequestSummaryTypeDef(
    _RequiredSubscriptionRequestSummaryTypeDef, _OptionalSubscriptionRequestSummaryTypeDef
):
    pass

_RequiredSubscriptionSummaryTypeDef = TypedDict(
    "_RequiredSubscriptionSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "id": str,
        "status": SubscriptionStatusType,
        "subscribedListing": "SubscribedListingTypeDef",
        "subscribedPrincipal": "SubscribedPrincipalTypeDef",
        "updatedAt": datetime,
    },
)
_OptionalSubscriptionSummaryTypeDef = TypedDict(
    "_OptionalSubscriptionSummaryTypeDef",
    {
        "retainPermissions": bool,
        "subscriptionRequestId": str,
        "updatedBy": str,
    },
    total=False,
)

class SubscriptionSummaryTypeDef(
    _RequiredSubscriptionSummaryTypeDef, _OptionalSubscriptionSummaryTypeDef
):
    pass

SubscriptionTargetFormTypeDef = TypedDict(
    "SubscriptionTargetFormTypeDef",
    {
        "content": str,
        "formName": str,
    },
)

_RequiredSubscriptionTargetSummaryTypeDef = TypedDict(
    "_RequiredSubscriptionTargetSummaryTypeDef",
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
        "subscriptionTargetConfig": List["SubscriptionTargetFormTypeDef"],
        "type": str,
    },
)
_OptionalSubscriptionTargetSummaryTypeDef = TypedDict(
    "_OptionalSubscriptionTargetSummaryTypeDef",
    {
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

class SubscriptionTargetSummaryTypeDef(
    _RequiredSubscriptionTargetSummaryTypeDef, _OptionalSubscriptionTargetSummaryTypeDef
):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TermRelationsTypeDef = TypedDict(
    "TermRelationsTypeDef",
    {
        "classifies": List[str],
        "isA": List[str],
    },
    total=False,
)

_RequiredTimeSeriesDataPointFormInputTypeDef = TypedDict(
    "_RequiredTimeSeriesDataPointFormInputTypeDef",
    {
        "formName": str,
        "timestamp": Union[datetime, str],
        "typeIdentifier": str,
    },
)
_OptionalTimeSeriesDataPointFormInputTypeDef = TypedDict(
    "_OptionalTimeSeriesDataPointFormInputTypeDef",
    {
        "content": str,
        "typeRevision": str,
    },
    total=False,
)

class TimeSeriesDataPointFormInputTypeDef(
    _RequiredTimeSeriesDataPointFormInputTypeDef, _OptionalTimeSeriesDataPointFormInputTypeDef
):
    pass

_RequiredTimeSeriesDataPointFormOutputTypeDef = TypedDict(
    "_RequiredTimeSeriesDataPointFormOutputTypeDef",
    {
        "formName": str,
        "timestamp": datetime,
        "typeIdentifier": str,
    },
)
_OptionalTimeSeriesDataPointFormOutputTypeDef = TypedDict(
    "_OptionalTimeSeriesDataPointFormOutputTypeDef",
    {
        "content": str,
        "id": str,
        "typeRevision": str,
    },
    total=False,
)

class TimeSeriesDataPointFormOutputTypeDef(
    _RequiredTimeSeriesDataPointFormOutputTypeDef, _OptionalTimeSeriesDataPointFormOutputTypeDef
):
    pass

_RequiredTimeSeriesDataPointSummaryFormOutputTypeDef = TypedDict(
    "_RequiredTimeSeriesDataPointSummaryFormOutputTypeDef",
    {
        "formName": str,
        "timestamp": datetime,
        "typeIdentifier": str,
    },
)
_OptionalTimeSeriesDataPointSummaryFormOutputTypeDef = TypedDict(
    "_OptionalTimeSeriesDataPointSummaryFormOutputTypeDef",
    {
        "contentSummary": str,
        "id": str,
        "typeRevision": str,
    },
    total=False,
)

class TimeSeriesDataPointSummaryFormOutputTypeDef(
    _RequiredTimeSeriesDataPointSummaryFormOutputTypeDef,
    _OptionalTimeSeriesDataPointSummaryFormOutputTypeDef,
):
    pass

TopicTypeDef = TypedDict(
    "TopicTypeDef",
    {
        "resource": "NotificationResourceTypeDef",
        "role": NotificationRoleType,
        "subject": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateDataSourceInputRequestTypeDef = TypedDict(
    "_RequiredUpdateDataSourceInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
_OptionalUpdateDataSourceInputRequestTypeDef = TypedDict(
    "_OptionalUpdateDataSourceInputRequestTypeDef",
    {
        "assetFormsInput": List["FormInputTypeDef"],
        "configuration": "DataSourceConfigurationInputTypeDef",
        "description": str,
        "enableSetting": EnableSettingType,
        "name": str,
        "publishOnImport": bool,
        "recommendation": "RecommendationConfigurationTypeDef",
        "schedule": "ScheduleConfigurationTypeDef",
    },
    total=False,
)

class UpdateDataSourceInputRequestTypeDef(
    _RequiredUpdateDataSourceInputRequestTypeDef, _OptionalUpdateDataSourceInputRequestTypeDef
):
    pass

UpdateDataSourceOutputTypeDef = TypedDict(
    "UpdateDataSourceOutputTypeDef",
    {
        "assetFormsOutput": List["FormOutputTypeDef"],
        "configuration": "DataSourceConfigurationOutputTypeDef",
        "createdAt": datetime,
        "description": str,
        "domainId": str,
        "enableSetting": EnableSettingType,
        "environmentId": str,
        "errorMessage": "DataSourceErrorMessageTypeDef",
        "id": str,
        "lastRunAt": datetime,
        "lastRunErrorMessage": "DataSourceErrorMessageTypeDef",
        "lastRunStatus": DataSourceRunStatusType,
        "name": str,
        "projectId": str,
        "publishOnImport": bool,
        "recommendation": "RecommendationConfigurationTypeDef",
        "schedule": "ScheduleConfigurationTypeDef",
        "status": DataSourceStatusType,
        "type": str,
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDomainInputRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainInputRequestTypeDef",
    {
        "identifier": str,
    },
)
_OptionalUpdateDomainInputRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainInputRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "domainExecutionRole": str,
        "name": str,
        "singleSignOn": "SingleSignOnTypeDef",
    },
    total=False,
)

class UpdateDomainInputRequestTypeDef(
    _RequiredUpdateDomainInputRequestTypeDef, _OptionalUpdateDomainInputRequestTypeDef
):
    pass

UpdateDomainOutputTypeDef = TypedDict(
    "UpdateDomainOutputTypeDef",
    {
        "description": str,
        "domainExecutionRole": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "singleSignOn": "SingleSignOnTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEnvironmentInputRequestTypeDef = TypedDict(
    "_RequiredUpdateEnvironmentInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
_OptionalUpdateEnvironmentInputRequestTypeDef = TypedDict(
    "_OptionalUpdateEnvironmentInputRequestTypeDef",
    {
        "description": str,
        "glossaryTerms": List[str],
        "name": str,
    },
    total=False,
)

class UpdateEnvironmentInputRequestTypeDef(
    _RequiredUpdateEnvironmentInputRequestTypeDef, _OptionalUpdateEnvironmentInputRequestTypeDef
):
    pass

UpdateEnvironmentOutputTypeDef = TypedDict(
    "UpdateEnvironmentOutputTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "createdAt": datetime,
        "createdBy": str,
        "deploymentProperties": "DeploymentPropertiesTypeDef",
        "description": str,
        "domainId": str,
        "environmentActions": List["ConfigurableEnvironmentActionTypeDef"],
        "environmentBlueprintId": str,
        "environmentProfileId": str,
        "glossaryTerms": List[str],
        "id": str,
        "lastDeployment": "DeploymentTypeDef",
        "name": str,
        "projectId": str,
        "provider": str,
        "provisionedResources": List["ResourceTypeDef"],
        "provisioningProperties": "ProvisioningPropertiesTypeDef",
        "status": EnvironmentStatusType,
        "updatedAt": datetime,
        "userParameters": List["CustomParameterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEnvironmentProfileInputRequestTypeDef = TypedDict(
    "_RequiredUpdateEnvironmentProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
_OptionalUpdateEnvironmentProfileInputRequestTypeDef = TypedDict(
    "_OptionalUpdateEnvironmentProfileInputRequestTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "description": str,
        "name": str,
        "userParameters": List["EnvironmentParameterTypeDef"],
    },
    total=False,
)

class UpdateEnvironmentProfileInputRequestTypeDef(
    _RequiredUpdateEnvironmentProfileInputRequestTypeDef,
    _OptionalUpdateEnvironmentProfileInputRequestTypeDef,
):
    pass

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
        "userParameters": List["CustomParameterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGlossaryInputRequestTypeDef = TypedDict(
    "_RequiredUpdateGlossaryInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
_OptionalUpdateGlossaryInputRequestTypeDef = TypedDict(
    "_OptionalUpdateGlossaryInputRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "name": str,
        "status": GlossaryStatusType,
    },
    total=False,
)

class UpdateGlossaryInputRequestTypeDef(
    _RequiredUpdateGlossaryInputRequestTypeDef, _OptionalUpdateGlossaryInputRequestTypeDef
):
    pass

UpdateGlossaryOutputTypeDef = TypedDict(
    "UpdateGlossaryOutputTypeDef",
    {
        "description": str,
        "domainId": str,
        "id": str,
        "name": str,
        "owningProjectId": str,
        "status": GlossaryStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGlossaryTermInputRequestTypeDef = TypedDict(
    "_RequiredUpdateGlossaryTermInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
_OptionalUpdateGlossaryTermInputRequestTypeDef = TypedDict(
    "_OptionalUpdateGlossaryTermInputRequestTypeDef",
    {
        "glossaryIdentifier": str,
        "longDescription": str,
        "name": str,
        "shortDescription": str,
        "status": GlossaryTermStatusType,
        "termRelations": "TermRelationsTypeDef",
    },
    total=False,
)

class UpdateGlossaryTermInputRequestTypeDef(
    _RequiredUpdateGlossaryTermInputRequestTypeDef, _OptionalUpdateGlossaryTermInputRequestTypeDef
):
    pass

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
        "termRelations": "TermRelationsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGroupProfileInputRequestTypeDef = TypedDict(
    "UpdateGroupProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "groupIdentifier": str,
        "status": GroupProfileStatusType,
    },
)

UpdateGroupProfileOutputTypeDef = TypedDict(
    "UpdateGroupProfileOutputTypeDef",
    {
        "domainId": str,
        "groupName": str,
        "id": str,
        "status": GroupProfileStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProjectInputRequestTypeDef = TypedDict(
    "_RequiredUpdateProjectInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
_OptionalUpdateProjectInputRequestTypeDef = TypedDict(
    "_OptionalUpdateProjectInputRequestTypeDef",
    {
        "description": str,
        "glossaryTerms": List[str],
        "name": str,
    },
    total=False,
)

class UpdateProjectInputRequestTypeDef(
    _RequiredUpdateProjectInputRequestTypeDef, _OptionalUpdateProjectInputRequestTypeDef
):
    pass

UpdateProjectOutputTypeDef = TypedDict(
    "UpdateProjectOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "failureReasons": List["ProjectDeletionErrorTypeDef"],
        "glossaryTerms": List[str],
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "projectStatus": ProjectStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSubscriptionGrantStatusInputRequestTypeDef = TypedDict(
    "_RequiredUpdateSubscriptionGrantStatusInputRequestTypeDef",
    {
        "assetIdentifier": str,
        "domainIdentifier": str,
        "identifier": str,
        "status": SubscriptionGrantStatusType,
    },
)
_OptionalUpdateSubscriptionGrantStatusInputRequestTypeDef = TypedDict(
    "_OptionalUpdateSubscriptionGrantStatusInputRequestTypeDef",
    {
        "failureCause": "FailureCauseTypeDef",
        "targetName": str,
    },
    total=False,
)

class UpdateSubscriptionGrantStatusInputRequestTypeDef(
    _RequiredUpdateSubscriptionGrantStatusInputRequestTypeDef,
    _OptionalUpdateSubscriptionGrantStatusInputRequestTypeDef,
):
    pass

UpdateSubscriptionGrantStatusOutputTypeDef = TypedDict(
    "UpdateSubscriptionGrantStatusOutputTypeDef",
    {
        "assets": List["SubscribedAssetTypeDef"],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "grantedEntity": "GrantedEntityTypeDef",
        "id": str,
        "status": SubscriptionGrantOverallStatusType,
        "subscriptionId": str,
        "subscriptionTargetId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSubscriptionRequestInputRequestTypeDef = TypedDict(
    "UpdateSubscriptionRequestInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "requestReason": str,
    },
)

UpdateSubscriptionRequestOutputTypeDef = TypedDict(
    "UpdateSubscriptionRequestOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "decisionComment": str,
        "domainId": str,
        "id": str,
        "requestReason": str,
        "reviewerId": str,
        "status": SubscriptionRequestStatusType,
        "subscribedListings": List["SubscribedListingTypeDef"],
        "subscribedPrincipals": List["SubscribedPrincipalTypeDef"],
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSubscriptionTargetInputRequestTypeDef = TypedDict(
    "_RequiredUpdateSubscriptionTargetInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "identifier": str,
    },
)
_OptionalUpdateSubscriptionTargetInputRequestTypeDef = TypedDict(
    "_OptionalUpdateSubscriptionTargetInputRequestTypeDef",
    {
        "applicableAssetTypes": List[str],
        "authorizedPrincipals": List[str],
        "manageAccessRole": str,
        "name": str,
        "provider": str,
        "subscriptionTargetConfig": List["SubscriptionTargetFormTypeDef"],
    },
    total=False,
)

class UpdateSubscriptionTargetInputRequestTypeDef(
    _RequiredUpdateSubscriptionTargetInputRequestTypeDef,
    _OptionalUpdateSubscriptionTargetInputRequestTypeDef,
):
    pass

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
        "subscriptionTargetConfig": List["SubscriptionTargetFormTypeDef"],
        "type": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserProfileInputRequestTypeDef = TypedDict(
    "_RequiredUpdateUserProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "status": UserProfileStatusType,
        "userIdentifier": str,
    },
)
_OptionalUpdateUserProfileInputRequestTypeDef = TypedDict(
    "_OptionalUpdateUserProfileInputRequestTypeDef",
    {
        "type": UserProfileTypeType,
    },
    total=False,
)

class UpdateUserProfileInputRequestTypeDef(
    _RequiredUpdateUserProfileInputRequestTypeDef, _OptionalUpdateUserProfileInputRequestTypeDef
):
    pass

UpdateUserProfileOutputTypeDef = TypedDict(
    "UpdateUserProfileOutputTypeDef",
    {
        "details": "UserProfileDetailsTypeDef",
        "domainId": str,
        "id": str,
        "status": UserProfileStatusType,
        "type": UserProfileTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserDetailsTypeDef = TypedDict(
    "UserDetailsTypeDef",
    {
        "userId": str,
    },
)

UserProfileDetailsTypeDef = TypedDict(
    "UserProfileDetailsTypeDef",
    {
        "iam": "IamUserProfileDetailsTypeDef",
        "sso": "SsoUserProfileDetailsTypeDef",
    },
    total=False,
)

UserProfileSummaryTypeDef = TypedDict(
    "UserProfileSummaryTypeDef",
    {
        "details": "UserProfileDetailsTypeDef",
        "domainId": str,
        "id": str,
        "status": UserProfileStatusType,
        "type": UserProfileTypeType,
    },
    total=False,
)
