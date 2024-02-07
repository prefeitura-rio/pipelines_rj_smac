{{ config(alias='investimento_valongo') }}

SELECT
    CAST(nome_org AS STRING) AS nome_org,
    CAST(v__nculo_institucional AS STRING) AS vinculo_institucional,
    CAST(natureza_inv AS STRING) AS natureza_inv,
    CAST(origem_inv AS STRING) AS origem_inv,
    CAST(fonte_inv AS STRING) AS fonte_inv,
    CAST(abrang__ncia_origem_inv AS STRING) AS abrangencia_origem_inv,
    SAFE_CAST(valor_inv__R__ AS INT64) AS valor_inv,
    CAST(periodo_inv AS STRING) AS periodo_inv,
    CAST(objetivo_inv_ AS STRING) AS objetivo_inv,
    CAST(fonte_dados AS STRING) AS fonte_dados
FROM `rj-smac.investimento_valongo_staging.investimento_valongo`