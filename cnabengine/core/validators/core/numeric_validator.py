class NumericValidator:
    
    @staticmethod
    def validate_numeric(field: str, context: str, position: str, errors: list[str]) -> None:
        
        if field.strip() == "":
            errors.append(f"[{context}] Posição {position}: campo vazio. "
                        "Valor esperado: sequência numérica.")
            
        elif not field.isdigit():
            errors.append(f"[{context}] Posição {position}: não é um número."
                        "Valor esperado: sequência numérica.")
            
    @staticmethod        
    def validate_numeric_no_zeros(field: str, context: str, position: str, errors: list[str], fieldName: str) -> None:
        
        if field.strip() == "":
            errors.append(f"[{context}] Posição {position}: campo vazio. "
                        "Valor esperado: sequência numérica.")
            
        elif not field.isdigit():
            errors.append(f"[{context}] Posição {position}: não é um número."
                        "Valor esperado: sequência numérica.")
            
        elif field == '0' * len(field):
            errors.append(f"[{context}] Posição {position}: campo preenchido apenas com zeros. "
                        f"Valor esperado: {fieldName}.")
            
    @staticmethod        
    def validate_numeric_no_zeros_and_register(field: str, context: str, position: str, errors: list[str], fieldName: str, number_lines: int) -> None:
        
        if field.strip() == "":
            errors.append(f"[{context}] Posição {position}: campo vazio. "
                        "Valor esperado: sequência numérica.")
            
        elif not field.isdigit():
            errors.append(f"[{context}] Posição {position}: não é um número."
                        "Valor esperado: sequência numérica.")
            
        elif field == '0' * len(field):
            errors.append(f"[{context}] Posição {position}: campo preenchido apenas com zeros. "
                        f"Valor esperado: {fieldName}.")   
                     
        else:
            sequence = int(field)
            if sequence != number_lines:
                errors.append(f"[{context}] Posição {position}: sequência errada. Valor esperado: {number_lines}")