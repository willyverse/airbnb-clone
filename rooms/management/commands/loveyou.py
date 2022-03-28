from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "This command tells you that I love you!"

    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How many times do you want me to tell you that I love you?",
        )

    def handle(self, *args, **options):
        times = options.get("times")
        for time in range(0, int(times)):
            self.stdout.write(self.style.ERROR("I love you"))
