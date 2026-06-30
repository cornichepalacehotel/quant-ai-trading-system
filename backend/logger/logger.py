import logging

logging.basicConfig(

    filename="quant.log",

    level=logging.INFO,

    format="%(asctime)s %(levelname)s %(message)s"

)

logger = logging.getLogger("QuantAI")
