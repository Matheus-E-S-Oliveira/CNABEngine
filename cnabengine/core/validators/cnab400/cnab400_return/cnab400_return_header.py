from cnabengine.core.validators.core.numeric_validator import NumericValidator
from cnabengine.core.validators.core.date_validator import DateValidator

# Observações:
# A validação do arquivo de retorno foi feita com base no codígo conforme pedido, como codigo não valida os valores
# no momento esta sendo feita apenas as validações de conversão para valore numéricos e valores de datas
# no caso das strings não esta sendoo feita nehuma validação no momento pois por natureza eles são strings dede o começo
# e não está sendo validação dos valores, pois não e especificado quais campos podem ou não estar vazios e como requerimento 
# foi de fazer baseado no codígo do sistema nenhuma validação foi aplicada alem da de checar conversão dos valores
# e além disso não será feita validação do TRILLER pois no sistema não está sendo implementada

def validate_header(header: str, errors: list[str]) -> None:
    context = "HEADER"
    
    if len(header) != 400:
        errors.append(f"[{context}]: O cabeçalho (HEADER) do CNAB 400 deve conter exatamente 400 caracteres.")
        return
    
    # Posição 001-001 - Tipo de Registro
    NumericValidator.validate_numeric(field=header[0:1], context=context, position="001-001", errors=errors)
    
    # Posição 002-002 - Codigo de retorno
    NumericValidator.validate_numeric(field=header[1:2], context=context, position="002-002", errors=errors)
    
    # Posição 003-009 - Literal retorno
    # Validação de conversão de string desnecessária
    
    # Posição 010-011 - Codigo Serviço
    NumericValidator.validate_numeric(field=header[9:11], context=context, position="010-011", errors=errors)
    
    # Posição 012-026 - Literal Serviço
    # Validação de conversão de string desnecessária
    
    # Posição 027-030 - Agencia
    NumericValidator.validate_numeric(field=header[26:30], context=context, position="027-030", errors=errors)
    
    # Posição 031-032 - Complemento Registro 1
    NumericValidator.validate_numeric(field=header[30:32], context=context, position="031-032", errors=errors)
    
    # Posição 033-037 - Conta
    NumericValidator.validate_numeric(field=header[32:37], context=context, position="033-037", errors=errors)
    
    # Posição 038-038 - DAC Conta
    NumericValidator.validate_numeric(field=header[37:38], context=context, position="038-038", errors=errors)
    
    # Posição 039-046 - Complemento Registro 2
    # validação de conversão de string desnecessária
    
    # Posição 047-076 - Nome da Empresa
    # Validação de conversão de string desnecessária
    
    # Posição 077-079 - Código Banco
    NumericValidator.validate_numeric(field=header[76:79], context=context, position="077-079", errors=errors)
    
    # Posição 080-094 - Nome Banco
    # Validação de conversão de string desnecessária
    
    # Posição 095-100 - Data Geração
    DateValidator.validate_date_format_ddmmaa(field=header[94:100], context=context, position="095-100", errors=errors)
    
    # Posição 101-105 - Densidade
    NumericValidator.validate_numeric(field=header[100:105], context=context, position="101-105", errors=errors)
    
    # Posição 106-108 - Unidade Densidade
    # Validação de conversão de string descenessária
    
    # Posição 109-113 - Número Sequencial Arquivo Retorno
    # Verificar para ver se é para vir dado aqui ta meio controversio, verificar se é obrigatorio
    NumericValidator.validate_numeric(field=header[108:113], context=context, position="109-113", errors=errors)
    
    # Posição 114-119 - Data Credito
    # Verificar para ver se é para vir dado aqui ta meio controversio, verificar se é obrigatorio
    DateValidator.validate_date_format_ddmmaa(field=header[113:119], context=context, position="114-119", errors=errors)
    
    # Posição 120-394 - Complemento Registro 3
    # Validação de conversão de string desncessária
    
    # Posição 395-400 - Número sequencial
    NumericValidator.validate_numeric(field=header[394:400], context=context, position="395-400", errors=errors)