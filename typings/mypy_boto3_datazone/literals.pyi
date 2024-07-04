"""
Type annotations for datazone service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/literals.html)

Usage::

    ```python
    from mypy_boto3_datazone.literals import AcceptRuleBehaviorType

    data: AcceptRuleBehaviorType = "ALL"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AcceptRuleBehaviorType",
    "AuthTypeType",
    "ChangeActionType",
    "ConfigurableActionTypeAuthorizationType",
    "DataAssetActivityStatusType",
    "DataSourceErrorTypeType",
    "DataSourceRunStatusType",
    "DataSourceRunTypeType",
    "DataSourceStatusType",
    "DeploymentStatusType",
    "DeploymentTypeType",
    "DomainStatusType",
    "EdgeDirectionType",
    "EnableSettingType",
    "EntityTypeType",
    "EnvironmentStatusType",
    "FilterExpressionTypeType",
    "FormTypeStatusType",
    "GlossaryStatusType",
    "GlossaryTermStatusType",
    "GroupProfileStatusType",
    "GroupSearchTypeType",
    "InventorySearchScopeType",
    "ListAssetRevisionsPaginatorName",
    "ListDataSourceRunActivitiesPaginatorName",
    "ListDataSourceRunsPaginatorName",
    "ListDataSourcesPaginatorName",
    "ListDomainsPaginatorName",
    "ListEnvironmentActionsPaginatorName",
    "ListEnvironmentBlueprintConfigurationsPaginatorName",
    "ListEnvironmentBlueprintsPaginatorName",
    "ListEnvironmentProfilesPaginatorName",
    "ListEnvironmentsPaginatorName",
    "ListLineageNodeHistoryPaginatorName",
    "ListMetadataGenerationRunsPaginatorName",
    "ListNotificationsPaginatorName",
    "ListProjectMembershipsPaginatorName",
    "ListProjectsPaginatorName",
    "ListSubscriptionGrantsPaginatorName",
    "ListSubscriptionRequestsPaginatorName",
    "ListSubscriptionTargetsPaginatorName",
    "ListSubscriptionsPaginatorName",
    "ListTimeSeriesDataPointsPaginatorName",
    "ListingStatusType",
    "MetadataGenerationRunStatusType",
    "MetadataGenerationRunTypeType",
    "MetadataGenerationTargetTypeType",
    "NotificationResourceTypeType",
    "NotificationRoleType",
    "NotificationTypeType",
    "ProjectStatusType",
    "RejectRuleBehaviorType",
    "SearchGroupProfilesPaginatorName",
    "SearchListingsPaginatorName",
    "SearchOutputAdditionalAttributeType",
    "SearchPaginatorName",
    "SearchTypesPaginatorName",
    "SearchUserProfilesPaginatorName",
    "SelfGrantStatusType",
    "SortFieldProjectType",
    "SortKeyType",
    "SortOrderType",
    "SubscriptionGrantOverallStatusType",
    "SubscriptionGrantStatusType",
    "SubscriptionRequestStatusType",
    "SubscriptionStatusType",
    "TaskStatusType",
    "TimeSeriesEntityTypeType",
    "TimezoneType",
    "TypesSearchScopeType",
    "UserAssignmentType",
    "UserDesignationType",
    "UserProfileStatusType",
    "UserProfileTypeType",
    "UserSearchTypeType",
    "UserTypeType",
)

AcceptRuleBehaviorType = Literal["ALL", "NONE"]
AuthTypeType = Literal["DISABLED", "IAM_IDC"]
ChangeActionType = Literal["PUBLISH", "UNPUBLISH"]
ConfigurableActionTypeAuthorizationType = Literal["HTTPS", "IAM"]
DataAssetActivityStatusType = Literal[
    "FAILED",
    "PUBLISHING_FAILED",
    "SKIPPED_ALREADY_IMPORTED",
    "SKIPPED_ARCHIVED",
    "SKIPPED_NO_ACCESS",
    "SUCCEEDED_CREATED",
    "SUCCEEDED_UPDATED",
    "UNCHANGED",
]
DataSourceErrorTypeType = Literal[
    "ACCESS_DENIED_EXCEPTION",
    "CONFLICT_EXCEPTION",
    "INTERNAL_SERVER_EXCEPTION",
    "RESOURCE_NOT_FOUND_EXCEPTION",
    "SERVICE_QUOTA_EXCEEDED_EXCEPTION",
    "THROTTLING_EXCEPTION",
    "VALIDATION_EXCEPTION",
]
DataSourceRunStatusType = Literal[
    "FAILED", "PARTIALLY_SUCCEEDED", "REQUESTED", "RUNNING", "SUCCESS"
]
DataSourceRunTypeType = Literal["PRIORITIZED", "SCHEDULED"]
DataSourceStatusType = Literal[
    "CREATING",
    "DELETING",
    "FAILED_CREATION",
    "FAILED_DELETION",
    "FAILED_UPDATE",
    "READY",
    "RUNNING",
    "UPDATING",
]
DeploymentStatusType = Literal["FAILED", "IN_PROGRESS", "PENDING_DEPLOYMENT", "SUCCESSFUL"]
DeploymentTypeType = Literal["CREATE", "DELETE", "UPDATE"]
DomainStatusType = Literal[
    "AVAILABLE", "CREATING", "CREATION_FAILED", "DELETED", "DELETING", "DELETION_FAILED"
]
EdgeDirectionType = Literal["DOWNSTREAM", "UPSTREAM"]
EnableSettingType = Literal["DISABLED", "ENABLED"]
EntityTypeType = Literal["ASSET"]
EnvironmentStatusType = Literal[
    "ACTIVE",
    "CREATE_FAILED",
    "CREATING",
    "DELETED",
    "DELETE_FAILED",
    "DELETING",
    "DISABLED",
    "EXPIRED",
    "INACCESSIBLE",
    "SUSPENDED",
    "UPDATE_FAILED",
    "UPDATING",
    "VALIDATION_FAILED",
]
FilterExpressionTypeType = Literal["EXCLUDE", "INCLUDE"]
FormTypeStatusType = Literal["DISABLED", "ENABLED"]
GlossaryStatusType = Literal["DISABLED", "ENABLED"]
GlossaryTermStatusType = Literal["DISABLED", "ENABLED"]
GroupProfileStatusType = Literal["ASSIGNED", "NOT_ASSIGNED"]
GroupSearchTypeType = Literal["DATAZONE_SSO_GROUP", "SSO_GROUP"]
InventorySearchScopeType = Literal["ASSET", "GLOSSARY", "GLOSSARY_TERM"]
ListAssetRevisionsPaginatorName = Literal["list_asset_revisions"]
ListDataSourceRunActivitiesPaginatorName = Literal["list_data_source_run_activities"]
ListDataSourceRunsPaginatorName = Literal["list_data_source_runs"]
ListDataSourcesPaginatorName = Literal["list_data_sources"]
ListDomainsPaginatorName = Literal["list_domains"]
ListEnvironmentActionsPaginatorName = Literal["list_environment_actions"]
ListEnvironmentBlueprintConfigurationsPaginatorName = Literal[
    "list_environment_blueprint_configurations"
]
ListEnvironmentBlueprintsPaginatorName = Literal["list_environment_blueprints"]
ListEnvironmentProfilesPaginatorName = Literal["list_environment_profiles"]
ListEnvironmentsPaginatorName = Literal["list_environments"]
ListLineageNodeHistoryPaginatorName = Literal["list_lineage_node_history"]
ListMetadataGenerationRunsPaginatorName = Literal["list_metadata_generation_runs"]
ListNotificationsPaginatorName = Literal["list_notifications"]
ListProjectMembershipsPaginatorName = Literal["list_project_memberships"]
ListProjectsPaginatorName = Literal["list_projects"]
ListSubscriptionGrantsPaginatorName = Literal["list_subscription_grants"]
ListSubscriptionRequestsPaginatorName = Literal["list_subscription_requests"]
ListSubscriptionTargetsPaginatorName = Literal["list_subscription_targets"]
ListSubscriptionsPaginatorName = Literal["list_subscriptions"]
ListTimeSeriesDataPointsPaginatorName = Literal["list_time_series_data_points"]
ListingStatusType = Literal["ACTIVE", "CREATING", "INACTIVE"]
MetadataGenerationRunStatusType = Literal[
    "CANCELED", "FAILED", "IN_PROGRESS", "SUBMITTED", "SUCCEEDED"
]
MetadataGenerationRunTypeType = Literal["BUSINESS_DESCRIPTIONS"]
MetadataGenerationTargetTypeType = Literal["ASSET"]
NotificationResourceTypeType = Literal["PROJECT"]
NotificationRoleType = Literal[
    "DOMAIN_OWNER", "PROJECT_CONTRIBUTOR", "PROJECT_OWNER", "PROJECT_SUBSCRIBER", "PROJECT_VIEWER"
]
NotificationTypeType = Literal["EVENT", "TASK"]
ProjectStatusType = Literal["ACTIVE", "DELETE_FAILED", "DELETING"]
RejectRuleBehaviorType = Literal["ALL", "NONE"]
SearchGroupProfilesPaginatorName = Literal["search_group_profiles"]
SearchListingsPaginatorName = Literal["search_listings"]
SearchOutputAdditionalAttributeType = Literal["FORMS", "TIME_SERIES_DATA_POINT_FORMS"]
SearchPaginatorName = Literal["search"]
SearchTypesPaginatorName = Literal["search_types"]
SearchUserProfilesPaginatorName = Literal["search_user_profiles"]
SelfGrantStatusType = Literal[
    "GRANTED",
    "GRANT_FAILED",
    "GRANT_IN_PROGRESS",
    "GRANT_PENDING",
    "REVOKE_FAILED",
    "REVOKE_IN_PROGRESS",
    "REVOKE_PENDING",
]
SortFieldProjectType = Literal["NAME"]
SortKeyType = Literal["CREATED_AT", "UPDATED_AT"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
SubscriptionGrantOverallStatusType = Literal[
    "COMPLETED",
    "GRANT_AND_REVOKE_FAILED",
    "GRANT_FAILED",
    "INACCESSIBLE",
    "IN_PROGRESS",
    "PENDING",
    "REVOKE_FAILED",
]
SubscriptionGrantStatusType = Literal[
    "GRANTED",
    "GRANT_FAILED",
    "GRANT_IN_PROGRESS",
    "GRANT_PENDING",
    "REVOKED",
    "REVOKE_FAILED",
    "REVOKE_IN_PROGRESS",
    "REVOKE_PENDING",
]
SubscriptionRequestStatusType = Literal["ACCEPTED", "PENDING", "REJECTED"]
SubscriptionStatusType = Literal["APPROVED", "CANCELLED", "REVOKED"]
TaskStatusType = Literal["ACTIVE", "INACTIVE"]
TimeSeriesEntityTypeType = Literal["ASSET", "LISTING"]
TimezoneType = Literal[
    "AFRICA_JOHANNESBURG",
    "AMERICA_MONTREAL",
    "AMERICA_SAO_PAULO",
    "ASIA_BAHRAIN",
    "ASIA_BANGKOK",
    "ASIA_CALCUTTA",
    "ASIA_DUBAI",
    "ASIA_HONG_KONG",
    "ASIA_JAKARTA",
    "ASIA_KUALA_LUMPUR",
    "ASIA_SEOUL",
    "ASIA_SHANGHAI",
    "ASIA_SINGAPORE",
    "ASIA_TAIPEI",
    "ASIA_TOKYO",
    "AUSTRALIA_MELBOURNE",
    "AUSTRALIA_SYDNEY",
    "CANADA_CENTRAL",
    "CET",
    "CST6CDT",
    "ETC_GMT",
    "ETC_GMT0",
    "ETC_GMT_ADD_0",
    "ETC_GMT_ADD_1",
    "ETC_GMT_ADD_10",
    "ETC_GMT_ADD_11",
    "ETC_GMT_ADD_12",
    "ETC_GMT_ADD_2",
    "ETC_GMT_ADD_3",
    "ETC_GMT_ADD_4",
    "ETC_GMT_ADD_5",
    "ETC_GMT_ADD_6",
    "ETC_GMT_ADD_7",
    "ETC_GMT_ADD_8",
    "ETC_GMT_ADD_9",
    "ETC_GMT_NEG_0",
    "ETC_GMT_NEG_1",
    "ETC_GMT_NEG_10",
    "ETC_GMT_NEG_11",
    "ETC_GMT_NEG_12",
    "ETC_GMT_NEG_13",
    "ETC_GMT_NEG_14",
    "ETC_GMT_NEG_2",
    "ETC_GMT_NEG_3",
    "ETC_GMT_NEG_4",
    "ETC_GMT_NEG_5",
    "ETC_GMT_NEG_6",
    "ETC_GMT_NEG_7",
    "ETC_GMT_NEG_8",
    "ETC_GMT_NEG_9",
    "EUROPE_DUBLIN",
    "EUROPE_LONDON",
    "EUROPE_PARIS",
    "EUROPE_STOCKHOLM",
    "EUROPE_ZURICH",
    "ISRAEL",
    "MEXICO_GENERAL",
    "MST7MDT",
    "PACIFIC_AUCKLAND",
    "US_CENTRAL",
    "US_EASTERN",
    "US_MOUNTAIN",
    "US_PACIFIC",
    "UTC",
]
TypesSearchScopeType = Literal["ASSET_TYPE", "FORM_TYPE", "LINEAGE_NODE_TYPE"]
UserAssignmentType = Literal["AUTOMATIC", "MANUAL"]
UserDesignationType = Literal["PROJECT_CONTRIBUTOR", "PROJECT_OWNER"]
UserProfileStatusType = Literal["ACTIVATED", "ASSIGNED", "DEACTIVATED", "NOT_ASSIGNED"]
UserProfileTypeType = Literal["IAM", "SSO"]
UserSearchTypeType = Literal["DATAZONE_IAM_USER", "DATAZONE_SSO_USER", "DATAZONE_USER", "SSO_USER"]
UserTypeType = Literal["IAM_ROLE", "IAM_USER", "SSO_USER"]
