import sys


def error_message_detail(error_message: str, error_detail: sys):
    filename = error_detail.exc_info()[2].tb_frame.f_code.co_filename
    lineno = error_detail.exc_info()[2].tb_lineno

    custom_message = f"ERROR OCCURED IN FILE: [{filename}] AT LINE: [{lineno}] AND ERROR IS: [{error_message}]"

    return custom_message


class CustomException(Exception):
    def __init__(self, error_message: str, error_detail: sys) -> None:
        super().__init__(error_message)
        self.error_message: str = error_message_detail(error_message=error_message, error_detail=error_detail)

    def __str__(self) -> str:
        return self.error_message