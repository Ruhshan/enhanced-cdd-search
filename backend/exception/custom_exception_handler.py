from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from backend.exception.custom_exceptions import CallToNCBIFailed, DhandleNotFound, InvalidBatchSearchId, \
    JobIsStillRunning, BatchSearchIdNotFound


def handle_call_to_NCBIFailed_exception(request: Request, exc: CallToNCBIFailed) -> JSONResponse:
    return JSONResponse(
        status_code=500,
        content={"message": "Unable to communicate with NCBI, received status code " + exc.message},
    )


def handle_dhandle_not_found_exception(request: Request, exc: DhandleNotFound) -> JSONResponse:
    return JSONResponse(
        status_code=500,
        content={"message": "Unable to parse data handle from ncbi response " + exc.message},
    )


def handle_job_is_still_running_exception(request: Request, exc: JobIsStillRunning) -> JSONResponse:
    return JSONResponse(
        status_code=202,
        content={"message": "Job is still running for search id: {}".format(exc.message)}
    )


def handle_invalid_batch_search_id(request: Request, exc: InvalidBatchSearchId) -> JSONResponse:
    return JSONResponse(status_code=400, content={"message": "Invalid batch search id" + exc.message})


def handle_batch_search_id_not_found(request: Request, exc: BatchSearchIdNotFound) -> JSONResponse:
    return JSONResponse(status_code=500,
                        content={"message": "Search Id not parseable"})


def include_custom_exception_handler(app: FastAPI):
    app.add_exception_handler(CallToNCBIFailed, handle_call_to_NCBIFailed_exception)
    app.add_exception_handler(DhandleNotFound, handle_dhandle_not_found_exception)
    app.add_exception_handler(InvalidBatchSearchId, handle_invalid_batch_search_id)
    app.add_exception_handler(JobIsStillRunning, handle_job_is_still_running_exception)
    app.add_exception_handler(BatchSearchIdNotFound, handle_batch_search_id_not_found)
