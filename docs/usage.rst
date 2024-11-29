Usage
=====

Basic Usage
----------

Generate Random Invoices
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from fakeinvoicegen import InvoiceGenerator

   # Initialize the generator
   generator = InvoiceGenerator()

   # Generate a single random invoice
   generator.generate_invoice()

   # Generate multiple random invoices
   generator.generate_invoices(count=5)

Custom Invoice Data
~~~~~~~~~~~~~~~~

You can customize any aspect of the generated invoices:

.. code-block:: python

   custom_data = {
       'client_name': 'John Doe',
       'amount': 1000.00,
       'currency': 'EUR',
       'due_date': '2024-12-31'
   }

   generator.generate_invoice(custom_data=custom_data)

API Reference
-----------

InvoiceGenerator
~~~~~~~~~~~~~~

.. autoclass:: fakeinvoicegen.InvoiceGenerator
   :members:
   :undoc-members:
   :show-inheritance: