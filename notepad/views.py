# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from .models import Notepad
from .serializers import NotepadsSerializer


class NotepadView(
    APIView,  # Basic View class provided by the Django Rest Framework
    UpdateModelMixin,  # Mixin that allows the basic APIView to handle PUT HTTP requests
    DestroyModelMixin,  # Mixin that allows the basic APIView to handle DELETE HTTP requests
):

    def get(self, request, id=None):
        if id:
            # If an id is provided in the GET request, retrieve the Notepad item by that id
            try:
                # Check if the notepad item the user wants to get exists
                queryset = Notepad.objects.get(id=id)
            except Notepad.DoesNotExist:
                # If the notepad item does not exist, return an error response
                return Response({'errors': 'This notepad item does not exist.'}, status=400)

            # Serialize notepad item from Django queryset object to JSON formatted data
            read_serializer = NotepadsSerializer(queryset)

        else:
            # Get all notepad items from the database using Django's model ORM
            queryset = Notepad.objects.all()

            # Serialize list of notepads item from Django queryset object to JSON formatted data
            read_serializer = NotepadsSerializer(queryset, many=True)

        # Return a HTTP response object with the list of notepad items as JSON
        return Response(read_serializer.data)

    def post(self, request):
        # Pass JSON data from user POST request to serializer for validation
        create_serializer = NotepadsSerializer(data=request.data)

        # Check if user POST data passes validation checks from serializer
        if create_serializer.is_valid():
            # If user data is valid, create a new notepad item record in the database
            notepad_item_object = create_serializer.save()

            # Serialize the new notepad item from a Python object to JSON format
            read_serializer = NotepadsSerializer(notepad_item_object)

            # Return a HTTP response with the newly created notepad item data
            return Response(read_serializer.data, status=201)

        # If the users POST data is not valid, return a 400 response with an error message
        return Response(create_serializer.errors, status=400)

    def put(self, request, id=None):
        try:
            # Check if the todo item the user wants to update exists
            notepad_item = Notepad.objects.get(id=id)
        except Notepad.DoesNotExist:
            # If the notepad item does not exist, return an error response
            return Response({'errors': 'This notepad item does not exist.'}, status=400)

        # If the notepad item does exists, use the serializer to validate the updated data
        update_serializer = NotepadsSerializer(notepad_item, data=request.data)

        # If the data to update the notepad item is valid, proceed to saving data to the database
        if update_serializer.is_valid():
            # Data was valid, update the notepad item in the database
            notepad_item_object = update_serializer.save()

            # Serialize the notepad item from Python object to JSON format
            read_serializer = NotepadsSerializer(notepad_item_object)

            # Return a HTTP response with the newly updated notepad item
            return Response(read_serializer.data, status=200)

        # If the update data is not valid, return an error response
        return Response(update_serializer.errors, status=400)

    def delete(self, request, id=None):
        try:
            # Check if the notepad item the user wants to delete exists
            notepad_item = Notepad.objects.get(id=id)
        except Notepad.DoesNotExist:
            # If the notepad item does not exist, return an error response
            return Response({'errors': 'This notepad item does not exist.'}, status=400)

        # Delete the chosen notepad item from the database
        notepad_item.delete()

        # Return a HTTP response notifying that the notepad item was successfully deleted
        return Response(status=204)
