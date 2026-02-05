from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm


def note_list(request):
    '''
    Lists all notes for user
    Queries database for all notes
    :param request: HTTP request object.
    :return: Rendered template with a list of posts.
    '''
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})


def note_detail(request, pk):
    '''
    Show a single note
    Gets one Note by primary key (pk) or returns a 404 if it doesn't exist.
    :param request: HTTP request object.
    :param pk: Primary key of the post.
    :return: Rendered template with details of the specified post.
    '''
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})


def note_create(request):
    '''
    Create a new note
    :param request: HTTP request object.
    :return: Rendered template for creating a new post.
    '''
    if request.method == 'POST':
        form = NoteForm(request.POST)
        # Check this line why commit=False?? Also why slip from note to form?
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})


def note_update(request, pk):
    '''
    View to update an existing post.
    :param request: HTTP request object.
    :param pk: Primary key of the post to be updated.
    :return: Rendered template for updating the specified post.
    '''
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})


def note_delete(request, pk):
    '''
    View to delete an existing post.
    :param request: HTTP request object.
    :param pk: Primary key of the post to be deleted.
    :return: Redirect to the post list after deletion.
    '''
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})
