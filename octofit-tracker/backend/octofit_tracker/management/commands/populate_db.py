from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', members=['Iron Man', 'Captain America', 'Thor', 'Hulk'])
        dc = Team.objects.create(name='DC', members=['Superman', 'Batman', 'Wonder Woman', 'Flash'])

        # Create users
        users = [
            User(email='ironman@marvel.com', name='Tony Stark', superhero='Iron Man', team='Marvel'),
            User(email='cap@marvel.com', name='Steve Rogers', superhero='Captain America', team='Marvel'),
            User(email='thor@marvel.com', name='Thor Odinson', superhero='Thor', team='Marvel'),
            User(email='hulk@marvel.com', name='Bruce Banner', superhero='Hulk', team='Marvel'),
            User(email='superman@dc.com', name='Clark Kent', superhero='Superman', team='DC'),
            User(email='batman@dc.com', name='Bruce Wayne', superhero='Batman', team='DC'),
            User(email='wonderwoman@dc.com', name='Diana Prince', superhero='Wonder Woman', team='DC'),
            User(email='flash@dc.com', name='Barry Allen', superhero='Flash', team='DC'),
        ]
        User.objects.bulk_create(users)

        # Create activities
        activities = [
            Activity(user='Iron Man', activity_type='Running', duration=30, date='2024-02-01'),
            Activity(user='Superman', activity_type='Flying', duration=60, date='2024-02-02'),
            Activity(user='Batman', activity_type='Martial Arts', duration=45, date='2024-02-03'),
            Activity(user='Thor', activity_type='Weightlifting', duration=50, date='2024-02-04'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=120)
        Leaderboard.objects.create(team='DC', points=110)

        # Create workouts
        workouts = [
            Workout(name='Super Strength', description='Strength training for superheroes.', suggested_for='Hulk, Superman'),
            Workout(name='Speed Run', description='Running workout for speedsters.', suggested_for='Flash, Quicksilver'),
            Workout(name='Flight Training', description='Aerobic workout for flyers.', suggested_for='Iron Man, Superman'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
