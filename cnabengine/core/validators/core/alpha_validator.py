class AlphaValidator:
    
    @staticmethod
    def validate_alpha(field: str, context: str, position: str, errors: list[str], fieldName: str) -> None:
        if field.strip() == "":
            errors.append(f"[{context}] Posição {position}: campo vazio. Valor esperado: {fieldName}")