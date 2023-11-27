"""
Type annotations for trustedadvisor service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/literals.html)

Usage::

    ```python
    from mypy_boto3_trustedadvisor.literals import ListChecksPaginatorName

    data: ListChecksPaginatorName = "list_checks"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ListChecksPaginatorName",
    "ListOrganizationRecommendationAccountsPaginatorName",
    "ListOrganizationRecommendationResourcesPaginatorName",
    "ListOrganizationRecommendationsPaginatorName",
    "ListRecommendationResourcesPaginatorName",
    "ListRecommendationsPaginatorName",
    "RecommendationLanguageType",
    "RecommendationLifecycleStageType",
    "RecommendationPillarType",
    "RecommendationSourceType",
    "RecommendationStatusType",
    "RecommendationTypeType",
    "ResourceStatusType",
    "UpdateRecommendationLifecycleStageReasonCodeType",
    "UpdateRecommendationLifecycleStageType",
)

ListChecksPaginatorName = Literal["list_checks"]
ListOrganizationRecommendationAccountsPaginatorName = Literal[
    "list_organization_recommendation_accounts"
]
ListOrganizationRecommendationResourcesPaginatorName = Literal[
    "list_organization_recommendation_resources"
]
ListOrganizationRecommendationsPaginatorName = Literal["list_organization_recommendations"]
ListRecommendationResourcesPaginatorName = Literal["list_recommendation_resources"]
ListRecommendationsPaginatorName = Literal["list_recommendations"]
RecommendationLanguageType = Literal[
    "de", "en", "es", "fr", "id", "it", "ja", "ko", "pt_BR", "zh", "zh_TW"
]
RecommendationLifecycleStageType = Literal[
    "dismissed", "in_progress", "pending_response", "resolved"
]
RecommendationPillarType = Literal[
    "cost_optimizing",
    "fault_tolerance",
    "operational_excellence",
    "performance",
    "security",
    "service_limits",
]
RecommendationSourceType = Literal[
    "aws_config",
    "compute_optimizer",
    "cost_explorer",
    "lse",
    "manual",
    "pse",
    "rds",
    "resilience",
    "resilience_hub",
    "security_hub",
    "stir",
    "ta_check",
    "well_architected",
]
RecommendationStatusType = Literal["error", "ok", "warning"]
RecommendationTypeType = Literal["priority", "standard"]
ResourceStatusType = Literal["error", "ok", "warning"]
UpdateRecommendationLifecycleStageReasonCodeType = Literal[
    "low_priority",
    "non_critical_account",
    "not_applicable",
    "other",
    "other_methods_available",
    "temporary_account",
    "valid_business_case",
]
UpdateRecommendationLifecycleStageType = Literal[
    "dismissed", "in_progress", "pending_response", "resolved"
]
