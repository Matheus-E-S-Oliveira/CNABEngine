from cnabengine.core.validators.core.static_validator import StaticValidator
from cnabengine.core.validators.core.numeric_validator import NumericValidator
from cnabengine.core.validators.core.alpha_validator import AlphaValidator
from cnabengine.core.validators.core.date_validator import DateValidator

def validate_trailer(trailer: str, len: int) -> list[str]:
    context = "TRAILER"
    errors = []
    
    if len(trailer) != 400:
        errors.append(f"[{context}]: comprimento inválido. Cada linha do CNAB 400 deve conter exatamente 400 caracteres.")
        return errors
    
    # Posição no arquivo: 001-001
    StaticValidator.validate_field_static_numeric(trailer[0:1], context=context, position="001-001", errors=errors, value="9")
    
    # Posição no arquivo: 002-394
    StaticValidator.validate_field_space(trailer[1:394], context=context, position="002-394", errors=errors)
    
    # Posição no arquivo: 395-400
    NumericValidator.validate_numeric_no_zeros(trailer[394:400], context=context, position="395-400", errors=errors fieldName="número de registro")
    
    return errors