from cnabengine.utils.enums import FileType, ModelCNAB
from cnabengine.core.validators.cnab400.cnab400_shipment import validate_header, validate_body, validate_trailer
    
class CNAB400Shipment:
    def __init__(self, lines: list[str]):
        self.lines = lines
        self.model = ModelCNAB.CNAB400.value           
        self.tipo = FileType.REM.value
        self.header = lines[0]
        self.details = lines[1:-1]
        self.trailer = lines[-1]
        
    def check_layout(self):
        try: 
            self.validate_header()
            self.validate_details()
            self.validate_trailer()
        except ValueError as e:
            print(f"❌ {e}")

    def validate_header(self):
        validate_header(self.header)

    def validate_details(self):
        validate_body(self.details)

    def validate_trailer(self):
        validate_trailer(self.trailer)

