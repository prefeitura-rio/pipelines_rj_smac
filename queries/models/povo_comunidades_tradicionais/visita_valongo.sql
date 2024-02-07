SELECT
    DATETIME(periodo, "America/Sao_Paulo") AS ano_mes,
    SAFECAST(ano AS INT64) AS ano,
    CAST(mes AS STRING) AS mes,
    CAST(valor_visitacao AS INT64) AS valor_visitacao
FROM `rj-smac.povo_comunidades_tradicionais_staging.visita_valongo`