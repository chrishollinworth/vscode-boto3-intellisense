# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for sagemaker service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_sagemaker import SageMakerClient
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

    client: SageMakerClient = boto3.client("sagemaker")

    endpoint_deleted_waiter: EndpointDeletedWaiter = client.get_waiter("endpoint_deleted")
    endpoint_in_service_waiter: EndpointInServiceWaiter = client.get_waiter("endpoint_in_service")
    notebook_instance_deleted_waiter: NotebookInstanceDeletedWaiter = client.get_waiter("notebook_instance_deleted")
    notebook_instance_in_service_waiter: NotebookInstanceInServiceWaiter = client.get_waiter("notebook_instance_in_service")
    notebook_instance_stopped_waiter: NotebookInstanceStoppedWaiter = client.get_waiter("notebook_instance_stopped")
    processing_job_completed_or_stopped_waiter: ProcessingJobCompletedOrStoppedWaiter = client.get_waiter("processing_job_completed_or_stopped")
    training_job_completed_or_stopped_waiter: TrainingJobCompletedOrStoppedWaiter = client.get_waiter("training_job_completed_or_stopped")
    transform_job_completed_or_stopped_waiter: TransformJobCompletedOrStoppedWaiter = client.get_waiter("transform_job_completed_or_stopped")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_sagemaker.type_defs import WaiterConfigTypeDef

__all__ = (
    "EndpointDeletedWaiter",
    "EndpointInServiceWaiter",
    "NotebookInstanceDeletedWaiter",
    "NotebookInstanceInServiceWaiter",
    "NotebookInstanceStoppedWaiter",
    "ProcessingJobCompletedOrStoppedWaiter",
    "TrainingJobCompletedOrStoppedWaiter",
    "TransformJobCompletedOrStoppedWaiter",
)


class EndpointDeletedWaiter(Boto3Waiter):
    """
    [Waiter.EndpointDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Waiter.EndpointDeleted)
    """

    def wait(self, EndpointName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [EndpointDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Waiter.EndpointDeleted.wait)
        """


class EndpointInServiceWaiter(Boto3Waiter):
    """
    [Waiter.EndpointInService documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Waiter.EndpointInService)
    """

    def wait(self, EndpointName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [EndpointInService.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Waiter.EndpointInService.wait)
        """


class NotebookInstanceDeletedWaiter(Boto3Waiter):
    """
    [Waiter.NotebookInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceDeleted)
    """

    def wait(self, NotebookInstanceName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [NotebookInstanceDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceDeleted.wait)
        """


class NotebookInstanceInServiceWaiter(Boto3Waiter):
    """
    [Waiter.NotebookInstanceInService documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceInService)
    """

    def wait(self, NotebookInstanceName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [NotebookInstanceInService.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceInService.wait)
        """


class NotebookInstanceStoppedWaiter(Boto3Waiter):
    """
    [Waiter.NotebookInstanceStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceStopped)
    """

    def wait(self, NotebookInstanceName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [NotebookInstanceStopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceStopped.wait)
        """


class ProcessingJobCompletedOrStoppedWaiter(Boto3Waiter):
    """
    [Waiter.ProcessingJobCompletedOrStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Waiter.ProcessingJobCompletedOrStopped)
    """

    def wait(self, ProcessingJobName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [ProcessingJobCompletedOrStopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Waiter.ProcessingJobCompletedOrStopped.wait)
        """


class TrainingJobCompletedOrStoppedWaiter(Boto3Waiter):
    """
    [Waiter.TrainingJobCompletedOrStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Waiter.TrainingJobCompletedOrStopped)
    """

    def wait(self, TrainingJobName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [TrainingJobCompletedOrStopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Waiter.TrainingJobCompletedOrStopped.wait)
        """


class TransformJobCompletedOrStoppedWaiter(Boto3Waiter):
    """
    [Waiter.TransformJobCompletedOrStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Waiter.TransformJobCompletedOrStopped)
    """

    def wait(self, TransformJobName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [TransformJobCompletedOrStopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sagemaker.html#SageMaker.Waiter.TransformJobCompletedOrStopped.wait)
        """
