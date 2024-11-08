from urllib import response
import pytest

from django.urls import reverse

@pytest.mark.django_db
def test_post_view(client):
    url = reverse('home')
    responde = client.get(url)
    assert response.status.code == 200
    assert response.content == 'Hello World'