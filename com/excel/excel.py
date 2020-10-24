import xlsxwriter
import abc


class Excel(metaclass=abc.ABCMeta):
    def __init__(self, url_file):
        self._workbook = xlsxwriter.Workbook(url_file)

    @abc.abstractmethod
    def _write_header(self):
        raise NotImplementedError("Excel", "write_header", None, "The user has not implemented this method")

    @abc.abstractmethod
    def write_row(self, params):
        raise NotImplementedError("Excel", "write_now", None, "The user has not implemented this method")

    def __del__(self):
        self._workbook.close()
        del self._workbook
