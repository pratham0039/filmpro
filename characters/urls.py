# # characters/urls.py
# from django.urls import path
# from .views import CharacterListView, SceneListView, CharacterDetailView, SceneUpdateView

# urlpatterns = [
#     path('characters/', CharacterListView.as_view(), name='character_list'),
#     path('characters/<int:pk>/', SceneListView.as_view(), name='scenes_for_character'),
#     path('scenes/<int:pk>/', CharacterDetailView.as_view(), name='character_detail'),
#     path('scenes/edit/<int:pk>/', SceneUpdateView.as_view(), name='scene_edit'),
# ]

# characters/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import CharacterListView, SceneListView, scene_list,homepage,save_story_notes,loginpage, CharacterDetailView,add_duration_remark,save_kp,save_hm,save_pro, save_pr, save_sd, save_ex, save_pv, save_prod, save_sp, save_sfx, save_vfx,save_seq, save_notes,save_costume_notes,save_description, edit_character, upload_pdf, delete_all_entries,add_duration_remark

urlpatterns = [
    path('loginpage/',loginpage, name='loginpage'),
    path('',homepage, name='homepage'),
    path('characters/', CharacterListView.as_view(), name='character_list'),
    path('scenes/', scene_list, name='scene_list'),
    path('delete_all_entries/', delete_all_entries, name='delete_all_entries'),
    path('upload/', upload_pdf, name='upload_pdf'),
    path('characters/<int:pk>/', SceneListView.as_view(), name='scenes_for_character'),
    path('scenes/<int:pk>/', CharacterDetailView, name='character_detail'),
    path('scenes/edit/<int:pk>/', edit_character, name='desc'),
    path('save_description/<int:pk>/', save_description, name='save_description'),
    path('save_costume_notes/<int:pk>/', save_costume_notes, name='save_costume_notes'),
    path('save_hm/<int:pk>/', save_hm, name='save_hm'),
    path('save_kp/<int:pk>/', save_kp, name='save_kp'),
    path('save_pro/<int:pk>/', save_pro, name='save_pro'),
    path('save_pr/<int:pk>/', save_pr, name='save_pr'),
    path('save_sd/<int:pk>/', save_sd, name='save_sd'),
    path('save_ex/<int:pk>/', save_ex, name='save_ex'),
    path('save_pv/<int:pk>/', save_pv, name='save_pv'),
    path('save_prod/<int:pk>/', save_prod, name='save_prod'),
    path('save_sp/<int:pk>/', save_sp, name='save_sp'),
    path('save_sfx/<int:pk>/', save_sfx, name='save_sfx'),
    path('save_vfx/<int:pk>/', save_vfx, name='save_vfx'),
    path('save_seq/<int:pk>/', save_seq, name='save_seq'),
    path('save_story_notes/<int:pk>/', save_story_notes, name='save_story_notes'),
    path('add_duration_remark/<int:pk>/', save_seq, name='add_duration_remark'),
    path('save_notes/<int:pk>/', save_notes, name='save_notes'),
    path('scenes/add_duration_remark/<int:pk>/', add_duration_remark, name='add_duration_remark'),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

