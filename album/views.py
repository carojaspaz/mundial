from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView, TemplateView
from album.models import Selection, Player
from .forms import PlayerCreateForm, PlayerUpdateForm

import requests


class HomeView(TemplateView):
    template_name = 'home.html'


class SelectionListView(ListView):
    model = Selection


class SelectionCreate(CreateView):
    model = Selection
    fields = '__all__'
    success_url = reverse_lazy('selection-list')    
    
    def form_valid(self, form):
        # Guardar el objeto de formulario en memoria sin persistirlo aún
        selection = form.save(commit=False)

        # Obtener las rutas de las imágenes desde los campos del formulario
        shield_path = form.cleaned_data['shield']
        team_path = form.cleaned_data['team']

        # Asignar las rutas de las imágenes al objeto de selección
        selection.shield = shield_path
        selection.team = team_path

        # Guardar el objeto de selección con las rutas de las imágenes
        selection.save()

        # Consumir la API para crear la selección
        api_url = "http://localhost:8080/selections/"  # Reemplaza con la URL correcta
        data = {
            "name": selection.name,
            "shield": shield_path,
            "team": team_path
        }
        response = requests.post(api_url, data=data)

        if response.status_code == 201:
            print("Selección creada en la API exitosamente.")
        else:
            print("Error al crear la selección en la API:", response.text)

        return super().form_valid(form)


class SelectionDetailView(DetailView):
    model = Selection


class PlayerListView(ListView):
    model = Player


class PlayerDetailView(DetailView):
    model = Player


class PlayerUpdate(UpdateView):
    model = Player
    form_class = PlayerUpdateForm
    # Asegúrate de tener la plantilla adecuada
    template_name = 'album/player_update.html'

    def get_success_url(self):
        return reverse_lazy('selection-detail', kwargs={'pk': self.object.selection_id})


class PlayerCreate(CreateView):
    model = Player
    form_class = PlayerCreateForm
    # Asegúrate de tener la plantilla adecuada
    template_name = 'album/player_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pasa el ID de la selección al contexto
        context['selection_id'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
        # Establece el ID de la selección
        form.instance.selection_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('selection-detail', kwargs={'pk': self.kwargs['pk']})


class PlayerDelete(DeleteView):
    model = Player
    # Asegúrate de tener la plantilla adecuada
    template_name = 'album/player_confirm_delete.html'

    def get_success_url(self):
        # Cambia 'team-detail' por el nombre de la vista de detalles del equipo
        return reverse_lazy('selection-detail', kwargs={'pk': self.object.selection.id})
