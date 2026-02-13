from cnabengine.core.validators.core.static_validator import StaticValidator
from cnabengine.core.validators.core.numeric_validator import NumericValidator

def validate_triller(triller: str, errors: list[str], number_lines: int) -> None:
    context = "TRILLER"
    
    if len(triller) != 400:
        errors.append(f"[{context}]: comprimento inválido. Cada linha do CNAB 400 deve conter exatamente 400 caracteres.")
        return errors
    
    # Posição no arquivo: 001-001
    StaticValidator.validate_field_static_numeric(triller[0:1], context=context, position="001-001", errors=errors, value="9")
    
    # Posição no arquivo: 002-394
    StaticValidator.validate_field_space(triller[1:394], context=context, position="002-394", errors=errors)
    
    # Posição no arquivo: 395-400
    NumericValidator.validate_numeric_no_zeros_and_register(triller[394:400], context=context, position="395-400", errors=errors, fieldName="número de registro", number_lines=number_lines)
    
    return