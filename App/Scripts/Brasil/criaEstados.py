import pandas as pd

dataset = pd.DataFrame(
    {
        'Estado': [
            "Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul",
            "Alagoas", "Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco",
            "Piauí", "Rio Grande do Norte", "Sergipe", "Acre", "Amapá", "Amazonas",
            "Pará", "Rondônia", "Roraima", "Tocantins", "Espírito Santo", "Minas Gerais",
            "Rio de Janeiro", "São Paulo", "Paraná", "Rio Grande do Sul", "Santa Catarina"
        ],
        'UF': [
            "DF", "GO", "MT", "MS", "AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE",
            "AC", "AP", "AM", "PA", "RO", "RR", "TO", "ES", "MG", "RJ", "SP", "PR", "RS", "SC"
        ],
        'Capital': [
            "Brasília", "Goiânia", "Cuiabá", "Campo Grande", "Maceió", "Salvador", "Fortaleza",
            "São Luís", "João Pessoa", "Recife", "Teresina", "Natal", "Aracaju", "Rio Branco",
            "Macapá", "Manaus", "Belém", "Porto Velho", "Boa Vista", "Palmas", "Vitória",
            "Belo Horizonte", "Rio de Janeiro", "São Paulo", "Curitiba", "Porto Alegre",
            "Florianópolis"
        ],
        'Região': [
            "Centro-Oeste", "Centro-Oeste", "Centro-Oeste", "Centro-Oeste", "Nordeste",
            "Nordeste", "Nordeste", "Nordeste", "Nordeste", "Nordeste", "Nordeste", "Nordeste",
            "Nordeste", "Norte", "Norte", "Norte", "Norte", "Norte", "Norte", "Norte", "Sudeste",
            "Sudeste", "Sudeste", "Sudeste", "Sul", "Sul", "Sul"
        ]
    }
)
