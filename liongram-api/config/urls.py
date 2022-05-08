from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import routers
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from posts.views import PostListCreateView, PostRetrieveUpdateView, PostModelViewSet, calculator, CalculatorAPIView
from accounts.views import login_view, LoginView

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('posts', PostModelViewSet)

urlpatterns = [
    re_path('^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path('^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path('^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('', include(router.urls)),
    path('admin/', admin.site.urls),

    # path('login/', login_view),
    path('login/', LoginView.as_view()),

    # path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    # path('posts/<int:pk>/', PostRetrieveUpdateView.as_view(), name='post-detail'),

    # path('calculator/', calculator, name='calculator-fbv'),
    path('calculator/', CalculatorAPIView.as_view(), name='calculator-cbv'),
]
