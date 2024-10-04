def success_response(data: dict) -> dict:
    return {
        "status": "success",
        "data": data,
        "errors": []
    }


def failuer_response(errors: list) -> dict:
    return {
        "status": "failure",
        "data": None,
        "errors": errors
    }