# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for cloudformation service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_cloudformation import CloudFormationClient
    from mypy_boto3_cloudformation.waiter import (
        ChangeSetCreateCompleteWaiter,
        StackCreateCompleteWaiter,
        StackDeleteCompleteWaiter,
        StackExistsWaiter,
        StackImportCompleteWaiter,
        StackRollbackCompleteWaiter,
        StackUpdateCompleteWaiter,
        TypeRegistrationCompleteWaiter,
    )

    client: CloudFormationClient = boto3.client("cloudformation")

    change_set_create_complete_waiter: ChangeSetCreateCompleteWaiter = client.get_waiter("change_set_create_complete")
    stack_create_complete_waiter: StackCreateCompleteWaiter = client.get_waiter("stack_create_complete")
    stack_delete_complete_waiter: StackDeleteCompleteWaiter = client.get_waiter("stack_delete_complete")
    stack_exists_waiter: StackExistsWaiter = client.get_waiter("stack_exists")
    stack_import_complete_waiter: StackImportCompleteWaiter = client.get_waiter("stack_import_complete")
    stack_rollback_complete_waiter: StackRollbackCompleteWaiter = client.get_waiter("stack_rollback_complete")
    stack_update_complete_waiter: StackUpdateCompleteWaiter = client.get_waiter("stack_update_complete")
    type_registration_complete_waiter: TypeRegistrationCompleteWaiter = client.get_waiter("type_registration_complete")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_cloudformation.type_defs import WaiterConfigTypeDef

__all__ = (
    "ChangeSetCreateCompleteWaiter",
    "StackCreateCompleteWaiter",
    "StackDeleteCompleteWaiter",
    "StackExistsWaiter",
    "StackImportCompleteWaiter",
    "StackRollbackCompleteWaiter",
    "StackUpdateCompleteWaiter",
    "TypeRegistrationCompleteWaiter",
)


class ChangeSetCreateCompleteWaiter(Boto3Waiter):
    """
    [Waiter.ChangeSetCreateComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Waiter.ChangeSetCreateComplete)
    """

    def wait(
        self,
        ChangeSetName: str,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ChangeSetCreateComplete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Waiter.ChangeSetCreateComplete.wait)
        """


class StackCreateCompleteWaiter(Boto3Waiter):
    """
    [Waiter.StackCreateComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Waiter.StackCreateComplete)
    """

    def wait(
        self, StackName: str = None, NextToken: str = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [StackCreateComplete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Waiter.StackCreateComplete.wait)
        """


class StackDeleteCompleteWaiter(Boto3Waiter):
    """
    [Waiter.StackDeleteComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Waiter.StackDeleteComplete)
    """

    def wait(
        self, StackName: str = None, NextToken: str = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [StackDeleteComplete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Waiter.StackDeleteComplete.wait)
        """


class StackExistsWaiter(Boto3Waiter):
    """
    [Waiter.StackExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Waiter.StackExists)
    """

    def wait(
        self, StackName: str = None, NextToken: str = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [StackExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Waiter.StackExists.wait)
        """


class StackImportCompleteWaiter(Boto3Waiter):
    """
    [Waiter.StackImportComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Waiter.StackImportComplete)
    """

    def wait(
        self, StackName: str = None, NextToken: str = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [StackImportComplete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Waiter.StackImportComplete.wait)
        """


class StackRollbackCompleteWaiter(Boto3Waiter):
    """
    [Waiter.StackRollbackComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Waiter.StackRollbackComplete)
    """

    def wait(
        self, StackName: str = None, NextToken: str = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [StackRollbackComplete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Waiter.StackRollbackComplete.wait)
        """


class StackUpdateCompleteWaiter(Boto3Waiter):
    """
    [Waiter.StackUpdateComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Waiter.StackUpdateComplete)
    """

    def wait(
        self, StackName: str = None, NextToken: str = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [StackUpdateComplete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Waiter.StackUpdateComplete.wait)
        """


class TypeRegistrationCompleteWaiter(Boto3Waiter):
    """
    [Waiter.TypeRegistrationComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Waiter.TypeRegistrationComplete)
    """

    def wait(self, RegistrationToken: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [TypeRegistrationComplete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Waiter.TypeRegistrationComplete.wait)
        """
