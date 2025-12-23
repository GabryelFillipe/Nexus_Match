from rest_framework.renderers import JSONRenderer

class NexusRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
     
        status_code = renderer_context['response'].status_code
        if status_code >= 400:
            return super().render(data, accepted_media_type, renderer_context)

        response_data = {
            "api_info": {
                "developer": "Gabryel Fillipe",
                "status": "Online",
                "version": "1.0",
                "project": "NexusMatch"
            },
            "count": len(data) if isinstance(data, list) else 1,
            "results": data
        }

        return super().render(response_data, accepted_media_type, renderer_context)