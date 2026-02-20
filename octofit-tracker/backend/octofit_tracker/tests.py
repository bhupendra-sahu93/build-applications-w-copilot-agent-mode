from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@example.com', name='Test User', superhero='Batman', team='Alpha')
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Alpha', members=['test@example.com'])
        self.assertEqual(team.name, 'Alpha')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user='test@example.com', activity_type='run', duration=30, date='2024-01-01')
        self.assertEqual(activity.activity_type, 'run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team='Alpha', points=100)
        self.assertEqual(leaderboard.team, 'Alpha')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='Batman')
        self.assertEqual(workout.name, 'Pushups')
