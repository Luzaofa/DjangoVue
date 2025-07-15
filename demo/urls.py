from django.urls import path
from .views import GetActDataView

urlpatterns = [
    path(r'datas/', GetActDataView.as_view(), name='datas'),  # 测试数据
]
