def validate_structure(lines: list[str], errors: list[str]) -> None:
    context = "ESTRUCTURE"

    if len(lines) < 3:
        errors.append(
            f"[{context}] Estrutura inválida: o arquivo deve conter "
            "HEADER, ao menos um BODY e TRAILER."
        )
        return

    if not lines[0] or lines[0][0] != "0":
        errors.append(
            f"[{context}] Estrutura inválida: a primeira linha deve ser um HEADER (registro '0')."
        )

    if not lines[-1] or lines[-1][0] != "9":
        errors.append(
            f"[{context}] Estrutura inválida: a última linha deve ser um TRAILER (registro '9')."
        )

    for index, line in enumerate(lines[1:-1], start=2):
        if not line or line[0] != "7":
            errors.append(
                f"[{context}] Linha {index}: registro inválido. "
                "Entre HEADER e TRAILER são permitidos apenas registros do tipo '7' (BODY)."
            )
