from django.urls import  path
# views
from pages.views import (PAGEHOMEVIEW,PAGEABOUTVIEW,PAGEBLOGDETAILVIEW, PAGEBLOGVIEW,PAGECONTACTVIEW,PAGESHOPVIEW, PageCommentView
)

app_name = 'pages'

urlpatterns = [
    path('', PAGEHOMEVIEW.as_view(), name='home' ),
    path('about/', PAGEABOUTVIEW.as_view(), name='about' ),
    path('<int:pk>/blog_detail/', PAGEBLOGDETAILVIEW.as_view(), name='blog_detail' ),
    path('blog/', PAGEBLOGVIEW.as_view(), name='blog' ),
    path('contact/', PAGECONTACTVIEW.as_view(), name='contact' ),
    path('shop/', PAGESHOPVIEW.as_view(), name='shop' ),
    path('comments/<int:pk>/', PageCommentView, name='comments')
]