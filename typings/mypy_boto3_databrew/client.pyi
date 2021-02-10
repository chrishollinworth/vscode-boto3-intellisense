"""
Main interface for databrew service client

Usage::

    ```python
    import boto3
    from mypy_boto3_databrew import GlueDataBrewClient

    client: GlueDataBrewClient = boto3.client("databrew")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_databrew.paginator import (
    ListDatasetsPaginator,
    ListJobRunsPaginator,
    ListJobsPaginator,
    ListProjectsPaginator,
    ListRecipesPaginator,
    ListRecipeVersionsPaginator,
    ListSchedulesPaginator,
)
from mypy_boto3_databrew.type_defs import (
    BatchDeleteRecipeVersionResponseTypeDef,
    CreateDatasetResponseTypeDef,
    CreateProfileJobResponseTypeDef,
    CreateProjectResponseTypeDef,
    CreateRecipeJobResponseTypeDef,
    CreateRecipeResponseTypeDef,
    CreateScheduleResponseTypeDef,
    DeleteDatasetResponseTypeDef,
    DeleteJobResponseTypeDef,
    DeleteProjectResponseTypeDef,
    DeleteRecipeVersionResponseTypeDef,
    DeleteScheduleResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeJobResponseTypeDef,
    DescribeJobRunResponseTypeDef,
    DescribeProjectResponseTypeDef,
    DescribeRecipeResponseTypeDef,
    DescribeScheduleResponseTypeDef,
    FormatOptionsTypeDef,
    InputTypeDef,
    ListDatasetsResponseTypeDef,
    ListJobRunsResponseTypeDef,
    ListJobsResponseTypeDef,
    ListProjectsResponseTypeDef,
    ListRecipesResponseTypeDef,
    ListRecipeVersionsResponseTypeDef,
    ListSchedulesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    OutputTypeDef,
    PublishRecipeResponseTypeDef,
    RecipeReferenceTypeDef,
    RecipeStepTypeDef,
    S3LocationTypeDef,
    SampleTypeDef,
    SendProjectSessionActionResponseTypeDef,
    StartJobRunResponseTypeDef,
    StartProjectSessionResponseTypeDef,
    StopJobRunResponseTypeDef,
    UpdateDatasetResponseTypeDef,
    UpdateProfileJobResponseTypeDef,
    UpdateProjectResponseTypeDef,
    UpdateRecipeJobResponseTypeDef,
    UpdateRecipeResponseTypeDef,
    UpdateScheduleResponseTypeDef,
    ViewFrameTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GlueDataBrewClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class GlueDataBrewClient:
    """
    [GlueDataBrew.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_delete_recipe_version(
        self, Name: str, RecipeVersions: List[str]
    ) -> BatchDeleteRecipeVersionResponseTypeDef:
        """
        [Client.batch_delete_recipe_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.batch_delete_recipe_version)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.can_paginate)
        """

    def create_dataset(
        self,
        Name: str,
        Input: "InputTypeDef",
        FormatOptions: "FormatOptionsTypeDef" = None,
        Tags: Dict[str, str] = None,
    ) -> CreateDatasetResponseTypeDef:
        """
        [Client.create_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.create_dataset)
        """

    def create_profile_job(
        self,
        DatasetName: str,
        Name: str,
        OutputLocation: "S3LocationTypeDef",
        RoleArn: str,
        EncryptionKeyArn: str = None,
        EncryptionMode: Literal["SSE-KMS", "SSE-S3"] = None,
        LogSubscription: Literal["ENABLE", "DISABLE"] = None,
        MaxCapacity: int = None,
        MaxRetries: int = None,
        Tags: Dict[str, str] = None,
        Timeout: int = None,
    ) -> CreateProfileJobResponseTypeDef:
        """
        [Client.create_profile_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.create_profile_job)
        """

    def create_project(
        self,
        DatasetName: str,
        Name: str,
        RecipeName: str,
        RoleArn: str,
        Sample: "SampleTypeDef" = None,
        Tags: Dict[str, str] = None,
    ) -> CreateProjectResponseTypeDef:
        """
        [Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.create_project)
        """

    def create_recipe(
        self,
        Name: str,
        Steps: List["RecipeStepTypeDef"],
        Description: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateRecipeResponseTypeDef:
        """
        [Client.create_recipe documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.create_recipe)
        """

    def create_recipe_job(
        self,
        Name: str,
        Outputs: List["OutputTypeDef"],
        RoleArn: str,
        DatasetName: str = None,
        EncryptionKeyArn: str = None,
        EncryptionMode: Literal["SSE-KMS", "SSE-S3"] = None,
        LogSubscription: Literal["ENABLE", "DISABLE"] = None,
        MaxCapacity: int = None,
        MaxRetries: int = None,
        ProjectName: str = None,
        RecipeReference: "RecipeReferenceTypeDef" = None,
        Tags: Dict[str, str] = None,
        Timeout: int = None,
    ) -> CreateRecipeJobResponseTypeDef:
        """
        [Client.create_recipe_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.create_recipe_job)
        """

    def create_schedule(
        self,
        CronExpression: str,
        Name: str,
        JobNames: List[str] = None,
        Tags: Dict[str, str] = None,
    ) -> CreateScheduleResponseTypeDef:
        """
        [Client.create_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.create_schedule)
        """

    def delete_dataset(self, Name: str) -> DeleteDatasetResponseTypeDef:
        """
        [Client.delete_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.delete_dataset)
        """

    def delete_job(self, Name: str) -> DeleteJobResponseTypeDef:
        """
        [Client.delete_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.delete_job)
        """

    def delete_project(self, Name: str) -> DeleteProjectResponseTypeDef:
        """
        [Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.delete_project)
        """

    def delete_recipe_version(
        self, Name: str, RecipeVersion: str
    ) -> DeleteRecipeVersionResponseTypeDef:
        """
        [Client.delete_recipe_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.delete_recipe_version)
        """

    def delete_schedule(self, Name: str) -> DeleteScheduleResponseTypeDef:
        """
        [Client.delete_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.delete_schedule)
        """

    def describe_dataset(self, Name: str) -> DescribeDatasetResponseTypeDef:
        """
        [Client.describe_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.describe_dataset)
        """

    def describe_job(self, Name: str) -> DescribeJobResponseTypeDef:
        """
        [Client.describe_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.describe_job)
        """

    def describe_job_run(self, Name: str, RunId: str) -> DescribeJobRunResponseTypeDef:
        """
        [Client.describe_job_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.describe_job_run)
        """

    def describe_project(self, Name: str) -> DescribeProjectResponseTypeDef:
        """
        [Client.describe_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.describe_project)
        """

    def describe_recipe(
        self, Name: str, RecipeVersion: str = None
    ) -> DescribeRecipeResponseTypeDef:
        """
        [Client.describe_recipe documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.describe_recipe)
        """

    def describe_schedule(self, Name: str) -> DescribeScheduleResponseTypeDef:
        """
        [Client.describe_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.describe_schedule)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.generate_presigned_url)
        """

    def list_datasets(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListDatasetsResponseTypeDef:
        """
        [Client.list_datasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.list_datasets)
        """

    def list_job_runs(
        self, Name: str, MaxResults: int = None, NextToken: str = None
    ) -> ListJobRunsResponseTypeDef:
        """
        [Client.list_job_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.list_job_runs)
        """

    def list_jobs(
        self,
        DatasetName: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        ProjectName: str = None,
    ) -> ListJobsResponseTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.list_jobs)
        """

    def list_projects(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListProjectsResponseTypeDef:
        """
        [Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.list_projects)
        """

    def list_recipe_versions(
        self, Name: str, MaxResults: int = None, NextToken: str = None
    ) -> ListRecipeVersionsResponseTypeDef:
        """
        [Client.list_recipe_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.list_recipe_versions)
        """

    def list_recipes(
        self, MaxResults: int = None, NextToken: str = None, RecipeVersion: str = None
    ) -> ListRecipesResponseTypeDef:
        """
        [Client.list_recipes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.list_recipes)
        """

    def list_schedules(
        self, JobName: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListSchedulesResponseTypeDef:
        """
        [Client.list_schedules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.list_schedules)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.list_tags_for_resource)
        """

    def publish_recipe(self, Name: str, Description: str = None) -> PublishRecipeResponseTypeDef:
        """
        [Client.publish_recipe documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.publish_recipe)
        """

    def send_project_session_action(
        self,
        Name: str,
        Preview: bool = None,
        RecipeStep: "RecipeStepTypeDef" = None,
        StepIndex: int = None,
        ClientSessionId: str = None,
        ViewFrame: ViewFrameTypeDef = None,
    ) -> SendProjectSessionActionResponseTypeDef:
        """
        [Client.send_project_session_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.send_project_session_action)
        """

    def start_job_run(self, Name: str) -> StartJobRunResponseTypeDef:
        """
        [Client.start_job_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.start_job_run)
        """

    def start_project_session(
        self, Name: str, AssumeControl: bool = None
    ) -> StartProjectSessionResponseTypeDef:
        """
        [Client.start_project_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.start_project_session)
        """

    def stop_job_run(self, Name: str, RunId: str) -> StopJobRunResponseTypeDef:
        """
        [Client.stop_job_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.stop_job_run)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.untag_resource)
        """

    def update_dataset(
        self, Name: str, Input: "InputTypeDef", FormatOptions: "FormatOptionsTypeDef" = None
    ) -> UpdateDatasetResponseTypeDef:
        """
        [Client.update_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.update_dataset)
        """

    def update_profile_job(
        self,
        Name: str,
        OutputLocation: "S3LocationTypeDef",
        RoleArn: str,
        EncryptionKeyArn: str = None,
        EncryptionMode: Literal["SSE-KMS", "SSE-S3"] = None,
        LogSubscription: Literal["ENABLE", "DISABLE"] = None,
        MaxCapacity: int = None,
        MaxRetries: int = None,
        Timeout: int = None,
    ) -> UpdateProfileJobResponseTypeDef:
        """
        [Client.update_profile_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.update_profile_job)
        """

    def update_project(
        self, RoleArn: str, Name: str, Sample: "SampleTypeDef" = None
    ) -> UpdateProjectResponseTypeDef:
        """
        [Client.update_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.update_project)
        """

    def update_recipe(
        self, Name: str, Description: str = None, Steps: List["RecipeStepTypeDef"] = None
    ) -> UpdateRecipeResponseTypeDef:
        """
        [Client.update_recipe documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.update_recipe)
        """

    def update_recipe_job(
        self,
        Name: str,
        Outputs: List["OutputTypeDef"],
        RoleArn: str,
        EncryptionKeyArn: str = None,
        EncryptionMode: Literal["SSE-KMS", "SSE-S3"] = None,
        LogSubscription: Literal["ENABLE", "DISABLE"] = None,
        MaxCapacity: int = None,
        MaxRetries: int = None,
        Timeout: int = None,
    ) -> UpdateRecipeJobResponseTypeDef:
        """
        [Client.update_recipe_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.update_recipe_job)
        """

    def update_schedule(
        self, CronExpression: str, Name: str, JobNames: List[str] = None
    ) -> UpdateScheduleResponseTypeDef:
        """
        [Client.update_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Client.update_schedule)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_datasets"]) -> ListDatasetsPaginator:
        """
        [Paginator.ListDatasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Paginator.ListDatasets)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_job_runs"]) -> ListJobRunsPaginator:
        """
        [Paginator.ListJobRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Paginator.ListJobRuns)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Paginator.ListJobs)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_projects"]) -> ListProjectsPaginator:
        """
        [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Paginator.ListProjects)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_recipe_versions"]
    ) -> ListRecipeVersionsPaginator:
        """
        [Paginator.ListRecipeVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Paginator.ListRecipeVersions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_recipes"]) -> ListRecipesPaginator:
        """
        [Paginator.ListRecipes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Paginator.ListRecipes)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_schedules"]) -> ListSchedulesPaginator:
        """
        [Paginator.ListSchedules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Paginator.ListSchedules)
        """
