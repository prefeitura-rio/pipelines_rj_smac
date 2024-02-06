# -*- coding: utf-8 -*-
"""
DBT-related flows.
"""

from copy import deepcopy

from prefect.run_configs import KubernetesRun
from prefect.storage import GCS

from pipelines.constants import constants
from pipelines.povo_comunidades_tradicionais.materialize_povo_comunidades_tradicionais.schedules import (  # noqa
    materialize_povo_comunidades_tradicionais_schedule,
)
from pipelines.templates.run_dbt_model.flows import templates__run_dbt_model_smac__flow

# from prefeitura_rio.pipelines_utils.state_handlers import handler_inject_bd_credentials


materialize_povo_comunidades_tradicionais_flow = deepcopy(templates__run_dbt_model_smac__flow)
materialize_povo_comunidades_tradicionais_flow.name = (
    "SMAC: povo_comunidades_tradicionais - Materializa tabelas"
)
# materialize_povo_comunidades_tradicionais_flow.state_handlers = [handler_inject_bd_credentials]


materialize_povo_comunidades_tradicionais_flow.storage = GCS(constants.GCS_FLOWS_BUCKET.value)
materialize_povo_comunidades_tradicionais_flow.run_config = KubernetesRun(
    image=constants.DOCKER_IMAGE.value,
    labels=[
        constants.RJ_SMAC_AGENT_LABEL.value,
    ],
)
materialize_povo_comunidades_tradicionais_flow.schedule = (
    materialize_povo_comunidades_tradicionais_schedule
)
