def validate_sequence(lines: list[str], errors: list[str]) -> None:
    context = "SEQUENCE"
    expected = 1

    for i, line in enumerate(lines, start=1):
        if not line:
            errors.append(
                f"[{context}] Linha {i}: linha vazia."
            )
            continue

        if len(line) != 400:
            errors.append(
                f"[{context}] Linha {i}: tamanho inválido. Esperado: 400 caracteres."
            )
            continue

        raw_sequence = line[394:400]

        if not raw_sequence.isdigit():
            errors.append(
                f"[{context}] Linha {i}: número sequencial inválido "
                f"(posição 395–400). Valor encontrado: '{raw_sequence}'."
            )
            continue

        sequence = int(raw_sequence)

        if sequence != expected:
            errors.append(
                f"[{context}] Linha {i}: sequência incorreta. "
                f"Sequência esperada: {expected}. Sequência encontrada: {sequence}."
            )

        expected += 1
    return
