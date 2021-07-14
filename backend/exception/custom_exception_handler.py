from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from backend.exception.custom_exceptions import CallToNCBIFailed, DhandleNotFound


def handle_call_to_NCBIFailed_exception(request: Request, exc: CallToNCBIFailed) -> JSONResponse:
    return JSONResponse(
        status_code=418,
        content={"message": "Unable to communicate with NCBI, received status code " + exc.message},
    )


def handle_dhandle_not_found_exception(request: Request, exc: DhandleNotFound) -> JSONResponse:
    return JSONResponse(
        status_code=419,
        content={"message": "Unable to parse data handle from ncbi response " + exc.message},
    )


def inclue_custom_exception_handler(app: FastAPI):
    app.add_exception_handler(CallToNCBIFailed, handle_call_to_NCBIFailed_exception)
    app.add_exception_handler(DhandleNotFound, handle_dhandle_not_found_exception)
