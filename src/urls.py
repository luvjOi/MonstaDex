from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
import src.views as src_views
from django.contrib.auth import views as auth_views


from attacks.models import Attack
from bindings.models import Binding
from monster.models import Monsta
from players.models import Player
from src.views import HomePageView


admin.site.register(Monsta)
admin.site.register(Player)
admin.site.register(Binding)
admin.site.register(Attack)

urlpatterns = [
    # DRF API
    path('', include('api.urls')),

    # Django built in
    path('admin/', admin.site.urls),

    # Wagtail Site URLS
    path('', HomePageView.as_view(), name='home'),

    # Our App URLS
    path('', include('players.urls')),
    path('', include('bindings.urls')),
    path('', include('monster.urls')),
    path('', include('attacks.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home_page.html'), name='home'),
    path('signup/', src_views.signup, name='signup'),
    path('profile/', TemplateView.as_view(template_name='players/player_detail.html'), name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

]

if settings.DEBUG:
    # Static files for local dev, so we don't have to collectstatic and such
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)

    # Django debug toolbar
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
