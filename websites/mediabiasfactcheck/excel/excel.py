from com.excel.excel import Excel


class MediaBiasFatchcheckEXCEL(Excel):
    def __init__(self, url_file):
        super().__init__(url_file)
        self.__worksheet = self._workbook.add_worksheet("Sheet1")
        self._write_header()

    def _write_header(self):
        self.__worksheet.write(0, 0, "MEDIA COMPANY NAME")
        self.__worksheet.write(0, 1, "TYPE")
        self.__worksheet.write(0, 2, "BIAS")

    def write_row(self, params):
        '''
        :param params: We are going to receive a dictionary with keys: row, media, type, bias
        :return: Write on excel a row
        '''
        #print(f"row: {params['row']} media: {params['media']} type: {params['type']} bias: {params['bias']}")
        self.__worksheet.write(params["row"], 0, params["media"])
        self.__worksheet.write(params["row"], 1, params["type"])
        self.__worksheet.write(params["row"], 2, str(params["bias"]).upper())
