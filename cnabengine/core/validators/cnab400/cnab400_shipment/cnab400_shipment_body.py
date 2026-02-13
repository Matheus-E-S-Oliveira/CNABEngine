from cnabengine.core.validators.core.static_validator import StaticValidator
from cnabengine.core.validators.core.numeric_validator import NumericValidator
from cnabengine.core.validators.core.alpha_validator import AlphaValidator
from cnabengine.core.validators.core.date_validator import DateValidator

def validate_body(body: list[str], errors: list[str]) -> None:
    
    for i, line in enumerate(body, start=2):
        context = f"BODY LINE {i}"
        
        if len(line) != 400:
            errors.append(f"[{context}]: comprimento inválido. Cada linha do CNAB 400 deve conter exatamente 400 caracteres.")
            continue
        
        # Posição no arquivo: 001-001
        StaticValidator.validate_field_static_numeric(field=line[0:1], context=context, position="001-001", errors=errors, value="7")
        
        # Posição no arquivo: 002-003
        NumericValidator.validate_numeric_no_zeros(field=line[1:3], context=context, position="002-003", errors=errors, fieldName="tipo cedente")
        
        # Posição no arquivo: 004-017
        NumericValidator.validate_numeric_no_zeros(field=line[3:17], context=context, position="004-017", errors=errors, fieldName="cpf/cnpj")
        
        # Posição no arquivo: 018-021
        NumericValidator.validate_numeric_no_zeros(field=line[17:21], context=context, position="018-021", errors=errors, fieldName="agência")
        
        # Posição no arquivo: 022-022
        AlphaValidator.validate_alpha(field=line[21:22], context=context, position="022-022", errors=errors, fieldName="dígito da agência")
        
        # Posição no arquivo: 023-030
        NumericValidator.validate_numeric_no_zeros(field=line[22:30], context=context, position="023-030", errors=errors, fieldName="conta")
        
        # Posição no arquivo: 031-031
        AlphaValidator.validate_alpha(field=line[30:31], context=context, position="031-031", errors=errors, fieldName="dígito da conta")
        
        # Posição no arquivo: 032-038
        AlphaValidator.validate_alpha(field=line[31:38], context=context, position="032-038", errors=errors, fieldName="convênio")
        
        # Posição no arquivo: 039-063
        AlphaValidator.validate_alpha(field=line[38:63], context=context, position="039-063", errors=errors, fieldName="número de controle")
        
        # Posição no arquivo: 064-080
        NumericValidator.validate_numeric_no_zeros(field=line[63:80], context=context, position="064-080", errors=errors, fieldName="nosso número")
        
        # Posição no arquivo: 081-082
        StaticValidator.validate_field_static_numeric(field=line[80:82], context=context, position="081-082", errors=errors, value="00")
        
        # Posição no arquivo: 083-084
        StaticValidator.validate_field_static_numeric(field=line[82:84], context=context, position="081-082", errors=errors, value="00")
        
        # Posição no arquivo: 085-087
        StaticValidator.validate_field_space(field=line[84:87], context= context, position="085-087", errors=errors)
        
        # Posição no arquivo: 088-088
        StaticValidator.validate_field_space(field=line[87:88], context=context, position="088-088", errors=errors)
        
        # Posição no arquivo: 089-091
        StaticValidator.validate_field_space(field=line[88:91], context=context, position="089-094", errors=errors)
        
        # Posição no arquivo: 092-094
        NumericValidator.validate_numeric(field=line[91:94], context=context, position="092-094", errors=errors)
        
        # Posição no arquivo: 095-095
        StaticValidator.validate_field_static_numeric(field=line[94:95], context=context, position="095-095", errors=errors, value="0")
        
        # Posição no arquivo: 096-101
        StaticValidator.validate_field_static_numeric(field=line[95:101], context=context, position="096-101", errors=errors, value="000000")
        
        # Posição no arquivo: 102-106
        StaticValidator.validate_field_space(field=line[101:106], context=context, position="102-106", errors=errors)
        
        # Posição no arquivo: 107-108
        NumericValidator.validate_numeric(field=line[106:108], context=context, position="107-108", errors=errors)
        
        # Posição no arquivo: 109-110
        AlphaValidator.validate_alpha(field=line[108:110], context=context, position="109-110", errors=errors, fieldName="código da ocorrência")
        
        # Posição no arquivo: 111-120
        NumericValidator.validate_numeric_no_zeros(field=line[110:120], context=context, position="111-120", errors=errors, fieldName="núemro controle")
        
        # Posição no arquivo: 121-126
        DateValidator.validate_date_format_ddmmaa(field=line[120:126], context=context, position="121-126", errors=errors)
        
        # Posição no arquivo: 127-139
        NumericValidator.validate_numeric_no_zeros(field=line[126:139], context=context, position="127-139", errors=errors, fieldName="valor do boleto")
        
        # Posição no arquivo: 140-142
        StaticValidator.validate_field_static_numeric(field=line[139:142], context=context, position="140-142", errors=errors, value="001")
        
        # Posição no arquivo: 143-146
        StaticValidator.validate_field_static_numeric(field=line[142:146], context=context, position="143-146", errors=errors, value="0000")
        
        # Posição no arquivo: 147-147
        StaticValidator.validate_field_space(field=line[146:147], context=context, position="147-147", errors=errors)        
        
        # Posição no arquivo: 148-149
        NumericValidator.validate_numeric_no_zeros(field=line[147:149], context=context, position="148-149", errors=errors, fieldName="espécie")
        
        # Posição no arquivo: 150-150
        AlphaValidator.validate_alpha(field=line[149:150], context=context, position="150-150", errors=errors, fieldName="aceite")
        
        # Posição no arquivo: 151-156
        DateValidator.validate_date_format_ddmmaa(field=line[150:156], context=context, position="151-156", errors=errors)
        
        # Posição no arquivo: 157-158
        NumericValidator.validate_numeric(field=line[156:158], context=context, position="157-158", errors=errors)
        
        # Posição no arquivo: 159-160
        NumericValidator.validate_numeric(field=line[158:160], context=context, position="159-160", errors=errors)
        
        # Posição no arquivo: 161-173
        NumericValidator.validate_numeric(field=line[160:173], context=context, position="161-173", errors=errors)
        
        # Posição no arquivo: 174 à 205 layout de multa ou desconto
        if(line[108:110] in ["35", "36"]):
            __fineFieldsLayout(line=line, context=context, errors=errors)
        else:
            __discountFieldsLayout(line=line, context=context, errors=errors)
            
        # Posição no arquivo: 206-218
        NumericValidator.validate_numeric(field=line[205:218], context=context, position="206-218", errors=errors)
        
        # Posição no arquivo: 219-220
        NumericValidator.validate_numeric_no_zeros(field=line[218:220], context=context, position="219-220", errors=errors, fieldName="tipo inscrição sacado")
        
        # Posição no arquivo: 221-234
        NumericValidator.validate_numeric_no_zeros(field=line[220:234], context=context, position="221-234", errors=errors, fieldName="cpf/cnpj")
        
        # Posição no arquivo: 235-271
        AlphaValidator.validate_alpha(field=line[234:271], context=context, position="235-271", errors=errors, fieldName="nome do sacado")
        
        # Posição no arquivo: 272-274
        StaticValidator.validate_field_space(field=line[271:274], context=context, position="272-274", errors=errors)
        
        # Posição no arquivo: 275-314
        AlphaValidator.validate_alpha(field=line[274:314], context=context, position="275-314", errors=errors, fieldName="endereço do sacado com número")
        
        # Posição no arquivo: 315-326
        AlphaValidator.validate_alpha(field=line[314:326], context=context, position="315-326", errors=errors, fieldName="bairro do sacado")
        
        # Posição no arquivo: 327-334
        NumericValidator.validate_numeric_no_zeros(field=line[326:334], context=context, position="327-334", errors=errors, fieldName="cep do sacado")
        
        # Posição no arquivo: 335-349
        AlphaValidator.validate_alpha(field=line[334:349], context=context, position="335-349", errors=errors, fieldName="cidade do sacado")
        
        # Posição no arquivo: 350-351
        AlphaValidator.validate_alpha(field=line[349:351], context=context, position="350-351", errors=errors, fieldName="uf do sacado")
        
        # Posição no arquivo: 352-391
        StaticValidator.validate_field_space(field=line[351:391], context=context, position="352-391", errors=errors)
        
        # Posição no arquivo: 392-393
        # Esse e por causa daquele switch que da 0, aí como não sabia se é obrigatorio este dado (provavelmente não) deixei verificando se o campo dele não esta vazio
        AlphaValidator.validate_alpha(field=line[391:393], context=context, position="392-393", errors=errors, fieldName="dias protesto")
        
        # Posição no arquivo: 394-394
        StaticValidator.validate_field_space(field=line[393:394], context=context, position="394-394", errors=errors)
        
        # Posição no arquivo: 395-400
        NumericValidator.validate_numeric_no_zeros(field=line[394:400], context=context, position="395-400", errors=errors, fieldName="número do registro")
    
    return
        
def __fineFieldsLayout(line: str, context: str, errors: list[str]) -> None:
    # Posição no arquivo: 174-174
    NumericValidator.validate_numeric_no_zeros(field=line[173:174], context=context, position="174-174", errors=errors, fieldName="código da multa")
    
    # Posição no arquivo: 175-180
    # Verificar se é obrigatorio
    DateValidator.validate_date_format_ddmmaa(field=line[174:180], context=context, position="175-180", errors=errors)
    
    # Posição no arquivo: 181-192
    NumericValidator.validate_numeric(field=line[180:192], context=context, position="181-192", errors=errors)
    
def __discountFieldsLayout(line: str, context: str, errors: list[str]) -> None:
    # Posição no arquivo: 174-179
    # Verificar se é obrigatorio
    DateValidator.validate_date_format_ddmmaa(field=line[173:179], context=context, position="174-179", errors=errors)
    
    # Posição no arquivo: 180-192
    NumericValidator.validate_numeric(field=line[179:192], context=context, position="180-192", errors=errors)
    
    # Posição no arquivo: 193-205
    NumericValidator.validate_numeric(field=line[192:205], context=context, position="193-205", errors=errors)
