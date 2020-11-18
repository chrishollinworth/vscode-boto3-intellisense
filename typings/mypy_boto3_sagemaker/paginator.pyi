# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for sagemaker service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_sagemaker import SageMakerClient
    from mypy_boto3_sagemaker.paginator import (
        ListAlgorithmsPaginator,
        ListAppsPaginator,
        ListAutoMLJobsPaginator,
        ListCandidatesForAutoMLJobPaginator,
        ListCodeRepositoriesPaginator,
        ListCompilationJobsPaginator,
        ListDomainsPaginator,
        ListEndpointConfigsPaginator,
        ListEndpointsPaginator,
        ListExperimentsPaginator,
        ListFlowDefinitionsPaginator,
        ListHumanTaskUisPaginator,
        ListHyperParameterTuningJobsPaginator,
        ListImageVersionsPaginator,
        ListImagesPaginator,
        ListLabelingJobsPaginator,
        ListLabelingJobsForWorkteamPaginator,
        ListModelPackagesPaginator,
        ListModelsPaginator,
        ListMonitoringExecutionsPaginator,
        ListMonitoringSchedulesPaginator,
        ListNotebookInstanceLifecycleConfigsPaginator,
        ListNotebookInstancesPaginator,
        ListProcessingJobsPaginator,
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

    list_algorithms_paginator: ListAlgorithmsPaginator = client.get_paginator("list_algorithms")
    list_apps_paginator: ListAppsPaginator = client.get_paginator("list_apps")
    list_auto_ml_jobs_paginator: ListAutoMLJobsPaginator = client.get_paginator("list_auto_ml_jobs")
    list_candidates_for_auto_ml_job_paginator: ListCandidatesForAutoMLJobPaginator = client.get_paginator("list_candidates_for_auto_ml_job")
    list_code_repositories_paginator: ListCodeRepositoriesPaginator = client.get_paginator("list_code_repositories")
    list_compilation_jobs_paginator: ListCompilationJobsPaginator = client.get_paginator("list_compilation_jobs")
    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    list_endpoint_configs_paginator: ListEndpointConfigsPaginator = client.get_paginator("list_endpoint_configs")
    list_endpoints_paginator: ListEndpointsPaginator = client.get_paginator("list_endpoints")
    list_experiments_paginator: ListExperimentsPaginator = client.get_paginator("list_experiments")
    list_flow_definitions_paginator: ListFlowDefinitionsPaginator = client.get_paginator("list_flow_definitions")
    list_human_task_uis_paginator: ListHumanTaskUisPaginator = client.get_paginator("list_human_task_uis")
    list_hyper_parameter_tuning_jobs_paginator: ListHyperParameterTuningJobsPaginator = client.get_paginator("list_hyper_parameter_tuning_jobs")
    list_image_versions_paginator: ListImageVersionsPaginator = client.get_paginator("list_image_versions")
    list_images_paginator: ListImagesPaginator = client.get_paginator("list_images")
    list_labeling_jobs_paginator: ListLabelingJobsPaginator = client.get_paginator("list_labeling_jobs")
    list_labeling_jobs_for_workteam_paginator: ListLabelingJobsForWorkteamPaginator = client.get_paginator("list_labeling_jobs_for_workteam")
    list_model_packages_paginator: ListModelPackagesPaginator = client.get_paginator("list_model_packages")
    list_models_paginator: ListModelsPaginator = client.get_paginator("list_models")
    list_monitoring_executions_paginator: ListMonitoringExecutionsPaginator = client.get_paginator("list_monitoring_executions")
    list_monitoring_schedules_paginator: ListMonitoringSchedulesPaginator = client.get_paginator("list_monitoring_schedules")
    list_notebook_instance_lifecycle_configs_paginator: ListNotebookInstanceLifecycleConfigsPaginator = client.get_paginator("list_notebook_instance_lifecycle_configs")
    list_notebook_instances_paginator: ListNotebookInstancesPaginator = client.get_paginator("list_notebook_instances")
    list_processing_jobs_paginator: ListProcessingJobsPaginator = client.get_paginator("list_processing_jobs")
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
from typing import Any, Dict, Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_sagemaker.type_defs import (
    ListAlgorithmsOutputTypeDef,
    ListAppsResponseTypeDef,
    ListAutoMLJobsResponseTypeDef,
    ListCandidatesForAutoMLJobResponseTypeDef,
    ListCodeRepositoriesOutputTypeDef,
    ListCompilationJobsResponseTypeDef,
    ListDomainsResponseTypeDef,
    ListEndpointConfigsOutputTypeDef,
    ListEndpointsOutputTypeDef,
    ListExperimentsResponseTypeDef,
    ListFlowDefinitionsResponseTypeDef,
    ListHumanTaskUisResponseTypeDef,
    ListHyperParameterTuningJobsResponseTypeDef,
    ListImagesResponseTypeDef,
    ListImageVersionsResponseTypeDef,
    ListLabelingJobsForWorkteamResponseTypeDef,
    ListLabelingJobsResponseTypeDef,
    ListModelPackagesOutputTypeDef,
    ListModelsOutputTypeDef,
    ListMonitoringExecutionsResponseTypeDef,
    ListMonitoringSchedulesResponseTypeDef,
    ListNotebookInstanceLifecycleConfigsOutputTypeDef,
    ListNotebookInstancesOutputTypeDef,
    ListProcessingJobsResponseTypeDef,
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
    PaginatorConfigTypeDef,
    SearchResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAlgorithmsPaginator",
    "ListAppsPaginator",
    "ListAutoMLJobsPaginator",
    "ListCandidatesForAutoMLJobPaginator",
    "ListCodeRepositoriesPaginator",
    "ListCompilationJobsPaginator",
    "ListDomainsPaginator",
    "ListEndpointConfigsPaginator",
    "ListEndpointsPaginator",
    "ListExperimentsPaginator",
    "ListFlowDefinitionsPaginator",
    "ListHumanTaskUisPaginator",
    "ListHyperParameterTuningJobsPaginator",
    "ListImageVersionsPaginator",
    "ListImagesPaginator",
    "ListLabelingJobsPaginator",
    "ListLabelingJobsForWorkteamPaginator",
    "ListModelPackagesPaginator",
    "ListModelsPaginator",
    "ListMonitoringExecutionsPaginator",
    "ListMonitoringSchedulesPaginator",
    "ListNotebookInstanceLifecycleConfigsPaginator",
    "ListNotebookInstancesPaginator",
    "ListProcessingJobsPaginator",
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


class ListAlgorithmsPaginator(Boto3Paginator):
    """
    [Paginator.ListAlgorithms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListAlgorithms)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAlgorithmsOutputTypeDef]:
        """
        [ListAlgorithms.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListAlgorithms.paginate)
        """


class ListAppsPaginator(Boto3Paginator):
    """
    [Paginator.ListApps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListApps)
    """

    def paginate(
        self,
        SortOrder: Literal["Ascending", "Descending"] = None,
        SortBy: Literal["CreationTime"] = None,
        DomainIdEquals: str = None,
        UserProfileNameEquals: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAppsResponseTypeDef]:
        """
        [ListApps.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListApps.paginate)
        """


class ListAutoMLJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListAutoMLJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListAutoMLJobs)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: Literal["Completed", "InProgress", "Failed", "Stopped", "Stopping"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAutoMLJobsResponseTypeDef]:
        """
        [ListAutoMLJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListAutoMLJobs.paginate)
        """


class ListCandidatesForAutoMLJobPaginator(Boto3Paginator):
    """
    [Paginator.ListCandidatesForAutoMLJob documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListCandidatesForAutoMLJob)
    """

    def paginate(
        self,
        AutoMLJobName: str,
        StatusEquals: Literal["Completed", "InProgress", "Failed", "Stopped", "Stopping"] = None,
        CandidateNameEquals: str = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        SortBy: Literal["CreationTime", "Status", "FinalObjectiveMetricValue"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListCandidatesForAutoMLJobResponseTypeDef]:
        """
        [ListCandidatesForAutoMLJob.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListCandidatesForAutoMLJob.paginate)
        """


class ListCodeRepositoriesPaginator(Boto3Paginator):
    """
    [Paginator.ListCodeRepositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListCodeRepositories)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: Literal["Name", "CreationTime", "LastModifiedTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListCodeRepositoriesOutputTypeDef]:
        """
        [ListCodeRepositories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListCodeRepositories.paginate)
        """


class ListCompilationJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListCompilationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListCompilationJobs)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: Literal[
            "INPROGRESS", "COMPLETED", "FAILED", "STARTING", "STOPPING", "STOPPED"
        ] = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListCompilationJobsResponseTypeDef]:
        """
        [ListCompilationJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListCompilationJobs.paginate)
        """


class ListDomainsPaginator(Boto3Paginator):
    """
    [Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListDomains)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDomainsResponseTypeDef]:
        """
        [ListDomains.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListDomains.paginate)
        """


class ListEndpointConfigsPaginator(Boto3Paginator):
    """
    [Paginator.ListEndpointConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpointConfigs)
    """

    def paginate(
        self,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListEndpointConfigsOutputTypeDef]:
        """
        [ListEndpointConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpointConfigs.paginate)
        """


class ListEndpointsPaginator(Boto3Paginator):
    """
    [Paginator.ListEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpoints)
    """

    def paginate(
        self,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: Literal[
            "OutOfService",
            "Creating",
            "Updating",
            "SystemUpdating",
            "RollingBack",
            "InService",
            "Deleting",
            "Failed",
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListEndpointsOutputTypeDef]:
        """
        [ListEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpoints.paginate)
        """


class ListExperimentsPaginator(Boto3Paginator):
    """
    [Paginator.ListExperiments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListExperiments)
    """

    def paginate(
        self,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListExperimentsResponseTypeDef]:
        """
        [ListExperiments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListExperiments.paginate)
        """


class ListFlowDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.ListFlowDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListFlowDefinitions)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListFlowDefinitionsResponseTypeDef]:
        """
        [ListFlowDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListFlowDefinitions.paginate)
        """


class ListHumanTaskUisPaginator(Boto3Paginator):
    """
    [Paginator.ListHumanTaskUis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListHumanTaskUis)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListHumanTaskUisResponseTypeDef]:
        """
        [ListHumanTaskUis.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListHumanTaskUis.paginate)
        """


class ListHyperParameterTuningJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListHyperParameterTuningJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListHyperParameterTuningJobs)
    """

    def paginate(
        self,
        SortBy: Literal["Name", "Status", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        StatusEquals: Literal["Completed", "InProgress", "Failed", "Stopped", "Stopping"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListHyperParameterTuningJobsResponseTypeDef]:
        """
        [ListHyperParameterTuningJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListHyperParameterTuningJobs.paginate)
        """


class ListImageVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListImageVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListImageVersions)
    """

    def paginate(
        self,
        ImageName: str,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        SortBy: Literal["CREATION_TIME", "LAST_MODIFIED_TIME", "VERSION"] = None,
        SortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListImageVersionsResponseTypeDef]:
        """
        [ListImageVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListImageVersions.paginate)
        """


class ListImagesPaginator(Boto3Paginator):
    """
    [Paginator.ListImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListImages)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: Literal["CREATION_TIME", "LAST_MODIFIED_TIME", "IMAGE_NAME"] = None,
        SortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListImagesResponseTypeDef]:
        """
        [ListImages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListImages.paginate)
        """


class ListLabelingJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListLabelingJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobs)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        StatusEquals: Literal[
            "Initializing", "InProgress", "Completed", "Failed", "Stopping", "Stopped"
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListLabelingJobsResponseTypeDef]:
        """
        [ListLabelingJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobs.paginate)
        """


class ListLabelingJobsForWorkteamPaginator(Boto3Paginator):
    """
    [Paginator.ListLabelingJobsForWorkteam documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobsForWorkteam)
    """

    def paginate(
        self,
        WorkteamArn: str,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        JobReferenceCodeContains: str = None,
        SortBy: Literal["CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListLabelingJobsForWorkteamResponseTypeDef]:
        """
        [ListLabelingJobsForWorkteam.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobsForWorkteam.paginate)
        """


class ListModelPackagesPaginator(Boto3Paginator):
    """
    [Paginator.ListModelPackages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListModelPackages)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListModelPackagesOutputTypeDef]:
        """
        [ListModelPackages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListModelPackages.paginate)
        """


class ListModelsPaginator(Boto3Paginator):
    """
    [Paginator.ListModels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListModels)
    """

    def paginate(
        self,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListModelsOutputTypeDef]:
        """
        [ListModels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListModels.paginate)
        """


class ListMonitoringExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.ListMonitoringExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringExecutions)
    """

    def paginate(
        self,
        MonitoringScheduleName: str = None,
        EndpointName: str = None,
        SortBy: Literal["CreationTime", "ScheduledTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        ScheduledTimeBefore: datetime = None,
        ScheduledTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: Literal[
            "Pending",
            "Completed",
            "CompletedWithViolations",
            "InProgress",
            "Failed",
            "Stopping",
            "Stopped",
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListMonitoringExecutionsResponseTypeDef]:
        """
        [ListMonitoringExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringExecutions.paginate)
        """


class ListMonitoringSchedulesPaginator(Boto3Paginator):
    """
    [Paginator.ListMonitoringSchedules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringSchedules)
    """

    def paginate(
        self,
        EndpointName: str = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: Literal["Pending", "Failed", "Scheduled", "Stopped"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListMonitoringSchedulesResponseTypeDef]:
        """
        [ListMonitoringSchedules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringSchedules.paginate)
        """


class ListNotebookInstanceLifecycleConfigsPaginator(Boto3Paginator):
    """
    [Paginator.ListNotebookInstanceLifecycleConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstanceLifecycleConfigs)
    """

    def paginate(
        self,
        SortBy: Literal["Name", "CreationTime", "LastModifiedTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListNotebookInstanceLifecycleConfigsOutputTypeDef]:
        """
        [ListNotebookInstanceLifecycleConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstanceLifecycleConfigs.paginate)
        """


class ListNotebookInstancesPaginator(Boto3Paginator):
    """
    [Paginator.ListNotebookInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstances)
    """

    def paginate(
        self,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: Literal[
            "Pending", "InService", "Stopping", "Stopped", "Failed", "Deleting", "Updating"
        ] = None,
        NotebookInstanceLifecycleConfigNameContains: str = None,
        DefaultCodeRepositoryContains: str = None,
        AdditionalCodeRepositoryEquals: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListNotebookInstancesOutputTypeDef]:
        """
        [ListNotebookInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstances.paginate)
        """


class ListProcessingJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListProcessingJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListProcessingJobs)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"] = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListProcessingJobsResponseTypeDef]:
        """
        [ListProcessingJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListProcessingJobs.paginate)
        """


class ListSubscribedWorkteamsPaginator(Boto3Paginator):
    """
    [Paginator.ListSubscribedWorkteams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListSubscribedWorkteams)
    """

    def paginate(
        self, NameContains: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSubscribedWorkteamsResponseTypeDef]:
        """
        [ListSubscribedWorkteams.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListSubscribedWorkteams.paginate)
        """


class ListTagsPaginator(Boto3Paginator):
    """
    [Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListTags)
    """

    def paginate(
        self, ResourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsOutputTypeDef]:
        """
        [ListTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListTags.paginate)
        """


class ListTrainingJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListTrainingJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobs)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"] = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTrainingJobsResponseTypeDef]:
        """
        [ListTrainingJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobs.paginate)
        """


class ListTrainingJobsForHyperParameterTuningJobPaginator(Boto3Paginator):
    """
    [Paginator.ListTrainingJobsForHyperParameterTuningJob documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobsForHyperParameterTuningJob)
    """

    def paginate(
        self,
        HyperParameterTuningJobName: str,
        StatusEquals: Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"] = None,
        SortBy: Literal["Name", "CreationTime", "Status", "FinalObjectiveMetricValue"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTrainingJobsForHyperParameterTuningJobResponseTypeDef]:
        """
        [ListTrainingJobsForHyperParameterTuningJob.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobsForHyperParameterTuningJob.paginate)
        """


class ListTransformJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListTransformJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListTransformJobs)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"] = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTransformJobsResponseTypeDef]:
        """
        [ListTransformJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListTransformJobs.paginate)
        """


class ListTrialComponentsPaginator(Boto3Paginator):
    """
    [Paginator.ListTrialComponents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListTrialComponents)
    """

    def paginate(
        self,
        ExperimentName: str = None,
        TrialName: str = None,
        SourceArn: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTrialComponentsResponseTypeDef]:
        """
        [ListTrialComponents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListTrialComponents.paginate)
        """


class ListTrialsPaginator(Boto3Paginator):
    """
    [Paginator.ListTrials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListTrials)
    """

    def paginate(
        self,
        ExperimentName: str = None,
        TrialComponentName: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTrialsResponseTypeDef]:
        """
        [ListTrials.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListTrials.paginate)
        """


class ListUserProfilesPaginator(Boto3Paginator):
    """
    [Paginator.ListUserProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListUserProfiles)
    """

    def paginate(
        self,
        SortOrder: Literal["Ascending", "Descending"] = None,
        SortBy: Literal["CreationTime", "LastModifiedTime"] = None,
        DomainIdEquals: str = None,
        UserProfileNameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListUserProfilesResponseTypeDef]:
        """
        [ListUserProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListUserProfiles.paginate)
        """


class ListWorkforcesPaginator(Boto3Paginator):
    """
    [Paginator.ListWorkforces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkforces)
    """

    def paginate(
        self,
        SortBy: Literal["Name", "CreateDate"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListWorkforcesResponseTypeDef]:
        """
        [ListWorkforces.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkforces.paginate)
        """


class ListWorkteamsPaginator(Boto3Paginator):
    """
    [Paginator.ListWorkteams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkteams)
    """

    def paginate(
        self,
        SortBy: Literal["Name", "CreateDate"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListWorkteamsResponseTypeDef]:
        """
        [ListWorkteams.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkteams.paginate)
        """


class SearchPaginator(Boto3Paginator):
    """
    [Paginator.Search documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.Search)
    """

    def paginate(
        self,
        Resource: Literal[
            "TrainingJob", "Experiment", "ExperimentTrial", "ExperimentTrialComponent"
        ],
        SearchExpression: Dict[str, Any] = None,
        SortBy: str = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[SearchResponseTypeDef]:
        """
        [Search.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.Search.paginate)
        """
