from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .tasks import send_test_email_task


class SendTestEmailView(APIView):
  permission_classes = []

  def post(self, request):
    email = request.data.get("email")

    if not email:
      return Response({"error": "Email required"}, status=400)

    send_test_email_task.delay(email)

    return Response(
      {"message": "Email will be sent in background"},
      status=status.HTTP_200_OK
    )
