from django.test import TestCase, Client
from django.contrib.auth.models import User
from todo.models import ToDo


class TestGetToDoDetauil(TestCase):
    # テスト実行時に毎回実行されるセットアップメソッド
    def setUp(self):
        print("setup")
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.todo = ToDo.objects.create(title="test01", is_completed=False)
        self.todo = ToDo.objects.create(title="test02", is_completed=True)
        # テスト用にhttpリクエストを送るためのクライアントを作成
        self.client = Client()

    def test_get_todo_detail(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get("/todo/1")

        self.assertEqual(response.status_code, 200)
        self.assertIn("application/json", response["Content-Type"])
        self.assertEquals(response.json().get("todo").get("id"), 1)
        self.assertEquals(response.json().get("todo").get("title"), "test01")
        self.assertEquals(response.json().get("todo").get("is_completed"), False)
