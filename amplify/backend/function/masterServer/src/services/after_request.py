from flask import Response


class Handler:
    def __init__(self, response: Response):
        self.response = response

    def handle_after_request(self) -> Response:
        """Handle after request processing."""
        # Add CORS headers
        self.response.headers.add('Access-Control-Allow-Origin', '*')
        self.response.headers.add(
            'Access-Control-Allow-Headers', 'Content-Type,Authorization')
        self.response.headers.add(
            'Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')

        # Add security headers
        self.response.headers.add('X-Content-Type-Options', 'nosniff')
        self.response.headers.add('X-Frame-Options', 'DENY')
        self.response.headers.add('X-XSS-Protection', '1; mode=block')

        return self.response
