from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, CSRFCheck


class SessionAuthentication(BaseAuthentication):
    """
    Use Django's session framework for authentication.
    """

    def authenticate(self, request):
        """
        Returns a `User` if the request session currently has a logged in user.
        Otherwise returns `None`.
        """
        print("Auth")
        # Get the session-based user from the underlying HttpRequest object
        user = getattr(request._request, 'user', None)
        print("USER === ",user)

        # Unauthenticated, CSRF validation not required
        if not user or not user.is_active:
            return None

        #self.enforce_csrf(request)

        # CSRF passed with authenticated user
        return (user, None)

    def enforce_csrf(self, request):
        """
        Enforce CSRF validation for session based authentication.
        """
        def dummy_get_response(request):  # pragma: no cover
            return None

        check = CSRFCheck(dummy_get_response)
        print("check ",check)
        # populates request.META['CSRF_COOKIE'], which is used in process_view()
        check.process_request(request)
        reason = check.process_view(request, None, (), {})
        print("reason ", reason)
        if reason:
            # CSRF failed, bail with explicit error message
            raise exceptions.PermissionDenied('CSRF Failed: %s' % reason)