# # basic URL Configurations
# from django.urls import include, path
# # import routers
# from rest_framework import routers
#
# # import everything from views
# from .views import *
#
# # define the router
# router = routers.DefaultRouter()
#
# # define the router path and viewset to be used
# router.register(r'login', SimpleUserViewSet)
#
# # specify URL Path for rest_framework
# urlpatterns = [
# 	path('', include(router.urls)),
# 	# path('api-auth/', include('rest_framework.urls'))
# ]


from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apis import views

urlpatterns = [
	path('login/', views.SimpleUserViewSet.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
