from django.urls import path
from .import views

app_name='superAdmin'
urlpatterns = [
    path('user_details', views.user_details, name ='user_details'),

    path('create_user', views.create_user, name ='create_user'),
    path('loadUserCell', views.loadUserCell, name ='loadUserCell'),
    path('updateuser', views.updateuser, name ='updateuser'),
    path('save_user_and_return', views.save_user_and_return, name ='save_user_and_return'),
    path('role_index', views.role_index, name ='role_index'),
    path('users', views.users, name ='users'),
    path('active_users', views.active_users, name ='active_users'),
    path('load_permission', views.load_permission, name ='load_permission'),
    path('view_permission', views.view_permission, name ='view_permission'),
    path('delete_permission', views.delete_permission, name ='delete_permission'),
    path('permit', views.permit, name ='permit'),
    path('delete', views.Delete, name ='delete'),
    path('user_edit_view', views.user_edit_view, name ='user_edit_view'),
    path('create_role', views.create_role, name ='create_role'),
    path('save_role', views.save_role, name ='save_role'),
    path('role_edit', views.role_edit, name ='role_edit'),
    path('update_role', views.update_role, name ='update_role'),
    path('delete_role', views.delete_role, name ='delete_role'),
    path('delete_group', views.delete_group, name ='delete_group'),
    path('update_profile', views.update_profile, name ='update_profile'),
    path('update_profile/<str:file_id>/', views.update_profile, name='update_profile'),


 # region
    path('region_index', views.region_index, name ='region_index'),
    path('create_region', views.create_region, name ='create_region'),
    path('save_region', views.save_region, name ='save_region'),
    path('region_edit', views.region_edit, name ='region_edit'),
    path('update_region', views.update_region, name ='update_region'),
    path('delete_region', views.delete_region, name ='delete_region'),


 # Zone
    path('zone_index', views.zone_index, name ='zone_index'),
    path('create_zone', views.create_zone, name ='create_zone'),
    path('save_zone', views.save_zone, name ='save_zone'),
    path('zone_edit', views.zone_edit, name ='zone_edit'),
    path('update_zone', views.update_zone, name ='update_zone'),
    path('delete_zone', views.delete_zone, name ='delete_zone'),

 # nation
    path('nation_index', views.nation_index, name ='nation_index'),
    path('create_nation', views.create_nation, name ='create_nation'),
    path('save_nation', views.save_nation, name ='save_nation'),
    path('nation_edit', views.nation_edit, name ='nation_edit'),
    path('update_nation', views.update_nation, name ='update_nation'),
    path('delete_nation', views.delete_nation, name ='delete_nation'),


 # Kebele
    path('kebele_index', views.kebele_index, name ='kebele_index'),
    path('create_kebele', views.create_kebele, name ='create_kebele'),
    path('save_kebele', views.save_kebele, name ='save_kebele'),
    path('kebele_edit', views.kebele_edit, name ='kebele_edit'),
    path('update_kebele', views.update_kebele, name ='update_kebele'),
    path('delete_kebele', views.delete_kebele, name ='delete_kebele'),

 # Woreda
    path('woreda_index', views.woreda_index, name ='woreda_index'),
    path('create_woreda', views.create_woreda, name ='create_woreda'),
    path('save_woreda', views.save_woreda, name ='save_woreda'),
    path('woreda_edit', views.woreda_edit, name ='woreda_edit'),
    path('update_woreda', views.update_woreda, name ='update_woreda'),
    path('delete_woreda', views.delete_woreda, name ='delete_woreda'),


   #  Notification 
    path('email_index', views.email_index, name ='email_index'),
    path('create_email', views.create_email, name ='create_email'),
    path('save_email', views.save_email, name ='save_email'),
    path('email_edit', views.email_edit, name ='email_edit'),
    path('update_email', views.update_email, name ='update_email'),
    path('delete_email', views.delete_email, name ='delete_email'),

   #  System Notification 
   path('not_user', views.not_user, name ='not_user'),
   path('create_not_user', views.create_not_user, name ='create_not_user'),
   path('save_not_user', views.save_not_user, name ='save_not_user'),
   path('delete_not_user', views.delete_not_user, name ='delete_not_user'),

    path('id_card/<int:id_card_id>/', views.generate_id_card, name='generate_id_card'),
   #  path('report', views.report, name ='report'),
    path('notif_test', views.notif_test, name ='notif_test'),
    path('profile/<int:id>/edit/', views.update_ownProfile, name='update_profile'),

]