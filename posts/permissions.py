from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        #only Authenticated users can view list
        if request.user.is_authenticated:
            return True
        return False
    def has_object_permission(self, request, view, obj):
        #write permissions allowed for superuser or post author
        #read permissions allowed for allowed user user
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
