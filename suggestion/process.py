import random
from django.db.models import Max
from suggestion.models import SuggestionEvent


class SuggestionProcess:
    def get_random_event(self):
        max_id = SuggestionEvent.objects.all().aggregate(max_id=Max("id"))['max_id']
        while True:
            pk = random.randint(1, max_id)
            event = SuggestionEvent.objects.filter(pk=pk).first()
            if event:
                return event

