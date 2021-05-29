from django.urls import path
from   .views import EsewaPay,MyView,EsewaVerify
urlpatterns = [
    path('',MyView.as_view(),name='home'),
    # path('<int:id>',detail,name='detail'),
    path('esewapay/<int:id>', EsewaPay.as_view(),name='esewapay'),
    path('esewa-verify', EsewaVerify.as_view(),name='esewa-verify'),
    # path()
]
