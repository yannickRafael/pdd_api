from config import Config

app_config = Config()


def get_error_message(error_code):
    """Retrieve the  error code and message based on the error code."""
    pair = app_config.error_codes.get(error_code, {"An unknown error occured", 500})
    return pair.get("message"), pair.get("code")


def get_error_message(error_code):
    """Retrieve the error code and message based on the error code."""
    pair = app_config.error_codes.get(
        error_code,
        {"message": "An unknown error occurred", "code": 500}
    )
    return pair.get("message"), pair.get("code")
