import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path, re_path
from django.views.static import serve
from whitenoise import WhiteNoise

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("store.urls", namespace="store")),
    path("checkout/", include("checkout.urls", namespace="checkout")),
    path("basket/", include("basket.urls", namespace="basket")),
    path("account/", include("account.urls", namespace="account")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("__debug__/", include(debug_toolbar.urls)),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

if not settings.DEBUG:
    # Serve static files via Whitenoise
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', WhiteNoise(settings.STATICFILES_DIRS), name='static'),
    ]