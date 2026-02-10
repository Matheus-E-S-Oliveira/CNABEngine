from cnabengine.utils.enums import FileType, ModelCNAB
from cnabengine.core.validators.cnab400.cnab400_shipment import (
    validate_header,
    validate_body,
    validate_trailer,
    validate_structure,
    validate_sequence
)

class CNAB400Shipment:
    def __init__(self, lines: list[str]):
        self.lines = lines
        self.model = ModelCNAB.CNAB400.value
        self.tipo = FileType.REM.value
        
        self.header: str | None = None
        self.details: list[str] = []
        self.trailer: str | None = None
        
        self.errors: list[str] = []

    def validate(self):
        validate_structure(self.lines, self.errors)
        
        if self.errors:
            return self.errors
        
        validate_sequence(self.lines, self.errors)
        
        if self.errors:
            return self.errors
        
        self.__split_blocks()
        
        self.__validate_header()
        self.__validate_details()
        self.__validate_trailer()

    def __validate_header(self) -> None:
        validate_header(self.header, self.errors)

    def __validate_details(self) -> None:
        validate_body(self.details, self.errors)

    def __validate_trailer(self) -> None:
        number_lines = len(self.lines)
        validate_trailer(self.trailer, self.errors, number_lines)
        
    def __check_errors(self) -> list[str]:
        if self.errors:
            return self.errors
        
    def __split_blocks(self) -> None:
        if len(self.lines) < 3:
            return
        
        self.header = self.lines[0]
        self.details = self.lines[1:-1]
        self.trailer = self.lines[-1]
