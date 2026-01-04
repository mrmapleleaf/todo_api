from django.test import TestCase, Client
from django.contrib.auth.models import User
from todo.models import ToDo


class TestCreateToDo(TestCase):
    # テスト実行時に毎回実行されるセットアップメソッド
    def setUp(self):
        print("setup")
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.todo = ToDo.objects.create(title="test01", is_completed=False)
        self.todo = ToDo.objects.create(title="test02", is_completed=True)
        # テスト用にhttpリクエストを送るためのクライアントを作成
        self.client = Client()

    def test_create_todo(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            "/todo/create",
            {
                "title": "test03",
                "is_completed": False,
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("application/json", response["Content-Type"])
        self.assertEquals(response.json().get("id"), 3)
        self.assertEquals(response.json().get("message"), "ToDo created successfully")
