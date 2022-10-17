"""
.. _traded_as:

Institution Traded As
~~~~~~~~~~~~~~~~~~~~~

Fetch this open data all banks trading initials.

.. _country_initials:

Country Initials
~~~~~~~~~~~~~~~~

Fetch this open data all countries initials.

.. _city_initials:

City Initials
~~~~~~~~~~~~~

Fetch this open data all cities initials.

.. _conversion_rates:

Conversion Rates
~~~~~~~~~~~~~~~~

Fetch this open data with conversion rates between EUR, DKK and USD. This data is used in the :ref:`transaction amount <transaction_amount>` dataset.

.. _transaction_amount:

Transaction Amount
~~~~~~~~~~~~~~~~~~

The dataset represents the amount for each transaction and what the transaction was about. Dataset fields:

* ``country``: Country of the transaction. Finite list of country initials. See: :ref:`country initials <country_initials>`.
* ``city``: City of the transaction. Finite list of cities initials. See: :ref:`city initials <city_initials>`.
* ``year``: Year of the transaction
* ``month``: Month of the transaction
* ``day``: Day of the transaction
* ``time``: Time of the transaction, hours:minutes:seconds
* ``dkk``: Amount of the transaction in DKK. If the transaction was in another currency, it is converted to DKK according with the conversion value in place  according to the date of the transaction.
* ``eur``: Amount of the transaction in EUR. If the transaction was in another currency, it is converted to EUR according with the conversion value in place  according to the date of the transaction.
* ``usd``: Amount of the transaction in USD. If the transaction was in another currency, it is converted to USD according with the conversion value in place  according to the date of the transaction.
* ``traded``: Institution holding the transaction. Finite list of banks initials. See: :ref:`Institution Traded As <traded_as>`.

The calculation of ``dkk``, ``eur`` and ``usd`` is attained through the :ref:`conversion rates <conversion_rates>` dataset. The data arrives in parquet files depending on the ``institution``, meaning all files must be concatenated in a single file, persisting the information of the ``institution`` holding the transaction on the dedicated field.
"""

import pandas as pd

bnp = {
    'country': [None],
    'city': [None],
    'year': [2018],
    'month': [1],
    'day': [1],
    'time': ['00:00:00'],
    'dkk': [None],
    'eur': [550],
    'usd': [None]
}

danske = {
    'country': [None],
    'city': [None],
    'year': [2022],
    'month': [1],
    'day': [1],
    'time': ['00:00:00'],
    'dkk': [5000],
    'eur': [None],
    'usd': [None]
}

df_bnp = pd.DataFrame(bnp)
df_danske = pd.DataFrame(danske)

df_bnp.to_parquet('bnp.parquet', index=False)
df_danske.to_parquet('danske.parquet', index=False)
