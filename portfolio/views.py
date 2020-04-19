from django.views.generic import TemplateView

# ポートフォリオトップページ
class HomeView(TemplateView):
  template_name = 'portfolio/home.html'

home = HomeView.as_view()