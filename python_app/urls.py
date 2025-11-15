from django.urls import path
from python_app import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.python, name="python"), 
    path('python/giriş', views.python_giriş, name='python_giriş'),
    path('python/değişkenler', views.python_değişkenler, name='python değişkenler'),
    path('python/operatörler', views.python_operatörler, name='python operatörler'),
    path('python/if-else', views.python_if, name='python_if_else'),
    path('python/döngüler', views.python_döngüler, name='python döngüler'),
    path('python/girdi-işlemleri', views.python_girdi, name='python girdi'),
    path('python/yorum-satırları', views.python_yorum, name='python yorum'),
    path('python/string', views.python_string, name='python_string'),
    path('python/listeler', views.python_listeler, name='python listeler'),
    path('python/yurples', views.python_turples, name='python turples'),
    path('python/sözlükler', views.python_sözlükler, name='python_sözlükler'),
    path('python/türeçler', views.python_türeç, name='python_türeç'),
    path('python/kwargs', views.python_args, name='python_args'),
    path('python/time', views.python_time, name='python_time'),
    path('python/fonksiyonlar', views.python_fonksiyon, name='python_fonksiyon'),
    path('python/oop', views.python_oop, name='python oop'),
    path('python/dosya-işlemleri', views.python_dosya, name='python dosya'),
    path('python/hata-yakalama', views.python_hata, name='python hata'),
    path('python/context-managers', views.python_context, name='python context'),
    path('python/metaclass', views.python_metaclass, name='python metaclass'),
    path('python/eşzamanlılık', views.python_eşzamanlılık, name='python eşzamanlılık'),
    path('python/testing', views.python_test, name='python test'),
    path('python/sanal-ortamlar', views.python_sanal, name='python sanal'),
    path('python/düzenli-ifadeler', views.python_düzen, name='python düzen'),
    path('python/web-scraping', views.python_scraping, name='python scraping'),
    path('python/apı', views.python_apı, name='python api'),
    path('python/decorators', views.python_decorators, name='python decorators'),
    path('python/jenerators', views.python_jenerator, name='python jenerators'),
    
   
] 

