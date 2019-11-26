from views import create_app
from config import LocalApplicationConfig

from const import _LOCAL_RUN_CONFIG, _PRODUCT_RUN_CONFIG

if __name__ == '__main__':
    app = create_app(LocalApplicationConfig)
    app.run(**_PRODUCT_RUN_CONFIG)