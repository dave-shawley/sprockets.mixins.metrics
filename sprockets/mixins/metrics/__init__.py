try:
    from .influxdb import InfluxDBMixin
    from .statsd import StatsdMixin
except ImportError as error:
    def InfluxDBMixin(*args, **kwargs):
        raise error

    def StatsdMixin(*args, **kwargs):
        raise error

version_info = (1, 0, 0)
__version__ = '.'.join(str(v) for v in version_info)
__all__ = ['InfluxDBMixin', 'StatsdMixin']
