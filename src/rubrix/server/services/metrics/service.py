from typing import Any, Dict, Optional, Type, TypeVar

from fastapi import Depends

from rubrix.server.daos.models.records import RecordSearch
from rubrix.server.daos.records import DatasetRecordsDAO
from rubrix.server.services.datasets import Dataset
from rubrix.server.services.metrics.models import BaseMetric, PythonMetric
from rubrix.server.services.tasks.commons.record import BaseRecordDB

GenericQuery = TypeVar("GenericQuery")


class MetricsService:
    """The dataset metrics service singleton"""

    _INSTANCE = None

    @classmethod
    def get_instance(
        cls,
        dao: DatasetRecordsDAO = Depends(DatasetRecordsDAO.get_instance),
    ) -> "MetricsService":
        """
        Creates the service instance.

        Parameters
        ----------
        dao:
            The dataset records dao

        Returns
        -------
            The metrics service instance

        """
        if not cls._INSTANCE:
            cls._INSTANCE = cls(dao)
        return cls._INSTANCE

    def __init__(self, dao: DatasetRecordsDAO):
        """
        Creates a service instance

        Parameters
        ----------
        dao:
            The dataset records dao
        """
        self.__dao__ = dao

    def summarize_metric(
        self,
        dataset: Dataset,
        metric: BaseMetric,
        record_class: Optional[Type[BaseRecordDB]] = None,
        query: Optional[GenericQuery] = None,
        **metric_params,
    ) -> Dict[str, Any]:
        """
        Applies a metric summarization.

        Parameters
        ----------
        dataset:
            The records dataset
        metric:
            The selected metric
        record_class:
            The record class type for python metrics computation
        query:
            An optional query passed for records filtering
        metric_params:
            Related metrics parameters

        Returns
        -------
            The metric summarization info
        """

        if isinstance(metric, PythonMetric):
            records = self.__dao__.scan_dataset(
                dataset, search=RecordSearch(query=query)
            )
            return metric.apply(map(record_class.parse_obj, records))

        return self.__dao__.compute_metric(
            metric_id=metric.id,
            metric_params=metric_params,
            dataset=dataset,
            query=query,
        )