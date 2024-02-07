{{ config(alias='visita_valongo') }}

SELECT 
    PARSE_DATE('%Y%m', CAST(periodo AS STRING)) as ano_mes,
    CAST(ano AS INT64) as ano,
    CAST(mes AS STRING) as mes,
    CAST(valor_visitacao AS INT64) as valor_visitacao
FROM `rj-smac.povo_comunidades_tradicionais_staging.visita_valongo`
ORDER BY 1