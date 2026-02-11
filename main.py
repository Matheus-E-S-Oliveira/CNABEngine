import sys
from cnabengine.core.validators import validate_file
from cnabengine.utils.enums import FileType
from cnabengine.layouts.cnab400.cnab400_shipment import CNAB400Shipment
from cnabengine.utils import log_utils

def main():
    if len(sys.argv) < 2:
        print("Informe o caminho do arquivo.")
        print("Exemplo: python main.py arquivo.txt")
        return

    file_path = sys.argv[1]

    try:
        lines, extension = validate_file(file_path)
        print("\n")
        print("✔ Arquivo carregado com sucesso.")
        print(f"ℹ Total de linhas: {len(lines)}")

        if extension.lower() == FileType.REM.value:
            file = CNAB400Shipment(lines)
            errors = file.validate()

        elif extension.lower() == FileType.RET.value:
            print("ℹ Arquivo de retorno (RET) identificado.")
            errors = []

        if errors:
            print("-" * 50 + "\n")
            print("✖ Validação concluída: o arquivo contém erros.")
            print(f"ℹ Total de erros encontrados: {len(errors)}")
                        
            # Exibir log no terminal
            # log_utils.show_log_terminal(errors=errors, original_file=file_path)
            
            log_utils.save_log_txt(errors=errors, original_file=file_path)
        else:
            print("✔ Validação concluída: arquivo válido.")
        
    except FileNotFoundError as e:
        print(f"❌ {e}")
    except ValueError as e:
        print(f"❌ {e}")
    except OSError as e:
        print(f"❌ {e}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
    
if __name__ == "__main__":
    main()  
