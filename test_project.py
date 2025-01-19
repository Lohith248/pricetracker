import pytest
from project import get_price, send_email, track_price

def test_get_price(monkeypatch):
    class MockResponse:
        @property
        def content(self):
            return '''
            <html>
                <body>
                    <span class="a-price-whole">1,499</span>
                </body>
            </html>
            '''
    def mock_get(*args, **kwargs):
        return MockResponse()
    monkeypatch.setattr('requests.get', mock_get)
    assert get_price("mock_url") == 1499.0

def test_send_email(monkeypatch):
    def mock_smtp(*args, **kwargs):
        class MockSMTP:
            def login(self, *args, **kwargs):
                pass
            def sendmail(self, *args, **kwargs):
                pass
            def quit(self):
                pass
        return MockSMTP()
    monkeypatch.setattr('smtplib.SMTP_SSL', mock_smtp)
    send_email("Test Subject", "Test Body", "test@example.com")

def test_track_price(monkeypatch):
    def mock_get_price(url):
        return 1499.0
    def mock_send_email(subject, body, to_email):
        assert subject == "Price Alert"
        assert "1499.0" in body
        assert to_email == "recipient@example.com"
    monkeypatch.setattr('project.get_price', mock_get_price)
    monkeypatch.setattr('project.send_email', mock_send_email)
    track_price("mock_url", 1500.0, "recipient@example.com")