from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    print("12131312")
    def has_object_permission(self, request, view, obj):
        print("request method ",request.method)
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user