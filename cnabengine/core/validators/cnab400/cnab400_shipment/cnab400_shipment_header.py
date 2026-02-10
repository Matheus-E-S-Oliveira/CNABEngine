from cnabengine.core.validators.core.static_validator import StaticValidator
from cnabengine.core.validators.core.numeric_validator import NumericValidator
from cnabengine.core.validators.core.alpha_validator import AlphaValidator
from cnabengine.core.validators.core.date_validator import DateValidator

def validate_header(header: str) -> list[str]:
    errors = []
    context = "HEADER"
 
    if len(header) != 400:
        errors.append(f"[{context}]: O cabeçalho (HEADER) do CNAB 400 deve conter exatamente 400 caracteres.")
        return errors

    # Posição no arquivo: 001-001
    StaticValidator.validate_field_static_numeric(field=header[0:1], context=context, position='001-001', errors=errors, value="0")    

    # Posição no arquivo: 002-002
    StaticValidator.validate_field_static_numeric(field=header[1:2], context=context, position='002-002', errors=errors, value="1")
        
    # Posição no arquivo: 003-009
    StaticValidator.validate_field_static_alpha(field=header[2:9], context=context, position='003-009', errors=errors, value="REMESSA")
        
    # Posição no arquivo: 010-011
    StaticValidator.validate_field_static_alpha(field=header[9:11], context=context, position="010-011", errors=errors, value="01")
        
    # Posição no arquivo: 012-019
    StaticValidator.validate_field_static_alpha(field=header[11:19], context=context, position="012-019", errors=errors, value="COBRANCA")
        
    # Posição no arquivo: 020-026
    StaticValidator.validate_field_space(field=header[19:26], context=context, position="020-026", errors=errors)
    
    # Posição no arquivo: 027-030
    NumericValidator.validate_numeric_no_zeros(field=header[26:30], context=context, position="027-030", errors=errors, fieldName="agência")

    # Posição no arquivo: 031-031
    AlphaValidator.validate_alpha(field=header[30:31], context=context, position="031-031", errors=errors, fieldName="dígito da agência")
    
    # Posição no arquivo: 032-039
    NumericValidator.validate_numeric_no_zeros(field=header[31:39], context=context, position="032-039", errors=errors, fieldName="conta")
        
    # Posição no arquivo: 040-040
    AlphaValidator.validate_alpha(field=header[39:40], context=context, position="040-040", errors=errors, fieldName="dígito da conta")

    # Posição no arquivo: 041-046
    StaticValidator.validate_field_static_numeric(field=header[40:46], context=context, position="041-046", errors=errors, value="000000")
    
    # Posição no arquivo: 047-076
    AlphaValidator.validate_alpha(field=header[46:76], context=context, position="047-076", errors=errors, fieldName="nome do cedente")
        
    # Posição no arquivo: 077-094
    StaticValidator.validate_field_static_alpha(field=header[76:94], context=context, position="077-094", errors=errors, value="001BANCODOBRASIL")
    
    # Posição no arquivo: 094-100
    DateValidator.validate_date_format_ddmmaa(field=header[94:100], context=context, position="095-100", errors=errors)
        
    # Posição no arquivo: 101-107
    NumericValidator.validate_numeric_no_zeros(field=header[100:107], context=context, position="101-107", errors=errors, fieldName="número arquivo remessa")        

    # Posição no arquivo: 108-129
    StaticValidator.validate_field_space(field=header[107:129], context=context, position="108-129", errors=errors)        

    # Posição no arquivo: 130-136
    NumericValidator.validate_numeric_no_zeros(field=header[129:136], context=context, position="130-136", errors=errors, fieldName="convênio")   
    
    # Posição no arquivo: 137-394
    StaticValidator.validate_field_space(field=header[136:394], context=context, position="137-394", errors=errors)
    
    # Posição no arquivo: 395-400
    StaticValidator.validate_field_static_numeric(field=header[394:400], context=context, position="395-400", errors=errors, value="000001")
    
    return errors