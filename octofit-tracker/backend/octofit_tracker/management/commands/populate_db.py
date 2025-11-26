from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with initial data for OctoFit Tracker'

    def handle(self, *args, **options):
        # Example data
        users = [
            {'username': 'alice', 'email': 'alice@example.com', 'team': 'Team Alpha'},
            {'username': 'bob', 'email': 'bob@example.com', 'team': 'Team Beta'},
        ]
        teams = [
            {'name': 'Team Alpha', 'members': ['alice']},
            {'name': 'Team Beta', 'members': ['bob']},
        ]
        activities = [
            {'user': 'alice', 'type': 'run', 'duration': 30, 'calories': 250, 'date': '2025-11-26'},
            {'user': 'bob', 'type': 'cycle', 'duration': 45, 'calories': 400, 'date': '2025-11-26'},
        ]
        leaderboard = [
            {'team': 'Team Alpha', 'points': 100},
            {'team': 'Team Beta', 'points': 80},
        ]
        workouts = [
            {'name': 'Pushups', 'description': 'Do 20 pushups', 'difficulty': 'Easy'},
            {'name': 'Sprints', 'description': 'Run 5 sprints', 'difficulty': 'Medium'},
        ]

        for u in users:
            User.objects.get_or_create(**u)
        for t in teams:
            Team.objects.get_or_create(**t)
        for a in activities:
            Activity.objects.get_or_create(**a)
        for l in leaderboard:
            Leaderboard.objects.get_or_create(**l)
        for w in workouts:
            Workout.objects.get_or_create(**w)

        self.stdout.write(self.style.SUCCESS('Database populated with initial data.'))
