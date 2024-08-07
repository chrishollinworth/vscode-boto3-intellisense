"""
Type annotations for sagemaker service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_sagemaker import SageMakerClient
    from mypy_boto3_sagemaker.paginator import (
        ListActionsPaginator,
        ListAlgorithmsPaginator,
        ListAliasesPaginator,
        ListAppImageConfigsPaginator,
        ListAppsPaginator,
        ListArtifactsPaginator,
        ListAssociationsPaginator,
        ListAutoMLJobsPaginator,
        ListCandidatesForAutoMLJobPaginator,
        ListClusterNodesPaginator,
        ListClustersPaginator,
        ListCodeRepositoriesPaginator,
        ListCompilationJobsPaginator,
        ListContextsPaginator,
        ListDataQualityJobDefinitionsPaginator,
        ListDeviceFleetsPaginator,
        ListDevicesPaginator,
        ListDomainsPaginator,
        ListEdgeDeploymentPlansPaginator,
        ListEdgePackagingJobsPaginator,
        ListEndpointConfigsPaginator,
        ListEndpointsPaginator,
        ListExperimentsPaginator,
        ListFeatureGroupsPaginator,
        ListFlowDefinitionsPaginator,
        ListHumanTaskUisPaginator,
        ListHyperParameterTuningJobsPaginator,
        ListImageVersionsPaginator,
        ListImagesPaginator,
        ListInferenceComponentsPaginator,
        ListInferenceExperimentsPaginator,
        ListInferenceRecommendationsJobStepsPaginator,
        ListInferenceRecommendationsJobsPaginator,
        ListLabelingJobsPaginator,
        ListLabelingJobsForWorkteamPaginator,
        ListLineageGroupsPaginator,
        ListMlflowTrackingServersPaginator,
        ListModelBiasJobDefinitionsPaginator,
        ListModelCardExportJobsPaginator,
        ListModelCardVersionsPaginator,
        ListModelCardsPaginator,
        ListModelExplainabilityJobDefinitionsPaginator,
        ListModelMetadataPaginator,
        ListModelPackageGroupsPaginator,
        ListModelPackagesPaginator,
        ListModelQualityJobDefinitionsPaginator,
        ListModelsPaginator,
        ListMonitoringAlertHistoryPaginator,
        ListMonitoringAlertsPaginator,
        ListMonitoringExecutionsPaginator,
        ListMonitoringSchedulesPaginator,
        ListNotebookInstanceLifecycleConfigsPaginator,
        ListNotebookInstancesPaginator,
        ListPipelineExecutionStepsPaginator,
        ListPipelineExecutionsPaginator,
        ListPipelineParametersForExecutionPaginator,
        ListPipelinesPaginator,
        ListProcessingJobsPaginator,
        ListResourceCatalogsPaginator,
        ListSpacesPaginator,
        ListStageDevicesPaginator,
        ListStudioLifecycleConfigsPaginator,
        ListSubscribedWorkteamsPaginator,
        ListTagsPaginator,
        ListTrainingJobsPaginator,
        ListTrainingJobsForHyperParameterTuningJobPaginator,
        ListTransformJobsPaginator,
        ListTrialComponentsPaginator,
        ListTrialsPaginator,
        ListUserProfilesPaginator,
        ListWorkforcesPaginator,
        ListWorkteamsPaginator,
        SearchPaginator,
    )

    client: SageMakerClient = boto3.client("sagemaker")

    list_actions_paginator: ListActionsPaginator = client.get_paginator("list_actions")
    list_algorithms_paginator: ListAlgorithmsPaginator = client.get_paginator("list_algorithms")
    list_aliases_paginator: ListAliasesPaginator = client.get_paginator("list_aliases")
    list_app_image_configs_paginator: ListAppImageConfigsPaginator = client.get_paginator("list_app_image_configs")
    list_apps_paginator: ListAppsPaginator = client.get_paginator("list_apps")
    list_artifacts_paginator: ListArtifactsPaginator = client.get_paginator("list_artifacts")
    list_associations_paginator: ListAssociationsPaginator = client.get_paginator("list_associations")
    list_auto_ml_jobs_paginator: ListAutoMLJobsPaginator = client.get_paginator("list_auto_ml_jobs")
    list_candidates_for_auto_ml_job_paginator: ListCandidatesForAutoMLJobPaginator = client.get_paginator("list_candidates_for_auto_ml_job")
    list_cluster_nodes_paginator: ListClusterNodesPaginator = client.get_paginator("list_cluster_nodes")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_code_repositories_paginator: ListCodeRepositoriesPaginator = client.get_paginator("list_code_repositories")
    list_compilation_jobs_paginator: ListCompilationJobsPaginator = client.get_paginator("list_compilation_jobs")
    list_contexts_paginator: ListContextsPaginator = client.get_paginator("list_contexts")
    list_data_quality_job_definitions_paginator: ListDataQualityJobDefinitionsPaginator = client.get_paginator("list_data_quality_job_definitions")
    list_device_fleets_paginator: ListDeviceFleetsPaginator = client.get_paginator("list_device_fleets")
    list_devices_paginator: ListDevicesPaginator = client.get_paginator("list_devices")
    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    list_edge_deployment_plans_paginator: ListEdgeDeploymentPlansPaginator = client.get_paginator("list_edge_deployment_plans")
    list_edge_packaging_jobs_paginator: ListEdgePackagingJobsPaginator = client.get_paginator("list_edge_packaging_jobs")
    list_endpoint_configs_paginator: ListEndpointConfigsPaginator = client.get_paginator("list_endpoint_configs")
    list_endpoints_paginator: ListEndpointsPaginator = client.get_paginator("list_endpoints")
    list_experiments_paginator: ListExperimentsPaginator = client.get_paginator("list_experiments")
    list_feature_groups_paginator: ListFeatureGroupsPaginator = client.get_paginator("list_feature_groups")
    list_flow_definitions_paginator: ListFlowDefinitionsPaginator = client.get_paginator("list_flow_definitions")
    list_human_task_uis_paginator: ListHumanTaskUisPaginator = client.get_paginator("list_human_task_uis")
    list_hyper_parameter_tuning_jobs_paginator: ListHyperParameterTuningJobsPaginator = client.get_paginator("list_hyper_parameter_tuning_jobs")
    list_image_versions_paginator: ListImageVersionsPaginator = client.get_paginator("list_image_versions")
    list_images_paginator: ListImagesPaginator = client.get_paginator("list_images")
    list_inference_components_paginator: ListInferenceComponentsPaginator = client.get_paginator("list_inference_components")
    list_inference_experiments_paginator: ListInferenceExperimentsPaginator = client.get_paginator("list_inference_experiments")
    list_inference_recommendations_job_steps_paginator: ListInferenceRecommendationsJobStepsPaginator = client.get_paginator("list_inference_recommendations_job_steps")
    list_inference_recommendations_jobs_paginator: ListInferenceRecommendationsJobsPaginator = client.get_paginator("list_inference_recommendations_jobs")
    list_labeling_jobs_paginator: ListLabelingJobsPaginator = client.get_paginator("list_labeling_jobs")
    list_labeling_jobs_for_workteam_paginator: ListLabelingJobsForWorkteamPaginator = client.get_paginator("list_labeling_jobs_for_workteam")
    list_lineage_groups_paginator: ListLineageGroupsPaginator = client.get_paginator("list_lineage_groups")
    list_mlflow_tracking_servers_paginator: ListMlflowTrackingServersPaginator = client.get_paginator("list_mlflow_tracking_servers")
    list_model_bias_job_definitions_paginator: ListModelBiasJobDefinitionsPaginator = client.get_paginator("list_model_bias_job_definitions")
    list_model_card_export_jobs_paginator: ListModelCardExportJobsPaginator = client.get_paginator("list_model_card_export_jobs")
    list_model_card_versions_paginator: ListModelCardVersionsPaginator = client.get_paginator("list_model_card_versions")
    list_model_cards_paginator: ListModelCardsPaginator = client.get_paginator("list_model_cards")
    list_model_explainability_job_definitions_paginator: ListModelExplainabilityJobDefinitionsPaginator = client.get_paginator("list_model_explainability_job_definitions")
    list_model_metadata_paginator: ListModelMetadataPaginator = client.get_paginator("list_model_metadata")
    list_model_package_groups_paginator: ListModelPackageGroupsPaginator = client.get_paginator("list_model_package_groups")
    list_model_packages_paginator: ListModelPackagesPaginator = client.get_paginator("list_model_packages")
    list_model_quality_job_definitions_paginator: ListModelQualityJobDefinitionsPaginator = client.get_paginator("list_model_quality_job_definitions")
    list_models_paginator: ListModelsPaginator = client.get_paginator("list_models")
    list_monitoring_alert_history_paginator: ListMonitoringAlertHistoryPaginator = client.get_paginator("list_monitoring_alert_history")
    list_monitoring_alerts_paginator: ListMonitoringAlertsPaginator = client.get_paginator("list_monitoring_alerts")
    list_monitoring_executions_paginator: ListMonitoringExecutionsPaginator = client.get_paginator("list_monitoring_executions")
    list_monitoring_schedules_paginator: ListMonitoringSchedulesPaginator = client.get_paginator("list_monitoring_schedules")
    list_notebook_instance_lifecycle_configs_paginator: ListNotebookInstanceLifecycleConfigsPaginator = client.get_paginator("list_notebook_instance_lifecycle_configs")
    list_notebook_instances_paginator: ListNotebookInstancesPaginator = client.get_paginator("list_notebook_instances")
    list_pipeline_execution_steps_paginator: ListPipelineExecutionStepsPaginator = client.get_paginator("list_pipeline_execution_steps")
    list_pipeline_executions_paginator: ListPipelineExecutionsPaginator = client.get_paginator("list_pipeline_executions")
    list_pipeline_parameters_for_execution_paginator: ListPipelineParametersForExecutionPaginator = client.get_paginator("list_pipeline_parameters_for_execution")
    list_pipelines_paginator: ListPipelinesPaginator = client.get_paginator("list_pipelines")
    list_processing_jobs_paginator: ListProcessingJobsPaginator = client.get_paginator("list_processing_jobs")
    list_resource_catalogs_paginator: ListResourceCatalogsPaginator = client.get_paginator("list_resource_catalogs")
    list_spaces_paginator: ListSpacesPaginator = client.get_paginator("list_spaces")
    list_stage_devices_paginator: ListStageDevicesPaginator = client.get_paginator("list_stage_devices")
    list_studio_lifecycle_configs_paginator: ListStudioLifecycleConfigsPaginator = client.get_paginator("list_studio_lifecycle_configs")
    list_subscribed_workteams_paginator: ListSubscribedWorkteamsPaginator = client.get_paginator("list_subscribed_workteams")
    list_tags_paginator: ListTagsPaginator = client.get_paginator("list_tags")
    list_training_jobs_paginator: ListTrainingJobsPaginator = client.get_paginator("list_training_jobs")
    list_training_jobs_for_hyper_parameter_tuning_job_paginator: ListTrainingJobsForHyperParameterTuningJobPaginator = client.get_paginator("list_training_jobs_for_hyper_parameter_tuning_job")
    list_transform_jobs_paginator: ListTransformJobsPaginator = client.get_paginator("list_transform_jobs")
    list_trial_components_paginator: ListTrialComponentsPaginator = client.get_paginator("list_trial_components")
    list_trials_paginator: ListTrialsPaginator = client.get_paginator("list_trials")
    list_user_profiles_paginator: ListUserProfilesPaginator = client.get_paginator("list_user_profiles")
    list_workforces_paginator: ListWorkforcesPaginator = client.get_paginator("list_workforces")
    list_workteams_paginator: ListWorkteamsPaginator = client.get_paginator("list_workteams")
    search_paginator: SearchPaginator = client.get_paginator("search")
    ```
"""

import sys
from datetime import datetime
from typing import Iterator, List, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    AlgorithmSortByType,
    AppImageConfigSortKeyType,
    AssociationEdgeTypeType,
    AutoMLJobStatusType,
    AutoMLSortByType,
    AutoMLSortOrderType,
    CandidateSortByType,
    CandidateStatusType,
    ClusterSortByType,
    CodeRepositorySortByType,
    CodeRepositorySortOrderType,
    CompilationJobStatusType,
    CrossAccountFilterOptionType,
    EdgePackagingJobStatusType,
    EndpointConfigSortKeyType,
    EndpointSortKeyType,
    EndpointStatusType,
    ExecutionStatusType,
    FeatureGroupSortByType,
    FeatureGroupSortOrderType,
    FeatureGroupStatusType,
    HyperParameterTuningJobSortByOptionsType,
    HyperParameterTuningJobStatusType,
    ImageSortByType,
    ImageSortOrderType,
    ImageVersionSortByType,
    ImageVersionSortOrderType,
    InferenceComponentSortKeyType,
    InferenceComponentStatusType,
    InferenceExperimentStatusType,
    LabelingJobStatusType,
    ListCompilationJobsSortByType,
    ListDeviceFleetsSortByType,
    ListEdgeDeploymentPlansSortByType,
    ListEdgePackagingJobsSortByType,
    ListInferenceRecommendationsJobsSortByType,
    ListWorkforcesSortByOptionsType,
    ListWorkteamsSortByOptionsType,
    ModelApprovalStatusType,
    ModelCardExportJobSortByType,
    ModelCardExportJobSortOrderType,
    ModelCardExportJobStatusType,
    ModelCardSortByType,
    ModelCardSortOrderType,
    ModelCardStatusType,
    ModelPackageGroupSortByType,
    ModelPackageSortByType,
    ModelPackageTypeType,
    ModelSortKeyType,
    MonitoringAlertHistorySortKeyType,
    MonitoringAlertStatusType,
    MonitoringExecutionSortKeyType,
    MonitoringJobDefinitionSortKeyType,
    MonitoringScheduleSortKeyType,
    MonitoringTypeType,
    NotebookInstanceLifecycleConfigSortKeyType,
    NotebookInstanceLifecycleConfigSortOrderType,
    NotebookInstanceSortKeyType,
    NotebookInstanceSortOrderType,
    NotebookInstanceStatusType,
    OfflineStoreStatusValueType,
    OrderKeyType,
    ProcessingJobStatusType,
    RecommendationJobStatusType,
    ResourceCatalogSortOrderType,
    ResourceTypeType,
    ScheduleStatusType,
    SearchSortOrderType,
    SortActionsByType,
    SortAssociationsByType,
    SortByType,
    SortContextsByType,
    SortExperimentsByType,
    SortInferenceExperimentsByType,
    SortLineageGroupsByType,
    SortOrderType,
    SortPipelineExecutionsByType,
    SortPipelinesByType,
    SortTrackingServerByType,
    SortTrialComponentsByType,
    SortTrialsByType,
    SpaceSortKeyType,
    StudioLifecycleConfigAppTypeType,
    StudioLifecycleConfigSortKeyType,
    TrackingServerStatusType,
    TrainingJobSortByOptionsType,
    TrainingJobStatusType,
    TransformJobStatusType,
    UserProfileSortKeyType,
    WarmPoolResourceStatusType,
)
from .type_defs import (
    ListActionsResponseTypeDef,
    ListAlgorithmsOutputTypeDef,
    ListAliasesResponseTypeDef,
    ListAppImageConfigsResponseTypeDef,
    ListAppsResponseTypeDef,
    ListArtifactsResponseTypeDef,
    ListAssociationsResponseTypeDef,
    ListAutoMLJobsResponseTypeDef,
    ListCandidatesForAutoMLJobResponseTypeDef,
    ListClusterNodesResponseTypeDef,
    ListClustersResponseTypeDef,
    ListCodeRepositoriesOutputTypeDef,
    ListCompilationJobsResponseTypeDef,
    ListContextsResponseTypeDef,
    ListDataQualityJobDefinitionsResponseTypeDef,
    ListDeviceFleetsResponseTypeDef,
    ListDevicesResponseTypeDef,
    ListDomainsResponseTypeDef,
    ListEdgeDeploymentPlansResponseTypeDef,
    ListEdgePackagingJobsResponseTypeDef,
    ListEndpointConfigsOutputTypeDef,
    ListEndpointsOutputTypeDef,
    ListExperimentsResponseTypeDef,
    ListFeatureGroupsResponseTypeDef,
    ListFlowDefinitionsResponseTypeDef,
    ListHumanTaskUisResponseTypeDef,
    ListHyperParameterTuningJobsResponseTypeDef,
    ListImagesResponseTypeDef,
    ListImageVersionsResponseTypeDef,
    ListInferenceComponentsOutputTypeDef,
    ListInferenceExperimentsResponseTypeDef,
    ListInferenceRecommendationsJobsResponseTypeDef,
    ListInferenceRecommendationsJobStepsResponseTypeDef,
    ListLabelingJobsForWorkteamResponseTypeDef,
    ListLabelingJobsResponseTypeDef,
    ListLineageGroupsResponseTypeDef,
    ListMlflowTrackingServersResponseTypeDef,
    ListModelBiasJobDefinitionsResponseTypeDef,
    ListModelCardExportJobsResponseTypeDef,
    ListModelCardsResponseTypeDef,
    ListModelCardVersionsResponseTypeDef,
    ListModelExplainabilityJobDefinitionsResponseTypeDef,
    ListModelMetadataResponseTypeDef,
    ListModelPackageGroupsOutputTypeDef,
    ListModelPackagesOutputTypeDef,
    ListModelQualityJobDefinitionsResponseTypeDef,
    ListModelsOutputTypeDef,
    ListMonitoringAlertHistoryResponseTypeDef,
    ListMonitoringAlertsResponseTypeDef,
    ListMonitoringExecutionsResponseTypeDef,
    ListMonitoringSchedulesResponseTypeDef,
    ListNotebookInstanceLifecycleConfigsOutputTypeDef,
    ListNotebookInstancesOutputTypeDef,
    ListPipelineExecutionsResponseTypeDef,
    ListPipelineExecutionStepsResponseTypeDef,
    ListPipelineParametersForExecutionResponseTypeDef,
    ListPipelinesResponseTypeDef,
    ListProcessingJobsResponseTypeDef,
    ListResourceCatalogsResponseTypeDef,
    ListSpacesResponseTypeDef,
    ListStageDevicesResponseTypeDef,
    ListStudioLifecycleConfigsResponseTypeDef,
    ListSubscribedWorkteamsResponseTypeDef,
    ListTagsOutputTypeDef,
    ListTrainingJobsForHyperParameterTuningJobResponseTypeDef,
    ListTrainingJobsResponseTypeDef,
    ListTransformJobsResponseTypeDef,
    ListTrialComponentsResponseTypeDef,
    ListTrialsResponseTypeDef,
    ListUserProfilesResponseTypeDef,
    ListWorkforcesResponseTypeDef,
    ListWorkteamsResponseTypeDef,
    ModelMetadataSearchExpressionTypeDef,
    PaginatorConfigTypeDef,
    SearchExpressionTypeDef,
    SearchResponseTypeDef,
    VisibilityConditionsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ListActionsPaginator",
    "ListAlgorithmsPaginator",
    "ListAliasesPaginator",
    "ListAppImageConfigsPaginator",
    "ListAppsPaginator",
    "ListArtifactsPaginator",
    "ListAssociationsPaginator",
    "ListAutoMLJobsPaginator",
    "ListCandidatesForAutoMLJobPaginator",
    "ListClusterNodesPaginator",
    "ListClustersPaginator",
    "ListCodeRepositoriesPaginator",
    "ListCompilationJobsPaginator",
    "ListContextsPaginator",
    "ListDataQualityJobDefinitionsPaginator",
    "ListDeviceFleetsPaginator",
    "ListDevicesPaginator",
    "ListDomainsPaginator",
    "ListEdgeDeploymentPlansPaginator",
    "ListEdgePackagingJobsPaginator",
    "ListEndpointConfigsPaginator",
    "ListEndpointsPaginator",
    "ListExperimentsPaginator",
    "ListFeatureGroupsPaginator",
    "ListFlowDefinitionsPaginator",
    "ListHumanTaskUisPaginator",
    "ListHyperParameterTuningJobsPaginator",
    "ListImageVersionsPaginator",
    "ListImagesPaginator",
    "ListInferenceComponentsPaginator",
    "ListInferenceExperimentsPaginator",
    "ListInferenceRecommendationsJobStepsPaginator",
    "ListInferenceRecommendationsJobsPaginator",
    "ListLabelingJobsPaginator",
    "ListLabelingJobsForWorkteamPaginator",
    "ListLineageGroupsPaginator",
    "ListMlflowTrackingServersPaginator",
    "ListModelBiasJobDefinitionsPaginator",
    "ListModelCardExportJobsPaginator",
    "ListModelCardVersionsPaginator",
    "ListModelCardsPaginator",
    "ListModelExplainabilityJobDefinitionsPaginator",
    "ListModelMetadataPaginator",
    "ListModelPackageGroupsPaginator",
    "ListModelPackagesPaginator",
    "ListModelQualityJobDefinitionsPaginator",
    "ListModelsPaginator",
    "ListMonitoringAlertHistoryPaginator",
    "ListMonitoringAlertsPaginator",
    "ListMonitoringExecutionsPaginator",
    "ListMonitoringSchedulesPaginator",
    "ListNotebookInstanceLifecycleConfigsPaginator",
    "ListNotebookInstancesPaginator",
    "ListPipelineExecutionStepsPaginator",
    "ListPipelineExecutionsPaginator",
    "ListPipelineParametersForExecutionPaginator",
    "ListPipelinesPaginator",
    "ListProcessingJobsPaginator",
    "ListResourceCatalogsPaginator",
    "ListSpacesPaginator",
    "ListStageDevicesPaginator",
    "ListStudioLifecycleConfigsPaginator",
    "ListSubscribedWorkteamsPaginator",
    "ListTagsPaginator",
    "ListTrainingJobsPaginator",
    "ListTrainingJobsForHyperParameterTuningJobPaginator",
    "ListTransformJobsPaginator",
    "ListTrialComponentsPaginator",
    "ListTrialsPaginator",
    "ListUserProfilesPaginator",
    "ListWorkforcesPaginator",
    "ListWorkteamsPaginator",
    "SearchPaginator",
)

class ListActionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListActions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listactionspaginator)
    """

    def paginate(
        self,
        *,
        SourceUri: str = None,
        ActionType: str = None,
        CreatedAfter: Union[datetime, str] = None,
        CreatedBefore: Union[datetime, str] = None,
        SortBy: SortActionsByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListActionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListActions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listactionspaginator)
        """

class ListAlgorithmsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListAlgorithms)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listalgorithmspaginator)
    """

    def paginate(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        SortBy: AlgorithmSortByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAlgorithmsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListAlgorithms.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listalgorithmspaginator)
        """

class ListAliasesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListAliases)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listaliasespaginator)
    """

    def paginate(
        self,
        *,
        ImageName: str,
        Alias: str = None,
        Version: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAliasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListAliases.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listaliasespaginator)
        """

class ListAppImageConfigsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListAppImageConfigs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listappimageconfigspaginator)
    """

    def paginate(
        self,
        *,
        NameContains: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        ModifiedTimeBefore: Union[datetime, str] = None,
        ModifiedTimeAfter: Union[datetime, str] = None,
        SortBy: AppImageConfigSortKeyType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAppImageConfigsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListAppImageConfigs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listappimageconfigspaginator)
        """

class ListAppsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListApps)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listappspaginator)
    """

    def paginate(
        self,
        *,
        SortOrder: SortOrderType = None,
        SortBy: Literal["CreationTime"] = None,
        DomainIdEquals: str = None,
        UserProfileNameEquals: str = None,
        SpaceNameEquals: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAppsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListApps.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listappspaginator)
        """

class ListArtifactsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListArtifacts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listartifactspaginator)
    """

    def paginate(
        self,
        *,
        SourceUri: str = None,
        ArtifactType: str = None,
        CreatedAfter: Union[datetime, str] = None,
        CreatedBefore: Union[datetime, str] = None,
        SortBy: Literal["CreationTime"] = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListArtifactsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListArtifacts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listartifactspaginator)
        """

class ListAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listassociationspaginator)
    """

    def paginate(
        self,
        *,
        SourceArn: str = None,
        DestinationArn: str = None,
        SourceType: str = None,
        DestinationType: str = None,
        AssociationType: AssociationEdgeTypeType = None,
        CreatedAfter: Union[datetime, str] = None,
        CreatedBefore: Union[datetime, str] = None,
        SortBy: SortAssociationsByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listassociationspaginator)
        """

class ListAutoMLJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListAutoMLJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listautomljobspaginator)
    """

    def paginate(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        StatusEquals: AutoMLJobStatusType = None,
        SortOrder: AutoMLSortOrderType = None,
        SortBy: AutoMLSortByType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAutoMLJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListAutoMLJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listautomljobspaginator)
        """

class ListCandidatesForAutoMLJobPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListCandidatesForAutoMLJob)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listcandidatesforautomljobpaginator)
    """

    def paginate(
        self,
        *,
        AutoMLJobName: str,
        StatusEquals: CandidateStatusType = None,
        CandidateNameEquals: str = None,
        SortOrder: AutoMLSortOrderType = None,
        SortBy: CandidateSortByType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCandidatesForAutoMLJobResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListCandidatesForAutoMLJob.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listcandidatesforautomljobpaginator)
        """

class ListClusterNodesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListClusterNodes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listclusternodespaginator)
    """

    def paginate(
        self,
        *,
        ClusterName: str,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        InstanceGroupNameContains: str = None,
        SortBy: ClusterSortByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListClusterNodesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListClusterNodes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listclusternodespaginator)
        """

class ListClustersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListClusters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listclusterspaginator)
    """

    def paginate(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        SortBy: ClusterSortByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListClustersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListClusters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listclusterspaginator)
        """

class ListCodeRepositoriesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListCodeRepositories)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listcoderepositoriespaginator)
    """

    def paginate(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        SortBy: CodeRepositorySortByType = None,
        SortOrder: CodeRepositorySortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCodeRepositoriesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListCodeRepositories.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listcoderepositoriespaginator)
        """

class ListCompilationJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListCompilationJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listcompilationjobspaginator)
    """

    def paginate(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        StatusEquals: CompilationJobStatusType = None,
        SortBy: ListCompilationJobsSortByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCompilationJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListCompilationJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listcompilationjobspaginator)
        """

class ListContextsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListContexts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listcontextspaginator)
    """

    def paginate(
        self,
        *,
        SourceUri: str = None,
        ContextType: str = None,
        CreatedAfter: Union[datetime, str] = None,
        CreatedBefore: Union[datetime, str] = None,
        SortBy: SortContextsByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListContextsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListContexts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listcontextspaginator)
        """

class ListDataQualityJobDefinitionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListDataQualityJobDefinitions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listdataqualityjobdefinitionspaginator)
    """

    def paginate(
        self,
        *,
        EndpointName: str = None,
        SortBy: MonitoringJobDefinitionSortKeyType = None,
        SortOrder: SortOrderType = None,
        NameContains: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataQualityJobDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListDataQualityJobDefinitions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listdataqualityjobdefinitionspaginator)
        """

class ListDeviceFleetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListDeviceFleets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listdevicefleetspaginator)
    """

    def paginate(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        SortBy: ListDeviceFleetsSortByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeviceFleetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListDeviceFleets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listdevicefleetspaginator)
        """

class ListDevicesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListDevices)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listdevicespaginator)
    """

    def paginate(
        self,
        *,
        LatestHeartbeatAfter: Union[datetime, str] = None,
        ModelName: str = None,
        DeviceFleetName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDevicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListDevices.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listdevicespaginator)
        """

class ListDomainsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListDomains)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listdomainspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDomainsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListDomains.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listdomainspaginator)
        """

class ListEdgeDeploymentPlansPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListEdgeDeploymentPlans)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listedgedeploymentplanspaginator)
    """

    def paginate(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        DeviceFleetNameContains: str = None,
        SortBy: ListEdgeDeploymentPlansSortByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEdgeDeploymentPlansResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListEdgeDeploymentPlans.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listedgedeploymentplanspaginator)
        """

class ListEdgePackagingJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListEdgePackagingJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listedgepackagingjobspaginator)
    """

    def paginate(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        ModelNameContains: str = None,
        StatusEquals: EdgePackagingJobStatusType = None,
        SortBy: ListEdgePackagingJobsSortByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEdgePackagingJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListEdgePackagingJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listedgepackagingjobspaginator)
        """

class ListEndpointConfigsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpointConfigs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listendpointconfigspaginator)
    """

    def paginate(
        self,
        *,
        SortBy: EndpointConfigSortKeyType = None,
        SortOrder: OrderKeyType = None,
        NameContains: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEndpointConfigsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpointConfigs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listendpointconfigspaginator)
        """

class ListEndpointsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpoints)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listendpointspaginator)
    """

    def paginate(
        self,
        *,
        SortBy: EndpointSortKeyType = None,
        SortOrder: OrderKeyType = None,
        NameContains: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        StatusEquals: EndpointStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEndpointsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpoints.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listendpointspaginator)
        """

class ListExperimentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListExperiments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listexperimentspaginator)
    """

    def paginate(
        self,
        *,
        CreatedAfter: Union[datetime, str] = None,
        CreatedBefore: Union[datetime, str] = None,
        SortBy: SortExperimentsByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListExperimentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListExperiments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listexperimentspaginator)
        """

class ListFeatureGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListFeatureGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listfeaturegroupspaginator)
    """

    def paginate(
        self,
        *,
        NameContains: str = None,
        FeatureGroupStatusEquals: FeatureGroupStatusType = None,
        OfflineStoreStatusEquals: OfflineStoreStatusValueType = None,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        SortOrder: FeatureGroupSortOrderType = None,
        SortBy: FeatureGroupSortByType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFeatureGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListFeatureGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listfeaturegroupspaginator)
        """

class ListFlowDefinitionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListFlowDefinitions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listflowdefinitionspaginator)
    """

    def paginate(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFlowDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListFlowDefinitions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listflowdefinitionspaginator)
        """

class ListHumanTaskUisPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListHumanTaskUis)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listhumantaskuispaginator)
    """

    def paginate(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHumanTaskUisResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListHumanTaskUis.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listhumantaskuispaginator)
        """

class ListHyperParameterTuningJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListHyperParameterTuningJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listhyperparametertuningjobspaginator)
    """

    def paginate(
        self,
        *,
        SortBy: HyperParameterTuningJobSortByOptionsType = None,
        SortOrder: SortOrderType = None,
        NameContains: str = None,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        StatusEquals: HyperParameterTuningJobStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHyperParameterTuningJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListHyperParameterTuningJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listhyperparametertuningjobspaginator)
        """

class ListImageVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListImageVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listimageversionspaginator)
    """

    def paginate(
        self,
        *,
        ImageName: str,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        SortBy: ImageVersionSortByType = None,
        SortOrder: ImageVersionSortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListImageVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListImageVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listimageversionspaginator)
        """

class ListImagesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListImages)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listimagespaginator)
    """

    def paginate(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        SortBy: ImageSortByType = None,
        SortOrder: ImageSortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListImagesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListImages.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listimagespaginator)
        """

class ListInferenceComponentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListInferenceComponents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listinferencecomponentspaginator)
    """

    def paginate(
        self,
        *,
        SortBy: InferenceComponentSortKeyType = None,
        SortOrder: OrderKeyType = None,
        NameContains: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        StatusEquals: InferenceComponentStatusType = None,
        EndpointNameEquals: str = None,
        VariantNameEquals: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInferenceComponentsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListInferenceComponents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listinferencecomponentspaginator)
        """

class ListInferenceExperimentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListInferenceExperiments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listinferenceexperimentspaginator)
    """

    def paginate(
        self,
        *,
        NameContains: str = None,
        Type: Literal["ShadowMode"] = None,
        StatusEquals: InferenceExperimentStatusType = None,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        SortBy: SortInferenceExperimentsByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInferenceExperimentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListInferenceExperiments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listinferenceexperimentspaginator)
        """

class ListInferenceRecommendationsJobStepsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListInferenceRecommendationsJobSteps)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listinferencerecommendationsjobstepspaginator)
    """

    def paginate(
        self,
        *,
        JobName: str,
        Status: RecommendationJobStatusType = None,
        StepType: Literal["BENCHMARK"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInferenceRecommendationsJobStepsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListInferenceRecommendationsJobSteps.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listinferencerecommendationsjobstepspaginator)
        """

class ListInferenceRecommendationsJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListInferenceRecommendationsJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listinferencerecommendationsjobspaginator)
    """

    def paginate(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        StatusEquals: RecommendationJobStatusType = None,
        SortBy: ListInferenceRecommendationsJobsSortByType = None,
        SortOrder: SortOrderType = None,
        ModelNameEquals: str = None,
        ModelPackageVersionArnEquals: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInferenceRecommendationsJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListInferenceRecommendationsJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listinferencerecommendationsjobspaginator)
        """

class ListLabelingJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listlabelingjobspaginator)
    """

    def paginate(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        SortBy: SortByType = None,
        SortOrder: SortOrderType = None,
        StatusEquals: LabelingJobStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLabelingJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listlabelingjobspaginator)
        """

class ListLabelingJobsForWorkteamPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobsForWorkteam)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listlabelingjobsforworkteampaginator)
    """

    def paginate(
        self,
        *,
        WorkteamArn: str,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        JobReferenceCodeContains: str = None,
        SortBy: Literal["CreationTime"] = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLabelingJobsForWorkteamResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobsForWorkteam.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listlabelingjobsforworkteampaginator)
        """

class ListLineageGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListLineageGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listlineagegroupspaginator)
    """

    def paginate(
        self,
        *,
        CreatedAfter: Union[datetime, str] = None,
        CreatedBefore: Union[datetime, str] = None,
        SortBy: SortLineageGroupsByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLineageGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListLineageGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listlineagegroupspaginator)
        """

class ListMlflowTrackingServersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListMlflowTrackingServers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmlflowtrackingserverspaginator)
    """

    def paginate(
        self,
        *,
        CreatedAfter: Union[datetime, str] = None,
        CreatedBefore: Union[datetime, str] = None,
        TrackingServerStatus: TrackingServerStatusType = None,
        MlflowVersion: str = None,
        SortBy: SortTrackingServerByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMlflowTrackingServersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListMlflowTrackingServers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmlflowtrackingserverspaginator)
        """

class ListModelBiasJobDefinitionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListModelBiasJobDefinitions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelbiasjobdefinitionspaginator)
    """

    def paginate(
        self,
        *,
        EndpointName: str = None,
        SortBy: MonitoringJobDefinitionSortKeyType = None,
        SortOrder: SortOrderType = None,
        NameContains: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListModelBiasJobDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListModelBiasJobDefinitions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelbiasjobdefinitionspaginator)
        """

class ListModelCardExportJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListModelCardExportJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelcardexportjobspaginator)
    """

    def paginate(
        self,
        *,
        ModelCardName: str,
        ModelCardVersion: int = None,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        ModelCardExportJobNameContains: str = None,
        StatusEquals: ModelCardExportJobStatusType = None,
        SortBy: ModelCardExportJobSortByType = None,
        SortOrder: ModelCardExportJobSortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListModelCardExportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListModelCardExportJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelcardexportjobspaginator)
        """

class ListModelCardVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListModelCardVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelcardversionspaginator)
    """

    def paginate(
        self,
        *,
        ModelCardName: str,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        ModelCardStatus: ModelCardStatusType = None,
        SortBy: Literal["Version"] = None,
        SortOrder: ModelCardSortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListModelCardVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListModelCardVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelcardversionspaginator)
        """

class ListModelCardsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListModelCards)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelcardspaginator)
    """

    def paginate(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        ModelCardStatus: ModelCardStatusType = None,
        SortBy: ModelCardSortByType = None,
        SortOrder: ModelCardSortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListModelCardsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListModelCards.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelcardspaginator)
        """

class ListModelExplainabilityJobDefinitionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListModelExplainabilityJobDefinitions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelexplainabilityjobdefinitionspaginator)
    """

    def paginate(
        self,
        *,
        EndpointName: str = None,
        SortBy: MonitoringJobDefinitionSortKeyType = None,
        SortOrder: SortOrderType = None,
        NameContains: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListModelExplainabilityJobDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListModelExplainabilityJobDefinitions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelexplainabilityjobdefinitionspaginator)
        """

class ListModelMetadataPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListModelMetadata)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelmetadatapaginator)
    """

    def paginate(
        self,
        *,
        SearchExpression: "ModelMetadataSearchExpressionTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListModelMetadataResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListModelMetadata.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelmetadatapaginator)
        """

class ListModelPackageGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListModelPackageGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelpackagegroupspaginator)
    """

    def paginate(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        SortBy: ModelPackageGroupSortByType = None,
        SortOrder: SortOrderType = None,
        CrossAccountFilterOption: CrossAccountFilterOptionType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListModelPackageGroupsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListModelPackageGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelpackagegroupspaginator)
        """

class ListModelPackagesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListModelPackages)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelpackagespaginator)
    """

    def paginate(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        ModelApprovalStatus: ModelApprovalStatusType = None,
        ModelPackageGroupName: str = None,
        ModelPackageType: ModelPackageTypeType = None,
        SortBy: ModelPackageSortByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListModelPackagesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListModelPackages.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelpackagespaginator)
        """

class ListModelQualityJobDefinitionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListModelQualityJobDefinitions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelqualityjobdefinitionspaginator)
    """

    def paginate(
        self,
        *,
        EndpointName: str = None,
        SortBy: MonitoringJobDefinitionSortKeyType = None,
        SortOrder: SortOrderType = None,
        NameContains: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListModelQualityJobDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListModelQualityJobDefinitions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelqualityjobdefinitionspaginator)
        """

class ListModelsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListModels)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelspaginator)
    """

    def paginate(
        self,
        *,
        SortBy: ModelSortKeyType = None,
        SortOrder: OrderKeyType = None,
        NameContains: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListModelsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListModels.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelspaginator)
        """

class ListMonitoringAlertHistoryPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringAlertHistory)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmonitoringalerthistorypaginator)
    """

    def paginate(
        self,
        *,
        MonitoringScheduleName: str = None,
        MonitoringAlertName: str = None,
        SortBy: MonitoringAlertHistorySortKeyType = None,
        SortOrder: SortOrderType = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        StatusEquals: MonitoringAlertStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMonitoringAlertHistoryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringAlertHistory.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmonitoringalerthistorypaginator)
        """

class ListMonitoringAlertsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringAlerts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmonitoringalertspaginator)
    """

    def paginate(
        self, *, MonitoringScheduleName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMonitoringAlertsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringAlerts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmonitoringalertspaginator)
        """

class ListMonitoringExecutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringExecutions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmonitoringexecutionspaginator)
    """

    def paginate(
        self,
        *,
        MonitoringScheduleName: str = None,
        EndpointName: str = None,
        SortBy: MonitoringExecutionSortKeyType = None,
        SortOrder: SortOrderType = None,
        ScheduledTimeBefore: Union[datetime, str] = None,
        ScheduledTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        StatusEquals: ExecutionStatusType = None,
        MonitoringJobDefinitionName: str = None,
        MonitoringTypeEquals: MonitoringTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMonitoringExecutionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringExecutions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmonitoringexecutionspaginator)
        """

class ListMonitoringSchedulesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringSchedules)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmonitoringschedulespaginator)
    """

    def paginate(
        self,
        *,
        EndpointName: str = None,
        SortBy: MonitoringScheduleSortKeyType = None,
        SortOrder: SortOrderType = None,
        NameContains: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        StatusEquals: ScheduleStatusType = None,
        MonitoringJobDefinitionName: str = None,
        MonitoringTypeEquals: MonitoringTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMonitoringSchedulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringSchedules.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmonitoringschedulespaginator)
        """

class ListNotebookInstanceLifecycleConfigsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstanceLifecycleConfigs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listnotebookinstancelifecycleconfigspaginator)
    """

    def paginate(
        self,
        *,
        SortBy: NotebookInstanceLifecycleConfigSortKeyType = None,
        SortOrder: NotebookInstanceLifecycleConfigSortOrderType = None,
        NameContains: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNotebookInstanceLifecycleConfigsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstanceLifecycleConfigs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listnotebookinstancelifecycleconfigspaginator)
        """

class ListNotebookInstancesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listnotebookinstancespaginator)
    """

    def paginate(
        self,
        *,
        SortBy: NotebookInstanceSortKeyType = None,
        SortOrder: NotebookInstanceSortOrderType = None,
        NameContains: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        StatusEquals: NotebookInstanceStatusType = None,
        NotebookInstanceLifecycleConfigNameContains: str = None,
        DefaultCodeRepositoryContains: str = None,
        AdditionalCodeRepositoryEquals: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNotebookInstancesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstances.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listnotebookinstancespaginator)
        """

class ListPipelineExecutionStepsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelineExecutionSteps)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listpipelineexecutionstepspaginator)
    """

    def paginate(
        self,
        *,
        PipelineExecutionArn: str = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPipelineExecutionStepsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelineExecutionSteps.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listpipelineexecutionstepspaginator)
        """

class ListPipelineExecutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelineExecutions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listpipelineexecutionspaginator)
    """

    def paginate(
        self,
        *,
        PipelineName: str,
        CreatedAfter: Union[datetime, str] = None,
        CreatedBefore: Union[datetime, str] = None,
        SortBy: SortPipelineExecutionsByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPipelineExecutionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelineExecutions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listpipelineexecutionspaginator)
        """

class ListPipelineParametersForExecutionPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelineParametersForExecution)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listpipelineparametersforexecutionpaginator)
    """

    def paginate(
        self, *, PipelineExecutionArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPipelineParametersForExecutionResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelineParametersForExecution.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listpipelineparametersforexecutionpaginator)
        """

class ListPipelinesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelines)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listpipelinespaginator)
    """

    def paginate(
        self,
        *,
        PipelineNamePrefix: str = None,
        CreatedAfter: Union[datetime, str] = None,
        CreatedBefore: Union[datetime, str] = None,
        SortBy: SortPipelinesByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPipelinesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelines.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listpipelinespaginator)
        """

class ListProcessingJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListProcessingJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listprocessingjobspaginator)
    """

    def paginate(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        StatusEquals: ProcessingJobStatusType = None,
        SortBy: SortByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProcessingJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListProcessingJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listprocessingjobspaginator)
        """

class ListResourceCatalogsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListResourceCatalogs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listresourcecatalogspaginator)
    """

    def paginate(
        self,
        *,
        NameContains: str = None,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        SortOrder: ResourceCatalogSortOrderType = None,
        SortBy: Literal["CreationTime"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourceCatalogsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListResourceCatalogs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listresourcecatalogspaginator)
        """

class ListSpacesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListSpaces)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listspacespaginator)
    """

    def paginate(
        self,
        *,
        SortOrder: SortOrderType = None,
        SortBy: SpaceSortKeyType = None,
        DomainIdEquals: str = None,
        SpaceNameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSpacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListSpaces.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listspacespaginator)
        """

class ListStageDevicesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListStageDevices)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#liststagedevicespaginator)
    """

    def paginate(
        self,
        *,
        EdgeDeploymentPlanName: str,
        StageName: str,
        ExcludeDevicesDeployedInOtherStage: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStageDevicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListStageDevices.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#liststagedevicespaginator)
        """

class ListStudioLifecycleConfigsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListStudioLifecycleConfigs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#liststudiolifecycleconfigspaginator)
    """

    def paginate(
        self,
        *,
        NameContains: str = None,
        AppTypeEquals: StudioLifecycleConfigAppTypeType = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        ModifiedTimeBefore: Union[datetime, str] = None,
        ModifiedTimeAfter: Union[datetime, str] = None,
        SortBy: StudioLifecycleConfigSortKeyType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStudioLifecycleConfigsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListStudioLifecycleConfigs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#liststudiolifecycleconfigspaginator)
        """

class ListSubscribedWorkteamsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListSubscribedWorkteams)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listsubscribedworkteamspaginator)
    """

    def paginate(
        self, *, NameContains: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSubscribedWorkteamsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListSubscribedWorkteams.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listsubscribedworkteamspaginator)
        """

class ListTagsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListTags)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listtagspaginator)
    """

    def paginate(
        self, *, ResourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListTags.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listtagspaginator)
        """

class ListTrainingJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listtrainingjobspaginator)
    """

    def paginate(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        StatusEquals: TrainingJobStatusType = None,
        SortBy: SortByType = None,
        SortOrder: SortOrderType = None,
        WarmPoolStatusEquals: WarmPoolResourceStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTrainingJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listtrainingjobspaginator)
        """

class ListTrainingJobsForHyperParameterTuningJobPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobsForHyperParameterTuningJob)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listtrainingjobsforhyperparametertuningjobpaginator)
    """

    def paginate(
        self,
        *,
        HyperParameterTuningJobName: str,
        StatusEquals: TrainingJobStatusType = None,
        SortBy: TrainingJobSortByOptionsType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTrainingJobsForHyperParameterTuningJobResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobsForHyperParameterTuningJob.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listtrainingjobsforhyperparametertuningjobpaginator)
        """

class ListTransformJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListTransformJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listtransformjobspaginator)
    """

    def paginate(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        StatusEquals: TransformJobStatusType = None,
        SortBy: SortByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTransformJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListTransformJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listtransformjobspaginator)
        """

class ListTrialComponentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListTrialComponents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listtrialcomponentspaginator)
    """

    def paginate(
        self,
        *,
        ExperimentName: str = None,
        TrialName: str = None,
        SourceArn: str = None,
        CreatedAfter: Union[datetime, str] = None,
        CreatedBefore: Union[datetime, str] = None,
        SortBy: SortTrialComponentsByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTrialComponentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListTrialComponents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listtrialcomponentspaginator)
        """

class ListTrialsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListTrials)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listtrialspaginator)
    """

    def paginate(
        self,
        *,
        ExperimentName: str = None,
        TrialComponentName: str = None,
        CreatedAfter: Union[datetime, str] = None,
        CreatedBefore: Union[datetime, str] = None,
        SortBy: SortTrialsByType = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTrialsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListTrials.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listtrialspaginator)
        """

class ListUserProfilesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListUserProfiles)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listuserprofilespaginator)
    """

    def paginate(
        self,
        *,
        SortOrder: SortOrderType = None,
        SortBy: UserProfileSortKeyType = None,
        DomainIdEquals: str = None,
        UserProfileNameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUserProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListUserProfiles.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listuserprofilespaginator)
        """

class ListWorkforcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkforces)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listworkforcespaginator)
    """

    def paginate(
        self,
        *,
        SortBy: ListWorkforcesSortByOptionsType = None,
        SortOrder: SortOrderType = None,
        NameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorkforcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkforces.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listworkforcespaginator)
        """

class ListWorkteamsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkteams)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listworkteamspaginator)
    """

    def paginate(
        self,
        *,
        SortBy: ListWorkteamsSortByOptionsType = None,
        SortOrder: SortOrderType = None,
        NameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorkteamsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkteams.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listworkteamspaginator)
        """

class SearchPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.Search)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#searchpaginator)
    """

    def paginate(
        self,
        *,
        Resource: ResourceTypeType,
        SearchExpression: "SearchExpressionTypeDef" = None,
        SortBy: str = None,
        SortOrder: SearchSortOrderType = None,
        CrossAccountFilterOption: CrossAccountFilterOptionType = None,
        VisibilityConditions: List["VisibilityConditionsTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sagemaker.html#SageMaker.Paginator.Search.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#searchpaginator)
        """
