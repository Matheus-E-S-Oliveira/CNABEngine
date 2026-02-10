class StaticValidator:
    
    @staticmethod
    def validate_field_static_alpha(field: str, context: str, position: str, errors: list[str], value: str) -> None:
        if field.rstrip() != value:
            errors.append(f"[{context}] Posição {position}: valor inválido. "
                         f"Valor esperado: {value}.")
            
    @staticmethod
    def validate_field_static_numeric(field: str, context: str, position: str, errors: list[str], value: str) -> None:
        if field != value:
            errors.append(f"[{context}] Posição {position}: valor inválido. "
                         f"Valor esperado: {value}.")
            
    @staticmethod
    def validate_field_space(field: str, context: str, position: str, errors: list[str]) -> None:
        if field.strip() != "":
            errors.append(f"[{context}] Posição {position}: valor inválido. Valor esperado: campo preenchido apenas com espaços") 