import sys

from loguru import logger
from typing import Iterable, Union

from core import Tuple
from core.data_processor import DataProcessor
from core.models.tuple import InputExhausted
from core.udf import UDFOperator
from edu.uci.ics.amber.engine.common import LinkIdentity


class EchoOperator(UDFOperator):
    def process_texera_tuple(self, row: Union[Tuple, InputExhausted], link: LinkIdentity) -> Iterable[Tuple]:
        yield row


if __name__ == '__main__':
    data_processor = DataProcessor(host="localhost", input_port=int(sys.argv[1]), output_port=int(sys.argv[2]),
                                   udf_operator=EchoOperator())

    data_processor.start()

    data_processor.join()

    logger.info("main finished")
