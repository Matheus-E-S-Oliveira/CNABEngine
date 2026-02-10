def validate_structure(lines: list[str], errors: list[str]) -> None:
    context = "ESTRUCTURE"

    if len(lines) < 3:
        errors.append(
            f"[{context}] Arquivo inválido: é necessário conter ao menos 3 linhas "
            "(HEADER, BODY e TRAILER)."
        )
        return

    if not lines[0] or lines[0][0] != "0":
        errors.append(
            f"[{context}] HEADER inválido: o arquivo deve iniciar com o registro '0'."
        )

    if not lines[-1] or lines[-1][0] != "9":
        errors.append(
            f"[{context}] TRAILER inválido: o arquivo deve finalizar com o registro '9'."
        )

    for index, line in enumerate(lines[1:-1], start=2):
        if not line or line[0] != "7":
            errors.append(
                f"[{context}] Linha {index}: registro inválido. "
                "Esperado registro do tipo '7'."
            )