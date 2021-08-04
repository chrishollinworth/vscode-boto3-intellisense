"""
Type annotations for sagemaker service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/literals.html)

Usage::

    ```python
    from mypy_boto3_sagemaker.literals import ActionStatusType

    data: ActionStatusType = "Completed"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActionStatusType",
    "AlgorithmSortByType",
    "AlgorithmStatusType",
    "AppImageConfigSortKeyType",
    "AppInstanceTypeType",
    "AppNetworkAccessTypeType",
    "AppSortKeyType",
    "AppStatusType",
    "AppTypeType",
    "ArtifactSourceIdTypeType",
    "AssemblyTypeType",
    "AssociationEdgeTypeType",
    "AthenaResultCompressionTypeType",
    "AthenaResultFormatType",
    "AuthModeType",
    "AutoMLJobObjectiveTypeType",
    "AutoMLJobSecondaryStatusType",
    "AutoMLJobStatusType",
    "AutoMLMetricEnumType",
    "AutoMLS3DataTypeType",
    "AutoMLSortByType",
    "AutoMLSortOrderType",
    "AwsManagedHumanLoopRequestSourceType",
    "BatchStrategyType",
    "BooleanOperatorType",
    "CandidateSortByType",
    "CandidateStatusType",
    "CandidateStepTypeType",
    "CapacitySizeTypeType",
    "CaptureModeType",
    "CaptureStatusType",
    "CodeRepositorySortByType",
    "CodeRepositorySortOrderType",
    "CompilationJobStatusType",
    "CompressionTypeType",
    "ConditionOutcomeType",
    "ContainerModeType",
    "ContentClassifierType",
    "DataDistributionTypeType",
    "DetailedAlgorithmStatusType",
    "DetailedModelPackageStatusType",
    "DirectInternetAccessType",
    "DomainStatusType",
    "EdgePackagingJobStatusType",
    "EdgePresetDeploymentStatusType",
    "EdgePresetDeploymentTypeType",
    "EndpointConfigSortKeyType",
    "EndpointDeletedWaiterName",
    "EndpointInServiceWaiterName",
    "EndpointSortKeyType",
    "EndpointStatusType",
    "ExecutionStatusType",
    "FeatureGroupSortByType",
    "FeatureGroupSortOrderType",
    "FeatureGroupStatusType",
    "FeatureTypeType",
    "FileSystemAccessModeType",
    "FileSystemTypeType",
    "FlowDefinitionStatusType",
    "FrameworkType",
    "HumanTaskUiStatusType",
    "HyperParameterScalingTypeType",
    "HyperParameterTuningJobObjectiveTypeType",
    "HyperParameterTuningJobSortByOptionsType",
    "HyperParameterTuningJobStatusType",
    "HyperParameterTuningJobStrategyTypeType",
    "HyperParameterTuningJobWarmStartTypeType",
    "ImageCreatedWaiterName",
    "ImageDeletedWaiterName",
    "ImageSortByType",
    "ImageSortOrderType",
    "ImageStatusType",
    "ImageUpdatedWaiterName",
    "ImageVersionCreatedWaiterName",
    "ImageVersionDeletedWaiterName",
    "ImageVersionSortByType",
    "ImageVersionSortOrderType",
    "ImageVersionStatusType",
    "InferenceExecutionModeType",
    "InputModeType",
    "InstanceTypeType",
    "JoinSourceType",
    "LabelingJobStatusType",
    "ListActionsPaginatorName",
    "ListAlgorithmsPaginatorName",
    "ListAppImageConfigsPaginatorName",
    "ListAppsPaginatorName",
    "ListArtifactsPaginatorName",
    "ListAssociationsPaginatorName",
    "ListAutoMLJobsPaginatorName",
    "ListCandidatesForAutoMLJobPaginatorName",
    "ListCodeRepositoriesPaginatorName",
    "ListCompilationJobsPaginatorName",
    "ListCompilationJobsSortByType",
    "ListContextsPaginatorName",
    "ListDataQualityJobDefinitionsPaginatorName",
    "ListDeviceFleetsPaginatorName",
    "ListDeviceFleetsSortByType",
    "ListDevicesPaginatorName",
    "ListDomainsPaginatorName",
    "ListEdgePackagingJobsPaginatorName",
    "ListEdgePackagingJobsSortByType",
    "ListEndpointConfigsPaginatorName",
    "ListEndpointsPaginatorName",
    "ListExperimentsPaginatorName",
    "ListFeatureGroupsPaginatorName",
    "ListFlowDefinitionsPaginatorName",
    "ListHumanTaskUisPaginatorName",
    "ListHyperParameterTuningJobsPaginatorName",
    "ListImageVersionsPaginatorName",
    "ListImagesPaginatorName",
    "ListLabelingJobsForWorkteamPaginatorName",
    "ListLabelingJobsForWorkteamSortByOptionsType",
    "ListLabelingJobsPaginatorName",
    "ListModelBiasJobDefinitionsPaginatorName",
    "ListModelExplainabilityJobDefinitionsPaginatorName",
    "ListModelPackageGroupsPaginatorName",
    "ListModelPackagesPaginatorName",
    "ListModelQualityJobDefinitionsPaginatorName",
    "ListModelsPaginatorName",
    "ListMonitoringExecutionsPaginatorName",
    "ListMonitoringSchedulesPaginatorName",
    "ListNotebookInstanceLifecycleConfigsPaginatorName",
    "ListNotebookInstancesPaginatorName",
    "ListPipelineExecutionStepsPaginatorName",
    "ListPipelineExecutionsPaginatorName",
    "ListPipelineParametersForExecutionPaginatorName",
    "ListPipelinesPaginatorName",
    "ListProcessingJobsPaginatorName",
    "ListSubscribedWorkteamsPaginatorName",
    "ListTagsPaginatorName",
    "ListTrainingJobsForHyperParameterTuningJobPaginatorName",
    "ListTrainingJobsPaginatorName",
    "ListTransformJobsPaginatorName",
    "ListTrialComponentsPaginatorName",
    "ListTrialsPaginatorName",
    "ListUserProfilesPaginatorName",
    "ListWorkforcesPaginatorName",
    "ListWorkforcesSortByOptionsType",
    "ListWorkteamsPaginatorName",
    "ListWorkteamsSortByOptionsType",
    "ModelApprovalStatusType",
    "ModelCacheSettingType",
    "ModelPackageGroupSortByType",
    "ModelPackageGroupStatusType",
    "ModelPackageSortByType",
    "ModelPackageStatusType",
    "ModelPackageTypeType",
    "ModelSortKeyType",
    "MonitoringExecutionSortKeyType",
    "MonitoringJobDefinitionSortKeyType",
    "MonitoringProblemTypeType",
    "MonitoringScheduleSortKeyType",
    "MonitoringTypeType",
    "NotebookInstanceAcceleratorTypeType",
    "NotebookInstanceDeletedWaiterName",
    "NotebookInstanceInServiceWaiterName",
    "NotebookInstanceLifecycleConfigSortKeyType",
    "NotebookInstanceLifecycleConfigSortOrderType",
    "NotebookInstanceSortKeyType",
    "NotebookInstanceSortOrderType",
    "NotebookInstanceStatusType",
    "NotebookInstanceStoppedWaiterName",
    "NotebookOutputOptionType",
    "ObjectiveStatusType",
    "OfflineStoreStatusValueType",
    "OperatorType",
    "OrderKeyType",
    "ParameterTypeType",
    "PipelineExecutionStatusType",
    "PipelineStatusType",
    "ProblemTypeType",
    "ProcessingInstanceTypeType",
    "ProcessingJobCompletedOrStoppedWaiterName",
    "ProcessingJobStatusType",
    "ProcessingS3CompressionTypeType",
    "ProcessingS3DataDistributionTypeType",
    "ProcessingS3DataTypeType",
    "ProcessingS3InputModeType",
    "ProcessingS3UploadModeType",
    "ProductionVariantAcceleratorTypeType",
    "ProductionVariantInstanceTypeType",
    "ProfilingStatusType",
    "ProjectSortByType",
    "ProjectSortOrderType",
    "ProjectStatusType",
    "RecordWrapperType",
    "RedshiftResultCompressionTypeType",
    "RedshiftResultFormatType",
    "RepositoryAccessModeType",
    "ResourceTypeType",
    "RetentionTypeType",
    "RootAccessType",
    "RuleEvaluationStatusType",
    "S3DataDistributionType",
    "S3DataTypeType",
    "SagemakerServicecatalogStatusType",
    "ScheduleStatusType",
    "SearchPaginatorName",
    "SearchSortOrderType",
    "SecondaryStatusType",
    "SortActionsByType",
    "SortArtifactsByType",
    "SortAssociationsByType",
    "SortByType",
    "SortContextsByType",
    "SortExperimentsByType",
    "SortOrderType",
    "SortPipelineExecutionsByType",
    "SortPipelinesByType",
    "SortTrialComponentsByType",
    "SortTrialsByType",
    "SplitTypeType",
    "StepStatusType",
    "TargetDeviceType",
    "TargetPlatformAcceleratorType",
    "TargetPlatformArchType",
    "TargetPlatformOsType",
    "TrafficRoutingConfigTypeType",
    "TrainingInputModeType",
    "TrainingInstanceTypeType",
    "TrainingJobCompletedOrStoppedWaiterName",
    "TrainingJobEarlyStoppingTypeType",
    "TrainingJobSortByOptionsType",
    "TrainingJobStatusType",
    "TransformInstanceTypeType",
    "TransformJobCompletedOrStoppedWaiterName",
    "TransformJobStatusType",
    "TrialComponentPrimaryStatusType",
    "UserProfileSortKeyType",
    "UserProfileStatusType",
    "VariantPropertyTypeType",
)

ActionStatusType = Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping", "Unknown"]
AlgorithmSortByType = Literal["CreationTime", "Name"]
AlgorithmStatusType = Literal["Completed", "Deleting", "Failed", "InProgress", "Pending"]
AppImageConfigSortKeyType = Literal["CreationTime", "LastModifiedTime", "Name"]
AppInstanceTypeType = Literal[
    "ml.c5.12xlarge",
    "ml.c5.18xlarge",
    "ml.c5.24xlarge",
    "ml.c5.2xlarge",
    "ml.c5.4xlarge",
    "ml.c5.9xlarge",
    "ml.c5.large",
    "ml.c5.xlarge",
    "ml.g4dn.12xlarge",
    "ml.g4dn.16xlarge",
    "ml.g4dn.2xlarge",
    "ml.g4dn.4xlarge",
    "ml.g4dn.8xlarge",
    "ml.g4dn.xlarge",
    "ml.m5.12xlarge",
    "ml.m5.16xlarge",
    "ml.m5.24xlarge",
    "ml.m5.2xlarge",
    "ml.m5.4xlarge",
    "ml.m5.8xlarge",
    "ml.m5.large",
    "ml.m5.xlarge",
    "ml.m5d.12xlarge",
    "ml.m5d.16xlarge",
    "ml.m5d.24xlarge",
    "ml.m5d.2xlarge",
    "ml.m5d.4xlarge",
    "ml.m5d.8xlarge",
    "ml.m5d.large",
    "ml.m5d.xlarge",
    "ml.p3.16xlarge",
    "ml.p3.2xlarge",
    "ml.p3.8xlarge",
    "ml.p3dn.24xlarge",
    "ml.r5.12xlarge",
    "ml.r5.16xlarge",
    "ml.r5.24xlarge",
    "ml.r5.2xlarge",
    "ml.r5.4xlarge",
    "ml.r5.8xlarge",
    "ml.r5.large",
    "ml.r5.xlarge",
    "ml.t3.2xlarge",
    "ml.t3.large",
    "ml.t3.medium",
    "ml.t3.micro",
    "ml.t3.small",
    "ml.t3.xlarge",
    "system",
]
AppNetworkAccessTypeType = Literal["PublicInternetOnly", "VpcOnly"]
AppSortKeyType = Literal["CreationTime"]
AppStatusType = Literal["Deleted", "Deleting", "Failed", "InService", "Pending"]
AppTypeType = Literal["JupyterServer", "KernelGateway", "TensorBoard"]
ArtifactSourceIdTypeType = Literal["Custom", "MD5Hash", "S3ETag", "S3Version"]
AssemblyTypeType = Literal["Line", "None"]
AssociationEdgeTypeType = Literal["AssociatedWith", "ContributedTo", "DerivedFrom", "Produced"]
AthenaResultCompressionTypeType = Literal["GZIP", "SNAPPY", "ZLIB"]
AthenaResultFormatType = Literal["AVRO", "JSON", "ORC", "PARQUET", "TEXTFILE"]
AuthModeType = Literal["IAM", "SSO"]
AutoMLJobObjectiveTypeType = Literal["Maximize", "Minimize"]
AutoMLJobSecondaryStatusType = Literal[
    "AnalyzingData",
    "CandidateDefinitionsGenerated",
    "Completed",
    "DeployingModel",
    "ExplainabilityError",
    "Failed",
    "FeatureEngineering",
    "GeneratingExplainabilityReport",
    "MaxAutoMLJobRuntimeReached",
    "MaxCandidatesReached",
    "ModelDeploymentError",
    "ModelTuning",
    "Starting",
    "Stopped",
    "Stopping",
]
AutoMLJobStatusType = Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
AutoMLMetricEnumType = Literal["AUC", "Accuracy", "F1", "F1macro", "MSE"]
AutoMLS3DataTypeType = Literal["ManifestFile", "S3Prefix"]
AutoMLSortByType = Literal["CreationTime", "Name", "Status"]
AutoMLSortOrderType = Literal["Ascending", "Descending"]
AwsManagedHumanLoopRequestSourceType = Literal[
    "AWS/Rekognition/DetectModerationLabels/Image/V3", "AWS/Textract/AnalyzeDocument/Forms/V1"
]
BatchStrategyType = Literal["MultiRecord", "SingleRecord"]
BooleanOperatorType = Literal["And", "Or"]
CandidateSortByType = Literal["CreationTime", "FinalObjectiveMetricValue", "Status"]
CandidateStatusType = Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
CandidateStepTypeType = Literal[
    "AWS::SageMaker::ProcessingJob", "AWS::SageMaker::TrainingJob", "AWS::SageMaker::TransformJob"
]
CapacitySizeTypeType = Literal["CAPACITY_PERCENT", "INSTANCE_COUNT"]
CaptureModeType = Literal["Input", "Output"]
CaptureStatusType = Literal["Started", "Stopped"]
CodeRepositorySortByType = Literal["CreationTime", "LastModifiedTime", "Name"]
CodeRepositorySortOrderType = Literal["Ascending", "Descending"]
CompilationJobStatusType = Literal[
    "COMPLETED", "FAILED", "INPROGRESS", "STARTING", "STOPPED", "STOPPING"
]
CompressionTypeType = Literal["Gzip", "None"]
ConditionOutcomeType = Literal["False", "True"]
ContainerModeType = Literal["MultiModel", "SingleModel"]
ContentClassifierType = Literal["FreeOfAdultContent", "FreeOfPersonallyIdentifiableInformation"]
DataDistributionTypeType = Literal["FullyReplicated", "ShardedByS3Key"]
DetailedAlgorithmStatusType = Literal["Completed", "Failed", "InProgress", "NotStarted"]
DetailedModelPackageStatusType = Literal["Completed", "Failed", "InProgress", "NotStarted"]
DirectInternetAccessType = Literal["Disabled", "Enabled"]
DomainStatusType = Literal[
    "Delete_Failed", "Deleting", "Failed", "InService", "Pending", "Update_Failed", "Updating"
]
EdgePackagingJobStatusType = Literal[
    "COMPLETED", "FAILED", "INPROGRESS", "STARTING", "STOPPED", "STOPPING"
]
EdgePresetDeploymentStatusType = Literal["COMPLETED", "FAILED"]
EdgePresetDeploymentTypeType = Literal["GreengrassV2Component"]
EndpointConfigSortKeyType = Literal["CreationTime", "Name"]
EndpointDeletedWaiterName = Literal["endpoint_deleted"]
EndpointInServiceWaiterName = Literal["endpoint_in_service"]
EndpointSortKeyType = Literal["CreationTime", "Name", "Status"]
EndpointStatusType = Literal[
    "Creating",
    "Deleting",
    "Failed",
    "InService",
    "OutOfService",
    "RollingBack",
    "SystemUpdating",
    "Updating",
]
ExecutionStatusType = Literal[
    "Completed", "CompletedWithViolations", "Failed", "InProgress", "Pending", "Stopped", "Stopping"
]
FeatureGroupSortByType = Literal["CreationTime", "FeatureGroupStatus", "Name", "OfflineStoreStatus"]
FeatureGroupSortOrderType = Literal["Ascending", "Descending"]
FeatureGroupStatusType = Literal["CreateFailed", "Created", "Creating", "DeleteFailed", "Deleting"]
FeatureTypeType = Literal["Fractional", "Integral", "String"]
FileSystemAccessModeType = Literal["ro", "rw"]
FileSystemTypeType = Literal["EFS", "FSxLustre"]
FlowDefinitionStatusType = Literal["Active", "Deleting", "Failed", "Initializing"]
FrameworkType = Literal[
    "DARKNET", "KERAS", "MXNET", "ONNX", "PYTORCH", "SKLEARN", "TENSORFLOW", "TFLITE", "XGBOOST"
]
HumanTaskUiStatusType = Literal["Active", "Deleting"]
HyperParameterScalingTypeType = Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"]
HyperParameterTuningJobObjectiveTypeType = Literal["Maximize", "Minimize"]
HyperParameterTuningJobSortByOptionsType = Literal["CreationTime", "Name", "Status"]
HyperParameterTuningJobStatusType = Literal[
    "Completed", "Failed", "InProgress", "Stopped", "Stopping"
]
HyperParameterTuningJobStrategyTypeType = Literal["Bayesian", "Random"]
HyperParameterTuningJobWarmStartTypeType = Literal["IdenticalDataAndAlgorithm", "TransferLearning"]
ImageCreatedWaiterName = Literal["image_created"]
ImageDeletedWaiterName = Literal["image_deleted"]
ImageSortByType = Literal["CREATION_TIME", "IMAGE_NAME", "LAST_MODIFIED_TIME"]
ImageSortOrderType = Literal["ASCENDING", "DESCENDING"]
ImageStatusType = Literal[
    "CREATED", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING", "UPDATE_FAILED", "UPDATING"
]
ImageUpdatedWaiterName = Literal["image_updated"]
ImageVersionCreatedWaiterName = Literal["image_version_created"]
ImageVersionDeletedWaiterName = Literal["image_version_deleted"]
ImageVersionSortByType = Literal["CREATION_TIME", "LAST_MODIFIED_TIME", "VERSION"]
ImageVersionSortOrderType = Literal["ASCENDING", "DESCENDING"]
ImageVersionStatusType = Literal[
    "CREATED", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING"
]
InferenceExecutionModeType = Literal["Direct", "Serial"]
InputModeType = Literal["File", "Pipe"]
InstanceTypeType = Literal[
    "ml.c4.2xlarge",
    "ml.c4.4xlarge",
    "ml.c4.8xlarge",
    "ml.c4.xlarge",
    "ml.c5.18xlarge",
    "ml.c5.2xlarge",
    "ml.c5.4xlarge",
    "ml.c5.9xlarge",
    "ml.c5.xlarge",
    "ml.c5d.18xlarge",
    "ml.c5d.2xlarge",
    "ml.c5d.4xlarge",
    "ml.c5d.9xlarge",
    "ml.c5d.xlarge",
    "ml.m4.10xlarge",
    "ml.m4.16xlarge",
    "ml.m4.2xlarge",
    "ml.m4.4xlarge",
    "ml.m4.xlarge",
    "ml.m5.12xlarge",
    "ml.m5.24xlarge",
    "ml.m5.2xlarge",
    "ml.m5.4xlarge",
    "ml.m5.xlarge",
    "ml.p2.16xlarge",
    "ml.p2.8xlarge",
    "ml.p2.xlarge",
    "ml.p3.16xlarge",
    "ml.p3.2xlarge",
    "ml.p3.8xlarge",
    "ml.t2.2xlarge",
    "ml.t2.large",
    "ml.t2.medium",
    "ml.t2.xlarge",
    "ml.t3.2xlarge",
    "ml.t3.large",
    "ml.t3.medium",
    "ml.t3.xlarge",
]
JoinSourceType = Literal["Input", "None"]
LabelingJobStatusType = Literal[
    "Completed", "Failed", "InProgress", "Initializing", "Stopped", "Stopping"
]
ListActionsPaginatorName = Literal["list_actions"]
ListAlgorithmsPaginatorName = Literal["list_algorithms"]
ListAppImageConfigsPaginatorName = Literal["list_app_image_configs"]
ListAppsPaginatorName = Literal["list_apps"]
ListArtifactsPaginatorName = Literal["list_artifacts"]
ListAssociationsPaginatorName = Literal["list_associations"]
ListAutoMLJobsPaginatorName = Literal["list_auto_ml_jobs"]
ListCandidatesForAutoMLJobPaginatorName = Literal["list_candidates_for_auto_ml_job"]
ListCodeRepositoriesPaginatorName = Literal["list_code_repositories"]
ListCompilationJobsPaginatorName = Literal["list_compilation_jobs"]
ListCompilationJobsSortByType = Literal["CreationTime", "Name", "Status"]
ListContextsPaginatorName = Literal["list_contexts"]
ListDataQualityJobDefinitionsPaginatorName = Literal["list_data_quality_job_definitions"]
ListDeviceFleetsPaginatorName = Literal["list_device_fleets"]
ListDeviceFleetsSortByType = Literal["CREATION_TIME", "LAST_MODIFIED_TIME", "NAME"]
ListDevicesPaginatorName = Literal["list_devices"]
ListDomainsPaginatorName = Literal["list_domains"]
ListEdgePackagingJobsPaginatorName = Literal["list_edge_packaging_jobs"]
ListEdgePackagingJobsSortByType = Literal[
    "CREATION_TIME", "LAST_MODIFIED_TIME", "MODEL_NAME", "NAME", "STATUS"
]
ListEndpointConfigsPaginatorName = Literal["list_endpoint_configs"]
ListEndpointsPaginatorName = Literal["list_endpoints"]
ListExperimentsPaginatorName = Literal["list_experiments"]
ListFeatureGroupsPaginatorName = Literal["list_feature_groups"]
ListFlowDefinitionsPaginatorName = Literal["list_flow_definitions"]
ListHumanTaskUisPaginatorName = Literal["list_human_task_uis"]
ListHyperParameterTuningJobsPaginatorName = Literal["list_hyper_parameter_tuning_jobs"]
ListImageVersionsPaginatorName = Literal["list_image_versions"]
ListImagesPaginatorName = Literal["list_images"]
ListLabelingJobsForWorkteamPaginatorName = Literal["list_labeling_jobs_for_workteam"]
ListLabelingJobsForWorkteamSortByOptionsType = Literal["CreationTime"]
ListLabelingJobsPaginatorName = Literal["list_labeling_jobs"]
ListModelBiasJobDefinitionsPaginatorName = Literal["list_model_bias_job_definitions"]
ListModelExplainabilityJobDefinitionsPaginatorName = Literal[
    "list_model_explainability_job_definitions"
]
ListModelPackageGroupsPaginatorName = Literal["list_model_package_groups"]
ListModelPackagesPaginatorName = Literal["list_model_packages"]
ListModelQualityJobDefinitionsPaginatorName = Literal["list_model_quality_job_definitions"]
ListModelsPaginatorName = Literal["list_models"]
ListMonitoringExecutionsPaginatorName = Literal["list_monitoring_executions"]
ListMonitoringSchedulesPaginatorName = Literal["list_monitoring_schedules"]
ListNotebookInstanceLifecycleConfigsPaginatorName = Literal[
    "list_notebook_instance_lifecycle_configs"
]
ListNotebookInstancesPaginatorName = Literal["list_notebook_instances"]
ListPipelineExecutionStepsPaginatorName = Literal["list_pipeline_execution_steps"]
ListPipelineExecutionsPaginatorName = Literal["list_pipeline_executions"]
ListPipelineParametersForExecutionPaginatorName = Literal["list_pipeline_parameters_for_execution"]
ListPipelinesPaginatorName = Literal["list_pipelines"]
ListProcessingJobsPaginatorName = Literal["list_processing_jobs"]
ListSubscribedWorkteamsPaginatorName = Literal["list_subscribed_workteams"]
ListTagsPaginatorName = Literal["list_tags"]
ListTrainingJobsForHyperParameterTuningJobPaginatorName = Literal[
    "list_training_jobs_for_hyper_parameter_tuning_job"
]
ListTrainingJobsPaginatorName = Literal["list_training_jobs"]
ListTransformJobsPaginatorName = Literal["list_transform_jobs"]
ListTrialComponentsPaginatorName = Literal["list_trial_components"]
ListTrialsPaginatorName = Literal["list_trials"]
ListUserProfilesPaginatorName = Literal["list_user_profiles"]
ListWorkforcesPaginatorName = Literal["list_workforces"]
ListWorkforcesSortByOptionsType = Literal["CreateDate", "Name"]
ListWorkteamsPaginatorName = Literal["list_workteams"]
ListWorkteamsSortByOptionsType = Literal["CreateDate", "Name"]
ModelApprovalStatusType = Literal["Approved", "PendingManualApproval", "Rejected"]
ModelCacheSettingType = Literal["Disabled", "Enabled"]
ModelPackageGroupSortByType = Literal["CreationTime", "Name"]
ModelPackageGroupStatusType = Literal[
    "Completed", "DeleteFailed", "Deleting", "Failed", "InProgress", "Pending"
]
ModelPackageSortByType = Literal["CreationTime", "Name"]
ModelPackageStatusType = Literal["Completed", "Deleting", "Failed", "InProgress", "Pending"]
ModelPackageTypeType = Literal["Both", "Unversioned", "Versioned"]
ModelSortKeyType = Literal["CreationTime", "Name"]
MonitoringExecutionSortKeyType = Literal["CreationTime", "ScheduledTime", "Status"]
MonitoringJobDefinitionSortKeyType = Literal["CreationTime", "Name"]
MonitoringProblemTypeType = Literal[
    "BinaryClassification", "MulticlassClassification", "Regression"
]
MonitoringScheduleSortKeyType = Literal["CreationTime", "Name", "Status"]
MonitoringTypeType = Literal["DataQuality", "ModelBias", "ModelExplainability", "ModelQuality"]
NotebookInstanceAcceleratorTypeType = Literal[
    "ml.eia1.large",
    "ml.eia1.medium",
    "ml.eia1.xlarge",
    "ml.eia2.large",
    "ml.eia2.medium",
    "ml.eia2.xlarge",
]
NotebookInstanceDeletedWaiterName = Literal["notebook_instance_deleted"]
NotebookInstanceInServiceWaiterName = Literal["notebook_instance_in_service"]
NotebookInstanceLifecycleConfigSortKeyType = Literal["CreationTime", "LastModifiedTime", "Name"]
NotebookInstanceLifecycleConfigSortOrderType = Literal["Ascending", "Descending"]
NotebookInstanceSortKeyType = Literal["CreationTime", "Name", "Status"]
NotebookInstanceSortOrderType = Literal["Ascending", "Descending"]
NotebookInstanceStatusType = Literal[
    "Deleting", "Failed", "InService", "Pending", "Stopped", "Stopping", "Updating"
]
NotebookInstanceStoppedWaiterName = Literal["notebook_instance_stopped"]
NotebookOutputOptionType = Literal["Allowed", "Disabled"]
ObjectiveStatusType = Literal["Failed", "Pending", "Succeeded"]
OfflineStoreStatusValueType = Literal["Active", "Blocked", "Disabled"]
OperatorType = Literal[
    "Contains",
    "Equals",
    "Exists",
    "GreaterThan",
    "GreaterThanOrEqualTo",
    "In",
    "LessThan",
    "LessThanOrEqualTo",
    "NotEquals",
    "NotExists",
]
OrderKeyType = Literal["Ascending", "Descending"]
ParameterTypeType = Literal["Categorical", "Continuous", "FreeText", "Integer"]
PipelineExecutionStatusType = Literal["Executing", "Failed", "Stopped", "Stopping", "Succeeded"]
PipelineStatusType = Literal["Active"]
ProblemTypeType = Literal["BinaryClassification", "MulticlassClassification", "Regression"]
ProcessingInstanceTypeType = Literal[
    "ml.c4.2xlarge",
    "ml.c4.4xlarge",
    "ml.c4.8xlarge",
    "ml.c4.xlarge",
    "ml.c5.18xlarge",
    "ml.c5.2xlarge",
    "ml.c5.4xlarge",
    "ml.c5.9xlarge",
    "ml.c5.xlarge",
    "ml.g4dn.12xlarge",
    "ml.g4dn.16xlarge",
    "ml.g4dn.2xlarge",
    "ml.g4dn.4xlarge",
    "ml.g4dn.8xlarge",
    "ml.g4dn.xlarge",
    "ml.m4.10xlarge",
    "ml.m4.16xlarge",
    "ml.m4.2xlarge",
    "ml.m4.4xlarge",
    "ml.m4.xlarge",
    "ml.m5.12xlarge",
    "ml.m5.24xlarge",
    "ml.m5.2xlarge",
    "ml.m5.4xlarge",
    "ml.m5.large",
    "ml.m5.xlarge",
    "ml.p2.16xlarge",
    "ml.p2.8xlarge",
    "ml.p2.xlarge",
    "ml.p3.16xlarge",
    "ml.p3.2xlarge",
    "ml.p3.8xlarge",
    "ml.r5.12xlarge",
    "ml.r5.16xlarge",
    "ml.r5.24xlarge",
    "ml.r5.2xlarge",
    "ml.r5.4xlarge",
    "ml.r5.8xlarge",
    "ml.r5.large",
    "ml.r5.xlarge",
    "ml.t3.2xlarge",
    "ml.t3.large",
    "ml.t3.medium",
    "ml.t3.xlarge",
]
ProcessingJobCompletedOrStoppedWaiterName = Literal["processing_job_completed_or_stopped"]
ProcessingJobStatusType = Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
ProcessingS3CompressionTypeType = Literal["Gzip", "None"]
ProcessingS3DataDistributionTypeType = Literal["FullyReplicated", "ShardedByS3Key"]
ProcessingS3DataTypeType = Literal["ManifestFile", "S3Prefix"]
ProcessingS3InputModeType = Literal["File", "Pipe"]
ProcessingS3UploadModeType = Literal["Continuous", "EndOfJob"]
ProductionVariantAcceleratorTypeType = Literal[
    "ml.eia1.large",
    "ml.eia1.medium",
    "ml.eia1.xlarge",
    "ml.eia2.large",
    "ml.eia2.medium",
    "ml.eia2.xlarge",
]
ProductionVariantInstanceTypeType = Literal[
    "ml.c4.2xlarge",
    "ml.c4.4xlarge",
    "ml.c4.8xlarge",
    "ml.c4.large",
    "ml.c4.xlarge",
    "ml.c5.18xlarge",
    "ml.c5.2xlarge",
    "ml.c5.4xlarge",
    "ml.c5.9xlarge",
    "ml.c5.large",
    "ml.c5.xlarge",
    "ml.c5d.18xlarge",
    "ml.c5d.2xlarge",
    "ml.c5d.4xlarge",
    "ml.c5d.9xlarge",
    "ml.c5d.large",
    "ml.c5d.xlarge",
    "ml.g4dn.12xlarge",
    "ml.g4dn.16xlarge",
    "ml.g4dn.2xlarge",
    "ml.g4dn.4xlarge",
    "ml.g4dn.8xlarge",
    "ml.g4dn.xlarge",
    "ml.inf1.24xlarge",
    "ml.inf1.2xlarge",
    "ml.inf1.6xlarge",
    "ml.inf1.xlarge",
    "ml.m4.10xlarge",
    "ml.m4.16xlarge",
    "ml.m4.2xlarge",
    "ml.m4.4xlarge",
    "ml.m4.xlarge",
    "ml.m5.12xlarge",
    "ml.m5.24xlarge",
    "ml.m5.2xlarge",
    "ml.m5.4xlarge",
    "ml.m5.large",
    "ml.m5.xlarge",
    "ml.m5d.12xlarge",
    "ml.m5d.24xlarge",
    "ml.m5d.2xlarge",
    "ml.m5d.4xlarge",
    "ml.m5d.large",
    "ml.m5d.xlarge",
    "ml.p2.16xlarge",
    "ml.p2.8xlarge",
    "ml.p2.xlarge",
    "ml.p3.16xlarge",
    "ml.p3.2xlarge",
    "ml.p3.8xlarge",
    "ml.r5.12xlarge",
    "ml.r5.24xlarge",
    "ml.r5.2xlarge",
    "ml.r5.4xlarge",
    "ml.r5.large",
    "ml.r5.xlarge",
    "ml.r5d.12xlarge",
    "ml.r5d.24xlarge",
    "ml.r5d.2xlarge",
    "ml.r5d.4xlarge",
    "ml.r5d.large",
    "ml.r5d.xlarge",
    "ml.t2.2xlarge",
    "ml.t2.large",
    "ml.t2.medium",
    "ml.t2.xlarge",
]
ProfilingStatusType = Literal["Disabled", "Enabled"]
ProjectSortByType = Literal["CreationTime", "Name"]
ProjectSortOrderType = Literal["Ascending", "Descending"]
ProjectStatusType = Literal[
    "CreateCompleted",
    "CreateFailed",
    "CreateInProgress",
    "DeleteCompleted",
    "DeleteFailed",
    "DeleteInProgress",
    "Pending",
]
RecordWrapperType = Literal["None", "RecordIO"]
RedshiftResultCompressionTypeType = Literal["BZIP2", "GZIP", "None", "SNAPPY", "ZSTD"]
RedshiftResultFormatType = Literal["CSV", "PARQUET"]
RepositoryAccessModeType = Literal["Platform", "Vpc"]
ResourceTypeType = Literal[
    "Endpoint",
    "Experiment",
    "ExperimentTrial",
    "ExperimentTrialComponent",
    "FeatureGroup",
    "ModelPackage",
    "ModelPackageGroup",
    "Pipeline",
    "PipelineExecution",
    "TrainingJob",
]
RetentionTypeType = Literal["Delete", "Retain"]
RootAccessType = Literal["Disabled", "Enabled"]
RuleEvaluationStatusType = Literal[
    "Error", "InProgress", "IssuesFound", "NoIssuesFound", "Stopped", "Stopping"
]
S3DataDistributionType = Literal["FullyReplicated", "ShardedByS3Key"]
S3DataTypeType = Literal["AugmentedManifestFile", "ManifestFile", "S3Prefix"]
SagemakerServicecatalogStatusType = Literal["Disabled", "Enabled"]
ScheduleStatusType = Literal["Failed", "Pending", "Scheduled", "Stopped"]
SearchPaginatorName = Literal["search"]
SearchSortOrderType = Literal["Ascending", "Descending"]
SecondaryStatusType = Literal[
    "Completed",
    "Downloading",
    "DownloadingTrainingImage",
    "Failed",
    "Interrupted",
    "LaunchingMLInstances",
    "MaxRuntimeExceeded",
    "MaxWaitTimeExceeded",
    "PreparingTrainingStack",
    "Restarting",
    "Starting",
    "Stopped",
    "Stopping",
    "Training",
    "Updating",
    "Uploading",
]
SortActionsByType = Literal["CreationTime", "Name"]
SortArtifactsByType = Literal["CreationTime"]
SortAssociationsByType = Literal[
    "CreationTime", "DestinationArn", "DestinationType", "SourceArn", "SourceType"
]
SortByType = Literal["CreationTime", "Name", "Status"]
SortContextsByType = Literal["CreationTime", "Name"]
SortExperimentsByType = Literal["CreationTime", "Name"]
SortOrderType = Literal["Ascending", "Descending"]
SortPipelineExecutionsByType = Literal["CreationTime", "PipelineExecutionArn"]
SortPipelinesByType = Literal["CreationTime", "Name"]
SortTrialComponentsByType = Literal["CreationTime", "Name"]
SortTrialsByType = Literal["CreationTime", "Name"]
SplitTypeType = Literal["Line", "None", "RecordIO", "TFRecord"]
StepStatusType = Literal["Executing", "Failed", "Starting", "Stopped", "Stopping", "Succeeded"]
TargetDeviceType = Literal[
    "aisage",
    "amba_cv22",
    "amba_cv25",
    "coreml",
    "deeplens",
    "imx8qm",
    "jacinto_tda4vm",
    "jetson_nano",
    "jetson_tx1",
    "jetson_tx2",
    "jetson_xavier",
    "lambda",
    "ml_c4",
    "ml_c5",
    "ml_eia2",
    "ml_g4dn",
    "ml_inf1",
    "ml_m4",
    "ml_m5",
    "ml_p2",
    "ml_p3",
    "qcs603",
    "qcs605",
    "rasp3b",
    "rk3288",
    "rk3399",
    "sbe_c",
    "sitara_am57x",
    "x86_win32",
    "x86_win64",
]
TargetPlatformAcceleratorType = Literal["INTEL_GRAPHICS", "MALI", "NVIDIA"]
TargetPlatformArchType = Literal["ARM64", "ARM_EABI", "ARM_EABIHF", "X86", "X86_64"]
TargetPlatformOsType = Literal["ANDROID", "LINUX"]
TrafficRoutingConfigTypeType = Literal["ALL_AT_ONCE", "CANARY"]
TrainingInputModeType = Literal["File", "Pipe"]
TrainingInstanceTypeType = Literal[
    "ml.c4.2xlarge",
    "ml.c4.4xlarge",
    "ml.c4.8xlarge",
    "ml.c4.xlarge",
    "ml.c5.18xlarge",
    "ml.c5.2xlarge",
    "ml.c5.4xlarge",
    "ml.c5.9xlarge",
    "ml.c5.xlarge",
    "ml.c5n.18xlarge",
    "ml.c5n.2xlarge",
    "ml.c5n.4xlarge",
    "ml.c5n.9xlarge",
    "ml.c5n.xlarge",
    "ml.g4dn.12xlarge",
    "ml.g4dn.16xlarge",
    "ml.g4dn.2xlarge",
    "ml.g4dn.4xlarge",
    "ml.g4dn.8xlarge",
    "ml.g4dn.xlarge",
    "ml.m4.10xlarge",
    "ml.m4.16xlarge",
    "ml.m4.2xlarge",
    "ml.m4.4xlarge",
    "ml.m4.xlarge",
    "ml.m5.12xlarge",
    "ml.m5.24xlarge",
    "ml.m5.2xlarge",
    "ml.m5.4xlarge",
    "ml.m5.large",
    "ml.m5.xlarge",
    "ml.p2.16xlarge",
    "ml.p2.8xlarge",
    "ml.p2.xlarge",
    "ml.p3.16xlarge",
    "ml.p3.2xlarge",
    "ml.p3.8xlarge",
    "ml.p3dn.24xlarge",
    "ml.p4d.24xlarge",
]
TrainingJobCompletedOrStoppedWaiterName = Literal["training_job_completed_or_stopped"]
TrainingJobEarlyStoppingTypeType = Literal["Auto", "Off"]
TrainingJobSortByOptionsType = Literal[
    "CreationTime", "FinalObjectiveMetricValue", "Name", "Status"
]
TrainingJobStatusType = Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
TransformInstanceTypeType = Literal[
    "ml.c4.2xlarge",
    "ml.c4.4xlarge",
    "ml.c4.8xlarge",
    "ml.c4.xlarge",
    "ml.c5.18xlarge",
    "ml.c5.2xlarge",
    "ml.c5.4xlarge",
    "ml.c5.9xlarge",
    "ml.c5.xlarge",
    "ml.g4dn.12xlarge",
    "ml.g4dn.16xlarge",
    "ml.g4dn.2xlarge",
    "ml.g4dn.4xlarge",
    "ml.g4dn.8xlarge",
    "ml.g4dn.xlarge",
    "ml.m4.10xlarge",
    "ml.m4.16xlarge",
    "ml.m4.2xlarge",
    "ml.m4.4xlarge",
    "ml.m4.xlarge",
    "ml.m5.12xlarge",
    "ml.m5.24xlarge",
    "ml.m5.2xlarge",
    "ml.m5.4xlarge",
    "ml.m5.large",
    "ml.m5.xlarge",
    "ml.p2.16xlarge",
    "ml.p2.8xlarge",
    "ml.p2.xlarge",
    "ml.p3.16xlarge",
    "ml.p3.2xlarge",
    "ml.p3.8xlarge",
]
TransformJobCompletedOrStoppedWaiterName = Literal["transform_job_completed_or_stopped"]
TransformJobStatusType = Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
TrialComponentPrimaryStatusType = Literal[
    "Completed", "Failed", "InProgress", "Stopped", "Stopping"
]
UserProfileSortKeyType = Literal["CreationTime", "LastModifiedTime"]
UserProfileStatusType = Literal[
    "Delete_Failed", "Deleting", "Failed", "InService", "Pending", "Update_Failed", "Updating"
]
VariantPropertyTypeType = Literal["DataCaptureConfig", "DesiredInstanceCount", "DesiredWeight"]
