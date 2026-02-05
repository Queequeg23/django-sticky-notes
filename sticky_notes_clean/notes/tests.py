from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ValidationError
from .models import Note
from .forms import NoteForm


class NoteModelTests(TestCase):

    # Set up a dummy sticky-note
    def setUp(self):
        self.note = Note.objects.create(
            title="Test note 1",
            content="Initial content",
        )

    def test_create_note(self):
        note = Note.objects.create(
            title="Test note 2",
            content="Some content"
        )
        # Check two note objects now exist
        self.assertEqual(Note.objects.count(), 2)
        # Check the note object just created has the correct title
        self.assertEqual(note.title, "Test note 2")

    def test_create_note_missing_title(self):
        with self.assertRaises(ValidationError):
            note = Note(title='', content="More content")
            # Checks field requirements raises validation error if not met
            note.full_clean()

    def test_create_note_with_too_long_title(self):
        long_title = "x" * 256  # Exceeds max_length=255
        with self.assertRaises(ValidationError):
            note = Note(title=long_title, content="More content")
            # Checks max_length constraint raises validation error
            note.full_clean()

    def test_timestamps_are_set(self):
        note = Note.objects.create(title="Test", content="Some content")
        self.assertIsNotNone(note.created_at)
        self.assertIsNotNone(note.updated_at)

    def test_created_at_timestamp_immutable(self):
        # create initial note
        note = Note.objects.create(
            title="Test note", content="Initial content"
        )
        initial_timestamp = note.created_at
        # update content
        note.content = "New content"
        note.save()  # Save updated note
        note.refresh_from_db()  # Ensure note has saved DB attributes
        # test timestamps correct
        self.assertEqual(note.created_at, initial_timestamp)
        self.assertNotEqual(note.updated_at, initial_timestamp)


class NoteViewTests(TestCase):

    def test_create_note_GET(self):
        #  Simulate browser GET request
        response = self.client.get(reverse('note_create'))
        # Check response code is 200 i.e. page load successful
        self.assertEqual(response.status_code, 200)
        # Check HTTP response object is an object of NoteForm class
        self.assertIsInstance(response.context['form'], NoteForm)

    def test_create_note_POST_valid(self):
        # Simulate browser POST request
        response = self.client.post(reverse('note_create'), {
            'title': 'New Note',
            'content': 'New Content'
        })
        # Checks one Note object created
        self.assertEqual(Note.objects.count(), 1)
        # Checks if response is redirecting to expected URL
        self.assertRedirects(response, reverse('note_list'))

    def test_create_note_POST_invalid(self):
        # Attempts to post an invalid note i.e. title blank
        response = self.client.post(reverse('note_create'), {
            'title': '',
            'content': 'Content'
        })
        # Check form displayed (200), form redisplayed
        self.assertEqual(response.status_code, 200)
        # Check form object has expected contents
        self.assertFormError(
            response.context['form'], 'title', 'This field is required.'
        )
        # Check no note object created
        self.assertEqual(Note.objects.count(), 0)
