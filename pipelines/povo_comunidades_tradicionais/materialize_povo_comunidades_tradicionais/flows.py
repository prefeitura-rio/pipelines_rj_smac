# -*- coding: utf-8 -*-
"""
DBT-related flows.
"""

from copy import deepcopy

from prefect.run_configs import KubernetesRun
from prefect.storage import GCS
from prefeitura_rio.pipelines_templates.run_dbt_model.flows import (
    templates__run_dbt_model__flow,
)

from pipelines.constants import constants
from pipelines.povo_comunidades_tradicionais.materialize_povo_comunidades_tradicionais.schedules import (
    materialize_povo_comunidades_tradicionais_schedule,
)

materialize_povo_comunidades_tradicionais_flow = deepcopy(templates__run_dbt_model__flow)
materialize_povo_comunidades_tradicionais_flow.name = (
    "SMAC: povo_comunidades_tradicionais - Materializar tabelas."
)
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
