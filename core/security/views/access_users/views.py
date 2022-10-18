from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import FormView, DeleteView

from core.pos.mixins import ValidatePermissionRequiredMixin
from core.reports.forms import ReportForm
from core.security.models import AccessUsers


class AccessUsersListView(ValidatePermissionRequiredMixin, FormView):
    form_class = ReportForm
    template_name = 'access_users/list.html'
    permission_required = 'view_access_users'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search':
                data = []
                start_date = request.POST['start_date']
                end_date = request.POST['end_date']
                queryset = AccessUsers.objects.all()
                if len(start_date) and len(end_date):
                    queryset = queryset.filter(date_joined__range=[start_date, end_date])
                for i in queryset:
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Accesos de Usuarios'
        context['list_url'] = reverse_lazy('access_users_list')
        context['entity'] = 'Accesos de Usuarios'
        return context


class AccessUsersDeleteView(ValidatePermissionRequiredMixin, DeleteView):
    model = AccessUsers
    template_name = 'access_users/delete.html'
    success_url = reverse_lazy('access_users_list')
    url_redirect = success_url
    permission_required = 'delete_access_users'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una Accesos de Usuarios'
        context['entity'] = 'Accesos de Usuarios'
        context['list_url'] = self.success_url
        return context
