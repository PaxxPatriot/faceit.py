"""
MIT License

Copyright (c) 2025-present PaxxPatriot

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__all__ = (
    "FaceitException",
    "HTTPException",
    "BadRequest",
    "Unauthorized",
    "Forbidden",
    "NotFound",
    "ServiceUnavailable",
)


class FaceitException(Exception):
    """Base exception class for faceit.py

    Ideally speaking, this could be caught to handle any exceptions raised from this library.
    """

    pass


class HTTPException(FaceitException):
    """Exception that's raised when an HTTP request operation fails.
    Attributes
    ------------
    response: :class:`aiohttp.ClientResponse`
        The response of the failed HTTP request. This is an
        instance of :class:`aiohttp.ClientResponse`. In some cases
        this could also be a :class:`requests.Response`.
    text: :class:`str`
        The text of the error. Could be an empty string.
    status: :class:`int`
        The status code of the HTTP request.
    """

    def __init__(self, response, message):
        self.response = response
        self.status = response.status
        if isinstance(message, dict):
            base = message.get("message", "")
            errors = message.get("errors")
            if errors:
                errors = {error["code"]: error["message"] for error in errors}
                helpful = "\n".join("In %s: %s" % t for t in errors.items())
                self.text = base + "\n" + helpful
            else:
                self.text = base
        else:
            self.text = message or ""

        fmt = "{0.status} {0.reason})"
        if len(self.text):
            fmt += ": {1}"

        super().__init__(fmt.format(self.response, self.text))


class BadRequest(HTTPException):
    """Exception that's raised for when status code 400 occurs.

    Subclass of :exc:`HTTPException`"""

    pass


class Unauthorized(HTTPException):
    """Exception that's raised for when status code 401 occurs.

    Subclass of :exc:`HTTPException`"""

    pass


class Forbidden(HTTPException):
    """Exception that's raised for when status code 403 occurs.

    Subclass of :exc:`HTTPException`"""

    pass


class NotFound(HTTPException):
    """Exception that's raised for when status code 404 occurs.

    Subclass of :exc:`HTTPException`"""

    pass


class ServiceUnavailable(HTTPException):
    """Exception that's raised for when status code 503 occurs.

    Subclass of :exc:`HTTPException`"""

    pass
