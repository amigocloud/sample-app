# -*- encoding: utf-8 -*-

from amigocloud import AmigoCloud, AmigoCloudError

from django.views.generic.base import TemplateView


class IndexView(TemplateView):

    def get_template_names(self):
        if 'dataset_id' in self.request.GET:
            return ['show_map.html']
        if 'project_id' in self.request.GET:
            return ['show_datasets.html']
        if 'token' in self.request.GET:
            return ['show_projects.html']
        return ['index.html']

    def get_context_data(self, **kwargs):
        kwargs = super(IndexView, self).get_context_data(**kwargs)
        token = self.request.GET.get('token', '')
        project_id = self.request.GET.get('project_id')
        dataset_id = self.request.GET.get('dataset_id')
        if not token:
            return kwargs
        kwargs['token'] = token
        try:
            amigocloud = AmigoCloud(token=token, use_websockets=False)
            if dataset_id:
                url = '/users/0/projects/0/datasets/%s' % dataset_id
                kwargs['dataset'] = amigocloud.get(url)
            elif project_id:
                url = '/users/0/projects/%s/datasets?type=vector' % project_id
                kwargs['datasets'] = amigocloud.get(url)
            else:
                kwargs['projects'] = amigocloud.get('/me/projects')
        except AmigoCloudError as err:
            kwargs['error'] = err.message
        return kwargs
