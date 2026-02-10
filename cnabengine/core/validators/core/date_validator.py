class DateValidator:
    @staticmethod
    def validate_date_format_ddmmaa(field: str, context: str, position: str, errors: list[str]) -> None:
        if field.strip() == "":
            errors.append(f"[{context}] Posição {position}: campo vazio. Valor esperado: Data no formato DDMMAA.")
        
        elif not field.isdigit():
            errors.append(f"[{context}] Posição {position}: valor inválido. Valor Eperado: Data numérica no formato DDMMAA.")
        
        else:
            from datetime import datetime
            
            try:
                datetime.strptime(field, "%d%m%y")
            except ValueError:
                errors.append(f"[{context}] Posição {position}: data inválido. Valor Eperado: Data no formato DDMMAA.")