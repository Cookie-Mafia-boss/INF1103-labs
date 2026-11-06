# supplier.py

class Supplier:
    def __init__(self, supplier_id: str, supplier_name: str, contact_email: str):
        self.supplier_id: str = supplier_id
        self.supplier_name: str = supplier_name
        self.contact_email: str = contact_email 

    def display_information(self) -> None:
        print(f"  Supplier: {self.supplier_name} (ID: {self.supplier_id}, Contact: {self.contact_email})")