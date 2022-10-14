"""
Type annotations for databrew service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_databrew import GlueDataBrewClient

    client: GlueDataBrewClient = boto3.client("databrew")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import EncryptionModeType, InputFormatType, LogSubscriptionType
from .paginator import (
    ListDatasetsPaginator,
    ListJobRunsPaginator,
    ListJobsPaginator,
    ListProjectsPaginator,
    ListRecipesPaginator,
    ListRecipeVersionsPaginator,
    ListRulesetsPaginator,
    ListSchedulesPaginator,
)
from .type_defs import (
    BatchDeleteRecipeVersionResponseTypeDef,
    CreateDatasetResponseTypeDef,
    CreateProfileJobResponseTypeDef,
    CreateProjectResponseTypeDef,
    CreateRecipeJobResponseTypeDef,
    CreateRecipeResponseTypeDef,
    CreateRulesetResponseTypeDef,
    CreateScheduleResponseTypeDef,
    DatabaseOutputTypeDef,
    DataCatalogOutputTypeDef,
    DeleteDatasetResponseTypeDef,
    DeleteJobResponseTypeDef,
    DeleteProjectResponseTypeDef,
    DeleteRecipeVersionResponseTypeDef,
    DeleteRulesetResponseTypeDef,
    DeleteScheduleResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeJobResponseTypeDef,
    DescribeJobRunResponseTypeDef,
    DescribeProjectResponseTypeDef,
    DescribeRecipeResponseTypeDef,
    DescribeRulesetResponseTypeDef,
    DescribeScheduleResponseTypeDef,
    FormatOptionsTypeDef,
    InputTypeDef,
    JobSampleTypeDef,
    ListDatasetsResponseTypeDef,
    ListJobRunsResponseTypeDef,
    ListJobsResponseTypeDef,
    ListProjectsResponseTypeDef,
    ListRecipesResponseTypeDef,
    ListRecipeVersionsResponseTypeDef,
    ListRulesetsResponseTypeDef,
    ListSchedulesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    OutputTypeDef,
    PathOptionsTypeDef,
    ProfileConfigurationTypeDef,
    PublishRecipeResponseTypeDef,
    RecipeReferenceTypeDef,
    RecipeStepTypeDef,
    RuleTypeDef,
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
    UpdateRulesetResponseTypeDef,
    UpdateScheduleResponseTypeDef,
    ValidationConfigurationTypeDef,
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

class GlueDataBrewClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        GlueDataBrewClient exceptions.
        """
    def batch_delete_recipe_version(
        self, *, Name: str, RecipeVersions: List[str]
    ) -> BatchDeleteRecipeVersionResponseTypeDef:
        """
        Deletes one or more versions of a recipe at a time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.batch_delete_recipe_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#batch_delete_recipe_version)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#close)
        """
    def create_dataset(
        self,
        *,
        Name: str,
        Input: "InputTypeDef",
        Format: InputFormatType = None,
        FormatOptions: "FormatOptionsTypeDef" = None,
        PathOptions: "PathOptionsTypeDef" = None,
        Tags: Dict[str, str] = None
    ) -> CreateDatasetResponseTypeDef:
        """
        Creates a new DataBrew dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.create_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#create_dataset)
        """
    def create_profile_job(
        self,
        *,
        DatasetName: str,
        Name: str,
        OutputLocation: "S3LocationTypeDef",
        RoleArn: str,
        EncryptionKeyArn: str = None,
        EncryptionMode: EncryptionModeType = None,
        LogSubscription: LogSubscriptionType = None,
        MaxCapacity: int = None,
        MaxRetries: int = None,
        Configuration: "ProfileConfigurationTypeDef" = None,
        ValidationConfigurations: List["ValidationConfigurationTypeDef"] = None,
        Tags: Dict[str, str] = None,
        Timeout: int = None,
        JobSample: "JobSampleTypeDef" = None
    ) -> CreateProfileJobResponseTypeDef:
        """
        Creates a new job to analyze a dataset and create its data profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.create_profile_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#create_profile_job)
        """
    def create_project(
        self,
        *,
        DatasetName: str,
        Name: str,
        RecipeName: str,
        RoleArn: str,
        Sample: "SampleTypeDef" = None,
        Tags: Dict[str, str] = None
    ) -> CreateProjectResponseTypeDef:
        """
        Creates a new DataBrew project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.create_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#create_project)
        """
    def create_recipe(
        self,
        *,
        Name: str,
        Steps: List["RecipeStepTypeDef"],
        Description: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateRecipeResponseTypeDef:
        """
        Creates a new DataBrew recipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.create_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#create_recipe)
        """
    def create_recipe_job(
        self,
        *,
        Name: str,
        RoleArn: str,
        DatasetName: str = None,
        EncryptionKeyArn: str = None,
        EncryptionMode: EncryptionModeType = None,
        LogSubscription: LogSubscriptionType = None,
        MaxCapacity: int = None,
        MaxRetries: int = None,
        Outputs: List["OutputTypeDef"] = None,
        DataCatalogOutputs: List["DataCatalogOutputTypeDef"] = None,
        DatabaseOutputs: List["DatabaseOutputTypeDef"] = None,
        ProjectName: str = None,
        RecipeReference: "RecipeReferenceTypeDef" = None,
        Tags: Dict[str, str] = None,
        Timeout: int = None
    ) -> CreateRecipeJobResponseTypeDef:
        """
        Creates a new job to transform input data, using steps defined in an existing
        Glue DataBrew recipe See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/databrew-2017-07-25/CreateRecipeJob>`_
        **Request Syntax** response = client.create_recipe_job( DatasetName...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.create_recipe_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#create_recipe_job)
        """
    def create_ruleset(
        self,
        *,
        Name: str,
        TargetArn: str,
        Rules: List["RuleTypeDef"],
        Description: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateRulesetResponseTypeDef:
        """
        Creates a new ruleset that can be used in a profile job to validate the data
        quality of a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.create_ruleset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#create_ruleset)
        """
    def create_schedule(
        self,
        *,
        CronExpression: str,
        Name: str,
        JobNames: List[str] = None,
        Tags: Dict[str, str] = None
    ) -> CreateScheduleResponseTypeDef:
        """
        Creates a new schedule for one or more DataBrew jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.create_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#create_schedule)
        """
    def delete_dataset(self, *, Name: str) -> DeleteDatasetResponseTypeDef:
        """
        Deletes a dataset from DataBrew.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.delete_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#delete_dataset)
        """
    def delete_job(self, *, Name: str) -> DeleteJobResponseTypeDef:
        """
        Deletes the specified DataBrew job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.delete_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#delete_job)
        """
    def delete_project(self, *, Name: str) -> DeleteProjectResponseTypeDef:
        """
        Deletes an existing DataBrew project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.delete_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#delete_project)
        """
    def delete_recipe_version(
        self, *, Name: str, RecipeVersion: str
    ) -> DeleteRecipeVersionResponseTypeDef:
        """
        Deletes a single version of a DataBrew recipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.delete_recipe_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#delete_recipe_version)
        """
    def delete_ruleset(self, *, Name: str) -> DeleteRulesetResponseTypeDef:
        """
        Deletes a ruleset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.delete_ruleset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#delete_ruleset)
        """
    def delete_schedule(self, *, Name: str) -> DeleteScheduleResponseTypeDef:
        """
        Deletes the specified DataBrew schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.delete_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#delete_schedule)
        """
    def describe_dataset(self, *, Name: str) -> DescribeDatasetResponseTypeDef:
        """
        Returns the definition of a specific DataBrew dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.describe_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#describe_dataset)
        """
    def describe_job(self, *, Name: str) -> DescribeJobResponseTypeDef:
        """
        Returns the definition of a specific DataBrew job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.describe_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#describe_job)
        """
    def describe_job_run(self, *, Name: str, RunId: str) -> DescribeJobRunResponseTypeDef:
        """
        Represents one run of a DataBrew job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.describe_job_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#describe_job_run)
        """
    def describe_project(self, *, Name: str) -> DescribeProjectResponseTypeDef:
        """
        Returns the definition of a specific DataBrew project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.describe_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#describe_project)
        """
    def describe_recipe(
        self, *, Name: str, RecipeVersion: str = None
    ) -> DescribeRecipeResponseTypeDef:
        """
        Returns the definition of a specific DataBrew recipe corresponding to a
        particular version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.describe_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#describe_recipe)
        """
    def describe_ruleset(self, *, Name: str) -> DescribeRulesetResponseTypeDef:
        """
        Retrieves detailed information about the ruleset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.describe_ruleset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#describe_ruleset)
        """
    def describe_schedule(self, *, Name: str) -> DescribeScheduleResponseTypeDef:
        """
        Returns the definition of a specific DataBrew schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.describe_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#describe_schedule)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#generate_presigned_url)
        """
    def list_datasets(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListDatasetsResponseTypeDef:
        """
        Lists all of the DataBrew datasets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.list_datasets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_datasets)
        """
    def list_job_runs(
        self, *, Name: str, MaxResults: int = None, NextToken: str = None
    ) -> ListJobRunsResponseTypeDef:
        """
        Lists all of the previous runs of a particular DataBrew job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.list_job_runs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_job_runs)
        """
    def list_jobs(
        self,
        *,
        DatasetName: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        ProjectName: str = None
    ) -> ListJobsResponseTypeDef:
        """
        Lists all of the DataBrew jobs that are defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.list_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_jobs)
        """
    def list_projects(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListProjectsResponseTypeDef:
        """
        Lists all of the DataBrew projects that are defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.list_projects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_projects)
        """
    def list_recipe_versions(
        self, *, Name: str, MaxResults: int = None, NextToken: str = None
    ) -> ListRecipeVersionsResponseTypeDef:
        """
        Lists the versions of a particular DataBrew recipe, except for `LATEST_WORKING`
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.list_recipe_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_recipe_versions)
        """
    def list_recipes(
        self, *, MaxResults: int = None, NextToken: str = None, RecipeVersion: str = None
    ) -> ListRecipesResponseTypeDef:
        """
        Lists all of the DataBrew recipes that are defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.list_recipes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_recipes)
        """
    def list_rulesets(
        self, *, TargetArn: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListRulesetsResponseTypeDef:
        """
        List all rulesets available in the current account or rulesets associated with a
        specific resource (dataset).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.list_rulesets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_rulesets)
        """
    def list_schedules(
        self, *, JobName: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListSchedulesResponseTypeDef:
        """
        Lists the DataBrew schedules that are defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.list_schedules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_schedules)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all the tags for a DataBrew resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_tags_for_resource)
        """
    def publish_recipe(self, *, Name: str, Description: str = None) -> PublishRecipeResponseTypeDef:
        """
        Publishes a new version of a DataBrew recipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.publish_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#publish_recipe)
        """
    def send_project_session_action(
        self,
        *,
        Name: str,
        Preview: bool = None,
        RecipeStep: "RecipeStepTypeDef" = None,
        StepIndex: int = None,
        ClientSessionId: str = None,
        ViewFrame: "ViewFrameTypeDef" = None
    ) -> SendProjectSessionActionResponseTypeDef:
        """
        Performs a recipe step within an interactive DataBrew session that's currently
        open.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.send_project_session_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#send_project_session_action)
        """
    def start_job_run(self, *, Name: str) -> StartJobRunResponseTypeDef:
        """
        Runs a DataBrew job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.start_job_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#start_job_run)
        """
    def start_project_session(
        self, *, Name: str, AssumeControl: bool = None
    ) -> StartProjectSessionResponseTypeDef:
        """
        Creates an interactive session, enabling you to manipulate data in a DataBrew
        project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.start_project_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#start_project_session)
        """
    def stop_job_run(self, *, Name: str, RunId: str) -> StopJobRunResponseTypeDef:
        """
        Stops a particular run of a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.stop_job_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#stop_job_run)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds metadata tags to a DataBrew resource, such as a dataset, project, recipe,
        job, or schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes metadata tags from a DataBrew resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#untag_resource)
        """
    def update_dataset(
        self,
        *,
        Name: str,
        Input: "InputTypeDef",
        Format: InputFormatType = None,
        FormatOptions: "FormatOptionsTypeDef" = None,
        PathOptions: "PathOptionsTypeDef" = None
    ) -> UpdateDatasetResponseTypeDef:
        """
        Modifies the definition of an existing DataBrew dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.update_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#update_dataset)
        """
    def update_profile_job(
        self,
        *,
        Name: str,
        OutputLocation: "S3LocationTypeDef",
        RoleArn: str,
        Configuration: "ProfileConfigurationTypeDef" = None,
        EncryptionKeyArn: str = None,
        EncryptionMode: EncryptionModeType = None,
        LogSubscription: LogSubscriptionType = None,
        MaxCapacity: int = None,
        MaxRetries: int = None,
        ValidationConfigurations: List["ValidationConfigurationTypeDef"] = None,
        Timeout: int = None,
        JobSample: "JobSampleTypeDef" = None
    ) -> UpdateProfileJobResponseTypeDef:
        """
        Modifies the definition of an existing profile job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.update_profile_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#update_profile_job)
        """
    def update_project(
        self, *, RoleArn: str, Name: str, Sample: "SampleTypeDef" = None
    ) -> UpdateProjectResponseTypeDef:
        """
        Modifies the definition of an existing DataBrew project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.update_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#update_project)
        """
    def update_recipe(
        self, *, Name: str, Description: str = None, Steps: List["RecipeStepTypeDef"] = None
    ) -> UpdateRecipeResponseTypeDef:
        """
        Modifies the definition of the `LATEST_WORKING` version of a DataBrew recipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.update_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#update_recipe)
        """
    def update_recipe_job(
        self,
        *,
        Name: str,
        RoleArn: str,
        EncryptionKeyArn: str = None,
        EncryptionMode: EncryptionModeType = None,
        LogSubscription: LogSubscriptionType = None,
        MaxCapacity: int = None,
        MaxRetries: int = None,
        Outputs: List["OutputTypeDef"] = None,
        DataCatalogOutputs: List["DataCatalogOutputTypeDef"] = None,
        DatabaseOutputs: List["DatabaseOutputTypeDef"] = None,
        Timeout: int = None
    ) -> UpdateRecipeJobResponseTypeDef:
        """
        Modifies the definition of an existing DataBrew recipe job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.update_recipe_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#update_recipe_job)
        """
    def update_ruleset(
        self, *, Name: str, Rules: List["RuleTypeDef"], Description: str = None
    ) -> UpdateRulesetResponseTypeDef:
        """
        Updates specified ruleset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.update_ruleset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#update_ruleset)
        """
    def update_schedule(
        self, *, CronExpression: str, Name: str, JobNames: List[str] = None
    ) -> UpdateScheduleResponseTypeDef:
        """
        Modifies the definition of an existing DataBrew schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Client.update_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#update_schedule)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_datasets"]) -> ListDatasetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Paginator.ListDatasets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listdatasetspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_job_runs"]) -> ListJobRunsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Paginator.ListJobRuns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listjobrunspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Paginator.ListJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listjobspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_projects"]) -> ListProjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Paginator.ListProjects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listprojectspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_recipe_versions"]
    ) -> ListRecipeVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Paginator.ListRecipeVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listrecipeversionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_recipes"]) -> ListRecipesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Paginator.ListRecipes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listrecipespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_rulesets"]) -> ListRulesetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Paginator.ListRulesets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listrulesetspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_schedules"]) -> ListSchedulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/databrew.html#GlueDataBrew.Paginator.ListSchedules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listschedulespaginator)
        """
