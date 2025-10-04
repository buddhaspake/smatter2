from pathlib import Path
from django.core.management.base import BaseCommand
from home.models import HomePage
from base.models.pages import PublicationsPage, TeamPage, GalleryPage
from base.models.snippets import NewsItem
from base.management.cmd_utils import read_ods

LEGACY_DATA_FPATH = "datasheets/legacy_data.ods"
HOMEPAGE_SHEET = "page_home"


def update_homepage(root_dir: str):
    df = read_ods(
        Path(root_dir) / LEGACY_DATA_FPATH,
        sheet_name=HOMEPAGE_SHEET,
    )
    row = df.iloc[0]
    homepage = HomePage.objects.all()[0]
    # Update params
    homepage.intent = row.intent
    homepage.methods = row.methods
    homepage.vision = row.vision
    # Update news items
    homepage.news.clear()
    for snippet in row.news.split(";"):
        news_objs = NewsItem.objects.filter(
            caption__startswith = snippet.strip()
        )
        if news_objs:
            homepage.news.append(("new", news_objs[0]))
    homepage.save()


class Command(BaseCommand):
    help = "Pre-load pages to blog"

    def add_arguments(self, parser):

        parser.add_argument(
            "root",
            help = "Root directory for legacy data",
            type = str,
        )

        parser.add_argument(
            "-c", "--clean",
            help = "Clean existing entries",
            action = "store_true",
        )

    def validate(self, **kwargs):
        if not Path(kwargs["root"]).is_dir():
            raise ValueError(f"Invalid root directory: {kwargs['root']}")

    def handle(self, *args, **kwargs):
        # Validate + read params
        self.validate(**kwargs)
        root_dir = kwargs["root"]
        clean = kwargs["clean"]
        # Clean existing objects if necessary
        if clean:
            print("Cleaning old page(s)...") # debug
        # Pre-load new objects
        print("Loading new page(s)...") # debug
        update_homepage(root_dir)

