from pathlib import Path
import pandas as pd
from django.core.management.base import BaseCommand
from base.models.snippets import Publication


PUBLICATIONS_FPATH = "datasheets/publications.csv"


def read_tsv(filepath: Path):
    df = pd.read_csv(
        filepath.resolve(),
        sep="\t",
        header=0
    )
    return df


def add_publications(root_dir: str):
    df = read_tsv(Path(root_dir) / PUBLICATIONS_FPATH)
    pub_objs = (
        Publication(
            topic = row.topic,
            authors = row.authors,
            citation = row.citation,
            year = row.year,
        )
        for row in df.itertuples()
    )
    Publication.objects.bulk_create(pub_objs)


class Command(BaseCommand):
    help = "Add curated data to blog"

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
            Publication.objects.all().delete()
        # Pre-load new objects
        add_publications(root_dir)

