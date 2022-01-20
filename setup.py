import sys

from flask_script   import Manager
from flask_twisted  import Twisted
from twisted.python import log
from .app import create_app

### python -m 으로 실행해도 __name__ 은 여전히 __main__ 임
if __name__ == "__main__":
    app = create_app()

    twisted = Twisted(app)
    log.startLogging(sys.stdout)

    app.logger.info(f"Running the app...")

    manager = Manager(app)
    manager.run()