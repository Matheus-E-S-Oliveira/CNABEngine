import os
from cnabengine.utils.enums import FileType

def validate_file(path: str) -> tuple[list[str], str]:
    if not path:
        raise ValueError("O caminho para o arquivo não foi informado!")
    
    if not os.path.isfile(path):
        raise FileNotFoundError("Não encontrado o arquivo no caminho informado!")
    
    _, ext = os.path.splitext(path)
    
    validate_file_type(ext)
    
    encodings = ["utf-8", "latin-1"]
    
    for encoding in encodings:
        try:
            with open(path, "r", encoding=encoding) as file:
                lines = [line.rstrip("\n") for line in file]
                
                if not lines:
                    raise ValueError("O arquivo está vazio.")
                
                return lines, ext
        except UnicodeDecodeError:
            continue
        except OSError as e:
            raise OSError(f"Erro ao abrir os arquivo: {e}")
    
    raise ValueError("Encoding do arquivo não suportado. Os encodings aceitos são UTF-8 e ANSI.")

def validate_file_type(extension: str) -> None:
    if extension.lower() not in [ft.value for ft in FileType]:
        raise ValueError(f"Extensão {extension} não suportada. O sistema suporta apenas as extensões {[ft.value for ft in FileType]}")

