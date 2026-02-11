from datetime import datetime
from cnabengine.utils.file_utils import generate_log_filename

def save_log_txt(errors: list[str], original_file: str) -> None:
    log_path = generate_log_filename(original_file)

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(f"Arquivo: {original_file}\n")
        f.write(f"Data Validação: {datetime.now()}\n")
        f.write(f"Total de Erros: {len(errors)}\n")
        # f.write("-" * 50 + "\n\n")

        last_context = None

        for error in errors:
            context = error.split("]")[0] + "]"
            message = error.split("] ")[1]

            if context != last_context:
                if last_context is not None:
                    f.write("\n")

                f.write("-" * 50 + "\n\n")
                f.write(f"{context}\n")
                f.write("-" * 50 + "\n")

                last_context = context

            f.write(f"  • {message}\n")

    print(f"📄 Log detalhado salvo com sucesso em: {log_path}")
    return

def show_log_terminal(errors: list[str], original_file: str) -> None:
    log_path = generate_log_filename(original_file)
    print("\n")
    print(f"Arquivo: {original_file}")
    print(f"Data Validação: {datetime.now()}")
    print(f"Total de Erros: {len(errors)}")

    last_context = None

    for error in errors:
        context = error.split("]")[0] + "]"
        message = error.split("] ")[1]

        if context != last_context:
            print("-" * 50 + "\n")
            print(f"{context}")
            print("-" * 50 + "\n")

            last_context = context

        print(f"  • {message}\n")

    return
