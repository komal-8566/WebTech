from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('signup/',views.signup_view,name='signup'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('<str:name>/listmenu',views.listmenu,name='listmenu'),
    path('contact',views.contact,name='contact'),
    path('home',views.home,name='home'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('checkout',views.checkout,name='checkout'),
    path('placeorder',views.placeorder,name='placeorder'),
    path('faq',views.faq,name='faq'),
    path('see_order_status',views.see_order_status,name='see_order_status'),
    path('curr_orders',views.curr_orders,name='curr_orders'),
    path('mark_order',views.mark_order,name='mark_order'),
    path('delete_item',views.delete_item,name='delete_item'),
    path('reviews', views.review, name='reviews'),
    path('DeleteReview', views.delReview, name='delReview'),
    path('AddReview', views.addReview, name='addReview')
]
