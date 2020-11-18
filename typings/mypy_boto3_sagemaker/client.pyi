# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for sagemaker service client

Usage::

    ```python
    import boto3
    from mypy_boto3_sagemaker import SageMakerClient

    client: SageMakerClient = boto3.client("sagemaker")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

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
    ListImagesPaginator,
    ListImageVersionsPaginator,
    ListLabelingJobsForWorkteamPaginator,
    ListLabelingJobsPaginator,
    ListModelPackagesPaginator,
    ListModelsPaginator,
    ListMonitoringExecutionsPaginator,
    ListMonitoringSchedulesPaginator,
    ListNotebookInstanceLifecycleConfigsPaginator,
    ListNotebookInstancesPaginator,
    ListProcessingJobsPaginator,
    ListSubscribedWorkteamsPaginator,
    ListTagsPaginator,
    ListTrainingJobsForHyperParameterTuningJobPaginator,
    ListTrainingJobsPaginator,
    ListTransformJobsPaginator,
    ListTrialComponentsPaginator,
    ListTrialsPaginator,
    ListUserProfilesPaginator,
    ListWorkforcesPaginator,
    ListWorkteamsPaginator,
    SearchPaginator,
)
from mypy_boto3_sagemaker.type_defs import (
    AddTagsOutputTypeDef,
    AlgorithmSpecificationTypeDef,
    AlgorithmValidationSpecificationTypeDef,
    AppSpecificationTypeDef,
    AssociateTrialComponentResponseTypeDef,
    AutoMLChannelTypeDef,
    AutoMLJobConfigTypeDef,
    AutoMLJobObjectiveTypeDef,
    AutoMLOutputDataConfigTypeDef,
    ChannelTypeDef,
    CheckpointConfigTypeDef,
    CognitoConfigTypeDef,
    ContainerDefinitionTypeDef,
    CreateAlgorithmOutputTypeDef,
    CreateAppImageConfigResponseTypeDef,
    CreateAppResponseTypeDef,
    CreateAutoMLJobResponseTypeDef,
    CreateCodeRepositoryOutputTypeDef,
    CreateCompilationJobResponseTypeDef,
    CreateDomainResponseTypeDef,
    CreateEndpointConfigOutputTypeDef,
    CreateEndpointOutputTypeDef,
    CreateExperimentResponseTypeDef,
    CreateFlowDefinitionResponseTypeDef,
    CreateHumanTaskUiResponseTypeDef,
    CreateHyperParameterTuningJobResponseTypeDef,
    CreateImageResponseTypeDef,
    CreateImageVersionResponseTypeDef,
    CreateLabelingJobResponseTypeDef,
    CreateModelOutputTypeDef,
    CreateModelPackageOutputTypeDef,
    CreateMonitoringScheduleResponseTypeDef,
    CreateNotebookInstanceLifecycleConfigOutputTypeDef,
    CreateNotebookInstanceOutputTypeDef,
    CreatePresignedDomainUrlResponseTypeDef,
    CreatePresignedNotebookInstanceUrlOutputTypeDef,
    CreateProcessingJobResponseTypeDef,
    CreateTrainingJobResponseTypeDef,
    CreateTransformJobResponseTypeDef,
    CreateTrialComponentResponseTypeDef,
    CreateTrialResponseTypeDef,
    CreateUserProfileResponseTypeDef,
    CreateWorkforceResponseTypeDef,
    CreateWorkteamResponseTypeDef,
    DataCaptureConfigTypeDef,
    DataProcessingTypeDef,
    DebugHookConfigTypeDef,
    DebugRuleConfigurationTypeDef,
    DeleteExperimentResponseTypeDef,
    DeleteTrialComponentResponseTypeDef,
    DeleteTrialResponseTypeDef,
    DeleteWorkteamResponseTypeDef,
    DescribeAlgorithmOutputTypeDef,
    DescribeAppImageConfigResponseTypeDef,
    DescribeAppResponseTypeDef,
    DescribeAutoMLJobResponseTypeDef,
    DescribeCodeRepositoryOutputTypeDef,
    DescribeCompilationJobResponseTypeDef,
    DescribeDomainResponseTypeDef,
    DescribeEndpointConfigOutputTypeDef,
    DescribeEndpointOutputTypeDef,
    DescribeExperimentResponseTypeDef,
    DescribeFlowDefinitionResponseTypeDef,
    DescribeHumanTaskUiResponseTypeDef,
    DescribeHyperParameterTuningJobResponseTypeDef,
    DescribeImageResponseTypeDef,
    DescribeImageVersionResponseTypeDef,
    DescribeLabelingJobResponseTypeDef,
    DescribeModelOutputTypeDef,
    DescribeModelPackageOutputTypeDef,
    DescribeMonitoringScheduleResponseTypeDef,
    DescribeNotebookInstanceLifecycleConfigOutputTypeDef,
    DescribeNotebookInstanceOutputTypeDef,
    DescribeProcessingJobResponseTypeDef,
    DescribeSubscribedWorkteamResponseTypeDef,
    DescribeTrainingJobResponseTypeDef,
    DescribeTransformJobResponseTypeDef,
    DescribeTrialComponentResponseTypeDef,
    DescribeTrialResponseTypeDef,
    DescribeUserProfileResponseTypeDef,
    DescribeWorkforceResponseTypeDef,
    DescribeWorkteamResponseTypeDef,
    DesiredWeightAndCapacityTypeDef,
    DisassociateTrialComponentResponseTypeDef,
    ExperimentConfigTypeDef,
    FlowDefinitionOutputConfigTypeDef,
    GetSearchSuggestionsResponseTypeDef,
    GitConfigForUpdateTypeDef,
    GitConfigTypeDef,
    HumanLoopActivationConfigTypeDef,
    HumanLoopConfigTypeDef,
    HumanLoopRequestSourceTypeDef,
    HumanTaskConfigTypeDef,
    HyperParameterTrainingJobDefinitionTypeDef,
    HyperParameterTuningJobConfigTypeDef,
    HyperParameterTuningJobWarmStartConfigTypeDef,
    InferenceSpecificationTypeDef,
    InputConfigTypeDef,
    KernelGatewayImageConfigTypeDef,
    LabelingJobAlgorithmsConfigTypeDef,
    LabelingJobInputConfigTypeDef,
    LabelingJobOutputConfigTypeDef,
    LabelingJobStoppingConditionsTypeDef,
    ListAlgorithmsOutputTypeDef,
    ListAppImageConfigsResponseTypeDef,
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
    MemberDefinitionTypeDef,
    ModelClientConfigTypeDef,
    ModelPackageValidationSpecificationTypeDef,
    MonitoringScheduleConfigTypeDef,
    NetworkConfigTypeDef,
    NotebookInstanceLifecycleHookTypeDef,
    NotificationConfigurationTypeDef,
    OidcConfigTypeDef,
    OutputConfigTypeDef,
    OutputDataConfigTypeDef,
    ProcessingInputTypeDef,
    ProcessingOutputConfigTypeDef,
    ProcessingResourcesTypeDef,
    ProcessingStoppingConditionTypeDef,
    ProductionVariantTypeDef,
    RenderableTaskTypeDef,
    RenderUiTemplateResponseTypeDef,
    ResourceConfigTypeDef,
    ResourceSpecTypeDef,
    RetentionPolicyTypeDef,
    SearchResponseTypeDef,
    SourceAlgorithmSpecificationTypeDef,
    SourceIpConfigTypeDef,
    StoppingConditionTypeDef,
    SuggestionQueryTypeDef,
    TagTypeDef,
    TensorBoardOutputConfigTypeDef,
    TrainingSpecificationTypeDef,
    TransformInputTypeDef,
    TransformOutputTypeDef,
    TransformResourcesTypeDef,
    TrialComponentArtifactTypeDef,
    TrialComponentParameterValueTypeDef,
    TrialComponentStatusTypeDef,
    UiTemplateTypeDef,
    UpdateAppImageConfigResponseTypeDef,
    UpdateCodeRepositoryOutputTypeDef,
    UpdateDomainResponseTypeDef,
    UpdateEndpointOutputTypeDef,
    UpdateEndpointWeightsAndCapacitiesOutputTypeDef,
    UpdateExperimentResponseTypeDef,
    UpdateImageResponseTypeDef,
    UpdateMonitoringScheduleResponseTypeDef,
    UpdateTrialComponentResponseTypeDef,
    UpdateTrialResponseTypeDef,
    UpdateUserProfileResponseTypeDef,
    UpdateWorkforceResponseTypeDef,
    UpdateWorkteamResponseTypeDef,
    UserSettingsTypeDef,
    VariantPropertyTypeDef,
    VpcConfigTypeDef,
)
from mypy_boto3_sagemaker.waiter import (
    EndpointDeletedWaiter,
    EndpointInServiceWaiter,
    NotebookInstanceDeletedWaiter,
    NotebookInstanceInServiceWaiter,
    NotebookInstanceStoppedWaiter,
    ProcessingJobCompletedOrStoppedWaiter,
    TrainingJobCompletedOrStoppedWaiter,
    TransformJobCompletedOrStoppedWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SageMakerClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ResourceInUse: Type[BotocoreClientError]
    ResourceLimitExceeded: Type[BotocoreClientError]
    ResourceNotFound: Type[BotocoreClientError]


class SageMakerClient:
    """
    [SageMaker.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_tags(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> AddTagsOutputTypeDef:
        """
        [Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.add_tags)
        """

    def associate_trial_component(
        self, TrialComponentName: str, TrialName: str
    ) -> AssociateTrialComponentResponseTypeDef:
        """
        [Client.associate_trial_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.associate_trial_component)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.can_paginate)
        """

    def create_algorithm(
        self,
        AlgorithmName: str,
        TrainingSpecification: "TrainingSpecificationTypeDef",
        AlgorithmDescription: str = None,
        InferenceSpecification: "InferenceSpecificationTypeDef" = None,
        ValidationSpecification: "AlgorithmValidationSpecificationTypeDef" = None,
        CertifyForMarketplace: bool = None,
    ) -> CreateAlgorithmOutputTypeDef:
        """
        [Client.create_algorithm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_algorithm)
        """

    def create_app(
        self,
        DomainId: str,
        UserProfileName: str,
        AppType: Literal["JupyterServer", "KernelGateway", "TensorBoard"],
        AppName: str,
        Tags: List["TagTypeDef"] = None,
        ResourceSpec: "ResourceSpecTypeDef" = None,
    ) -> CreateAppResponseTypeDef:
        """
        [Client.create_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_app)
        """

    def create_app_image_config(
        self,
        AppImageConfigName: str,
        Tags: List["TagTypeDef"] = None,
        KernelGatewayImageConfig: "KernelGatewayImageConfigTypeDef" = None,
    ) -> CreateAppImageConfigResponseTypeDef:
        """
        [Client.create_app_image_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_app_image_config)
        """

    def create_auto_ml_job(
        self,
        AutoMLJobName: str,
        InputDataConfig: List["AutoMLChannelTypeDef"],
        OutputDataConfig: "AutoMLOutputDataConfigTypeDef",
        RoleArn: str,
        ProblemType: Literal[
            "BinaryClassification", "MulticlassClassification", "Regression"
        ] = None,
        AutoMLJobObjective: "AutoMLJobObjectiveTypeDef" = None,
        AutoMLJobConfig: "AutoMLJobConfigTypeDef" = None,
        GenerateCandidateDefinitionsOnly: bool = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateAutoMLJobResponseTypeDef:
        """
        [Client.create_auto_ml_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_auto_ml_job)
        """

    def create_code_repository(
        self, CodeRepositoryName: str, GitConfig: "GitConfigTypeDef"
    ) -> CreateCodeRepositoryOutputTypeDef:
        """
        [Client.create_code_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_code_repository)
        """

    def create_compilation_job(
        self,
        CompilationJobName: str,
        RoleArn: str,
        InputConfig: "InputConfigTypeDef",
        OutputConfig: "OutputConfigTypeDef",
        StoppingCondition: "StoppingConditionTypeDef",
        Tags: List["TagTypeDef"] = None,
    ) -> CreateCompilationJobResponseTypeDef:
        """
        [Client.create_compilation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_compilation_job)
        """

    def create_domain(
        self,
        DomainName: str,
        AuthMode: Literal["SSO", "IAM"],
        DefaultUserSettings: "UserSettingsTypeDef",
        SubnetIds: List[str],
        VpcId: str,
        Tags: List["TagTypeDef"] = None,
        AppNetworkAccessType: Literal["PublicInternetOnly", "VpcOnly"] = None,
        HomeEfsFileSystemKmsKeyId: str = None,
        KmsKeyId: str = None,
    ) -> CreateDomainResponseTypeDef:
        """
        [Client.create_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_domain)
        """

    def create_endpoint(
        self, EndpointName: str, EndpointConfigName: str, Tags: List["TagTypeDef"] = None
    ) -> CreateEndpointOutputTypeDef:
        """
        [Client.create_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_endpoint)
        """

    def create_endpoint_config(
        self,
        EndpointConfigName: str,
        ProductionVariants: List["ProductionVariantTypeDef"],
        DataCaptureConfig: "DataCaptureConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        KmsKeyId: str = None,
    ) -> CreateEndpointConfigOutputTypeDef:
        """
        [Client.create_endpoint_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_endpoint_config)
        """

    def create_experiment(
        self,
        ExperimentName: str,
        DisplayName: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateExperimentResponseTypeDef:
        """
        [Client.create_experiment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_experiment)
        """

    def create_flow_definition(
        self,
        FlowDefinitionName: str,
        HumanLoopConfig: "HumanLoopConfigTypeDef",
        OutputConfig: "FlowDefinitionOutputConfigTypeDef",
        RoleArn: str,
        HumanLoopRequestSource: "HumanLoopRequestSourceTypeDef" = None,
        HumanLoopActivationConfig: "HumanLoopActivationConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateFlowDefinitionResponseTypeDef:
        """
        [Client.create_flow_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_flow_definition)
        """

    def create_human_task_ui(
        self, HumanTaskUiName: str, UiTemplate: UiTemplateTypeDef, Tags: List["TagTypeDef"] = None
    ) -> CreateHumanTaskUiResponseTypeDef:
        """
        [Client.create_human_task_ui documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_human_task_ui)
        """

    def create_hyper_parameter_tuning_job(
        self,
        HyperParameterTuningJobName: str,
        HyperParameterTuningJobConfig: "HyperParameterTuningJobConfigTypeDef",
        TrainingJobDefinition: "HyperParameterTrainingJobDefinitionTypeDef" = None,
        TrainingJobDefinitions: List["HyperParameterTrainingJobDefinitionTypeDef"] = None,
        WarmStartConfig: "HyperParameterTuningJobWarmStartConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateHyperParameterTuningJobResponseTypeDef:
        """
        [Client.create_hyper_parameter_tuning_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_hyper_parameter_tuning_job)
        """

    def create_image(
        self,
        ImageName: str,
        RoleArn: str,
        Description: str = None,
        DisplayName: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateImageResponseTypeDef:
        """
        [Client.create_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_image)
        """

    def create_image_version(
        self, BaseImage: str, ClientToken: str, ImageName: str
    ) -> CreateImageVersionResponseTypeDef:
        """
        [Client.create_image_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_image_version)
        """

    def create_labeling_job(
        self,
        LabelingJobName: str,
        LabelAttributeName: str,
        InputConfig: "LabelingJobInputConfigTypeDef",
        OutputConfig: "LabelingJobOutputConfigTypeDef",
        RoleArn: str,
        HumanTaskConfig: "HumanTaskConfigTypeDef",
        LabelCategoryConfigS3Uri: str = None,
        StoppingConditions: "LabelingJobStoppingConditionsTypeDef" = None,
        LabelingJobAlgorithmsConfig: "LabelingJobAlgorithmsConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateLabelingJobResponseTypeDef:
        """
        [Client.create_labeling_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_labeling_job)
        """

    def create_model(
        self,
        ModelName: str,
        ExecutionRoleArn: str,
        PrimaryContainer: "ContainerDefinitionTypeDef" = None,
        Containers: List["ContainerDefinitionTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        EnableNetworkIsolation: bool = None,
    ) -> CreateModelOutputTypeDef:
        """
        [Client.create_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_model)
        """

    def create_model_package(
        self,
        ModelPackageName: str = None,
        ModelPackageDescription: str = None,
        InferenceSpecification: "InferenceSpecificationTypeDef" = None,
        ValidationSpecification: "ModelPackageValidationSpecificationTypeDef" = None,
        SourceAlgorithmSpecification: "SourceAlgorithmSpecificationTypeDef" = None,
        CertifyForMarketplace: bool = None,
    ) -> CreateModelPackageOutputTypeDef:
        """
        [Client.create_model_package documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_model_package)
        """

    def create_monitoring_schedule(
        self,
        MonitoringScheduleName: str,
        MonitoringScheduleConfig: "MonitoringScheduleConfigTypeDef",
        Tags: List["TagTypeDef"] = None,
    ) -> CreateMonitoringScheduleResponseTypeDef:
        """
        [Client.create_monitoring_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_monitoring_schedule)
        """

    def create_notebook_instance(
        self,
        NotebookInstanceName: str,
        InstanceType: Literal[
            "ml.t2.medium",
            "ml.t2.large",
            "ml.t2.xlarge",
            "ml.t2.2xlarge",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.c5d.xlarge",
            "ml.c5d.2xlarge",
            "ml.c5d.4xlarge",
            "ml.c5d.9xlarge",
            "ml.c5d.18xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
        ],
        RoleArn: str,
        SubnetId: str = None,
        SecurityGroupIds: List[str] = None,
        KmsKeyId: str = None,
        Tags: List["TagTypeDef"] = None,
        LifecycleConfigName: str = None,
        DirectInternetAccess: Literal["Enabled", "Disabled"] = None,
        VolumeSizeInGB: int = None,
        AcceleratorTypes: List[
            Literal[
                "ml.eia1.medium",
                "ml.eia1.large",
                "ml.eia1.xlarge",
                "ml.eia2.medium",
                "ml.eia2.large",
                "ml.eia2.xlarge",
            ]
        ] = None,
        DefaultCodeRepository: str = None,
        AdditionalCodeRepositories: List[str] = None,
        RootAccess: Literal["Enabled", "Disabled"] = None,
    ) -> CreateNotebookInstanceOutputTypeDef:
        """
        [Client.create_notebook_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_notebook_instance)
        """

    def create_notebook_instance_lifecycle_config(
        self,
        NotebookInstanceLifecycleConfigName: str,
        OnCreate: List["NotebookInstanceLifecycleHookTypeDef"] = None,
        OnStart: List["NotebookInstanceLifecycleHookTypeDef"] = None,
    ) -> CreateNotebookInstanceLifecycleConfigOutputTypeDef:
        """
        [Client.create_notebook_instance_lifecycle_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_notebook_instance_lifecycle_config)
        """

    def create_presigned_domain_url(
        self, DomainId: str, UserProfileName: str, SessionExpirationDurationInSeconds: int = None
    ) -> CreatePresignedDomainUrlResponseTypeDef:
        """
        [Client.create_presigned_domain_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_presigned_domain_url)
        """

    def create_presigned_notebook_instance_url(
        self, NotebookInstanceName: str, SessionExpirationDurationInSeconds: int = None
    ) -> CreatePresignedNotebookInstanceUrlOutputTypeDef:
        """
        [Client.create_presigned_notebook_instance_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_presigned_notebook_instance_url)
        """

    def create_processing_job(
        self,
        ProcessingJobName: str,
        ProcessingResources: "ProcessingResourcesTypeDef",
        AppSpecification: "AppSpecificationTypeDef",
        RoleArn: str,
        ProcessingInputs: List["ProcessingInputTypeDef"] = None,
        ProcessingOutputConfig: "ProcessingOutputConfigTypeDef" = None,
        StoppingCondition: "ProcessingStoppingConditionTypeDef" = None,
        Environment: Dict[str, str] = None,
        NetworkConfig: "NetworkConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        ExperimentConfig: "ExperimentConfigTypeDef" = None,
    ) -> CreateProcessingJobResponseTypeDef:
        """
        [Client.create_processing_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_processing_job)
        """

    def create_training_job(
        self,
        TrainingJobName: str,
        AlgorithmSpecification: "AlgorithmSpecificationTypeDef",
        RoleArn: str,
        OutputDataConfig: "OutputDataConfigTypeDef",
        ResourceConfig: "ResourceConfigTypeDef",
        StoppingCondition: "StoppingConditionTypeDef",
        HyperParameters: Dict[str, str] = None,
        InputDataConfig: List["ChannelTypeDef"] = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        EnableNetworkIsolation: bool = None,
        EnableInterContainerTrafficEncryption: bool = None,
        EnableManagedSpotTraining: bool = None,
        CheckpointConfig: "CheckpointConfigTypeDef" = None,
        DebugHookConfig: "DebugHookConfigTypeDef" = None,
        DebugRuleConfigurations: List["DebugRuleConfigurationTypeDef"] = None,
        TensorBoardOutputConfig: "TensorBoardOutputConfigTypeDef" = None,
        ExperimentConfig: "ExperimentConfigTypeDef" = None,
    ) -> CreateTrainingJobResponseTypeDef:
        """
        [Client.create_training_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_training_job)
        """

    def create_transform_job(
        self,
        TransformJobName: str,
        ModelName: str,
        TransformInput: "TransformInputTypeDef",
        TransformOutput: "TransformOutputTypeDef",
        TransformResources: "TransformResourcesTypeDef",
        MaxConcurrentTransforms: int = None,
        ModelClientConfig: "ModelClientConfigTypeDef" = None,
        MaxPayloadInMB: int = None,
        BatchStrategy: Literal["MultiRecord", "SingleRecord"] = None,
        Environment: Dict[str, str] = None,
        DataProcessing: "DataProcessingTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        ExperimentConfig: "ExperimentConfigTypeDef" = None,
    ) -> CreateTransformJobResponseTypeDef:
        """
        [Client.create_transform_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_transform_job)
        """

    def create_trial(
        self,
        TrialName: str,
        ExperimentName: str,
        DisplayName: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateTrialResponseTypeDef:
        """
        [Client.create_trial documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_trial)
        """

    def create_trial_component(
        self,
        TrialComponentName: str,
        DisplayName: str = None,
        Status: "TrialComponentStatusTypeDef" = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Parameters: Dict[str, "TrialComponentParameterValueTypeDef"] = None,
        InputArtifacts: Dict[str, "TrialComponentArtifactTypeDef"] = None,
        OutputArtifacts: Dict[str, "TrialComponentArtifactTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateTrialComponentResponseTypeDef:
        """
        [Client.create_trial_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_trial_component)
        """

    def create_user_profile(
        self,
        DomainId: str,
        UserProfileName: str,
        SingleSignOnUserIdentifier: str = None,
        SingleSignOnUserValue: str = None,
        Tags: List["TagTypeDef"] = None,
        UserSettings: "UserSettingsTypeDef" = None,
    ) -> CreateUserProfileResponseTypeDef:
        """
        [Client.create_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_user_profile)
        """

    def create_workforce(
        self,
        WorkforceName: str,
        CognitoConfig: "CognitoConfigTypeDef" = None,
        OidcConfig: OidcConfigTypeDef = None,
        SourceIpConfig: "SourceIpConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateWorkforceResponseTypeDef:
        """
        [Client.create_workforce documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_workforce)
        """

    def create_workteam(
        self,
        WorkteamName: str,
        MemberDefinitions: List["MemberDefinitionTypeDef"],
        Description: str,
        WorkforceName: str = None,
        NotificationConfiguration: "NotificationConfigurationTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateWorkteamResponseTypeDef:
        """
        [Client.create_workteam documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.create_workteam)
        """

    def delete_algorithm(self, AlgorithmName: str) -> None:
        """
        [Client.delete_algorithm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.delete_algorithm)
        """

    def delete_app(
        self,
        DomainId: str,
        UserProfileName: str,
        AppType: Literal["JupyterServer", "KernelGateway", "TensorBoard"],
        AppName: str,
    ) -> None:
        """
        [Client.delete_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.delete_app)
        """

    def delete_app_image_config(self, AppImageConfigName: str) -> None:
        """
        [Client.delete_app_image_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.delete_app_image_config)
        """

    def delete_code_repository(self, CodeRepositoryName: str) -> None:
        """
        [Client.delete_code_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.delete_code_repository)
        """

    def delete_domain(self, DomainId: str, RetentionPolicy: RetentionPolicyTypeDef = None) -> None:
        """
        [Client.delete_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.delete_domain)
        """

    def delete_endpoint(self, EndpointName: str) -> None:
        """
        [Client.delete_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.delete_endpoint)
        """

    def delete_endpoint_config(self, EndpointConfigName: str) -> None:
        """
        [Client.delete_endpoint_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.delete_endpoint_config)
        """

    def delete_experiment(self, ExperimentName: str) -> DeleteExperimentResponseTypeDef:
        """
        [Client.delete_experiment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.delete_experiment)
        """

    def delete_flow_definition(self, FlowDefinitionName: str) -> Dict[str, Any]:
        """
        [Client.delete_flow_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.delete_flow_definition)
        """

    def delete_human_task_ui(self, HumanTaskUiName: str) -> Dict[str, Any]:
        """
        [Client.delete_human_task_ui documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.delete_human_task_ui)
        """

    def delete_image(self, ImageName: str) -> Dict[str, Any]:
        """
        [Client.delete_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.delete_image)
        """

    def delete_image_version(self, ImageName: str, Version: int) -> Dict[str, Any]:
        """
        [Client.delete_image_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.delete_image_version)
        """

    def delete_model(self, ModelName: str) -> None:
        """
        [Client.delete_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.delete_model)
        """

    def delete_model_package(self, ModelPackageName: str) -> None:
        """
        [Client.delete_model_package documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.delete_model_package)
        """

    def delete_monitoring_schedule(self, MonitoringScheduleName: str) -> None:
        """
        [Client.delete_monitoring_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.delete_monitoring_schedule)
        """

    def delete_notebook_instance(self, NotebookInstanceName: str) -> None:
        """
        [Client.delete_notebook_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.delete_notebook_instance)
        """

    def delete_notebook_instance_lifecycle_config(
        self, NotebookInstanceLifecycleConfigName: str
    ) -> None:
        """
        [Client.delete_notebook_instance_lifecycle_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.delete_notebook_instance_lifecycle_config)
        """

    def delete_tags(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.delete_tags)
        """

    def delete_trial(self, TrialName: str) -> DeleteTrialResponseTypeDef:
        """
        [Client.delete_trial documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.delete_trial)
        """

    def delete_trial_component(
        self, TrialComponentName: str
    ) -> DeleteTrialComponentResponseTypeDef:
        """
        [Client.delete_trial_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.delete_trial_component)
        """

    def delete_user_profile(self, DomainId: str, UserProfileName: str) -> None:
        """
        [Client.delete_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.delete_user_profile)
        """

    def delete_workforce(self, WorkforceName: str) -> Dict[str, Any]:
        """
        [Client.delete_workforce documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.delete_workforce)
        """

    def delete_workteam(self, WorkteamName: str) -> DeleteWorkteamResponseTypeDef:
        """
        [Client.delete_workteam documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.delete_workteam)
        """

    def describe_algorithm(self, AlgorithmName: str) -> DescribeAlgorithmOutputTypeDef:
        """
        [Client.describe_algorithm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_algorithm)
        """

    def describe_app(
        self,
        DomainId: str,
        UserProfileName: str,
        AppType: Literal["JupyterServer", "KernelGateway", "TensorBoard"],
        AppName: str,
    ) -> DescribeAppResponseTypeDef:
        """
        [Client.describe_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_app)
        """

    def describe_app_image_config(
        self, AppImageConfigName: str
    ) -> DescribeAppImageConfigResponseTypeDef:
        """
        [Client.describe_app_image_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_app_image_config)
        """

    def describe_auto_ml_job(self, AutoMLJobName: str) -> DescribeAutoMLJobResponseTypeDef:
        """
        [Client.describe_auto_ml_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_auto_ml_job)
        """

    def describe_code_repository(
        self, CodeRepositoryName: str
    ) -> DescribeCodeRepositoryOutputTypeDef:
        """
        [Client.describe_code_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_code_repository)
        """

    def describe_compilation_job(
        self, CompilationJobName: str
    ) -> DescribeCompilationJobResponseTypeDef:
        """
        [Client.describe_compilation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_compilation_job)
        """

    def describe_domain(self, DomainId: str) -> DescribeDomainResponseTypeDef:
        """
        [Client.describe_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_domain)
        """

    def describe_endpoint(self, EndpointName: str) -> DescribeEndpointOutputTypeDef:
        """
        [Client.describe_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_endpoint)
        """

    def describe_endpoint_config(
        self, EndpointConfigName: str
    ) -> DescribeEndpointConfigOutputTypeDef:
        """
        [Client.describe_endpoint_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_endpoint_config)
        """

    def describe_experiment(self, ExperimentName: str) -> DescribeExperimentResponseTypeDef:
        """
        [Client.describe_experiment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_experiment)
        """

    def describe_flow_definition(
        self, FlowDefinitionName: str
    ) -> DescribeFlowDefinitionResponseTypeDef:
        """
        [Client.describe_flow_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_flow_definition)
        """

    def describe_human_task_ui(self, HumanTaskUiName: str) -> DescribeHumanTaskUiResponseTypeDef:
        """
        [Client.describe_human_task_ui documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_human_task_ui)
        """

    def describe_hyper_parameter_tuning_job(
        self, HyperParameterTuningJobName: str
    ) -> DescribeHyperParameterTuningJobResponseTypeDef:
        """
        [Client.describe_hyper_parameter_tuning_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_hyper_parameter_tuning_job)
        """

    def describe_image(self, ImageName: str) -> DescribeImageResponseTypeDef:
        """
        [Client.describe_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_image)
        """

    def describe_image_version(
        self, ImageName: str, Version: int = None
    ) -> DescribeImageVersionResponseTypeDef:
        """
        [Client.describe_image_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_image_version)
        """

    def describe_labeling_job(self, LabelingJobName: str) -> DescribeLabelingJobResponseTypeDef:
        """
        [Client.describe_labeling_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_labeling_job)
        """

    def describe_model(self, ModelName: str) -> DescribeModelOutputTypeDef:
        """
        [Client.describe_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_model)
        """

    def describe_model_package(self, ModelPackageName: str) -> DescribeModelPackageOutputTypeDef:
        """
        [Client.describe_model_package documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_model_package)
        """

    def describe_monitoring_schedule(
        self, MonitoringScheduleName: str
    ) -> DescribeMonitoringScheduleResponseTypeDef:
        """
        [Client.describe_monitoring_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_monitoring_schedule)
        """

    def describe_notebook_instance(
        self, NotebookInstanceName: str
    ) -> DescribeNotebookInstanceOutputTypeDef:
        """
        [Client.describe_notebook_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_notebook_instance)
        """

    def describe_notebook_instance_lifecycle_config(
        self, NotebookInstanceLifecycleConfigName: str
    ) -> DescribeNotebookInstanceLifecycleConfigOutputTypeDef:
        """
        [Client.describe_notebook_instance_lifecycle_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_notebook_instance_lifecycle_config)
        """

    def describe_processing_job(
        self, ProcessingJobName: str
    ) -> DescribeProcessingJobResponseTypeDef:
        """
        [Client.describe_processing_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_processing_job)
        """

    def describe_subscribed_workteam(
        self, WorkteamArn: str
    ) -> DescribeSubscribedWorkteamResponseTypeDef:
        """
        [Client.describe_subscribed_workteam documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_subscribed_workteam)
        """

    def describe_training_job(self, TrainingJobName: str) -> DescribeTrainingJobResponseTypeDef:
        """
        [Client.describe_training_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_training_job)
        """

    def describe_transform_job(self, TransformJobName: str) -> DescribeTransformJobResponseTypeDef:
        """
        [Client.describe_transform_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_transform_job)
        """

    def describe_trial(self, TrialName: str) -> DescribeTrialResponseTypeDef:
        """
        [Client.describe_trial documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_trial)
        """

    def describe_trial_component(
        self, TrialComponentName: str
    ) -> DescribeTrialComponentResponseTypeDef:
        """
        [Client.describe_trial_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_trial_component)
        """

    def describe_user_profile(
        self, DomainId: str, UserProfileName: str
    ) -> DescribeUserProfileResponseTypeDef:
        """
        [Client.describe_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_user_profile)
        """

    def describe_workforce(self, WorkforceName: str) -> DescribeWorkforceResponseTypeDef:
        """
        [Client.describe_workforce documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_workforce)
        """

    def describe_workteam(self, WorkteamName: str) -> DescribeWorkteamResponseTypeDef:
        """
        [Client.describe_workteam documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.describe_workteam)
        """

    def disassociate_trial_component(
        self, TrialComponentName: str, TrialName: str
    ) -> DisassociateTrialComponentResponseTypeDef:
        """
        [Client.disassociate_trial_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.disassociate_trial_component)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.generate_presigned_url)
        """

    def get_search_suggestions(
        self,
        Resource: Literal[
            "TrainingJob", "Experiment", "ExperimentTrial", "ExperimentTrialComponent"
        ],
        SuggestionQuery: SuggestionQueryTypeDef = None,
    ) -> GetSearchSuggestionsResponseTypeDef:
        """
        [Client.get_search_suggestions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.get_search_suggestions)
        """

    def list_algorithms(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        MaxResults: int = None,
        NameContains: str = None,
        NextToken: str = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
    ) -> ListAlgorithmsOutputTypeDef:
        """
        [Client.list_algorithms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_algorithms)
        """

    def list_app_image_configs(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        ModifiedTimeBefore: datetime = None,
        ModifiedTimeAfter: datetime = None,
        SortBy: Literal["CreationTime", "LastModifiedTime", "Name"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
    ) -> ListAppImageConfigsResponseTypeDef:
        """
        [Client.list_app_image_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_app_image_configs)
        """

    def list_apps(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        SortBy: Literal["CreationTime"] = None,
        DomainIdEquals: str = None,
        UserProfileNameEquals: str = None,
    ) -> ListAppsResponseTypeDef:
        """
        [Client.list_apps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_apps)
        """

    def list_auto_ml_jobs(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: Literal["Completed", "InProgress", "Failed", "Stopped", "Stopping"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListAutoMLJobsResponseTypeDef:
        """
        [Client.list_auto_ml_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_auto_ml_jobs)
        """

    def list_candidates_for_auto_ml_job(
        self,
        AutoMLJobName: str,
        StatusEquals: Literal["Completed", "InProgress", "Failed", "Stopped", "Stopping"] = None,
        CandidateNameEquals: str = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        SortBy: Literal["CreationTime", "Status", "FinalObjectiveMetricValue"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListCandidatesForAutoMLJobResponseTypeDef:
        """
        [Client.list_candidates_for_auto_ml_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_candidates_for_auto_ml_job)
        """

    def list_code_repositories(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        MaxResults: int = None,
        NameContains: str = None,
        NextToken: str = None,
        SortBy: Literal["Name", "CreationTime", "LastModifiedTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
    ) -> ListCodeRepositoriesOutputTypeDef:
        """
        [Client.list_code_repositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_code_repositories)
        """

    def list_compilation_jobs(
        self,
        NextToken: str = None,
        MaxResults: int = None,
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
    ) -> ListCompilationJobsResponseTypeDef:
        """
        [Client.list_compilation_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_compilation_jobs)
        """

    def list_domains(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListDomainsResponseTypeDef:
        """
        [Client.list_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_domains)
        """

    def list_endpoint_configs(
        self,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
    ) -> ListEndpointConfigsOutputTypeDef:
        """
        [Client.list_endpoint_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_endpoint_configs)
        """

    def list_endpoints(
        self,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NextToken: str = None,
        MaxResults: int = None,
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
    ) -> ListEndpointsOutputTypeDef:
        """
        [Client.list_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_endpoints)
        """

    def list_experiments(
        self,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListExperimentsResponseTypeDef:
        """
        [Client.list_experiments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_experiments)
        """

    def list_flow_definitions(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListFlowDefinitionsResponseTypeDef:
        """
        [Client.list_flow_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_flow_definitions)
        """

    def list_human_task_uis(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListHumanTaskUisResponseTypeDef:
        """
        [Client.list_human_task_uis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_human_task_uis)
        """

    def list_hyper_parameter_tuning_jobs(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        SortBy: Literal["Name", "Status", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        StatusEquals: Literal["Completed", "InProgress", "Failed", "Stopped", "Stopping"] = None,
    ) -> ListHyperParameterTuningJobsResponseTypeDef:
        """
        [Client.list_hyper_parameter_tuning_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_hyper_parameter_tuning_jobs)
        """

    def list_image_versions(
        self,
        ImageName: str,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: Literal["CREATION_TIME", "LAST_MODIFIED_TIME", "VERSION"] = None,
        SortOrder: Literal["ASCENDING", "DESCENDING"] = None,
    ) -> ListImageVersionsResponseTypeDef:
        """
        [Client.list_image_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_image_versions)
        """

    def list_images(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        MaxResults: int = None,
        NameContains: str = None,
        NextToken: str = None,
        SortBy: Literal["CREATION_TIME", "LAST_MODIFIED_TIME", "IMAGE_NAME"] = None,
        SortOrder: Literal["ASCENDING", "DESCENDING"] = None,
    ) -> ListImagesResponseTypeDef:
        """
        [Client.list_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_images)
        """

    def list_labeling_jobs(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        MaxResults: int = None,
        NextToken: str = None,
        NameContains: str = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        StatusEquals: Literal[
            "Initializing", "InProgress", "Completed", "Failed", "Stopping", "Stopped"
        ] = None,
    ) -> ListLabelingJobsResponseTypeDef:
        """
        [Client.list_labeling_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_labeling_jobs)
        """

    def list_labeling_jobs_for_workteam(
        self,
        WorkteamArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        JobReferenceCodeContains: str = None,
        SortBy: Literal["CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
    ) -> ListLabelingJobsForWorkteamResponseTypeDef:
        """
        [Client.list_labeling_jobs_for_workteam documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_labeling_jobs_for_workteam)
        """

    def list_model_packages(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        MaxResults: int = None,
        NameContains: str = None,
        NextToken: str = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
    ) -> ListModelPackagesOutputTypeDef:
        """
        [Client.list_model_packages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_model_packages)
        """

    def list_models(
        self,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
    ) -> ListModelsOutputTypeDef:
        """
        [Client.list_models documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_models)
        """

    def list_monitoring_executions(
        self,
        MonitoringScheduleName: str = None,
        EndpointName: str = None,
        SortBy: Literal["CreationTime", "ScheduledTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NextToken: str = None,
        MaxResults: int = None,
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
    ) -> ListMonitoringExecutionsResponseTypeDef:
        """
        [Client.list_monitoring_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_monitoring_executions)
        """

    def list_monitoring_schedules(
        self,
        EndpointName: str = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: Literal["Pending", "Failed", "Scheduled", "Stopped"] = None,
    ) -> ListMonitoringSchedulesResponseTypeDef:
        """
        [Client.list_monitoring_schedules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_monitoring_schedules)
        """

    def list_notebook_instance_lifecycle_configs(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        SortBy: Literal["Name", "CreationTime", "LastModifiedTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
    ) -> ListNotebookInstanceLifecycleConfigsOutputTypeDef:
        """
        [Client.list_notebook_instance_lifecycle_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_notebook_instance_lifecycle_configs)
        """

    def list_notebook_instances(
        self,
        NextToken: str = None,
        MaxResults: int = None,
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
    ) -> ListNotebookInstancesOutputTypeDef:
        """
        [Client.list_notebook_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_notebook_instances)
        """

    def list_processing_jobs(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"] = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListProcessingJobsResponseTypeDef:
        """
        [Client.list_processing_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_processing_jobs)
        """

    def list_subscribed_workteams(
        self, NameContains: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListSubscribedWorkteamsResponseTypeDef:
        """
        [Client.list_subscribed_workteams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_subscribed_workteams)
        """

    def list_tags(
        self, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsOutputTypeDef:
        """
        [Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_tags)
        """

    def list_training_jobs(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"] = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
    ) -> ListTrainingJobsResponseTypeDef:
        """
        [Client.list_training_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_training_jobs)
        """

    def list_training_jobs_for_hyper_parameter_tuning_job(
        self,
        HyperParameterTuningJobName: str,
        NextToken: str = None,
        MaxResults: int = None,
        StatusEquals: Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"] = None,
        SortBy: Literal["Name", "CreationTime", "Status", "FinalObjectiveMetricValue"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
    ) -> ListTrainingJobsForHyperParameterTuningJobResponseTypeDef:
        """
        [Client.list_training_jobs_for_hyper_parameter_tuning_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_training_jobs_for_hyper_parameter_tuning_job)
        """

    def list_transform_jobs(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"] = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListTransformJobsResponseTypeDef:
        """
        [Client.list_transform_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_transform_jobs)
        """

    def list_trial_components(
        self,
        ExperimentName: str = None,
        TrialName: str = None,
        SourceArn: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListTrialComponentsResponseTypeDef:
        """
        [Client.list_trial_components documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_trial_components)
        """

    def list_trials(
        self,
        ExperimentName: str = None,
        TrialComponentName: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListTrialsResponseTypeDef:
        """
        [Client.list_trials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_trials)
        """

    def list_user_profiles(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        SortBy: Literal["CreationTime", "LastModifiedTime"] = None,
        DomainIdEquals: str = None,
        UserProfileNameContains: str = None,
    ) -> ListUserProfilesResponseTypeDef:
        """
        [Client.list_user_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_user_profiles)
        """

    def list_workforces(
        self,
        SortBy: Literal["Name", "CreateDate"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListWorkforcesResponseTypeDef:
        """
        [Client.list_workforces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_workforces)
        """

    def list_workteams(
        self,
        SortBy: Literal["Name", "CreateDate"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListWorkteamsResponseTypeDef:
        """
        [Client.list_workteams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.list_workteams)
        """

    def render_ui_template(
        self,
        Task: RenderableTaskTypeDef,
        RoleArn: str,
        UiTemplate: UiTemplateTypeDef = None,
        HumanTaskUiArn: str = None,
    ) -> RenderUiTemplateResponseTypeDef:
        """
        [Client.render_ui_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.render_ui_template)
        """

    def search(
        self,
        Resource: Literal[
            "TrainingJob", "Experiment", "ExperimentTrial", "ExperimentTrialComponent"
        ],
        SearchExpression: Dict[str, Any] = None,
        SortBy: str = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> SearchResponseTypeDef:
        """
        [Client.search documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.search)
        """

    def start_monitoring_schedule(self, MonitoringScheduleName: str) -> None:
        """
        [Client.start_monitoring_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.start_monitoring_schedule)
        """

    def start_notebook_instance(self, NotebookInstanceName: str) -> None:
        """
        [Client.start_notebook_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.start_notebook_instance)
        """

    def stop_auto_ml_job(self, AutoMLJobName: str) -> None:
        """
        [Client.stop_auto_ml_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.stop_auto_ml_job)
        """

    def stop_compilation_job(self, CompilationJobName: str) -> None:
        """
        [Client.stop_compilation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.stop_compilation_job)
        """

    def stop_hyper_parameter_tuning_job(self, HyperParameterTuningJobName: str) -> None:
        """
        [Client.stop_hyper_parameter_tuning_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.stop_hyper_parameter_tuning_job)
        """

    def stop_labeling_job(self, LabelingJobName: str) -> None:
        """
        [Client.stop_labeling_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.stop_labeling_job)
        """

    def stop_monitoring_schedule(self, MonitoringScheduleName: str) -> None:
        """
        [Client.stop_monitoring_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.stop_monitoring_schedule)
        """

    def stop_notebook_instance(self, NotebookInstanceName: str) -> None:
        """
        [Client.stop_notebook_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.stop_notebook_instance)
        """

    def stop_processing_job(self, ProcessingJobName: str) -> None:
        """
        [Client.stop_processing_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.stop_processing_job)
        """

    def stop_training_job(self, TrainingJobName: str) -> None:
        """
        [Client.stop_training_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.stop_training_job)
        """

    def stop_transform_job(self, TransformJobName: str) -> None:
        """
        [Client.stop_transform_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.stop_transform_job)
        """

    def update_app_image_config(
        self,
        AppImageConfigName: str,
        KernelGatewayImageConfig: "KernelGatewayImageConfigTypeDef" = None,
    ) -> UpdateAppImageConfigResponseTypeDef:
        """
        [Client.update_app_image_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.update_app_image_config)
        """

    def update_code_repository(
        self, CodeRepositoryName: str, GitConfig: GitConfigForUpdateTypeDef = None
    ) -> UpdateCodeRepositoryOutputTypeDef:
        """
        [Client.update_code_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.update_code_repository)
        """

    def update_domain(
        self, DomainId: str, DefaultUserSettings: "UserSettingsTypeDef" = None
    ) -> UpdateDomainResponseTypeDef:
        """
        [Client.update_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.update_domain)
        """

    def update_endpoint(
        self,
        EndpointName: str,
        EndpointConfigName: str,
        RetainAllVariantProperties: bool = None,
        ExcludeRetainedVariantProperties: List[VariantPropertyTypeDef] = None,
    ) -> UpdateEndpointOutputTypeDef:
        """
        [Client.update_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.update_endpoint)
        """

    def update_endpoint_weights_and_capacities(
        self, EndpointName: str, DesiredWeightsAndCapacities: List[DesiredWeightAndCapacityTypeDef]
    ) -> UpdateEndpointWeightsAndCapacitiesOutputTypeDef:
        """
        [Client.update_endpoint_weights_and_capacities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.update_endpoint_weights_and_capacities)
        """

    def update_experiment(
        self, ExperimentName: str, DisplayName: str = None, Description: str = None
    ) -> UpdateExperimentResponseTypeDef:
        """
        [Client.update_experiment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.update_experiment)
        """

    def update_image(
        self,
        ImageName: str,
        DeleteProperties: List[str] = None,
        Description: str = None,
        DisplayName: str = None,
        RoleArn: str = None,
    ) -> UpdateImageResponseTypeDef:
        """
        [Client.update_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.update_image)
        """

    def update_monitoring_schedule(
        self,
        MonitoringScheduleName: str,
        MonitoringScheduleConfig: "MonitoringScheduleConfigTypeDef",
    ) -> UpdateMonitoringScheduleResponseTypeDef:
        """
        [Client.update_monitoring_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.update_monitoring_schedule)
        """

    def update_notebook_instance(
        self,
        NotebookInstanceName: str,
        InstanceType: Literal[
            "ml.t2.medium",
            "ml.t2.large",
            "ml.t2.xlarge",
            "ml.t2.2xlarge",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.c5d.xlarge",
            "ml.c5d.2xlarge",
            "ml.c5d.4xlarge",
            "ml.c5d.9xlarge",
            "ml.c5d.18xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
        ] = None,
        RoleArn: str = None,
        LifecycleConfigName: str = None,
        DisassociateLifecycleConfig: bool = None,
        VolumeSizeInGB: int = None,
        DefaultCodeRepository: str = None,
        AdditionalCodeRepositories: List[str] = None,
        AcceleratorTypes: List[
            Literal[
                "ml.eia1.medium",
                "ml.eia1.large",
                "ml.eia1.xlarge",
                "ml.eia2.medium",
                "ml.eia2.large",
                "ml.eia2.xlarge",
            ]
        ] = None,
        DisassociateAcceleratorTypes: bool = None,
        DisassociateDefaultCodeRepository: bool = None,
        DisassociateAdditionalCodeRepositories: bool = None,
        RootAccess: Literal["Enabled", "Disabled"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_notebook_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.update_notebook_instance)
        """

    def update_notebook_instance_lifecycle_config(
        self,
        NotebookInstanceLifecycleConfigName: str,
        OnCreate: List["NotebookInstanceLifecycleHookTypeDef"] = None,
        OnStart: List["NotebookInstanceLifecycleHookTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_notebook_instance_lifecycle_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.update_notebook_instance_lifecycle_config)
        """

    def update_trial(self, TrialName: str, DisplayName: str = None) -> UpdateTrialResponseTypeDef:
        """
        [Client.update_trial documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.update_trial)
        """

    def update_trial_component(
        self,
        TrialComponentName: str,
        DisplayName: str = None,
        Status: "TrialComponentStatusTypeDef" = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Parameters: Dict[str, "TrialComponentParameterValueTypeDef"] = None,
        ParametersToRemove: List[str] = None,
        InputArtifacts: Dict[str, "TrialComponentArtifactTypeDef"] = None,
        InputArtifactsToRemove: List[str] = None,
        OutputArtifacts: Dict[str, "TrialComponentArtifactTypeDef"] = None,
        OutputArtifactsToRemove: List[str] = None,
    ) -> UpdateTrialComponentResponseTypeDef:
        """
        [Client.update_trial_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.update_trial_component)
        """

    def update_user_profile(
        self, DomainId: str, UserProfileName: str, UserSettings: "UserSettingsTypeDef" = None
    ) -> UpdateUserProfileResponseTypeDef:
        """
        [Client.update_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.update_user_profile)
        """

    def update_workforce(
        self,
        WorkforceName: str,
        SourceIpConfig: "SourceIpConfigTypeDef" = None,
        OidcConfig: OidcConfigTypeDef = None,
    ) -> UpdateWorkforceResponseTypeDef:
        """
        [Client.update_workforce documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.update_workforce)
        """

    def update_workteam(
        self,
        WorkteamName: str,
        MemberDefinitions: List["MemberDefinitionTypeDef"] = None,
        Description: str = None,
        NotificationConfiguration: "NotificationConfigurationTypeDef" = None,
    ) -> UpdateWorkteamResponseTypeDef:
        """
        [Client.update_workteam documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Client.update_workteam)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_algorithms"]) -> ListAlgorithmsPaginator:
        """
        [Paginator.ListAlgorithms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListAlgorithms)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_apps"]) -> ListAppsPaginator:
        """
        [Paginator.ListApps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListApps)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_auto_ml_jobs"]
    ) -> ListAutoMLJobsPaginator:
        """
        [Paginator.ListAutoMLJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListAutoMLJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_candidates_for_auto_ml_job"]
    ) -> ListCandidatesForAutoMLJobPaginator:
        """
        [Paginator.ListCandidatesForAutoMLJob documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListCandidatesForAutoMLJob)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_code_repositories"]
    ) -> ListCodeRepositoriesPaginator:
        """
        [Paginator.ListCodeRepositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListCodeRepositories)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_compilation_jobs"]
    ) -> ListCompilationJobsPaginator:
        """
        [Paginator.ListCompilationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListCompilationJobs)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_domains"]) -> ListDomainsPaginator:
        """
        [Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListDomains)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_endpoint_configs"]
    ) -> ListEndpointConfigsPaginator:
        """
        [Paginator.ListEndpointConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpointConfigs)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_endpoints"]) -> ListEndpointsPaginator:
        """
        [Paginator.ListEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpoints)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_experiments"]
    ) -> ListExperimentsPaginator:
        """
        [Paginator.ListExperiments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListExperiments)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_flow_definitions"]
    ) -> ListFlowDefinitionsPaginator:
        """
        [Paginator.ListFlowDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListFlowDefinitions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_human_task_uis"]
    ) -> ListHumanTaskUisPaginator:
        """
        [Paginator.ListHumanTaskUis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListHumanTaskUis)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_hyper_parameter_tuning_jobs"]
    ) -> ListHyperParameterTuningJobsPaginator:
        """
        [Paginator.ListHyperParameterTuningJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListHyperParameterTuningJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_image_versions"]
    ) -> ListImageVersionsPaginator:
        """
        [Paginator.ListImageVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListImageVersions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_images"]) -> ListImagesPaginator:
        """
        [Paginator.ListImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListImages)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_labeling_jobs"]
    ) -> ListLabelingJobsPaginator:
        """
        [Paginator.ListLabelingJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_labeling_jobs_for_workteam"]
    ) -> ListLabelingJobsForWorkteamPaginator:
        """
        [Paginator.ListLabelingJobsForWorkteam documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobsForWorkteam)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_packages"]
    ) -> ListModelPackagesPaginator:
        """
        [Paginator.ListModelPackages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListModelPackages)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_models"]) -> ListModelsPaginator:
        """
        [Paginator.ListModels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListModels)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_monitoring_executions"]
    ) -> ListMonitoringExecutionsPaginator:
        """
        [Paginator.ListMonitoringExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringExecutions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_monitoring_schedules"]
    ) -> ListMonitoringSchedulesPaginator:
        """
        [Paginator.ListMonitoringSchedules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringSchedules)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_notebook_instance_lifecycle_configs"]
    ) -> ListNotebookInstanceLifecycleConfigsPaginator:
        """
        [Paginator.ListNotebookInstanceLifecycleConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstanceLifecycleConfigs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_notebook_instances"]
    ) -> ListNotebookInstancesPaginator:
        """
        [Paginator.ListNotebookInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_processing_jobs"]
    ) -> ListProcessingJobsPaginator:
        """
        [Paginator.ListProcessingJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListProcessingJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscribed_workteams"]
    ) -> ListSubscribedWorkteamsPaginator:
        """
        [Paginator.ListSubscribedWorkteams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListSubscribedWorkteams)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tags"]) -> ListTagsPaginator:
        """
        [Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListTags)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_training_jobs"]
    ) -> ListTrainingJobsPaginator:
        """
        [Paginator.ListTrainingJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_training_jobs_for_hyper_parameter_tuning_job"]
    ) -> ListTrainingJobsForHyperParameterTuningJobPaginator:
        """
        [Paginator.ListTrainingJobsForHyperParameterTuningJob documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobsForHyperParameterTuningJob)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_transform_jobs"]
    ) -> ListTransformJobsPaginator:
        """
        [Paginator.ListTransformJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListTransformJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_trial_components"]
    ) -> ListTrialComponentsPaginator:
        """
        [Paginator.ListTrialComponents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListTrialComponents)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_trials"]) -> ListTrialsPaginator:
        """
        [Paginator.ListTrials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListTrials)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_user_profiles"]
    ) -> ListUserProfilesPaginator:
        """
        [Paginator.ListUserProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListUserProfiles)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_workforces"]) -> ListWorkforcesPaginator:
        """
        [Paginator.ListWorkforces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkforces)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_workteams"]) -> ListWorkteamsPaginator:
        """
        [Paginator.ListWorkteams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkteams)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search"]) -> SearchPaginator:
        """
        [Paginator.Search documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Paginator.Search)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["endpoint_deleted"]) -> EndpointDeletedWaiter:
        """
        [Waiter.EndpointDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Waiter.EndpointDeleted)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["endpoint_in_service"]) -> EndpointInServiceWaiter:
        """
        [Waiter.EndpointInService documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Waiter.EndpointInService)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["notebook_instance_deleted"]
    ) -> NotebookInstanceDeletedWaiter:
        """
        [Waiter.NotebookInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceDeleted)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["notebook_instance_in_service"]
    ) -> NotebookInstanceInServiceWaiter:
        """
        [Waiter.NotebookInstanceInService documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceInService)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["notebook_instance_stopped"]
    ) -> NotebookInstanceStoppedWaiter:
        """
        [Waiter.NotebookInstanceStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceStopped)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["processing_job_completed_or_stopped"]
    ) -> ProcessingJobCompletedOrStoppedWaiter:
        """
        [Waiter.ProcessingJobCompletedOrStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Waiter.ProcessingJobCompletedOrStopped)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["training_job_completed_or_stopped"]
    ) -> TrainingJobCompletedOrStoppedWaiter:
        """
        [Waiter.TrainingJobCompletedOrStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Waiter.TrainingJobCompletedOrStopped)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["transform_job_completed_or_stopped"]
    ) -> TransformJobCompletedOrStoppedWaiter:
        """
        [Waiter.TransformJobCompletedOrStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Waiter.TransformJobCompletedOrStopped)
        """
