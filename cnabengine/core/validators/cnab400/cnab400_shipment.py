def validate_header(header: str) -> None:
    if len(header) != 400:
        raise ValueError("O cabeçalho do CNAB 400 deve ter 400 caracteres!")
    
    if header[0] != "0":
        raise ValueError("")
    

def validate_body(body: list[str]) -> None:
    pass

def validate_trailer(trailer: list[str]) -> None:
    pass