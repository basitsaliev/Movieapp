from rest_framework.permissions import BasePermission



class CheckStatus(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.status == 'pro':
            return True
        elif request.user.status == 'simle' and obj.status_movie == 'simle':
            return True
        return False


class RatingPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'pro':
            return True
        else:
            return False