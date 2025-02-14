#sudo apt install python3-venv
#python3 -m venv .venv #create a new virtual environment in a directory 
#source .venv/bin/activate 
#pip install pygelf
#deactivate

import uuid
from pygelf import GelfTcpHandler
import logging

# Создадим класс с методом filter, который будет подставлять reuqest_id в каждую запись
class ContextFilter(logging.Filter):
    def filter(self, record):
        record.request_id = str(uuid.uuid4())
        return True

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api")

# Все, что нужно для отправки логов - добавить обработчик в логгер
logger.addHandler(GelfTcpHandler(host='127.0.0.1', port=12201, include_extra_fields=True))
logger.addFilter(ContextFilter())

logger.info('hello gelf')

