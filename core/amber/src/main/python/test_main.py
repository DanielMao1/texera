import time
from loguru import logger
from pandas import DataFrame
from pyarrow import Table
from typing import Iterable

from core import Tuple
from core.data_processor import DataProcessor
from core.udf.udf_operator import UDFOperator
from proxy import ProxyClient, ProxyServer

if __name__ == '__main__':
    class EchoOperator(UDFOperator):
        def process_texera_tuple(self, row: Tuple, nth_child: int = 0) -> Iterable[Tuple]:
            logger.debug("processing one row")
            return [row]


    server = ProxyServer(port=5006)
    server.register_data_handler(lambda x: print(x.to_pandas()))
    with server:
        data_processor = DataProcessor(host="localhost", input_port=5005, output_port=5006, udf_operator=EchoOperator())

        data_processor.start()

        df_to_sent = DataFrame({
            'Brand': ['Honda Civic', 'Toyota Corolla', 'Ford Focus', 'Audi A4'],
            'Price': [22000, 25000, 27000, 35000]
        }, columns=['Brand', 'Price'])
        table = Table.from_pandas(df_to_sent)

        client = ProxyClient(port=5005)
        # send the pyarrow table to server as a flight
        client.send_data(table)
        time.sleep(2)

        data_processor.stop()
