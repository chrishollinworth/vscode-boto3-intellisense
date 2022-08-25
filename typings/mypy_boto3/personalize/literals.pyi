"""
Type annotations for personalize service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/literals.html)

Usage::

    ```python
    from mypy_boto3_personalize.literals import DomainType

    data: DomainType = "ECOMMERCE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DomainType",
    "ImportModeType",
    "IngestionModeType",
    "ListBatchInferenceJobsPaginatorName",
    "ListBatchSegmentJobsPaginatorName",
    "ListCampaignsPaginatorName",
    "ListDatasetExportJobsPaginatorName",
    "ListDatasetGroupsPaginatorName",
    "ListDatasetImportJobsPaginatorName",
    "ListDatasetsPaginatorName",
    "ListEventTrackersPaginatorName",
    "ListFiltersPaginatorName",
    "ListRecipesPaginatorName",
    "ListRecommendersPaginatorName",
    "ListSchemasPaginatorName",
    "ListSolutionVersionsPaginatorName",
    "ListSolutionsPaginatorName",
    "ObjectiveSensitivityType",
    "RecipeProviderType",
    "TrainingModeType",
)

DomainType = Literal["ECOMMERCE", "VIDEO_ON_DEMAND"]
ImportModeType = Literal["FULL", "INCREMENTAL"]
IngestionModeType = Literal["ALL", "BULK", "PUT"]
ListBatchInferenceJobsPaginatorName = Literal["list_batch_inference_jobs"]
ListBatchSegmentJobsPaginatorName = Literal["list_batch_segment_jobs"]
ListCampaignsPaginatorName = Literal["list_campaigns"]
ListDatasetExportJobsPaginatorName = Literal["list_dataset_export_jobs"]
ListDatasetGroupsPaginatorName = Literal["list_dataset_groups"]
ListDatasetImportJobsPaginatorName = Literal["list_dataset_import_jobs"]
ListDatasetsPaginatorName = Literal["list_datasets"]
ListEventTrackersPaginatorName = Literal["list_event_trackers"]
ListFiltersPaginatorName = Literal["list_filters"]
ListRecipesPaginatorName = Literal["list_recipes"]
ListRecommendersPaginatorName = Literal["list_recommenders"]
ListSchemasPaginatorName = Literal["list_schemas"]
ListSolutionVersionsPaginatorName = Literal["list_solution_versions"]
ListSolutionsPaginatorName = Literal["list_solutions"]
ObjectiveSensitivityType = Literal["HIGH", "LOW", "MEDIUM", "OFF"]
RecipeProviderType = Literal["SERVICE"]
TrainingModeType = Literal["FULL", "UPDATE"]
