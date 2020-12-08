
from django.contrib import admin
from django.urls import path,include
import products.views  
import accounts.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
   
    # path('accounts/',accounts.views.signup,name='homeacc'),
    path('accounts/',include('accounts.urls')),
    path('products/',include('products.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
