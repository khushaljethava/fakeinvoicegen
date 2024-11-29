from fakeinvoicegen import InvoiceGenerator

def test_basic_invoice():
    """Test generating a basic invoice"""
    generator = InvoiceGenerator()
    path = generator.generate_invoice("basic_invoice.pdf")
    print(f"Generated invoice at: {path}")

def test_custom_invoice():
    """Test generating an invoice with custom data"""
    generator = InvoiceGenerator()
    
    custom_data = {
        'client_name': 'ACME Corp',
        'provider_name': 'My Company Ltd',
        'creator_name': 'John Smith',
        'bank_account': '1234567890',
        'bank_code': 'ABCDEF',
        'items': [
            {'qty': 10, 'price': 100, 'description': "Consulting", 'tax': 20},
            {'qty': 5, 'price': 200, 'description': "Development", 'tax': 20}
        ]
    }
    
    path = generator.generate_invoice(
        output_path="custom_invoice.pdf",
        custom_data=custom_data
    )
    print(f"Generated custom invoice at: {path}")

def test_multiple_invoices():
    """Test generating multiple invoices"""
    generator = InvoiceGenerator()
    paths = generator.generate_invoices(count=3, output_dir="multiple_invoices")
    print("Generated multiple invoices at:")
    for path in paths:
        print(f"- {path}")

if __name__ == "__main__":
    print("Testing basic invoice generation...")
    test_basic_invoice()
    
    print("\nTesting custom invoice generation...")
    test_custom_invoice()
    
    print("\nTesting multiple invoice generation...")
    test_multiple_invoices()