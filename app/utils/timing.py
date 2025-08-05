from contextlib import contextmanager
import time, structlog
log = structlog.get_logger()
@contextmanager
def timed(name: str):
    start = time.perf_counter(); yield
    log.info('timed', name=name, ms=round((time.perf_counter()-start)*1_000,1))
