import logging, sys, structlog
def setup_logging(level: str = 'INFO') -> None:
    logging.basicConfig(format='%(message)s', stream=sys.stdout, level=level, force=True)
    structlog.configure(
        wrapper_class=structlog.make_filtering_bound_logger(level),
        processors=[
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt='iso'),
            structlog.processors.JSONRenderer(),
        ],
    )
