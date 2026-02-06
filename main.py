import sys
from cnabengine.core.validators import validate_file
from cnabengine.utils.enums import FileType
from cnabengine.layouts.cnab400 import CNAB400Shipment

def main():
    if len(sys.argv) < 2:
        print("Informe o caminho do arquivo.")
        print("Exemplo: python main.py arquivo.txt")
        return

    caminho_arquivo = sys.argv[1]

    try:
        lines, extension = validate_file(caminho_arquivo)
        
        if(extension.lower() == FileType.REM.value):
            file = CNAB400Shipment(lines)
            file.check_layout()
            
        elif(extension.lower() == FileType.RET.value):
            print("É um arquivo de retorno")
        
        print("✅ Arquivo validado com sucesso.")
        print(f"📄 Total de linhas: {len(lines)}")
        
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