from django.urls import path
from . import views
from django.urls import path


urlpatterns = [
 path('', views.Home.as_view(), name='home'),

 path('about/', views.about, name='about'),

 path('profile/', views.profile, name='profile'),

 path('milestoneCreate/', views.MilestoneCreate.as_view(), name='milestone-create'), 

 path('tips-catgory/', views.tips, name='tips-catgory'),

 path('tips-catgory/<int:Tips_catgory_id>', views.tips_detail, name='tips-catgory_details'),

 path('tips-catgory/<int:Tips_catgory_id>/add_tip/', views.add_tip, name='add_tip'),

 path('tips/<int:pk>/update/', views.TipUpdate.as_view(), name='tips_update'),

 path('tips/<int:pk>/delete/', views.TipDelete.as_view(), name='tips_delete'),

 path('accounts/signup/', views.signup, name='signup'),

 path('profile/milestoneCreate/<int:milestone_id>/', views.milestone_detail, name='milestone_detail'),

 path('profile/milestoneCreate/<int:milestone_id>/add_photo', views.add_photo, name='add_photo'),
]