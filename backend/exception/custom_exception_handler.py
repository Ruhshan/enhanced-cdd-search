from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from backend.exception.custom_exceptions import CallToNCBIFailed


def handle_call_to_NCBIFailed_exception(request: Request, exc: CallToNCBIFailed)->JSONResponse:
    return JSONResponse(
        status_code=418,
        content={"message": "Unable to communicate with NCBI, received status code "+exc.message},
    )


def inclue_custom_exception_handler(app:FastAPI):
    app.add_exception_handler(CallToNCBIFailed,handle_call_to_NCBIFailed_exception)

