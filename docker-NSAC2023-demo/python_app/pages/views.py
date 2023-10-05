from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializer import PageSerializer
from .models import Page, Content

# Create your views here.


class PageView(viewsets.ModelViewSet):
    serializer_class = PageSerializer
    queryset = Page.objects.all()

    @action(detail=False, methods=["GET"])
    def get_by_code(self, request, code=None):
        try:
            page = Page.objects.get(code=code)
            content = Content.objects.filter(page=page)

            # Obtener el tipo de contenido para cada contenido y
            # agregarlo al resultado.
            content_data = []
            for item in content:
                content_type = item.content_type
                content_data.append({
                    "id": item.id,
                    "title": item.title,
                    "description": item.description,
                    "imageUrl": item.image_url,
                    "videoUrl": item.video_url,
                    "theme": item.theme,
                    "createAt": item.create_at,
                    "contentType": {
                        "id": content_type.id,
                        "code": content_type.code,
                        "name": content_type.name,
                    }
                })

            # Combinar la información de Page y sus Content en una respuesta
            response_data = {
                "id": page.id,
                "title": page.title,
                "code": page.code,
                "nameTab": page.name_tab,
                "createAt": page.create_at,
                "contents": content_data,
            }
            return Response(response_data)
        except Page.DoesNotExist:
            return Response({"error": "Contenido de página no encontrado"},
                            status=status.HTTP_404_NOT_FOUND)
