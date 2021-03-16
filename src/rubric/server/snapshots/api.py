from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from rubric.server.commons.models import TaskType
from rubric.server.commons.settings import settings as api_settings
from rubric.server.security.api import get_current_active_user
from rubric.server.users.model import User

from .model import DatasetSnapshot
from .service import SnapshotsService, create_snapshots_service

router = APIRouter(
    tags=["snapshots"],
    prefix="/datasets",
    include_in_schema=not api_settings.only_bulk_api,
)


@router.get(
    "/{name}/snapshots",
    response_model=List[DatasetSnapshot],
    operation_id="list_dataset_snapshots",
)
def list_dataset_snapshots(
    name: str,
    task: Optional[TaskType] = Query(None),
    service: SnapshotsService = Depends(create_snapshots_service),
    current_user: User = Depends(get_current_active_user),
) -> List[DatasetSnapshot]:
    """
    List the created dataset snapshots

    Parameters
    ----------
    name:
        Dataset name
    task:
        Task type query selector. Optional
    service:
        Snapshots service
    current_user:
        Current request user

    Returns
    -------
        Snapshots list

    """
    return service.list(dataset=name, owner=current_user.current_group, task=task)


@router.get(
    "/{name}/snapshots/{snapshot_id}",
    response_model=DatasetSnapshot,
    operation_id="get_dataset_snapshot",
)
def get_dataset_snapshot(
    name: str,
    snapshot_id: str,
    service: SnapshotsService = Depends(create_snapshots_service),
    current_user: User = Depends(get_current_active_user),
) -> DatasetSnapshot:
    """
    Get snapshot by id

    Parameters
    ----------
    name:
        Dataset name
    snapshot_id:
        Snapshot id
    service:
        Snapshots service
    current_user:
        Current request user

    Returns
    -------
        Found snapshot
    """
    return service.get(dataset=name, owner=current_user.current_group, id=snapshot_id)


@router.post(
    "/{name}/snapshots",
    response_model=DatasetSnapshot,
    operation_id="create_dataset_snapshots",
)
def create_dataset_snapshots(
    name: str,
    task: Optional[TaskType] = Query(None),
    service: SnapshotsService = Depends(create_snapshots_service),
    current_user: User = Depends(get_current_active_user),
) -> DatasetSnapshot:
    """
    Creates a dataset snapshot

    Parameters
    ----------
    name:
        Dataset name
    task:
        Task type query selector
    service:
        Snapshots service
    current_user:
        Current request user

    Returns
    -------
        Created snapshot
    """

    return service.create(dataset=name, owner=current_user.current_group, task=task)


@router.delete(
    "/{name}/snapshots/{snapshot_id}", operation_id="delete_dataset_snapshot"
)
def delete_dataset_snapshot(
    name: str,
    snapshot_id: str,
    service: SnapshotsService = Depends(create_snapshots_service),
    current_user: User = Depends(get_current_active_user),
):
    """
    Deletes an dataset snapshot

    Parameters
    ----------

    name:
        Dataset name
    snapshot_id:
        Snapshot id
    service:
        Snapshots service
    current_user:
        Current request user

    """
    service.delete(name, owner=current_user.current_group, id=snapshot_id)