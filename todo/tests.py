from django.test import TestCase, Client
from django.contrib.auth.models import User
from todo.models import ToDo


# Create your tests here.
class ToDoApiTest(TestCase):
    # テスト実行時に毎回実行されるセットアップメソッド
    def setUp(self):
        print("setup")
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.todo = ToDo.objects.create(title="test01", is_completed=False)
        self.todo = ToDo.objects.create(title="test02", is_completed=True)
        # テスト用にhttpリクエストを送るためのクライアントを作成
        self.client = Client()

    # スネークケースにしないとテストとして認識されない
    def test_get_todo_list(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get("/todos/")

        self.assertEqual(response.status_code, 200)
        self.assertIn("application/json", response["Content-Type"])
        self.assertContains(response, "test01")
        self.assertContains(response, "test02")
