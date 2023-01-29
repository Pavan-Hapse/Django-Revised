from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('abc/', include('todolist_app.urls')),
    path('account/', include('user_app.urls'))

]
