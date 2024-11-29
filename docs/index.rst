Welcome to FakeInvoiceGen's documentation!
===============================================

FakeInvoiceGen is a Python package that combines the power of Faker and
InvoiceGenerator libraries to create realistic fake invoices for testing and
development purposes.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage

Installation
-----------

You can install the package using pip:

.. code-block:: bash

   pip install fakeinvoicegen

Quick Start
----------

Here's a simple example to get you started:

.. code-block:: python

   from fakeinvoicegen import InvoiceGenerator

   # Initialize the generator
   generator = InvoiceGenerator()

   # Generate 5 random invoices
   generator.generate_invoices(count=5)

For more detailed information, check out the :doc:`usage` section.