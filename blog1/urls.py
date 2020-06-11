from django.urls import path
from blog1 import views
app_name = 'blog1'
urlpatterns = [
            path('',views.landing,name= 'landing'),
            path('loggedin/',views.next1,name= 'after'),
            path('signup/',views.registration,name='signup'),
            path('congo/',views.congo,name='congo'),
            path('login/',views.userlogin,name='login'),
            path('blogs/',views.postmaker,name='blogs'),
            path('logout/',views.userlogout,name='logout'),
            path('newpost/',views.newposter,name='poster'),
            path('drafts/<int:pk>/',views.draftsuser,name='drafts'),
            path('save/',views.publish,name='publish')


]
